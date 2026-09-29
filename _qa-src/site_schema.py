# Shared site identity for youreastbay.com, used by both builds
# (_qa-src/build.py for the question pages and _guide-src/build.py for the home page).
SITE = "https://youreastbay.com/"
SITE_NAME = "Your East Bay"  # the name Google shows above results; change here, then rebuild both
SITE_ALT_NAMES = ["What Happens to the House?", "youreastbay.com"]

AREAS = [{"@type": "AdministrativeArea", "name": "Alameda County, California"},
         {"@type": "AdministrativeArea", "name": "Contra Costa County, California"}]

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
