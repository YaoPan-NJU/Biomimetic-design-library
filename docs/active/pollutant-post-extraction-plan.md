---
title: 污染物提参后处理计划 — 质量审计 / 知识聚合 / 仿生匹配前置 / BMDL 回写
date: 2026-06-27
status: ready-for-execution
owner: claude-code (mac mini)
author: panyao
revision: v2 — 吸收 7 条优化建议（backup前置 / 扁平输出 / 两阶段聚合 / 加权匹配 / Task 5 回写 / confidence 阈值 / 并行调度）
scope: 2879 篇论文提参完成后，1-审计 2-聚合 4-匹配前置 5-BMDL 回写（跳过 v1.0 路线图 M1-M4）
---

# 污染物提参后处理计划

## 背景

提参已 100% 完成：2879 篇 PDF → 2879 个 JSON，覆盖 20 种污染物，共 27592 条 knowledge_items（平均 9.6 条/篇）。数据存储在 `pollutant_knowledge_base/by_pollutant/<污染物>/` 下，与 BMDL 仿生知识库隔离。

### 当前数据概况

| 指标 | 数值 |
|------|------|
| 总论文 | 2879 |
| 总 KI | 27592 |
| 平均每篇 KI | 9.6 |
| 空结果论文（0 KI） | 360（主要集中在 BPA 286篇、DDT 54篇） |
| verification | 27583 unverified / 9 missing |
| confidence | 22034 条=1.0, 4960 条=0.8-0.99, 556 条=0.5-0.79, 42 条<0.5 |

### domain_direction 分布（含异常）

| domain_direction | KI 数 | 备注 |
|---|---|---|
| D1_adsorption_performance | 8240 | 正常 |
| D4_adsorption_mechanism | 4766 | 正常 |
| D11_pollutant_property | 3618 | 正常 |
| D5_engineering_constraint | 3068 | 正常 |
| D2_material_structure | 2899 | 正常 |
| D12_occurrence_pattern | 2368 | 正常 |
| D6_pollutant_application | 1362 | 正常 |
| D8_characterization | 621 | 正常 |
| D7_synthesis_method | 519 | 正常 |
| D9_comparison_review | 106 | 正常 |
| D1_engineering_constraint | 12 | **异常**，应为 D5 |
| D1_pollutant_application | 5 | **异常**，应为 D6 |
| D11_pollutant_application | 4 | **异常**，应为 D6 |
| D1_adsorption_mechanism | 1 | **异常**，应为 D4 |
| D1_pollutant_property | 1 | **异常**，应为 D11 |
| D1_engineering_performance | 1 | **异常**，应为 D1 |
| DDT | 1 | **异常**，模型幻觉 |

### 20 种污染物论文数

| 污染物 | 论文数 | 空结果 |
|---|---|---|
| 双酚A（BPA） | 1416 | 286 |
| 全氟辛酸（PFOA） | 275 | 10 |
| 十溴二苯醚 | 236 | 1 |
| 滴滴涕（DDT） | 230 | 54 |
| 五氯苯酚 | 171 | 1 |
| 壬基酚 | 152 | 5 |
| 2,3,7,8-四氯二苯并-p-二噁英（TCDD） | 122 | 2 |
| 全氟丁烷磺酸（PFBS） | 67 | 0 |
| 狄氏剂（Dieldrin） | 53 | 0 |
| 三氯甲烷 | 26 | 1 |
| 全氟己烷磺酸（PFHxS） | 33 | 0 |
| 六氟环氧丙烷二聚酸 | 32 | 0 |
| 多氯联苯-209（PCB-209） | 2 | 0 |
| 2,6-二氯苯酚 | 13 | 0 |
| 滴滴伊（DDE） | 12 | 0 |
| 罗红霉素 | 10 | 0 |
| 六氯丁二烯 | 4 | 0 |
| 奥克立林 | 8 | 0 |
| β-六氯环己烷 | 9 | 0 |
| 硫丹 | 8 | 0 |

### 现有 BMDL 资产

- **prototypes_db/**：43 个仿生原型 JSON（chitosan, lotus-leaf, mussel-foot-adhesion 等）
  - `performance_data` 字段共 502 条，其中 **101 条 `pollutant` 字段为空**（分布在 15 个原型中）
  - 空 pollutant 分布：chitosan 40 条、mussel-foot-adhesion 9 条、polydopamine-coating 9 条、superhydrophobic-artificial 8 条、cell-membrane-ion-channel 11 条 等
- **pollutant_profiles.json**：45 个污染物分子特征画像（含本次 20 种 + 重金属/染料等）
- **feature_matching_rules.json**：11 条分子特征→原型匹配规则（芳香环→polydopamine/plant-tannin 等）

---

## Task 1：提参质量审计

**目标**：对 2879 个 JSON 做全面质量扫描，输出审计报告，修复可自动修复的问题。

**输出文件**：`pollutant_knowledge_base/audit/quality_audit_report.json` + `.md`

### 1.1 字段完整度扫描

逐文件检查以下字段是否为空/缺失：

- `bibliographic_metadata.title` / `.doi` / `.abstract` / `.year`
- `decision_summary.one_sentence_value` / `.key_findings`
- 每个 `knowledge_item` 的：`parameter`, `value`, `evidence`（至少 1 条）, `ref_doi`, `source_file`, `domain_direction`, `confidence`

统计缺失率，按污染物分组。

### 1.2 domain_direction 异常修复

**前置步骤（必须先执行）**：

```bash
cd /Users/panyao/Desktop/Biomimetic-design-library/pollutant_knowledge_base
cp -r by_pollutant by_pollutant.bak
echo "backup done: by_pollutant.bak"
```

确认 backup 存在后再执行修复脚本。

发现 25 条 KI 的 `domain_direction` 有拼写错误（见背景表）。写脚本批量修复：

```python
# 修复映射
DD_FIX = {
    "D1_engineering_constraint": "D5_engineering_constraint",
    "D1_pollutant_application": "D6_pollutant_application",
    "D11_pollutant_application": "D6_pollutant_application",
    "D1_adsorption_mechanism": "D4_adsorption_mechanism",
    "D1_pollutant_property": "D11_pollutant_property",
    "D1_engineering_performance": "D1_adsorption_performance",
    "DDT": "D11_pollutant_property",  # 模型幻觉，归入污染物属性
}
```

逐 JSON 文件扫描，修复后写回，记录修改的文件名和 KI record_id 到 `audit/dd_fix_log.json`。

### 1.3 空结果论文分析（可与主线并行，不阻塞）

360 篇论文提取了 0 条 KI。需要分析原因：

- 抽样 20 篇空结果论文（BPA 10 篇 + DDT 5 篇 + 其他 5 篇）
- 检查 `processing_notes` 和 `decision_summary` 中是否有说明
- 判断是 PDF 质量问题（扫描件/非英文）还是模型提取失败
- 若为模型失败且 PDF 可读，标记为"可重跑候选"

输出：`audit/empty_results_analysis.md`

### 1.4 重复 KI 检测（可与主线并行，不阻塞）

检查同一污染物目录下是否存在 parameter 值高度重复的 KI（如同一 logP 值出现在多篇论文中但引用了不同 DOI — 这是正常的文献引用；但如果同一论文内出现完全重复的 record_id 或 parameter+value 组合，则是 bug）。

### 1.5 schema 合规性验证

用 `tools/litextract/schema/biomimetic_extraction_v2.schema.json` 对所有 2879 个 JSON 做 schema validation（可用 `jsonschema` Python 库）。记录不符合 schema 的文件和具体字段。

### 1.6 生成审计报告

汇总以上所有检查，生成 `quality_audit_report.md`：

- 总体质量评分（完整性百分比）
- 按污染物维度的质量热力图（文字表格）
- 异常清单及修复状态
- 低 confidence KI 清单（42 条 < 0.5，记录但不删除）
- 建议重跑的论文列表

---

## Task 2：污染物知识聚合

**目标**：从 2879 篇论文的 KI 中，按污染物维度聚合出结构化摘要，为 BMDL 仿生匹配提供输入。

**输出文件**：
- `pollutant_knowledge_base/summaries/<污染物>.json`（20 个文件，嵌套结构）
- `pollutant_knowledge_base/summaries/adsorption_performance_flat.jsonl`（扁平化，每行一条）
- `pollutant_knowledge_base/pollutant_aggregate_index.json`（汇总索引）

### 2.1 聚合结构定义

每种污染物的聚合 JSON 结构（嵌套版）：

```json
{
  "pollutant_name": "双酚A（BPA）",
  "pollutant_class": "内分泌干扰物 / 有机污染物",
  "paper_count": 1416,
  "total_ki": 15000,
  "ki_by_domain": {
    "D1_adsorption_performance": 5000,
    "D4_adsorption_mechanism": 3000,
    "D11_pollutant_property": 2000,
    ...
  },
  "properties": {
    "molecular_formula": [{"value": "C15H16O2", "ref_doi": "...", "source_file": "..."}],
    "molecular_weight": [{"value": "228.29", "ref_doi": "...", "source_file": "..."}],
    "logP": [{"value": "3.32", "ref_doi": "...", "source_file": "..."}],
    "pKa": [...],
    "solubility": [...],
    "other_properties": [...]
  },
  "removal_mechanisms": [
    {
      "mechanism": "吸附",
      "details": [...],
      "evidence_count": 120,
      "key_references": ["doi1", "doi2"]
    }
  ],
  "adsorption_performance": {
    "best_materials": [
      {"material": "活性炭", "qmax_mg_g": 450, "ref_doi": "...", "source_file": "..."},
      ...
    ],
    "common_adsorbents": [...],
    "ph_range": [...],
    "temperature_range": [...]
  },
  "engineering_constraints": [...],
  "occurrence_patterns": [...],
  "molecular_features_for_biomimetic_matching": [
    "芳香环",
    "酚羟基",
    "疏水性",
    ...
  ],
  "recommended_biomimetic_prototypes": [
    "polydopamine-coating",
    "plant-tannin",
    ...
  ]
}
```

**同时输出扁平化 JSONL**（`adsorption_performance_flat.jsonl`），每行一条记录，方便下游 join 和分析：

```jsonl
{"pollutant": "双酚A（BPA）", "material": "活性炭", "qmax_mg_g": 450, "ph": 7, "temperature": "25°C", "ref_doi": "10.1016/...", "source_file": "..."}
{"pollutant": "双酚A（BPA）", "material": "壳聚糖", "qmax_mg_g": 120, "ph": 6, "temperature": "25°C", "ref_doi": "10.1016/...", "source_file": "..."}
{"pollutant": "全氟辛酸（PFOA）", "material": "活性炭", "qmax_mg_g": 89, "ph": 5, "temperature": "25°C", "ref_doi": "...", "source_file": "..."}
```

### 2.2 聚合脚本（分两阶段）

写 `scripts/aggregate_pollutant_knowledge.py`，分两阶段执行：

**Stage 1：纯统计（快速验证数据完整性）**

```python
# 逻辑：
# 1. 遍历 by_pollutant/<污染物>/ 下所有 JSON
# 2. 统计：论文数、KI 总数、KI 按 domain_direction 分布
# 3. 统计：confidence 分布、verification 分布
# 4. 输出每个污染物的统计摘要到 stderr / 控制台
# 5. 验证：KI 总数应 = 27592 - 25(已修复的DD) ± 少量偏差
```

Stage 1 完成后，人工或自动校验数据一致性。确认无误后再跑 Stage 2。

**Stage 2：语义聚合（跨 KI 合并）**

```python
# 逻辑：
# 1. 遍历 by_pollutant/<污染物>/ 下所有 JSON
# 2. 过滤：confidence < 0.5 的 KI 跳过聚合（记录到审计报告的"低 confidence"章节）
# 3. 按 domain_direction 分类提取 KI：
#    - D11_pollutant_property → properties（按 parameter 去重，保留所有不同值+引用）
#    - D4_adsorption_mechanism → removal_mechanisms（按机理关键词聚类）
#    - D1_adsorption_performance → adsorption_performance（提取 qmax 值并排序）
#    - D5_engineering_constraint → engineering_constraints
#    - D12_occurrence_pattern → occurrence_patterns
# 4. 从 properties + mechanisms 推导 molecular_features_for_biomimetic_matching
# 5. 根据 molecular_features 对照 feature_matching_rules.json 推荐 prototypes
# 6. 输出 summaries/<污染物>.json（嵌套版）
# 7. 同时输出 adsorption_performance_flat.jsonl（扁平版，逐行追加）
```

**confidence 阈值规则**：

| confidence 范围 | 处理方式 |
|---|---|
| ≥ 0.8 | 正常参与聚合 |
| 0.5 - 0.79 | 参与聚合但标记 `low_confidence: true` |
| < 0.5 | 不参与聚合，记录到审计报告 |

### 2.3 更新 pollutant_profiles.json

**前置步骤**：`cp pollutant_profiles.json pollutant_profiles.json.bak`

当前 `pollutant_profiles.json` 已有这 20 种污染物的条目，但 `molecular_features` 和 `likely_interactions` 可能不够完整。用聚合结果补充：

- 将提参中发现的物化性质（logP、pKa、溶解度等）作为 `profile_basis: "literature"` 的证据
- 补充 `likely_interactions`（如从 D4_adsorption_mechanism KI 中提取实际观察到的相互作用类型）
- 新增 `literature_evidence_count` 字段

**注意**：保持知识隔离 — 更新 `pollutant_profiles.json` 中的特征画像是允许的（它是 BMDL 子项），但不要把原始 KI 灌入 BMDL。

### 2.4 生成汇总索引

`pollutant_aggregate_index.json`：20 种污染物的概览表，包含每种污染物的论文数、KI 数、主要机理、推荐原型数。

---

## Task 4：仿生匹配前置准备

**目标**：建立污染物→仿生原型的匹配桥梁，输出加权匹配矩阵，识别规则缺口。

**输出文件**：
- `pollutant_knowledge_base/biomimetic_matching/matching_matrix.json`
- `pollutant_knowledge_base/biomimetic_matching/matching_matrix.md`
- `pollutant_knowledge_base/biomimetic_matching/rule_gaps.md`

### 4.1 构建加权匹配矩阵

对 20 种污染物，逐一匹配 BMDL 43 个原型。

**匹配逻辑（三层 + 加权）**：

| 层级 | 匹配方式 | weight | 信号强度 |
|------|---------|--------|---------|
| 性能层 | 从 `adsorption_performance` 中提取实际使用过的吸附材料，与仿生原型对照 | **3** | 强（有实测数据） |
| 机理层 | 从 `removal_mechanisms` 中提取关键词，与原型功能描述匹配 | **2** | 中（有机理解释） |
| 特征层 | 污染物 `molecular_features` → `feature_matching_rules.json` → 命中原型 | **1** | 弱（仅特征推断） |

**排序逻辑**：按 `total_weight` 降序排列，而非简单取并集。

输出 `matching_matrix.json`：

```json
{
  "双酚A（BPA）": {
    "molecular_features": ["芳香环", "酚羟基", "疏水性"],
    "matched_prototypes": [
      {
        "prototype": "chitosan",
        "total_weight": 6,
        "feature_match": {"hit": true, "weight": 1, "reason": "酚羟基→chitosan 规则命中"},
        "mechanism_match": {"hit": true, "weight": 2, "reason": "BPA 通过氢键与壳聚糖羟基结合", "evidence_count": 15},
        "performance_match": {"hit": true, "weight": 3, "reason": "壳聚糖对 BPA 实测 qmax=120 mg/g", "ref_doi": "10.1016/..."},
        "has_qmax": true,
        "qmax_mg_g": 120
      },
      {
        "prototype": "polydopamine-coating",
        "total_weight": 4,
        "feature_match": {"hit": true, "weight": 1, "reason": "芳香环→polydopamine 规则命中"},
        "mechanism_match": {"hit": true, "weight": 2, "reason": "π-π堆积", "evidence_count": 8},
        "performance_match": {"hit": false, "weight": 0, "reason": "无实测数据"},
        "has_qmax": false
      },
      ...
    ],
    "unmatched_mechanisms": ["光催化降解 — 无对应仿生原型"]
  },
  ...
}
```

### 4.2 识别规则缺口

检查 `feature_matching_rules.json` 中缺失的特征：

当前有 11 条规则（芳香环、疏水性、酚羟基、二价阳离子、软酸、正电荷、磺酰胺基、酰胺基、氯代烯烃、平面结构、水溶性）。

从 20 种污染物的聚合数据中提取所有出现过的分子特征，对比已有规则，找出缺失：

- 氟碳链（PFOA/PFBS/PFHxS/HFPO-DA 共有）→ 需新增规则
- 氯代芳香环（PCB-209/TCDD/五氯苯酚/2,6-二氯苯酚 共有）→ 可能需要细化
- 内分泌干扰特征（BPA/壬基酚 共有）→ 需评估是否作为匹配特征
- 大分子疏水性（十溴二苯醚/奥克立林）→ 疏水性规则已有但需检查 weight

输出 `rule_gaps.md`：列出缺失特征、建议规则、候选原型、建议 weight。

### 4.3 匹配优先级排序

对每种污染物的 `matched_prototypes` 列表（已按 `total_weight` 降序），增加以下维度细化排序：

1. `total_weight` 降序（主排序键）
2. `has_qmax` = true 优先（有实测数据的排前面）
3. 原型 `library_tier` = core 优先（查 prototypes_db）

输出 `matching_matrix.md`：人类可读的推荐表，每种污染物 Top 5 推荐原型 + 理由 + weight 分数。

### 4.4 原型缺口识别

如果某些污染物没有合适的仿生原型匹配（如"光催化降解"机理无对应原型），记录到 `rule_gaps.md` 的"原型缺口"章节，供后续 BMDL 扩展参考。

---

## Task 5：BMDL 回写

**目标**：将 Task 4 的匹配结果回写到 BMDL 核心文件，填充现有数据缺口。

**前置步骤**：
```bash
cd /Users/panyao/Desktop/Biomimetic-design-library
cp -r prototypes_db prototypes_db.bak
cp feature_matching_rules.json feature_matching_rules.json.bak
```

**输出文件**：
- 修改 `prototypes_db/*.json`（填充 101 条空 pollutant 字段）
- 修改 `feature_matching_rules.json`（新增缺失规则）
- 新建 `docs/active/bmdl-writeback-report.md`（回写记录）

### 5.1 填充 performance_data 空 pollutant 字段

prototypes_db 中 15 个原型共有 101 条 `performance_data` 条目的 `pollutant` 字段为空。这些条目有 material、value、unit 等信息，但缺少关联的污染物名称。

**回写逻辑**：

1. 从 Task 4 的 `matching_matrix.json` 中提取所有**性能层命中**（`performance_match.hit = true`）的记录
2. 建立反向映射：`material_name → [pollutant_name, ref_doi, qmax]`
3. 遍历 101 条空 pollutant 条目，按 `material` 字段匹配：
   - 精确匹配 material 名称 → 填入 pollutant
   - 模糊匹配（material 包含关键词）→ 填入 pollutant，标记 `match_confidence: "fuzzy"`
   - 无匹配 → 跳过，记录到回写报告
4. 回写时同时补充 `ref_doi`（如果原条目 doi 为空但提参数据有）

**空 pollutant 分布**（需回写的原型）：

| 原型 | 空 pollutant 条数 |
|---|---|
| chitosan | 40 |
| cell-membrane-ion-channel | 11 |
| mussel-foot-adhesion | 9 |
| polydopamine-coating | 9 |
| superhydrophobic-artificial | 8 |
| diatom-frustule | 4 |
| fish-scale-hydroxyapatite | 3 |
| iron-oxidizing-bacteria | 4 |
| lotus-leaf | 4 |
| mangrove-root | 2 |
| oyster-shell | 2 |
| scallop-shell | 2 |
| silk-fibroin | 1 |
| mycelium | 1 |
| pitcher-plant-slippery-surface | 1 |
| **合计** | **101** |

### 5.2 扩充 feature_matching_rules.json

从 Task 4.2 识别的规则缺口中，将**有提参证据支撑**的新规则写入 `feature_matching_rules.json`：

```json
// 新增规则示例
"氟碳链": {
  "prototypes": ["lotus-leaf", "pitcher-plant-slippery-surface", "superhydrophobic-artificial"],
  "reason": "氟碳链具有强疏水性，可与超疏水表面通过疏水分配作用结合",
  "weight": 0.7,
  "evidence_source": "PFOA/PFBS/PFHxS/HFPO-DA 提参聚合",
  "evidence_count": 407
}
```

**写入条件**：只有当新规则的 `evidence_count ≥ 10`（至少 10 条 KI 支持该特征→原型关联）时才写入。低于阈值的记录到 `rule_gaps.md` 待人工审核。

### 5.3 生成回写报告

`docs/active/bmdl-writeback-report.md`：

- performance_data 回写统计：成功填充 X/101 条，模糊匹配 Y 条，未匹配 Z 条
- feature_matching_rules 新增规则列表
- 每条回写操作的 before/after 对照（抽样 10 条）
- 数据完整性验证：回写后重新扫描 prototypes_db 确认 pollutant 字段空值数下降

---

## 执行顺序

```
主线（串行）:
  Task 1.1 字段完整度扫描
     ↓
  Task 1.2 backup → domain_direction 修复
     ↓
  Task 1.6 生成审计报告（汇总 1.1 + 1.2 结果）
     ↓
  Task 2 Stage 1 纯统计（验证数据完整性）
     ↓
  Task 2 Stage 2 语义聚合 → 输出 summaries/*.json + flat.jsonl
     ↓
  Task 2.3 更新 pollutant_profiles.json
  Task 2.4 生成汇总索引
     ↓
  Task 4.1 加权匹配矩阵
  Task 4.2 规则缺口识别
  Task 4.3 优先级排序 → 输出 matching_matrix.md
  Task 4.4 原型缺口识别
     ↓
  Task 5.1 填充 101 条空 pollutant
  Task 5.2 扩充 feature_matching_rules.json
  Task 5.3 生成回写报告

并行支线（不阻塞主线）:
  Task 1.3 空结果论文分析  ──┐
  Task 1.4 重复 KI 检测    ──┤  可与 Task 1.1-1.6 并行
  Task 1.5 schema 合规验证  ──┘  结果汇入 Task 1.6 审计报告
```

## 关键路径与文件清单

### 输入文件（只读）

| 路径 | 说明 |
|------|------|
| `pollutant_knowledge_base/by_pollutant/*/` | 2879 个提参 JSON |
| `pollutant_profiles.json` | 45 个污染物分子特征画像 |
| `feature_matching_rules.json` | 11 条分子特征→原型规则 |
| `prototypes_db/*.json` | 43 个仿生原型（含 502 条 performance_data，101 条 pollutant 空） |
| `tools/litextract/schema/biomimetic_extraction_v2.schema.json` | JSON schema |

### 输出文件（新建）

| 路径 | 说明 |
|------|------|
| `pollutant_knowledge_base/audit/quality_audit_report.json` | 审计数据 |
| `pollutant_knowledge_base/audit/quality_audit_report.md` | 审计报告 |
| `pollutant_knowledge_base/audit/empty_results_analysis.md` | 空结果分析 |
| `pollutant_knowledge_base/audit/dd_fix_log.json` | domain_direction 修复日志 |
| `scripts/aggregate_pollutant_knowledge.py` | 聚合脚本（Stage 1 + Stage 2） |
| `pollutant_knowledge_base/summaries/<污染物>.json` | 20 个污染物聚合摘要（嵌套版） |
| `pollutant_knowledge_base/summaries/adsorption_performance_flat.jsonl` | 扁平化吸附性能数据 |
| `pollutant_knowledge_base/pollutant_aggregate_index.json` | 汇总索引 |
| `pollutant_knowledge_base/biomimetic_matching/matching_matrix.json` | 加权匹配矩阵数据 |
| `pollutant_knowledge_base/biomimetic_matching/matching_matrix.md` | 人类可读匹配推荐 |
| `pollutant_knowledge_base/biomimetic_matching/rule_gaps.md` | 规则与原型缺口 |
| `docs/active/bmdl-writeback-report.md` | BMDL 回写报告 |

### 修改文件（已有，均需先 backup）

| 路径 | 修改内容 | backup 路径 | 触发 Task |
|------|----------|------------|----------|
| `pollutant_knowledge_base/by_pollutant/*/*.json` | 修复 domain_direction 异常（25 条 KI） | `by_pollutant.bak/` | Task 1.2 |
| `pollutant_profiles.json` | 补充 literature-backed 证据 | `pollutant_profiles.json.bak` | Task 2.3 |
| `prototypes_db/*.json` | 填充 101 条空 pollutant 字段 | `prototypes_db.bak/` | Task 5.1 |
| `feature_matching_rules.json` | 新增缺失特征→原型规则 | `feature_matching_rules.json.bak` | Task 5.2 |

## 注意事项

1. **知识隔离原则**：提参原始 KI 始终留在 `pollutant_knowledge_base/` 下。Task 5 回写的是**聚合后的摘要信息**（性能数据、匹配规则），不是原始 KI。
2. **Task 5 例外说明**：虽然注意事项 1 说不灌入原始 KI，但 Task 5.1 填充 `performance_data.pollutant` 字段是**回填已有条目的缺失字段**，属于补充 BMDL 现有数据缺口，不是新增 KI。回填值来自聚合摘要而非原始 KI。
3. **脚本放 scripts/**：所有新写的处理脚本放在 `scripts/` 下。
4. **backup 先行**：每个 Task 修改已有文件前，必须先执行 backup 命令，确认 backup 文件存在后再修改。具体 backup 路径见上方"修改文件"表。
5. **confidence 阈值**：聚合时 `confidence < 0.5` 的 42 条 KI 不参与聚合，但完整记录到审计报告。
