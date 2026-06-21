#!/usr/bin/env python3
"""M7: 检查 ADRMATS brief 的有用性回归指标。"""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIEFS_DIR = os.path.join(REPO, 'examples', 'adrmats_briefs')

REQUIRED_CANDIDATE_FIELDS = ['prototype_id', 'candidate_honesty', 'match', 'mechanism', 'design_translation', 'boundaries', 'honesty_summary', 'boundary_summary']

def check_brief(filepath):
    """检查单个 brief 的有用性。"""
    issues = []

    with open(filepath, encoding='utf-8') as f:
        d = json.load(f)

    brief = d.get('brief', d)
    candidates = brief.get('candidates', [])
    hl = brief.get('honesty_ledger', {})

    if not candidates:
        issues.append("no candidates")
        return issues

    # Check global honesty_ledger
    if not hl.get('facts') and not hl.get('leads') and not hl.get('inferences'):
        issues.append("global honesty_ledger empty")

    for i, c in enumerate(candidates):
        # Required fields
        for field in REQUIRED_CANDIDATE_FIELDS:
            if field not in c:
                issues.append(f"candidate[{i}] missing {field}")

        # candidate_honesty must be fact/lead/inference
        ch = c.get('candidate_honesty', '')
        if ch not in ('fact', 'lead', 'inference'):
            issues.append(f"candidate[{i}] invalid candidate_honesty: {ch}")

        # design_translation must have material_handle
        dt = c.get('design_translation', {})
        if not dt.get('material_handle'):
            issues.append(f"candidate[{i}] missing material_handle")

        # honesty_summary must be non-empty
        if not c.get('honesty_summary'):
            issues.append(f"candidate[{i}] empty honesty_summary")

        # boundary_summary must be non-empty
        if not c.get('boundary_summary'):
            issues.append(f"candidate[{i}] empty boundary_summary")

    return issues


def main():
    briefs = sorted(glob.glob(os.path.join(BRIEFS_DIR, '*.json')))
    if not briefs:
        print("❌ No briefs found")
        return 1

    total_issues = 0
    for f in briefs:
        fname = os.path.basename(f)
        issues = check_brief(f)
        if issues:
            print(f"❌ {fname}: {len(issues)} issues")
            for issue in issues[:5]:
                print(f"    - {issue}")
            total_issues += len(issues)
        else:
            print(f"✅ {fname}")

    print(f"\n总计: {len(briefs)} briefs, {total_issues} issues")
    return 1 if total_issues > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
