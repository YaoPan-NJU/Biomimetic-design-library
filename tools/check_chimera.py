#!/usr/bin/env python3
"""
检查 chimera 原型（机制串库 / organism 不一致）。

检测逻辑：
1. organism 字段检查：organism.scientific 包含 ≥2 个不同类生物
2. 机制主题一致性：机制条目的 name/description 是否与原型 ID 的领域一致
3. 来源论文路由检查：读取 raw extraction JSON，检查 routing.biomimetic_organism

运行模式：
  --report-only (默认)：输出违规清单
  --strict：零违规通过才返回 0
"""

import json
import os
import sys
import re
import argparse
from pathlib import Path


# 原型 ID → 允许的机制关键词（用于主题一致性检查）
PROTOTYPE_DOMAIN_KEYWORDS = {
    'mussel-foot-adhesion': ['mussel', 'DOPA', 'catechol', '贻贝', '邻苯二酚', 'PDA', 'polydopamine', '足丝'],
    'polydopamine-coating': ['PDA', 'polydopamine', 'dopamine', '多巴胺', 'catechol', '邻苯二酚'],
    'metal-organic-framework': ['MOF', 'metal-organic', '金属有机框架', 'coordination polymer'],
    'chitosan': ['chitosan', '壳聚糖', 'chitin', '甲壳素', 'amino group', '氨基'],
    'alginate': ['alginate', '海藻酸', 'alginate', 'guluronic', 'mannuronic'],
    'cellulose-nanocrystal': ['cellulose', '纤维素', 'nanocrystal', 'nanocellulose', 'CNC', 'CNF'],
    'starch-granule': ['starch', '淀粉', 'amylose', 'amylopectin'],
    'lotus-leaf': ['lotus', '荷叶', 'superhydrophobic', '超疏水', 'self-cleaning', 'selfcleaning'],
    'shark-skin': ['shark', '鲨鱼', 'denticle', 'riblet', 'dermal'],
    'spider-silk': ['spider', '蜘蛛', 'silk', 'fibroin', 'dragline'],
    'water-strider-leg': ['water strider', '水黾', 'Gerridae', 'superhydrophobic', '微针'],
    'cactus-spine': ['cactus', '仙人掌', 'spine', 'cone', 'fog collection'],
    'superhydrophobic-artificial': ['superhydrophobic', '超疏水', 'contact angle', 'WCA', 'lotus', 'PTFE', 'PDMS'],
    'silkworm-silk': ['silkworm', '蚕丝', 'silk fibroin', 'Bombyx'],
}

# 不相关生物关键词（出现在 organism 中则为 chimera）
UNRELATED_ORGANISMS = {
    'shark-skin': ['lotus', 'Nelumbo', 'gecko', 'butterfly', 'rose', 'Salvinia', 'fish scale'],
    'polydopamine-coating': ['Stenocara', 'beetle', 'gecko', 'lotus', 'butterfly'],
    'spider-silk': ['lotus', 'Nelumbo', 'gecko', 'butterfly', 'rose', 'fish scale', 'Nepenthes'],
    'water-strider-leg': ['lotus', 'Nelumbo', 'gecko', 'butterfly', 'rose'],
    'cactus-spine': ['lotus', 'Nelumbo', 'gecko', 'butterfly', 'rose', 'spider'],
}


def check_organism(pid: str, data: dict) -> list:
    """检查 organism 字段是否包含不相关生物。"""
    issues = []
    org = data.get('organism', {})
    sci = org.get('scientific', '')
    if not sci:
        return issues

    # 检查不相关生物
    if pid in UNRELATED_ORGANISMS:
        for bad_kw in UNRELATED_ORGANISMS[pid]:
            if bad_kw.lower() in sci.lower():
                issues.append(f'organism 含不相关生物 "{bad_kw}": {sci[:60]}')

    # 通用检查：≥3 个不同类生物
    parts = [p.strip() for p in re.split(r'[,;/]', sci) if p.strip()]
    if len(parts) > 2 and 'spp.' not in sci and '多物种' not in sci:
        issues.append(f'organism 含 {len(parts)} 个不同类生物: {sci[:60]}')

    return issues


def check_mechanism_consistency(pid: str, data: dict) -> list:
    """检查机制条目是否与原型 ID 的领域一致。"""
    issues = []
    allowed_kw = PROTOTYPE_DOMAIN_KEYWORDS.get(pid, [])

    if not allowed_kw:
        return issues

    for m in data.get('mechanisms', []):
        name = m.get('name', '')
        desc = m.get('description', '')
        text = f'{name} {desc}'.lower()

        # 检查是否包含不相关的机制关键词
        if pid in UNRELATED_ORGANISMS:
            for bad_kw in UNRELATED_ORGANISMS[pid]:
                if bad_kw.lower() in text:
                    issues.append(f'机制含不相关关键词 "{bad_kw}": {name[:50]}')
                    break

    return issues


def check_blocklist(pid: str, data: dict, blocklist: dict) -> list:
    """检查 mechanism / performance_data / narrative 是否命中 blocklist 污染关键词。"""
    issues = []
    blocked_kws = blocklist.get(pid, [])
    if not blocked_kws:
        return issues

    def match(text, label, detail=''):
        text_lower = text.lower()
        for kw in blocked_kws:
            if kw.lower() in text_lower:
                issues.append(
                    f'BLOCKLIST[{label}]: {detail} 命中 "{kw}"'
                )
                return True
        return False

    # 1. mechanisms
    for m in data.get('mechanisms', []):
        name = m.get('name', '')
        desc = m.get('description', '')
        principle = m.get('基本原理', '')
        match(f'{name} {desc} {principle}', 'mechanism', f'"{name[:60]}"')

    # 1b. mechanism_instances（同 mechanisms 扫描逻辑）
    for m in data.get('mechanism_instances', []):
        name = m.get('name', '')
        desc = m.get('description', '')
        match(f'{name} {desc}', 'instance', f'"{name[:60]}"')

    # 2. performance_data
    for i, p in enumerate(data.get('performance_data', [])):
        fields = ' '.join(str(p.get(k, '')) for k in ['pollutant', 'parameter', 'value', 'material', 'conditions', 'source_file'])
        match(fields, 'perf', f'perf[{i}] pollutant={p.get("pollutant","")}, material={p.get("material","")[:40]}')

    # 3. narrative entries
    for entry in data.get('narrative', {}).get('entries', []):
        sections = entry.get('sections', {})
        all_text = ' '.join(str(v) for v in sections.values() if v)
        paper_id = entry.get('paper_id', '')
        match(all_text, 'narrative', f'paper_id={paper_id[:40]}')

    return issues


def check_routing(pid: str, data: dict, extraction_dir: str) -> list:
    """检查来源论文的 routing.biomimetic_organism 是否与原型 ID 匹配。"""
    issues = []
    # 从 source_file 提取文件名，查找对应的 raw extraction JSON
    for p in data.get('performance_data', []):
        sf = p.get('source_file', '')
        if not sf:
            continue
        # 提取文件名
        basename = os.path.basename(sf)
        # 尝试在 extraction 目录中找到对应的 JSON
        for category in ['论文', '专利', '标准']:
            candidate = os.path.join(extraction_dir, category, 'json', basename)
            if os.path.exists(candidate):
                try:
                    with open(candidate, 'r', encoding='utf-8') as f:
                        raw = json.load(f)
                    routing = raw.get('routing', {})
                    bio_org = routing.get('biomimetic_organism', '')
                    if bio_org and pid not in bio_org.lower():
                        # 检查是否真的是不匹配
                        issues.append(f'routing.biomimetic_organism="{bio_org}" 与原型 {pid} 不匹配: {basename[:40]}')
                except:
                    pass
                break
    return issues


def main():
    parser = argparse.ArgumentParser(description='检查 chimera 原型')
    parser.add_argument('--db-dir', default=None)
    parser.add_argument('--extraction-dir', default=None)
    parser.add_argument('--strict', action='store_true', help='严格模式：零违规通过')
    parser.add_argument('--report-only', action='store_true', help='报告模式：输出清单')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = args.db_dir or str(repo_dir / 'prototypes_db')
    extraction_dir = args.extraction_dir or str(repo_dir / 'tools' / 'litextract' / 'outputs' / 'extractions')

    # 加载 blocklist
    blocklist_path = os.path.join(os.path.dirname(__file__), 'chimera_blocklist.json')
    blocklist = {}
    if os.path.exists(blocklist_path):
        with open(blocklist_path, 'r', encoding='utf-8') as f:
            blocklist = json.load(f)

    mode = 'strict' if args.strict else 'report-only'
    print(f'=== Chimera 检查 ({mode} 模式) ===\n')

    total_issues = 0
    issue_details = {}

    for fname in sorted(os.listdir(db_dir)):
        if not fname.endswith('.json'):
            continue
        pid = fname.replace('.json', '')
        fpath = os.path.join(db_dir, fname)

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            continue

        issues = []

        # 1. organism 检查
        issues.extend(check_organism(pid, data))

        # 2. 机制主题一致性
        issues.extend(check_mechanism_consistency(pid, data))

        # 2b. blocklist 检查
        issues.extend(check_blocklist(pid, data, blocklist))

        # 3. routing 检查（如果 extraction 目录存在）
        if os.path.exists(extraction_dir):
            issues.extend(check_routing(pid, data, extraction_dir))

        if issues:
            issue_details[pid] = issues
            total_issues += len(issues)
            print(f'❌ {pid}:')
            for issue in issues[:10]:  # 最多显示 10 个
                print(f'    - {issue}')
            if len(issues) > 10:
                print(f'    ... 还有 {len(issues) - 10} 个问题')
            print()

    print(f'=== 总结 ===')
    print(f'  违规原型: {len(issue_details)}')
    print(f'  总违规数: {total_issues}')

    if args.strict:
        if total_issues > 0:
            print(f'\n❌ 严格模式：发现 {total_issues} 个违规')
            sys.exit(1)
        else:
            print('\n✅ 严格模式：无违规')
            sys.exit(0)
    else:
        if total_issues > 0:
            print(f'\n⚠️ 报告模式：发现 {total_issues} 个违规（详见上方）')
        else:
            print('\n✅ 报告模式：无违规')
        sys.exit(0)


if __name__ == '__main__':
    main()
