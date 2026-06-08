#!/usr/bin/env python3
"""
BiomimeticContext 接口
ADRMATS 对抗设计模块的仿生启发检索接口

用法:
    from biomimetic_context import BiomimeticContext

    ctx = BiomimeticContext()

    # 查询 1: direct evidence (有直接实验数据)
    brief = ctx.query(
        pollutant="Pb(II)",
        water_quality={"pH": 6.0, "temperature": 25, "salinity": "low"},
        engineering_constraints=["水稳定性", "可回收性"]
    )

    # 查询 2: feature-based inspiration (基于分子特征)
    brief = ctx.query(
        pollutant="PFOA",
        water_quality={"pH": 7.0, "temperature": 25, "salinity": "medium"},
        engineering_constraints=["水稳定性"]
    )
"""

import json
import os
from typing import Dict, List, Optional, Any


# 污染物分子特征画像数据库
POLLUTANT_PROFILES = {
    "Pb(II)": {
        "canonical_name": "Pb(II)",
        "pollutant_class": "重金属",
        "molecular_features": ["二价阳离子", "软酸", "高电荷密度", "可与含硫/氮配体配位"],
        "likely_interactions": ["配位", "静电吸引", "离子交换", "络合"],
        "profile_basis": "database"
    },
    "PFOA": {
        "canonical_name": "PFOA（Perfluorooctanoic acid）",
        "pollutant_class": "PFASs（全氟和多氟烷基物质）",
        "molecular_features": ["长链全氟烷基", "羧酸基团", "疏水性", "两亲性", "化学稳定性"],
        "likely_interactions": ["疏水分配", "氢键", "静电吸引", "孔道限域"],
        "profile_basis": "database"
    },
    "BPA": {
        "canonical_name": "BPA（Bisphenol A）",
        "pollutant_class": "内分泌干扰物/酚类化合物",
        "molecular_features": ["芳香环", "酚羟基", "疏水性", "弱酸性"],
        "likely_interactions": ["氢键", "π-π堆积", "疏水分配", "静电吸引"],
        "profile_basis": "database"
    },
    "TC": {
        "canonical_name": "TC（Tetracycline）",
        "pollutant_class": "抗生素",
        "molecular_features": ["芳香环", "酚羟基", "酰胺基", "二甲氨基", "弱碱性"],
        "likely_interactions": ["氢键", "π-π堆积", "静电吸引", "配位"],
        "profile_basis": "database"
    },
    "SMX": {
        "canonical_name": "SMX（Sulfamethoxazole）",
        "pollutant_class": "抗生素/磺胺类",
        "molecular_features": ["芳香环", "磺酰胺基", "异恶唑环", "弱酸性"],
        "likely_interactions": ["氢键", "π-π堆积", "静电吸引", "疏水分配"],
        "profile_basis": "database"
    },
    "TCE": {
        "canonical_name": "TCE（Trichloroethylene）",
        "pollutant_class": "卤代烃/VOCs",
        "molecular_features": ["氯代烯烃", "疏水性", "挥发性", "弱极性"],
        "likely_interactions": ["疏水分配", "π-π堆积", "孔道限域"],
        "profile_basis": "database"
    },
    "MB": {
        "canonical_name": "MB（Methylene Blue）",
        "pollutant_class": "阳离子染料",
        "molecular_features": ["芳香环", "正电荷", "平面结构", "水溶性"],
        "likely_interactions": ["静电吸引", "π-π堆积", "氢键"],
        "profile_basis": "database"
    },
    "Cr(VI)": {
        "canonical_name": "Cr(VI)",
        "pollutant_class": "重金属",
        "molecular_features": ["六价铬", "含氧阴离子", "强氧化性"],
        "likely_interactions": ["静电吸引", "还原沉淀", "配位"],
        "profile_basis": "database"
    },
    "Hg(II)": {
        "canonical_name": "Hg(II)",
        "pollutant_class": "重金属",
        "molecular_features": ["二价阳离子", "软酸", "高亲硫性"],
        "likely_interactions": ["配位", "离子交换", "沉淀"],
        "profile_basis": "database"
    },
    "Cd(II)": {
        "canonical_name": "Cd(II)",
        "pollutant_class": "重金属",
        "molecular_features": ["二价阳离子", "软酸", "中等电荷密度"],
        "likely_interactions": ["配位", "静电吸引", "离子交换"],
        "profile_basis": "database"
    }
}


class BiomimeticContext:
    """ADRMATS 仿生启发检索接口"""

    def __init__(self, prototypes_db_path: str = "prototypes_db", feature_mapping_path: str = "feature-mapping.json", matching_rules_path: str = "feature_matching_rules.json"):
        self.prototypes_db_path = prototypes_db_path
        self.feature_mapping_path = feature_mapping_path
        self.matching_rules_path = matching_rules_path

        # 加载 feature-mapping
        with open(feature_mapping_path, encoding='utf-8') as f:
            self.feature_mapping = json.load(f)

        # 加载匹配规则
        with open(matching_rules_path, encoding='utf-8') as f:
            self.matching_rules = json.load(f)

        # 加载所有原型
        self.prototypes = {}
        for filename in os.listdir(prototypes_db_path):
            if filename.endswith('.json'):
                filepath = os.path.join(prototypes_db_path, filename)
                with open(filepath, encoding='utf-8') as f:
                    d = json.load(f)
                self.prototypes[d.get('id', '')] = d

    def get_pollutant_profile(self, pollutant: str) -> Dict[str, Any]:
        """获取污染物分子特征画像"""
        # 精确匹配
        if pollutant in POLLUTANT_PROFILES:
            return POLLUTANT_PROFILES[pollutant].copy()

        # 模糊匹配
        for key, profile in POLLUTANT_PROFILES.items():
            if pollutant.lower() in key.lower() or key.lower() in pollutant.lower():
                return profile.copy()

        # 默认画像
        return {
            "canonical_name": pollutant,
            "pollutant_class": "未知",
            "molecular_features": [],
            "likely_interactions": [],
            "profile_basis": "llm_inference"
        }

    def find_direct_evidence(self, pollutant: str) -> List[Dict[str, Any]]:
        """查找有直接实验数据的原型"""
        candidates = []

        ppm = self.feature_mapping.get('pollutant_prototype_map', {})

        # 污染物别名映射（用于匹配）
        pollutant_aliases = {
            'Pb(II)': ['Pb(II)', 'Pb²⁺', 'Pb2+', 'Pb'],
            'Cd(II)': ['Cd(II)', 'Cd²⁺', 'Cd2+', 'Cd'],
            'Hg(II)': ['Hg(II)', 'Hg²⁺', 'Hg2+', 'Hg'],
            'Cu(II)': ['Cu(II)', 'Cu²⁺', 'Cu2+', 'Cu'],
            'Cr(VI)': ['Cr(VI)', 'Cr⁶⁺', 'Cr'],
            'As(V)': ['As(V)', 'As(III)', 'As'],
            'U(VI)': ['U(VI)', 'U'],
        }

        # 获取所有可能的别名
        aliases = [pollutant]
        for canonical, alias_list in pollutant_aliases.items():
            if pollutant in alias_list or pollutant.lower() in [a.lower() for a in alias_list]:
                aliases = alias_list
                break

        def matches_pollutant(text):
            """检查文本是否包含目标污染物"""
            if not text:
                return False
            text_lower = text.lower()
            return any(alias.lower() in text_lower for alias in aliases)

        def search_prototypes(obj, path=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'prototypes' and isinstance(v, list):
                        for p in v:
                            if isinstance(p, dict) and 'id' in p:
                                # 检查是否匹配污染物
                                if matches_pollutant(str(p.get('mechanism_summary', ''))):
                                    candidates.append({
                                        'prototype_id': p['id'],
                                        'weight': p.get('weight', 0.5),
                                        'reason': p.get('mechanism_summary', ''),
                                        'design_hint': p.get('design_hint', ''),
                                        'match_basis': 'direct_pollutant_evidence',
                                        'direct_evidence': True
                                    })
                    elif isinstance(v, (dict, list)):
                        search_prototypes(v, f"{path}.{k}")
                # 检查 key 是否匹配
                if isinstance(k, str) and matches_pollutant(k):
                    if isinstance(v, dict) and 'prototypes' in v:
                        for p in v['prototypes']:
                            if isinstance(p, dict) and 'id' in p:
                                candidates.append({
                                    'prototype_id': p['id'],
                                    'weight': p.get('weight', 0.5),
                                    'reason': p.get('mechanism_summary', ''),
                                    'design_hint': p.get('design_hint', ''),
                                    'match_basis': 'direct_pollutant_evidence',
                                    'direct_evidence': True
                                })
            elif isinstance(obj, list):
                for v in obj:
                    search_prototypes(v, path)

        search_prototypes(ppm)

        # 去重
        seen = set()
        unique_candidates = []
        for c in candidates:
            if c['prototype_id'] not in seen:
                seen.add(c['prototype_id'])
                unique_candidates.append(c)

        return unique_candidates

    def find_feature_based(self, pollutant_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """基于分子特征查找匹配的原型"""
        candidates = []

        molecular_features = pollutant_profile.get('molecular_features', [])
        likely_interactions = pollutant_profile.get('likely_interactions', [])
        pollutant_class = pollutant_profile.get('pollutant_class', '')

        # 从数据化规则加载映射
        feature_to_prototype = self.matching_rules.get('molecular_feature_to_prototype', {})
        interaction_to_prototype = self.matching_rules.get('interaction_to_prototype', {})
        class_to_prototype = self.matching_rules.get('pollutant_class_to_prototype', {})

        # 收集匹配的原型
        prototype_scores = {}

        # 1. 按分子特征匹配
        for feature in molecular_features:
            if feature in feature_to_prototype:
                rule = feature_to_prototype[feature]
                for pid in rule.get('prototypes', []):
                    if pid not in prototype_scores:
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': []}
                    prototype_scores[pid]['score'] += 1
                    prototype_scores[pid]['weight'] += rule.get('weight', 0.5)
                    prototype_scores[pid]['features'].append(feature)
                    prototype_scores[pid]['reasons'].append(rule.get('reason', ''))

        # 2. 按相互作用匹配
        for interaction in likely_interactions:
            if interaction in interaction_to_prototype:
                rule = interaction_to_prototype[interaction]
                for pid in rule.get('prototypes', []):
                    if pid not in prototype_scores:
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': []}
                    prototype_scores[pid]['score'] += 1
                    prototype_scores[pid]['weight'] += rule.get('weight', 0.5)
                    prototype_scores[pid]['interactions'].append(interaction)
                    prototype_scores[pid]['reasons'].append(rule.get('reason', ''))

        # 3. 按污染物类别匹配
        for class_name, rule in class_to_prototype.items():
            if class_name in pollutant_class:
                for pid in rule.get('prototypes', []):
                    if pid not in prototype_scores:
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': []}
                    prototype_scores[pid]['score'] += 1
                    prototype_scores[pid]['weight'] += rule.get('weight', 0.5)
                    prototype_scores[pid]['reasons'].append(f"污染物类别匹配: {class_name}")

        # 转换为候选列表
        for pid, score_info in prototype_scores.items():
            if score_info['score'] >= 1:  # 至少匹配 1 个特征
                avg_weight = score_info['weight'] / score_info['score']
                reason = score_info['reasons'][0] if score_info['reasons'] else "分子特征匹配"
                candidates.append({
                    'prototype_id': pid,
                    'weight': min(avg_weight, 0.9),
                    'reason': reason,
                    'match_basis': 'molecular_feature_inference',
                    'direct_evidence': False,
                    'molecular_feature_links': score_info['features'][:5]
                })

        # 按权重排序
        candidates.sort(key=lambda x: x['weight'], reverse=True)

        return candidates[:10]  # 返回 top 10

    def query(self, pollutant: str, water_quality: Dict[str, Any] = None, engineering_constraints: List[str] = None) -> Dict[str, Any]:
        """查询接口：输入污染物和工况，输出 brief"""

        # 1. 获取污染物画像
        pollutant_profile = self.get_pollutant_profile(pollutant)

        # 2. 查找 direct evidence
        direct_candidates = self.find_direct_evidence(pollutant)

        # 3. 查找 feature-based inspiration
        feature_candidates = self.find_feature_based(pollutant_profile)

        # 4. 合并候选（direct evidence 优先）
        all_candidates = []
        seen_ids = set()

        for c in direct_candidates:
            if c['prototype_id'] not in seen_ids:
                seen_ids.add(c['prototype_id'])
                all_candidates.append(c)

        for c in feature_candidates:
            if c['prototype_id'] not in seen_ids:
                seen_ids.add(c['prototype_id'])
                all_candidates.append(c)

        # 5. 构建 brief
        brief_candidates = []
        for c in all_candidates[:10]:  # top 10
            pid = c['prototype_id']
            if pid in self.prototypes:
                proto = self.prototypes[pid]

                # 获取机制
                mechs = proto.get('mechanisms', [])
                main_mech = mechs[0] if mechs else {}

                # 获取设计转译
                entries = proto.get('narrative', {}).get('entries', [])
                design_mapping = ''
                for e in entries:
                    dm = e.get('sections', {}).get('design_mapping', '')
                    if dm:
                        design_mapping = dm
                        break

                brief_candidates.append({
                    'prototype_id': pid,
                    'organism': proto.get('organism', {}).get('scientific', '未知'),
                    'match': {
                        'reason': c.get('reason', ''),
                        'weight': c.get('weight', 0.5),
                        'applicability_fit': self._get_applicability(proto),
                        'match_basis': c.get('match_basis', 'unknown'),
                        'direct_evidence': c.get('direct_evidence', False)
                    },
                    'mechanism': {
                        'name': main_mech.get('name', '未知'),
                        '基本原理': main_mech.get('基本原理', 'needs_review'),
                        'key_structures': main_mech.get('key_structures', []),
                        'functional_groups': main_mech.get('functional_groups', []),
                        'molecular_feature_links': c.get('molecular_feature_links', []),
                        'attribution': {
                            'source': main_mech.get('source', 'unknown'),
                            'ref': main_mech.get('ref_doi', main_mech.get('ref', '')),
                            'verification_tier': 'single_source'
                        }
                    },
                    'design_translation': {
                        'idea': design_mapping[:200] if design_mapping else 'needs_review',
                        'material_realization_examples': [],
                        'source_tier': 'literature' if design_mapping else 'llm_inference'
                    },
                    'evidence_context': {
                        'performance_leads': self._get_performance_leads(proto, pollutant)
                    }
                })

        # 6. 构建 honesty_ledger
        facts = []
        leads = []
        inferences = []

        if direct_candidates:
            facts.append(f"有 {len(direct_candidates)} 个原型对 {pollutant} 有直接实验数据")

        for c in all_candidates[:5]:
            if c.get('direct_evidence'):
                leads.append(f"{c['prototype_id']}: 有直接实验数据，但未经独立核实")
            else:
                inferences.append(f"{c['prototype_id']}: 基于分子特征推断，非直接证据")

        return {
            'context': {
                'water_quality': water_quality or {},
                'removal_target': {'污染物': pollutant},
                'pollutant_profile': pollutant_profile,
                'engineering_constraints': engineering_constraints or []
            },
            'candidates': brief_candidates,
            'honesty_ledger': {
                'facts': facts,
                'leads': leads,
                'inferences': inferences
            }
        }

    def _get_applicability(self, proto: Dict) -> str:
        """获取原型的适用条件"""
        tested = proto.get('tested_conditions', {})
        ph = tested.get('tested_ph_range', [])
        temp = tested.get('tested_temp_range', [])
        salinity = tested.get('salinity', 'any')

        parts = []
        if ph:
            parts.append(f"pH {ph[0]}-{ph[1]}")
        if temp:
            parts.append(f"温度 {temp[0]}-{temp[1]}°C")
        parts.append(f"盐度 {salinity}")

        return ', '.join(parts)

    def _get_performance_leads(self, proto: Dict, pollutant: str) -> List[Dict]:
        """获取性能线索"""
        leads = []

        for p in proto.get('performance_data', []):
            pol = p.get('pollutant', '')
            if pollutant.lower() in pol.lower() or pol.lower() in pollutant.lower():
                leads.append({
                    'pollutant': pol,
                    'material': p.get('material', ''),
                    'value': p.get('value', ''),
                    'unit': p.get('unit', ''),
                    'verification_tier': p.get('verification', 'unverified')
                })

        return leads[:5]  # 返回 top 5


def main():
    """测试接口"""
    ctx = BiomimeticContext()

    # 测试 1: direct evidence 查询
    print("=== 测试 1: Pb(II) direct evidence ===")
    brief = ctx.query(
        pollutant="Pb(II)",
        water_quality={"pH": 6.0, "temperature": 25, "salinity": "low"},
        engineering_constraints=["水稳定性", "可回收性"]
    )
    print(f"候选原型数: {len(brief['candidates'])}")
    for c in brief['candidates']:
        print(f"  - {c['prototype_id']}: {c['match']['match_basis']} (direct_evidence={c['match']['direct_evidence']})")

    # 测试 2: feature-based 查询
    print("\n=== 测试 2: PFOA feature-based ===")
    brief = ctx.query(
        pollutant="PFOA",
        water_quality={"pH": 7.0, "temperature": 25, "salinity": "medium"},
        engineering_constraints=["水稳定性"]
    )
    print(f"候选原型数: {len(brief['candidates'])}")
    for c in brief['candidates']:
        print(f"  - {c['prototype_id']}: {c['match']['match_basis']} (direct_evidence={c['match']['direct_evidence']})")


if __name__ == "__main__":
    main()
