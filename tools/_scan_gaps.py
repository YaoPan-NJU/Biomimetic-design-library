import json, os

db = 'prototypes_db'
print("=== MECHANISMS needs_review ===")
total_m = 0
for f in sorted(os.listdir(db)):
    if not f.endswith('.json'):
        continue
    fp = os.path.join(db, f)
    try:
        d = json.load(open(fp, 'r', encoding='utf-8'))
    except:
        continue
    mechs = d.get('mechanisms', [])
    nr = sum(1 for m in mechs if m.get('verification', 'unverified') in ('unverified', 'needs_review'))
    if nr > 0:
        total_m += nr
        print(f"  {f.replace('.json','')}: {len(mechs)} total, {nr} needs_review")
print(f"  TOTAL: {total_m}")

print("\n=== PERFORMANCE needs_review/missing ===")
total_p = 0
for f in sorted(os.listdir(db)):
    if not f.endswith('.json'):
        continue
    fp = os.path.join(db, f)
    try:
        d = json.load(open(fp, 'r', encoding='utf-8'))
    except:
        continue
    perf = d.get('performance_data', [])
    nr = sum(1 for p in perf if p.get('verification', 'unverified') in ('unverified', 'needs_review', 'missing_pdf'))
    if nr > 0:
        total_p += nr
        print(f"  {f.replace('.json','')}: {len(perf)} total, {nr} needs_review")
print(f"  TOTAL: {total_p}")

print("\n=== DIATOM path variants ===")
import glob
variants = glob.glob("仿生文献库/**/*硅藻*2.pdf", recursive=True)
for v in variants:
    print(f"  {v}")
variants2 = glob.glob("仿生文献库/**/*杜*2.pdf", recursive=True)
for v in variants2:
    print(f"  {v}")
