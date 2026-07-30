---
title: R1-C Ledger v2 Validation Report
status: done
date: 2026-06-19
author: claude-code (coordinator)
---

# R1-C Ledger v2 Validation Report

## Summary

The existing 1,204 ledger entries are confirmed as **untrusted v1 migration input**.
All have `applied_commit=PENDING`. The v2 schema and validator are now in place.

## Validation Results

| Metric | Count |
|--------|-------|
| Total entries | 1,204 |
| Valid (structurally) | 1,204 |
| PENDING | 1,204 (100%) |
| Errors | 0 |
| Schema warnings | 628 |

## Schema Warnings (v1 → v2 migration gaps)

### Invalid Dispositions (248 entries)

The v1 value `replaced` is not in the v2 schema. These 248 entries were written by
the M2-a restore and need disposition mapping:

- `replaced` → likely `restored` (field was empty at HEAD, value filled from history)

### Invalid Bases (326 entries)

The v1 value `review` is not in the v2 schema. These 326 entries need basis mapping:

- `review` → likely `extraction` (value came from extraction output, not direct quote)

### Invalid Identity Levels (54 entries)

The v1 value `exact_fingerprint` is not in the v2 schema:

- `exact_fingerprint` → likely `perf_3` or `mech_3` (fingerprint-level match)

### Other Level: `prototype` (36 entries)

These are prototype-level entries (tier/lifecycle assignments), not field-level.
They should use level `unknown` or a new level `prototype_metadata`.

## What R1-C Delivered

1. **Ledger v2 schema**: `docs/registries/canon-recovery-ledger-v2.schema.json`
   - Required fields: id, prototype_id, field_path, record_identity, disposition,
     basis, applied_commit
   - Optional: source_file, source_hash, quote, locator, timestamp
   - Valid dispositions: restored, ambiguous, refuted, corrected, downgraded,
     removed, unchanged, scope_caveat
   - Valid bases: direct_quote, extraction, ambiguity_gate, correction, scope_review, none

2. **Validator**: `tools/validate_ledger_v2.py`
   - Reports disposition/basis/level distribution
   - Flags duplicate IDs, missing required fields, invalid enums, weak identity,
     array-index-only paths, orphan entries
   - No external package dependencies

3. **This report**: Documents v1→v2 migration gaps for future correction

## Migration Notes

The 1,204 v1 entries should NOT be bulk-corrected. They are retained as-is for
traceability. R1+ entries will conform to v2. The v1 migration gaps (replaced→restored,
review→extraction, exact_fingerprint→perf_3) are documented for when a future
corrective pass is authorized.
