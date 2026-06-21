#!/usr/bin/env python3
"""Semantic validator: no llm_inferred basis can be hard DO-NOT."""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(REPO, 'prototypes_db')

def main():
    violations = []
    for f in sorted(glob.glob(os.path.join(DB, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        pid = d.get('id', '')
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if not cc:
                continue
            for bc in cc.get('boundary_conditions', []):
                if bc.get('gate_level') == 'hard':
                    basis = bc.get('basis', '')
                    if basis != 'from_source':
                        violations.append(f"{pid}/{m.get('name','')[:30]}: hard DO-NOT with basis={basis}")

    if violations:
        print(f"❌ {len(violations)} inferred hard DO-NOT violations:")
        for v in violations[:10]:
            print(f"  - {v}")
        return 1
    else:
        print("✅ No inferred hard DO-NOT violations")
        return 0

if __name__ == '__main__':
    sys.exit(main())
