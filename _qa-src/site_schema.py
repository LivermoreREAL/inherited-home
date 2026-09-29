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
  "worksFor": {"@type": "RealEstateAgent", "name": "Legacy Real Estate & Associates"},
  "hasCredential": [
    {"@type": "EducationalOccupationalCredential", "name": "Certified Probate & Trust Specialist (CPTS)", "credentialCategory": "certification"},
    {"@type": "EducationalOccupationalCredential", "name": "California Real Estate Broker License", "identifier": "DRE# 02020587", "credentialCategory": "license",
     "recognizedBy": {"@type": "GovernmentOrganization", "name": "California Department of Real Estate"}}],
  "areaServed": AREAS,
  "knowsLanguage": ["English", "Persian", "Hindi"],
  "sameAs": ["https://www.facebook.com/samyusufibroker/", "https://www.linkedin.com/in/yusufi/", "https://www.instagram.com/samyusufi7/"],
}

ICON_TAGS = '<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">'

# Google Analytics 4 (property "youreastbay.com" in the "Sam Yusufi Real Estate" account).
# Counts page views, plus these events: generate_lead (guide form sent), text_me (sms taps),
# call_click, email_click, and guide_cta_click (a "Free guide" button that leads to the form).
# No names, emails, phone numbers, or addresses are ever sent to Google.
GA_ID = "G-CXF6CNWM21"
ANALYTICS = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('js',new Date());gtag('config','{GA_ID}');
document.addEventListener('click',function(e){{
  var a=e.target.closest&&e.target.closest('a');if(!a)return;
  var h=a.getAttribute('href')||'',p={{link_location:location.pathname}};
  var n=h.indexOf('sms:')===0?'text_me':h.indexOf('tel:')===0?'call_click':h.indexOf('mailto:')===0?'email_click':'';
  if(n){{
    // Texting, calling, and email apps take over the screen right away, which can cut off the
    // message to Google. Send it first (as a beacon), then open the app a moment later.
    e.preventDefault();
    var done=false,go=function(){{if(!done){{done=true;location.href=h;}}}};
    gtag('event',n,{{link_location:p.link_location,transport_type:'beacon',event_callback:go,event_timeout:600}});
    setTimeout(go,700);
  }}
  else if(h==='/'&&/free guide/i.test(a.textContent))gtag('event','guide_cta_click',p);
}});
</script>"""
PRIVACY_NOTE = "This site uses Google Analytics cookies to count visits and see which pages are read. What you type in the form goes only to me."
