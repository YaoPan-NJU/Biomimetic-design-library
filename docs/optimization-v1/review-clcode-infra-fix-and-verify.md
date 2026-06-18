# Infra Fix + Multimodal Verification Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## 1. Code Fixes

### build_prototypes_db.py
- **Line ~377**: Added `verification_quote` and `source_locator` preservation for mechanisms during merge
- **Line ~404**: Added `verification_quote` and `source_locator` to performance_data field preservation list
- **Result**: Build passes, quotes preserved after merge

### multimodal_verify.py
- **Line ~270**: Added `missing_pdf` to verification filter (now processes those rows too)
- **Line ~212**: Changed function signature to accept `client_pool` for retry support
- **Lines ~233-250**: Replaced single API call with 3-attempt retry loop using round-robin client pool
- **Lines ~285-289**: Updated call site to pass `client_pool` instead of single client
- **Lines ~308-312**: Added incremental checkpoint save every 5 rows

## 2. Verification Results

| prototype | perf verified | perf not_found | perf errors | mech verified | mech not_found |
|---|---|---|---|---|---|
| plant-tannin | 0 | 0 | 0 | 0 | 1 |
| lobster-exoskeleton | 1 | 0 | 0 | 0 | 1 |
| bone-structure | 1 | 0 | 0 | 0 | 1 |
| iron-oxidizing-bacteria | 0 | 0 | 0 | 0 | 2 |
| mycelium | 0 | 5 | 0 | 0 | 3 |
| cell-membrane-ion-channel | 1 | 3 | 1 | 0 | 4 |
| pitcher-plant-slippery-surface | 0 | 1 | 0 | 0 | 11 |
| silk-fibroin | 0 | 0 | 0 | 0 | 12 |
| spider-silk | 0 | 0 | 0 | 0 | 20 |
| polydopamine-coating | 4 | 0 | 0 | 0 | 28 |
| fish-scale-hydroxyapatite | 0 | 0 | 0 | 0 | 48 |
| mussel-foot-adhesion | 0 | 7 | 0 | 0 | 50 |
| chitosan | 17 | 3 | 5 | 0 | 82 |
| **Total** | **24** | **19** | **6** | **0** | **263** |

## 3. Validation Results

| script | result |
|---|---|
| build_prototypes_db.py | ✅ Passed (24 prototypes, 403 verified entries) |
| check_chimera.py --strict | ✅ 0 violations |
| validate_consistency.py | ✅ 0 errors, 194 warnings |

## 4. Quote Preservation

verification_quote preserved after build:
- bone-structure: 1 perf_quote
- cell-membrane-ion-channel: 10 perf_quote
- chitosan: 60 perf_quote
- diatom-frustule: 11 mech_quote
- lobster-exoskeleton: 1 perf_quote
- polydopamine-coating: 4 perf_quote

## 5. Coverage

| dimension | count | percentage |
|---|---|---|
| performance_data verified | 388/419 | 93% |
| mechanisms verified | 265/528 | 50% |

## 6. Issues

1. **263 mechanisms** still have no PDF match (need PDF acquisition)
2. **19 perf rows** returned NOT_FOUND (likely wrong-source or PDF content mismatch)
3. **6 perf rows** had parse errors (API response format issues)
4. **MuPDF errors** on some PDFs (format warnings, non-blocking)
