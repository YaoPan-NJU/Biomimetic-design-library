import os, glob, json, re

# 1. Build complete inventory of ALL local PDFs with full paths
all_pdfs = {}
for p in glob.glob('仿生文献库/**/*.pdf', recursive=True):
    bn = os.path.basename(p)
    # Store multiple keys: exact name, without " 2"/" 3" suffix, stem
    keys = [bn, bn.replace(' 2.pdf', '.pdf').replace(' 3.pdf', '.pdf')]
    stem = os.path.splitext(bn)[0].replace(' 2', '').replace(' 3', '')
    keys.append(stem)
    for k in keys:
        all_pdfs[k.lower()] = p

print(f"Total local PDFs: {len(set(all_pdfs.values()))}")

# 2. For each chitosan needs_review source_file, do fuzzy matching
with open('prototypes_db/chitosan.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("\n=== CHITOSAN: Deep PDF search ===")
seen = set()
for p in d.get('performance_data', []):
    if p.get('verification', 'unverified') not in ('needs_review', 'missing_pdf'):
        continue
    sf = p.get('source_file', '')
    bn = os.path.basename(sf)
    if bn in seen:
        continue
    seen.add(bn)
    
    # Extract author+year from filename: e.g. "2021-Aramesh-..." -> "aramesh", "2021"
    m = re.match(r'(\d{4})-([A-Za-z\u4e00-\u9fff]+)', bn)
    author_year = f"{m.group(2)}{m.group(1)}".lower() if m else ''
    
    # Try multiple matching strategies
    found = None
    # Strategy 1: exact or variant match
    if bn.lower() in all_pdfs:
        found = all_pdfs[bn.lower()]
    # Strategy 2: stem match (without " 2"/" 3")
    stem = os.path.splitext(bn)[0].replace(' 2', '').replace(' 3', '')
    if stem.lower() in all_pdfs:
        found = all_pdfs[stem.lower()]
    # Strategy 3: author+year match
    if not found and author_year:
        for k, v in all_pdfs.items():
            if author_year in k:
                found = v
                break
    # Strategy 4: DOI-based match (check extraction JSONs)
    if not found:
        doi = p.get('ref_doi', '')
        if doi:
            # Search extraction JSONs for this DOI
            for ej in glob.glob('tools/litextract/outputs/extractions/**/*.json', recursive=True):
                try:
                    with open(ej, 'r', encoding='utf-8') as ef:
                        ed = json.load(ef)
                    if ed.get('bibliographic_metadata', {}).get('doi', '') == doi:
                        # Found extraction JSON, check if corresponding PDF exists
                        pdf_name = os.path.basename(ej).replace('.json', '.pdf')
                        if pdf_name.lower() in all_pdfs:
                            found = all_pdfs[pdf_name.lower()]
                            break
                        # Try variant
                        for variant in [' 2.pdf', ' 3.pdf']:
                            vname = os.path.splitext(pdf_name)[0] + variant
                            if vname.lower() in all_pdfs:
                                found = all_pdfs[vname.lower()]
                                break
                        if found:
                            break
                except:
                    pass
    
    status = "FOUND" if found else "TRULY_MISSING"
    detail = f"  -> {found}" if found else ""
    print(f"  {status}: {bn}")
    if found:
        print(f"    matched: {found}")

# 3. Cell-membrane
with open('prototypes_db/cell-membrane-ion-channel.json', 'r', encoding='utf-8') as f:
    d2 = json.load(f)

print("\n=== CELL-MEMBRANE: Deep PDF search ===")
seen2 = set()
for p in d2.get('performance_data', []):
    if p.get('verification', 'unverified') not in ('needs_review', 'missing_pdf'):
        continue
    sf = p.get('source_file', '')
    bn = os.path.basename(sf)
    if bn in seen2:
        continue
    seen2.add(bn)
    
    found = None
    if bn.lower() in all_pdfs:
        found = all_pdfs[bn.lower()]
    stem = os.path.splitext(bn)[0].replace(' 2', '').replace(' 3', '')
    if not found and stem.lower() in all_pdfs:
        found = all_pdfs[stem.lower()]
    # Author match
    m = re.match(r'(\d{4})-([A-Za-z]+)', bn)
    if not found and m:
        author = m.group(2).lower()
        for k, v in all_pdfs.items():
            if author in k:
                found = v
                break
    
    status = "FOUND" if found else "TRULY_MISSING"
    print(f"  {status}: {bn}")
    if found:
        print(f"    matched: {found}")

# 4. Oyster-shell
with open('prototypes_db/oyster-shell.json', 'r', encoding='utf-8') as f:
    d3 = json.load(f)

print("\n=== OYSTER-SHELL: Deep PDF search ===")
for p in d3.get('performance_data', []):
    if p.get('verification', 'unverified') not in ('needs_review', 'missing_pdf'):
        continue
    sf = p.get('source_file', '')
    bn = os.path.basename(sf)
    found = None
    if bn.lower() in all_pdfs:
        found = all_pdfs[bn.lower()]
    stem = os.path.splitext(bn)[0].replace(' 2', '').replace(' 3', '')
    if not found and stem.lower() in all_pdfs:
        found = all_pdfs[stem.lower()]
    if not found:
        for k, v in all_pdfs.items():
            if 'qiu' in k:
                found = v
                break
    status = "FOUND" if found else "TRULY_MISSING"
    print(f"  {status}: {bn}")
    if found:
        print(f"    matched: {found}")
