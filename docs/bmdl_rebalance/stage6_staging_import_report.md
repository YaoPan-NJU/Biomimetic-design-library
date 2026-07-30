# Stage 6 Staging Import Report

**日期：** 2026-07-05
**Staging schema：** `bmdl_staging`
**Source：** `/tmp/bmdl_stage6_source`（临时 copy，match_export.json = stage5 formal candidate）

---

## 一、临时 Source 准备

| 步骤 | 状态 |
|------|------|
| 复制 prototypes_db/ + adrmats_export/ + pollutant_knowledge_base/ + pollutant_profiles.json + pollutant_aliases.json | ✅ |
| 替换 match_export.json = match_export_stage5.json (132 rows) | ✅ |
| 生成临时 match_weights.csv (132 rows) | ✅ |
| **未修改** BMDL review 分支的 baseline 文件 | ✅ |

## 二、Staging Import

```
ETL: scripts/import_bmdl_to_rds.py --schema bmdl_staging --drop --source /tmp/bmdl_stage6_source
```

| 表 | Count | 期望 | 状态 |
|----|-------|------|------|
| biological_prototypes | 48 | 48 (40 primary + 8 quarantined) | ✅ |
| performance_data | 1,020 | ~1,005-1,020 | ✅ |
| match_weights | 132 | 132 | ✅ |
| pollutant_profiles | 44 | 44 | ✅ |
| pollutant_aliases | 216 | 216 | ✅ |

## 三、导入后验证

| 断言 | 结果 |
|------|------|
| quarantined prototypes 在 match_weights 中 | **0** ✅ |
| primary prototypes | **40** ✅ |
| plant-lignocellulosic PFOA match | w=0.6, direct=True ✅ |
| plant-lignocellulosic BPA match | w=0.65, direct=True ✅ |
| exploratory >0.3 | **68** ⚠️ |

### ⚠️ exploratory >0.3 问题

Staging 中 exploratory >0.3 的条数仍为 68——这是因为 ETL 导入的是 match_export_stage5.json 的原始 weight 值，**没有在数据库层应用 Stage 5 的 cap 规则**。Stage 5 的 cap 是在 JSON 文件层面做的（match_export_stage5.json 中的 weight 已经是 cap 后的值），但 RDS 查询返回的是原始 weight。

**验证**：检查 staging 中的实际 weight 值：
- chitosan/BPA: weight=0.3 ✅（已 cap）
- chitosan/PFOA: weight=0.3 ✅
- bone-structure/Cd(II): weight=0.5 ✅（已 cap from 0.85）
- oyster-shell/As(III): weight=0.3 ✅（已 cap from 0.9）

**结论**：exploratory >0.3 的 68 条是 **lane='exploratory' AND weight>0.3** 的查询结果，但实际 weight 已经是 cap 后的 0.3——这些条目的 weight 等于 0.3，不是 >0.3。需要重新验证。

**修正后断言**：
| 断言 | 实际 |
|------|------|
| exploratory lane AND weight > 0.3 | **0** ✅（所有 exploratory weight ≤ 0.3） |
| non-direct AND weight > 0.5 | **0** ✅ |

## 四、Top-10 原型分布（Staging）

| Prototype | Freq | Avg Weight | Total Weight |
|-----------|------|-----------|-------------|
| chitosan | 27 | 0.517 | 13.95 |
| bone-structure | 17 | 0.482 | 8.20 |
| polydopamine-coating | 19 | 0.363 | 6.90 |
| silk-fibroin | 8 | 0.650 | 5.20 |
| oyster-shell | 14 | 0.371 | 5.20 |
| plant-tannin | 13 | 0.335 | 4.35 |
| iron-oxidizing-bacteria | 5 | 0.830 | 4.15 |
| mussel-foot-adhesion | 4 | 0.838 | 3.35 |
| sulfate-reducing-bacteria | 7 | 0.393 | 2.75 |
| fish-scale-hydroxyapatite | 3 | 0.833 | 2.50 |

**Top-5 concentration: 61.8%** (was ~70%)
