# BMDL 执行计划（修订版）

> 日期: 2026-06-25（修订）
> 状态: 待执行
> 执行者: 本地 Claude Code
> 规划者: AI（规划者角色，不直接执行）

---

## 修订说明

基于用户反馈，对原 A/B/C 计划进行以下调整：

1. **性能数据缺失不是硬伤** — BMDL 输出以机制和 brief 为核心，不要求 solid performance_data。原有"可用性分级"中以 performance_data 数量评判原型强弱的逻辑不适用。
2. **污染物数据集成交给 Axl_Huang** — 原计划 A（BMDL 集成代码）转为交接文档，不自行实现。2879 篇文献提取的特征可能在 ADRMATS 其他模块也会用到。
3. **新增数据可靠度优化计划** — 针对_verification 低、LLM 推理广泛等问题。
4. **新增占位符原型处理计划** — 针对 5 个真占位符原型 + 代码未过滤的问题。
5. **原计划 B/C 保留** — feature_matching_rules 扩充和 101 条空字段溯源不变。

---

## 目录

- [BMDL 查询流程确认](#bmdl-查询流程确认)
- [计划 A: 数据可靠度优化](#计划-a-数据可靠度优化)
- [计划 B: 占位符原型处理](#计划-b-占位符原型处理)
- [计划 C: feature_matching_rules 扩充](#计划-c-feature_matching_rules-扩充)
- [计划 D: 101 条空字段溯源](#计划-d-101-条空字段溯源)
- [交接文档: 污染物数据集成 → Axl_Huang](#交接文档-污染物数据集成--axl_huang)
- [执行顺序建议](#执行顺序建议)

---

## BMDL 查询流程确认

### 用户确认的流程

用户指出：水质约束传递到 BMDL 后，BMDL 需要先分析用户需要去除什么污染物、性质如何，然后才能匹配仿生原型、仿生机制，给出设计要点。

### 当前代码实现（`tools/biomimetic_context.py` 第 343-700 行）

```
query(pollutant, water_quality, engineering_constraints)
  │
  ├─ Step 1: get_pollutant_profile(pollutant)
  │          → 从 pollutant_profiles.json 获取污染物画像
  │          → 包含 molecular_features, likely_interactions, pollutant_class 等
  │
  ├─ Step 2: find_direct_evidence(pollutant)
  │          → 从 feature-mapping.json 的 pollutant_prototype_map 递归查找
  │          → 找到有直接实验数据的原型（match_basis='direct_pollutant_evidence'）
  │
  ├─ Step 3: find_feature_based(pollutant_profile)
  │          → 4 层匹配：分子特征 → 相互作用 → 污染物类别 → 使用场景
  │          → 返回 top 10 候选（match_basis='molecular_feature_inference'）
  │
  ├─ Step 4: 合并候选（direct evidence 优先，去重）
  │
  ├─ Step 5: gold_set_forbidden 过滤（per-query 禁止列表）
  │
  ├─ Step 6: 逐候选构建 brief
  │          ├─ _mech_score(): 按查询条件对机制评分排序，选主机制
  │          ├─ 诚实度分类: fact / lead / inference
  │          ├─ 有机污染物门控: 无 direct evidence → 强制 inference
  │          ├─ lane 分配: fact / lead / exploratory
  │          └─ 提取 design_translation, boundaries, charge_state 等
  │
  ├─ Step 7: 构建 honesty_ledger (facts / leads / inferences)
  │
  ├─ Step 8: find_applicable_rules() + _collect_rule_based_cautions()
  │          → 按 water_quality (pH/温度/盐度) 匹配设计规则和边界条件
  │
  └─ return {'brief': {context, candidates, applicable_rules, rule_based_cautions, honesty_ledger}}
```

### 水质约束的使用方式

`water_quality` 参数（含 pH、temperature、salinity 等）在以下环节使用：

1. **context 输出**: 直接放入 `brief.context.water_quality`
2. **机制评分** (`_mech_score`): 查询条件的特征关键词用于机制相关性评分
3. **设计规则匹配** (`find_applicable_rules`): 按 pH/温度范围匹配 `design-rules.json` 中的规则
4. **边界条件收集** (`_collect_rule_based_cautions`): 按 water_quality 匹配 causal_chain.boundary_conditions，分 hard/soft 输出

**注意**: 当前代码中污染物名称由 ADRMATS 直接传入，BMDL 不从 water_quality 推断污染物。污染物性质分析通过 `get_pollutant_profile()` 完成（读取 `pollutant_profiles.json`）。如果 ADRMATS 需要从水质指标推断污染物，那是在 ADRMATS 侧的约束智能体完成的，BMDL 接收已确定的污染物名称。

### 输出格式

最终输出为一个嵌套 dict，核心结构：

```json
{
  "brief": {
    "context": {
      "water_quality": {"pH": 6.0, "temperature": 25},
      "removal_target": {"污染物": "Pb(II)"},
      "pollutant_profile": {"molecular_features": [...], ...},
      "engineering_constraints": ["水稳定性"]
    },
    "candidates": [
      {
        "prototype_id": "chitosan",
        "organism": "...",
        "candidate_honesty": "fact|lead|inference",
        "lane": "fact|lead|exploratory",
        "match": {"reason": "...", "weight": 0.8, "match_basis": "...", "direct_evidence": true},
        "mechanism": {"name": "...", "attribution": {"verification_tier": "...", "ref": "..."}, ...},
        "design_translation": {"idea": "...", "material_handle": "...", "constraints": "...", ...},
        "boundaries": [...],
        "honesty_summary": "...",
        "evidence_context": {"performance_leads": [...]},
        "relevance_gating": {"is_excluded": false, ...}
      }
    ],
    "applicable_rules": [...],
    "rule_based_cautions": {"hard": [...], "soft": [...]},
    "honesty_ledger": {"facts": [...], "leads": [...], "inferences": [...]}
  }
}
```

---

## 计划 A: 数据可靠度优化

### A.1 问题诊断

对 44 个原型（排除 7 个 background/superseded 后，334 条机制）的数据质量统计：

| 指标 | 数量 | 占比 | 说明 |
|------|------|------|------|
| verified | 9 | 2.7% | 有文献验证的机制 |
| partial | 160 | 47.9% | 部分验证 |
| needs_review | 137 | 41.0% | 需要审核 |
| unverified | 11 | 3.3% | 未验证 |
| unknown | 9 | 2.7% | 未知 |
| llm_inferred | 5 | 1.5% | LLM 推理 |
| knowledge_gap | 3 | 0.9% | 知识空白 |

**核心问题**：

1. **LLM 推理的 boundary_conditions（536 条，100%）**：所有 44 个原型的所有 boundary_conditions 的 `basis` 均为 `"llm_inferred"`，没有任何一条有文献支撑。分布集中在高影响力原型：

   | 原型 | LLM boundary 数 | 总 boundary 数 |
   |------|----------------|---------------|
   | chitosan | 116 | 116 |
   | mussel-foot-adhesion | 63 | 63 |
   | superhydrophobic-artificial | 60 | 60 |
   | water-strider-leg | 52 | 52 |
   | polydopamine-coating | 36 | 36 |
   | lotus-leaf | 33 | 33 |
   | spider-silk | 24 | 24 |
   | pitcher-plant-slippery-surface | 23 | 23 |
   | shark-skin | 18 | 18 |
   | silk-fibroin | 17 | 17 |
   | 其他 34 个原型 | 94 | 94 |
   | **总计** | **536** | **536** |

2. **LLM 推理的 design_translation（39 条，覆盖 39 个原型）**：几乎每个原型都有 1 条 `source_tier: "llm_inference"` 的 design_translation。仅 mussel-foot-adhesion 有 2 条（1 LLM + 1 非 LLM）。design_translation 是 brief 的核心输出之一（设计思路、材料手柄、实现约束），全部来自 LLM 推理意味着设计建议的质量取决于 LLM 推理质量。

3. **boundary_rules 全部为空**：44 个原型的 `boundary_rules` 字段总数为 0。`get_do_not_list()` 方法依赖此字段输出 hard DO-NOT 规则，当前无任何输出。

4. **needs_review 占比高（41%）**：137 条机制标记为 needs_review，需要文献溯源升级。

### A.2 优化策略（按优先级）

#### 优先级 1: 代码层 — 在 brief 输出中暴露 boundary_conditions 的 basis

**问题**: 当前 `_get_mechanism_boundaries()` 提取 boundary_conditions 时不暴露 `basis` 字段，ADRMATS 无法区分哪些边界条件是 LLM 推理的、哪些有文献支撑。

**方案**: 在 `tools/biomimetic_context.py` 的 `_get_mechanism_boundaries()` 方法中，为每条 boundary 添加 `basis` 字段输出。

**修改文件**: `tools/biomimetic_context.py`

**步骤**:

1. 定位 `_get_mechanism_boundaries()` 方法（约第 750 行）
2. 在返回的 boundary dict 中添加 `'basis': bc.get('basis', 'unknown')`
3. 运行 `python tools/generate_adrmats_briefs.py` 验证输出中包含 `basis` 字段

**验证**: 检查 chitosan 的 brief 中 boundaries 是否包含 `"basis": "llm_inferred"`

#### 优先级 2: 数据层 — 高影响力原型的 verification 升级

**问题**: chitosan（110 机制）、polydopamine-coating（35 机制）、mussel-foot-adhesion（55 机制）是 BMDL 最常匹配的原型，但大量机制标记为 needs_review。

**方案**: 逐批使用 ref_doi 溯源文献，验证机制声明，升级 verification tier。

**修改文件**: `prototypes_db/chitosan.json`, `prototypes_db/polydopamine-coating.json`, `prototypes_db/mussel-foot-adhesion.json`

**步骤**:

1. 提取 needs_review 机制的 ref_doi 列表
2. 通过 Crossref API 获取文献摘要
3. 核对机制声明与文献内容是否一致
4. 一致的升级为 `partial`，不一致的保持 `needs_review` 并添加 note
5. 无法溯源的保持原状

**验证**: 统计升级前后 needs_review 数量变化

#### 优先级 3: 数据层 — boundary_rules 从已验证 boundary_conditions 提取

**问题**: boundary_rules 全部为空，`get_do_not_list()` 无输出。

**方案**: 在优先级 2 完成后（部分 boundary_conditions 升级为文献支撑后），从已验证的 boundary_conditions 中提取 hard 规则到 boundary_rules 字段。

**前提**: 优先级 2 至少完成 chitosan 的验证

**步骤**:

1. 对每个原型，遍历 `mechanisms[].causal_chain.boundary_conditions`
2. 筛选 `basis != "llm_inferred"` 且 `gate_level == "hard"` 的条目
3. 提取关键约束文本写入 `boundary_rules` 数组
4. 格式: `{"rule": "...", "source_mechanism": "...", "gate_level": "hard"}`

**验证**: 检查 chitosan 的 `boundary_rules` 是否非空，`get_do_not_list()` 是否有输出

#### 优先级 4: 长期 — LLM boundary_conditions 的文献验证

**问题**: 536 条 boundary_conditions 全部为 LLM 推理，需要逐步用文献验证或诚实降级。

**方案**: 这是一个长期工作，建议按原型分批处理，每批 1 个原型。

**处理流程**:
- 对每条 LLM boundary_condition:
  - 能找到文献支撑 → 升级 `basis` 为 `"literature"`，添加 `ref_doi`
  - 找不到文献支撑但逻辑合理 → 保持 `"llm_inferred"` 但确保 brief 中诚实标注
  - 逻辑有误 → 修正或删除

**优先顺序**: chitosan (116) → mussel-foot-adhesion (63) → polydopamine-coating (36) → spider-silk (24) → silk-fibroin (17)

### A.3 关于 design_translation 的说明

39 个原型各有 1 条 LLM 推理的 design_translation。这是 BMDL 构建时批量生成的，当前通过 `source_tier: "llm_inference"` 诚实标注。

**当前处理**: 暂不批量修改。design_translation 作为设计灵感而非硬性结论，LLM 推理在诚实标注的前提下可接受。后续可在优先级 2 的文献溯源过程中，顺带验证和升级高影响力原型的 design_translation。

---

## 计划 B: 占位符原型处理

### B.1 分类结果

对原"14 个弱原型"重新分析后，按用户反馈（无 performance_data 不是硬伤），分为三类：

#### 真占位符（5 个）— 需要处理

| 原型 | 机制来源 | scope_note | generated_by | status |
|------|---------|-----------|-------------|--------|
| biomineralization-template | llm_inference | Placeholder prototype | P1d-补全 | needs_literature |
| coral-skeleton | llm_inference | Placeholder prototype | P1d-补全 | active |
| dna-aptamer | llm_inference | Placeholder prototype | P1d-补全 | needs_literature |
| magnetic-bacteria | llm_inference | Placeholder prototype | P1d-补全 | active |
| mycelium | llm_inference | Placeholder prototype | P1c-auto | active |

特征：机制全部由 LLM 生成，scope_note 明确标注 "Placeholder"，无真实文献支撑。

#### 背景原型（7 个）— 已有标注但代码未过滤

| 原型 | 机制数 | scope_note | status |
|------|--------|-----------|--------|
| diatom-inspired-porous | 1 | Background-only, superseded by diatom-frustule | (空) |
| lotus-leaf | 33 | V1-A: Surface physics, reclassified to background | parked_separation |
| pitcher-plant-slippery-surface | 21 | V1-A: Surface physics, reclassified to background | active |
| shark-skin | 18 | V1-A: Surface physics, reclassified to background | parked_separation |
| silkworm-silk | 1 | Background-only, superseded by silk-fibroin | (空) |
| superhydrophobic-artificial | 60 | V1-A: Surface physics, reclassified to background | parked_separation |
| water-strider-leg | 52 | V1-A: Surface physics, reclassified to background | parked_separation |

特征：有真实机制（非 LLM），但已被重新分类为背景/被替代。数据中已有标注（scope_note、status），但代码未读取这些字段。

#### 活跃但机制少（8 个）— 无需处理

bird-feather-keratin, fungal-biosorption, insect-chitin, microbial-exopolysaccharide, namib-beetle, plant-wax-cuticle, rice-husk-phytolith, sulfate-reducing-bacteria

特征：机制来自真实文献（非 LLM），仅 1 个机制 + 0 条 performance_data。**按用户反馈，这不是硬伤**，BMDL 输出以机制和 brief 为核心，这些原型有真实的仿生机制可输出。

### B.2 代码缺陷

**关键发现**: `tools/biomimetic_context.py` 中 **完全没有** 检查以下字段：
- `brief_visibility`（grep 返回 0 匹配）
- `scope_note`（grep 返回 0 匹配）
- `evidence_status`（grep 返回 0 匹配）
- `placeholder`（grep 返回 0 匹配）

这意味着：占位符原型（如 dna-aptamer）和背景原型（如 water-strider-leg）如果通过 feature_matching_rules 匹配到，**会出现在查询结果中**，且没有任何标记告诉 ADRMATS 这些是占位符或背景原型。

### B.3 修改文件

`tools/biomimetic_context.py`

### B.4 具体步骤

#### Step 1: 在 query() 中添加原型过滤逻辑

在 `query()` 方法第 388 行 `if pid in self.prototypes:` 之后、机制获取之前，添加原型状态检查：

```python
if pid in self.prototypes:
    proto = self.prototypes[pid]

    # --- 新增: 占位符/背景原型过滤 ---
    proto_scope = (proto.get('scope_note') or '').lower()
    proto_ev_status = (proto.get('evidence_status') or '').lower()
    proto_status = (proto.get('status') or '').lower()

    is_placeholder = 'placeholder' in proto_scope
    is_background = 'background' in proto_scope or proto_ev_status == 'background_only'
    is_parked = proto_status == 'parked_separation' or proto_status == 'needs_literature'

    if is_placeholder:
        # 占位符原型: 跳过，不进入候选列表
        continue
    if is_parked and not is_background:
        # needs_literature 状态的原型也跳过
        continue
    # 背景原型 (is_background): 保留但标记
    # --- 过滤结束 ---
```

**关键设计**:
- 占位符原型（scope_note 含 "placeholder"）: **完全跳过**，不出现在候选列表中
- needs_literature 状态的原型: **跳过**
- 背景原型（background_only / superseded）: 保留在候选中但需要在 brief 中标记

#### Step 2: 在 brief 输出中标记背景原型

在构建 `brief_candidates` 时（约第 587 行），添加背景标记：

```python
# 在 brief_candidates.append({...}) 中添加
'prototype_status': {
    'is_background': is_background,
    'scope_note': proto.get('scope_note', ''),
    'superseded_by': _extract_superseded_by(proto_scope)  # 如 "diatom-frustule"
},
```

添加辅助函数：

```python
def _extract_superseded_by(scope_note):
    """从 scope_note 中提取 'superseded by XXX' 的替代原型 ID"""
    if not scope_note:
        return None
    import re
    m = re.search(r'superseded by ([\w-]+)', scope_note)
    return m.group(1) if m else None
```

#### Step 3: 对 5 个占位符原型添加 brief_visibility

作为双重保险（即使代码过滤逻辑遗漏，机制级别也有标记），在 5 个占位符原型的所有 mechanisms 中添加 `"brief_visibility": "hidden"`：

```bash
# 对以下 5 个文件执行:
# prototypes_db/biomineralization-template.json
# prototypes_db/coral-skeleton.json
# prototypes_db/dna-aptamer.json
# prototypes_db/magnetic-bacteria.json
# prototypes_db/mycelium.json
```

对每个文件的每个 mechanism，如果没有 `brief_visibility` 字段，添加 `"brief_visibility": "hidden"`。

#### Step 4: 在代码中添加 brief_visibility 检查（双重保险）

在 `_mech_score()` 或机制选择逻辑中，跳过 `brief_visibility == "hidden"` 的机制：

```python
# 在机制遍历前过滤
visible_mechs = [m for m in mechs if m.get('brief_visibility', 'visible') != 'hidden']
if not visible_mechs:
    continue  # 所有机制都隐藏，跳过此原型
mechs = visible_mechs
```

### B.5 验证

```bash
cd /Users/panyao/Desktop/Biomimetic-design-library

# 1. 验证占位符原型不再出现在查询结果中
python3 -c "
import sys; sys.path.insert(0, '.')
from tools.biomimetic_context import BiomimeticContext
ctx = BiomimeticContext()
# dna-aptamer 不在任何 feature_matching_rules 中，不会匹配到
# 但用 Pb(II) 查询，检查候选列表中无占位符原型
result = ctx.query('Pb(II)', {'pH': 6.0, 'temperature': 25})
candidates = result['brief']['candidates']
placeholder_ids = {'biomineralization-template', 'coral-skeleton', 'dna-aptamer', 'magnetic-bacteria', 'mycelium'}
found = [c['prototype_id'] for c in candidates if c['prototype_id'] in placeholder_ids]
assert not found, f'占位符原型出现在结果中: {found}'
print('占位符原型过滤验证通过')
"

# 2. 验证背景原型有标记
python3 -c "
import sys; sys.path.insert(0, '.')
from tools.biomimetic_context import BiomimeticContext
ctx = BiomimeticContext()
# 查询一个可能匹配到背景原型的污染物
result = ctx.query('Pb(II)', {'pH': 6.0, 'temperature': 25})
candidates = result['brief']['candidates']
for c in candidates:
    ps = c.get('prototype_status', {})
    if ps.get('is_background'):
        print(f'背景原型已标记: {c[\"prototype_id\"]} (scope: {ps.get(\"scope_note\", \"\")[:50]})')
print('背景原型标记验证通过')
"

# 3. 运行完整测试
python tools/generate_adrmats_briefs.py
```

**预期结果**:
- 所有 7 个测试用例 PASS
- 候选列表中不包含 5 个占位符原型
- 背景原型（如出现）有 `prototype_status.is_background: true`

### B.6 风险与注意事项

1. **不过度清理**: 8 个"活跃但机制少"的原型不处理 — 它们有真实机制，只是数量少，这是可以接受的
2. **背景原型保留**: 背景/被替代的原型不完全删除，因为它们的机制可能仍有参考价值，只是需要在 brief 中标记
3. **双重保险**: 代码级过滤 + 数据级 `brief_visibility` 两层防护，确保占位符不会泄漏到输出中

---

## 计划 C: feature_matching_rules 扩充

### C.1 目标

向 `feature_matching_rules.json` 的 `molecular_feature_to_prototype` 中添加 4 条缺失规则：
- 可配位
- 可电离
- 大分子
- 内分泌干扰

### C.2 证据数据（来自 2879 篇论文提参聚合）

| 特征 | 关联污染物数 | 论文总数 | evidence_count |
|------|------------|---------|----------------|
| 可配位 | 20 种 | 2879 篇 | 2879 |
| 可电离 | 19 种 | 2877 篇 | 2877 |
| 大分子 | 15 种 | 2839 篇 | 2839 |
| 内分泌干扰 | 1 种 (BPA) | 1416 篇 | 1416 |

### C.3 修改文件

`feature_matching_rules.json`

### C.4 具体步骤

#### Step 1: 在 `molecular_feature_to_prototype` 末尾添加 4 条规则

在 `"氯代"` 规则之后添加：

```json
    "可配位": {
      "prototypes": ["chitosan", "bone-structure"],
      "reason": "可配位的污染物分子含供电子原子（N/O/S），可与吸附剂上的金属活性位点或极性基团形成配位键",
      "weight": 0.6,
      "evidence_source": "20种有机污染物提参聚合（TCDD/PFOA/BPA/壬基酚等）",
      "evidence_count": 2879
    },
    "可电离": {
      "prototypes": ["chitosan"],
      "reason": "可电离污染物在不同pH下以不同形态存在，壳聚糖的氨基(-NH2/-NH3+)可随pH切换电荷状态实现pH依赖性吸附",
      "weight": 0.6,
      "evidence_source": "19种有机污染物提参聚合（TCDD/PFOA/BPA/壬基酚等）",
      "evidence_count": 2877
    },
    "大分子": {
      "prototypes": ["chitosan", "diatom-frustule"],
      "reason": "大分子污染物需要大孔径或柔性链状吸附材料，壳聚糖的高分子链可提供缠绕位点，硅藻土的介孔可提供空间限域",
      "weight": 0.5,
      "evidence_source": "15种有机污染物提参聚合（TCDD/PFOA/BPA/十溴二苯醚等）",
      "evidence_count": 2839
    },
    "内分泌干扰": {
      "prototypes": ["chitosan", "plant-tannin"],
      "reason": "内分泌干扰物多为含酚羟基的芳香族化合物，可通过氢键和π-π堆积与壳聚糖/植物单宁结合",
      "weight": 0.6,
      "evidence_source": "BPA提参聚合",
      "evidence_count": 1416
    }
```

**注意**: 添加后需确保 JSON 格式正确。`"氯代"` 条目末尾的 `}` 需改为 `},`，最后一条 `"内分泌干扰"` 的 `}` 后不需要逗号。

#### Step 2: 验证

```bash
cd /Users/panyao/Desktop/Biomimetic-design-library

# 1. JSON 格式验证
python3 -c "import json; d = json.load(open('feature_matching_rules.json', encoding='utf-8')); print(f'规则数: {len(d[\"molecular_feature_to_prototype\"])}')"

# 2. 新规则存在性验证
python3 -c "
import json
d = json.load(open('feature_matching_rules.json', encoding='utf-8'))
rules = d['molecular_feature_to_prototype']
for feat in ['可配位', '可电离', '大分子', '内分泌干扰']:
    assert feat in rules, f'{feat} 规则不存在!'
    print(f'{feat}: {rules[feat][\"prototypes\"]} (weight={rules[feat][\"weight\"]})')
print('全部 4 条新规则验证通过')
"

# 3. 功能验证
python tools/generate_adrmats_briefs.py
```

**预期结果**:
- `molecular_feature_to_prototype` 包含 17 条规则
- `generate_adrmats_briefs.py` 所有测试用例 PASS

---

## 计划 D: 101 条空字段溯源

### D.1 目标

通过 BMDL 自身文献溯源（非 2879 篇论文数据），解决 `prototypes_db/*.json` 中 101 条空 `pollutant` 字段。

### D.2 当前状态

| 指标 | 数量 |
|------|------|
| 空字段总数 | 101 条 |
| 有 DOI 的 | 71 条（可溯源） |
| 有 material 的 | 48 条 |
| 有 DOI + material 的 | 42 条 |
| 两者都没有的 | 24 条（无法溯源） |

按原型分布（Top 5）：

| 原型 | 空字段数 | 有DOI | 有material |
|------|---------|-------|-----------|
| chitosan | 40 | 32 | 18 |
| cell-membrane-ion-channel | 11 | 11 | 11 |
| mussel-foot-adhesion | 9 | 5 | 3 |
| polydopamine-coating | 9 | 3 | 5 |
| superhydrophobic-artificial | 8 | 0 | 1 |

### D.3 修改文件

- `prototypes_db/*.json`（15 个原型文件中的空字段）
- 新建 `docs/active/empty-field-traceability-log.md`（溯源日志）

### D.4 具体步骤

#### Step 1: 提取所有空字段信息

编写 Python 脚本，提取所有 101 条空字段的 DOI、material、原型 ID，输出为 `docs/active/empty-fields-extract.json`。

#### Step 2: 通过 Crossref API 溯源 DOI

对 71 条有 DOI 的空字段，调用 Crossref API（`https://api.crossref.org/works/{DOI}`）获取文献元数据（标题、摘要）。API 调用间隔 1 秒。

#### Step 3: 从文献标题/摘要识别污染物名称

使用 `pollutant_aliases.json` 的别名列表进行关键词匹配：
- 匹配到 1 个 → `confidence: high`
- 匹配到多个 → `confidence: medium`（需人工审核）
- 未匹配 → `confidence: none`（保持空值）

#### Step 4: 人工审核并回填

1. `confidence: high` → 直接采用
2. `confidence: medium` → 人工查看标题/摘要确认
3. `confidence: none` → 保持空值
4. 确认后修改对应 `prototypes_db/*.json` 的 `performance_data[index].pollutant` 字段

#### Step 5: 编写溯源日志

创建 `docs/active/empty-field-traceability-log.md`，记录溯源日期、总数、成功数、未回填列表。

### D.5 验证

```bash
cd /Users/panyao/Desktop/Biomimetic-design-library

# 验证回填后空字段减少
python3 -c "
import json, os, glob
count = 0
for f in glob.glob('prototypes_db/*.json'):
    with open(f, encoding='utf-8') as fh:
        data = json.load(fh)
    for pd in data.get('performance_data', []):
        if not pd.get('pollutant', '').strip():
            count += 1
print(f'剩余空字段: {count} (原: 101)')
"

# 运行 brief 生成确认无回归
python tools/generate_adrmats_briefs.py
```

### D.6 风险与注意事项

1. **知识隔离**: 溯源使用 Crossref API，不使用 2879 篇论文的提参数据
2. **人工审核必须**: `confidence: medium` 的记录必须人工确认
3. **备份优先**: 回填前确认 `prototypes_db.bak/` 存在
4. **24 条无法溯源**: 没有 DOI 也没有 material 的保持原状
5. **不混合材料体系**: 溯源识别的污染物名称必须与 BMDL 自身的仿生吸附文献体系一致

---

## 交接文档: 污染物数据集成 → Axl_Huang

### 背景

2879 篇有机污染物吸附文献的提参结果存储在 `pollutant_knowledge_base/summaries/` 下（20 个 JSON 文件），当前**完全独立于 BMDL 查询流程**。这部分数据可能在 BMDL 和 ADRMATS 其他模块中都会用到，交给 Axl_Huang 评估和实施集成。

### 数据描述

#### 文件位置

```
pollutant_knowledge_base/summaries/
├── 2,3,7,8-四氯二苯并-p-二噁英（TCDD）.json
├── 2,6-二氯苯酚.json
├── β-六氯环己烷.json
├── 三氯甲烷.json
├── 五氯苯酚.json
├── 全氟丁烷磺酸（PFBS）.json
├── 全氟己烷磺酸（PFHxS）.json
├── 全氟辛酸（PFOA）.json
├── 六氟环氧丙烷二聚酸.json
├── 六氯丁二烯.json
├── 十溴二苯醚.json
├── 双酚A（BPA）.json
├── 壬基酚.json
├── 多氯联苯-209（PCB-209）.json
├── 奥克立林.json
├── 滴滴伊（DDE）.json
├── 滴滴涕（DDT）.json
├── 狄氏剂（Dieldrin）.json
├── 硫丹.json
└── 罗红霉素.json
```

#### Summary 文件结构（以 PFOA 为例）

```json
{
  "pollutant_name": "全氟辛酸（PFOA）",
  "paper_count": 275,           // 该污染物相关论文数
  "total_ki": 3182,              // 提取的知识项总数
  "ki_by_domain": {...},         // 按域分类的知识项统计
  "properties": {                // 污染物基本性质（可直接增益 BMDL）
    "APFO分子量": [{"value": "431", "unit": "g/mol", "ref_doi": "...", "confidence": 1.0}],
    "C-F键能": [{"value": "451.9", "unit": "kJ/mol", ...}],
    ...
  },
  "removal_mechanisms": [        // 文献报道的去除机理（可直接增益 BMDL）
    {"mechanism": "吸附", "evidence_count": 288, "key_references": [...], "details": [...]},
    {"mechanism": "静电", "evidence_count": 134, ...},
    {"mechanism": "疏水", "evidence_count": 133, ...},
    ...  // 共 11 种机理，按证据量排序
  ],
  "adsorption_performance": {    // 吸附性能数据（不可与 BMDL performance_data 混合）
    "best_materials": [
      {"material": "MOF", "qmax_mg_g": 419.8, "evidence_count": 47},
      {"material": "活性炭", "qmax_mg_g": 720.0, "evidence_count": 45},
      ...
    ]
  },
  "molecular_features_for_biomimetic_matching": [
    "可电离", "可配位", "大分子", "弱酸性", "氟碳链", "水溶性", "疏水性", "芳香环"
  ],
  "recommended_biomimetic_prototypes": ["chitosan", "lotus-leaf", "plant-tannin", "polydopamine-coating"]
}
```

#### 为 BMDL 集成设计的关键字段

| 字段 | 用途 | 增益目标 |
|------|------|---------|
| `molecular_features_for_biomimetic_matching` | 补充 pollutant_profile 的 molecular_features | 增强 feature-based 匹配 |
| `removal_mechanisms` | 补充 honesty_ledger 的 facts | 提供文献支撑的去除路径证据 |
| `recommended_biomimetic_prototypes` | 补充候选列表 | 提供文献推荐的仿生原型 |
| `properties` | 补充 pollutant_profile 的物化性质 | 增强污染物画像 |
| `adsorption_performance` | **不使用** | 知识隔离：不与 BMDL performance_data 混合 |

### 集成方案（原计划 A，供 Axl_Huang 参考）

#### 需要修改的文件

`tools/biomimetic_context.py`（唯一需要修改的 BMDL 代码）

#### 集成步骤概要

1. **在 `__init__` 中加载 summaries**: 遍历 `pollutant_knowledge_base/summaries/*.json`，以 `pollutant_name` 为 key 存储
2. **新增 `get_pollutant_summary(pollutant)` 方法**: 精确匹配 + 模糊匹配 + 别名匹配
3. **在 `query()` 中用 summary 增强 `pollutant_profile`**: 将 `molecular_features_for_biomimetic_matching` 合并到 profile（只追加不覆盖）
4. **在 `query()` 中用 summary 的 `removal_mechanisms` 增强 `honesty_ledger`**: 作为 `facts` 添加，标注来源"文献聚合(N篇)"
5. **用 summary 的 `recommended_biomimetic_prototypes` 补充候选**: weight 0.4，标注 `match_basis: "summary_recommendation"`

### 知识隔离规则（不可违反）

1. **不修改** `prototypes_db/*.json` 中的任何数据
2. **不混合** summary 的 `adsorption_performance` 与 BMDL 的 `performance_data`（两个不同材料体系）
3. summary 数据作为**只读参考**，不写入 BMDL 核心数据文件
4. 增益仅限：污染物基本性质 + 文献报道的去除机理

### BMDL 的正确增益边界

2879 篇论文对 BMDL 的增益仅限两类：
1. **污染物基本性质**（分子式、分子量、logP、pKa、溶解度等）
2. **文献报道的去除机理**（作用力类型、贡献比例等）

这两类信息用于辅助仿生匹配前的污染物认知，不参与 BMDL 原型自身的 performance_data。

### ADRMATS 其他模块可能的复用

Axl_Huang 需要评估以下数据在 ADRMATS 其他模块（非 BMDL）中的复用价值：

| 数据 | 可能的 ADRMATS 模块 | 用途 |
|------|-------------------|------|
| `properties` | 约束智能体 | 水质约束分析时参考污染物物化性质 |
| `removal_mechanisms` | 去除机理智能体 | 直接作为已知去除路径输入 |
| `adsorption_performance` | 性能评估模块 | 作为性能基准参考（不与 BMDL 混合） |
| `molecular_features_for_biomimetic_matching` | BMDL + 特征匹配模块 | 仿生原型匹配的特征输入 |
| `recommended_biomimetic_prototypes` | BMDL | 文献推荐的仿生原型补充候选 |

### 关键文件索引

| 文件 | 行数 | 说明 |
|------|------|------|
| `tools/biomimetic_context.py` | 1127 | BMDL 对 ADRMATS 的核心接口类 |
| `feature_matching_rules.json` | 304 | 4 层匹配规则（分子特征/相互作用/类别/场景） |
| `pollutant_profiles.json` | - | 静态污染物画像（待被 summary 增强） |
| `pollutant_aliases.json` | - | 污染物别名映射 |
| `feature-mapping.json` | - | 直接实验证据映射 |
| `pollutant_knowledge_base/summaries/*.json` | 20 个文件 | 2879 篇论文提参聚合 |

### BiomimeticContext 关键方法位置

| 方法 | 行号 | 说明 |
|------|------|------|
| `__init__` | 51-93 | 初始化，加载 6 个数据源（待增加 summaries） |
| `get_pollutant_profile` | 94-117 | 获取污染物画像（待被 summary 增强） |
| `find_direct_evidence` | 130-200 | 查找直接实验数据 |
| `find_feature_based` | 202-281 | 基于分子特征匹配原型 |
| `query` | 343-700 | 主查询接口（待集成 summary） |
| `find_applicable_rules` | 283-341 | 查找适用设计规则 |

---

## 执行顺序建议

```
计划 B（占位符过滤 + 代码修复）← 最紧急，防止占位符泄漏到 ADRMATS
    ↓ 验证通过
计划 C（feature_matching_rules 扩充）← 最简单，纯数据修改
    ↓ 验证通过
计划 A.优先级1（brief 输出暴露 basis）← 小改动，高价值
    ↓ 验证通过
计划 D（101 条空字段溯源）← 独立工作，可并行
    ↓
计划 A.优先级2-4（verification 升级 + boundary 验证）← 长期工作，按原型分批
    ↓
交接文档 → Axl_Huang 评估并实施污染物数据集成
```

**理由**:
- **B 先行**: 占位符原型当前会泄漏到查询结果中，这是最紧急的代码缺陷
- **C 次之**: 纯数据修改，简单且为后续 A 优先级 2 的规则匹配提供基础
- **A.优先级1**: 小改动（在 `_get_mechanism_boundaries` 中暴露 basis 字段），但让 ADRMATS 能区分 LLM 推理和文献支撑的边界条件
- **D 独立**: 空字段溯源不依赖其他计划，可并行
- **A.优先级2-4**: 长期工作，需要逐原型文献溯源
- **交接文档**: 立即可用，Axl_Huang 可随时开始评估

---

## 附录: 44 个原型分类总览

| 分类 | 数量 | 原型 | 处理方式 |
|------|------|------|---------|
| 充实原型 | ~5 | chitosan, polydopamine-coating, mussel-foot-adhesion, silk-fibroin, spider-silk | 数据可靠度优化重点 |
| 活跃但机制少 | 8 | bird-feather-keratin, fungal-biosorption, insect-chitin, microbial-exopolysaccharide, namib-beetle, plant-wax-cuticle, rice-husk-phytolith, sulfate-reducing-bacteria | 无需处理（有真实机制） |
| 背景原型 | 7 | diatom-inspired-porous, lotus-leaf, pitcher-plant-slippery-surface, shark-skin, silkworm-silk, superhydrophobic-artificial, water-strider-leg | 代码过滤+标记 |
| 占位符原型 | 5 | biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria, mycelium | 代码过滤+brief_visibility |
| 其他活跃原型 | ~19 | bone-structure, cactus-spine, cell-membrane-ion-channel, ... | 按需优化 |
