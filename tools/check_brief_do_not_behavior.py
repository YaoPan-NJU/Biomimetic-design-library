#!/usr/bin/env python3
"""Semantic validator: hard DO-NOT must have source-backed behavior, not just display."""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIEFS_DIR = os.path.join(REPO, 'examples', 'adrmats_briefs')

def main():
    issues = []
    for f in sorted(glob.glob(os.path.join(BRIEFS_DIR, '*.json'))):
        fname = os.path.basename(f)
        with open(f, encoding='utf-8') as fp:
            d = json.load(fp)
        brief = d.get('brief', d)
        rbc = brief.get('rule_based_cautions', {})
        do_not = rbc.get('do_not', [])
        for dn in do_not:
            basis = dn.get('basis', '')
            verification = dn.get('verification', '')
            # Hard DO-NOT must be from_source + verified/corroborated
            if basis != 'from_source':
                issues.append(f"{fname}: hard DO-NOT with basis={basis} (should be from_source)")
            if verification not in ('verified', 'corroborated'):
                issues.append(f"{fname}: hard DO-NOT with verification={verification}")

    if issues:
        print(f"❌ {len(issues)} hard DO-NOT behavior issues:")
        for i in issues[:10]:
            print(f"  - {i}")
        return 1
    else:
        print("✅ All hard DO-NOT have source-backed behavior")
        return 0

if __name__ == '__main__':
    sys.exit(main())
