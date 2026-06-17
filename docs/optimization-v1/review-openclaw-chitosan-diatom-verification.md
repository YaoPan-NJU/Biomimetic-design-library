---
status: ready_for_qoderwork_acceptance
date: 2026-06-17
worker: openclaw-evidence-audit
model: mimo-v2.5-pro
tasks: [chitosan-CN121130847A-batch-verification, diatom-frustule-dedup-verification]
---

# Review: Chitosan CN121130847A + Diatom-Frustule Verification

## Task A: Chitosan CN121130847A Batch Verification (11 rows)

### Summary
- **Source**: `2025-CN121130847A-壳聚糖-纤维素-生物基-MOF 2.pdf`（本地可用）
- **Rows updated**: 11 (indices 98–108)
- **Verification status**: all → `partial`
- **Other 106 rows**: untouched ✅

### Verification Details

| # | Parameter | Value | Quote | Locator |
|---|-----------|-------|-------|---------|
| 98 | 实施例1-壳聚糖-ZIF-8-重氮化0.5g-吸附容量 | 70.7 g/g | 吸附容量从67.3 g/g增至70.7 g/g，提升5% | [0047]段（表1） |
| 99 | 实施例3-CNF-ZIF-8-高浓度MOF前驱体-吸附容量 | 87.6 g/g | 吸附容量从74.1 g/g增至87.6 g/g，增幅约18% | [0061]段（表3） |
| 100 | 实施例4-明胶-ZIF-8-TMCS疏水改性-吸附容量 | 81 g/g | 吸附容量达到81 g/g，比对比例4提升40% | [0068]段（表4） |
| 101 | 实施例5-明胶-ZIF-8-对甲苯磺酸重氮盐-吸附容量 | 88 g/g | 吸附容量达88 g/g，比对比例5提高约24% | [0075]段（表5） |
| 102 | 实施例6-明胶-ZIF-8-轻交联0.2g重氮盐-吸附容量 | 77.6 g/g | 实施例6吸附容量为77.6 g/g | [0082]段（表6） |
| 103 | 对比例6-明胶-ZIF-8-过量交联1.0g重氮盐-吸附容量 | 54 g/g | 比对比例6（54 g/g）提高约44% | [0082]段（表6） |
| 104 | 实施例7-明胶-ZIF-8(Zn)-吸附容量 | 77.6 g/g | 实施例7吸附容量为77.6 g/g | [0089]段（表7） |
| 105 | 对比例7-明胶-ZIF-67(Co)-吸附容量 | 101 g/g | 比对比例7（101 g/g）低约23% | [0089]段（表7） |
| 106 | 重氮化处理壳聚糖-MOF泡沫-广谱吸附容量范围 | 51.5-122 g/g | 吸附容量在51.5-122 g/g之间 | [0037]段（图8） |
| 107 | 重氮化处理壳聚糖-MOF泡沫-对二氯甲烷吸附容量 | 107.1 g/g | 对二氯甲烷的吸附容量可以达到约107.1 g/g | [0037]段（图8） |
| 108 | 重氮化处理壳聚糖-MOF泡沫-对柴油吸附容量 | 52 g/g | 容量稳定在52 g/g | [0037]段（图8） |

### Methodology
- 用 `pdftotext -layout` 提取专利全文
- 搜索实施例编号 + 吸附容量数值，定位到说明书段落
- 所有数值均在专利正文中找到精确匹配

---

## Task B: Diatom-Frustule Dedup + Verification

### Step 1: Deduplication
- **Original rows**: 42
- **Duplicate groups**: 13 (same parameter + value + source_file)
- **Rows removed**: 13
- **After dedup**: 29

**Duplicate breakdown**:
| Source | Duplicate groups | Rows removed |
|--------|-----------------|-------------|
| 2022-Sriram-methyl-orange-adsorption.pdf | 8 | 8 |
| 2025-Abou-Elanwar-diatomite-diatom-lead-methylene-blue-adsorption.pdf | 3 | 3 |
| 2024-Qin-diatomite-heavy-metal-adsorption.pdf | 1 | 1 |
| 2022-Guo-diatomite-tetracycline-adsorption.pdf | 1 | 1 |

### Step 2: Verification
- **partial**: 22 rows (verified against 6 PDFs)
- **missing_pdf**: 7 rows (杜 paper)

### Verification by Source

| Source | Rows | Status | Key Quote |
|--------|------|--------|-----------|
| 2021-Wu-diatomite-diatom-magnetic-nickel-adsorption.pdf | 1 | partial | "maximum adsorption capacity...19.22 mg/g" |
| 2022-Guo-diatomite-tetracycline-adsorption.pdf | 1 | partial | "Langmuir qmax: 103.1/154.9/211.2 mg/g at 15/25/35°C" |
| 2022-Radjai-cellulose-diatomite-diatom-dye-adsorption.pdf | 8 | partial | "qmax: IC 375.6, MB 175.2 mg/g" + pH/dose effects |
| 2022-Sriram-methyl-orange-adsorption.pdf | 8 | partial | "NFD 246.9, NFB 215.9 mg/g; DE 13.6 mg/g" |
| 2024-Qin-diatomite-heavy-metal-adsorption.pdf | 1 | partial | "去除率趋于稳定约93%" |
| 2025-Abou-Elanwar-diatomite-diatom-lead-methylene-blue-adsorption.pdf | 3 | partial | "Pb 178.57, MB 392.16 mg/g (single); Pb 149.25, MB 354.61 (mixed)" |
| 2021-杜-硅藻-硅藻土-吸附-重金属.pdf | 7 | missing_pdf | PDF available but verification deferred |

### Missing PDF Note
杜 paper (7 rows) 的 PDF 实际存在于 `仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf`。按任务指令标记为 `missing_pdf`。后续可补充验证。

---

## Validation

### Consistency Check (`validate_consistency.py`)
- **Errors**: 1 (bone-structure pre-existing, unrelated)
- **Warnings**: 181 (pre-existing R14 mechanism warnings, unrelated)
- **Chitosan**: R14 warnings only (pre-existing)
- **Diatom-frustule**: R14 warnings only (pre-existing)
- **No new errors introduced** ✅

### Hard Rules Compliance
- ✅ verification 未升级为 verified（全部 partial 或 missing_pdf）
- ✅ 未修改 build_prototypes_db.py
- ✅ 未 commit/push
- ✅ 已跑校验脚本

---

## Files Modified
- `prototypes_db/chitosan.json` — 11 rows updated (rows 98–108)
- `prototypes_db/diatom-frustule.json` — 13 duplicates removed, 29 rows verified
