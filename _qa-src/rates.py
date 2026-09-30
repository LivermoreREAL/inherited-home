# Recomputes the typical city tax rates used by the Prop 19 calculator (AREAS in prop19.py)
# from each county's official rate book. See UPDATING.md for where to download the files.
#
# Usage (from the repo root):
#   python3 _qa-src/rates.py --alameda ac.csv --contra-costa cc.pdf --san-joaquin sj.pdf
# Prints each city's new rate next to the current one, flags big changes, and prints a ready-to-paste AREAS block.
# Method: a city's "typical" rate is the median total rate (1% base + voter-approved bonds) across its tax rate areas.
import argparse, collections, csv, re, statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def alameda(path):
    # Alameda County open data "Property Tax Rates <year>" CSV: one row per tax per tax rate area.
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    tot, desc = collections.defaultdict(float), {}
    for r in rows:
        k = (r["TRA_PRIM"], r["TRA_SEC"]); tot[k] += float(r["TAX_RATE"]); desc[k] = r["TRA_LONG_DESC"].strip()
    def city(name):
        v = [tot[k] * 100 for k in tot if name.lower() in desc[k].lower()]
        return round(statistics.median(v), 3) if v else None
    allv = [v * 100 for v in tot.values() if 1.0 <= v * 100 < 1.6]
    out = {c: city(c) for c in ["Dublin", "Fremont", "Livermore", "Newark", "Pleasanton", "San Leandro", "Union City"]}
    out["Other Alameda County"] = round(statistics.median(allv), 3)
    return out, len(rows)

def _pdf_text(path):
    import fitz  # PyMuPDF
    return "\n".join(p.get_text() for p in fitz.open(path))

def contra_costa(path):
    # "Detail of Tax Rates <yyyy-yyyy>" PDF: each tax rate area starts with a 5-digit TRA and its total rate.
    t = _pdf_text(path)
    tras = []
    for b in re.split(r"\n(?=\d{5}\n1\.\d{4}\n)", t):
        m = re.match(r"(\d{5})\n(1\.\d{4})\n", b)
        if m: tras.append((float(m.group(2)), b))
    srv = [r for r, b in tras if "SAN RAMON UNIFIED" in b]   # San Ramon Valley USD areas = Danville and San Ramon
    med = round(statistics.median(srv), 3)
    return {"Danville": med, "San Ramon": med, "Other Contra Costa County": round(statistics.median([r for r, _ in tras]), 3)}, len(tras)

def san_joaquin(path):
    # "<yyyy-yy> Property Tax Rates" PDF: each tax rate area ends with "TRA ddd-ddd / 7 / total / Net of All".
    t = _pdf_text(path)
    parts = re.split(r"TRA\s+(\d{3}-\d{3})\s*\n7\n\s*([\d.]+)\n\s*Net of All", t)
    blocks = [(float(parts[i + 1]), parts[i - 1].upper()) for i in range(1, len(parts) - 1, 3)]
    def by(kw):
        v = [r for r, b in blocks if kw in b and r < 1.9]
        return round(statistics.median(v), 3) if v else None
    manteca = by("MANTECA")
    return {"Lathrop": manteca, "Manteca": manteca, "Mountain House": by("LAMMERSV"),
            "Stockton (Stockton Unified)": by("STOCKTON"), "Stockton (Lincoln Unified)": by("LINCOLN"),
            "Tracy": by("TRACY"), "Other San Joaquin County": round(statistics.median([r for r, _ in blocks if r < 1.9]), 3)}, len(blocks)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alameda"); ap.add_argument("--contra-costa"); ap.add_argument("--san-joaquin")
    a = ap.parse_args()
    from prop19 import AREAS
    new = {}
    for label, fn, path in [("Alameda County", alameda, a.alameda), ("Contra Costa County", contra_costa, a.contra_costa), ("San Joaquin County", san_joaquin, a.san_joaquin)]:
        if path:
            vals, n = fn(path); new[label] = vals
            print(f"{label}: parsed {n} rows/areas from {os.path.basename(path)}")
    print("\nCity                          current   new     change")
    flags = 0
    for county, cities in AREAS:
        for name, cur in cities:
            nv = new.get(county, {}).get(name)
            if nv is None:
                print(f"  {name:28s} {cur:.3f}   (no new value)"); flags += county in new; continue
            ch = nv - cur; flag = "  <-- CHECK" if abs(ch) >= 0.10 else ""
            flags += bool(flag)
            print(f"  {name:28s} {cur:.3f}   {nv:.3f}   {ch:+.3f}{flag}")
    print("\nPaste into prop19.py (AREAS):\nAREAS = [")
    for county, cities in AREAS:
        items = ", ".join(f'("{name}", {new.get(county, {}).get(name) or cur:.3f})' for name, cur in cities)
        print(f'  ("{county}", [{items}]),')
    print("]")
    if flags: print(f"\n{flags} value(s) flagged: changed by 0.10 points or more, or missing. Check them by hand before publishing.")

if __name__ == "__main__":
    main()
