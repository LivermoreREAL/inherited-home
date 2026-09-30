# Site-wide checks before publishing. Run from the repo root: python3 _qa-src/check.py
# Verifies every page's structured data parses, root-relative links resolve, and no em dashes slipped in.
import json, os, re, sys
bad, links, blocks = [], 0, 0
for dp, _, fs in os.walk('.'):
    if any(x in dp for x in ('_qa-src', '_guide-src', '.git')): continue
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(dp, f); s = open(p, encoding='utf-8').read()
        for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try: json.loads(j); blocks += 1
            except Exception as e: bad.append((p, 'bad JSON-LD: %s' % e))
        for m in re.findall(r'(?:href|src)="(/[^"#?]*)"', s):
            t = '.' + m; t = t + 'index.html' if t.endswith('/') else t; links += 1
            if not os.path.exists(t): bad.append((p, 'broken link ' + m))
        if '—' in s: bad.append((p, 'em dash'))
        if 'G-CXF6CNWM21' not in s and '404' not in f and 'prop19/' not in p.replace('\\', '/') + '/': bad.append((p, 'missing Google Analytics'))
print('structured data blocks OK: %d | links checked: %d | problems: %s' % (blocks, links, bad or 'none'))
sys.exit(1 if bad else 0)
