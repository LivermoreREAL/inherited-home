# Tells Bing (and every search engine and AI tool that uses IndexNow) that pages on youreastbay.com are new or changed,
# so they are re-read within hours instead of days. Run after a change is live:  python3 _qa-src/indexnow.py
# The key file at the site root (bb272f9904c5aa4502982d4042a2d9e8.txt) proves the site is ours.
import json, re, subprocess
KEY = "bb272f9904c5aa4502982d4042a2d9e8"
HOST = "youreastbay.com"
urls = re.findall(r"<loc>([^<]+)</loc>", open("sitemap.xml").read())
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls})
# curl is used (not urllib) because the Python that ships with macOS often lacks the certificates to open https links
r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST", "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8", "-d", body], capture_output=True, text=True, timeout=60)
print("IndexNow:", r.stdout.strip(), f"({len(urls)} URLs sent; 200 or 202 means accepted)")
