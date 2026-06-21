#!/usr/bin/env python3
"""Semantic validator: facts in briefs must have source + locator."""
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
        candidates = brief.get('candidates', [])
        for c in candidates:
            honesty = c.get('candidate_honesty', '')
            if honesty == 'fact':
                # Check if mechanism has source attribution
                mech = c.get('mechanism', {})
                attr = mech.get('attribution', {})
                if not attr.get('ref') and not attr.get('source'):
                    issues.append(f"{fname}/{c.get('prototype_id','')}: fact but mechanism has no source ref")
                # Check if design_translation has evidence_tier
                dt = c.get('design_translation', {})
                if not dt.get('evidence_tier'):
                    issues.append(f"{fname}/{c.get('prototype_id','')}: fact but DT has no evidence_tier")

    if issues:
        print(f"❌ {len(issues)} fact-without-locator issues:")
        for i in issues[:10]:
            print(f"  - {i}")
        return 1
    else:
        print("✅ All facts have source/locator")
        return 0

if __name__ == '__main__':
    sys.exit(main())
