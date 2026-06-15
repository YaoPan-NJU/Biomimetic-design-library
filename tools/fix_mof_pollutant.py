#!/usr/bin/env python3
"""补全 MOF 的 pollutant 字段（简化版）。"""

import json

db_path = 'prototypes_db/metal-organic-framework.json'

with open(db_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

perf = data.get('performance_data', [])
fixed = 0

for p in perf:
    if p.get('pollutant') and str(p.get('pollutant')).strip():
        continue

    param = str(p.get('parameter', ''))
    pollutant = None

    # Simple keyword matching
    keywords = {
        'Pb': 'Pb2+', 'Cu': 'Cu2+', 'Cr': 'Cr(VI)', 'Cd': 'Cd2+',
        'Zn': 'Zn2+', 'Ni': 'Ni2+', 'As': 'As(V)', 'Hg': 'Hg2+',
        'U': 'U(VI)', 'F': 'F-', 'P': 'PO4^3-', 'N': 'NH4+',
        'MB': 'Methylene Blue', 'MO': 'Methyl Orange', 'RhB': 'Rhodamine B',
        'CR': 'Congo Red', 'AR': 'Acid Red', 'AO7': 'Azo dye AO7',
        'PFAS': 'PFAS', 'PFBS': 'PFBS', 'PFOA': 'PFOA',
        'Glyphosate': 'Glyphosate', 'Diclofenac': 'Diclofenac',
        'Roxarsone': 'Roxarsone', 'Eosin': 'Eosin Y',
        'Tetracycline': 'Tetracycline', 'Ciprofloxacin': 'Ciprofloxacin',
    }

    for kw, poll in keywords.items():
        if kw in param:
            pollutant = poll
            break

    if pollutant:
        p['pollutant'] = pollutant
        fixed += 1

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

has_pollutant = sum(1 for p in perf if p.get('pollutant') and str(p.get('pollutant')).strip())
no_pollutant = len(perf) - has_pollutant

print(f'MOF pollutant 补全结果:')
print(f'  修复: {fixed} 条')
print(f'  有 pollutant: {has_pollutant}')
print(f'  无 pollutant: {no_pollutant}')
