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


def get_project_root():
    """获取项目根目录"""
    # 从 tools/biomimetic_context.py 向上两级
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BiomimeticContext:
    """ADRMATS 仿生启发检索接口"""

    def __init__(self, prototypes_db_path: str = None, feature_mapping_path: str = None, matching_rules_path: str = None, pollutant_profiles_path: str = None, pollutant_aliases_path: str = None, design_rules_path: str = None):
        # 获取项目根目录
        project_root = get_project_root()

        # 设置默认路径
        self.prototypes_db_path = prototypes_db_path or os.path.join(project_root, "prototypes_db")
        self.feature_mapping_path = feature_mapping_path or os.path.join(project_root, "feature-mapping.json")
        self.matching_rules_path = matching_rules_path or os.path.join(project_root, "feature_matching_rules.json")
        self.pollutant_profiles_path = pollutant_profiles_path or os.path.join(project_root, "pollutant_profiles.json")
        self.pollutant_aliases_path = pollutant_aliases_path or os.path.join(project_root, "pollutant_aliases.json")
        self.design_rules_path = design_rules_path or os.path.join(project_root, "docs/imported/library-enhancement/design-rules.json")

        # 加载 feature-mapping
        with open(self.feature_mapping_path, encoding='utf-8') as f:
            self.feature_mapping = json.load(f)

        # 加载匹配规则
        with open(self.matching_rules_path, encoding='utf-8') as f:
            self.matching_rules = json.load(f)

        # 加载污染物画像
        with open(self.pollutant_profiles_path, encoding='utf-8') as f:
            self.pollutant_profiles = json.load(f)

        # 加载污染物别名
        with open(self.pollutant_aliases_path, encoding='utf-8') as f:
            self.pollutant_aliases = json.load(f)

        # 加载设计规则（pending_validation 状态）
        self.design_rules = {}
        if os.path.exists(self.design_rules_path):
            with open(self.design_rules_path, encoding='utf-8') as f:
                self.design_rules = json.load(f)

        # 加载所有原型
        self.prototypes = {}
        for filename in os.listdir(self.prototypes_db_path):
            if filename.endswith('.json'):
                filepath = os.path.join(self.prototypes_db_path, filename)
                with open(filepath, encoding='utf-8') as f:
                    d = json.load(f)
                self.prototypes[d.get('id', '')] = d

    def get_pollutant_profile(self, pollutant: str) -> Dict[str, Any]:
        """获取污染物分子特征画像"""
        profiles = self.pollutant_profiles.get('profiles', {})

        # 首先通过别名查找 canonical name
        canonical = self._get_canonical_name(pollutant)

        # 精确匹配
        if canonical in profiles:
            return profiles[canonical].copy()

        # 模糊匹配
        for key, profile in profiles.items():
            if canonical.lower() in key.lower() or key.lower() in canonical.lower():
                return profile.copy()

        # 默认画像
        return {
            "canonical_name": canonical,
            "pollutant_class": "未知",
            "molecular_features": [],
            "likely_interactions": [],
            "profile_basis": "llm_inference"
        }

    def _get_canonical_name(self, pollutant: str) -> str:
        """通过别名获取 canonical name"""
        aliases_data = self.pollutant_aliases.get('aliases', {})

        for canonical, info in aliases_data.items():
            alias_list = info.get('aliases', [])
            if pollutant in alias_list or pollutant.lower() in [a.lower() for a in alias_list]:
                return canonical

        return pollutant

    def find_direct_evidence(self, pollutant: str) -> List[Dict[str, Any]]:
        """查找有直接实验数据的原型"""
        candidates = []

        ppm = self.feature_mapping.get('pollutant_prototype_map', {})

        # 从 JSON 文件获取别名
        canonical = self._get_canonical_name(pollutant)
        aliases_data = self.pollutant_aliases.get('aliases', {})

        # 获取所有可能的别名
        aliases = [pollutant]
        for canon, info in aliases_data.items():
            alias_list = info.get('aliases', [])
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

    def find_applicable_rules(self, water_quality: Dict[str, Any] = None, pollutant: str = None) -> List[Dict[str, Any]]:
        """查找适用的设计规则（pending_validation 状态）"""
        if not water_quality or not self.design_rules:
            return []

        applicable_rules = []
        rules = self.design_rules.get('condition_mechanism_rules', [])

        for rule in rules:
            condition = rule.get('condition', {})
            param = condition.get('parameter', '').lower()
            operator = condition.get('operator', '')
            value = condition.get('value', [])

            # 检查 pH 条件
            if param == 'ph' and 'ph' in water_quality:
                ph = water_quality['ph']
                if operator == 'range' and len(value) == 2:
                    if value[0] <= ph <= value[1]:
                        applicable_rules.append({
                            'rule_id': rule.get('rule_id'),
                            'title': rule.get('title'),
                            'title_zh': rule.get('title_zh', ''),
                            'behavior': rule.get('behavior', ''),
                            'behavior_zh': rule.get('behavior_zh', ''),
                            'affected_prototypes': rule.get('affected_prototypes', []),
                            'confidence': rule.get('confidence', 0.5),
                            'validation_status': 'pending_validation'
                        })
                elif operator == 'threshold' and len(value) == 1:
                    if ph < value[0]:
                        applicable_rules.append({
                            'rule_id': rule.get('rule_id'),
                            'title': rule.get('title'),
                            'title_zh': rule.get('title_zh', ''),
                            'behavior': rule.get('behavior', ''),
                            'behavior_zh': rule.get('behavior_zh', ''),
                            'affected_prototypes': rule.get('affected_prototypes', []),
                            'confidence': rule.get('confidence', 0.5),
                            'validation_status': 'pending_validation'
                        })

            # 检查温度条件
            elif param == 'temperature' and 'temperature' in water_quality:
                temp = water_quality['temperature']
                if operator == 'range' and len(value) == 2:
                    if value[0] <= temp <= value[1]:
                        applicable_rules.append({
                            'rule_id': rule.get('rule_id'),
                            'title': rule.get('title'),
                            'title_zh': rule.get('title_zh', ''),
                            'behavior': rule.get('behavior', ''),
                            'behavior_zh': rule.get('behavior_zh', ''),
                            'affected_prototypes': rule.get('affected_prototypes', []),
                            'confidence': rule.get('confidence', 0.5),
                            'validation_status': 'pending_validation'
                        })

        return applicable_rules

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

                # 获取机制（按 verification 优先级排序：verified > corroborated > 其他 > needs_review）
                mechs = proto.get('mechanisms', [])
                _verif_priority = {'verified': 0, 'corroborated': 1, 'needs_review': 3}
                sorted_mechs = sorted(mechs, key=lambda m: _verif_priority.get(m.get('verification', 'needs_review'), 2))
                main_mech = sorted_mechs[0] if sorted_mechs else {}

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
                            'verification_tier': main_mech.get('verification', 'needs_review') or 'needs_review',
                            'confidence': 'low' if (main_mech.get('verification', 'needs_review') or 'needs_review') == 'needs_review' else 'normal'
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
            pid = c['prototype_id']
            if c.get('direct_evidence'):
                # 检查该候选展示的主机制 verification
                if pid in self.prototypes:
                    proto_check = self.prototypes[pid]
                    mechs_check = proto_check.get('mechanisms', [])
                    sorted_check = sorted(mechs_check, key=lambda m: _verif_priority.get(m.get('verification', 'needs_review'), 2))
                    top_mech_check = sorted_check[0] if sorted_check else {}
                    if top_mech_check.get('verification') == 'needs_review':
                        inferences.append(f"{pid}: 有直接实验数据但机制未经核实，置信度低")
                    else:
                        leads.append(f"{pid}: 有直接实验数据，但未经独立核实")
                else:
                    leads.append(f"{pid}: 有直接实验数据，但未经独立核实")
            else:
                inferences.append(f"{pid}: 基于分子特征推断，非直接证据")

        # 7. 查找适用规则（pending_validation）
        applicable_rules = self.find_applicable_rules(water_quality, pollutant)

        return {
            'brief': {
                'context': {
                    'water_quality': water_quality or {},
                    'removal_target': {'污染物': pollutant},
                    'pollutant_profile': pollutant_profile,
                    'engineering_constraints': engineering_constraints or []
                },
                'candidates': brief_candidates,
                'applicable_rules': applicable_rules,
                'honesty_ledger': {
                    'facts': facts,
                    'leads': leads,
                    'inferences': inferences
                }
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
            if not pol or not pol.strip():
                continue  # 空 pollutant 不参与匹配
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
    print(f"候选原型数: {len(brief['brief']['candidates'])}")
    for c in brief['brief']['candidates']:
        print(f"  - {c['prototype_id']}: {c['match']['match_basis']} (direct_evidence={c['match']['direct_evidence']})")

    # 测试 2: feature-based 查询
    print("\n=== 测试 2: PFOA feature-based ===")
    brief = ctx.query(
        pollutant="PFOA",
        water_quality={"pH": 7.0, "temperature": 25, "salinity": "medium"},
        engineering_constraints=["水稳定性"]
    )
    print(f"候选原型数: {len(brief['brief']['candidates'])}")
    for c in brief['brief']['candidates']:
        print(f"  - {c['prototype_id']}: {c['match']['match_basis']} (direct_evidence={c['match']['direct_evidence']})")


if __name__ == "__main__":
    main()
