#!/usr/bin/env python3
"""Semantic validator: honesty_ledger consistency in briefs."""
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
        hl = brief.get('honesty_ledger', {})
        candidates = brief.get('candidates', [])

        # Check that honesty_ledger is not empty
        if not hl.get('facts') and not hl.get('leads') and not hl.get('inferences'):
            issues.append(f"{fname}: honesty_ledger empty")

        # Check that per-candidate honesty matches global ledger
        fact_count = sum(1 for c in candidates if c.get('candidate_honesty') == 'fact')
        lead_count = sum(1 for c in candidates if c.get('candidate_honesty') == 'lead')
        infer_count = sum(1 for c in candidates if c.get('candidate_honesty') == 'inference')

        # Global ledger should reflect candidate counts
        if fact_count > 0 and not hl.get('facts'):
            issues.append(f"{fname}: {fact_count} fact candidates but no global facts")

    if issues:
        print(f"❌ {len(issues)} ledger consistency issues:")
        for i in issues[:10]:
            print(f"  - {i}")
        return 1
    else:
        print("✅ Brief ledger consistency OK")
        return 0

if __name__ == '__main__':
    sys.exit(main())
