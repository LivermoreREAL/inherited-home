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
