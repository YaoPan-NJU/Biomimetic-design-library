# Task 4 — Next Steps Roadmap

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Current State Summary

| dimension | status |
|---|---|
| Decision queue | 126 pending_yao items across 28 prototypes |
| Boundary register | 105 pending_yao items (22 hard_do_not, 43 soft_boundary, 40 knowledge_gap) |
| Missing PDFs | 748 source_file paths not found; 18 prototypes affected |
| Uncommitted changes | 3 modified files + 4 new files (this session) |
| Submodule | tools/litextract initialized at 203b0cf |

## Phase 1: Yao Approval Gate (Immediate Priority)

**Goal:** Clear the decision queue backlog so database edits can resume.

### Batch 1A — wrong_source Removal (23 items)
- All 23 items are clear domain mismatches with direct literature evidence
- **Action:** Yao approves → Claude Code/Qoder applies removals to `prototypes_db/*.json`
- **Estimated effort:** 1 hour (Yao review) + 2 hours (automated removal)
- **Impact:** Cleans ~100+ contaminated rows across fish-scale, MOF, diatom, lotus, chlorella, mycelium, SRB, bone, PDA, plant-tannin

### Batch 1B — hard_do_not Boundaries (22 items)
- Overlaps significantly with 1A wrong_source items
- **Action:** Yao approves → boundary conditions added to JSON
- **Estimated effort:** 30 min (Yao review) + 1 hour (automated)

### Batch 1C — Metadata Fixes (25 partial items)
- Path normalization, precision narrowing, quote insertion, provenance correction
- **Action:** Yao approves → Claude Code applies mechanical fixes
- **Estimated effort:** 30 min (Yao review) + 1 hour (automated)

### Batch 1D — Scope Decisions (10-15 needs_human_decision items)
- PDA/mussel 32-row ownership
- cell-membrane-ion-channel adsorption vs separation
- coral-skeleton / magnetic-bacteria retirement
- namib-beetle retirement
- fish-scale biochar scope expansion
- **Action:** Yao reviews individually
- **Estimated effort:** 1-2 hours (Yao decision time)

## Phase 2: PDF Recovery (After Phase 1)

**Goal:** Acquire critical missing PDFs to unblock verification.

### Step 2A — Path Normalization Sweep
- Re-scan `仿生文献库/` for ` 2.pdf`/` 3.pdf` variants of "missing" PDFs
- Estimated recovery: 20-30% of 748 missing paths
- **Action:** Claude Code runs automated scan + fix
- **Estimated effort:** 1 hour

### Step 2B — Critical PDF Acquisition
- Download from DOI/patent databases:
  - Aramesh2021 (10.1016/j.ijbiomac.2021.04.158) — 14 chitosan rows
  - Upadhyay2020 (10.1016/j.carbpol.2020.117000) — 3 chitosan rows
  - Dong2025 — 26 alginate rows
  - CN114887602A patent — 4 PDA rows
  - Vo2023 (10.1007/s10311-023-01563-9) — lobster + chitosan
- **Action:** Yao or Claude Code downloads; Claude Code verifies
- **Estimated effort:** 1-2 hours

### Step 2C — Demote Unverified Rows
- For PDFs that cannot be acquired, demote to `missing_pdf` status
- **Action:** Claude Code applies after Yao approval
- **Estimated effort:** 1 hour

## Phase 3: Scope Splitting (After Phase 2)

**Goal:** Break overbroad prototypes into focused, rankable units.

### Candidates for Splitting
| prototype | issue | proposed split |
|---|---|---|
| lotus-leaf | 355 mechanisms, mixed domains | lotus-specific vs shared wetting/separation |
| cellulose-nanocrystal | 108+ rows, mixed materials | CNC vs CNF vs general cellulose vs composite |
| metal-organic-framework | 252 rows, wrong-source contamination | MOF-only vs composite/reference |
| starch-granule | 121 rows, extreme/engineered values | starch-granule vs engineered-hydrogel vs oil-sorbent |
| cell-membrane-ion-channel | membrane separation vs adsorption | split or reclassify |

**Action:** Claude Code/Qoder proposes split plans; Yao approves
**Estimated effort:** 2-4 hours per prototype

## Phase 4: Verification Upgrade (After Phase 3)

**Goal:** Add quote+locator verification to surviving rows.

### Priority Order
1. Prototypes with strong evidence: mussel-foot-adhesion, polydopamine-coating, chitosan (after PDF recovery)
2. Prototypes with moderate evidence: diatom-frustule, silk-fibroin, plant-tannin, oyster-shell
3. Material references: MOF, starch, alginate (after scope splitting)
4. Knowledge-gap prototypes: coral, magnetic-bacteria, namib-beetle (park or retire)

**Action:** Claude Code reads PDFs, extracts quotes, adds locators
**Estimated effort:** 2-4 hours per prototype

## Phase 5: Build & Rank (After Phase 4)

**Goal:** Run `tools/build_prototypes_db.py` and generate ranked adsorption performance tables.

### Prerequisites
- All wrong_source rows removed
- All scope decisions made
- Critical PDFs acquired or rows demoted
- Quote+locator verification complete for top prototypes

**Action:** Yao authorizes build → Claude Code runs build script
**Estimated effort:** 1 hour

## Recommended Next Action

**For Yao right now:**
1. Review `review-clcode-task1-decision-queue-summary.md` — approve Category A (wrong_source, 23 items) and Category D (metadata fixes, 25 items)
2. Review Category C scope decisions — especially PDA/mussel ownership and prototype retirement

**For Claude Code/Qoder after Yao approval:**
1. Apply wrong_source removals
2. Apply metadata fixes
3. Run path normalization sweep for missing PDFs
4. Start verification upgrade for clean prototypes

## Session Handoff Notes

| item | state |
|---|---|
| Branch | `review`, up to date with `origin/review` |
| Uncommitted | `phase5-chains.md`, `verify_adrmats_delivery.py`, `tools/litextract` (pre-existing) + 4 new files (this session) |
| CLAUDE.md | Created for office Windows environment |
| Submodule | `tools/litextract` initialized at 203b0cf |
| Memory files | `office-environment-setup.md`, `project-workflow.md` created |
| Decision queue | 126 items pending Yao (summarized in task1) |
| Boundary register | 105 items pending Yao (summarized in task2) |
| Missing PDFs | 748 paths not found, 18 prototypes affected (analyzed in task3) |
