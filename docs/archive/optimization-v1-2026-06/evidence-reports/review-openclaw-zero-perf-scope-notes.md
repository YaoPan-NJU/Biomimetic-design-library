---
status: ready_for_qoderwork_acceptance
---

# Review: Zero-Performance Prototypes -- scope_note Annotations

**Date:** 2026-06-18
**Scope:** 3 prototypes in `prototypes_db/` with zero or proxy performance data
**Action:** Added `scope_note` field to `provenance_summary` in each file

## Files Modified

| File | Key Issue |
|---|---|
| `coral-skeleton.json` | No literature support; mechanism is LLM-inferred; narrative source is antifouling review, not CaCO3 adsorption |
| `magnetic-bacteria.json` | Sole source is MTB ecology review (Goswami 2022), not adsorption; mechanism is LLM-inferred |
| `lobster-exoskeleton.json` | Proxy prototype; performance data (1385 mg/g) belongs to synthetic chitosan beads, not lobster; redundant with `chitosan.json`; source PDF missing |

## Changes Made

Each file received a single new field `scope_note` inside the existing `provenance_summary` object. No other fields were modified. The scope_note documents:

1. Why the prototype has zero or unreliable performance data.
2. What specific literature gap must be filled before reactivation.
3. That a Yao decision is pending on whether to move the prototype to `parked/`.

## Validation

Ran `python3 -X utf8 tools/validate_consistency.py` after edits:

- **1 error** (pre-existing, in `bone-structure` -- unrelated to this change)
- **181 warnings** (all pre-existing)
- **No new errors or warnings introduced** by the scope_note additions.

## Next Steps

- Yao decision on each prototype: move to `parked/` or deprecate.
- If reactivating, source peer-reviewed adsorption papers specific to each organism before removing the scope_note.
