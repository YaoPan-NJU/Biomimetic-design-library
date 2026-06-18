import json

# Get DOIs for all missing chitosan sources
with open('prototypes_db/chitosan.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== Missing chitosan PDFs with DOIs ===")
for p in d.get('performance_data', []):
    if p.get('verification', 'unverified') not in ('needs_review', 'missing_pdf'):
        continue
    doi = p.get('ref_doi', '')
    sf = p.get('source_file', '')
    # Extract just the filename
    bn = sf.split('/')[-1] if '/' in sf else sf
    print(f"DOI: {doi}")
    print(f"  file: {bn}")
    print()
