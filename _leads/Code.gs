/**
 * youreastbay.com lead catcher (Sam Yusufi)
 *
 * When the guide form on youreastbay.com is sent, this script:
 *   1. Adds a row to the "youreastbay.com Leads" Google Sheet (created automatically in the Drive of the account that deploys this).
 *   2. Emails Sam a notification. Reply goes straight to the visitor.
 *   3. Emails the visitor a short thank-you with the guide link.
 *
 * Deploy as a web app: Deploy > New deployment > Web app. Execute as: Me. Who has access: Anyone.
 * Then put the /exec URL into LEADS_ENDPOINT in _qa-src/site_schema.py, rebuild, and push.
 * Setup notes: _leads/README.md
 */

var CFG = {
  NOTIFY_TO: 'sam@samyusufi.com',
  SHEET_TITLE: 'youreastbay.com Leads',
  TAB: 'Leads',
  GUIDE_URL: 'https://youreastbay.com/What-Happens-to-the-House.pdf',
  SITE_URL: 'https://youreastbay.com/',
  MAIN_SITE_URL: 'https://samyusufi.com/',
  PHONE_DISPLAY: '925.425.8929',
  PHONE_TEL: '+19254258929',
  MIN_FILL_MS: 1200,     // forms sent faster than this are bots
  MAX_PER_HOUR: 40,      // safety valve against floods
  STATUSES: ['New', 'Contacted', 'Call scheduled', 'Listing conversation', 'Not a fit', 'Closed']
};
var HEADERS = ['Received', 'Name', 'Email', 'Phone', 'Property address', 'Role', 'Where things stand', 'Message', 'Page', 'Follow-up status', 'Notes'];

// ---------- web app entry points ----------

function doGet() {
  return reply_({ ok: true, service: 'youreastbay.com leads' });
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var p = (e && e.parameter) || {};
    if (p.hp_url) return reply_({ ok: true });                                   // hidden field: only bots fill it
    var fillMs = Number(p.t || 0);
    if (fillMs && fillMs < CFG.MIN_FILL_MS) return reply_({ ok: true });         // too fast to be a person
    var cache = CacheService.getScriptCache();
    var id = clean_(p.id, 64);
    if (id && cache.get('id:' + id)) return reply_({ ok: true, duplicate: true }); // the page may resend the same request

    var lead = {
      name: clean_(p.name, 120),
      email: clean_(p.email, 200),
      phone: clean_(p.phone, 40),
      address: clean_(p.property_address, 200),
      role: clean_(p.role, 120),
      stage: clean_(p.stage, 120),
      message: clean_(p.message, 3000),
      page: clean_(p.page, 200)
    };
    var problem = validate_(lead);
    if (problem) return reply_({ ok: false, error: problem });
    if (!underLimit_(cache)) return reply_({ ok: false, error: 'busy' });

    var sheet = sheet_();
    saveRow_(sheet, lead);
    if (id) cache.put('id:' + id, '1', 21600);

    try { notify_(lead, sheet.getParent().getUrl()); } catch (err1) { console.error('notify failed', err1); }
    try { thankYou_(lead, cache); } catch (err2) { console.error('thank-you failed', err2); }
    return reply_({ ok: true });
  } catch (err) {
    console.error(err);
    return reply_({ ok: false, error: 'server' });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

// ---------- helpers ----------

function reply_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

function clean_(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max);
}

function validate_(l) {
  if (!l.name) return 'name';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(l.email)) return 'email';
  var digits = l.phone.replace(/\D/g, '');
  if (digits.length < 10 || digits.length > 15) return 'phone';
  return '';
}

function underLimit_(cache) {
  var d = new Date();
  var key = 'rate:' + Utilities.formatDate(d, 'America/Los_Angeles', 'yyyyMMddHH');
  var n = Number(cache.get(key) || 0) + 1;
  cache.put(key, String(n), 3600);
  return n <= CFG.MAX_PER_HOUR;
}

// Stops spreadsheet formulas from running if someone types "=..." into the form.
function safe_(v) {
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function firstName_(name) {
  var f = String(name || '').trim().split(/\s+/)[0] || '';
  return f.length > 40 ? '' : f;
}

function esc_(s) {
  return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// ---------- the Google Sheet ----------

function sheet_() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty('SHEET_ID');
  var ss = null;
  if (id) { try { ss = SpreadsheetApp.openById(id); } catch (err) { ss = null; } }
  if (!ss) {
    ss = SpreadsheetApp.create(CFG.SHEET_TITLE);
    ss.setSpreadsheetTimeZone('America/Los_Angeles');
    props.setProperty('SHEET_ID', ss.getId());
  }
  var sh = ss.getSheetByName(CFG.TAB);
  if (!sh) { sh = ss.getSheets()[0]; sh.setName(CFG.TAB); }
  if (sh.getLastRow() === 0) formatSheet_(sh);
  return sh;
}

function formatSheet_(sh) {
  sh.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS])
    .setFontWeight('bold').setFontColor('#ffffff').setBackground('#001d49').setVerticalAlignment('middle');
  sh.setFrozenRows(1);
  var widths = [150, 160, 220, 130, 220, 200, 230, 340, 150, 150, 260];
  for (var i = 0; i < widths.length; i++) sh.setColumnWidth(i + 1, widths[i]);
  sh.getRange('B2:I2000').setNumberFormat('@');                       // keep names, phones, and addresses as plain text
  sh.getRange('A2:A2000').setNumberFormat('mmm d, yyyy h:mm AM/PM');
  sh.getRange('H2:H2000').setWrap(true);
  sh.getRange('A2:K2000').setVerticalAlignment('top');
  var status = SpreadsheetApp.newDataValidation().requireValueInList(CFG.STATUSES, true).setAllowInvalid(true).build();
  sh.getRange('J2:J2000').setDataValidation(status);
  var newRows = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied('=$J2="New"').setBackground('#fff4d6').setRanges([sh.getRange('A2:K2000')]).build();
  sh.setConditionalFormatRules([newRows]);
}

function saveRow_(sh, l) {
  sh.appendRow([new Date(), safe_(l.name), safe_(l.email), safe_(l.phone), safe_(l.address), safe_(l.role), safe_(l.stage), safe_(l.message), l.page, 'New', '']);
}

// ---------- email ----------

function notify_(l, sheetUrl) {
  var lines = [
    'Name: ' + l.name,
    'Phone: ' + l.phone,
    'Email: ' + l.email,
    'Property address: ' + (l.address || '(not given)'),
    'Role: ' + (l.role || '(not given)'),
    'Where things stand: ' + (l.stage || '(not given)'),
    '',
    'Message: ' + (l.message || '(none)'),
    '',
    'All leads: ' + sheetUrl,
    'Reply to this email to write to ' + (firstName_(l.name) || 'them') + ' directly.'
  ];
  var tel = 'tel:' + l.phone.replace(/[^\d+]/g, '');
  var html = '<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.55;color:#1d2433">' +
    '<p style="margin:0 0 10px"><b>New guide request from youreastbay.com</b></p>' +
    '<table style="border-collapse:collapse;font-size:15px">' + [
      ['Name', esc_(l.name)],
      ['Phone', '<a href="' + esc_(tel) + '">' + esc_(l.phone) + '</a>'],
      ['Email', '<a href="mailto:' + esc_(l.email) + '">' + esc_(l.email) + '</a>'],
      ['Property address', esc_(l.address || '(not given)')],
      ['Role', esc_(l.role || '(not given)')],
      ['Where things stand', esc_(l.stage || '(not given)')],
      ['Message', esc_(l.message || '(none)').replace(/\n/g, '<br>')]
    ].map(function (r) {
      return '<tr><td style="padding:4px 14px 4px 0;color:#5a6478;vertical-align:top">' + r[0] + '</td><td style="padding:4px 0">' + r[1] + '</td></tr>';
    }).join('') + '</table>' +
    '<p style="margin:14px 0 0"><a href="' + esc_(sheetUrl) + '">Open the leads sheet</a> &nbsp;|&nbsp; Reply to this email to write to them directly.</p></div>';
  MailApp.sendEmail({
    to: CFG.NOTIFY_TO,
    replyTo: l.email,
    name: 'youreastbay.com leads',
    subject: 'New guide request: ' + l.name + (l.role ? ' (' + l.role + ')' : ''),
    body: lines.join('\n'),
    htmlBody: html
  });
}

function thankYou_(l, cache) {
  var key = 'ar:' + l.email.toLowerCase();
  if (cache.get(key)) return;                    // one thank-you per address every few hours
  cache.put(key, '1', 21600);
  var first = firstName_(l.name);
  var hi = first ? 'Hi ' + first + ',' : 'Hi,';
  var text = [
    hi,
    '',
    'I appreciate you reaching out. Here is your free guide, What Happens to the House?',
    CFG.GUIDE_URL,
    '',
    "It covers who's in charge, what to do first, and how a probate or trust sale works. You don't have to read it all at once.",
    '',
    "If you'd like to talk it through, reply to this email, or call or text me at " + CFG.PHONE_DISPLAY + '.',
    '',
    'Sam Yusufi, Realtor®',
    'Certified Probate & Trust Specialist',
    'Legacy Real Estate & Associates | DRE# 02020587',
    CFG.PHONE_DISPLAY + ' | youreastbay.com | samyusufi.com',
    '',
    'General information about California law, not legal or tax advice.'
  ].join('\n');
  var html = '<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.55;color:#1d2433;max-width:560px">' +
    '<p>' + esc_(hi) + '</p>' +
    '<p>I appreciate you reaching out. Here is your free guide, <b>What Happens to the House?</b></p>' +
    '<p><a href="' + CFG.GUIDE_URL + '" style="display:inline-block;background:#b48b1b;color:#ffffff;text-decoration:none;font-weight:bold;padding:12px 20px;border-radius:8px">Download the Guide (PDF)</a></p>' +
    "<p>It covers who's in charge, what to do first, and how a probate or trust sale works. You don't have to read it all at once.</p>" +
    '<p>If you\'d like to talk it through, reply to this email, or call or text me at <a href="tel:' + CFG.PHONE_TEL + '">' + CFG.PHONE_DISPLAY + '</a>.</p>' +
    '<p style="margin-top:22px">Sam Yusufi, Realtor&reg;<br>Certified Probate &amp; Trust Specialist<br>Legacy Real Estate &amp; Associates | DRE# 02020587<br>' +
    CFG.PHONE_DISPLAY + ' | <a href="' + CFG.SITE_URL + '">youreastbay.com</a> | <a href="' + CFG.MAIN_SITE_URL + '">samyusufi.com</a></p>' +
    '<p style="font-size:12px;color:#6b7280">General information about California law, not legal or tax advice.</p></div>';
  MailApp.sendEmail({
    to: l.email,
    replyTo: CFG.NOTIFY_TO,
    name: 'Sam Yusufi',
    subject: 'Your free guide: What Happens to the House?',
    body: text,
    htmlBody: html
  });
}

// ---------- run these by hand from the editor ----------

/** Creates the Leads sheet (if needed) and shows its link in the log. Run once after pasting the script. */
function setup() {
  var sh = sheet_();
  Logger.log('Leads sheet: ' + sh.getParent().getUrl());
}

/** Sends one pretend lead through the whole path (row, notification, thank-you), using Sam's own address. */
function sendTest() {
  var out = doPost({ parameter: {
    name: 'Test Person', email: CFG.NOTIFY_TO, phone: '(925) 555-0100', property_address: '123 Test St, Livermore',
    role: "I'm an heir or beneficiary", stage: 'Probate has been opened', message: 'This is a test from sendTest().',
    page: '/', id: 'test-' + new Date().getTime(), t: '9000'
  } });
  Logger.log(out.getContent());
}
