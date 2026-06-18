import os, glob, json

# Scan all local PDFs
pdfs = glob.glob('仿生文献库/**/*.pdf', recursive=True)
pdf_names = set()
for p in pdfs:
    bn = os.path.basename(p)
    pdf_names.add(bn)
    # Also add without " 2.pdf" / " 3.pdf" suffix
    pdf_names.add(bn.replace(' 2.pdf', '.pdf').replace(' 3.pdf', '.pdf'))

# Check chitosan needs_review source_files
with open('prototypes_db/chitosan.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== CHITOSAN: PDF availability for needs_review rows ===")
seen_sf = set()
found = 0
missing = 0
for p in d.get('performance_data', []):
    if p.get('verification', 'unverified') not in ('needs_review', 'missing_pdf'):
        continue
    sf = p.get('source_file', '')
    bn = os.path.basename(sf)
    if bn in seen_sf:
        continue
    seen_sf.add(bn)
    # Check if PDF exists (try exact name and variants)
    exists = bn in pdf_names
    if not exists:
        # Try variant names
        for pn in pdf_names:
            if bn.replace('.pdf', '') in pn or bn.replace('.pdf', ' 2') in pn:
                exists = True
                break
    status = "OK" if exists else "MISSING"
    if exists:
        found += 1
    else:
        missing += 1
    print(f"  {status}: {bn}")

print(f"\n  Found: {found}, Missing: {missing}")

# Also check Aramesh2021 specifically (user already downloaded this)
print("\n=== Aramesh2021 check ===")
aramesh_pdfs = [p for p in pdfs if 'Aramesh' in p]
for p in aramesh_pdfs:
    print(f"  {p} ({os.path.getsize(p)} bytes)")
