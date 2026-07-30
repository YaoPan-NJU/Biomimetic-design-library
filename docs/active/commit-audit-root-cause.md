---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
---

# Commit Audit & Root-Cause Report

Independently reproduced failure timeline and the operational rules it implies.
Derived from `git log`/`git show` on the actual tree, not from historical reports.

## 1. Failure timeline (all confirmed as ancestors of local `review@4987c0a`)

| Commit | What happened | Verified consequence |
|---|---|---|
| `1e50581` | Office-side bulk JSON rewrite stripped root `design_translation`, mechanism `causal_chain`, boundary registrations, and 63 quotes; its validation report was produced from a different state than the committed tree | Structured data only partially recovered later |
| `1313dd5` | `build_prototypes_db.py` run against frozen canon; stripped 15 quotes from surviving chitosan performance rows | Proves the build is destructive on canon |
| `13dfdbf` | Keyword-based PDF sentence matching upgraded **228 mechanisms** to `partial`; independent audits showed **all 48 chitosan upgrades invalid** and **only 6 of 36 mussel upgrades acceptable** | Mechanism coverage at cloud HEAD is materially overstated |
| `82fa2c0` | Canon rebuild rewrote all 24 root prototype files; removed 242 performance quotes + 242 mechanism quotes + locators + translations + causal chains + boundaries; reintroduced an older 419/528 row set | Largest unresolved evidence regression |
| `e4dc2d0` | Prototype expansion 24→36 added useful prototypes but **inherited the damaged core**, reintroduced 13 diatom performance rows, and added 12 root prototypes absent from `feature-mapping.json` | Cloud HEAD is not a correct canonical baseline |

## 2. Root cause

**Immediate cause:** destructive regeneration of frozen canon by
`tools/build_prototypes_db.py`. The script generates a subset of the canon schema and
merges by **unstable row keys**; empty/regenerated fields silently replace manually
curated evidence, with **no invariant that rejects data loss**.

**Deeper cause:** project instructions had already prohibited running the script, but
later task files (`CLAUDE-CODE-TASK-64-68/69-73`, now archived) instructed workers to
run it. Prohibition that lives only in prose is not enforced.

**Compounding factor:** bulk auto-verification (`13dfdbf`) treated DOI→PDF mapping and
keyword overlap as evidence, inflating coverage and masking the quote/locator loss.

## 3. What recovery must NOT repeat (operational rules)

1. Never run `build_prototypes_db.py` against canon (it is staging-only after M1).
2. Never reconstruct a whole JSON from extraction outputs or a historical commit.
3. Never match cross-version records by array index.
4. Never let an empty field replace a non-empty field.
5. Never restore a row recorded in `docs/registries/refuted-log.md`.
6. Never upgrade `verification` because a DOI maps to a PDF or keywords match.
7. Never trust a report's totals — recompute from the committed JSON at the named commit.

## 4. Evidence regressions to reverse (M2 scope)

- Restore accepted performance quotes + locators lost at `82fa2c0`.
- Restore translations, causal chains, boundary structures, accepted top-level fields.
- Return core diatom row set to the accepted deduplicated state.
- Roll back `13dfdbf` mechanism upgrades except the 6 independently accepted mussel-v3 rows.

## 5. The `prototype_metadata` gap (M3 scope)

`feature-mapping.json → prototype_metadata` has **24** entries (the true Core set). **12**
prototypes present on disk have **no** metadata:

```
alginate  cactus-spine  cellulose-nanocrystal  diatom-inspired-porous  lotus-leaf
metal-organic-framework  namib-beetle  shark-skin  silkworm-silk  starch-granule
superhydrophobic-artificial  water-strider-leg
```

`biomineralization-template` and `dna-aptamer` are **present** in prototype_metadata and
must not be treated as missing. (An earlier audit wrongly counted recommendation-layer
`id` occurrences; the authoritative count is `prototype_metadata` keys.)

Root/subdir duplication is also observed (5 separation prototypes copied root-ward at
`e4dc2d0` from `b6ab7df` originals; 4 materials_reference + namib-beetle present in both
locations with unconfirmed generation relationship). These are **recorded only** —
merge/delete/demote decisions are deferred to M2/M3 with Yao approval.

## 6. Pre-existing validation baseline (record, do not change without approval)

- `check_repo_hygiene.py`: 1 failure — root `CLAUDE.md` not in allowlist. Pre-existing;
  M0 must not add failures (Phase 0 verified: still exactly 1).
- `validate_consistency.py`: ~1 pre-existing error (bone-structure R12) + ~130 warnings
  (per archived reconciliation report) — to be re-baselined in M1/M2.
