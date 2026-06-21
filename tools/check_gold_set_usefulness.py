#!/usr/bin/env python3
"""Executable gold-set gate: checks briefs against v0.2 gold-set expectations."""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIEFS_DIR = os.path.join(REPO, 'examples', 'adrmats_briefs')

# Gold-set: forbidden candidates per query
FORBIDDEN_CANDIDATES = {
    'bpa_内分泌干扰物去除': {
        'forbidden_normal': ['lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'],
        'required_domain': 'organic',
        'note': 'lotus-leaf has no BPA evidence'
    },
    'pfoa_痕量吸附去除': {
        'forbidden_normal': ['lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'],
        'required_domain': 'organic',
        'note': 'lotus-leaf has no PFAS evidence'
    },
    'pb(ii)_重金属离子去除': {
        'forbidden_normal': ['lotus-leaf', 'shark-skin', 'water-strider-leg'],
        'required_domain': 'heavy_metal',
        'note': 'lotus-leaf has no heavy-metal evidence'
    },
    'cr(vi)_六价铬去除': {
        'forbidden_normal': ['lotus-leaf', 'shark-skin', 'water-strider-leg'],
        'required_domain': 'heavy_metal',
        'note': 'lotus-leaf has no Cr(VI) evidence'
    },
    'smx_抗生素吸附去除': {
        'forbidden_normal': ['lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'],
        'required_domain': 'organic',
        'note': 'lotus-leaf has no SMX evidence'
    },
    '亚甲基蓝染料去除': {
        'forbidden_normal': ['lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'],
        'required_domain': 'dye',
        'note': 'lotus-leaf has no dye evidence'
    },
    '油水分离': {
        'forbidden_normal': ['chitosan', 'bone-structure', 'oyster-shell'],
        'required_domain': 'superwetting',
        'note': 'chitosan is not an oil-water separation material'
    }
}

def check_brief(filepath, case_name):
    """Check a single brief against gold-set expectations."""
    issues = []

    with open(filepath, encoding='utf-8') as f:
        d = json.load(f)

    brief = d.get('brief', d)
    candidates = brief.get('candidates', [])

    if case_name not in FORBIDDEN_CANDIDATES:
        return issues

    rules = FORBIDDEN_CANDIDATES[case_name]
    forbidden = set(rules['forbidden_normal'])

    # Check for forbidden candidates in normal lane
    for c in candidates:
        pid = c.get('prototype_id', '')
        honesty = c.get('candidate_honesty', '')

        if pid in forbidden and honesty in ('fact', 'lead'):
            issues.append(f"FORBIDDEN: {pid} appears as {honesty} in normal lane (should be excluded)")

    return issues


def main():
    briefs = sorted(glob.glob(os.path.join(BRIEFS_DIR, '*.json')))
    if not briefs:
        print("❌ No briefs found")
        return 1

    total_issues = 0
    for f in briefs:
        fname = os.path.basename(f)
        case_name = fname.replace('.json', '')
        issues = check_brief(f, case_name)
        if issues:
            print(f"❌ {fname}: {len(issues)} issues")
            for issue in issues:
                print(f"    - {issue}")
            total_issues += len(issues)
        else:
            print(f"✅ {fname}")

    print(f"\n总计: {len(briefs)} briefs, {total_issues} gold-set issues")
    return 1 if total_issues > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
