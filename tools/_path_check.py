import os, glob, json

# Check existing chitosan PDFs and their locations
print("=== EXISTING chitosan-related PDFs ===")
for p in glob.glob('仿生文献库/**/*.pdf', recursive=True):
    bn = os.path.basename(p).lower()
    if 'chitosan' in bn or '壳聚糖' in bn:
        print(f"  {p}")

# Check what source_files the chitosan JSON uses
print("\n=== CHITOSAN source_file paths (first few chars of each unique dir) ===")
with open('prototypes_db/chitosan.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
dirs = set()
for p in d.get('performance_data', []):
    sf = p.get('source_file', '')
    if sf:
        d_part = os.path.dirname(sf)
        dirs.add(d_part)
for dd in sorted(dirs):
    print(f"  {dd}")

# Check cell-membrane paths
print("\n=== CELL-MEMBRANE source_file dirs ===")
with open('prototypes_db/cell-membrane-ion-channel.json', 'r', encoding='utf-8') as f:
    d2 = json.load(f)
dirs2 = set()
for p in d2.get('performance_data', []):
    sf = p.get('source_file', '')
    if sf:
        d_part = os.path.dirname(sf)
        dirs2.add(d_part)
for dd in sorted(dirs2):
    print(f"  {dd}")

# Check patent dir for converted CAJ->PDF
print("\n=== PATENT PDFs (converted from CAJ) ===")
for p in glob.glob('仿生文献库/专利/*.pdf', recursive=False):
    bn = os.path.basename(p)
    if 'CN105' in bn or 'CN113' in bn or 'CN114' in bn:
        print(f"  {p} ({os.path.getsize(p)} bytes)")

# List all paper directories
print("\n=== PAPER DIRECTORY STRUCTURE ===")
for d in sorted(glob.glob('仿生文献库/论文/*')):
    if os.path.isdir(d):
        print(f"  {d}")
