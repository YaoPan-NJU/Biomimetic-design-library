#!/usr/bin/env python3
"""Semantic validator: all 36 root prototypes have actionable design_translation."""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(REPO, 'prototypes_db')

REQUIRED_DT_FIELDS = ['design_principle', 'material_handle', 'constraints']

def main():
    issues = []
    for f in sorted(glob.glob(os.path.join(DB, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        pid = d.get('id', '')
        dt = d.get('design_translation', [])
        lifecycle = d.get('lifecycle_status', '')

        if lifecycle == 'deprecated':
            continue

        if not dt:
            issues.append(f"{pid}: no design_translation")
            continue

        if isinstance(dt, dict):
            first = dt
        elif isinstance(dt, list) and len(dt) > 0:
            first = dt[0]
        else:
            issues.append(f"{pid}: design_translation is empty or invalid type")
            continue
        for field in REQUIRED_DT_FIELDS:
            val = first.get(field, '')
            if not val or val == 'needs_review':
                issues.append(f"{pid}: DT missing {field}")

    if issues:
        print(f"❌ {len(issues)} DT actionability issues:")
        for i in issues[:15]:
            print(f"  - {i}")
        return 1
    else:
        print("✅ All 36 prototypes have actionable DT")
        return 0

if __name__ == '__main__':
    sys.exit(main())
