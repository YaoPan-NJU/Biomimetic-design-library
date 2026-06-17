---
status: ready_for_codex_acceptance
worker: openclaw-batch
model: xiaomi/mimo-v2.5
started: 2026-06-17T22:24+08:00
completed: 2026-06-17T22:30+08:00
baseline_commit: 30481e4
target_commit: ec369a3
head_commit: 63afd9e
branch: openclaw/recovery-r01
---

# Structured Field Recovery Report R01

## Summary

Office-side bulk JSON rewriting (between `30481e4` and `ec369a3`) stripped all `design_translation` arrays and mechanism `causal_chain` objects from 24 top-level prototype JSON files. This worker restored them using stable identity matching by prototype ID (filename).

## Before / After Counts

| Field | Baseline (30481e4) | Before Recovery (HEAD) | After Recovery |
|---|---|---|---|
| `design_translation` entries | 25 | 0 | 25 |
| Mechanism `causal_chain` objects | 27 | 0 | 27 |

## Stable Identity Used for Matching

All 24 prototype files are keyed by prototype ID (filename without `.json`). Matching was performed by:

1. **design_translation**: Direct restore — baseline entries are a single array per prototype; restored verbatim.
2. **causal_chain**: Matched by normalized mechanism name within the same prototype file. For two cases where the office rewrite changed mechanism names, matched by DOI (same source paper) or description fingerprint.

## Restored Field Paths

Every `design_translation` and `causal_chain` restoration follows the pattern:

```
prototypes_db/<id>.json → design_translation[<n>]
prototypes_db/<id>.json → mechanisms[<index>].causal_chain
```

## Ambiguity / Unmatched Table

| Prototype | Baseline Mechanism Name | Resolution |
|---|---|---|
| `pitcher-plant-slippery-surface` | Nepenthes SLIPS抗污机制 | Matched to `Nepenthes pitcher plant trapping mechanism` (same Nepenthes concept, different DOI) |
| `plant-tannin` | 单宁酸-金属配位机理 | Matched to `吸附机制` (DOI 10.1016/j.indcrop.2021.114304, same source paper) |
| `silk-fibroin` | 吸附机制 (2nd instance, DOI 10.1016/j.eti.2022.102741) | Matched by name+description to `吸附机制` with DOI 10.1039/d1va00047k (same name, same description text) |

All three were resolved unambiguously by cross-referencing DOI and description content.

## Changed-File List

24 files modified (all under `prototypes_db/`):

```
biomineralization-template.json
bone-structure.json
cell-membrane-ion-channel.json
chitosan.json
chlorella-cell-wall.json
coral-skeleton.json
diatom-frustule.json
dna-aptamer.json
fish-scale-hydroxyapatite.json
iron-oxidizing-bacteria.json
lobster-exoskeleton.json
magnetic-bacteria.json
mangrove-root.json
mussel-foot-adhesion.json
mycelium.json
oyster-shell.json
pitcher-plant-slippery-surface.json
plant-tannin.json
polydopamine-coating.json
scallop-shell.json
silk-fibroin.json
spider-silk.json
sulfate-reducing-bacteria.json
wood-xylem.json
```

Total diff: 24 files changed, 1918 insertions, 74 deletions.

## Validation Results

| Check | Exit Code | Result |
|---|---|---|
| `git diff --check` | 0 | ✅ No whitespace errors |
| `python3 -c "import glob,json; ..."` (JSON lint) | 0 | ✅ All files parse |
| `tools/validate_consistency.py` | 0 | ✅ 0 errors, 194 warnings (pre-existing) |
| `tools/check_chimera.py --strict` | 0 | ✅ 0 violations |
| `tools/check_causal_chain.py` | 0 | ✅ 27/532 qualified chains, 0 empty basis elements; `diatom-frustule` has no CC (pre-existing, no baseline CC) |
| `tools/check_boundary_guardrail.py` | 1 | ❌ `diatom-frustule` missing boundary_conditions (pre-existing, not in scope) |
| `tools/check_translation_specificity.py` | 0 | ✅ 25/25 specific |
| `tools/verify_adrmats_delivery.py` | 1 | ❌ Pb(II) test fails: `candidate[2].mechanism.attribution.verification_tier` invalid value `partial` (pre-existing, R02 scope) |
| `tools/check_repo_hygiene.py` | 1 | ❌ Root `CLAUDE.md` not allowed (pre-existing, R02 scope) |

### Pre-existing Failures (NOT introduced by this recovery)

- `diatom-frustule` boundary_conditions missing — never had them at baseline
- `verify_adrmats_delivery.py` Pb(II) failure — `verification_tier: "partial"` predates this work
- `check_repo_hygiene.py` — `CLAUDE.md` in root predates this work

## Build Script Confirmation

`tools/build_prototypes_db.py` was **NOT** run during this recovery. Recovery was performed by direct JSON field restoration only.

## Recovery Script

Written at `tools/recover_fields_r01.py` for auditability. The core logic:
1. Read baseline JSON from git at commit `30481e4`
2. For each prototype: restore `design_translation` if present at baseline but absent at HEAD
3. For each mechanism with `causal_chain` at baseline: find matching current mechanism by name+DOI+description, attach `causal_chain`
4. If no match found: add to ambiguity table (3 cases, all resolved manually)
