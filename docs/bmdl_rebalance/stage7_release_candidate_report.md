# Stage 7 Release Candidate Report

**日期：** 2026-07-05
**状态：** Release Candidate 已准备，待潘老师审计后执行 production cutover

---

## 一、Commit SHA

| Repo | Commit | 说明 |
|------|--------|------|
| ADRMATS | `5cb5902` | fix: allow BMDL schema selection via BMDL_SCHEMA |
| BMDL | (pending) | stage7: promote stage5 match weights to release candidate |

## 二、Release Candidate Checksum

| 文件 | SHA256[:16] | Rows |
|------|-------------|------|
| baseline match_export.json (旧) | `eee5821423089144` | 130 |
| release candidate match_export.json (新) | `dbd42a57d53e5166` | 132 |
| baseline backup | `docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json` | 130 |

## 三、Candidate Schema Import

- Schema: `bmdl_staging` (drop + fresh import)
- Source: BMDL review 工作区（release candidate match_export.json）

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
| BPA | plant-lignocellulosic | 0.65 | True | ✅ direct #1 |
| PFOA | plant-lignocellulosic | 0.6 | True | ✅ direct #1 |
| PFOS | chitosan (exploratory) | 0.3 | False | ⚠️ no direct (strict bucketing) |
| Cd(II) | chitosan | 0.9 | True | ✅ evidence-based |
| Pb(II) | fish-scale-hydroxyapatite | 0.9 | True | ✅ multi-prototype |
| Cr(VI) | chitosan | 0.85 | True | ✅ bone/oyster降权 |
| PO43- | oyster-shell | 0.8 | True | ✅ direct retained |
| Hospital wastewater | N/A | - | - | N/A (fallback in task层) |

## 五、ADRMATS Schema Env Test

- `BMDL_SCHEMA=bmdl_staging` → `PostgresBmdlRepository.SCHEMA == 'bmdl_staging'` ✅
- 默认（不设） → `SCHEMA == 'bmdl'` ✅
- py_compile 通过 ✅

## 六、Validator

- `tools/validate_consistency.py`: 0 errors ✅
- 40 primary prototypes consistent ✅

## 七、未触碰 Production

- ✅ 未 `--drop bmdl`
- ✅ 未覆盖 production RDS `bmdl` schema
- ✅ Production `bmdl` schema 保持不变
- ✅ 仅操作了 `bmdl_staging` schema
