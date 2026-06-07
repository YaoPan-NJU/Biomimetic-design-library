#!/usr/bin/env python3
"""
从 311 个提取 JSON 构建 prototypes_db/ 结构化存储。

映射策略（优先级从高到低）：
1. routing.prototype_targets（v2 文件 + 部分 v1 文件）
2. biomimetic_organism 字段映射
3. 标题/摘要关键词匹配

每个原型输出一个 JSON 文件，schema 参见优化计划 P0-1。
"""

import json
import os
import re
import glob
from pathlib import Path
from collections import defaultdict

# === ID 别名归一化 ===
ID_ALIASES = {
    'mof-adsorbent': 'metal-organic-framework',
    'alginate-adsorbent': 'alginate',
    'starch-adsorbent': 'starch-granule',
    'chlorella': 'chlorella-cell-wall',
    'wood-structure': 'wood-xylem',
    'superhydrophobic-surface': 'superhydrophobic-artificial',
    'diatom': 'diatom-frustule',
    'diatom-inspired-porous': 'diatom-frustule',
}

# === 关键词→原型映射（v1 无 prototype_targets 时的回退） ===
KEYWORD_TO_PROTOTYPE = {
    'sulfate-reducing': 'sulfate-reducing-bacteria',
    'sulfate reducing': 'sulfate-reducing-bacteria',
    'SRB': 'sulfate-reducing-bacteria',
    'iron-oxidizing': 'iron-oxidizing-bacteria',
    'iron oxidizing': 'iron-oxidizing-bacteria',
    'magnetic bacteria': 'magnetic-bacteria',
    'magnetotactic': 'magnetic-bacteria',
    'chitosan': 'chitosan',
    '壳聚糖': 'chitosan',
    'lotus': 'lotus-leaf',
    '荷叶': 'lotus-leaf',
    'mussel': 'mussel-foot-adhesion',
    '贻贝': 'mussel-foot-adhesion',
    'diatom': 'diatom-frustule',
    '硅藻': 'diatom-frustule',
    'MOF': 'metal-organic-framework',
    'metal-organic framework': 'metal-organic-framework',
    '金属有机框架': 'metal-organic-framework',
    'alginate': 'alginate',
    '海藻酸': 'alginate',
    'cellulose': 'cellulose-nanocrystal',
    '纤维素': 'cellulose-nanocrystal',
    'starch': 'starch-granule',
    '淀粉': 'starch-granule',
    'spider silk': 'spider-silk',
    '蜘蛛丝': 'spider-silk',
    'shark skin': 'shark-skin',
    '鲨鱼皮': 'shark-skin',
    'coral': 'coral-skeleton',
    '珊瑚': 'coral-skeleton',
    'oyster': 'oyster-shell',
    '牡蛎': 'oyster-shell',
    'wood': 'wood-xylem',
    '木材': 'wood-xylem',
    'bone': 'bone-structure',
    '骨': 'bone-structure',
    'mycelium': 'mycelium',
    '菌丝': 'mycelium',
    'silk fibroin': 'silk-fibroin',
    '丝素蛋白': 'silk-fibroin',
    'PDA': 'polydopamine-coating',
    'polydopamine': 'polydopamine-coating',
    '聚多巴胺': 'polydopamine-coating',
    'aquaporin': 'cell-membrane-ion-channel',
    '水通道蛋白': 'cell-membrane-ion-channel',
    'fish scale': 'fish-scale-hydroxyapatite',
    '鱼鳞': 'fish-scale-hydroxyapatite',
    'gecko': 'gecko-adhesion',
    '壁虎': 'gecko-adhesion',
    'mangrove': 'mangrove-root',
    '红树林': 'mangrove-root',
    'lobster': 'lobster-exoskeleton',
    '龙虾': 'lobster-exoskeleton',
    'scallop': 'scallop-shell',
    '扇贝': 'scallop-shell',
    'cactus': 'cactus-spine',
    '仙人掌': 'cactus-spine',
    'namib beetle': 'namib-beetle',
    '纳米布甲虫': 'namib-beetle',
    'water strider': 'water-strider-leg',
    '水黾': 'water-strider-leg',
    'pitcher plant': 'pitcher-plant-slippery-surface',
    '猪笼草': 'pitcher-plant-slippery-surface',
    'tannin': 'plant-tannin',
    '单宁': 'plant-tannin',
}

# === organism→原型映射 ===
ORGANISM_TO_PROTOTYPE = {
    'mussel': 'mussel-foot-adhesion',
    'lotus': 'lotus-leaf',
    'lotus leaf': 'lotus-leaf',
    'diatom': 'diatom-frustule',
    'chitosan': 'chitosan',
    'chlorella': 'chlorella-cell-wall',
    'alginate': 'alginate',
    'spider': 'spider-silk',
    'spider silk': 'spider-silk',
    'shark': 'shark-skin',
    'shark skin': 'shark-skin',
    'coral': 'coral-skeleton',
    'coral skeleton': 'coral-skeleton',
    'oyster': 'oyster-shell',
    'oyster shell': 'oyster-shell',
    'wood': 'wood-xylem',
    'bone': 'bone-structure',
    'mycelium': 'mycelium',
    'silk': 'silk-fibroin',
    'silk fibroin': 'silk-fibroin',
    'cellulose': 'cellulose-nanocrystal',
    'starch': 'starch-granule',
    'MOF': 'metal-organic-framework',
    'metal-organic framework': 'metal-organic-framework',
    'PDA': 'polydopamine-coating',
    'polydopamine': 'polydopamine-coating',
    'aquaporin': 'cell-membrane-ion-channel',
    'fish scale': 'fish-scale-hydroxyapatite',
    'gecko': 'gecko-adhesion',
    'mangrove': 'mangrove-root',
    'lobster': 'lobster-exoskeleton',
    'scallop': 'scallop-shell',
    'cactus': 'cactus-spine',
    'namib beetle': 'namib-beetle',
    'water strider': 'water-strider-leg',
    'pitcher plant': 'pitcher-plant-slippery-surface',
    'tannin': 'plant-tannin',
    'plant tannin': 'plant-tannin',
    'magnetic bacteria': 'magnetic-bacteria',
    'iron oxidizing bacteria': 'iron-oxidizing-bacteria',
    'sulfate reducing bacteria': 'sulfate-reducing-bacteria',
}


def normalize_id(raw_id: str) -> str:
    """将别名 ID 归一化为规范 ID。"""
    return ID_ALIASES.get(raw_id, raw_id)


def map_file_to_prototypes(data: dict, json_file: str) -> list:
    """将一个 JSON 文件映射到原型 ID 列表。"""
    targets = []
    routing = data.get('routing', {})

    # 策略 1: prototype_targets（最可靠）
    pt = routing.get('prototype_targets', [])
    if pt:
        for t in pt:
            pid = normalize_id(t.get('prototype_id', ''))
            if pid:
                targets.append({
                    'prototype_id': pid,
                    'confidence': t.get('confidence', 0.8),
                    'match_reason': t.get('match_reason', 'prototype_targets')
                })
        if targets:
            return targets

    # 策略 2: biomimetic_organism
    organism = routing.get('biomimetic_organism')
    if organism:
        if isinstance(organism, list):
            organism_parts = organism
        else:
            organism_parts = organism.split(',')
        for org in organism_parts:
            org = str(org).strip().lower()
            if org in ORGANISM_TO_PROTOTYPE:
                pid = ORGANISM_TO_PROTOTYPE[org]
                targets.append({
                    'prototype_id': pid,
                    'confidence': 0.8,
                    'match_reason': f'biomimetic_organism: {org}'
                })
        if targets:
            return targets

    # 策略 3: 关键词匹配（标题 + 摘要）
    meta = data.get('bibliographic_metadata', {})
    title = meta.get('title', '')
    abstract = meta.get('abstract', '')
    content = f'{title} {abstract}'.lower()

    seen = set()
    for keyword, pid in KEYWORD_TO_PROTOTYPE.items():
        if keyword.lower() in content and pid not in seen:
            seen.add(pid)
            targets.append({
                'prototype_id': pid,
                'confidence': 0.6,
                'match_reason': f'keyword: {keyword}'
            })

    return targets


def extract_performance_data(knowledge_items: list, file_meta: dict = None) -> list:
    """从 knowledge_items 中提取性能数据。file_meta 用于回退 patent_number/standard_number。"""
    file_patent = file_meta.get('patent_number') if file_meta else None
    file_standard = file_meta.get('standard_number') if file_meta else None
    perf_keywords = ['qmax', 'removal', 'adsorption capacity', '去除率', '吸附容量',
                     'adsorption rate', 'removal efficiency', 'removal rate']
    results = []
    for item in knowledge_items:
        param = item.get('parameter', '').lower()
        if any(kw in param for kw in perf_keywords):
            ctx = item.get('context', {})
            # 尝试从 context 中提取 pollutant 和 material
            pollutant = ctx.get('pollutant', '') or ctx.get('target_pollutant', '')
            material = ctx.get('material', '') or ctx.get('adsorbent', '')

            results.append({
                'parameter': item.get('parameter', ''),
                'value': item.get('value', ''),
                'unit': item.get('unit', ''),
                'pollutant': pollutant,
                'material': material,
                'ph': ctx.get('pH', ctx.get('ph', None)),
                'temperature': ctx.get('temperature', ctx.get('temp', None)),
                'conditions': ctx.get('conditions', ''),
                'source': item.get('source', 'literature'),
                'ref_doi': item.get('ref_doi'),
                'patent_number': item.get('patent_number') or file_patent,
                'standard_number': item.get('standard_number') or file_standard,
                'source_file': item.get('source_file'),
                'page': item.get('evidence', [{}])[0].get('page') if item.get('evidence') else None,
                'locator': item.get('evidence', [{}])[0].get('locator') if item.get('evidence') else None,
                'verification': 'unverified',
                'confidence': 0.8
            })
    return results


def extract_mechanisms(knowledge_items: list) -> list:
    """从 knowledge_items 中提取机制描述。"""
    mech_keywords = ['mechanism', 'adsorption mechanism', '吸附机制', '机理', '吸附机理',
                     'coordination', 'chelation', '配位', '螯合', '静电', 'hydrogen bond',
                     'hydrophobic', '疏水']
    results = []
    for item in knowledge_items:
        param = item.get('parameter', '').lower()
        val = str(item.get('value', '')).lower()
        if any(kw in param or kw in val for kw in mech_keywords):
            results.append({
                'name': item.get('parameter', ''),
                'description': item.get('value', ''),
                'functional_groups': item.get('context', {}).get('functional_groups', ''),
                'source': item.get('source', 'literature'),
                'ref_doi': item.get('ref_doi'),
                'verification': 'unverified'
            })
    return results


def extract_constraints(knowledge_items: list) -> list:
    """从 knowledge_items 中提取工程约束。"""
    constraint_keywords = ['ph', 'temperature', '再生', '循环', '稳定性',
                           'regeneration', 'stability', 'reusability', '循环使用']
    results = []
    seen = set()
    for item in knowledge_items:
        param = item.get('parameter', '')
        # 精确匹配 pH（避免匹配 phosphorus, graphene 等）
        param_lower = param.lower()
        is_constraint = False
        if re.search(r'\bpH\b', param, re.IGNORECASE):
            is_constraint = True
        elif any(kw in param_lower for kw in ['temperature', '再生', '循环', '稳定性',
                                                'regeneration', 'stability', 'reusability']):
            is_constraint = True

        if is_constraint:
            key = f'{param}:{item.get("value", "")}'
            if key not in seen:
                seen.add(key)
                results.append({
                    'constraint': param,
                    'value': item.get('value', ''),
                    'unit': item.get('unit', ''),
                    'relevance': 'high' if 'stability' in param_lower or '再生' in param else 'medium',
                    'explanation': item.get('context', {}).get('conditions', ''),
                    'source': item.get('source', 'literature'),
                    'ref_doi': item.get('ref_doi')
                })
    return results


def build_narrative_list(data: dict, json_file: str) -> list:
    """将 biomimetic_narrative 转为带来源的 list。"""
    narrative = data.get('biomimetic_narrative')
    if not narrative:
        return []
    return [{
        'source_file': json_file,
        'paper_id': data.get('paper_id', ''),
        'sections': narrative
    }]


def build_metadata_list(data: dict, json_file: str) -> list:
    """将 biomimetic_metadata 转为带来源的 list。"""
    metadata = data.get('biomimetic_metadata')
    if not metadata:
        return []
    return [{
        'source_file': json_file,
        'paper_id': data.get('paper_id', ''),
        'metadata': metadata
    }]


def aggregate_prototype(prototype_id: str, file_infos: list, feature_mapping: dict) -> dict:
    """将多个 JSON 文件的数据聚合为一个结构化原型。"""
    all_items = []
    all_perf = []
    all_mechs = []
    all_constraints = []
    all_narratives = []
    all_metadata = []
    all_sources = set()

    for fi in file_infos:
        json_file = fi['json_file']
        if not os.path.exists(json_file):
            continue

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f'  ERROR reading {json_file}: {e}')
            continue

        items = data.get('knowledge_items', [])
        for item in items:
            item['_source_file'] = json_file
        all_items.extend(items)

        file_meta = data.get('bibliographic_metadata', {})
        all_perf.extend(extract_performance_data(items, file_meta))
        all_mechs.extend(extract_mechanisms(items))
        all_constraints.extend(extract_constraints(items))
        all_narratives.extend(build_narrative_list(data, json_file))
        all_metadata.extend(build_metadata_list(data, json_file))

        # 收集来源
        meta = data.get('bibliographic_metadata', {})
        doi = meta.get('doi')
        if doi:
            all_sources.add(('literature', doi))
        pn = meta.get('patent_number')
        if pn:
            all_sources.add(('patent', pn))
        sn = meta.get('standard_number')
        if sn:
            all_sources.add(('standard', sn))

    # 从 feature-mapping 获取元数据
    pm = feature_mapping.get('prototype_metadata', {}).get(prototype_id, {})

    # 原型中文名和类别映射
    PROTOTYPE_NAMES = {
        'lotus-leaf': ('荷叶表面', '植物'),
        'mussel-foot-adhesion': ('贻贝足丝', '动物'),
        'chitosan': ('壳聚糖', '仿生材料'),
        'polydopamine-coating': ('聚多巴胺涂层', '仿生材料'),
        'metal-organic-framework': ('金属有机框架', '仿生材料'),
        'sulfate-reducing-bacteria': ('硫酸盐还原菌', '微生物'),
        'iron-oxidizing-bacteria': ('铁氧化细菌', '微生物'),
        'magnetic-bacteria': ('磁性细菌', '微生物'),
        'chlorella-cell-wall': ('小球藻细胞壁', '微生物'),
        'diatom-frustule': ('硅藻壳', '微生物'),
        'diatom-inspired-porous': ('仿硅藻多孔结构', '微生物'),
        'alginate': ('海藻酸盐', '植物'),
        'cellulose-nanocrystal': ('纤维素纳米晶', '植物'),
        'starch-granule': ('淀粉颗粒', '植物'),
        'spider-silk': ('蜘蛛丝', '动物'),
        'shark-skin': ('鲨鱼皮', '动物'),
        'coral-skeleton': ('珊瑚骨架', '动物'),
        'oyster-shell': ('牡蛎壳', '动物'),
        'lobster-exoskeleton': ('龙虾外骨骼', '动物'),
        'fish-scale-hydroxyapatite': ('鱼鳞羟基磷灰石', '动物'),
        'water-strider-leg': ('水黾腿部', '动物'),
        'namib-beetle': ('纳米布甲虫', '动物'),
        'scallop-shell': ('扇贝壳', '动物'),
        'bone-structure': ('骨结构', '动物'),
        'silk-fibroin': ('丝素蛋白', '动物'),
        'cell-membrane-ion-channel': ('细胞膜离子通道', '仿生材料'),
        'wood-xylem': ('木材木质部', '植物'),
        'mycelium': ('菌丝体', '微生物'),
        'mangrove-root': ('红树林根系', '植物'),
        'cactus-spine': ('仙人掌刺', '植物'),
        'pitcher-plant-slippery-surface': ('猪笼草滑溜表面', '植物'),
        'plant-tannin': ('植物单宁', '植物'),
        'superhydrophobic-artificial': ('超疏水人工表面', '仿生材料'),
        'biomineralization-template': ('生物矿化模板', '仿生材料'),
        'dna-aptamer': ('DNA 适配体', '仿生材料'),
        'silkworm-silk': ('蚕丝', '动物'),
    }

    name_zh, organism_category = PROTOTYPE_NAMES.get(prototype_id, (prototype_id, ''))
    name_en = prototype_id.replace('-', ' ').title()

    # 聚合 organism 信息（从 metadata list 中提取最常见的）
    organism_scientific = ''
    if all_metadata:
        organisms = []
        for m in all_metadata:
            org = m.get('metadata', {}).get('organism_scientific', '')
            if org:
                if isinstance(org, list):
                    organisms.extend([str(o) for o in org])
                else:
                    organisms.append(str(org))
        if organisms:
            from collections import Counter
            most_common = Counter(organisms).most_common(1)[0][0]
            organism_scientific = most_common

    # 构建结构化 JSON
    result = {
        'id': prototype_id,
        'name_zh': name_zh,
        'name_en': name_en,
        'organism': {
            'scientific': organism_scientific,
            'category': organism_category
        },
        'biomimetic_dimension': pm.get('biomimetic_dimension', ''),
        'features': pm.get('features', []),
        'tested_conditions': {
            'tested_ph_range': None,
            'tested_temp_range': None,
            'salinity': pm.get('applicability', {}).get('salinity') if pm.get('applicability') else None,
            'note': '测过的 pH/温度范围，不是适用范围。仅从 performance_data 中实际测试过的条件聚合。'
        },
        'performance_data': all_perf,
        'mechanisms': all_mechs,
        'narrative': {
            'entries': all_narratives
        },
        'engineering_constraints': all_constraints,
        'provenance_summary': {
            'n_papers': len(file_infos),
            'n_verified': 0,
            'n_unverified': len(all_perf) + len(all_mechs)
        },
        'coverage': 'normal' if len(all_perf) > 0 else 'low',
        'status': 'active' if len(all_items) > 0 else 'needs_literature'
    }

    # 从 performance_data 聚合 tested_ph_range 和 tested_temp_range
    ph_values = [p['ph'] for p in all_perf if p.get('ph') is not None]
    temp_values = [p['temperature'] for p in all_perf if p.get('temperature') is not None]

    if ph_values:
        try:
            ph_nums = [float(p) for p in ph_values if isinstance(p, (int, float)) or (isinstance(p, str) and p.replace('.', '').isdigit())]
            if ph_nums:
                result['tested_conditions']['tested_ph_range'] = [min(ph_nums), max(ph_nums)]
        except (ValueError, TypeError):
            pass

    if temp_values:
        try:
            temp_nums = [float(t) for t in temp_values if isinstance(t, (int, float)) or (isinstance(t, str) and str(t).replace('.', '').isdigit())]
            if temp_nums:
                result['tested_conditions']['tested_temp_range'] = [min(temp_nums), max(temp_nums)]
        except (ValueError, TypeError):
            pass

    return result


def main():
    repo_dir = Path(__file__).resolve().parents[1]
    extractions_dir = repo_dir / 'tools' / 'litextract' / 'outputs' / 'extractions'
    feature_mapping_path = repo_dir / 'feature-mapping.json'
    output_dir = repo_dir / 'prototypes_db'

    # 读取 feature-mapping
    with open(feature_mapping_path, 'r', encoding='utf-8') as f:
        feature_mapping = json.load(f)

    valid_ids = set(feature_mapping.get('prototype_metadata', {}).keys())
    print(f'Valid prototype IDs from feature-mapping: {len(valid_ids)}')

    # 收集所有 JSON 文件
    json_files = []
    for subdir in ['论文/json', '专利/json', '标准/json']:
        pattern = str(extractions_dir / subdir / '*.json')
        json_files.extend(glob.glob(pattern))
    print(f'Total JSON files: {len(json_files)}')

    # 映射文件→原型
    prototype_mapping = defaultdict(list)
    unmapped = 0
    mapped = 0

    for jf in json_files:
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            unmapped += 1
            continue

        targets = map_file_to_prototypes(data, jf)
        if not targets:
            unmapped += 1
            continue

        for t in targets:
            pid = t['prototype_id']
            if pid in valid_ids:
                prototype_mapping[pid].append({
                    'json_file': jf,
                    'confidence': t['confidence'],
                    'match_reason': t['match_reason']
                })
                mapped += 1

    print(f'\nMapping results:')
    print(f'  Mapped file-prototype pairs: {mapped}')
    print(f'  Unmapped files: {unmapped}')
    print(f'  Prototypes with data: {len(prototype_mapping)}')

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 聚合每个原型
    for pid in sorted(valid_ids):
        file_infos = prototype_mapping.get(pid, [])
        print(f'\n  {pid}: {len(file_infos)} files')

        result = aggregate_prototype(pid, file_infos, feature_mapping)

        output_path = output_dir / f'{pid}.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f'    → {output_path.name}: {len(result["performance_data"])} perf, {len(result["mechanisms"])} mech, {len(result["engineering_constraints"])} constr')

    # 统计
    print(f'\n=== 完成 ===')
    print(f'输出目录: {output_dir}')
    print(f'原型数: {len(valid_ids)}')

    # 检查空原型
    empty = []
    for pid in sorted(valid_ids):
        path = output_dir / f'{pid}.json'
        with open(path, 'r') as f:
            d = json.load(f)
        if d['status'] == 'needs_literature':
            empty.append(pid)
    if empty:
        print(f'空原型（needs_literature）: {len(empty)}')
        for pid in empty:
            print(f'  - {pid}')


if __name__ == '__main__':
    main()
