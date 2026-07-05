# Stage 7 Candidate Import Report

**日期：** 2026-07-05
**Candidate schema：** `bmdl_staging`
**Source：** BMDL review 工作区（release candidate match_export.json, commit `4f420f5`）

---

## Import Command

```bash
cd /Users/panyao/Qoder/ADRMATS
env -i HOME="$HOME" PATH="/usr/bin:/bin:/opt/homebrew/bin" .venv/bin/python \
  scripts/import_bmdl_to_rds.py --schema bmdl_staging --drop \
  --source /Users/panyao/Desktop/Biomimetic-design-library
```

## Import Counts

| 表 | Count | Expected | Status |
|----|-------|----------|--------|
| biological_prototypes | 48 | 48 (40 primary + 8 quarantined) | ✅ |
| performance_data | 1,020 | ~1,020 | ✅ |
| match_weights | 132 | 132 | ✅ |
| pollutant_profiles | 44 | 44 | ✅ |
| pollutant_aliases | 216 | 216 | ✅ |

## Post-Import Verification

| 断言 | 结果 | 说明 |
|------|------|------|
| quarantined in match_weights | **0** ✅ | quarantined prototypes excluded |
| primary prototypes | **40** ✅ | source_category filter working |
| exploratory weight > 0.3 (numeric) | **0** ✅ | all exploratory capped at 0.3 |
| non-direct weight > 0.5 (numeric) | **0** ✅ | all non-direct capped at 0.5 |
| plant-lignocellulosic PFOA | w=0.6, direct=True ✅ | new match from Stage 4 capacity |
| plant-lignocellulosic BPA | w=0.65, direct=True ✅ | new match from Stage 4 capacity |
| BMDL_SCHEMA env var | `bmdl_staging` ✅ | PostgresBmdlRepository reads env var |

## Float Precision Note

PostgreSQL REAL type stores 0.3 as 0.30000001192092896. Using `weight::numeric > 0.3` for correct comparison. All exploratory weights are exactly 0.3 (numeric), none exceed 0.3.

## Production Not Touched

- ✅ Only `bmdl_staging` schema was dropped and reimported
- ✅ Production `bmdl` schema was not modified
- ✅ ETL safety lock prevented `--schema bmdl --drop`
