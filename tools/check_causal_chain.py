#!/usr/bin/env python3
"""Phase 5 验收：检查每个 active 原型的 causal_chain 合格率。"""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(REPO, 'prototypes_db')

REQUIRED_ELEMENTS = ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']

def check_causal_chain(mech):
    """Check if a mechanism has a valid causal_chain card."""
    cc = mech.get('causal_chain')
    if not cc or not isinstance(cc, dict):
        return None, 'missing causal_chain'

    issues = []
    for elem in REQUIRED_ELEMENTS:
        val = cc.get(elem, {})
        if not isinstance(val, dict):
            issues.append(f'{elem}: not a dict')
        elif not (val.get('text') or '').strip():
            issues.append(f'{elem}: empty text')
        elif val.get('basis') not in ('from_source', 'llm_inferred'):
            issues.append(f'{elem}: missing/invalid basis')

    # boundary_conditions
    bc = cc.get('boundary_conditions', [])
    if not bc:
        issues.append('no boundary_conditions')

    # transferable_principle
    tp = cc.get('transferable_principle', '')
    if not (tp or '').strip():
        issues.append('no transferable_principle')

    if issues:
        return cc, '; '.join(issues)
    return cc, None

def main():
    results = []
    for f in sorted(glob.glob(os.path.join(DB, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        pid = d.get('id', os.path.basename(f).replace('.json', ''))
        mechs = d.get('mechanisms', [])

        qualified = 0
        unmarked_basis = 0
        details = []

        for m in mechs:
            cc, issue = check_causal_chain(m)
            if issue is None:
                qualified += 1
            else:
                details.append(f'  {m.get("name","")[:50]}: {issue}')
            # Check for unmarked basis
            if cc:
                for elem in REQUIRED_ELEMENTS:
                    val = cc.get(elem, {})
                    if isinstance(val, dict) and not val.get('basis'):
                        unmarked_basis += 1

        results.append({
            'pid': pid,
            'total': len(mechs),
            'qualified': qualified,
            'unmarked_basis': unmarked_basis,
            'details': details[:5]
        })

    # Count empty basis elements across entire DB
    empty_basis_total = 0
    for f in glob.glob(os.path.join(DB, '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain')
            if not cc:
                continue
            for elem in REQUIRED_ELEMENTS:
                val = cc.get(elem, {})
                if isinstance(val, dict) and not (val.get('basis') or '').strip():
                    empty_basis_total += 1
            for b in cc.get('boundary_conditions', []):
                if isinstance(b, dict) and not (b.get('basis') or '').strip():
                    empty_basis_total += 1

    # Print report
    print('=== Phase 5: Causal Chain 检查 ===\n')
    total_qualified = 0
    total_mechs = 0
    for r in results:
        status = '✅' if r['qualified'] >= 1 else '❌'
        print(f'{status} {r["pid"]}: {r["qualified"]}/{r["total"]} qualified')
        total_qualified += r['qualified']
        total_mechs += r['total']
        for d in r['details']:
            print(f'    {d}')

    no_qualified = [r for r in results if r['qualified'] < 1]
    print(f'\n=== 总结 ===')
    print(f'  已填合格卡: {total_qualified} / 总机制 {total_mechs}')
    print(f'  剩余 causal_chain 空 basis 要素数: {empty_basis_total} (须=0)')
    print(f'  无合格卡原型: {len(no_qualified)}')
    if no_qualified:
        print(f'    {[r["pid"] for r in no_qualified]}')

    # R1-E fix: no longer writes to user-owned docs/optimization-v1/
    # Output is printed to stdout only (validators must not write to user dirs)
    if '--out' in sys.argv:
        idx = sys.argv.index('--out')
        if idx + 1 < len(sys.argv):
            out_path = sys.argv[idx + 1]
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write('# Phase 5 — Causal Chain 合格率\n\n')
                f.write(f'| 原型 | 总机制 | 合格卡 | 未标basis |\n')
                f.write(f'|------|--------|--------|----------|\n')
                for r in results:
                    f.write(f'| {r["pid"]} | {r["total"]} | {r["qualified"]} | {r["unmarked_basis"]} |\n')
                f.write(f'\n总计: {total_qualified}/{total_mechs} qualified\n')
            print(f'\n输出: {out_path}')

if __name__ == '__main__':
    main()
