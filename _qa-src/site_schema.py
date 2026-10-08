# Shared site identity for youreastbay.com, used by both builds
# (_qa-src/build.py for the question pages and _guide-src/build.py for the home page).
SITE = "https://youreastbay.com/"
SITE_NAME = "What Happens to the House?"  # the name Google shows above results; change here, then rebuild both
SITE_ALT_NAMES = ["Your East Bay", "youreastbay.com"]

ALAMEDA = {"@type": "AdministrativeArea", "name": "Alameda County, California"}
CONTRA_COSTA = {"@type": "AdministrativeArea", "name": "Contra Costa County, California"}
CITIES = [("Livermore", ALAMEDA), ("Pleasanton", ALAMEDA), ("Dublin", ALAMEDA), ("San Ramon", CONTRA_COSTA),
          ("Danville", CONTRA_COSTA), ("Fremont", ALAMEDA), ("Union City", ALAMEDA), ("Newark", ALAMEDA), ("San Leandro", ALAMEDA)]
AREAS = [ALAMEDA, CONTRA_COSTA] + [{"@type": "City", "name": c + ", California", "containedInPlace": county} for c, county in CITIES]
# One sentence used on the pages, in the footers, and in llms.txt
CITY_LIST = ", ".join(c for c, _ in CITIES[:-1]) + ", and " + CITIES[-1][0]
SERVING = f"Serving families in {CITY_LIST}, across Alameda and Contra Costa Counties."

PERSON = {
  "@type": "Person", "@id": SITE + "#sam", "name": "Sam Yusufi",
  "jobTitle": "Realtor, Associate Broker", "url": "https://samyusufi.com",
  "image": SITE + "what-happens-to-the-house/assets/headshot.jpg", "telephone": "+1-925-425-8929", "email": "sam@samyusufi.com",
  "worksFor": {"@type": "RealEstateAgent", "name": "Legacy Real Estate & Associates",
                "address": {"@type": "PostalAddress", "streetAddress": "1983 Second St", "addressLocality": "Livermore", "addressRegion": "CA", "postalCode": "94550", "addressCountry": "US"}},
  "hasCredential": [
    {"@type": "EducationalOccupationalCredential", "name": "Certified Probate & Trust Specialist (CPTS)", "credentialCategory": "certification"},
    {"@type": "EducationalOccupationalCredential", "name": "California Real Estate Broker License", "identifier": "DRE# 02020587", "credentialCategory": "license",
     "recognizedBy": {"@type": "GovernmentOrganization", "name": "California Department of Real Estate"}}],
  "areaServed": AREAS,
  "description": "Realtor and Associate Broker (DRE# 02020587) and Certified Probate & Trust Specialist at Legacy Real Estate & Associates in Livermore, California. More than 20 years of professional experience, including over a decade in real estate and property management. Helps East Bay families sell inherited homes in probate or a trust.",
  "knowsLanguage": ["English", "Persian", "Dari", "Hindi"],
  "memberOf": [{"@type": "Organization", "name": "Bay East Association of Realtors"}, {"@type": "Organization", "name": "Valley Real Estate Network"}, {"@type": "Organization", "name": "Real Estate Alliance of Livermore"}],
  "sameAs": ["https://www.instagram.com/samyusufi7/", "https://www.facebook.com/samyusufi7/", "https://www.facebook.com/samyusufibroker/", "https://www.linkedin.com/in/yusufi/"],
}

# Sam's social accounts: @samyusufi7 is the same handle on Instagram and Facebook; LinkedIn is her profile address.
SOCIAL_HANDLE = "@samyusufi7"
INSTAGRAM = "https://www.instagram.com/samyusufi7/"
FACEBOOK = "https://www.facebook.com/samyusufi7/"
LINKEDIN = "https://www.linkedin.com/in/yusufi/"
# Round icon buttons (Instagram, Facebook, LinkedIn) with the handle beside them; used on the About Sam contact card.
def social_icons():
    ig = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.5 3h9A4.5 4.5 0 0 1 21 7.5v9a4.5 4.5 0 0 1-4.5 4.5h-9A4.5 4.5 0 0 1 3 16.5v-9A4.5 4.5 0 0 1 7.5 3Zm0 2A2.5 2.5 0 0 0 5 7.5v9A2.5 2.5 0 0 0 7.5 19h9a2.5 2.5 0 0 0 2.5-2.5v-9A2.5 2.5 0 0 0 16.5 5h-9ZM12 7.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5Zm5-3.2a1.1 1.1 0 1 1 0 2.2 1.1 1.1 0 0 1 0-2.2Z"/></svg>'
    fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.8c0-.9.3-1.5 1.6-1.5h1.7V3.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4.1 1.5-4.1 4.2v2.3H7.5V13h2.8v8h3.2Z"/></svg>'
    li = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6.3" cy="6.4" r="1.9"/><rect x="4.6" y="9.2" width="3.4" height="10.2" rx=".4"/><path d="M10.2 9.2h3.2v1.4c.6-1 1.7-1.7 3.3-1.7 3 0 3.8 2 3.8 4.7v5.8h-3.4v-5.1c0-1.3-.1-2.6-1.6-2.6s-1.9 1.2-1.9 2.5v5.2h-3.4V9.2Z"/></svg>'
    a = lambda u, label, icon: f'<a class="si" href="{u}" target="_blank" rel="me noopener" aria-label="{label}">{icon}</a>'
    return (f'<div class="socials">{a(INSTAGRAM, "Instagram: " + SOCIAL_HANDLE, ig)}{a(FACEBOOK, "Facebook: " + SOCIAL_HANDLE, fb)}{a(LINKEDIN, "LinkedIn: Sam Yusufi", li)}'
            f'<a class="sh" href="{INSTAGRAM}" target="_blank" rel="me noopener">{SOCIAL_HANDLE}</a></div>')

def social_line(prefix="Follow along: "):
    a = lambda u, t: f'<a href="{u}" target="_blank" rel="me noopener">{t}</a>'
    return f'{prefix}{SOCIAL_HANDLE} on {a(INSTAGRAM, "Instagram")} and {a(FACEBOOK, "Facebook")}, or connect on {a(LINKEDIN, "LinkedIn")}.'

ICON_TAGS = '<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">'

# Google Analytics 4 (property "youreastbay.com" in the "Sam Yusufi Real Estate" account).
# Counts page views, plus these events: generate_lead (guide form sent), text_me (sms taps),
# call_click, email_click, guide_cta_click (a "Free guide" button that leads to the form), and guide_jump
# (the phone button that scrolls to the form), about_click (a link to the About Sam page), and social_click (Instagram, Facebook, or LinkedIn; says which). Each tap also says where on the page it happened (placement).
# No names, emails, phone numbers, or addresses are ever sent to Google.
GA_ID = "G-CXF6CNWM21"
ANALYTICS = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('js',new Date());gtag('config','{GA_ID}');
function pl(a){{var m=[['.cbar','sticky_bar'],['.meet','meet_sam'],['.top','header'],['.hero','hero'],['.hcta','cta_card'],['.ag','agent_card'],['.ft','footer'],['.fe','form_fallback'],['.db','thank_you'],['.bd','form'],['.cta','page_cta'],['.hp','help_box']];for(var i=0;i<m.length;i++){{if(a.closest(m[i][0]))return m[i][1];}}return 'other';}}
document.addEventListener('click',function(e){{
  var a=e.target.closest&&e.target.closest('a');if(!a)return;
  var h=a.getAttribute('href')||'',p={{link_location:location.pathname,placement:pl(a)}};
  var n=h.indexOf('sms:')===0?'text_me':h.indexOf('tel:')===0?'call_click':h.indexOf('mailto:')===0?'email_click':'';
  if(n){{
    // Texting, calling, and email apps take over the screen right away, which can cut off the
    // message to Google. Send it first (as a beacon), then open the app a moment later.
    e.preventDefault();
    var done=false,go=function(){{if(!done){{done=true;location.href=h;}}}};
    gtag('event',n,{{link_location:p.link_location,placement:p.placement,transport_type:'beacon',event_callback:go,event_timeout:600}});
    setTimeout(go,700);
  }}
  else if(h==='/'&&/free guide/i.test(a.textContent))gtag('event','guide_cta_click',p);
  else if(h==='#guide')gtag('event','guide_jump',p);
  else if(h==='/about-sam/')gtag('event','about_click',p);
  else if(/(instagram|facebook|linkedin)\\.com/.test(h))gtag('event','social_click',{{link_location:p.link_location,placement:p.placement,network:(h.match(/instagram|facebook|linkedin/)||[''])[0],transport_type:'beacon'}});
}});
</script>"""
PRIVACY_NOTE = "This site uses Google Analytics cookies to count visits and see which pages are read. What you type in the form goes only to me."

# ---------- Lead catcher (Google Apps Script web app, see _leads/README.md) ----------
# Empty = the guide form opens the visitor's email app, as before.
# Paste the deployed web app's /exec URL here to send leads straight to the Google Sheet and email instead.
LEADS_ENDPOINT = "https://script.google.com/macros/s/AKfycbxmoYm3Gy8GN2AIF1A80Y_kJ9MATNOyFMFDu4otTAe_ZThk8IXxfMJZ8ARSERRtgJAQ/exec"

# ---------- Contact pieces shared by the home page and the question pages ----------
PHONE_DISPLAY = "925.425.8929"
PHONE_TEL = "tel:+19254258929"
EMAIL = "sam@samyusufi.com"
SMS_HREF = "sms:+19254258929?&amp;body=Hi%20Sam%2C%20I%20have%20a%20question%20about%20an%20inherited%20home."
PHONE_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'

# Mobile-only bar pinned to the bottom of the screen: Call, Text, and the guide. Hidden while a form field is in use.
CONTACT_CSS_RAW = """
.cbar{display:none}
@media (max-width:719px){
  body.hascbar{padding-bottom:78px}
  .cbar{display:grid;grid-template-columns:1fr 1fr 1.3fr;gap:8px;position:fixed;left:0;right:0;bottom:0;z-index:50;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(255,255,255,.98);border-top:1px solid var(--ln);box-shadow:0 -6px 20px rgba(0,29,73,.12);transition:transform .2s}
  .cbar.hide{transform:translateY(130%)}
  .cbar a{display:flex;align-items:center;justify-content:center;gap:6px;padding:13px 6px;border-radius:11px;font:700 15px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;text-decoration:none;white-space:nowrap}
  .cbar svg{width:16px;height:16px}
  .cb1{background:var(--navy);color:#fff}
  .cb2{border:1.5px solid var(--navy);color:var(--navy);background:#fff}
  .cb3{background:var(--gold-lt);color:var(--navy)}
}
"""
def contact_bar(guide_href, guide_label):
    return (f'<nav class="cbar" aria-label="Contact Sam">'
            f'<a class="cb1" href="{PHONE_TEL}">{PHONE_ICON}Call</a>'
            f'<a class="cb2" href="{SMS_HREF}">Text</a>'
            f'<a class="cb3" href="{guide_href}">{guide_label}</a></nav>')
CONTACT_JS = """<script>
(function(){var b=document.querySelector('.cbar');if(!b)return;document.body.classList.add('hascbar');
document.addEventListener('focusin',function(e){if(/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName))b.classList.add('hide');});
document.addEventListener('focusout',function(){b.classList.remove('hide');});})();
</script>"""
