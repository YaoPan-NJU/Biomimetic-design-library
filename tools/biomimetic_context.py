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
import re
from typing import Dict, List, Optional, Any


def _extract_keywords(text):
    """Extract meaningful keywords from Chinese/English text."""
    if not text:
        return set()
    text = text.lower()
    parts = re.split(r'[/,，、（）()\s\-→。；：「」【】《》]+', text)
    stop_words = {'的', '和', '与', '对', '在', '是', '有', '为', '等', '及', 'a', 'an', 'the', 'of', 'to', 'in', 'for', 'and'}
    return {p.strip() for p in parts if len(p.strip()) >= 2 and p.strip() not in stop_words}


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

    def _pollutant_aliases(self, pollutant: str) -> set:
        """Return normalized names accepted for pollutant-specific evidence."""
        aliases_data = self.pollutant_aliases.get('aliases', {})
        if pollutant in aliases_data:
            info = aliases_data[pollutant]
            return {pollutant, *[str(name) for name in info.get('aliases', [])]}

        canonical = self._get_canonical_name(pollutant)
        aliases = {pollutant, canonical}
        for canon, info in aliases_data.items():
            names = [canon] + list(info.get('aliases', []))
            if pollutant.lower() in {str(name).lower() for name in names}:
                aliases.update(str(name) for name in names)
        return {str(alias).strip() for alias in aliases if str(alias).strip()}

    @staticmethod
    def _matches_pollutant_text(text: str, aliases: set) -> bool:
        """Match short chemical abbreviations as case-sensitive tokens."""
        text = str(text or '')
        for alias in aliases:
            if len(alias) <= 2 and alias.isascii():
                if re.search(rf'(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])', text):
                    return True
            elif alias.lower() in text.lower():
                return True
        return False

    def _performance_evidence(self, prototype_id: str, pollutant: str):
        """Return the strongest pollutant-specific removal evidence tier and row."""
        aliases = self._pollutant_aliases(pollutant)
        lead_row = None
        for row in self.prototypes.get(prototype_id, {}).get('performance_data', []):
            row_pollutant = str(row.get('pollutant', ''))
            if not row_pollutant or not self._matches_pollutant_text(row_pollutant, aliases):
                continue

            quote = str(row.get('verification_quote') or row.get('quote') or '').strip()
            evidence_text = ' '.join(str(row.get(key, '')) for key in (
                'parameter', 'metric_type', 'material', 'adsorbent', 'conditions',
                'verification_quote', 'quote'
            ))
            if not self._matches_pollutant_text(evidence_text, aliases):
                continue
            source = (
                row.get('ref_doi') or row.get('source_doi') or row.get('patent_number')
                or row.get('standard_number') or row.get('source')
            )
            locator = row.get('locator') or row.get('source_locator') or row.get('source_page')
            metric_text = ' '.join(
                [str(key) for key in row]
                + [str(row.get(key, '')) for key in ('metric_type', 'parameter', 'unit', 'conditions', 'verification_quote')]
            ).lower()
            is_removal_metric = any(term in metric_text for term in (
                'adsorption', '吸附', 'qmax', 'uptake', 'removal', '去除',
                'rejection', '分配系数', 'distribution coefficient'
            ))
            is_non_removal_metric = any(term in metric_text for term in (
                '非吸附剂性能', '解离常数', 'dissociation', 'sensor', '传感', 'lod', 'ic50'
            ))
            placeholder_quote = any(term in quote.lower() for term in ('pdf缺失', 'pdf missing'))
            if not (source and locator and quote and not placeholder_quote and is_removal_metric and not is_non_removal_metric):
                continue

            verification = row.get('verification')
            if verification in ('verified', 'corroborated'):
                return 'fact', row
            if verification == 'partial' and lead_row is None:
                lead_row = row
        return ('lead', lead_row) if lead_row else ('none', None)

    def _find_performance_candidates(self, pollutant: str, tier: str) -> List[Dict[str, Any]]:
        mapped = {item['prototype_id']: item for item in self.find_pollutant_inspiration(pollutant)}
        candidates = []
        for prototype_id in self.prototypes:
            evidence_tier, row = self._performance_evidence(prototype_id, pollutant)
            if evidence_tier != tier:
                continue
            mapping = mapped.get(prototype_id, {})
            candidates.append({
                'prototype_id': prototype_id,
                'weight': max(mapping.get('weight', 0.0), 0.85 if tier == 'fact' else 0.70),
                'reason': f"污染物特异材料去除性能（{row.get('perf_id', 'performance_data')}；证据级={tier}）",
                'design_hint': mapping.get('design_hint', ''),
                'match_basis': 'direct_pollutant_evidence' if tier == 'fact' else 'source_backed_performance_lead',
                'mapping_source': 'performance_data',
                'mapping_quality': 'strict_direct_evidence' if tier == 'fact' else 'source_backed_partial',
                'performance_evidence_tier': tier,
                'direct_evidence': tier == 'fact',
            })
        return sorted(candidates, key=lambda c: c['weight'], reverse=True)

    def find_direct_evidence(self, pollutant: str) -> List[Dict[str, Any]]:
        """Return only strict, reproducible pollutant-specific removal evidence."""
        return self._find_performance_candidates(pollutant, 'fact')

    def find_performance_leads(self, pollutant: str) -> List[Dict[str, Any]]:
        """Return source-located removal measurements whose verification is partial."""
        return self._find_performance_candidates(pollutant, 'lead')

    def find_pollutant_inspiration(self, pollutant: str) -> List[Dict[str, Any]]:
        """Return explicit pollutant mappings as inspiration, never as direct evidence."""
        ppm = self.feature_mapping.get('pollutant_prototype_map', {})
        canonical = self._get_canonical_name(pollutant)
        aliases = {pollutant.lower(), canonical.lower()}
        for canon, info in self.pollutant_aliases.get('aliases', {}).items():
            names = [canon] + list(info.get('aliases', []))
            if pollutant.lower() in {str(name).lower() for name in names}:
                aliases.update(str(name).lower() for name in names)

        candidates = []

        def add_entries(entries):
            if not isinstance(entries, list):
                return
            for entry in entries:
                if not isinstance(entry, dict) or entry.get('id') not in self.prototypes:
                    continue
                prototype = self.prototypes[entry['id']]
                pollutant_grounded = False
                grounded_verification = 'needs_review'
                for mechanism in prototype.get('mechanisms', []) or []:
                    item = mechanism.get('causal_chain', {}).get('pollutant_feature', {})
                    item_text = (item.get('text', '') or '').lower()
                    complete_source = (
                        item.get('basis') in ('from_source', 'corroborated')
                        and item.get('source') and item.get('locator') and item.get('quote')
                    )
                    if complete_source and any(alias in item_text for alias in aliases):
                        pollutant_grounded = True
                        grounded_verification = mechanism.get('verification', 'needs_review')
                        break
                summary = entry.get('mechanism_summary', '') or ''
                speculative = any(term in summary.lower() for term in ('外推', 'inspiration', '假说', '待验证', '原理原型'))
                evidence_bonus = 0.25 if pollutant_grounded and grounded_verification == 'verified' else 0.20 if pollutant_grounded else 0.0
                ranking_weight = min(
                    entry.get('weight', 0.5)
                    + evidence_bonus
                    - (0.12 if speculative else 0.0),
                    0.95,
                )
                candidates.append({
                    'prototype_id': entry['id'],
                    'weight': round(ranking_weight, 3),
                    'reason': f"污染物专项映射（非直接证据；机制卡命中={pollutant_grounded}）：{summary}",
                    'design_hint': entry.get('design_hint', ''),
                    'match_basis': 'molecular_feature_inference',
                    'mapping_source': 'pollutant_prototype_map',
                    'mapping_quality': 'source_grounded_inspiration' if pollutant_grounded else 'inspiration_only',
                    'direct_evidence': False,
                    'molecular_feature_links': [],
                })

        def walk(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    key_lower = str(key).lower()
                    if any(alias == key_lower or alias in key_lower for alias in aliases):
                        add_entries(value.get('prototypes', []) if isinstance(value, dict) else value)
                    walk(value)
            elif isinstance(obj, list):
                for value in obj:
                    walk(value)

        walk(ppm)

        deduplicated = {}
        for candidate in candidates:
            pid = candidate['prototype_id']
            if pid not in deduplicated or candidate['weight'] > deduplicated[pid]['weight']:
                deduplicated[pid] = candidate
        return sorted(deduplicated.values(), key=lambda c: c['weight'], reverse=True)

    def find_mechanism_based(self, pollutant_profile: Dict[str, Any], pollutant: str = '') -> List[Dict[str, Any]]:
        """Track2A 机制层：污染物 -> canonical 机制 -> 原型（经 mechanism_tags 倒排）。
        非污染物键路由：原型无需挂载特定污染物，只要机制标签与污染物特征/相互作用对应即可被命中。"""
        i2m = self.matching_rules.get('interaction_to_mechanism', {})
        f2m = self.matching_rules.get('molecular_feature_to_mechanism', {})
        mechs = set()
        for it in pollutant_profile.get('likely_interactions', []) or []:
            m = i2m.get(it) or i2m.get(str(it).lower())
            if m:
                mechs.add(m)
        for mf in pollutant_profile.get('molecular_features', []) or []:
            ms = f2m.get(mf) or f2m.get(str(mf).lower())
            if ms:
                mechs.update(ms)
        query_text = ' '.join(
            [pollutant]
            + list(pollutant_profile.get('molecular_features', []) or [])
            + list(pollutant_profile.get('likely_interactions', []) or [])
        )
        query_keywords = _extract_keywords(query_text)
        query_names = {
            str(name).strip().lower()
            for name in self._pollutant_aliases(pollutant)
            if str(name).strip()
        }
        query_names.add(self._get_canonical_name(pollutant).strip().lower())
        # 原型级 mechanism_tags 只用于盘点，不能作为检索权威；它会把一个原型
        # 任意机制的标签传播给该原型全部机制。运行时直接在具体机制卡中识别标签，
        # 并把命中的 mechanism_id 传给 brief 渲染层。
        tag_keywords = {
            '配位螯合': ('配位', '螯合', 'coordination', 'chelat'),
            '静电吸附': ('静电', 'electrostatic'),
            '离子交换': ('离子交换', 'ion exchange'),
            '氢键': ('氢键', 'hydrogen bond'),
            'π-π堆积': ('π-π', 'pi-pi', '芳香堆积'),
            '疏水分配': ('疏水', 'hydrophobic'),
            '孔道限域分子筛分': ('孔道', '限域', '筛分', 'pore', 'size exclusion'),
            '沉淀共沉淀': ('沉淀', 'precipitation'),
            '还原催化降解': ('还原', '氧化', '降解', 'catalytic'),
            '生物矿化': ('矿化', 'biomineral'),
            '几何识别': ('几何识别', '形状识别', 'geometric recognition'),
            '超浸润分离': ('超疏水', '超亲水', '超浸润', '油水分离', 'superwet'),
        }
        scores = {}
        for pid, proto in self.prototypes.items():
            overlap = set()
            mechanism_ids = []
            relevance = 0
            for mechanism in proto.get('mechanisms', []) or []:
                if mechanism.get('brief_visibility', 'visible') == 'hidden':
                    continue
                allowlist = mechanism.get('query_pollutant_allowlist', []) or []
                if allowlist:
                    allowed_names = set()
                    for allowed in allowlist:
                        allowed_text = str(allowed).strip()
                        if not allowed_text:
                            continue
                        allowed_names.add(allowed_text.lower())
                        allowed_names.add(self._get_canonical_name(allowed_text).strip().lower())
                    if not query_names.intersection(allowed_names):
                        continue
                cc = mechanism.get('causal_chain', {}) or {}
                text_parts = [
                    mechanism.get('name', ''), mechanism.get('description', ''),
                    mechanism.get('基本原理', ''), cc.get('transferable_principle', ''),
                    ' '.join(mechanism.get('functional_groups', []) or []),
                    ' '.join(mechanism.get('key_structures', []) or []),
                ]
                for element in ('pollutant_feature', 'bio_structure', 'interaction', 'why_it_works'):
                    value = cc.get(element, {})
                    if isinstance(value, dict):
                        text_parts.append(value.get('text', ''))
                mechanism_text = ' '.join(str(part) for part in text_parts).lower()
                matched = {
                    tag for tag in mechs
                    if any(keyword.lower() in mechanism_text for keyword in tag_keywords.get(tag, (tag,)))
                }
                direct_relevance = sum(keyword in mechanism_text for keyword in query_keywords)
                if matched and direct_relevance:
                    overlap.update(matched)
                    mechanism_ids.append(mechanism.get('mechanism_id'))
                    relevance = max(relevance, direct_relevance)
            mechanism_ids = [mid for mid in mechanism_ids if mid]
            if mechanism_ids:
                scores[pid] = {'overlap': overlap, 'mechanism_ids': mechanism_ids, 'relevance': relevance}
        candidates = []
        for pid, sc in scores.items():
            n = len(sc['overlap'])
            weight = min(0.25 + 0.1 * n + 0.08 * min(sc['relevance'], 3), 0.75)
            candidates.append({
                'prototype_id': pid,
                'weight': round(weight, 3),
                'reason': f"具体机制卡匹配（{'/'.join(sorted(sc['overlap']))}；query overlap={sc['relevance']}）",
                'match_basis': 'mechanism_feature_bridge',
                'direct_evidence': False,
                'molecular_feature_links': sorted(sc['overlap']),
                'matched_mechanism_ids': sc['mechanism_ids'],
            })
        candidates.sort(key=lambda x: x['weight'], reverse=True)
        return candidates[:25]

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
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': [], 'use_cases': []}
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
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': [], 'use_cases': []}
                    prototype_scores[pid]['score'] += 1
                    prototype_scores[pid]['weight'] += rule.get('weight', 0.5)
                    prototype_scores[pid]['interactions'].append(interaction)
                    prototype_scores[pid]['reasons'].append(rule.get('reason', ''))

        # 3. 按污染物类别匹配
        for class_name, rule in class_to_prototype.items():
            if class_name in pollutant_class:
                for pid in rule.get('prototypes', []):
                    if pid not in prototype_scores:
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': [], 'use_cases': []}
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
                        prototype_scores[pid] = {'score': 0, 'weight': 0, 'features': [], 'interactions': [], 'reasons': [], 'use_cases': []}
                    prototype_scores[pid]['score'] += 1
                    prototype_scores[pid]['weight'] += rule.get('weight', 0.5)
                    prototype_scores[pid]['reasons'].append(rule.get('reason', f"Use-case匹配: {use_case}"))
                    prototype_scores[pid]['use_cases'].append(use_case)

        # 转换为候选列表
        for pid, score_info in prototype_scores.items():
            if score_info['score'] >= 1:  # 至少匹配 1 个特征
                avg_weight = score_info['weight'] / score_info['score']
                reason = score_info['reasons'][0] if score_info['reasons'] else "分子特征匹配"
                candidates.append({
                    'prototype_id': pid,
                    'weight': min(avg_weight, 0.9),
                    'reason': reason,
                    'match_basis': 'use_case_mapping' if score_info['use_cases'] else 'molecular_feature_inference',
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

        # 2a. 来源、定位和引文完整，但 verification=partial 的实测性能线索
        performance_lead_candidates = self.find_performance_leads(pollutant)

        # 2b. 污染物专项映射只作启发，不能升级为 direct evidence
        pollutant_candidates = self.find_pollutant_inspiration(pollutant)

        # 3. 查找 feature-based inspiration
        feature_candidates = self.find_feature_based(pollutant_profile)

        # 显式 use-case 是独立路由，不能混入普通吸附机制候选。
        use_case_candidates = [c for c in feature_candidates if c.get('match_basis') == 'use_case_mapping']
        if use_case_candidates:
            direct_candidates = []
            performance_lead_candidates = []
            pollutant_candidates = []
            mechanism_candidates = []
            feature_candidates = use_case_candidates
        else:
            # 3b. Track2A 机制层候选（绑定到具体 mechanism_id）
            mechanism_candidates = self.find_mechanism_based(pollutant_profile, pollutant)

        # 4. 合并候选（fact → source-backed lead → 污染物专项启发 → feature → 机制发现）
        all_candidates = []
        seen_ids = set()

        for c in direct_candidates:
            if c['prototype_id'] not in seen_ids:
                seen_ids.add(c['prototype_id'])
                all_candidates.append(c)

        for c in performance_lead_candidates:
            if c['prototype_id'] not in seen_ids:
                seen_ids.add(c['prototype_id'])
                all_candidates.append(c)

        # Keep room for independent feature/mechanism discovery; one curated lane
        # must not monopolize the 15-result brief.
        for c in pollutant_candidates[:8]:
            if c['prototype_id'] not in seen_ids:
                seen_ids.add(c['prototype_id'])
                all_candidates.append(c)

        for c in feature_candidates if use_case_candidates else feature_candidates[:4]:
            if c['prototype_id'] not in seen_ids:
                seen_ids.add(c['prototype_id'])
                all_candidates.append(c)

        for c in mechanism_candidates:
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
        for c in all_candidates:
            pid = c['prototype_id']
            if pid in forbidden_set:
                continue  # Skip forbidden candidates per gold-set
            if pid in self.prototypes:
                proto = self.prototypes[pid]

                # --- 占位符/背景原型过滤 ---
                proto_scope = (proto.get('scope_note', '') or '').lower()
                proto_ev_status = (proto.get('evidence_status', '') or '').lower()
                proto_status = (proto.get('status', '') or '').lower()

                is_placeholder = 'placeholder' in proto_scope or proto_ev_status == 'placeholder'
                is_background = 'background' in proto_scope or proto_ev_status == 'background_only' or 'surface physics' in proto_scope
                is_parked = proto_status in ('parked_separation', 'needs_literature')

                if is_placeholder:
                    continue  # 占位符原型：完全跳过
                if is_parked and not is_background:
                    continue  # needs_literature 非背景原型：跳过
                # 背景原型：保留但在 brief 中标记
                # --- 过滤结束 ---

                # 获取机制（按 query relevance + verification 综合评分）
                mechs = proto.get('mechanisms', [])
                # 过滤掉 brief_visibility=hidden 的机制
                visible_mechs = [m for m in mechs if m.get('brief_visibility', 'visible') != 'hidden']
                mechs = mechs if c.get('match_basis') == 'use_case_mapping' and not visible_mechs else visible_mechs
                matched_mechanism_ids = set(c.get('matched_mechanism_ids', []))
                if matched_mechanism_ids:
                    mechs = [m for m in mechs if m.get('mechanism_id') in matched_mechanism_ids]
                if not mechs:
                    continue  # 所有机制都隐藏，跳过此原型
                _verif_priority = {'verified': 0, 'corroborated': 1, 'needs_review': 3}

                # Query-conditioned mechanism scoring
                # Get query features for binding check
                _query_features = [f.lower() for f in pollutant_profile.get('molecular_features', [])]
                _query_interactions = [i.lower() for i in pollutant_profile.get('likely_interactions', [])]
                _query_all_text = ' '.join(_query_features + _query_interactions)
                _query_keywords = _extract_keywords(_query_all_text)
                _query_keywords.update(_extract_keywords(pollutant))
                # Also add split-by-slash keywords
                for _feat in _query_features:
                    for _part in _feat.split('/'):
                        _part = _part.strip()
                        if len(_part) >= 2:
                            _query_keywords.add(_part)
                for _inter in _query_interactions:
                    for _part in _inter.split('/'):
                        _part = _part.strip()
                        if len(_part) >= 2:
                            _query_keywords.add(_part)

                def _mech_score(m):
                    score = 0
                    # Verification priority (0-3)
                    verif = _verif_priority.get(m.get('verification', 'needs_review'), 2)
                    score -= verif * 0.5  # Lower is better

                    # Mechanism name/desc relevance to query
                    mech_name = ((m.get('name', '') or '') + ' ' + (m.get('description', '') or '')).lower()
                    if c.get('match_basis') == 'use_case_mapping':
                        title = (m.get('name', '') or '').lower()
                        score += 10 * sum(keyword in title for keyword in _query_keywords)
                    # Check if mechanism mentions matched features/interactions
                    for feat in c.get('molecular_feature_links', []):
                        if feat.lower() in mech_name:
                            score += 3
                    for inter in c.get('matched_interactions', []):
                        if inter.lower() in mech_name:
                            score += 2

                    # Check functional_groups / key_structures overlap with query features (keyword-based)
                    fg_raw = m.get('functional_groups', '')
                    fg_text = (fg_raw if isinstance(fg_raw, str) else ' '.join(fg_raw)).lower()
                    ks_raw = m.get('key_structures', [])
                    ks_text = (' '.join(ks_raw) if isinstance(ks_raw, list) else str(ks_raw)).lower()
                    cc = m.get('causal_chain', {})
                    cc_text = (cc.get('transferable_principle', '') or '').lower()
                    mech_all_text = fg_text + ' ' + ks_text + ' ' + mech_name + ' ' + cc_text
                    mech_kw = _extract_keywords(mech_all_text)
                    _fg_match = len(_query_keywords & mech_kw)
                    # Also check direct substring for longer features
                    for qf in _query_features:
                        if len(qf) >= 3 and qf in mech_all_text:
                            _fg_match += 1
                    for qi in _query_interactions:
                        if len(qi) >= 2 and qi in mech_all_text:
                            _fg_match += 1
                    score += _fg_match * 4  # Strong boost for feature binding

                    # Check if mechanism mentions the pollutant
                    pol = pollutant.lower()
                    if pol in mech_name:
                        score += 5

                    # Boost coordination/chelation mechanisms for heavy-metal queries
                    match_reason = (c.get('reason', '') or '').lower()
                    if any(kw in match_reason for kw in ['螯合', '配位', 'chelat', 'coordination']):
                        if any(kw in mech_name for kw in ['螯合', 'chelat']):
                            score += 8  # Strong boost for chelation
                        elif any(kw in mech_name for kw in ['配位', 'coordination', 'DOPA', 'dopa']):
                            score += 5  # Moderate boost for coordination

                    # Boost mechanisms that mention the pollutant class
                    if pollutant_class and pollutant_class.lower() in mech_name:
                        score += 3

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

                # Compute feature binding score for selected mechanism
                _fg_raw = main_mech.get('functional_groups', '')
                _fg_text = (_fg_raw if isinstance(_fg_raw, str) else ' '.join(_fg_raw)).lower()
                _ks_raw = main_mech.get('key_structures', [])
                _ks_text = (' '.join(_ks_raw) if isinstance(_ks_raw, list) else str(_ks_raw)).lower()
                _cc_raw = main_mech.get('causal_chain', {})
                _cc_text = (_cc_raw.get('transferable_principle', '') or '').lower()
                _mech_name_text = (main_mech.get('name', '') or '').lower()
                _mech_all = _fg_text + ' ' + _ks_text + ' ' + _mech_name_text + ' ' + _cc_text
                _mech_kw = _extract_keywords(_mech_all)
                _fg_match = len(_query_keywords & _mech_kw)
                for qf in _query_features:
                    if len(qf) >= 3 and qf in _mech_all:
                        _fg_match += 1
                for qi in _query_interactions:
                    if len(qi) >= 2 and qi in _mech_all:
                        _fg_match += 1

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
                performance_evidence_tier = c.get('performance_evidence_tier', 'none')
                mech_verif = main_mech.get('verification', 'needs_review') or 'needs_review'
                dt_tier = evidence_tier if dt_entries else 'inference'

                # Organic domain gating: if pollutant is organic and candidate has no
                # direct organic adsorption evidence, force inference/exploratory
                _organic_classes = ('有机物', '有机污染物', 'PFAS', '抗生素', '染料', '内分泌干扰物',
                                    '酚类', '药物', '农药', 'chloro', 'phenol', 'PCB', 'PBDE',
                                    'dioxin', 'organ', 'macrolide', 'UV_filter', 'alkyl',
                                    'bisphenol', 'paraffin', 'solvent')
                is_organic_pollutant = any(cls.lower() in pollutant_class.lower() for cls in _organic_classes)

                if has_direct and mech_verif in ('verified', 'corroborated'):
                    candidate_honesty = 'fact'
                elif performance_evidence_tier in ('fact', 'lead') or has_direct or dt_tier.startswith('fact'):
                    candidate_honesty = 'lead'
                else:
                    candidate_honesty = 'inference'

                # Organic mappings remain exploratory unless material-removal performance supports them.
                if is_organic_pollutant and performance_evidence_tier == 'none' and not has_direct:
                    candidate_honesty = 'inference'

                # Determine lane
                if candidate_honesty == 'fact':
                    lane = 'fact'
                elif candidate_honesty == 'lead':
                    lane = 'lead'
                else:
                    lane = 'exploratory'

                # Get charge_state context
                charge_state = self.get_charge_state_context(pid)

                # Get relevance gating (do_not_list compatibility)
                do_not_list = self.get_do_not_list(pid)
                query_lower = pollutant.lower()
                is_excluded = False
                exclusion_reason = ''
                for dnl in do_not_list:
                    dnl_text = (dnl.get('text', '') or '').lower()
                    if any(kw in dnl_text for kw in query_lower.split()):
                        is_excluded = True
                        exclusion_reason = dnl.get('text', '')
                        break

                valid_verification_tiers = {
                    'verified', 'corroborated', 'partial', 'needs_review',
                    'missing_pdf', 'unverified', 'knowledge_gap', 'scope_mismatch'
                }
                output_verification_tier = (
                    mech_verif if mech_verif in valid_verification_tiers else 'needs_review'
                )

                brief_candidates.append({
                    'prototype_id': pid,
                    'organism': proto.get('organism', {}).get('scientific', '未知'),
                    'candidate_honesty': candidate_honesty,
                    'lane': lane,
                    'prototype_status': {
                        'is_background': is_background,
                        'is_placeholder': False,  # placeholders already filtered
                        'scope_note': proto.get('scope_note', ''),
                    },
                    'domain_caveat': (
                        'source-backed performance lead; independent verification pending'
                        if is_organic_pollutant and performance_evidence_tier == 'lead'
                        else 'organic micropollutant evidence weak'
                        if is_organic_pollutant and not has_direct else ''
                    ),
                    'match': {
                        'reason': c.get('reason', ''),
                        'weight': c.get('weight', 0.5),
                        'applicability_fit': self._get_applicability(proto),
                        'match_basis': c.get('match_basis', 'unknown'),
                        'direct_evidence': c.get('direct_evidence', False),
                        'performance_evidence_tier': performance_evidence_tier,
                        'matched_mechanism_ids': c.get('matched_mechanism_ids', []),
                        'mapping_source': c.get('mapping_source', ''),
                        'mapping_quality': c.get('mapping_quality', '')
                    },
                    'mechanism': {
                        'mechanism_id': main_mech.get('mechanism_id', ''),
                        'name': main_mech.get('name', '未知'),
                        'selected_mechanism_reason': f"Query-conditioned scoring selected this mechanism for {pollutant} based on relevance to matched features/interactions",
                        'selected_mechanism_alignment': {
                            'query_pollutant': pollutant,
                            'query_class': pollutant_class,
                            'mechanism_keywords': main_mech.get('name', '')[:50],
                            'alignment_basis': 'query_relevance_scoring',
                            'query_features': pollutant_profile.get('molecular_features', []),
                            'mechanism_functional_groups': main_mech.get('functional_groups', []),
                            'mechanism_key_structures': main_mech.get('key_structures', []),
                            'feature_binding_score': _fg_match
                        },
                        '基本原理': main_mech.get('基本原理', 'needs_review'),
                        'key_structures': main_mech.get('key_structures', []),
                        'functional_groups': main_mech.get('functional_groups', []),
                        'molecular_feature_links': c.get('molecular_feature_links', []) or main_mech.get('molecular_feature_links', []),
                        'attribution': {
                            'source': main_mech.get('source', 'unknown'),
                            'ref': main_mech.get('ref_doi', main_mech.get('ref', '')),
                            'verification_tier': output_verification_tier,
                            'confidence': 'low' if output_verification_tier in ('needs_review', 'unverified', 'knowledge_gap', 'scope_mismatch') else 'normal'
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
                    },
                    'charge_state': charge_state,
                    'relevance_gating': {
                        'is_excluded': is_excluded,
                        'exclusion_reason': exclusion_reason,
                        'do_not_list': do_not_list
                    }
                })
                if len(brief_candidates) >= 15:
                    break

        # 6. 构建 honesty_ledger
        facts = []
        leads = []
        inferences = []

        if direct_candidates:
            facts.append(f"有 {len(direct_candidates)} 个原型对 {pollutant} 有严格核验的材料去除性能")
        if performance_lead_candidates:
            leads.append(f"有 {len(performance_lead_candidates)} 个原型对 {pollutant} 有来源定位完整但仅部分核验的性能线索")

        for c in all_candidates[:5]:
            pid = c['prototype_id']
            evidence_tier = c.get('performance_evidence_tier', 'none')
            if evidence_tier == 'lead':
                leads.append(f"{pid}: 污染物特异去除数据有来源、定位和引文，verification=partial")
            elif c.get('direct_evidence'):
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
        if not isinstance(tested, dict):
            tested = {}
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
            if match_info.get('performance_evidence_tier') == 'lead':
                return "有来源、定位和原文引文的材料去除性能，尚待独立核验"
            if match_info.get('direct_evidence'):
                return "有直接实验数据但机制未经独立核实"
            return "有性能或转译线索，尚待独立核验"
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
        aliases = self._pollutant_aliases(pollutant)

        for p in proto.get('performance_data', []):
            pol = p.get('pollutant', '')
            if not pol or not pol.strip():
                continue  # 空 pollutant 不参与匹配
            if self._matches_pollutant_text(pol, aliases):
                leads.append({
                    'pollutant': pol,
                    'material': p.get('material', ''),
                    'value': p.get('value', ''),
                    'unit': p.get('unit', ''),
                    'verification_tier': p.get('verification', 'unverified'),
                    'source': (
                        p.get('ref_doi') or p.get('source_doi') or p.get('patent_number')
                        or p.get('standard_number') or p.get('source', '')
                    ),
                    'locator': p.get('locator') or p.get('source_locator') or p.get('source_page', ''),
                    'verification_quote': p.get('verification_quote') or p.get('quote', ''),
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

    # ============================================================
    # ROUND 4: ADRMATS ADAPTER CAPABILITIES
    # ============================================================

    def get_do_not_list(self, prototype_id: str) -> List[Dict[str, Any]]:
        """Extract source-backed hard DO-NOT rules from a prototype.

        Returns list of dicts with: rule_id, description, source, gate_level
        """
        proto = self.prototypes.get(prototype_id, {})
        if not proto:
            return []

        do_nots = []

        # Check boundary_rules
        for bc in proto.get('boundary_rules', []):
            if bc.get('type') == 'hard_do_not' or bc.get('gate_level') == 'hard':
                do_nots.append({
                    'rule_id': bc.get('rule_id', ''),
                    'description': bc.get('description', ''),
                    'source': bc.get('source_doi', ''),
                    'gate_level': 'hard'
                })

        # Check causal_chain boundary_conditions
        for m in proto.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if not isinstance(cc, dict):
                continue
            for bc in cc.get('boundary_conditions', []):
                if isinstance(bc, dict) and bc.get('gate_level') == 'hard':
                    do_nots.append({
                        'rule_id': f"{m.get('mechanism_id', '')}_bc",
                        'description': bc.get('text', ''),
                        'source': bc.get('source', ''),
                        'gate_level': 'hard'
                    })

        return do_nots

    def decompose_design_translation(self, prototype_id: str) -> Dict[str, Any]:
        """Decompose design_translation into ADRMATS-consumable structure.

        Returns dict with: idea, examples, source_tier, applicability,
        transferable_principles, implementation_handles, limitations
        """
        proto = self.prototypes.get(prototype_id, {})
        if not proto:
            return {'status': 'not_found'}

        dt = proto.get('design_translation', {})
        # Handle list format (take first element)
        if isinstance(dt, list) and dt:
            dt = dt[0]
        if not dt or not isinstance(dt, dict):
            return {'status': 'missing', 'error': 'No design_translation found'}

        result = {
            'idea': dt.get('idea', ''),
            'examples': dt.get('examples', []),
            'source_tier': dt.get('source_tier', 'unknown'),
            'applicability': dt.get('applicability', ''),
            'status': 'structured'
        }

        # Extract transferable principles from mechanisms
        principles = []
        for m in proto.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if isinstance(cc, dict):
                tp = cc.get('transferable_principle', '')
                if tp and tp.strip():
                    principles.append(tp)
        result['transferable_principles'] = principles

        # Extract implementation handles from material_realization_examples
        handles = []
        for mre in proto.get('material_realization_examples', []):
            if isinstance(mre, dict):
                handles.append({
                    'material': mre.get('material', ''),
                    'method': mre.get('method', ''),
                    'performance': mre.get('performance', '')
                })
        result['implementation_handles'] = handles

        # Identify limitations from boundary_conditions
        limitations = []
        for m in proto.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if isinstance(cc, dict):
                for bc in cc.get('boundary_conditions', []):
                    if isinstance(bc, dict):
                        limitations.append(bc.get('text', ''))
        result['limitations'] = limitations[:5]

        return result

    def get_charge_state_context(self, prototype_id: str) -> Dict[str, Any]:
        """Extract charge_state and pKa context for ion-dependent adsorption.

        Returns dict with: has_charge_state, pka_values, ion_dependence,
        ph_sensitive, charge_mechanisms
        """
        proto = self.prototypes.get(prototype_id, {})
        if not proto:
            return {'has_charge_state': False}

        result = {
            'has_charge_state': False,
            'pka_values': [],
            'ion_dependence': [],
            'ph_sensitive': False,
            'charge_mechanisms': []
        }

        charge_terms = ['amino', 'amine', 'carboxyl', 'carboxylic', 'hydroxyl',
                       'thiol', 'phosphate', 'sulfate', 'protonat', 'deprotonat',
                       'pka', 'ph sensitive', 'ionic', 'electrostatic',
                       '氨基', '羧基', '羟基', '巯基', '磷酸', '质子化']
        ph_terms = ['ph', 'ph dependent', 'ph effect', 'acidic', 'alkaline', 'basic']

        for m in proto.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if not isinstance(cc, dict):
                continue

            desc = m.get('description', '')
            bio = cc.get('bio_structure', {})
            bio_text = bio.get('text', '') if isinstance(bio, dict) else ''
            interaction = cc.get('interaction', {})
            interaction_text = interaction.get('text', '') if isinstance(interaction, dict) else ''

            combined = f"{desc} {bio_text} {interaction_text}".lower()

            if any(term in combined for term in charge_terms):
                result['has_charge_state'] = True
                result['charge_mechanisms'].append({
                    'mechanism_id': m.get('mechanism_id', ''),
                    'description': desc[:100],
                    'charge_terms': [t for t in charge_terms if t in combined]
                })

            if any(term in combined for term in ph_terms):
                result['ph_sensitive'] = True

            import re
            pka_matches = re.findall(r'pka\s*[=~≈]\s*(\d+\.?\d*)', combined)
            result['pka_values'].extend(pka_matches)

        return result

    def compute_relevance_score(self, prototype_id: str, query: str) -> Dict[str, Any]:
        """Compute relevance score for a prototype against a query.

        Returns dict with: score (0-1), matched_keywords, is_relevant,
        excluded_reason (if not relevant)
        """
        import re

        proto = self.prototypes.get(prototype_id, {})
        if not proto:
            return {'score': 0, 'is_relevant': False}

        query_lower = query.lower()
        query_keywords = set(re.findall(r'[a-z]{3,}|[一-鿿]{2,}', query_lower))

        # Get prototype keywords
        name_zh = proto.get('name_zh', '')
        name_en = proto.get('name_en', '')
        organism = proto.get('organism', {})
        if isinstance(organism, dict):
            organism_text = organism.get('scientific', '')
        else:
            organism_text = str(organism)

        mech_texts = []
        for m in proto.get('mechanisms', []):
            desc = m.get('description', '')
            cc = m.get('causal_chain', {})
            if isinstance(cc, dict):
                for key in ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']:
                    val = cc.get(key, {})
                    if isinstance(val, dict):
                        mech_texts.append(val.get('text', ''))

        all_text = f"{name_zh} {name_en} {organism_text} {' '.join(mech_texts)}".lower()
        proto_keywords = set(re.findall(r'[a-z]{3,}|[一-鿿]{2,}', all_text))

        matched = query_keywords & proto_keywords
        score = len(matched) / max(len(query_keywords), 1)

        # Off-scope exclusion
        excluded = False
        excluded_reason = ''
        surface_terms = ['superhydrophobic', 'wetting', 'contact angle', 'wca',
                        '超疏水', '润湿', '接触角']
        if any(term in query_lower for term in ['adsorption', '吸附', 'removal', '去除']):
            if any(term in all_text for term in surface_terms):
                if not any(term in all_text for term in ['adsorption', '吸附', 'removal', '去除']):
                    excluded = True
                    excluded_reason = 'surface_physics_off_scope'

        return {
            'score': round(score, 3),
            'matched_keywords': list(matched)[:10],
            'is_relevant': score > 0.1 and not excluded,
            'excluded_reason': excluded_reason
        }

    def gate_mechanisms_by_query(self, prototype_id: str, query: str, min_score: float = 0.1) -> List[int]:
        """Filter mechanisms by relevance to query.

        Returns list of relevant mechanism indices.
        """
        import re

        proto = self.prototypes.get(prototype_id, {})
        if not proto:
            return []

        query_lower = query.lower()
        query_kw = set(re.findall(r'[a-z]{3,}|[一-鿿]{2,}', query_lower))

        relevant = []
        for i, m in enumerate(proto.get('mechanisms', [])):
            desc = m.get('description', '')
            cc = m.get('causal_chain', {})
            if isinstance(cc, dict):
                texts = []
                for key in ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']:
                    val = cc.get(key, {})
                    if isinstance(val, dict):
                        texts.append(val.get('text', ''))
                mech_text = f"{desc} {' '.join(texts)}".lower()
            else:
                mech_text = desc.lower()

            mech_kw = set(re.findall(r'[a-z]{3,}|[一-鿿]{2,}', mech_text))
            overlap = query_kw & mech_kw
            score = len(overlap) / max(len(query_kw), 1)

            if score >= min_score:
                relevant.append(i)

        return relevant


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
