# 2879 篇有机污染物提参结果总结 + BMDL 集成指南

日期: 2026-06-27
状态: ready-for-review
作者: claude-code (mac mini)

---

## 1. 提参结果概述

### 1.1 总体统计

| 指标 | 数值 |
|------|------|
| 总论文 | 2879 |
| 总 KI (knowledge items) | 27592 |
| 平均每篇 KI | 9.6 |
| 空结果论文 (0 KI) | 360 (12.5%) |
| 覆盖污染物 | 20 种 |
| 总体完整性评分 | 99.9% |
| confidence ≥ 0.8 的 KI | 27005 (97.9%) |

### 1.2 20 种污染物论文分布

| 污染物 | 论文数 | KI 总数 | 空论文 |
|--------|--------|---------|--------|
| 双酚A (BPA) | 1416 | 11800 | 286 |
| 全氟辛酸 (PFOA) | 275 | 3185 | 10 |
| 十溴二苯醚 | 236 | 2660 | 1 |
| 滴滴涕 (DDT) | 230 | 1754 | 54 |
| 五氯苯酚 | 171 | 1812 | 1 |
| 壬基酚 | 152 | 1764 | 5 |
| 2,3,7,8-四氯二苯并-p-二噁英 (TCDD) | 122 | 1221 | 2 |
| 全氟丁烷磺酸 (PFBS) | 67 | 872 | 0 |
| 狄氏剂 (Dieldrin) | 53 | 579 | 0 |
| 三氯甲烷 | 26 | 254 | 1 |
| 全氟己烷磺酸 (PFHxS) | 33 | 428 | 0 |
| 六氟环氧丙烷二聚酸 | 32 | 440 | 0 |
| β-六氯环己烷 | 9 | 94 | 0 |
| 奥克立林 | 8 | 78 | 0 |
| 硫丹 | 8 | 98 | 0 |
| 2,6-二氯苯酚 | 13 | 188 | 0 |
| 滴滴伊 (DDE) | 12 | 152 | 0 |
| 罗红霉素 | 10 | 133 | 0 |
| 六氯丁二烯 | 4 | 61 | 0 |
| 多氯联苯-209 (PCB-209) | 2 | 19 | 0 |

### 1.3 KI 按领域分布

| 领域 (domain_direction) | KI 数 | 占比 |
|--------------------------|-------|------|
| D1_adsorption_performance | 8241 | 29.9% |
| D4_adsorption_mechanism | 4767 | 17.3% |
| D11_pollutant_property | 3620 | 13.1% |
| D5_engineering_constraint | 3080 | 11.2% |
| D2_material_structure | 2899 | 10.5% |
| D12_occurrence_pattern | 2368 | 8.6% |
| D6_pollutant_application | 1371 | 5.0% |
| D8_characterization | 621 | 2.3% |
| D7_synthesis_method | 519 | 1.9% |
| D9_comparison_review | 106 | 0.4% |

### 1.4 质量审计结果

- **domain_direction 异常**: 25 条拼写错误已修复 (见 `audit/dd_fix_log.json`)
- **字段缺失率**: <0.1% (title 3, doi 4, abstract 9, year 4)
- **低 confidence KI**: 31 条 <0.5 未参与聚合，556 条 0.5-0.79 标记 `low_confidence` 参与聚合
- **空结果论文**: 360 篇 (BPA 286篇、DDT 54篇为主)，分析见 `audit/empty_results_analysis.md`

---

## 2. 知识隔离原则（核心红线）

### 2.1 两个独立的知识体系

| 知识体系 | 数据来源 | 存储位置 | 内容 |
|----------|----------|----------|------|
| **BMDL 仿生知识库** | 仿生吸附文献 (手工提取) | `prototypes_db/*.json` | 43 个仿生原型，502 条 performance_data，feature_matching_rules |
| **有机污染物提参库** | 2879 篇有机污染物论文 (LLM 提参) | `pollutant_knowledge_base/` | 20 种污染物的物化性质、去除机理、吸附性能、工程约束 |

**这两个体系属于不同材料体系，不可混为一体。**

### 2.2 BMDL 从 2879 篇论文获取的正确增益

BMDL 从 2879 篇论文的提参结果中**仅获取以下两类信息**：

1. **污染物基本性质** — 物化性质摘要（分子式、分子量、logP、pKa、溶解度等）
2. **文献报道的去除机理** — 什么作用力？特殊官能团？静电相互作用？贡献比例是多少？

**不获取的信息**:
- 吸附性能数据 (qmax、去除率等) — 这些属于不同材料体系
- 工程约束 — 属于吸附材料工程层面，不属于仿生设计层面
- 材料结构 — 属于吸附材料，不属于仿生原型

### 2.3 为什么不能混合

BMDL 的 `performance_data` 来自仿生吸附文献，记录的是仿生材料（如壳聚糖、荷叶、贻贝足丝等）对各种污染物的吸附性能。这些数据的污染物字段应该来自原始文献，而非用 2879 篇有机污染物论文的匹配矩阵去推断。

**错误案例**（已在回退中纠正）:
- chitosan 对 Cu(II)/Pb(II)/Cd(II) 的吸附数据被标记为"壬基酚" — 因为匹配矩阵中壬基酚对 chitosan 有最高权重
- 膜分离重金属数据被标记为"壬基酚" — 因为机理上下文中出现了有机污染物关键词
- F-/Cr(VI) 去除数据被标记为有机污染物 — 因为匹配矩阵的"性能层"命中了错误条目

详见 `docs/active/bmdl-writeback-report.md` 的回退记录。

---

## 3. 摘要 JSON 结构说明

### 3.1 文件位置

```
pollutant_knowledge_base/summaries/<污染物>.json  (20 个文件)
```

### 3.2 结构定义

每种污染物的摘要 JSON 包含以下顶层字段：

```json
{
  "pollutant_name": "全氟辛酸（PFOA）",
  "paper_count": 275,
  "total_ki": 3182,
  "empty_papers": 10,
  "skipped_low_confidence": 3,
  "ki_by_domain": { ... },
  "properties": { ... },
  "removal_mechanisms": [ ... ],
  "adsorption_performance": { ... },
  "engineering_constraints": [ ... ],
  "occurrence_patterns": [ ... ],
  "molecular_features_for_biomimetic_matching": [ ... ],
  "recommended_biomimetic_prototypes": [ ... ]
}
```

### 3.3 BMDL 需要关注的字段

#### `properties` — 污染物基本性质

BMDL 应读取此字段了解用户输入污染物的物化性质。每条性质包含 value、unit、ref_doi、source_file、confidence。

示例（PFOA）:
- C-F键能: 451.9 kJ/mol
- C-F键长范围: 1.309(14)–1.371(10) Å
- APFO分子量: 431 g/mol

#### `removal_mechanisms` — 文献报道的去除机理（BMDL 核心增益）

这是 2879 篇论文给 BMDL 提供的最核心增益。每种机理包含：
- `mechanism`: 机理名称（如"吸附"、"氢键"、"疏水"、"静电"、"π-π"等）
- `evidence_count`: 文献中支持该机理的 KI 数量（代表贡献比例）
- `key_references`: 主要参考 DOI 列表
- `details`: 具体描述列表（每条含 value、ref_doi、source_file）

示例（PFOA 的 11 种去除机理）:

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
| 还原 | 4 | 0.5% |
| 沉淀 | 4 | 0.5% |
| 螯合 | 2 | 0.2% |

示例（BPA 的 14 种去除机理）:

| 机理 | evidence_count | 贡献占比 |
|------|----------------|----------|
| 吸附 | 919 | 47.8% |
| 氢键 | 363 | 18.9% |
| 疏水 | 327 | 17.0% |
| π-π | 245 | 12.7% |
| 静电 | 243 | 12.6% |
| 氧化 | 55 | 2.9% |
| 离子交换 | 32 | 1.7% |
| 配位 | 26 | 1.4% |
| 生物降解 | 25 | 1.3% |
| 还原 | 16 | 0.8% |
| 螯合 | 14 | 0.7% |
| 沉淀 | 12 | 0.6% |
| 光降解 | 6 | 0.3% |
| 膜分离 | 1 | 0.05% |

BMDL 应使用这些机理信息来匹配用户输入污染物的去除需求与仿生原型的功能机制。

#### `molecular_features_for_biomimetic_matching` — 分子特征

从物化性质和去除机理中推导出的分子特征标签，用于触发 `feature_matching_rules.json` 中的匹配规则。

示例（PFOA）: `["可电离", "可配位", "大分子", "弱酸性", "氟碳链", "水溶性", "疏水性", "芳香环"]`

示例（BPA）: `["内分泌干扰", "可电离", "可配位", "大分子", "弱酸性", "水溶性", "疏水性", "芳香环", "酚羟基"]`

#### `recommended_biomimetic_prototypes` — 推荐仿生原型

基于分子特征匹配规则推荐的仿生原型列表。这是设计辅助参考，不是性能排名。

所有 20 种污染物的推荐原型主要集中在: chitosan, lotus-leaf, plant-tannin, polydopamine-coating 四个原型。

### 3.4 BMDL 不应直接使用的字段

- `adsorption_performance` — 含 qmax 等性能数据，属于吸附材料体系，不是仿生原型的性能
- `engineering_constraints` — 吸附材料的工程约束，不是仿生设计的约束
- `occurrence_patterns` — 污染物环境 occurrence，不是仿生设计信息

---

## 4. 仿生匹配矩阵使用方式

### 4.1 文件位置

```
pollutant_knowledge_base/biomimetic_matching/matching_matrix.json  (结构化数据)
pollutant_knowledge_base/biomimetic_matching/matching_matrix.md    (人类可读)
```

### 4.2 匹配逻辑

三层加权匹配矩阵（**注意：性能层仅用于匹配信号，不用于回填 BMDL**）:

| 层级 | 匹配方式 | weight | 信号强度 |
|------|---------|--------|---------|
| 性能层 | 提参中实际使用的吸附材料与仿生原型对照 | 3 | 强（有实测数据） |
| 机理层 | 提参中去除机理关键词与原型功能描述匹配 | 2 | 中（有机理解释） |
| 特征层 | 污染物分子特征 → feature_matching_rules → 命中原型 | 1 | 弱（仅特征推断） |

### 4.3 正确使用方式

BMDL 在接收到用户输入的污染物名称或性质后：

1. **查询摘要 JSON**: 从 `summaries/<污染物>.json` 获取 `properties` 和 `removal_mechanisms`
2. **提取分子特征**: 获取 `molecular_features_for_biomimetic_matching`
3. **触发匹配规则**: 用分子特征查询 `feature_matching_rules.json`，命中的原型作为候选
4. **参考匹配矩阵**: 查看 `matching_matrix.md` 中该污染物的推荐原型列表和权重
5. **结合机理信息**: 用 `removal_mechanisms` 中的贡献比例，判断哪些作用力是主要去除路径
6. **输出设计简报**: 按照 ADRMATS 接口契约，返回候选原型 + 诚实证据（fact/lead/inference）

### 4.4 接口契约约束

根据 `adrmats-interface-contract.md`:
- BMDL 作为**启发式候选检索模块**，返回候选 + 诚实证据
- **不按性能值排名** — `match.weight` 是特征匹配得分，不是性能得分
- `performance_leads` 全部为 LEAD，不作为设计目标

---

## 5. 规则缺口与原型缺口

### 5.1 缺失的分子特征→原型规则

当前 `feature_matching_rules.json` 有 11 条规则，聚合数据中发现 7 个缺失特征：

| 缺失特征 | 关联污染物 | 建议原型 | 建议weight |
|----------|-----------|----------|-----------|
| 内分泌干扰 | BPA | chitosan, plant-tannin | 0.6 |
| 可电离 | 壬基酚, 罗红霉素, 三氯甲烷 | chitosan | 0.6 |
| 可配位 | 壬基酚, 罗红霉素, 三氯甲烷 | chitosan | 0.6 |
| 大分子 | 壬基酚, 罗红霉素, 三氯甲烷 | chitosan | 0.6 |
| 弱酸性 | 壬基酚, 罗红霉素, β-六氯环己烷 | chitosan | 0.6 |
| 氟碳链 | PFHxS, HFPO-DA, PFOA | lotus-leaf, superhydrophobic-artificial | 0.6 |
| 氯代 | 三氯甲烷, β-六氯环己烷, 五氯苯酚 | polydopamine-coating | 0.6 |

**说明**: 新增特征匹配规则属于 `feature_matching_rules.json` 扩充，不涉及 `performance_data` 回填，不违反知识隔离原则。待 Yao 确认后可执行。

### 5.2 原型缺口

以下机理在提参数据中出现，但无对应仿生原型：

| 机理 | 出现频次 | 说明 |
|------|----------|------|
| π-π | 17/20 种污染物 | 几乎所有芳香族污染物都有，但 BMDL 无 π-π 专用原型 |
| 氧化 | 14/20 | 常见解离/氧化机理，BMDL 无氧化原型 |
| 生物降解 | 5/20 | 微生物降解，BMDL 有 sulfate-reducing-bacteria 但不直接对应 |
| 光降解 | 3/20 | 光催化降解，BMDL 无光催化原型 |
| 沉淀 | 5/20 | 化学沉淀，BMDL 有 oyster-shell/scallop-shell 可部分对应 |
| 膜分离 | 2/20 | 物理分离，BMDL 有 cell-membrane-ion-channel |
| 螯合 | 4/20 | 配位化学，BMDL 无专用螯合原型 |

---

## 6. 回填教训与数据治理

### 6.1 事件回顾

Task 5.1 尝试用 2879 篇论文的匹配矩阵/机理上下文回填 BMDL `prototypes_db` 中 101 条空 `pollutant` 字段。回填 71 条后发现系统性误分类，已全部回退。

### 6.2 根因

- 混合了两个不同材料体系的数据
- BMDL 的 `performance_data` 来自仿生吸附文献（重金属、油吸收等）
- 2879 篇论文的匹配矩阵来自有机污染物吸附文献
- 用后者的数据去填前者的空字段，导致错误标注

### 6.3 教训

1. **知识隔离不可违反**: 2879 篇论文的数据独立存储在 `pollutant_knowledge_base/` 下
2. **BMDL 的 performance_data 是重要证据**: 来源于仿生吸附文献，不能被外部数据覆盖
3. **匹配矩阵是设计辅助**: 用于推荐仿生原型，不用于回填 BMDL 数据
4. **空字段应溯源解决**: 101 条空 `pollutant` 字段应由 BMDL 自身文献溯源解决

### 6.4 当前状态

- `prototypes_db/` 已从 `prototypes_db.bak/` 完全恢复
- 101 条空 `pollutant` 字段维持原状
- `prototypes_db.bak/` 保留作为安全备份
- 详见 `docs/active/bmdl-writeback-report.md`

---

## 7. BMDL 集成路径

### 7.1 当用户输入污染物名称时

```
用户输入: "全氟辛酸 (PFOA)"
    ↓
BMDL 查询: pollutant_knowledge_base/summaries/全氟辛酸（PFOA）.json
    ↓
提取 properties → 了解 PFOA 的物化性质 (C-F键、弱酸性、水溶性等)
    ↓
提取 removal_mechanisms → 了解文献报道的 11 种去除机理及贡献比例
    → 吸附(35.4%) > 静电(16.5%) > 疏水(16.4%) > 氢键(5.8%) > 离子交换(3.7%) > ...
    ↓
提取 molecular_features → ["可电离", "可配位", "大分子", "弱酸性", "氟碳链", ...]
    ↓
触发 feature_matching_rules → 命中 chitosan, lotus-leaf, polydopamine-coating 等
    ↓
参考 matching_matrix.md → PFOA Top 推荐: magnetic-bacteria(3), alginate(3), chitosan(3), ...
    ↓
生成 BiomimeticDesignBrief → 候选原型 + 机理匹配理由 + 诚实证据
```

### 7.2 当用户输入污染物性质（非特定污染物名称）时

```
用户输入: "弱酸性、含氟碳链、水溶性的有机污染物"
    ↓
BMDL 匹配 molecular_features → "弱酸性" + "氟碳链" + "水溶性"
    ↓
查找所有 summaries/*.json 中具有相似特征的污染物
    → PFOA, PFBS, PFHxS, HFPO-DA 均匹配
    ↓
汇总这些污染物的 removal_mechanisms → 主要去除路径: 吸附 + 静电 + 疏水
    ↓
触发 feature_matching_rules → 氟碳链→lotus-leaf/superhydrophobic-artificial
    ↓
推荐仿生原型 + 设计理由
```

### 7.3 ADRMATS 集成

BMDL 作为 ADRMATS 的启发式候选检索模块:

1. ADRMATS 将用户需求（污染物名称或性质）传递给 BMDL
2. BMDL 查询 `pollutant_knowledge_base/summaries/` 获取性质和机理
3. BMDL 用 `feature_matching_rules.json` + `matching_matrix` 匹配仿生原型
4. BMDL 返回 `BiomimeticDesignBrief`:
   - 候选原型 + `match.weight`（特征匹配得分，非性能得分）
   - 机理匹配理由（引用 removal_mechanisms 的 evidence_count）
   - 直接证据 vs 特征推断（明确分离）
   - 诚实账本 (facts / leads / inferences)
5. ADRMATS 用这些候选进行发散式材料选择

---

## 8. 文件清单

### 8.1 提参结果（pollutant_knowledge_base/）

| 路径 | 说明 |
|------|------|
| `by_pollutant/*/` | 2879 个原始提参 JSON |
| `summaries/<污染物>.json` | 20 个污染物聚合摘要（BMDL 主要读取） |
| `summaries/adsorption_performance_flat.jsonl` | 扁平化吸附性能数据 |
| `pollutant_aggregate_index.json` | 20 种污染物汇总索引 |
| `biomimetic_matching/matching_matrix.json` | 加权匹配矩阵数据 |
| `biomimetic_matching/matching_matrix.md` | 人类可读匹配推荐表 |
| `biomimetic_matching/rule_gaps.md` | 规则与原型缺口分析 |
| `biomimetic_matching/pollutant_fix_log.json` | 回填修复日志（已回退） |
| `audit/quality_audit_report.json` | 审计数据 |
| `audit/quality_audit_report.md` | 审计报告 |
| `audit/empty_results_analysis.md` | 空结果论文分析 |
| `audit/dd_fix_log.json` | domain_direction 修复日志 |
| `audit/duplicate_ki_report.md` | 重复 KI 检测报告 |
| `audit/schema_validation_report.md` | schema 合规验证 |

### 8.2 BMDL 核心文件（未被 2879 篇论文修改）

| 路径 | 说明 |
|------|------|
| `prototypes_db/*.json` | 43 个仿生原型（已从备份恢复，未被修改） |
| `prototypes_db.bak/` | 安全备份 |
| `feature_matching_rules.json` | 11 条匹配规则（待扩充 7 条新规则） |
| `pollutant_profiles.json` | 45 个污染物分子特征画像 |

### 8.3 文档

| 路径 | 说明 |
|------|------|
| `docs/active/pollutant-post-extraction-plan.md` | 后处理计划（538 行） |
| `docs/active/bmdl-writeback-report.md` | 回写报告（含回退记录） |
| `docs/active/adrmats-interface-contract.md` | ADRMATS 接口契约 |
| `docs/active/pollutant-extraction-summary-and-bmdl-integration-guide.md` | 本文档 |

---

## 9. 待办事项

1. **Yao 确认 7 条新特征匹配规则** (见 §5.1) → 扩充 `feature_matching_rules.json`
2. **Yao 评估原型缺口** (见 §5.2) → 是否需要新增仿生原型
3. **101 条空 pollutant 字段** → 由 BMDL 自身文献溯源解决，不用 2879 篇论文数据
4. **feature_matching_rules.json 扩充** → 确认后执行，不涉及 performance_data 回填
