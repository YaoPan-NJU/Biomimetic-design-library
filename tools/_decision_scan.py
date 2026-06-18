import json, os

# 1. Chitosan: list all unique source DOIs from needs_review perf rows
with open('prototypes_db/chitosan.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== CHITOSAN needs_review perf rows - source DOIs ===")
doi_rows = {}
for p in d.get('performance_data', []):
    v = p.get('verification', 'unverified')
    if v in ('needs_review', 'missing_pdf'):
        doi = p.get('ref_doi', 'NO_DOI')
        sf = p.get('source_file', '')
        key = doi or 'NO_DOI'
        if key not in doi_rows:
            doi_rows[key] = {'count': 0, 'source_file': sf}
        doi_rows[key]['count'] += 1

for doi, info in sorted(doi_rows.items(), key=lambda x: -x[1]['count']):
    print(f"  {doi}: {info['count']} rows  ({info['source_file'][:60]})")

# 2. Cell-membrane: list all source DOIs
with open('prototypes_db/cell-membrane-ion-channel.json', 'r', encoding='utf-8') as f:
    d2 = json.load(f)

print("\n=== CELL-MEMBRANE needs_review perf rows - source DOIs ===")
for p in d2.get('performance_data', []):
    if p.get('verification', 'unverified') in ('needs_review', 'missing_pdf'):
        doi = p.get('ref_doi', 'NO_DOI')
        sf = p.get('source_file', '')
        print(f"  {doi}  ({sf[:60]})")

# 3. Oyster-shell: the 1 missing row
with open('prototypes_db/oyster-shell.json', 'r', encoding='utf-8') as f:
    d3 = json.load(f)

print("\n=== OYSTER-SHELL needs_review perf rows ===")
for p in d3.get('performance_data', []):
    if p.get('verification', 'unverified') in ('needs_review', 'missing_pdf'):
        doi = p.get('ref_doi', 'NO_DOI')
        sf = p.get('source_file', '')
        print(f"  {doi}  ({sf[:60]})")

# 4. Zero-perf prototypes
print("\n=== ZERO-PERF PROTOTYPES ===")
for name in ['coral-skeleton', 'magnetic-bacteria', 'lobster-exoskeleton']:
    fp = f'prototypes_db/{name}.json'
    try:
        d4 = json.load(open(fp, 'r', encoding='utf-8'))
        perf = len(d4.get('performance_data', []))
        mech = len(d4.get('mechanisms', []))
        prov = d4.get('provenance_summary', {})
        print(f"  {name}: perf={perf}, mech={mech}, provenance={prov}")
    except:
        print(f"  {name}: file not found")
