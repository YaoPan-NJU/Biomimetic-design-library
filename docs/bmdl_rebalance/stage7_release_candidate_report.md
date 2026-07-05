# Stage 7 Release Candidate Report

**日期：** 2026-07-05
**状态：** Release Candidate 已准备，待潘老师审计后执行 production cutover

---

## 一、Commit SHA

| Repo | Commit | 说明 |
|------|--------|------|
| ADRMATS | `5cb5902` | fix: allow BMDL schema selection via BMDL_SCHEMA |
| BMDL (release export) | `4f420f5` | stage7: promote stage5 match weights to release candidate export |
| BMDL (final report) | `63cbcbe` | stage7: candidate import + regression reports |

## 二、Release Candidate Checksum

| 文件 | SHA256[:16] | Rows | 说明 |
|------|-------------|------|------|
| baseline backup (旧 match_export) | `4c5ab4773e1d70e8` | 130 | `docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json` |
| match_export.json (release candidate) | `4bdbd34c5a3921bd` | 132 | `adrmats_export/match_export.json` |
| match_export_stage5.json (stage5 候选) | `f5585e72b0d8a320` | 132 | `adrmats_export/match_export_stage5.json` |
| canonical rows (内容一致) | `e92939746bdb3cc2` | 132 | rows 数组内容，两文件完全一致（由 Codex 审计提供） |

**说明**：`match_export.json` 与 `match_export_stage5.json` 的 rows 内容完全一致，但 meta 字段不同（stage5 标记 `5_formal_candidate`，RC 标记 `7_release_candidate`），所以文件级 SHA 不同。

## 三、Candidate Schema Import

- Schema: `bmdl_staging` (drop + fresh import)
- Source: BMDL review 工作区（release candidate match_export.json, commit `4f420f5`）

| 表 | Count |
|----|-------|
| biological_prototypes | 48 (40 primary + 8 quarantined) |
| performance_data | 1,020 |
| match_weights | 132 |
| pollutant_profiles | 44 |
| pollutant_aliases | 216 |
| quarantined in match_weights | 0 |

## 四、Query Regression（8 pollutants）

| Pollutant | #1 Candidate | Weight | Direct | 断言 |
|-----------|-------------|--------|--------|------|
| BPA | plant-lignocellulosic-architecture | 0.65 | True | ✅ direct #1 |
| PFOA | plant-lignocellulosic-architecture | 0.6 | True | ✅ direct #1 |
| PFOS | chitosan (exploratory) | 0.3 | False | ⚠️ no direct (strict bucketing) |
| Cd(II) | chitosan | 0.9 | True | ✅ evidence-based |
| Pb(II) | fish-scale-hydroxyapatite | 0.9 | True | ✅ multi-prototype |
| Cr(VI) | chitosan | 0.85 | True | ✅ bone/oyster降权 |
| PO43- | oyster-shell | 0.8 | True | ✅ direct retained |
| Hospital wastewater | N/A | - | - | ADRMATS task 层 fallback |

## 五、ADRMATS Schema Env Test

- `BMDL_SCHEMA=bmdl_staging` → `PostgresBmdlRepository.SCHEMA == 'bmdl_staging'` ✅
- 默认（不设） → `SCHEMA == 'bmdl'` ✅
- py_compile 通过 ✅
- Ad-hoc 验证: 5/5 passed

## 六、Validator

- `tools/validate_consistency.py`: 0 errors ✅
- 40 primary prototypes consistent ✅

## 七、未触碰 Production

- ✅ 未 `--drop bmdl`
- ✅ 未覆盖 production RDS `bmdl` schema
- ✅ Production `bmdl` schema 保持不变
- ✅ 仅操作了 `bmdl_staging` schema
