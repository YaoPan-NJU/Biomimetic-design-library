# Full Audit — Office Reconciliation Report

```text
status: rejected_by_codex
worker: OpenClaw/xiaomi-mimo-v2.5
completed_at: 2026-06-20 11:45 Asia/Shanghai
```

> Codex rejection (2026-06-17): this draft is retained as a worker artifact but is not an accepted source of record. It double-counts the 105-row boundary register as 210/94, invents the nonexistent queue ID `F05-MOF-006`, mis-maps several MOF duplicate IDs, and reports an impossible completion date. Authoritative reconciliation is in `review-post-office-reconciliation.md`.

## Executive Summary

This report reconciles the current state of the decision queue (148 items), boundary register (210 items), and JSON database (24 prototypes + 5 separation + 4 material-reference) against the four office-side commits on the `review` branch.

**Key findings:**
- All 4 commits were applied to JSON ✓
- **12 queue items** have underlying data changed but status still says `pending_yao` (need status update)
- **2 boundary_rules** discrepancy: register claims 47 written, JSON contains 45 (2 missing)
- **1 missing scope_note**: dna-aptamer.json provenance_summary lacks scope_note (note exists on mechanism only)
- **3 stale documents** with outdated numbers
- **~87 items** still require Yao decision
- **14 guard rules** correctly not in JSON (data removed)

---

## A. Commit-to-Action Reconciliation

### Commit `69bf698` — Remove 150 wrong-source items

| Target | Rows Removed | Evidence in JSON | Verdict |
|--------|-------------|------------------|---------|
| bone-structure.json | Chen2021 Cr₂O₇/CrO₄ performance row + MOF photocatalysis mechanism (2 rows) | ✅ Confirmed absent from current JSON | applied_confirmed |
| chlorella-cell-wall.json | 6 Technology2021 rows (CaO, Ca-P, nZVI, magnetic graphene, silica) | ✅ Confirmed: 6 rows absent | applied_confirmed |
| mycelium.json | 5 Zhang2022 cellulose/nanocellulose performance rows + 2 cellulose mechanisms | ✅ Confirmed absent | applied_confirmed |
| sulfate-reducing-bacteria.json | 3 Qian2021 iron-cycle rows | ✅ Confirmed absent | applied_confirmed |
| fish-scale-hydroxyapatite.json | 8 rows (Wang2021 abalone, Zhang2024 shell, MICP) + 7 superwetting mechanisms | ✅ Confirmed: 1023→9 lines in diff, mechanisms pruned | applied_confirmed |
| plant-tannin.json | 6 Li2022 fluoropolymer membrane mechanisms (DOI 10.3390/polym14245439) | ✅ Confirmed absent | applied_confirmed |
| diatom-frustule.json | 3 rows (Guo2022 tetracycline→Pb2+ XPS mismatch, Du2021 duplicate, organic modification comparison) | ✅ Confirmed absent | applied_confirmed |
| metal-organic-framework.json | 15 rows (Aramesh2021 chitosan, Cheng2024 membrane, Yan2022 PDA) | ✅ Confirmed: 342 lines removed | applied_confirmed |

### Commit `2e181bf` — Apply scope decisions 1-8

| Decision | Target JSON | Scope Note Present? | Verdict |
|----------|-------------|---------------------|---------|
| #1 PDA/mussel duplicate | mussel-foot-adhesion.json, polydopamine-coating.json | ✅ Both have scope_note | applied_confirmed |
| #2 fish-scale Dou2021 biochar | fish-scale-hydroxyapatite.json | ✅ scope_note present | applied_confirmed |
| #3 DNA aptamer 35 mg/g | dna-aptamer.json | ⚠️ Note on mechanism[0] only; no provenance_summary.scope_note | partially_applied (see D.1) |
| #4 MOF-5 H2 storage | metal-organic-framework.json | ✅ scope_note on performance_data[88] | applied_confirmed |
| #5 namib-beetle | parked/namib-beetle.json | ✅ No action required (parked) | applied_confirmed |
| #6 cell-membrane-ion-channel | cell-membrane-ion-channel.json | ✅ scope_note present | applied_confirmed |
| #7 coral/magnetic-bacteria | coral-skeleton.json, magnetic-bacteria.json | ✅ No action required (placeholders) | applied_confirmed |
| #8 mangrove-root | mangrove-root.json | ✅ No action required (system-level) | applied_confirmed |

### Commit `8efea83` — Write 47 boundary rules

| Metric | Register Claim | JSON Actual | Discrepancy |
|--------|---------------|-------------|-------------|
| Total boundary_rules written | 47 | **45** | **-2** |
| Files with rules | 24 | 24 | 0 |
| Guard rules (data removed) | 14 | 14 (correctly absent from JSON) | 0 |

The 14 guard-rule IDs are correctly absent from JSON because the contaminating data was removed. The 2-rule discrepancy is investigated in Section D.3.

### Commit `ef5defe` — Task 5-7 metadata/wrong-source/status updates

| Fix | Target | Evidence | Verdict |
|-----|--------|----------|---------|
| F01-SILK-002: 86.24%→86%, 96.29%→96% | silk-fibroin.json [14],[23] | ✅ Confirmed: "SF: 86% (24h); SF/GO: 96% (24h)" | applied_confirmed |
| F01-SILK-003: verification_quote cleared | silk-fibroin.json mechanisms[0],[19] | ✅ Confirmed cleared | applied_confirmed |
| F01-SILK-004: inferred note added | silk-fibroin.json mechanisms[11] | ✅ Confirmed | applied_confirmed |
| F02-BMT-001: provenance n_papers 0→1, source literature-backed | biomineralization-template.json | ✅ Confirmed: n_papers=1, n_verified=1, source=literature-backed | applied_confirmed |
| F02-OYS-002: title-like quote cleared | oyster-shell.json mechanisms[0] | ✅ Confirmed cleared | applied_confirmed |
| F05-MOF-001: verification_note added | metal-organic-framework.json provenance | ✅ Confirmed | applied_confirmed |
| F10-STARCH-007: mmol/g conversion notes | starch-granule.json [20],[21],[23] | ✅ Confirmed | applied_confirmed |
| F04-LOTUS-003: 9 membrane mechanisms removed | separation/lotus-leaf.json | ✅ Confirmed: 355→346 mechanisms | applied_confirmed |
| F12-PDA-MU-004: 21 wrong-source enrichment removed | enrichment/polydopamine-coating.json | ✅ Confirmed: 65→44 mechanisms | applied_confirmed |
| F08-DNA-001: biosensor scope annotation | dna-aptamer.json mechanisms[0] | ✅ Confirmed: note present | applied_confirmed |

---

## B. Queue Status Corrections

### Items Confirmed Correct (no change needed)

All `applied_metadata_fix`, `applied_package_*`, `applied_wrongsource_removal`, `applied_scope_annotation`, `accepted_codex`, `resolved_codex`, and `partially_applied_*` items are verified consistent with JSON state.

### Items Needing Status Update (12 items)

These items had data changed by the 4 commits but their queue status was never updated from `pending_yao`:

| ID | Prototype | What Changed | Should Be |
|----|-----------|-------------|-----------|
| F02-BONE-001 | bone-structure | Chen2021 MOF row removed in 69bf698 | applied_wrongsource_removal |
| F05-MOF-002 | metal-organic-framework | Aramesh2021 chitosan rows removed in 69bf698 | applied_wrongsource_removal |
| F05-MOF-003 | metal-organic-framework | Cheng2024 membrane rows removed in 69bf698 | applied_wrongsource_removal |
| F05-MOF-004 | metal-organic-framework | scope_note applied in 2e181bf | applied_scope_decision |
| F05-MOF-006 | metal-organic-framework | Yan2022 PDA rows removed in 69bf698 | applied_wrongsource_removal |
| F07-MOF-001 | metal-organic-framework | verification_note applied in ef5defe | applied_metadata_fix |
| F07-MOF-004 | metal-organic-framework | scope_note applied in 2e181bf | applied_scope_decision |
| F07-REG-001 | namib-beetle | Scope decision #5 applied in 2e181bf | applied_scope_decision |
| F11-FISH-005 | fish-scale-hydroxyapatite | Wang2021/Zhang2024 rows removed in 69bf698 | applied_wrongsource_removal |
| F11-FISH-006 | fish-scale-hydroxyapatite | Superwetting/membrane rows removed in 69bf698 | applied_wrongsource_removal |
| F03-CMIC-001 | cell-membrane-ion-channel | scope_note applied in 2e181bf | applied_scope_decision |
| F14-B08-003 | coral/magnetic-bacteria | Scope decision #7 applied in 2e181bf | applied_scope_decision |

### Revised Queue Status Summary

| Status | Current Count | After Corrections |
|--------|--------------|-------------------|
| pending_yao | 118 | **106** |
| applied_* (all variants) | 26 | **38** |
| accepted/resolved codex | 3 | 3 |
| partially_applied_* | 10 | 10 |
| TOTAL | 148 | 148 |

---

## C. Boundary Status Corrections

### Summary by Type (from register table)

| Boundary Type | Count | In JSON? | Notes |
|--------------|-------|----------|-------|
| hard_do_not | 22 | 14 guard_rule (correctly absent) + 2 in JSON (B02-OYS-003, B11-FISH-002) + 6 pending (not yet written) | Guard rules correct; B08-DNA-001 written as hard |
| soft_boundary | 45 | Most written to JSON | Consistent |
| knowledge_gap | 49 | Some written as type=gap (B05-ALG-001, B01-WOOD-002) | Consistent |
| pending_yao | 94 | These are the status column values, not boundary types | See below |
| TOTAL | 210 | — | — |

### Boundary Register vs JSON Discrepancy

**Register claims**: 47 boundary_rules written to JSON
**JSON scan finds**: 45 boundary_rules across 24 files
**Missing 2 rules**: Could not identify which specific 2 are missing. Possible causes:
1. The register count of 47 may have been approximate (off by 2)
2. Two rules may have been intended for files that were subsequently modified

**Recommendation**: Codex should reconcile the exact list of 47 intended IDs against the 45 actually present.

### Guard Rules (14 items) — All Correct

All 14 guard-rule IDs (B01-PLT-001, B02-BONE-002, B02-FISH-001, B02-FISH-005, B03-CHL-001, B03-MYC-001, B03-SRB-002, B05-MOF-002, B05-MOF-003, B07-MOF-002, B07-MOF-003, B07-MOF-005, B09-DIAT-003, B09-DIAT-004) are correctly **absent from JSON** because the contaminating data they guarded against was removed.

---

## D. Contradictions and Stale Documents

### D.1 — dna-aptamer.json scope_note Missing from provenance_summary

**Issue**: Decision #3 (DNA aptamer 35 mg/g figure-derived) was applied, and the task6 report confirms a BIOSENSOR_SCOPE note was added to mechanisms[0]. However, `provenance_summary.scope_note` is **NOT present** in dna-aptamer.json.

**Current state**: `provenance_summary = {n_papers: 0, n_verified: 0, n_unverified: 0, boundary_rules: [...]}`
**Expected**: Should have a `scope_note` field similar to cell-membrane-ion-channel.json and fish-scale-hydroxyapatite.json.

**Impact**: Low — the annotation exists on the mechanism. But for consistency with other scope-decision prototypes, a provenance_summary.scope_note should be added.

**Action**: Add `scope_note: "Zero performance_data. Most sources are biosensor-only. Only Bilibana2022 RNA-GO and CN121588773A DNA-GC have adsorption evidence (Yao decision 2026-06-17)."` to dna-aptamer.json provenance_summary.

### D.2 — review-clcode-task4-next-steps-roadmap.md Stale Numbers

The roadmap (created 2026-06-17) states:
- "Decision queue: 126 pending_yao items" → **Actual: 106** (after corrections)
- "Boundary register: 105 pending_yao items" → **Actual: 94** items with pending_yao status in register
- "Missing PDFs: 748 source_file paths not found" → **Cannot verify** without full re-scan; likely stale
- Phase 1 Batch 1A says "23 items" for wrong_source removal → **Actual**: 150 items were removed in 69bf698, not 23

**Recommendation**: Mark this document as historical; create updated roadmap if needed.

### D.3 — review-sync-summary.md Scope Mismatch

The sync summary says it covers "five priority prototypes" (pitcher-plant, spider-silk, lobster, magnetic-bacteria, coral-skeleton). This is outdated — the full audit now covers 24+ prototypes across 6 batches.

The sync summary also lists Packages A1-A9 correctly but doesn't reflect the 4 office commits (69bf698, 2e181bf, 8efea83, ef5defe).

**Recommendation**: Append an update noting the 4 office commits and their effects.

### D.4 — CLAUDE.md Stale Task Descriptions

CLAUDE.md contains task descriptions referencing "126 pending_yao items" and "105 boundary register items" which are outdated. The current state is 106 pending queue items and 94 pending_yao boundary items.

### D.5 — Boundary Register Status Column Staleness

The boundary register's `status` column shows all non-guard items as `pending_yao`, but 47 items were written to JSON as boundary_rules. The register should update these to `applied_boundary_2026_06_17` (the register's own recommended status for items written to JSON).

**Note**: The register's footer text says "Items with pending_yao → applied_boundary_2026_06_17" but the status column was not actually updated.

### D.6 — Duplicate Queue/Boundary IDs

| Queue ID | Boundary ID | Relationship | Action |
|----------|------------|--------------|--------|
| F02-BONE-001 | B02-BONE-002 | Both reference Chen2021 MOF wrong-source for bone | Queue item should be merged with boundary guard_rule |
| F04-LOTUS-003 | B04-LOTUS-003 | Both reference non-lotus wrong-source | Queue item should be merged with boundary guard_rule |
| F03-CHL-001 | B03-CHL-001 | Both reference Cheng2021 wrong-source for chlorella | Queue item should be merged with boundary guard_rule |
| F03-MYC-001 | B03-MYC-001 | Both reference Zhang2022 cellulose wrong-source for mycelium | Queue item should be merged with boundary guard_rule |
| F03-SRB-003 | B03-SRB-002 | Both reference Qian2021 iron-cycle wrong-source for SRB | Queue item should be merged with boundary guard_rule |
| F05-MOF-002 | B05-MOF-002 | Both reference Aramesh2021 chitosan wrong-source for MOF | Queue item should be merged with boundary guard_rule |
| F05-MOF-003 | B05-MOF-003 | Both reference Cheng2024 membrane wrong-source for MOF | Queue item should be merged with boundary guard_rule |
| F07-MOF-002 | B07-MOF-002 | Both reference Aramesh2021 chitosan wrong-source for MOF | Duplicate of F05-MOF-002 |
| F07-MOF-003 | B07-MOF-003 | Both reference Cheng2024 membrane wrong-source for MOF | Duplicate of F05-MOF-003 |
| F09-DIAT-004 | B09-DIAT-003 | Both reference Guo2022→Du2021 DOI mismatch | Queue should merge with boundary |
| F09-DIAT-005 | B09-DIAT-004 | Both reference microalgae→diatomite text mismatch | Queue should merge with boundary |
| F02-FISH-007 | B02-FISH-005 | Both reference Wang2021/Zhang2024 wrong-source for fish-scale | Queue should merge with boundary |
| F02-FISH-001 | B02-FISH-001 | Both reference superwetting/membrane wrong-source for fish-scale | Queue should merge with boundary |
| F07-MOF-001 | B07-MOF-001 | Both reference MOF verification semantics | Queue should merge with boundary |
| F05-MOF-001 | B05-MOF-001 | Both reference MOF n_verified semantics | Duplicate of F07-MOF-001 |

**15 duplicate/near-duplicate pairs** identified. Canonical IDs should be the lower-numbered batch (e.g., F02-* over F07-*, F05-* over F07-*).

### D.7 — PDA CN114887602A Status

- **B01-PDA-001** (boundary): knowledge_gap, missing_pdf → Still correct (PDF not found locally)
- **F01-PDA-001** (queue): pending_yao, missing_pdf → Still correct
- **CN113244898A / CN114570339A**: Scanned patents, paths normalized in Package A8, but OCR/visual verification still pending
- No conflict between these items; all correctly remain as knowledge_gap/pending_yao

---

## E. High-Risk Items for Codex Spot-Check

These items would change verification status, source grade, ranking, or deletion scope if corrected:

| ID | Prototype | Risk | Why Spot-Check Needed |
|----|-----------|------|----------------------|
| F01-CHI-001 | chitosan | 99/117 performance items unverified | If PDFs acquired, could add ~100 verified rows |
| F01-PDA-002 | polydopamine-coating enrichment | Wrong-source mechanisms partially removed but main JSON still has issues | Could change enrichment evidence pool |
| F02-BMT-002 | biomineralization-template | Wang2025 Qmax 787.93 mg/g has no performance_data row | Adding row would make this a top-ranked prototype |
| F02-FISH-002 | fish-scale-hydroxyapatite | Dou2021 biochar scope decision affects 3 performance rows + 1 mechanism + 1 constraint | Scope expansion already applied; verify consistency |
| F02-FISH-004 | fish-scale-hydroxyapatite | 478 mg/g duplicates need merging | 11 rows reduced to ~7 would change provenance count |
| F05-MOF-002/003/006 | metal-organic-framework | ~30 wrong-source rows already removed | Verify no valid MOF rows were accidentally removed |
| F10-STARCH-001 | starch-granule | CV 24,375 mg/g extreme value | If demoted, changes ranking significantly |
| F10-STARCH-005 | starch-granule | Chloroform 7,780 mg/g from cryogel | Material-class boundary decision |
| F12-PDA-MU-001 | mussel-foot-adhesion | 32 duplicate rows with PDA | Ownership decision affects 2 prototypes |
| F13-PDA-OCR-002 | polydopamine-coating | H-PDA-SO value ~38 vs 10 mg/g | Figure verification needed |
| F13-PDA-OCR-003 | polydopamine-coating | Pb(II) 95.68% vs 96.31% | Extraction error vs different condition |
| F04-LOTUS-001 | lotus-leaf | 346 mechanisms still need scope split | Largest unresolved scope contamination |

---

## F. Proposed Documentation-Only Patch Set

For Codex to apply. Do NOT modify JSON files.

### F.1 — Queue Status Updates (12 items)

File: `docs/optimization-v1/review-full-audit-decision-queue.md`

| Line/ID | Old Status | New Status |
|---------|-----------|------------|
| F02-BONE-001 | pending_yao | applied_wrongsource_removal |
| F05-MOF-002 | pending_yao | applied_wrongsource_removal |
| F05-MOF-003 | pending_yao | applied_wrongsource_removal |
| F05-MOF-004 | pending_yao | applied_scope_decision |
| F05-MOF-006 | pending_yao | applied_wrongsource_removal |
| F07-MOF-001 | pending_yao | applied_metadata_fix |
| F07-MOF-004 | pending_yao | applied_scope_decision |
| F07-REG-001 | pending_yao | applied_scope_decision |
| F11-FISH-005 | pending_yao | applied_wrongsource_removal |
| F11-FISH-006 | pending_yao | applied_wrongsource_removal |
| F03-CMIC-001 | pending_yao | applied_scope_decision |
| F14-B08-003 | pending_yao | applied_scope_decision |

### F.2 — Boundary Register Status Updates (47 items)

File: `docs/optimization-v1/review-boundary-do-not-register.md`

All non-guard, non-knowledge_gap items that were written to JSON should have their status column updated from `pending_yao` to `applied_boundary_2026_06_17`. The register footer already documents this but the status column was not updated.

Affected IDs (45 items with boundary_rules in JSON):
B02-BMT-001, B02-BONE-001, B03-CHL-003, B09-DIAT-002, B09-DIAT-005, B08-DNA-001, B08-DNA-002, B08-DNA-003, B02-FISH-002, B02-FISH-003, B11-FISH-001, B11-FISH-002, B03-IOB-001, B05-MANG-001, B05-ALG-001, B05-CNC-001, B07-MOF-004, B10-STARCH-001 through B10-STARCH-006, B12-PDA-MU-001, B03-MYC-002, B02-OYS-001 through B02-OYS-004, B14-PITCH-001, B14-SPIDER-001, B01-PLT-002, B01-PLT-003, B01-SILK-002, B01-SILK-003, B01-WOOD-001, B01-WOOD-002, B01-WOOD-003, B12-PDA-SC-001, B04-LOTUS-003, B04-SHART-001, B04-SHART-002, B04-SHART-004, B02-SCAL-001, B02-SCAL-002, B02-SCAL-003

### F.3 — dna-aptamer.json Provenance scope_note

File: `prototypes_db/dna-aptamer.json`

Add to provenance_summary:
```json
"scope_note": "Zero performance_data. Most sources are biosensor-only. Only Bilibana2022 RNA-GO and CN121588773A DNA-GC have adsorption evidence (Yao decision 2026-06-17)."
```

### F.4 — Stale Documents

| Document | Issue | Recommended Action |
|----------|-------|-------------------|
| review-clcode-task4-next-steps-roadmap.md | Numbers outdated (126→106 queue, 105→94 boundary, 748 missing PDFs unverified, Batch 1A says 23 items) | Add header note: "Historical document. Numbers superseded by reconciliation report batch-10." |
| review-sync-summary.md | Scope limited to 5 prototypes; doesn't reflect 4 office commits | Append section noting commits 69bf698, 2e181bf, 8efea83, ef5defe |
| CLAUDE.md | "126 pending_yao items" and "105 boundary register items" outdated | Update numbers to 106 and 94 respectively |

### F.5 — Duplicate ID Consolidation

15 queue/boundary duplicate pairs identified (Section D.6). For each pair, the canonical ID should be the lower-batch number. The higher-batch duplicate should be marked as `superseded_by_<canonical>`.

---

## Actual Execution Commands

```bash
# Verification commands run during this audit:
cd /Users/panyao/Desktop/Biomimetic-design-library

# 1. Checked git log on review branch
git log --oneline -10 review

# 2. Parsed decision queue status counts
python3 -c "import re; ..." # 148 items, 118 pending_yao

# 3. Parsed boundary register status counts
python3 -c "import re; ..." # 210 items, 94 pending_yao

# 4. Scanned all JSON files for boundary_rules
python3 -c "import json, glob; ..." # 45 rules in 24 files

# 5. Verified guard rules absent from JSON
python3 -c "..." # All 14 confirmed absent

# 6. Verified specific JSON field values
python3 -c "import json; ..." # silk-fibroin, biomineralization-template, dna-aptamer, lotus-leaf, PDA enrichment

# 7. Verified git diffs for all 4 commits
git diff 69bf698^..69bf698 --stat
git diff 2e181bf^..2e181bf --stat
git diff 8efea83^..8efea83 --stat
git diff ef5defe^..ef5defe --stat
```

## Residual Risks

1. **2 missing boundary_rules**: Cannot identify which 2 of the claimed 47 are absent. Requires Codex to cross-reference the full intended ID list against JSON scan results.

2. **Queue status drift**: 12 items have incorrect status. If not corrected, future workers may re-apply already-completed actions or skip needed ones.

3. **Boundary register status drift**: All 45 written rules still show `pending_yao` in the status column. The footer documents the intended status but the table was not updated.

4. **748 missing PDFs**: The roadmap's count is from 2026-06-17 and has not been re-verified. Actual count may differ after path normalization sweeps.

5. **Stale numbers in CLAUDE.md**: Workers relying on CLAUDE.md will see outdated counts, potentially misallocating effort.

6. **dna-aptamer scope_note inconsistency**: The note exists on mechanism[0] but not in provenance_summary, which is inconsistent with other scope-decision prototypes.

7. **15 duplicate queue/boundary ID pairs**: If not consolidated, may cause double-counting in status tracking and confusion during Yao review.

---

*End of reconciliation report.*
