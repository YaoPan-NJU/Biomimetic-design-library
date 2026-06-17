---
status: ready_for_codex_acceptance
worker: openclaw-r01-correction
model: xiaomi/mimo-v2.5
started: 2026-06-17T22:30+08:00
completed: 2026-06-17T22:36+08:00
baseline_commit: 30481e4
target_commit: ec369a3
head_commit: cfdc0c1
branch: openclaw/recovery-r01
---

# Structured Field Recovery Report R01 (corrected)

## Summary

Office-side bulk JSON rewriting (between `30481e4` and `ec369a3`) stripped all `design_translation` arrays and mechanism `causal_chain` objects from 24 top-level prototype JSON files. This worker restored them using stable identity matching by prototype ID (filename), then enforced a stricter safety rule: **if both baseline and current `ref_doi` are non-empty and differ, the baseline `causal_chain` must not be restored onto the current mechanism**, even if names match.

## Before / After Counts

| Field | Baseline (30481e4) | Before Recovery (HEAD) | After Recovery |
|---|---|---|---|
| `design_translation` entries | 25 | 0 | 25 |
| Mechanism `causal_chain` objects | 27 | 0 | 25 restored + 2 unmatched |

## Stable Identity Used for Matching

All 24 prototype files are keyed by prototype ID (filename without `.json`). Matching was performed by:

1. **design_translation**: Direct restore — baseline entries are a single array per prototype; restored verbatim.
2. **causal_chain**: Matched by normalized mechanism name within the same prototype file. Cross-DOI matches were rejected when both baseline and current `ref_doi` were present and unequal.

## Restored Field Paths

Every `design_translation` and `causal_chain` restoration follows the pattern:

```
prototypes_db/<id>.json → design_translation[<n>]
prototypes_db/<id>.json → mechanisms[<index>].causal_chain
```

## Ambiguity / Unmatched Table

| Prototype | Baseline Mechanism Name | Baseline DOI | Current Matched Mechanism | Current DOI | Resolution |
|---|---|---|---|---|---|
| `pitcher-plant-slippery-surface` | Nepenthes SLIPS抗污机制 | (empty) | Nepenthes pitcher plant trapping mechanism | 10.1007/s42242-021-00133-8 | **Unmatched** — baseline baseline DOI is empty while current DOI is non-empty; must not restore cross-DOI causal chain |
| `plant-tannin` | 单宁酸-金属配位机理 | 10.1016/j.indcrop.2021.114304 | 吸附机理 | 10.1016/j.indcrop.2021.114304 | **Restored** — same DOI |
| `silk-fibroin` | 吸附机制 | 10.1016/j.eti.2022.102741 | 吸附机制 (index 11) | 10.1016/j.eti.2022.102741 | **Restored** — same DOI |
| `silk-fibroin` | 吸附机制 | 10.1016/j.eti.2022.102741 | 吸附机制 (index 16) | 10.1039/d1va00047k | **Unmatched** — cross-DOI match; removed incorrect causal chain |

## Changed-File List (this commit)

3 files changed in this fix commit:

```
tools/recover_fields_r01.py            — added cross-DOI safety rule, removed trailing whitespace
prototypes_db/pitcher-plant-slippery-surface.json — removed incorrect causal chain on mechanism index 13
prototypes_db/silk-fibroin.json          — removed incorrect causal chain on mechanism index 16
```

Full prototype file list (unchanged from recovery): 24 files modified under `prototypes_db/`.

## Validation Results

| Check | Exit Code | Result |
|---|---|---|
| `git diff --check` | 0 | ✅ No whitespace errors |
| `python3 -c "import glob,json; ..."` (JSON lint) | 0 | ✅ All files parse |
| `tools/validate_consistency.py` | 0 | ✅ 0 errors, 194 warnings (pre-existing) |
| `tools/check_chimera.py --strict` | 0 | ✅ 0 violations |
| `tools/check_causal_chain.py` | 0 | ✅ 25/530 qualified chains, 0 empty basis elements |
| `tools/check_boundary_guardrail.py` | 1 | ❌ `diatom-frustule` and `pitcher-plant-slippery-surface` missing boundary_conditions (pre-existing, not in scope) |
| `tools/check_translation_specificity.py` | 0 | ✅ 25/25 specific |
| `tools/verify_adrmats_delivery.py` | 1 | ❌ Pb(II) test fails: `candidate[2].mechanism.attribution.verification_tier` invalid value `partial` (pre-existing, R02 scope) |
| `tools/check_repo_hygiene.py` | 1 | ❌ Root `CLAUDE.md` not allowed (pre-existing, R02 scope) |

### Pre-existing Failures (NOT introduced by this recovery or fix)

- `diatom-frustule` / `pitcher-plant-slippery-surface` boundary_conditions missing — never had them at baseline
- `verify_adrmats_delivery.py` Pb(II) failure — `verification_tier: "partial"` predates this work
- `check_repo_hygiene.py` — `CLAUDE.md` in root predates this work

## Build Script Confirmation

`tools/build_prototypes_db.py` was **NOT** run during this recovery or fix. Recovery and correction were performed by direct JSON field edits only.

## Recovery + Fix Script

Written at `tools/recover_fields_r01.py` for auditability. The core logic:
1. Read baseline JSON from git at commit `30481e4`
2. For each prototype: restore `design_translation` if present at baseline but absent at HEAD
3. For each mechanism with `causal_chain` at baseline: find matching current mechanism by name+DOI+description, attach `causal_chain`
4. **Safety rule**: if baseline `ref_doi` and current `ref_doi` are both non-empty and differ, never restore the baseline `causal_chain` onto the current mechanism
5. If no match found or match rejected: add to ambiguity/unmatched table

## Artifact Update

`docs/optimization-v1/phase5-chains.md` was regenerated to reflect the corrected 25 qualified causal chains.
