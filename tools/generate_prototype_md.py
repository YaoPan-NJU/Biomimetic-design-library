#!/usr/bin/env python3
"""
从 prototypes_db/*.json 渲染 prototype.md。

输入：prototypes_db/<id>.json（结构化正典）
模板：templates/prototype-template.md
输出：prototypes/<id>/prototype.md（带 YAML frontmatter + 6 个标准章节）
"""

import json
import os
import sys
import glob
from pathlib import Path


def load_feature_mapping(repo_dir: Path) -> dict:
    """加载 feature-mapping.json。"""
    fm_path = repo_dir / 'feature-mapping.json'
    with open(fm_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def compute_evidence_level(perf_data: list) -> str:
    """根据 verified 比例计算 evidence_level。"""
    if not perf_data:
        return 'low'
    verified = sum(1 for p in perf_data if p.get('verification') == 'verified')
    ratio = verified / len(perf_data)
    if ratio > 0.8:
        return 'high'
    elif ratio > 0.5:
        return 'medium'
    else:
        return 'low'


def extract_pollutants(perf_data: list) -> list:
    """从 performance_data 聚合所有污染物。"""
    pollutants = set()
    for p in perf_data:
        pol = p.get('pollutant', '')
        if pol and pol != 'unknown':
            pollutants.add(pol)
    return sorted(pollutants)


def extract_mechanism_names(mechanisms: list) -> list:
    """从 mechanisms 提取名称列表。"""
    names = []
    seen = set()
    for m in mechanisms:
        name = m.get('name', '')
        if name and name not in seen:
            seen.add(name)
            names.append(name)
    return names


def compute_qmax_range(perf_data: list) -> str:
    """从 performance_data 计算 qmax 范围。"""
    import re
    values = []
    for p in perf_data:
        val = p.get('value', '')
        unit = p.get('unit', '')
        if 'mg/g' in str(unit).lower() or 'qmax' in p.get('parameter', '').lower():
            if isinstance(val, (int, float)):
                values.append(float(val))
            elif isinstance(val, str):
                nums = re.findall(r'[\d.]+', val)
                for n in nums:
                    try:
                        v = float(n)
                        if 0 < v < 10000:
                            values.append(v)
                    except:
                        pass
    if values:
        return f'{min(values):.1f}-{max(values):.1f} mg/g'
    return ''


def render_frontmatter(d: dict, feature_mapping: dict) -> str:
    """渲染 YAML frontmatter。"""
    fm_meta = feature_mapping.get('prototype_metadata', {}).get(d['id'], {})

    lines = ['---']
    lines.append(f'id: {d["id"]}')
    lines.append(f'name: {d["name_zh"]}（{d["name_en"]}）')
    _cat = d["organism"]["category"]
    _cat = {'真菌': '微生物', '节肢动物': '动物', '海洋无脊椎动物': '动物'}.get(_cat, _cat)
    lines.append(f'category: {_cat}')
    lines.append(f'organism: {d["organism"]["scientific"]}')
    lines.append(f'biomimetic_dimension: {d.get("biomimetic_dimension", "")}')

    # features
    features = d.get('features', []) or fm_meta.get('features', [])
    if features:
        lines.append('features:')
        for f in features:
            lines.append(f'  - {f}')

    # pollutants
    pollutants = extract_pollutants(d.get('performance_data', []))
    if pollutants:
        lines.append('pollutants:')
        for p in pollutants:
            lines.append(f'  - {p}')

    # adsorption_mechanisms
    mech_names = extract_mechanism_names(d.get('mechanisms', []))
    if mech_names:
        lines.append('adsorption_mechanisms:')
        for m in mech_names[:10]:  # 最多 10 个
            lines.append(f'  - {m}')

    # qmax_range
    qmax_range = compute_qmax_range(d.get('performance_data', []))
    if qmax_range:
        lines.append(f'qmax_range: "{qmax_range}"')

    # applicability (tested_conditions)
    tc = d.get('tested_conditions', {})
    if not isinstance(tc, dict):
        tc = {}
    lines.append('applicability:')
    ph_range = tc.get('tested_ph_range')
    if ph_range:
        lines.append(f'  pH_range: [{ph_range[0]}, {ph_range[1]}]')
    else:
        lines.append('  pH_range: null')
    temp_range = tc.get('tested_temp_range')
    if temp_range:
        lines.append(f'  temp_range: [{temp_range[0]}, {temp_range[1]}]')
    else:
        lines.append('  temp_range: null')
    salinity = tc.get('salinity')
    lines.append(f'  salinity: {salinity if salinity else "null"}')

    # evidence_level
    evidence_level = compute_evidence_level(d.get('performance_data', []))
    lines.append(f'evidence_level: {evidence_level}')

    # provenance
    prov = d.get('provenance_summary', {})
    if not isinstance(prov, dict):
        prov = {}
    lines.append(f'# provenance: {prov.get("n_papers", 0)} papers, {prov.get("n_verified", 0)} verified, {prov.get("n_unverified", 0)} unverified')
    lines.append(f'# coverage: {d.get("coverage", "unknown")}')
    lines.append(f'# status: {d.get("status", "unknown")}')

    lines.append('---')
    return '\n'.join(lines)


def render_section_1(d: dict) -> str:
    """1. 生物原型简介"""
    lines = ['## 1. 生物原型简介', '']

    # 从 narrative 的第一个 entry 提取
    _nar = d.get('narrative', {})
    entries = _nar.get('entries', []) if isinstance(_nar, dict) else []
    if entries:
        sections = entries[0].get('sections', {})
        bio_solution = sections.get('biological_solution', sections.get('biological_strategy', ''))
        problem = sections.get('problem_definition', '')
        if problem:
            lines.append(f'**问题定义**：{problem}')
            lines.append('')
        if bio_solution:
            lines.append(f'**生物策略**：{bio_solution}')
            lines.append('')

    if len(lines) <= 2:
        lines.append('[待补充：200-300字介绍]')
        lines.append('')

    return '\n'.join(lines)


def render_section_2(d: dict) -> str:
    """2. 吸附机制详解"""
    lines = ['## 2. 吸附机制详解', '']

    mechs = d.get('mechanisms', [])
    if not mechs:
        lines.append('[待补充]')
        lines.append('')
        return '\n'.join(lines)

    # 去重
    seen = set()
    unique_mechs = []
    for m in mechs:
        key = m.get('name', '')[:50]
        if key and key not in seen:
            seen.add(key)
            unique_mechs.append(m)

    for i, m in enumerate(unique_mechs[:8], 1):  # 最多 8 个机制
        lines.append(f'### 机制{i}：{m.get("name", "未命名")}')
        lines.append('')
        lines.append(f'**描述**：{m.get("description", "")}')
        if m.get('functional_groups'):
            lines.append(f'**关键官能团**：{m["functional_groups"]}')
        if m.get('ref_doi'):
            lines.append(f'**来源**：DOI {m["ref_doi"]}')
        lines.append('')

    return '\n'.join(lines)


def render_section_3(d: dict) -> str:
    """3. 结构特征与结构-功能关系"""
    lines = ['## 3. 结构特征与结构-功能关系', '']

    _nar = d.get('narrative', {})
    entries = _nar.get('entries', []) if isinstance(_nar, dict) else []
    if entries:
        sections = entries[0].get('sections', {})
        key_features = sections.get('key_features', sections.get('structural_features', ''))
        if key_features:
            lines.append(str(key_features))
            lines.append('')
        else:
            lines.append('[待补充：多尺度结构描述]')
            lines.append('')
    else:
        lines.append('[待补充：多尺度结构描述]')
        lines.append('')

    return '\n'.join(lines)


def render_section_4(d: dict) -> str:
    """4. 已报道性能数据"""
    lines = ['## 4. 已报道性能数据', '']

    perf = d.get('performance_data', [])
    if not perf:
        lines.append('[待补充]')
        lines.append('')
        return '\n'.join(lines)

    # 去重（同 pollutant+material+value）
    seen = set()
    unique_perf = []
    for p in perf:
        key = f'{p.get("pollutant", "")}:{p.get("material", "")}:{str(p.get("value", ""))[:30]}'
        if key not in seen:
            seen.add(key)
            unique_perf.append(p)

    lines.append('| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |')
    lines.append('|--------|------|-------------|-----|------|------|')

    for p in unique_perf[:30]:  # 最多 30 行
        pol = p.get('pollutant', '')[:15]
        mat = p.get('material', '')[:20]
        val = str(p.get('value', ''))[:20]
        ph = p.get('ph', '')
        ph_str = str(ph) if ph else '-'

        # 来源标识
        ref = p.get('ref_doi', '') or p.get('patent_number', '') or p.get('standard_number', '')
        source = f'{p.get("source", "")}: {ref}' if ref else p.get('source', '')

        # 核查状态
        v = p.get('verification', 'unverified')
        v_icon = '✅' if v == 'verified' else '⚠️' if v == 'needs_review' else '❓'

        lines.append(f'| {pol} | {mat} | {val} | {ph_str} | {source[:30]} | {v_icon} |')

    if len(unique_perf) > 30:
        lines.append(f'| ... | ... | ... | ... | ... | 共 {len(unique_perf)} 条 |')
    lines.append('')

    return '\n'.join(lines)


def render_section_5(d: dict) -> str:
    """5. 适用场景"""
    lines = ['## 5. 适用场景', '']

    # 从 engineering_constraints 推导
    constraints = d.get('engineering_constraints', [])
    if constraints:
        lines.append('**约束条件**：')
        seen = set()
        for c in constraints[:10]:
            key = c.get('constraint', '')[:30]
            if key and key not in seen:
                seen.add(key)
                lines.append(f'- {c.get("constraint", "")}: {c.get("value", "")} {c.get("unit", "")}')
        lines.append('')
    else:
        lines.append('[待补充：最适合的应用场景和不适用的情况]')
        lines.append('')

    return '\n'.join(lines)


def render_section_6(d: dict, feature_mapping: dict) -> str:
    """6. 相关原型"""
    lines = ['## 6. 相关原型', '']

    # 从 feature-mapping 的 feature_prototype_map 推导相关原型
    features = set(d.get('features', []) or [])
    fpm = feature_mapping.get('feature_prototype_map', {})

    related = set()
    for feat_key, feat_data in fpm.items():
        if not isinstance(feat_data, dict):
            continue
        # 检查这个特征是否与当前原型共享
        proto_ids_in_feat = set()
        for entry in feat_data.get('prototypes', []):
            if isinstance(entry, dict):
                proto_ids_in_feat.add(entry.get('id', ''))
        if d['id'] in proto_ids_in_feat:
            # 找到共享特征的其他原型
            for entry in feat_data.get('prototypes', []):
                if isinstance(entry, dict):
                    pid = entry.get('id', '')
                    if pid and pid != d['id']:
                        related.add(pid)

    if related:
        for pid in sorted(related)[:5]:
            lines.append(f'- {pid}')
        lines.append('')
    else:
        lines.append('[待补充]')
        lines.append('')

    return '\n'.join(lines)


def render_references(d: dict) -> str:
    """参考文献"""
    lines = ['## 参考文献', '']

    refs = set()
    for p in d.get('performance_data', []):
        doi = p.get('ref_doi')
        if doi:
            refs.add(f'DOI: {doi}')
        pn = p.get('patent_number')
        if pn:
            refs.add(f'专利: {pn}')
        sn = p.get('standard_number')
        if sn:
            refs.add(f'标准: {sn}')

    for i, ref in enumerate(sorted(refs), 1):
        lines.append(f'[{i}] {ref}')

    if not refs:
        lines.append('[待补充]')

    lines.append('')
    return '\n'.join(lines)


def generate_prototype_md(d: dict, feature_mapping: dict) -> str:
    """生成完整的 prototype.md 内容。"""
    sections = [
        render_frontmatter(d, feature_mapping),
        f'# {d["name_zh"]}（{d["name_en"]}）',
        '',
        render_section_1(d),
        render_section_2(d),
        render_section_3(d),
        render_section_4(d),
        render_section_5(d),
        render_section_6(d, feature_mapping),
        render_references(d),
    ]
    return '\n'.join(sections)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='从 prototypes_db 渲染 prototype.md')
    parser.add_argument('--db-dir', default=None, help='prototypes_db 目录')
    parser.add_argument('--output-dir', default=None, help='输出目录')
    parser.add_argument('--prototype', default=None, help='只处理指定原型 ID')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = Path(args.db_dir) if args.db_dir else repo_dir / 'prototypes_db'
    output_dir = Path(args.output_dir) if args.output_dir else repo_dir / 'prototypes'

    feature_mapping = load_feature_mapping(repo_dir)

    # 找到所有 JSON
    if args.prototype:
        json_files = [db_dir / f'{args.prototype}.json']
    else:
        json_files = sorted(glob.glob(str(db_dir / '*.json')))

    print(f'生成 {len(json_files)} 个 prototype.md')

    for jf in json_files:
        with open(jf, 'r', encoding='utf-8') as f:
            d = json.load(f)

        pid = d['id']
        md_content = generate_prototype_md(d, feature_mapping)

        out_dir = output_dir / pid
        os.makedirs(out_dir, exist_ok=True)
        out_path = out_dir / 'prototype.md'

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        lines = md_content.count('\n') + 1
        has_frontmatter = md_content.startswith('---')
        print(f'  {pid}: {lines} lines, frontmatter={has_frontmatter}')

    print(f'\n完成! 共生成 {len(json_files)} 个 prototype.md')


if __name__ == '__main__':
    main()
