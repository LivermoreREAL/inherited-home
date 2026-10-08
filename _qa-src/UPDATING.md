# Yearly updates for whathappenstothehouse.com (Prop 19 calculator)

Two things change over time. Both are set in ONE place: the settings block at the top of `_qa-src/prop19.py`.
The calculator page, its FAQ and structured data, the Q&A Prop 19 page, and llms.txt all read from it.

Repo: `~/Documents/Claude/Projects/inherited-home` (GitHub: LivermoreREAL/inherited-home, GitHub Pages, custom domain whathappenstothehouse.com).
Writing rules for anything a visitor sees: no em dashes, plain and calm tone, California only.

---

## A. Prop 19 parent-child limit (check every February 16)

The Board of Equalization adjusts the $1 million amount every two years (next: transfers from Feb 16, 2027).

1. Open https://www.boe.ca.gov/prop19/ and find the table "Date of Transfer or Change in Ownership / Applicable $1 Million Amount".
2. If it lists a period that starts on Feb 16 of this year and that period is NOT already the first row of `LIMITS`:
   - Insert a new FIRST row in `LIMITS`, for example `("2027", "Feb 16, 2027 to Feb 15, 2029", 1066999),` (use the BOE's exact amount).
   - Add the matching short label to `SHORT_LABELS`, for example `"2027": "2/16/27 to 2/15/29"`.
   - Keep all older rows (they're still used for past transfers).
   - Set `CALC_UPDATED_ISO` / `CALC_UPDATED` to today (for example `"2027-02-16", "February 2027"`).
3. If there is no new period yet (or it's an even year), change nothing.
4. While on the BOE page, confirm these rules are unchanged: child must move in within 1 year and file the homeowners' exemption;
   55+ transfers up to 3 times within 2 years; equal-or-lesser thresholds 100% / 105% / 110%; forms BOE-19-P, BOE-19-G, BOE-19-B,
   BOE-19-D (+ BOE-19-DC), BOE-19-V with a 3-year filing deadline. **If any rule changed, do not publish. Ask Sam.**

## B. County tax rates (every October, when the new tax year's rate books are out)

1. Download the three official files for the new tax year:
   - **Alameda:** data.acgov.org, dataset "Property Tax Rates <year>" (Auditor-Controller). Export CSV.
     Last year's CSV came from `https://data.acgov.org/api/download/v1/items/8a6a0187bf3148b5a180c4bf6aad8f01/csv?layers=0` (the new year has a new dataset id).
     If the CSV has exactly 10,000 rows it may be cut off: spot-check a few cities with the county's Tax Rate Search
     (https://auditor.alamedacountyca.gov/tax-rate-search/) or use the Tax Rate Book PDF on the Auditor-Controller site.
   - **Contra Costa:** "Detail of Tax Rates <yyyy-yyyy>" PDF, contracosta.ca.gov Document Center (Auditor-Controller, usually October).
   - **San Joaquin:** "<yyyy-yy> Property Tax Rates" PDF, sjgov.org Auditor-Controller > Property Tax > Assessed Values and Tax Rates (usually September).
2. Run: `python3 _qa-src/rates.py --alameda ac.csv --contra-costa cc.pdf --san-joaquin sj.pdf`
   It prints each city's new rate next to the current one and a ready-to-paste `AREAS` block.
   **Anything flagged (a change of 0.10 points or more, or missing) must be explained before publishing.** If it can't be, ask Sam.
3. In `prop19.py`: paste the new `AREAS`, set `RATE_YEAR` (for example `"2026-27"`), update the three `RATE_SOURCES` titles and URLs
   to the new files, and set `CALC_UPDATED_ISO` / `CALC_UPDATED` to today.
4. If only some counties have published, don't mix years. Wait and try again in two weeks.

---

## Build, check, publish (both A and B)

```
cd ~/Documents/Claude/Projects/inherited-home
python3 _qa-src/build.py
```
Then check:
- `grep -c "<new amount or new RATE_YEAR>" prop19-calculator/index.html what-happens-to-the-house/prop-19-inherited-home/index.html llms.txt`
- `python3 _qa-src/check.py` must print `problems: none` (structured data parses, links resolve, no em dashes, analytics present)
- `git diff --stat` touches only the calculator, the Q&A Prop 19 page, llms.txt, and prop19.py

Publish:
```
git add -A && git commit -m "Update Prop 19 calculator: <what changed>" && git push
until curl -s https://whathappenstothehouse.com/prop19-calculator/ | grep -q "<new value>"; do sleep 15; done
```
Git pushes use the macOS keychain credentials for GitHub user LivermoreREAL (already set up).

After it's live:
1. Bing Webmaster Tools > URL Submission (site whathappenstothehouse.com): submit `https://whathappenstothehouse.com/prop19-calculator/`
   and `https://whathappenstothehouse.com/what-happens-to-the-house/prop-19-inherited-home/`.
2. Google Search Console (domain property whathappenstothehouse.com) > URL inspection > Request indexing for the calculator URL.
3. Update the Notes cell in row 19 of the Google Sheet "Sam Yusufi — Websites & Admin Links"
   (https://docs.google.com/spreadsheets/d/1QBh4KliTq76Ott_1No7fj7U9uVTmx_k502MlplTj1O0/edit).
4. Tell Sam in plain English what changed.

Do not change: the Google Analytics ID (G-CXF6CNWM21), the Bing verification meta tag, or the CNAME file.
