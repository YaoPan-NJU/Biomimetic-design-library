#!/usr/bin/env python3
"""Stage 2: 语义聚合 — 从提参 KI 中按污染物维度聚合出结构化摘要。"""
import json, os, re, sys
from collections import defaultdict, Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKB = os.path.join(BASE, 'pollutant_knowledge_base')
BY_POLL = os.path.join(PKB, 'by_pollutant')
OUT_SUM = os.path.join(PKB, 'summaries')
OUT_FLAT = os.path.join(OUT_SUM, 'adsorption_performance_flat.jsonl')

CONFIDENCE_THRESHOLD = 0.5
LOW_CONFIDENCE_THRESHOLD = 0.8

# Feature matching rules (from feature_matching_rules.json)
def load_feature_rules():
    path = os.path.join(BASE, 'feature_matching_rules.json')
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        return data.get('molecular_feature_to_prototype', {})
    return {}

# Prototype list
def load_prototypes():
    proto_dir = os.path.join(BASE, 'prototypes_db')
    return [fn.replace('.json', '') for fn in os.listdir(proto_dir) if fn.endswith('.json')]

# Keyword → prototype mapping for mechanism matching
MECH_KEYWORD_MAP = {
    '吸附': ['chitosan', 'plant-tannin', 'polydopamine-coating', 'diatom-frustule'],
    '配位': ['chitosan', 'mussel-foot-adhesion', 'polydopamine-coating'],
    '螯合': ['chitosan', 'mussel-foot-adhesion', 'polydopamine-coating'],
    '静电': ['chitosan', 'polydopamine-coating', 'silk-fibroin'],
    '氢键': ['chitosan', 'silk-fibroin', 'cellulose-nanocrystal'],
    'π-π': ['polydopamine-coating', 'plant-tannin', 'graphene'],
    '疏水': ['lotus-leaf', 'superhydrophobic-artificial', 'plant-wax-cuticle'],
    '离子交换': ['chitosan', 'bone-structure', 'oyster-shell'],
    '沉淀': ['oyster-shell', 'bone-structure', 'iron-oxidizing-bacteria'],
    '还原': ['iron-oxidizing-bacteria', 'sulfate-reducing-bacteria'],
    '氧化': ['iron-oxidizing-bacteria', 'polydopamine-coating'],
    '光降解': [],  # no biomimetic prototype
    '生物降解': ['fungal-biosorption', 'mycelium'],
    '超疏水': ['lotus-leaf', 'superhydrophobic-artificial'],
    '膜分离': ['cell-membrane-ion-channel'],
}


def extract_qmax(ki):
    """Extract qmax value from a KI if present."""
    val = str(ki.get('value', ''))
    param = (ki.get('parameter', '') or '').lower()

    # Direct qmax
    if 'qmax' in param or '最大吸附' in param:
        nums = re.findall(r'[\d.]+', val)
        if nums:
            try:
                return float(nums[0])
            except:
                pass

    # mg/g in value
    if 'mg/g' in val or 'mg g' in val:
        nums = re.findall(r'[\d.]+', val)
        if nums:
            try:
                return float(nums[0])
            except:
                pass

    return None


def extract_material(ki):
    """Extract material name from KI context."""
    param = (ki.get('parameter', '') or '')
    context = str(ki.get('context', '') or '')
    val = str(ki.get('value', ''))

    # Common material keywords
    materials = []
    material_keywords = [
        '活性炭', 'biochar', '生物炭', '壳聚糖', 'chitosan', 'MOF', '金属有机框架',
        '沸石', 'zeolite', '石墨烯', 'graphene', '碳纳米管', 'CNT', 'GO', 'rGO',
        '海藻酸', 'alginate', '纤维素', 'cellulose', '淀粉', 'starch',
        '钛酸盐', 'titanate', '氧化铁', 'iron oxide', '磁性', 'magnetic',
        '树脂', 'resin', '硅胶', 'silica', '硅藻土', 'diatomite',
        '聚苯胺', 'polyaniline', '聚吡咯', 'polypyrrole', 'PDA', '聚多巴胺',
        '水凝胶', 'hydrogel', '气凝胶', 'aerogel', '膜', 'membrane',
    ]

    text = param + ' ' + context + ' ' + val
    for kw in material_keywords:
        if kw.lower() in text.lower():
            materials.append(kw)

    return materials[0] if materials else None


def aggregate_pollutant(poll_dir, poll_path):
    """Aggregate all KI for one pollutant."""
    all_ki = []
    paper_count = 0
    empty_count = 0
    skipped_low_conf = 0

    for fn in os.listdir(poll_path):
        if not fn.endswith('.json'):
            continue
        with open(os.path.join(poll_path, fn)) as f:
            data = json.load(f)

        paper_count += 1
        ki_list = data.get('knowledge_items', [])
        if not ki_list:
            empty_count += 1
            continue

        doi = data.get('bibliographic_metadata', {}).get('doi', '')
        source_file = fn

        for ki in ki_list:
            conf = ki.get('confidence', 1.0) or 1.0
            if conf < CONFIDENCE_THRESHOLD:
                skipped_low_conf += 1
                continue

            ki['_paper_doi'] = doi
            ki['_source_file'] = source_file
            ki['_low_confidence'] = conf < LOW_CONFIDENCE_THRESHOLD
            all_ki.append(ki)

    # Group by domain_direction
    by_dd = defaultdict(list)
    for ki in all_ki:
        dd = ki.get('domain_direction', 'unknown')
        by_dd[dd].append(ki)

    # Properties (D11_pollutant_property)
    properties = defaultdict(list)
    for ki in by_dd.get('D11_pollutant_property', []):
        param = (ki.get('parameter', '') or '').strip()
        if not param:
            continue
        properties[param].append({
            'value': ki.get('value', ''),
            'unit': ki.get('unit', ''),
            'ref_doi': ki.get('ref_doi', '') or ki.get('_paper_doi', ''),
            'source_file': ki.get('source_file', '') or ki.get('_source_file', ''),
            'confidence': ki.get('confidence', 1.0),
            'low_confidence': ki.get('_low_confidence', False)
        })

    # Removal mechanisms (D4_adsorption_mechanism)
    mech_counter = Counter()
    mech_details = defaultdict(list)
    mech_refs = defaultdict(set)
    for ki in by_dd.get('D4_adsorption_mechanism', []):
        param = (ki.get('parameter', '') or '').strip()
        val = str(ki.get('value', ''))
        context = str(ki.get('context', '') or '')
        text = param + ' ' + val + ' ' + str(context)

        # Match mechanism keywords
        for kw, protos in MECH_KEYWORD_MAP.items():
            if kw in text:
                mech_counter[kw] += 1
                mech_details[kw].append({
                    'parameter': param,
                    'value': val[:200],
                    'ref_doi': ki.get('ref_doi', '') or ki.get('_paper_doi', ''),
                })
                doi = ki.get('ref_doi', '') or ki.get('_paper_doi', '')
                if doi:
                    mech_refs[kw].add(doi)

    removal_mechanisms = []
    for mech, count in mech_counter.most_common(20):
        removal_mechanisms.append({
            'mechanism': mech,
            'evidence_count': count,
            'key_references': list(mech_refs[mech])[:5],
            'details': mech_details[mech][:3]
        })

    # Adsorption performance (D1_adsorption_performance)
    perf_materials = defaultdict(lambda: {'qmax_values': [], 'refs': [], 'conditions': []})
    flat_rows = []

    for ki in by_dd.get('D1_adsorption_performance', []):
        param = (ki.get('parameter', '') or '').strip()
        val = str(ki.get('value', ''))
        context = str(ki.get('context', '') or '')
        doi = ki.get('ref_doi', '') or ki.get('_paper_doi', '')
        source_file = ki.get('source_file', '') or ki.get('_source_file', '')

        material = extract_material(ki)
        qmax = extract_qmax(ki)

        if material:
            entry = perf_materials[material]
            if qmax:
                entry['qmax_values'].append(qmax)
            if doi:
                entry['refs'].append(doi)
            entry['conditions'].append({
                'parameter': param,
                'value': val[:100],
                'ref_doi': doi,
                'source_file': source_file,
            })

            # Flat row
            flat_rows.append({
                'pollutant': poll_dir,
                'material': material,
                'parameter': param,
                'value': val[:200],
                'qmax_mg_g': qmax,
                'ref_doi': doi,
                'source_file': source_file,
                'confidence': ki.get('confidence', 1.0),
            })

    # Build best_materials list
    best_materials = []
    for mat, data in sorted(perf_materials.items(), key=lambda x: -len(x[1]['qmax_values'])):
        qmax_vals = data['qmax_values']
        best_materials.append({
            'material': mat,
            'qmax_mg_g': max(qmax_vals) if qmax_vals else None,
            'qmax_avg': round(sum(qmax_vals)/len(qmax_vals), 1) if qmax_vals else None,
            'evidence_count': len(data['conditions']),
            'ref_dois': list(set(data['refs']))[:5],
        })

    # Engineering constraints (D5_engineering_constraint)
    constraints = []
    for ki in by_dd.get('D5_engineering_constraint', []):
        param = (ki.get('parameter', '') or '').strip()
        val = str(ki.get('value', ''))
        if param or val:
            constraints.append({
                'parameter': param,
                'value': val[:200],
                'ref_doi': ki.get('ref_doi', '') or ki.get('_paper_doi', ''),
            })

    # Occurrence patterns (D12_occurrence_pattern)
    occurrences = []
    for ki in by_dd.get('D12_occurrence_pattern', []):
        param = (ki.get('parameter', '') or '').strip()
        val = str(ki.get('value', ''))
        if param or val:
            occurrences.append({
                'parameter': param,
                'value': val[:200],
                'ref_doi': ki.get('ref_doi', '') or ki.get('_paper_doi', ''),
            })

    # Derive molecular_features_for_biomimetic_matching
    molecular_features = set()
    # From properties
    for param in properties:
        p = param.lower()
        if 'logp' in p or '疏水' in p:
            molecular_features.add('疏水性')
        if 'pka' in p or '酸' in p:
            molecular_features.add('弱酸性')
        if '溶解' in p:
            molecular_features.add('水溶性')
        if '分子量' in p or 'mw' in p:
            molecular_features.add('大分子')

    # From mechanisms
    for mech in removal_mechanisms:
        m = mech['mechanism']
        if m in ('吸附', '配位', '螯合'):
            molecular_features.add('可配位')
        if m == 'π-π':
            molecular_features.add('芳香环')
        if m == '疏水' or m == '超疏水':
            molecular_features.add('疏水性')
        if m == '静电':
            molecular_features.add('可电离')

    # From pollutant name
    poll_lower = poll_dir.lower()
    if '酚' in poll_dir or 'phenol' in poll_lower:
        molecular_features.update(['芳香环', '酚羟基'])
    if '氟' in poll_dir or 'pfoa' in poll_lower or 'pfos' in poll_lower or 'pfas' in poll_lower:
        molecular_features.add('氟碳链')
    if '氯' in poll_dir or 'chlor' in poll_lower:
        molecular_features.add('氯代')
    if 'bpa' in poll_lower or '双酚' in poll_dir:
        molecular_features.update(['芳香环', '酚羟基', '内分泌干扰'])

    # Recommend prototypes
    feature_rules = load_feature_rules()
    recommended = set()
    for feat in molecular_features:
        if feat in feature_rules:
            for proto in feature_rules[feat].get('prototypes', []):
                recommended.add(proto)

    return {
        'pollutant_name': poll_dir,
        'paper_count': paper_count,
        'total_ki': len(all_ki),
        'empty_papers': empty_count,
        'skipped_low_confidence': skipped_low_conf,
        'ki_by_domain': {dd: len(ki_list) for dd, ki_list in sorted(by_dd.items(), key=lambda x: -len(x[1]))},
        'properties': {k: v for k, v in sorted(properties.items())},
        'removal_mechanisms': removal_mechanisms,
        'adsorption_performance': {
            'best_materials': best_materials[:20],
            'total_performance_ki': len(by_dd.get('D1_adsorption_performance', [])),
        },
        'engineering_constraints': constraints[:20],
        'occurrence_patterns': occurrences[:20],
        'molecular_features_for_biomimetic_matching': sorted(molecular_features),
        'recommended_biomimetic_prototypes': sorted(recommended),
    }, flat_rows


def main():
    os.makedirs(OUT_SUM, exist_ok=True)

    all_flat = []
    all_index = []

    for poll_dir in sorted(os.listdir(BY_POLL)):
        poll_path = os.path.join(BY_POLL, poll_dir)
        if not os.path.isdir(poll_path):
            continue

        print(f"聚合: {poll_dir}...", end=' ', flush=True)
        summary, flat_rows = aggregate_pollutant(poll_dir, poll_path)

        # Save nested summary
        out_path = os.path.join(OUT_SUM, f'{poll_dir}.json')
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        # Collect flat rows
        all_flat.extend(flat_rows)

        # Index entry
        all_index.append({
            'pollutant': poll_dir,
            'papers': summary['paper_count'],
            'ki_total': summary['total_ki'],
            'performance_ki': summary['adsorption_performance']['total_performance_ki'],
            'best_material_count': len(summary['adsorption_performance']['best_materials']),
            'recommended_prototypes': summary['recommended_biomimetic_prototypes'],
            'molecular_features': summary['molecular_features_for_biomimetic_matching'],
        })

        print(f"OK ({summary['total_ki']} KI, {len(flat_rows)} perf rows)")

    # Save flat JSONL
    with open(OUT_FLAT, 'w', encoding='utf-8') as f:
        for row in all_flat:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')

    # Save index
    index_path = os.path.join(PKB, 'pollutant_aggregate_index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_pollutants': len(all_index),
            'total_papers': sum(e['papers'] for e in all_index),
            'total_ki': sum(e['ki_total'] for e in all_index),
            'total_flat_rows': len(all_flat),
            'pollutants': all_index
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Stage 2 完成:")
    print(f"   聚合摘要: {len(all_index)} 个污染物 → {OUT_SUM}/")
    print(f"   扁平数据: {len(all_flat)} 行 → {OUT_FLAT}")
    print(f"   汇总索引: {index_path}")


if __name__ == '__main__':
    main()
