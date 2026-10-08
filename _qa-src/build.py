# Builds the "What Happens to the House?" question pages from content.py into what-happens-to-the-house/,
# plus the site-wide sitemap.xml, robots.txt, llms.txt and 404.html at the whathappenstothehouse.com root.
# Run from the repo root: python3 _qa-src/build.py
import html, json, os
from content import PAGES, GROUPS
import prop19 as P19

SITE = "https://whathappenstothehouse.com/"
BASE = SITE + "what-happens-to-the-house/"
LANDING = "/"  # the guide sign-up page is the site home
UPDATED_ISO, UPDATED = "2026-09-29", "September 2026"   # when the answers' content was last reviewed
SITE_REFRESH_ISO = "2026-10-08"                             # when any page of the site last changed (sitemap lastmod)
SMS = "sms:+19254258929?&amp;body=Hi%20Sam%2C%20I%20have%20a%20question%20about%20an%20inherited%20home."
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(SITE_ROOT, "what-happens-to-the-house")
BY = {p["slug"]: p for p in PAGES}
esc = lambda s: html.escape(s, quote=True)

from site_schema import SITE_NAME, PERSON, ICON_TAGS, SERVING, CITY_LIST, ANALYTICS, PRIVACY_NOTE, PHONE_DISPLAY, PHONE_TEL, EMAIL, PHONE_ICON, CONTACT_CSS_RAW, contact_bar, CONTACT_JS, social_line  # shared with the home page build

def head(title, desc, url, rel, ogtype, ld, noindex=False, og=None):
    index_tag = '<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{ANALYTICS}
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{index_tag}
<meta name="author" content="Sam Yusufi, Certified Probate &amp; Trust Specialist">
<meta name="theme-color" content="#001d49">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og or BASE + 'assets/og-image.jpg'}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{ICON_TAGS}
<link rel="apple-touch-icon" href="{rel}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,600;0,8..60,700;1,8..60,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/site.css">
<style>{CONTACT_CSS_RAW}</style>
<script type="application/ld+json">
{json.dumps(ld, indent=1, ensure_ascii=False)}
</script>
</head>
<body>
<header class="top"><div class="in"><a class="brand sf" href="{rel or './'}">What Happens to the House?</a><a class="tcall" href="{PHONE_TEL}">{PHONE_ICON}<span class="tl">Call or text&nbsp;</span><span class="tn">{PHONE_DISPLAY}</span><span class="tm">Call</span></a><a class="tbtn" href="{LANDING}">Free guide</a></div></header>
"""

def cta(rel, meet_card=True):
    return f"""<section class="cta">
  <div class="t sf">Get the full guide, free</div>
  <p>15 printable pages on probate, trusts, taxes, and selling an inherited home in California, with a checklist.</p>
  <a class="g" href="{LANDING}">Get the Free Guide</a>
  <a class="o" href="{SMS}">Text Me</a>
  <p class="n">A no-pressure conversation, whenever you're ready.</p>
</section>
{meet(rel) if meet_card else ""}"""

def foot(rel):
    return f"""<footer class="ft">
  <img src="{rel}assets/logo-combined.png" alt="Sam Yusufi, Realtor&reg; | Legacy Real Estate &amp; Associates" width="120" height="97">
  <div class="sg sf">See you around town.</div>
  Sam Yusufi, Realtor&reg; &middot; Associate Broker &middot; Certified Probate &amp; Trust Specialist &middot; DRE# 02020587<br>
  Legacy Real Estate &amp; Associates<br>
  <span class="fcon">Call or text <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span><br>
  <span class="area">{SERVING}</span><br>
  <a href="{rel or './'}">Guide home</a> &middot; <a href="{LANDING}">Free guide</a> &middot; <a href="/about-sam/">About Sam</a> &middot; <a href="https://samyusufi.com">samyusufi.com</a><br>
  <span class="soc">{social_line()}</span><br>
  <span class="eho"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2 1 11h3v11h16V11h3L12 2Zm4 16H8v-2h8v2Zm0-4H8v-2h8v2Z" fill="#5a6478"/></svg> Equal Housing Opportunity</span>
  <p class="fine">General educational information about California law, current as of {UPDATED}. It is not legal, tax, or financial advice, and reading it doesn't create a professional relationship. Please consult the estate's attorney and CPA about your situation. If your property is currently listed for sale, this is not intended as a solicitation of that listing. {esc(PRIVACY_NOTE)}</p>
</footer>
{contact_bar(LANDING, "Free guide")}
{CONTACT_JS}
</body>
</html>
"""

def meet(rel):
    # "Meet Sam" card: face, credentials, and one-tap Call / Text / Email, shown after the guide call to action.
    return f"""<section class="meet" id="contact" aria-label="Contact Sam Yusufi">
  <img src="{rel}assets/headshot.jpg" alt="Sam Yusufi, Realtor, Certified Probate &amp; Trust Specialist" width="140" height="140">
  <div class="mt">
    <div class="mk">Questions about your family's situation?</div>
    <div class="mn sf">Sam Yusufi, Realtor&reg;</div>
    <div class="mr">Certified Probate &amp; Trust Specialist &middot; DRE#&nbsp;02020587</div>
    <p>I'm happy to talk it through, on your timeline.</p>
    <a class="mph" href="{PHONE_TEL}">{PHONE_ICON}{PHONE_DISPLAY}</a>
    <div class="mbt"><a class="m1" href="{PHONE_TEL}">Call</a><a class="m2" href="{SMS}">Text</a><a class="m2" href="mailto:{EMAIL}">Email</a></div>
  </div>
</section>"""

def byline(rel):
    return f"""<div class="by"><img src="{rel}assets/headshot.jpg" alt="Sam Yusufi" width="36" height="36"><span>By <a href="/about-sam/">Sam Yusufi</a>, Certified Probate &amp; Trust Specialist<br>Updated <time datetime="{UPDATED_ISO}">{UPDATED}</time></span></div>"""

def build_page(p):
    rel = "../"; url = BASE + p["slug"] + "/"
    body = p["body"]
    if p.get("glossary"):
        body = '<dl class="g">\n' + "\n".join(f'<div id="{t.lower().replace(" ","-")}"><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in p["glossary"]) + "\n</dl>"
    graph = [
      {"@type": "Article", "headline": p["h1"], "description": p["meta"], "url": url, "mainEntityOfPage": url,
       "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO, "inLanguage": "en-US",
       "author": {"@id": SITE + "#sam"}, "publisher": {"@id": SITE + "#sam"}, "image": BASE + "assets/og-image.jpg",
       "isPartOf": {"@id": SITE + "#website"}},
      PERSON,
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "What Happens to the House?", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]},
    ]
    if p.get("glossary"):
        graph.append({"@type": "DefinedTermSet", "name": p["h1"], "url": url, "hasDefinedTerm": [
            {"@type": "DefinedTerm", "name": t, "description": d, "url": url + "#" + t.lower().replace(" ", "-")} for t, d in p["glossary"]]})
    else:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": p["h1"],
            "acceptedAnswer": {"@type": "Answer", "text": p["short"]}}]})
    rel_links = "\n".join(f'    <a href="../{s}/">{esc(BY[s]["h1"])}</a>' for s in p["related"])
    out = head(p["h1"] + " | What Happens to the House?", p["meta"], url, rel, "article", {"@context": "https://schema.org", "@graph": graph})
    out += f"""<main class="wrap">
  <nav class="crumb"><a href="../">Guide home</a> &rsaquo; {esc(p["topic"])}</nav>
  <article>
    <h1 class="sf">{esc(p["h1"])}</h1>
    {byline(rel)}
    <div class="short"><div class="k">Short answer</div><p>{esc(p["short"])}</p></div>
{body}
  </article>
  <aside class="rel"><h2 class="sf">Related questions</h2>
{rel_links}
  </aside>
{cta(rel)}
</main>
{foot(rel)}"""
    os.makedirs(os.path.join(ROOT, p["slug"]), exist_ok=True)
    open(os.path.join(ROOT, p["slug"], "index.html"), "w").write(out)

def build_home():
    rel = ""
    groups = ""
    for name, slugs in GROUPS:
        links = "\n".join(f'      <a href="{s}/"><span>{esc(BY[s]["h1"])}</span></a>' for s in slugs)
        groups += f'    <div class="grp"><h2 class="sf">{esc(name)}</h2>\n{links}\n    </div>\n'
    desc = "Answers for California families with an inherited home: probate or trust, who's in charge, overbids, Prop 19, capital gains, and selling. By Sam Yusufi, Certified Probate & Trust Specialist."
    graph = [
      {"@type": "CollectionPage", "@id": BASE + "#page", "name": "What Happens to the House?", "url": BASE, "inLanguage": "en-US",
       "description": desc, "isPartOf": {"@id": SITE + "#website"}, "author": {"@id": SITE + "#sam"}},
      PERSON,
      {"@type": "ItemList", "name": "Questions answered", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": BASE + p["slug"] + "/", "name": p["h1"]} for i, p in enumerate(PAGES)]},
    ]
    out = head("What Happens to the House? Inherited Homes in California | Sam Yusufi, CPTS", desc, BASE, rel, "website", {"@context": "https://schema.org", "@graph": graph})
    out += f"""<section class="hero">
  <div class="in">
    <img class="cpw" src="assets/cpts-white.png" alt="Certified Probate &amp; Trust Specialist" width="150" height="78">
    <div class="ey">A guide for California families</div>
    <h1 class="sf">What Happens to the House?</h1>
    <p>Who's in charge, what to do first, and how to keep or sell an inherited home, without the surprises that catch families off guard.</p>
  </div>
</section>
<main class="wrap">
  <div class="ag" id="about">
    <img src="assets/headshot.jpg" alt="Sam Yusufi" width="64" height="64">
    <div><div class="nm sf">Sam Yusufi, Realtor&reg;</div><div class="rl">Certified Probate &amp; Trust Specialist</div><div class="rl">DRE#&nbsp;02020587 &middot; Legacy Real Estate &amp; Associates</div><div class="rl"><a href="/about-sam/">More about Sam &rarr;</a></div></div>
  </div>
  <p class="lede">Someone you love has passed, and a house is part of what they left behind. Start with the question you're facing today. Each answer takes a few minutes to read.</p>
  <div class="groups">
    <div class="grp"><h2 class="sf">Free tool</h2>
      <a href="/prop19-calculator/"><span>Prop 19 Calculator: what happens to the property tax bill?</span></a>
    </div>
{groups}  </div>
{cta(rel)}
  <section class="hp">
    <img class="cp" src="assets/cpts.png" alt="Certified Probate &amp; Trust Specialist" width="150" height="78">
    <h2 class="sf">How I can help</h2>
    <ul>
      <li>I confirm who has the authority to sell before we ever talk about price.</li>
      <li>I build notice periods and court dates into the timeline from day one.</li>
      <li>I work alongside your attorney and CPA, not around them.</li>
      <li>I treat the home as your family's loss to move through with care, not a transaction to rush.</li>
    </ul>
    <p>I serve families in {CITY_LIST}, across Alameda and Contra Costa Counties, in English, Farsi, Dari, and Hindi.</p>
    <div class="hcta" id="contact">
      <div class="hk">Questions about your family's situation?</div>
      <div class="ht sf">Let's talk it through</div>
      <div class="hs">Call or text me, or send an email. No pressure, no obligation.</div>
      <a class="hph" href="tel:+19254258929">925.425.8929</a>
      <a class="hem" href="mailto:sam@samyusufi.com">sam@samyusufi.com</a>
      <div class="hb">
        <a class="b1" href="tel:+19254258929">Call</a>
        <a class="b2" href="{SMS}">Text</a>
        <a class="b2" href="mailto:sam@samyusufi.com">Email</a>
      </div>
    </div>
  </section>
  <p class="src">More free information: <a href="https://selfhelp.courts.ca.gov/probate">California Courts self-help: probate</a></p>
</main>
{foot(rel)}"""
    open(os.path.join(ROOT, "index.html"), "w").write(out)

def build_404():
    # Served by GitHub Pages for any missing path on whathappenstothehouse.com (including old WordPress links), so every URL is root-relative.
    rel = "/what-happens-to-the-house/"
    out = head("Page not found | What Happens to the House?", "This page isn't here anymore. Find the free guide and answers for California families with an inherited home.",
               SITE, rel, "website", {"@context": "https://schema.org", "@type": "WebPage", "name": "Page not found"}, noindex=True)
    out += f"""<main class="wrap">
  <h1 class="sf">We couldn't find that page</h1>
  <p class="lede">It may have moved, or the link may be from an older version of this site. Here's what you'll find here now.</p>
  <div class="grp"><h2 class="sf">Where to next</h2>
      <a href="/"><span>Get the free guide: What Happens to the House?</span></a>
      <a href="{rel}"><span>Read answers for families with an inherited home</span></a>
  </div>
</main>
{foot(rel)}"""
    open(os.path.join(SITE_ROOT, "404.html"), "w").write(out)

from html.parser import HTMLParser

class _Text(HTMLParser):
    """Turns a page body into plain text: paragraphs, list items as dashes, table rows joined with bars."""
    def __init__(self):
        super().__init__(); self.out = []; self.cell = []; self.row = None; self.in_dt = False
    def handle_starttag(self, tag, attrs):
        if tag in ("p", "ol", "ul", "table", "dl", "h2", "h3"): self.out.append("\n")
        if tag == "li": self.out.append("\n- ")
        if tag == "tr": self.row = []
        if tag in ("td", "th", "dt"): self.cell = []
        if tag == "dt": self.in_dt = True
    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.row is not None: self.row.append(" ".join("".join(self.cell).split()))
        if tag == "tr" and self.row is not None: self.out.append("\n" + " | ".join(self.row)); self.row = None
        if tag == "dt": self.out.append("\n" + " ".join("".join(self.cell).split()) + ": "); self.in_dt = False
        if tag in ("p", "h2", "h3", "dd"): self.out.append("\n")
    def handle_data(self, d):
        self.cell.append(d)
        if self.row is None and not self.in_dt: self.out.append(d)

def to_text(h):
    t = _Text(); t.feed(h)
    lines = [" ".join(l.split()) for l in "".join(t.out).splitlines()]
    out, blank = [], False
    for l in lines:
        if l: out.append(l); blank = False
        elif not blank: out.append(""); blank = True
    # keep list items together: drop the blank line between two "- " items
    tight = [l for i, l in enumerate(out) if not (l == "" and 0 < i < len(out) - 1 and out[i-1].startswith("- ") and out[i+1].startswith("- "))]
    return "\n".join(tight).strip()

def build_meta():
    urls = [SITE, BASE, SITE + "about-sam/", SITE + "prop19-calculator/"] + [BASE + p["slug"] + "/" for p in PAGES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{u}</loc><lastmod>{SITE_REFRESH_ISO}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(SITE_ROOT, "sitemap.xml"), "w").write(sm)
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "Googlebot"]
    rb = "# Everyone is welcome to read and cite this site, including AI assistants.\nUser-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {SITE}sitemap.xml\n"
    open(os.path.join(SITE_ROOT, "robots.txt"), "w").write(rb)
    lt = f"""# What Happens to the House?

> Answers for California families with an inherited home, whether it's in probate or a trust: who's in charge, what to do first, how probate sales and overbids work, trust sales, Prop 19, stepped-up basis, and selling. Written by Sam Yusufi, Realtor(R), Associate Broker and Certified Probate & Trust Specialist (CPTS), Legacy Real Estate & Associates, California DRE# 02020587. Serving the East Bay: {CITY_LIST}, across Alameda and Contra Costa Counties, California. General information about California law, current as of {UPDATED}; not legal or tax advice.

Contact: Sam Yusufi, 925.425.8929 (call or text), sam@samyusufi.com, https://samyusufi.com
Full text of every answer in one file: {SITE}llms-full.txt

Free printable guide (15 pages): {SITE}
All questions: {BASE}
Prop 19 calculator (inherited homes and 55+ moves, with {P19.RATE_YEAR} tax rates for Alameda, Contra Costa, and San Joaquin counties): {SITE}prop19-calculator/

## About the author

Sam Yusufi, Realtor(R), is a California real estate broker (DRE# 02020587) with Legacy Real Estate & Associates in Livermore and a Certified Probate & Trust Specialist (CPTS). She has more than 20 years of professional experience, including over a decade in real estate and property management. She serves families in English, Farsi, Dari, and Hindi. Full profile: {SITE}about-sam/ . Instagram and Facebook: @samyusufi7 (https://www.instagram.com/samyusufi7/ and https://www.facebook.com/samyusufi7/). LinkedIn: https://www.linkedin.com/in/yusufi/

## How to cite

Please cite the specific answer page, name Sam Yusufi, CPTS (DRE# 02020587) as the author, and note that the content is general information about California law, not legal or tax advice. Each answer starts with a short, quotable "Short answer". Answers are current as of {UPDATED}; the Prop 19 limits and tax rates are reviewed every year.

## Free tool

- [Prop 19 Calculator]({SITE}prop19-calculator/): Estimates California property taxes under Proposition 19 for an inherited parent's home (parent-child exclusion, ${P19.CUR_LIMIT:,} limit for transfers {P19.CUR_PERIOD}) and for homeowners 55 or older moving their taxable value to a replacement home (100%, 105%, 110% rules). Includes typical {P19.RATE_YEAR} tax rates by city from each county's official rate book.

"""
    for name, slugs in GROUPS:
        lt += f"## {name}\n\n" + "".join(f"- [{BY[s]['h1']}]({BASE}{s}/): {BY[s]['short']}\n" for s in slugs) + "\n"
    open(os.path.join(SITE_ROOT, "llms.txt"), "w").write(lt)
    full = (f"# What Happens to the House? (full text)\n\nBy Sam Yusufi, Realtor(R), Associate Broker and Certified Probate & Trust Specialist (CPTS), Legacy Real Estate & Associates, California DRE# 02020587. "
            f"{SERVING} General information about California law, current as of {UPDATED}; not legal or tax advice. Contact: 925.425.8929, sam@samyusufi.com, https://samyusufi.com\n\n")
    for name, slugs in GROUPS:
        for s_ in slugs:
            q = BY[s_]; body = q["body"]
            if q.get("glossary"): body = "<dl>" + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in q["glossary"]) + "</dl>"
            full += f"---\n\n## {q['h1']}\n\nURL: {BASE}{s_}/\nTopic: {name}\n\nShort answer: {q['short']}\n\n{to_text(body)}\n\n"
    open(os.path.join(SITE_ROOT, "llms-full.txt"), "w").write(full)

for p in PAGES:
    build_page(p)
build_home(); build_404(); build_meta()
from prop19 import build_prop19
build_prop19(globals())
from about import build_about
build_about(globals())
print(f"built {len(PAGES)} pages + home, prop19 calculator, 404.html, sitemap.xml, robots.txt, llms.txt")
