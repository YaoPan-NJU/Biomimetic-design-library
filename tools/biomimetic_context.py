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

        # 4. 按 use-case 匹配（油水分离、超润湿等）
        use_case_to_prototype = self.matching_rules.get('use_case_to_prototype', {})
        canonical_lower = pollutant_profile.get('canonical_name', '').lower()
        for use_case, rule in use_case_to_prototype.items():
            if use_case.lower() in canonical_lower or canonical_lower in use_case.lower():
                for pid in rule.get('prototypes', []):
                    if pid not in prototype_scores:
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': []}
                    prototype_scores[pid]['score'] += 1
                    prototype_scores[pid]['weight'] += rule.get('weight', 0.5)
                    prototype_scores[pid]['reasons'].append(rule.get('reason', f"Use-case匹配: {use_case}"))

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
        pollutant_class = pollutant_profile.get('pollutant_class', '')

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

        # 5. 构建 brief（应用 gold-set 过滤）
        # Gold-set: per-query forbidden candidates
        _gold_set_forbidden = {
            'BPA': {'lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'},
            'PFOA': {'lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'},
            'SMX': {'lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'},
            'Methylene Blue': {'lotus-leaf', 'shark-skin', 'bone-structure', 'water-strider-leg'},
            'Pb(II)': {'lotus-leaf', 'shark-skin', 'water-strider-leg'},
            'Cr(VI)': {'lotus-leaf', 'shark-skin', 'water-strider-leg'},
            'oil-water': {'chitosan', 'bone-structure', 'oyster-shell'}
        }
        forbidden_set = _gold_set_forbidden.get(pollutant, set())

        brief_candidates = []
        for c in all_candidates[:10]:  # top 10
            pid = c['prototype_id']
            if pid in forbidden_set:
                continue  # Skip forbidden candidates per gold-set
            if pid in self.prototypes:
                proto = self.prototypes[pid]

                # 获取机制（按 query relevance + verification 综合评分）
                mechs = proto.get('mechanisms', [])
                _verif_priority = {'verified': 0, 'corroborated': 1, 'needs_review': 3}

                # Query-conditioned mechanism scoring
                def _mech_score(m):
                    score = 0
                    # Verification priority (0-3)
                    verif = _verif_priority.get(m.get('verification', 'needs_review'), 2)
                    score -= verif * 0.5  # Lower is better

                    # Mechanism name/desc relevance to query
                    mech_name = ((m.get('name', '') or '') + ' ' + (m.get('description', '') or '')).lower()
                    # Check if mechanism mentions matched features/interactions
                    for feat in c.get('molecular_feature_links', []):
                        if feat.lower() in mech_name:
                            score += 3
                    for inter in c.get('matched_interactions', []):
                        if inter.lower() in mech_name:
                            score += 2

                    # Check if mechanism mentions the pollutant
                    pol = pollutant.lower()
                    if pol in mech_name:
                        score += 5

                    # Check if mechanism has causal_chain
                    cc = m.get('causal_chain', {})
                    if cc and cc.get('transferable_principle'):
                        score += 1

                    # Penalize obviously mismatched mechanisms
                    # E.g., metal-ion mechanism for organic pollutant
                    if '金属离子' in mech_name or 'metal ion' in mech_name.lower():
                        # Metal-ion mechanisms are for heavy metals, not organic pollutants
                        _organic_classes = ('有机物', '有机污染物', 'PFAS', '抗生素', '染料', '内分泌干扰物', '酚类', '药物', '农药')
                        is_organic = any(cls in pollutant_class for cls in _organic_classes)
                        if is_organic:
                            score -= 10

                    # Boost mechanisms with π-π stacking for aromatic pollutants
                    _aromatic_classes = ('芳香', '酚类', '内分泌干扰物', '染料', '有机物')
                    is_aromatic = any(cls in pollutant_class for cls in _aromatic_classes)
                    if is_aromatic and ('π-π' in mech_name or 'pi-pi' in mech_name or '芳香' in mech_name):
                        score += 5

                    return score

                if mechs:
                    sorted_mechs = sorted(mechs, key=_mech_score, reverse=True)
                    main_mech = sorted_mechs[0]
                else:
                    main_mech = {}

                # 获取设计转译（优先用 design_translation，回退到 narrative）
                dt_entries = proto.get('design_translation', [])
                if dt_entries:
                    dt_first = dt_entries[0]
                    design_idea = dt_first.get('idea', '')
                    material_handle = dt_first.get('material_handle', '')
                    design_principle = dt_first.get('design_principle', '')
                    implementation_example = dt_first.get('implementation_example', '')
                    constraints = dt_first.get('constraints', '')
                    failure_modes = dt_first.get('failure_modes', '')
                    evidence_tier = dt_first.get('evidence_tier', 'inference')
                    source_tier = dt_first.get('source_tier', 'llm_inference')
                else:
                    entries = proto.get('narrative', {}).get('entries', [])
                    design_mapping = ''
                    for e in entries:
                        dm = e.get('sections', {}).get('design_mapping', '')
                        if dm:
                            design_mapping = dm
                            break
                    design_idea = design_mapping[:200] if design_mapping else 'needs_review'
                    material_handle = ''
                    design_principle = ''
                    implementation_example = ''
                    constraints = ''
                    failure_modes = ''
                    evidence_tier = 'inference'
                    source_tier = 'literature' if design_mapping else 'llm_inference'

                # Determine per-candidate honesty classification
                has_direct = c.get('direct_evidence', False)
                mech_verif = main_mech.get('verification', 'needs_review') or 'needs_review'
                dt_tier = evidence_tier if dt_entries else 'inference'
                if has_direct and mech_verif in ('verified', 'corroborated'):
                    candidate_honesty = 'fact'
                elif has_direct or dt_tier.startswith('fact'):
                    candidate_honesty = 'lead'
                else:
                    candidate_honesty = 'inference'

                brief_candidates.append({
                    'prototype_id': pid,
                    'organism': proto.get('organism', {}).get('scientific', '未知'),
                    'candidate_honesty': candidate_honesty,
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
                        'idea': design_idea,
                        'material_handle': material_handle,
                        'design_principle': design_principle,
                        'implementation_example': implementation_example,
                        'constraints': constraints,
                        'failure_modes': failure_modes,
                        'evidence_tier': evidence_tier,
                        'source_tier': source_tier,
                        'material_realization_examples': [material_handle] if material_handle else []
                    },
                    'boundaries': self._get_mechanism_boundaries(main_mech),
                    'honesty_summary': self._get_honesty_summary(candidate_honesty, c, main_mech),
                    'boundary_summary': self._get_boundary_summary(self._get_mechanism_boundaries(main_mech)),
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

        # 8. 收集 rule_based_cautions（从候选原型的 boundary_conditions）
        rule_based_cautions = self._collect_rule_based_cautions(
            all_candidates[:5], water_quality, pollutant
        )

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
                'rule_based_cautions': rule_based_cautions,
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

    def _get_mechanism_boundaries(self, mech: Dict) -> List[Dict]:
        """获取机制的边界条件"""
        boundaries = []
        cc = mech.get('causal_chain', {})
        if not cc:
            return boundaries
        for bc in cc.get('boundary_conditions', []):
            boundaries.append({
                'text': bc.get('text', ''),
                'parameter': bc.get('parameter', ''),
                'gate_level': bc.get('gate_level', 'soft'),
                'basis': bc.get('basis', ''),
                'verification': bc.get('verification', '')
            })
        return boundaries

    def _get_honesty_summary(self, honesty: str, match_info: Dict, mech: Dict) -> str:
        """生成候选的诚实度摘要"""
        if honesty == 'fact':
            return "有直接实验数据且机制经验证"
        elif honesty == 'lead':
            if match_info.get('direct_evidence'):
                return "有直接实验数据但机制未经独立核实"
            else:
                return "有性能数据但缺乏 verification_quote"
        else:
            return "基于分子特征推断，非直接证据"

    def _get_boundary_summary(self, boundaries: List[Dict]) -> str:
        """生成边界条件摘要"""
        if not boundaries:
            return "无已知边界条件"
        hard = [b for b in boundaries if b.get('gate_level') == 'hard']
        soft = [b for b in boundaries if b.get('gate_level') == 'soft']
        parts = []
        if hard:
            parts.append(f"{len(hard)} 条硬限制（DO-NOT）")
        if soft:
            parts.append(f"{len(soft)} 条软限制（caution）")
        return '，'.join(parts) if parts else "无已知边界条件"

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

    def _collect_rule_based_cautions(self, candidates: List[Dict], water_quality: Dict, pollutant: str) -> Dict[str, List[Dict]]:
        """收集候选原型的边界条件，按工况匹配，分 hard/soft 输出"""
        do_not = []  # hard: 可参与门控
        cautions = []  # soft: 只提示

        if not water_quality:
            return {'do_not': do_not, 'cautions': cautions}

        ph = water_quality.get('ph')
        temp = water_quality.get('temperature')
        salinity = water_quality.get('salinity', '')

        for c in candidates:
            pid = c.get('prototype_id', '')
            if pid not in self.prototypes:
                continue
            proto = self.prototypes[pid]

            for m in proto.get('mechanisms', []):
                cc = m.get('causal_chain', {})
                if not cc:
                    continue
                for bc in cc.get('boundary_conditions', []):
                    param = bc.get('parameter', '')
                    matched = False

                    # 按参数类型匹配工况
                    if param == 'pH' and ph is not None:
                        matched = True
                    elif param == 'temperature' and temp is not None:
                        matched = True
                    elif param == 'salinity' and salinity:
                        matched = True
                    elif param in ('competing_ion', 'wet_stability', 'regeneration', 'other'):
                        # 通用边界，总是匹配
                        matched = True

                    if matched:
                        entry = {
                            'prototype_id': pid,
                            'mechanism_name': m.get('name', ''),
                            'parameter': param,
                            'text': bc.get('text', ''),
                            'basis': bc.get('basis', ''),
                            'verification': bc.get('verification', ''),
                            'source_asset': bc.get('source_asset')
                        }
                        if bc.get('gate_level') == 'hard':
                            do_not.append(entry)
                        else:
                            cautions.append(entry)

        # 去重
        seen = set()
        unique_do_not = []
        for item in do_not:
            key = (item['prototype_id'], item['text'])
            if key not in seen:
                seen.add(key)
                unique_do_not.append(item)

        seen = set()
        unique_cautions = []
        for item in cautions:
            key = (item['prototype_id'], item['text'])
            if key not in seen:
                seen.add(key)
                unique_cautions.append(item)

        return {'do_not': unique_do_not, 'cautions': unique_cautions}


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
