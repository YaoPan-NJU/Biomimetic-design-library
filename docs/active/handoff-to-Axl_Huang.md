# 交接文档：污染物提参数据 → BMDL & ADRMATS 集成

> 收件人: Axl_Huang
> 发件人: Yao
> 日期: 2026-06-25
> 仓库: https://github.com/YaoPan-NJU/Biomimetic-design-library.git
> 分支: review

---

## 1. 当前状况

### 1.1 我（Yao）在干什么

我正在本地执行 BMDL 数据库的修复和优化计划（4 个子计划，按顺序执行）：

| 计划 | 内容 | 状态 |
|------|------|------|
| B | 占位符原型过滤（5 个真占位符 + 7 个背景原型的代码过滤） | 待执行 |
| C | feature_matching_rules 扩充（新增 4 条分子特征规则） | 待执行 |
| A | 数据可靠度优化（暴露 LLM basis 字段 → verification 升级 → boundary_rules 填充） | 待执行 |
| D | 101 条空 pollutant 字段的 Crossref 溯源 | 待执行 |

详细执行计划见 `docs/active/execution-plans-ABC.md`（本地文档，不在仓库中）。

**预期结果**: 执行完成后，BMDL 的占位符原型不再泄漏到查询结果，feature_matching_rules 覆盖更全面，brief 输出能区分 LLM 推理和文献支撑的边界条件。

### 1.2 你（Axl_Huang）需要干什么

1. **评估并实施 2879 篇污染物提参数据接入 BMDL 查询流程**
2. **评估这些数据在 ADRMATS 其他模块中的复用价值**

核心任务：让 BMDL 在查询时能读取 `pollutant_knowledge_base/summaries/` 下的污染物摘要，用文献报道的去除机理和分子特征增强候选匹配和诚实度评估。

---

## 2. 数据概览

2879 篇有机污染物吸附文献的 LLM 提参结果，覆盖 20 种污染物，存储在 `pollutant_knowledge_base/` 下。

### 2.1 统计

| 指标 | 数值 |
|------|------|
| 总论文 | 2879 |
| 总 KI (knowledge items) | 27592 |
| 覆盖污染物 | 20 种 |
| confidence ≥ 0.8 的 KI | 27005 (97.9%) |

### 2.2 20 种污染物

双酚A (BPA, 1416篇), 全氟辛酸 (PFOA, 275篇), 十溴二苯醚 (236篇), 滴滴涕 (DDT, 230篇), 五氯苯酚 (171篇), 壬基酚 (152篇), TCDD (122篇), PFBS (67篇), 狄氏剂 (53篇), PFHxS (33篇), 六氟环氧丙烷二聚酸 (32篇), 三氯甲烷 (26篇), 2,6-二氯苯酚 (13篇), DDE (12篇), 罗红霉素 (10篇), β-六氯环己烷 (9篇), 硫丹 (8篇), 奥克立林 (8篇), 六氯丁二烯 (4篇), PCB-209 (2篇)

### 2.3 文件结构

```
pollutant_knowledge_base/
├── by_pollutant/*/                    # 2879 个原始提参 JSON（逐篇）
├── summaries/                         # ← 你主要读这里
│   ├── <污染物>.json                  # 20 个聚合摘要
│   └── adsorption_performance_flat.jsonl
├── biomimetic_matching/
│   ├── matching_matrix.json           # 加权匹配矩阵
│   ├── matching_matrix.md             # 人类可读推荐表
│   └── rule_gaps.md                   # 规则缺口分析
├── audit/
│   ├── quality_audit_report.json
│   └── empty_results_analysis.md
└── pollutant_aggregate_index.json
```

---

## 3. Summary JSON 结构（你集成的核心数据源）

每种污染物的摘要文件（`summaries/<污染物>.json`）结构如下，以 PFOA 为例：

```json
{
  "pollutant_name": "全氟辛酸（PFOA）",
  "paper_count": 275,
  "total_ki": 3182,
  "ki_by_domain": { ... },
  "properties": {                // ← BMDL 可用：污染物物化性质
    "APFO分子量": [{"value": "431", "unit": "g/mol", "ref_doi": "...", "confidence": 1.0}],
    "C-F键能": [{"value": "451.9", "unit": "kJ/mol", ...}],
    ...
  },
  "removal_mechanisms": [        // ← BMDL 核心增益：文献报道的去除机理
    {"mechanism": "吸附", "evidence_count": 288, "key_references": [...], "details": [...]},
    {"mechanism": "静电", "evidence_count": 134, ...},
    {"mechanism": "疏水", "evidence_count": 133, ...},
    // 共 11 种机理，按证据量降序
  ],
  "adsorption_performance": {    // ← BMDL 不可使用（见知识隔离规则）
    "best_materials": [
      {"material": "MOF", "qmax_mg_g": 419.8, "evidence_count": 47},
      ...
    ]
  },
  "molecular_features_for_biomimetic_matching": [  // ← BMDL 可用：触发匹配规则的特征
    "可电离", "可配位", "大分子", "弱酸性", "氟碳链", "水溶性", "疏水性", "芳香环"
  ],
  "recommended_biomimetic_prototypes": ["chitosan", "lotus-leaf", "plant-tannin", "polydopamine-coating"],
  "engineering_constraints": [...],   // ADRMATS 其他模块可用
  "occurrence_patterns": [...]         // ADRMATS 其他模块可用
}
```

### PFOA 去除机理分布（示例）

| 机理 | evidence_count | 贡献占比 |
|------|----------------|----------|
| 吸附 | 288 | 35.4% |
| 静电 | 134 | 16.5% |
| 疏水 | 133 | 16.4% |
| 氢键 | 47 | 5.8% |
| 离子交换 | 30 | 3.7% |
| 氧化 | 17 | 2.1% |
| 配位 | 11 | 1.4% |
| π-π | 7 | 0.9% |

---

## 4. BMDL 集成方案

### 4.1 哪些字段给 BMDL 用

| 字段 | 用途 | 增益目标 |
|------|------|---------|
| `molecular_features_for_biomimetic_matching` | 合并到 pollutant_profile | 增强 feature-based 匹配 |
| `removal_mechanisms` | 加入 honesty_ledger 的 facts | 文献支撑的去除路径 |
| `recommended_biomimetic_prototypes` | 补充候选列表 | 文献推荐的仿生原型 |
| `properties` | 合并到 pollutant_profile | 增强污染物画像 |
| `adsorption_performance` | **不用** | 知识隔离（见第 5 节） |

### 4.2 改哪个文件

`tools/biomimetic_context.py`（唯一需要改的 BMDL 代码）

### 4.3 集成步骤

1. **`__init__` 中加载 summaries**（第 51-93 行）
   遍历 `pollutant_knowledge_base/summaries/*.json`，以 `pollutant_name` 为 key 存储

2. **新增 `get_pollutant_summary(pollutant)` 方法**
   精确匹配 + 模糊匹配 + 别名匹配（用 `pollutant_aliases.json`）

3. **`query()` 中增强 `pollutant_profile`**（第 343-700 行）
   将 summary 的 `molecular_features_for_biomimetic_matching` 合并到 profile（只追加不覆盖）

4. **`query()` 中增强 `honesty_ledger`**
   summary 的 `removal_mechanisms` 作为 facts 添加，标注来源 "文献聚合(N篇)"

5. **`query()` 中补充候选**
   summary 的 `recommended_biomimetic_prototypes` 作为补充候选，weight 0.4，标注 `match_basis: "summary_recommendation"`

### 4.4 BiomimeticContext 关键方法位置

| 方法 | 行号 | 说明 |
|------|------|------|
| `__init__` | 51-93 | 初始化，加载 6 个数据源（待增加 summaries） |
| `get_pollutant_profile` | 94-117 | 获取污染物画像（待被 summary 增强） |
| `find_direct_evidence` | 130-200 | 查找直接实验数据 |
| `find_feature_based` | 202-281 | 基于分子特征匹配原型 |
| `query` | 343-700 | 主查询接口（待集成 summary） |
| `find_applicable_rules` | 283-341 | 查找适用设计规则 |

### 4.5 BMDL 当前查询流程（集成前的现状）

```
query(pollutant, water_quality, engineering_constraints)
  ├─ get_pollutant_profile(pollutant)       → 静态画像（pollutant_profiles.json）
  ├─ find_direct_evidence(pollutant)        → 直接实验数据（feature-mapping.json）
  ├─ find_feature_based(pollutant_profile)  → 4层匹配（feature_matching_rules.json）
  ├─ 合并候选 → gold_set 过滤
  ├─ 逐候选构建 brief（机制评分 / 诚实度分类 / 有机污染物门控）
  ├─ 构建 honesty_ledger (facts / leads / inferences)
  ├─ find_applicable_rules()               → 按 water_quality 匹配设计规则
  └─ return brief
```

注意：`water_quality`（pH/温度/盐度）用于机制评分和设计规则匹配，**不从水质推断污染物**。污染物名称由 ADRMATS 直接传入。

---

## 5. 知识隔离规则（核心红线，不可违反）

### 5.1 两个不同的材料体系

| 知识体系 | 数据来源 | 存储位置 |
|----------|----------|----------|
| BMDL 仿生知识库 | 仿生吸附文献（手工提取） | `prototypes_db/*.json` |
| 有机污染物提参库 | 2879 篇有机污染物论文（LLM 提参） | `pollutant_knowledge_base/` |

**这两个体系不可混合。**

### 5.2 BMDL 只取两类信息

1. **污染物基本性质** — 分子式、分子量、logP、pKa、溶解度等
2. **文献报道的去除机理** — 作用力类型、贡献比例等

### 5.3 不取的信息

- `adsorption_performance` — qmax 等性能数据，属于吸附材料体系，不是仿生原型性能
- `engineering_constraints` — 吸附材料的工程约束
- `occurrence_patterns` — 环境含量

### 5.4 前车之鉴

之前有人尝试用 2879 篇论文的匹配矩阵回填 BMDL `prototypes_db` 中 101 条空 `pollutant` 字段，回填 71 条后发现系统性误分类（重金属吸附数据被标记为"壬基酚"），已全部回退。根因就是混合了两个材料体系。

**铁律**: summary 数据作为只读参考，不写入 `prototypes_db/*.json`。

---

## 6. ADRMATS 其他模块复用

2879 篇论文提取的特征不仅在 BMDL 中有用，请评估以下数据在其他模块的复用：

| 数据 | 可能的模块 | 用途 |
|------|-----------|------|
| `properties` | 约束智能体 | 水质约束分析时参考污染物物化性质 |
| `removal_mechanisms` | 去除机理智能体 | 已知去除路径输入 |
| `adsorption_performance` | 性能评估模块 | 性能基准（不与 BMDL 混合） |
| `molecular_features_for_biomimetic_matching` | 特征匹配模块 | 仿生原型匹配的特征输入 |
| `engineering_constraints` | 工程约束智能体 | 吸附材料工程约束参考 |
| `occurrence_patterns` | 环境评估模块 | 污染物环境含量分布 |

---

## 7. 已知问题与缺口

### 7.1 BMDL 原型分类（我在处理中）

| 分类 | 数量 | 说明 |
|------|------|------|
| 占位符原型 | 5 | biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria, mycelium — 机制全 LLM 生成，我在计划 B 中过滤 |
| 背景原型 | 7 | lotus-leaf, superhydrophobic-artificial 等 — 被重新分类，我在计划 B 中标记 |
| 活跃但机制少 | 8 | bird-feather-keratin 等 — 有真实机制，无需处理 |
| 充实原型 | ~5 | chitosan, polydopamine 等 — 数据可靠度优化重点 |
| 其他活跃 | ~19 | 正常 |

### 7.2 代码缺陷（我在修复中）

`biomimetic_context.py` 的 `query()` 方法当前不检查 `scope_note`/`evidence_status`/`brief_visibility` 等字段，占位符和背景原型会泄漏到查询结果。我在计划 B 中修复。

### 7.3 规则缺口

当前 `feature_matching_rules.json` 有 13 条分子特征规则，缺少"可配位""可电离""大分子""内分泌干扰"等。我在计划 C 中扩充。

### 7.4 原型缺口

以下机理在提参数据中高频出现但 BMDL 无对应原型：

| 机理 | 出现频次 | 说明 |
|------|----------|------|
| π-π | 17/20 种 | 芳香族污染物通用，无专用原型 |
| 氧化 | 14/20 | 无氧化原型 |
| 生物降解 | 5/20 | sulfate-reducing-bacteria 部分对应 |
| 光降解 | 3/20 | 无光催化原型 |
| 螯合 | 4/20 | 无专用螯合原型 |

这部分需要你评估是否需要新增原型。

---

## 8. 接口契约

根据 `docs/active/adrmats-interface-contract.md`：

- BMDL 是**启发式候选检索模块**，返回候选 + 诚实证据
- **不按性能值排名** — `match.weight` 是特征匹配得分，不是性能得分
- 诚实度分层: fact → lead → inference
- 有机污染物门控: 无直接证据时强制 inference

---

## 9. 关键文件索引

| 文件 | 说明 |
|------|------|
| `tools/biomimetic_context.py` (1127行) | BMDL 核心接口，你需要改这里 |
| `feature_matching_rules.json` | 4层匹配规则（我在扩充） |
| `pollutant_profiles.json` | 静态污染物画像（待被 summary 增强） |
| `pollutant_aliases.json` | 污染物别名映射 |
| `feature-mapping.json` | 直接实验证据映射 |
| `design-rules.json` | pH/温度条件规则 |
| `prototypes_db/*.json` | 44个仿生原型（**只读，不修改**） |
| `pollutant_knowledge_base/summaries/*.json` | 20个污染物摘要（你的数据源） |
| `pollutant_knowledge_base/biomimetic_matching/matching_matrix.md` | 人类可读匹配推荐表 |
| `docs/active/adrmats-interface-contract.md` | ADRMATS 接口契约 |
| `docs/active/pollutant-extraction-summary-and-bmdl-integration-guide.md` | 更详细的提参总结和集成指南 |
