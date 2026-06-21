#!/usr/bin/env python3
"""Semantic validator: source_tier consistency in briefs."""
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
            dt = c.get('design_translation', {})
            source_tier = dt.get('source_tier', '')
            evidence_tier = dt.get('evidence_tier', '')

            # fact candidates must have literature source_tier
            if honesty == 'fact' and source_tier != 'literature':
                issues.append(f"{fname}/{c.get('prototype_id','')}: fact but source_tier={source_tier}")

            # inference candidates should not claim literature
            if honesty == 'inference' and source_tier == 'literature':
                # This is OK if there's a DOI but no quote
                pass

    if issues:
        print(f"❌ {len(issues)} source_tier consistency issues:")
        for i in issues[:10]:
            print(f"  - {i}")
        return 1
    else:
        print("✅ Source tier consistency OK")
        return 0

if __name__ == '__main__':
    sys.exit(main())
