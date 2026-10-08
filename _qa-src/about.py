# Builds the "About Sam" page (youreastbay.com/about-sam/). Called from build.py after the calculator page.
# Text comes from Sam's approved "About Sam Yusufi" bio and her profile; no testimonials or numbers beyond what she has given.
import os, json

URL_PATH = "about-sam/"

def build_about(g):
    SITE, BASE = g["SITE"], g["BASE"]
    esc, head, cta, foot, PERSON, SMS = g["esc"], g["head"], g["cta"], g["foot"], g["PERSON"], g["SMS"]
    from site_schema import PHONE_TEL, PHONE_DISPLAY, EMAIL, PHONE_ICON, CITY_LIST
    UPDATED_ISO = g["SITE_REFRESH_ISO"]
    url = SITE + URL_PATH
    rel = "/what-happens-to-the-house/"
    title = "About Sam Yusufi, Realtor® and Certified Probate & Trust Specialist | East Bay"
    desc = ("Meet Sam Yusufi, a California real estate broker and Certified Probate & Trust Specialist in Livermore "
            "who helps East Bay families sell an inherited home in probate or a trust.")
    graph = [
      {"@type": "ProfilePage", "@id": url + "#page", "url": url, "name": title, "description": desc, "inLanguage": "en-US",
       "isPartOf": {"@id": SITE + "#website"}, "mainEntity": {"@id": SITE + "#sam"}, "dateModified": UPDATED_ISO,
       "primaryImageOfPage": BASE + "assets/headshot.jpg"},
      PERSON,
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "What Happens to the House?", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "About Sam Yusufi", "item": url}]},
    ]
    out = head(title, desc, url, rel, "profile", {"@context": "https://schema.org", "@graph": graph})
    out += f"""<main class="wrap">
  <nav class="crumb"><a href="{rel}">Guide home</a> &rsaquo; About Sam</nav>
  <h1 class="sf">About Sam Yusufi</h1>
  <p class="lede">I help East Bay families through the sale of an inherited home, whether it's in probate or a trust. I'm a California real estate broker and a Certified Probate &amp; Trust Specialist, and I work with Legacy Real Estate &amp; Associates in Livermore.</p>

  <section class="meet" id="contact" aria-label="Contact Sam Yusufi">
    <img src="{rel}assets/headshot.jpg" alt="Sam Yusufi, Realtor, Certified Probate &amp; Trust Specialist" width="140" height="140">
    <div class="mt">
      <div class="mn sf">Sam Yusufi, Realtor&reg;</div>
      <div class="mr">Associate Broker &middot; Certified Probate &amp; Trust Specialist &middot; DRE#&nbsp;02020587</div>
      <p>Legacy Real Estate &amp; Associates<br>1983 Second St, Livermore, CA 94550</p>
      <a class="mph" href="{PHONE_TEL}">{PHONE_ICON}{PHONE_DISPLAY}</a>
      <div class="mbt"><a class="m1" href="{PHONE_TEL}">Call</a><a class="m2" href="{SMS}">Text</a><a class="m2" href="mailto:{EMAIL}">Email</a></div>
    </div>
  </section>

  <article>
    <h2 class="sf">A little about me</h2>
    <p>I've spent more than twenty years in administration, operations, and real estate, including over a decade in real estate and property management. That steady, detail-oriented background matters when a home sale comes with paperwork, notices, and court dates.</p>
    <p>My approach is built around your family. I believe in open communication and proactive solutions, and I handle every detail with care and precision. I treat the home as your family's loss to move through with care, not a transaction to rush.</p>
    <p>When I'm not helping families, you'll usually find me in an art class or fostering a neighborhood cat or two. A little curiosity and a lot of patience go a long way, in both.</p>

    <h2 class="sf">How I work with families</h2>
    <ul class="dots">
      <li>I confirm who has the authority to sell before we ever talk about price.</li>
      <li>I build notice periods and court dates into the timeline from day one.</li>
      <li>I work alongside your attorney and CPA, not around them.</li>
      <li>I treat the home as your family's loss to move through with care, not a transaction to rush.</li>
    </ul>

    <h2 class="sf">Experience and credentials</h2>
    <table class="t">
      <tr><td>Experience</td><td>More than 20 years across real estate, business development, and operations, including over a decade in real estate and property management and senior roles at Advantage Property Management and Commercial Brokers International.</td></tr>
      <tr><td>Specialty</td><td>Certified Probate &amp; Trust Specialist (CPTS)</td></tr>
      <tr><td>License</td><td>California Real Estate Broker, DRE#&nbsp;02020587</td></tr>
      <tr><td>Brokerage</td><td>Legacy Real Estate &amp; Associates, Livermore</td></tr>
      <tr><td>Languages</td><td>Fluent in English, Farsi, Dari, and Hindi</td></tr>
      <tr><td>Where I work</td><td>{esc(CITY_LIST)}, across Alameda and Contra Costa Counties</td></tr>
    </table>
  </article>

  <aside class="rel"><h2 class="sf">Start here</h2>
    <a href="{rel}inherited-house-first-30-days/">What should you do with an inherited house in the first 30 days?</a>
    <a href="{rel}does-inherited-house-go-through-probate/">Does an inherited house have to go through probate in California?</a>
    <a href="/prop19-calculator/">Prop 19 Calculator</a>
  </aside>
{cta(rel, meet_card=False)}
</main>
{foot(rel)}"""
    os.makedirs(os.path.join(g["SITE_ROOT"], URL_PATH), exist_ok=True)
    open(os.path.join(g["SITE_ROOT"], URL_PATH, "index.html"), "w").write(out)
