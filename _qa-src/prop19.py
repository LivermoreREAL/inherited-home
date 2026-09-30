# Builds the Prop 19 calculator page at /prop19-calculator/ (plus the short link /prop19/).
# Called from build.py with that module's globals, so it shares the site header, footer, and analytics.
# Rules: California State Board of Equalization, https://www.boe.ca.gov/prop19/ (checked Sept 2026).
# Rates: each county's official 2025-26 rate book (see RATE_SOURCES). Update both yearly.
import json, os

URL_PATH = "prop19-calculator/"
SHORT_PATH = "prop19/"

# Parent-child exclusion amount by date of transfer (BOE, adjusted every two years)
LIMITS = [("2025", "Feb 16, 2025 to Feb 15, 2027", 1044586),
          ("2023", "Feb 16, 2023 to Feb 15, 2025", 1022600),
          ("2021", "Feb 16, 2021 to Feb 15, 2023", 1000000)]

# Typical 2025-26 ad valorem rate (1% base + voter-approved bonds) for the main tax rate areas in each city.
AREAS = [
  ("Alameda County", [("Dublin", 1.238), ("Fremont", 1.174), ("Livermore", 1.133), ("Newark", 1.149),
                      ("Pleasanton", 1.169), ("San Leandro", 1.244), ("Union City", 1.262), ("Other Alameda County", 1.174)]),
  ("Contra Costa County", [("Danville", 1.083), ("San Ramon", 1.083), ("Other Contra Costa County", 1.102)]),
  ("San Joaquin County", [("Lathrop", 1.110), ("Manteca", 1.110), ("Mountain House", 1.062), ("Stockton (Stockton Unified)", 1.215),
                          ("Stockton (Lincoln Unified)", 1.092), ("Tracy", 1.148), ("Other San Joaquin County", 1.110)]),
]
DEFAULT_AREA = "Livermore"
RATE_SOURCES = [
  ("Alameda County Auditor-Controller, Property Tax Rates 2025", "https://data.acgov.org/datasets/8a6a0187bf3148b5a180c4bf6aad8f01_0/about"),
  ("Contra Costa County, Detail of Tax Rates 2025-2026", "https://www.contracosta.ca.gov/DocumentCenter/View/89669/Detail-of-Tax-Rates-2025-2026-PDF"),
  ("San Joaquin County Auditor-Controller, 2025-26 Property Tax Rates", "https://www.sjgov.org/docs/default-source/auditor-controller-documents/property-tax/assessed-values-and-tax-rates/2025-2026/2025-26-property-tax-rates.pdf"),
]
BOE = "https://www.boe.ca.gov/prop19/"

FAQ = [
  ("How much is the Prop 19 inheritance exclusion in 2026?",
   "For transfers from February 16, 2025 to February 15, 2027, a child who moves into a parent's home can keep the parent's taxable value on up to $1,044,586 of added market value. The amount started at $1,000,000 in 2021 and is adjusted every two years."),
  ("Do I keep my parent's property tax bill if I inherit the house?",
   "Only if the home was your parent's primary residence, you make it your own primary residence within one year, and you file for the homeowners' exemption. Even then, if the home is worth more than your parent's taxable value plus $1,044,586, the amount above that is added to your assessed value."),
  ("What happens if I inherit the house and rent it out or keep it empty?",
   "The home is reassessed at its current market value, the same as if it had been sold. For many East Bay families, that means a property tax bill several times higher than what the parent paid."),
  ("How does the Prop 19 transfer work for homeowners 55 or older?",
   "You can sell your primary home and move your taxable value to a replacement home anywhere in California, bought within two years before or after the sale, up to three times. If the new home costs more than your old home's sale price (with a 5% allowance in the first year after the sale and 10% in the second), the difference is added to your taxable value."),
  ("What property tax rate should I use?",
   "Use the total rate on your property tax bill: the 1% base plus voter-approved bonds for your tax rate area. Typical 2025-26 rates are about 1.13% in Livermore, 1.17% in Pleasanton, 1.24% in Dublin, 1.08% in San Ramon and Danville, and 1.15% in Tracy. Fixed charges, parcel taxes, and Mello-Roos are billed separately."),
  ("What do I need to file, and when?",
   "For an inherited home, file the homeowners' exemption within one year and form BOE-19-P (parent to child) or BOE-19-G (grandparent to grandchild) with the county assessor within three years, or before the home is sold, whichever comes first. For a move at 55 or older, file BOE-19-B within three years of buying the replacement home."),
]

def _money(n):
    return "${:,.0f}".format(n)

def build_prop19(g):
    SITE, BASE, UPDATED, UPDATED_ISO = g["SITE"], g["BASE"], g["UPDATED"], g["UPDATED_ISO"]
    esc, head, cta, foot, byline, PERSON, SMS = g["esc"], g["head"], g["cta"], g["foot"], g["byline"], g["PERSON"], g["SMS"]
    url = SITE + URL_PATH
    rel = "/what-happens-to-the-house/"
    rates = {name: r for _, cities in AREAS for name, r in cities}

    # Worked examples, computed here so the page text always matches the calculator's math.
    ex_rate = rates[DEFAULT_AREA] / 100
    ex_parent, ex_market, ex_limit = 150000, 1300000, LIMITS[0][2]
    ex_new = ex_parent if ex_market <= ex_parent + ex_limit else ex_market - ex_limit
    ex_tax_in, ex_tax_out = round((ex_new - 7000) * ex_rate), round(ex_market * ex_rate)
    # BOE's own 55+ example: sold for $400,000 with a $100,000 taxable value, bought for $600,000 in the first year after
    b_new = 100000 + (600000 - 400000 * 1.05)

    options = ""
    for county, cities in AREAS:
        options += f'<optgroup label="{esc(county)}">' + "".join(
            f'<option value="{r}" data-county="{esc(county)}"{" selected" if name == DEFAULT_AREA else ""}>{esc(name)} (about {r:.2f}%)</option>' for name, r in cities) + "</optgroup>"
    options += '<optgroup label="Somewhere else"><option value="custom">Not listed? Enter my own rate</option></optgroup>'
    short_label = {"2025": "2/16/25 to 2/15/27", "2023": "2/16/23 to 2/15/25", "2021": "2/16/21 to 2/15/23"}
    limit_opts = "".join(f'<option value="{v}">{short_label[k]} ({_money(v)})</option>' for k, _, v in LIMITS) + '<option value="old">Before 2/16/2021 (older rules)</option>'
    rate_rows = "".join(f"<tr><td>{esc(name)}</td><td>{esc(county.replace(' County',''))}</td><td>{r:.2f}%</td></tr>" for county, cities in AREAS for name, r in cities)
    sources = "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for t, u in RATE_SOURCES)
    faq_html = "".join(f'<div><dt>{esc(q)}</dt><dd>{esc(a)}</dd></div>' for q, a in FAQ)

    title = "Prop 19 Calculator (2026): Inherited Homes and 55+ Moves | Alameda, Contra Costa, San Joaquin"
    desc = ("Free Prop 19 property tax calculator for California. See what happens to the tax bill when you inherit a parent's home "
            "(2026 limit: $1,044,586) or move at 55 or older. Uses 2025-26 rates for Alameda, Contra Costa, and San Joaquin counties.")
    counties = [{"@type": "AdministrativeArea", "name": c + ", California"} for c, _ in AREAS]
    graph = [
      {"@type": "WebApplication", "@id": url + "#app", "name": "Prop 19 Calculator", "url": url,
       "applicationCategory": "FinanceApplication", "operatingSystem": "Any (runs in a web browser)", "browserRequirements": "Requires JavaScript",
       "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
       "description": "Estimates California property taxes under Proposition 19 for an inherited parent's home (parent-child exclusion) and for homeowners 55 or older moving their taxable value to a replacement home.",
       "featureList": ["Parent-child exclusion with the $1,044,586 limit (2025-2027)", "Age 55+ base year value transfer with 100%, 105%, and 110% rules",
                       "2025-26 tax rates by city for Alameda, Contra Costa, and San Joaquin counties", "Runs entirely in the browser; numbers are not sent anywhere"],
       "areaServed": counties, "author": {"@id": SITE + "#sam"}, "inLanguage": "en-US", "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO},
      {"@type": "WebPage", "@id": url + "#page", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE + "#website"},
       "mainEntity": {"@id": url + "#app"}, "author": {"@id": SITE + "#sam"}, "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO,
       "primaryImageOfPage": BASE + "assets/og-prop19.jpg", "citation": [BOE] + [u for _, u in RATE_SOURCES]},
      PERSON,
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
      {"@type": "Dataset", "name": "Typical 2025-26 property tax rates by city: Alameda, Contra Costa, and San Joaquin counties",
       "description": "Typical total ad valorem property tax rate (1% base plus voter-approved bonds) for the main tax rate areas in each city, taken from each county's official 2025-26 rate book.",
       "temporalCoverage": "2025/2026", "spatialCoverage": counties, "creator": {"@id": SITE + "#sam"}, "isBasedOn": [u for _, u in RATE_SOURCES],
       "variableMeasured": "Property tax rate (percent of assessed value)", "url": url + "#rates", "license": "https://creativecommons.org/licenses/by/4.0/"},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "What Happens to the House?", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "Prop 19 Calculator", "item": url}]},
    ]
    out = head(title, desc, url, rel, "website", {"@context": "https://schema.org", "@graph": graph}, og=BASE + "assets/og-prop19.jpg")
    out = out.replace("</head>", CALC_CSS + "\n</head>", 1)
    out += f"""<main class="wrap">
  <nav class="crumb"><a href="{rel}">Guide home</a> &rsaquo; Tools</nav>
  <h1 class="sf">Prop 19 Calculator</h1>
  <p class="lede">See what happens to the property tax bill when you inherit a parent's home, or when you move at 55 or older. Built for Alameda, Contra Costa, and San Joaquin counties.</p>
  {byline(rel)}
  <div class="short"><div class="k">Quick facts for 2026</div>
    <ul class="dots">
      <li><b>Inheriting a parent's home:</b> a child keeps the parent's tax base only by moving in within one year, and only up to the parent's taxable value plus {_money(LIMITS[0][2])} (transfers {LIMITS[0][1]}).</li>
      <li><b>Moving at 55 or older:</b> you can take your tax base to a new home anywhere in California, bought within two years of the sale, up to three times.</li>
      <li><b>Typical 2025-26 rates:</b> Livermore {rates['Livermore']:.2f}%, Pleasanton {rates['Pleasanton']:.2f}%, San Ramon {rates['San Ramon']:.2f}%, Tracy {rates['Tracy']:.2f}%.</li>
    </ul>
  </div>

  <section class="calc" id="calculator" aria-label="Prop 19 calculator">
    <div class="fld"><label for="c-area">Where is the home?</label>
      <select id="c-area">{options}</select>
      <span class="help">City not listed, or know your exact rate? Choose "Not listed? Enter my own rate" at the bottom of the list.</span>
      <div id="c-custom-wrap" class="custom" hidden><label for="c-custom">Your tax rate (%)</label><input id="c-custom" inputmode="decimal" placeholder="1.18"><span class="help">The total rate on your property tax bill, for example 1.18. It's usually a little over 1%.</span></div>
    </div>
    <div class="tabs" role="tablist">
      <button type="button" role="tab" id="t-inh" aria-selected="true" aria-controls="p-inh">Inheriting a parent's home</button>
      <button type="button" role="tab" id="t-mov" aria-selected="false" aria-controls="p-mov">Moving at 55 or older</button>
    </div>

    <div class="panel" id="p-inh" role="tabpanel" aria-labelledby="t-inh">
      <div class="grid">
        <div class="fld"><label for="i-taxable">Parent's assessed value</label><input id="i-taxable" inputmode="numeric" placeholder="$150,000"><span class="help">From the parent's tax bill: land plus improvements.</span></div>
        <div class="fld"><label for="i-market">Home's market value today</label><input id="i-market" inputmode="numeric" placeholder="$1,300,000"><span class="help">A recent estimate or appraisal.</span></div>
        <div class="fld"><label for="i-limit">Date of transfer (usually the date of death)</label><select id="i-limit">{limit_opts}</select></div>
        <div class="fld"><label for="i-primary">Was it your parent's primary home?</label><select id="i-primary"><option value="yes">Yes</option><option value="no">No (rental or second home)</option></select></div>
      </div>
      <div class="res" id="r-inh" aria-live="polite"></div>
    </div>

    <div class="panel" id="p-mov" role="tabpanel" aria-labelledby="t-mov" hidden>
      <div class="grid">
        <div class="fld"><label for="m-taxable">Current home's assessed value</label><input id="m-taxable" inputmode="numeric" placeholder="$300,000"><span class="help">From your property tax bill.</span></div>
        <div class="fld"><label for="m-sale">Sale price of current home</label><input id="m-sale" inputmode="numeric" placeholder="$1,000,000"></div>
        <div class="fld"><label for="m-new">Purchase price of new home</label><input id="m-new" inputmode="numeric" placeholder="$1,100,000"></div>
        <div class="fld"><label for="m-when">When is the new home bought?</label><select id="m-when"><option value="1.05">Within 1 year after selling</option><option value="1.10">In the 2nd year after selling</option><option value="1">Before selling the current home</option></select></div>
      </div>
      <p class="help">For homeowners 55 or older, severely disabled homeowners, and wildfire or disaster victims. The new home must be your primary residence.</p>
      <div class="res" id="r-mov" aria-live="polite"></div>
    </div>

    <p class="ratenote" id="c-ratenote"></p>
    <div class="actions"><a class="b1" href="{SMS}">Text Me to Go Over Your Numbers</a><a class="b2" href="/">Get the Free Guide</a></div>
    <p class="priv">Your numbers stay on your device. Nothing you type here is saved or sent anywhere.</p>
  </section>

  <article>
    <h2>How the inherited home calculation works</h2>
    <ol class="steps sm">
      <li>Start with your parent's current taxable value (the assessed value on the tax bill).</li>
      <li>Add the exclusion amount for the date of transfer: {_money(LIMITS[0][2])} for {LIMITS[0][1]}.</li>
      <li>If the home's market value is at or below that total, and a child moves in within a year, the child keeps the parent's taxable value.</li>
      <li>If the market value is higher, the amount above that total is added to the parent's taxable value.</li>
      <li>If no one moves in, the home is reassessed at full market value.</li>
    </ol>
    <div class="box"><p><b>Example ({DEFAULT_AREA}, {rates[DEFAULT_AREA]:.2f}%):</b> Your parent's assessed value is {_money(ex_parent)} and the home is worth {_money(ex_market)}. {_money(ex_parent)} plus {_money(ex_limit)} is {_money(ex_parent + ex_limit)}, so {_money(ex_market - ex_parent - ex_limit)} is added, for a new assessed value of {_money(ex_new)}. If a child moves in, the yearly tax is about {_money(ex_tax_in)} (after the $7,000 homeowners' exemption). If no one moves in, it's about {_money(ex_tax_out)}. That's a difference of about {_money(ex_tax_out - ex_tax_in)} a year.</p></div>

    <h2>How the move at 55 or older works</h2>
    <p>You sell your primary home and buy or build a replacement anywhere in California, within two years before or after the sale. You can do this up to three times. The question is whether the new home counts as "equal or lesser value":</p>
    <table class="t">
      <tr><th>When the new home is bought</th><th>Counts as equal or lesser value if it costs no more than</th></tr>
      <tr><td>Before the old home sells</td><td>100% of the old home's sale price</td></tr>
      <tr><td>Within 1 year after the sale</td><td>105% of the old home's sale price</td></tr>
      <tr><td>In the 2nd year after the sale</td><td>110% of the old home's sale price</td></tr>
    </table>
    <p>If it does, your taxable value carries over unchanged. If the new home costs more, the difference is added to your taxable value.</p>
    <div class="box"><p><b>The Board of Equalization's own example:</b> A home sold for $400,000 with a taxable value of $100,000. A replacement is bought in the first year after the sale for $600,000. 105% of $400,000 is $420,000, so $180,000 is added, and the new taxable value is {_money(b_new)}.</p></div>

    <h2 id="rates">2025-26 property tax rates by city</h2>
    <p>These are typical total rates for the main tax rate areas in each city: the 1% base plus voter-approved bonds. Your exact rate is on your tax bill and can differ by neighborhood. Fixed charges, parcel taxes, and Mello-Roos (common in newer areas like Mountain House and Dougherty Valley) are billed on top.</p>
    <table class="t rates"><tr><th>City or area</th><th>County</th><th>Typical rate</th></tr>{rate_rows}</table>
    <p class="src">Sources:</p><ul class="srcs">{sources}</ul>

    <h2>What to file, and when</h2>
    <table class="t">
      <tr><th>Situation</th><th>What to file with the county assessor</th></tr>
      <tr><td>Inherited a parent's home</td><td>Homeowners' exemption within 1 year, and form BOE-19-P within 3 years or before the home is sold</td></tr>
      <tr><td>Inherited a grandparent's home</td><td>Form BOE-19-G (the grandchild's parent must have passed away)</td></tr>
      <tr><td>Moving at 55 or older</td><td>Form BOE-19-B within 3 years of buying the replacement home</td></tr>
      <tr><td>Severely disabled, or wildfire or disaster victim</td><td>Forms BOE-19-D and BOE-19-DC, or BOE-19-V</td></tr>
    </table>

    <h2>Frequently asked questions</h2>
    <dl class="pit">{faq_html}</dl>

    <p class="src">This calculator gives estimates only. It isn't tax or legal advice. Please confirm with the county assessor and a CPA. Rules from the <a href="{BOE}">California State Board of Equalization</a>, current as of {UPDATED}.</p>
  </article>

  <aside class="rel"><h2 class="sf">Related questions</h2>
    <a href="{rel}prop-19-inherited-home/">Does Prop 19 apply to an inherited home in California?</a>
    <a href="{rel}inherited-house-capital-gains/">Do you pay capital gains tax when you sell an inherited house?</a>
    <a href="{rel}inherited-house-first-30-days/">What should you do with an inherited house in the first 30 days?</a>
  </aside>
{cta(rel)}
</main>
{CALC_JS}
{foot(rel)}"""
    os.makedirs(os.path.join(g["SITE_ROOT"], URL_PATH), exist_ok=True)
    open(os.path.join(g["SITE_ROOT"], URL_PATH, "index.html"), "w").write(out)

    # Short, shareable link: youreastbay.com/prop19 sends visitors to the calculator.
    stub = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Prop 19 Calculator</title>
<link rel="canonical" href="{url}"><meta http-equiv="refresh" content="0; url=/{URL_PATH}">
<script>location.replace("/{URL_PATH}"+location.search+location.hash);</script></head>
<body><p><a href="/{URL_PATH}">Go to the Prop 19 Calculator</a></p></body></html>
"""
    os.makedirs(os.path.join(g["SITE_ROOT"], SHORT_PATH), exist_ok=True)
    open(os.path.join(g["SITE_ROOT"], SHORT_PATH, "index.html"), "w").write(stub)
    return url

CALC_CSS = """<style>
.calc{border:1px solid var(--ln);border-radius:16px;padding:22px 20px;margin:24px 0 30px;box-shadow:0 8px 30px rgba(0,29,73,.08);background:#fff}
.calc label{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);font-weight:700;margin-bottom:6px}
.calc input,.calc select{width:100%;padding:13px 14px;border:1px solid var(--ln);border-radius:10px;font:inherit;font-size:16px;color:var(--ink);background:#fff}
.calc input:focus,.calc select:focus{outline:none;border-color:var(--navy);box-shadow:0 0 0 3px rgba(180,139,27,.3)}
.calc .fld{margin-bottom:14px}
.calc .help{display:block;font-size:13px;color:var(--mut);margin-top:5px}
.calc .custom{margin-top:10px}
.tabs{display:grid;grid-template-columns:1fr 1fr;gap:6px;background:var(--cream);padding:5px;border-radius:12px;margin:6px 0 18px}
.tabs button{border:0;background:transparent;padding:12px 8px;border-radius:9px;font:inherit;font-weight:700;font-size:14.5px;color:var(--mut);cursor:pointer}
.tabs button[aria-selected=true]{background:var(--navy);color:#fff}
.grid{display:grid;grid-template-columns:1fr;gap:0 16px}
@media (min-width:640px){.grid{grid-template-columns:1fr 1fr}}
.res{margin-top:6px}
.res .two{display:grid;grid-template-columns:1fr;gap:12px}
@media (min-width:640px){.res .two{grid-template-columns:1fr 1fr}}
.res .card{border-radius:12px;padding:16px;border:1px solid var(--ln)}
.res .card.a{background:var(--cream);border-color:#ead9b0}
.res .card .s{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:6px}
.res .big{font-family:"Source Serif 4",Georgia,serif;font-size:30px;font-weight:700;color:var(--navy);line-height:1.1}
.res .sub{font-size:14px;color:#34405a;margin-top:4px}
.res .diff{margin-top:12px;background:var(--navy);color:#fff;border-radius:12px;padding:14px 16px;font-size:15.5px}
.res .diff b{color:var(--gold-lt);font-size:19px}
.res .why2{font-size:14px;color:#34405a;margin-top:10px}
.res .empty{color:var(--mut);font-size:15px;background:var(--cream);border-radius:12px;padding:14px 16px}
.ratenote{font-size:13px;color:var(--mut);margin:14px 0 0}
.actions{display:grid;grid-template-columns:1fr;gap:10px;margin-top:16px}
@media (min-width:640px){.actions{grid-template-columns:1fr 1fr}}
.actions a{display:block;text-align:center;padding:14px;border-radius:11px;font-weight:700;text-decoration:none;font-size:15.5px}
.actions .b1{background:var(--navy);color:#fff}
.actions .b2{border:1.5px solid var(--navy);color:var(--navy)}
.priv{font-size:12.5px;color:var(--mut);text-align:center;margin-top:10px}
.short ul.dots{margin:4px 0 0}
.short ul.dots li{font-size:15.5px;margin-bottom:6px}
table.rates td:last-child{font-variant-numeric:tabular-nums;font-weight:600;color:var(--navy);width:auto}
table.rates td:first-child{width:auto}
ul.srcs{font-size:13.5px;margin:4px 0 0 18px;color:var(--mut)}
ul.srcs li{margin-bottom:4px}
</style>"""

CALC_JS = """<script>
(function(){
  var $=function(id){return document.getElementById(id);};
  var num=function(el){var v=(el.value||'').replace(/[^0-9.]/g,'');return v?parseFloat(v):0;};
  var money=function(n){return '$'+Math.round(Math.max(0,n)).toLocaleString('en-US');};
  var HOE=7000, used={};
  function rate(){
    var sel=$('c-area'), custom=sel.value==='custom';
    $('c-custom-wrap').hidden=!custom;
    var r=custom?num($('c-custom')):parseFloat(sel.value);
    if(custom&&r>0&&r<0.5)r=r*100; // typed as a decimal, like 0.0118
    var label=custom?'your rate':sel.options[sel.selectedIndex].text.replace(/ \\(about.*\\)$/,'')+', 2025-26 typical rate';
    $('c-ratenote').textContent=(r?'Using '+r.toFixed(3).replace(/0$/,'')+'% ('+label+'). ':'')+'That covers the 1% base plus voter-approved bonds, not fixed charges, parcel taxes, or Mello-Roos.';
    return r/100;
  }
  function track(mode){
    if(used[mode]||!window.gtag)return; used[mode]=true;
    var sel=$('c-area'); gtag('event','calculator_use',{calculator:'prop19',mode:mode,area:sel.options[sel.selectedIndex].text.replace(/ \\(about.*\\)$/,'')});
  }
  function inherit(){
    var r=rate(), t=num($('i-taxable')), m=num($('i-market')), lim=$('i-limit').value, prim=$('i-primary').value==='yes', out=$('r-inh');
    if(!r){out.innerHTML='<div class="empty">Enter your tax rate above to see the estimate.</div>';return;}
    if(!t||!m){out.innerHTML='<div class="empty">Enter the assessed value and market value to see the estimate.</div>';return;}
    if(lim==='old'){out.innerHTML='<div class="empty">Transfers before February 16, 2021 fall under the older Prop 58 rules, which this calculator doesn\\'t cover. The county assessor can tell you how they apply.</div>';return;}
    var L=parseFloat(lim), newIn, why;
    if(!prim){newIn=m; why='The parent-child exclusion only applies to a parent\\'s primary home, so the home is reassessed at market value either way.';}
    else if(m<=t+L){newIn=t; why='The home\\'s value is within your parent\\'s taxable value plus '+money(L)+' ('+money(t+L)+'), so a child who moves in keeps the parent\\'s taxable value.';}
    else{newIn=m-L; why='Your parent\\'s taxable value plus '+money(L)+' is '+money(t+L)+'. The home is worth '+money(m-t-L)+' more than that, so that amount is added.';}
    var taxIn=(newIn-HOE)*r, taxOut=m*r;
    out.innerHTML='<div class="two"><div class="card a"><div class="s">If a child moves in within a year</div><div class="big">'+money(taxIn)+'<span class="sub"> / year</span></div><div class="sub">New assessed value: '+money(newIn)+'<br>About '+money(taxIn/12)+' a month</div></div>'+
      '<div class="card"><div class="s">If no one moves in</div><div class="big">'+money(taxOut)+'<span class="sub"> / year</span></div><div class="sub">Reassessed at market value: '+money(m)+'<br>About '+money(taxOut/12)+' a month</div></div></div>'+
      (prim&&taxOut>taxIn?'<div class="diff">Moving in saves about <b>'+money(taxOut-taxIn)+'</b> a year.</div>':'')+
      '<p class="why2">'+why+' Your parent paid about '+money((prim?t-HOE:t)*r)+' a year.</p>';
    track('inherit');
  }
  function move(){
    var r=rate(), t=num($('m-taxable')), s=num($('m-sale')), n=num($('m-new')), f=parseFloat($('m-when').value), out=$('r-mov');
    if(!r){out.innerHTML='<div class="empty">Enter your tax rate above to see the estimate.</div>';return;}
    if(!t||!s||!n){out.innerHTML='<div class="empty">Enter your assessed value, sale price, and new purchase price to see the estimate.</div>';return;}
    var adj=s*f, pct=Math.round(f*100), newV, why;
    if(n<=adj){newV=Math.min(t,n); why='The new home costs no more than '+pct+'% of your sale price ('+money(adj)+'), so your taxable value carries over.';}
    else{newV=t+(n-adj); why=pct+'% of your sale price is '+money(adj)+'. The new home costs '+money(n-adj)+' more, so that amount is added to your taxable value.';}
    var withP=(newV-HOE)*r, without=(n-HOE)*r;
    out.innerHTML='<div class="two"><div class="card a"><div class="s">With Prop 19</div><div class="big">'+money(withP)+'<span class="sub"> / year</span></div><div class="sub">New taxable value: '+money(newV)+'<br>About '+money(withP/12)+' a month</div></div>'+
      '<div class="card"><div class="s">Without Prop 19</div><div class="big">'+money(without)+'<span class="sub"> / year</span></div><div class="sub">Taxed on the purchase price: '+money(n)+'<br>About '+money(without/12)+' a month</div></div></div>'+
      (without>withP?'<div class="diff">Prop 19 saves about <b>'+money(without-withP)+'</b> a year.</div>':'')+
      '<p class="why2">'+why+' Both include the $7,000 homeowners\\' exemption.</p>';
    track('move');
  }
  function all(){inherit();move();}
  document.querySelectorAll('.calc input,.calc select').forEach(function(el){el.addEventListener('input',all);el.addEventListener('change',all);});
  document.querySelectorAll('.calc input[inputmode=numeric]').forEach(function(el){el.addEventListener('blur',function(){var v=num(el);el.value=v?money(v):'';});});
  function tab(which){
    var inh=which==='inh';
    $('t-inh').setAttribute('aria-selected',inh);$('t-mov').setAttribute('aria-selected',!inh);
    $('p-inh').hidden=!inh;$('p-mov').hidden=inh;
  }
  $('t-inh').addEventListener('click',function(){tab('inh');});
  $('t-mov').addEventListener('click',function(){tab('mov');});
  if(location.hash==='#move')tab('mov');
  all();
})();
</script>"""
