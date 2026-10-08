# Tells Bing (and every search engine and AI tool that uses IndexNow) that pages on youreastbay.com are new or changed,
# so they are re-read within hours instead of days. Run after a change is live:  python3 _qa-src/indexnow.py
# The key file at the site root (bb272f9904c5aa4502982d4042a2d9e8.txt) proves the site is ours.
import json, re, sys, urllib.request
KEY = "bb272f9904c5aa4502982d4042a2d9e8"
HOST = "youreastbay.com"
urls = re.findall(r"<loc>([^<]+)</loc>", open("sitemap.xml").read())
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r: print("IndexNow:", r.status, f"({len(urls)} URLs sent)")
except urllib.error.HTTPError as e:
    print("IndexNow:", e.code, e.reason, "(200 or 202 means accepted)")
