# Task 5 — Metadata Fix Batch Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Fixes Applied

### 1. silk-fibroin — False Precision (F01-SILK-002)
- `performance_data[14].value`: `SF: 86.24% (24h); SF/GO: 96.29% (24h)` → `SF: 86% (24h); SF/GO: 96% (24h)`
- `performance_data[23].value`: `SF: 86.24%; SF/GO: 96.29%` → `SF: 86%; SF/GO: 96%`
- Source: Martis2022 PDF text supports rounded 86% and 96% values

### 2. silk-fibroin — Invalid Verification Quotes (F01-SILK-003)
- `mechanisms[0].verification_quote`: Cleared (was paper title, not text excerpt)
- `mechanisms[19].verification_quote`: Cleared (same issue)
- Both set to `verification: needs_review`

### 3. silk-fibroin — Carboxyl Group Inferred Note (F01-SILK-004)
- `mechanisms[11].note`: Added `-COOH/羧基 claim inferred, not in Epa/Gupta quoted source`
- The 基本原理 claims amino, carboxyl, and amide groups; source only supports hydroxyl, ketone, and amine

### 4. biomineralization-template — Provenance Metadata (F02-BMT-001)
- `provenance_summary.n_papers`: 0 → 1
- `provenance_summary.n_verified`: 0 → 1
- `mechanisms[0].source`: `llm_inference` → `literature-backed`
- Wang2025 is a real source with PDF quote

### 5. oyster-shell — Title-Like Quote (F02-OYS-002)
- `mechanisms[0].verification_quote`: Cleared (was `oyster shell biochar for heavy metal adsorption`, a title not a quote)
- Set to `verification: needs_review`

### 6. MOF — Verification Semantics Note (F05-MOF-001)
- `provenance_summary.verification_note`: Added explanation that `n_verified=252` counts `single_source` rows (review-table assertions), NOT full quote+locator verification
- No rows changed; semantic clarification only

### 7. starch-granule — mmol/g Unit Conversion Notes (F10-STARCH-007)
- `performance_data[20]`: Added `2.33 mmol/g ≈ 148.3 mg/g (Cu²⁺)`
- `performance_data[21]`: Added `1.25 mmol/g ≈ 259.0 mg/g (Pb²⁺)`
- `performance_data[23]`: Added `1.36 mmol/g ≈ 86.4 mg/g (Cu²⁺)`

## Already Handled by Qoder (No Fix Needed)

| item | prototype | status |
|---|---|---|
| F09-DIAT-004 | diatom-frustule | mechanisms[0] already has correct Du2021 DOI |
| F02-BONE-004 | bone-structure | mechanisms[1] boundary_conditions already marked `llm_inferred` + `needs_review` |
| F02-BMT-003 | biomineralization-template | causal_chain already has `from_source` basis with Wang2025 locators |

## Remaining Items (Need Deeper Work)

| item | prototype | issue | status |
|---|---|---|---|
| F03-IOB-003 | iron-oxidizing-bacteria | mechanisms[2-5] have empty source_file/verification_quote | needs PDF reading |
| F10-STARCH-001 | starch-granule | concentration-derived ranges need splitting | needs scope decision |
| F10-STARCH-002 | starch-granule | Khoo2023 review maxima need demotion | needs scope decision |
| F02-OYS-003 | oyster-shell | abalone HA vs oyster species ambiguity | needs Yao decision |

## Summary

| category | count |
|---|---|
| Fixes applied | 12 changes across 5 files |
| Already handled by Qoder | 3 items |
| Remaining (need deeper work) | 4 items |
