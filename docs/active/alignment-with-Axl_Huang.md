# 与 Axl_Huang 对齐清单 + BMDL 有机污染物融入建议

> 日期: 2026-06-28（更新于 6-29）
> 用途: 与 Axl_Huang 对齐讨论用
> 前置文档: docs/active/handoff-to-Axl_Huang.md
> BMDL 状态: 所有可做的提升已穷尽，可交付。HEAD = 2936baa

---

## 一、对齐清单

### 1. BMDL 侧有机污染物融入——路线确认

**背景**：交接文档（handoff-to-Axl_Huang.md 第 4 节）给了 5 步方案修改 `biomimetic_context.py` 加载 summaries。但 Axl_Huang 6/27 的 commit（`bddb889`）走了另一条路——创建了独立 SQLite DB + CrewAI 工具挂在 ConstraintAgent 上。

**需要对齐**：
- Axl_Huang 是打算用 ConstraintAgent 工具**替代** BMDL 侧融入，还是**还没做** BMDL 侧？
- 如果替代：BMDL 查有机污染物仍然返回全 inference，是否可接受？
- 如果还没做：交接文档的 5 步方案是否仍然有效？

### 2. BiomimeticMatchingAgent 的 BmdlAdapter

**背景**：ADRMATS 有 `BiomimeticMatchingAgent`（双模式：BMDL grounded / LLM fallback），通过 `BmdlAdapter` 查询 BMDL。

**需要对齐**：
- `BmdlAdapter` 调用的是 `biomimetic_context.py` 的 `query()` 吗？
- 如果是，那 BMDL 侧的有机污染物画像融入仍然必要——否则 BMDL 对有机污染物永远 miss，BiomimeticMatchingAgent 永远走 LLM fallback
- 这是否是预期行为？

### 3. 第 8 维门控（已确认）

**结论**：第 8 维是独立门控（`biomimetic_gate_judge.yaml`），评"仿生转译保真度"（organism → mechanism → motif → material feature），不参与 7 维加权评分。已对齐，无需讨论。

**但需提及**：BMDL brief 的质量影响门控精度。functional_groups/key_structures 已从 8%/4% 补到 84%/89%（见第 4 项），机制评分质量已显著改善，门控基准偏移风险降低。

### 4. functional_groups / key_structures 补全 ✅ 已完成

**结果**：functional_groups 从 8%→84% 有，key_structures 从 4%→89% 有。剩余 16%/11% 主要是背景原型（超疏水等）的物理机制，不含化学官能团，空着合理。commit: `a29872d`。

### 5. ADRMATS requirements.txt 缺少 psycopg2-binary

运行 ADRMATS 时发现 `requirements.txt` 缺少 `psycopg2-binary`（PostgreSQL 驱动），导致项目无法连接数据库。加上 `psycopg2-binary>=2.9.0` 后正常。

**建议**：在 ADRMATS 的 `requirements.txt` 中补上这一条。

### 6. feature_matching_rules 的 pollutant_features 为空

**现状**：17 条 `molecular_feature_to_prototype` 规则的 `pollutant_features` 字段全部为空 `[]`。

**建议**：用提参 summary 的 `molecular_features_for_biomimetic_matching` 反向填充——比如"芳香环"这条规则填入 `['BPA', '壬基酚', 'TCDD', ...]`。但这个优先级低，因为匹配靠 key 名称已经能工作。

---

## 二、补充建议：污染物数据如何介入 BMDL

### 问题陈述

BMDL 查询有机污染物时返回**全 inference** 候选（如 BPA: 8候选 0f/0l/5i）。原因：

1. ~~`pollutant_profiles.json` 只有重金属~~ **已解决**：现有 44 种污染物画像，含 BPA(9特征)、PFOA(12特征)、壬基酚、TCDD 等 20 种有机污染物
2. `find_feature_based()` 已能匹配——BPA 的 9 个特征匹配 17 条规则中的 5 条（可电离/可配位/大分子/芳香环/内分泌干扰），返回 feature-based 候选
3. 但 `find_direct_evidence()` 无有机污染物的直接证据映射（`feature-mapping.json` 无 BPA 条目）
4. **有机污染物门控**（代码第 580-582 行）：无直接证据时强制 `honesty=inference`

结论：BMDL **已能返回候选**，但诚实度被门控限制在 inference。要升级到 lead，需要第二层（直接证据映射）。

### 建议方案：最小改动 + 分层融入

#### 第一层：污染物画像融入 ✅ 已完成

`pollutant_profiles.json` 已有 44 种污染物（含 20 种有机污染物），BPA 有 9 个 molecular_features，PFOA 有 12 个。`find_feature_based()` 已能返回有机污染物的 feature-based 候选。不需要再做。

#### 第二层：直接证据映射（建议验证后做）

**做什么**：用 summary 的 `recommended_biomimetic_prototypes` 在 `feature-mapping.json` 中创建直接证据条目。

**改什么**：在 `feature-mapping.json` 中新增有机污染物 → 原型的映射，比如：
```json
{"pollutant": "BPA", "prototype_id": "chitosan", "evidence_type": "literature_aggregation", "confidence": 0.6}
```

**风险**：中等。需要验证 BMDL 中该原型是否有对应机制能解释该污染物的去除。比如 summary 推荐 chitosan 适合 BPA，但 BMDL 的 chitosan 机制中是否有"氢键吸附酚类"的机制？如果没有，直接证据映射会导致查询返回 chitosan 但选中的机制不匹配。

**建议**：先批量匹配，再用 LLM 逐条审核——"BPA 的酚羟基 + chitosan 的氨基 → 氢键吸附"是否在 chitosan 的机制描述中有对应。

#### 第三层：去除机理补强 ✅ 已完成（用替代方案）

已用 LLM 从机制 name/description/causal_chain 中提取 functional_groups 和 key_structures，从 8%/4% 补到 84%/89%。剩余缺口主要是背景原型（超疏水等）的物理机制，不含化学官能团。没有使用提参 summary 的 removal_mechanisms（避免跨体系语义映射风险）。commit: `a29872d`。

### 知识隔离红线（不可违反）

| 可用 | 不可用 |
|------|--------|
| `molecular_features_for_biomimetic_matching` | `adsorption_performance`（qmax 等） |
| `recommended_biomimetic_prototypes` | `engineering_constraints` |
| `removal_mechanisms`（仅机理类型） | `occurrence_patterns` |
| `properties`（物化性质） | — |

**铁律**：summary 数据作为只读参考，不写入 `prototypes_db/*.json`。前车之鉴：之前用匹配矩阵回填 71 条空 pollutant 字段导致系统性误分类，已全部回退。

### 与 Axl_Huang 现有工作的关系

Axl_Huang 已做的 ConstraintAgent pollutant KB 工具和第一层方案**不冲突**：
- Axl_Huang 的工具让 ConstraintAgent 能查询污染物文献（ADRMATS 侧增强）
- 第一层方案让 BMDL 能查有机污染物（BMDL 侧增强）
- 两者互补：ConstraintAgent 提供水质约束上下文，BMDL 提供仿生候选

但如果 Axl_Huang 打算让 ConstraintAgent 工具**替代** BMDL 侧融入，则需要讨论：
- BMDL 的 BiomimeticMatchingAgent 对有机污染物将永远走 LLM fallback
- 第 8 维门控的 brief 将完全由 LLM 生成，没有 BMDL 的 grounded evidence
- 这是否可接受？
