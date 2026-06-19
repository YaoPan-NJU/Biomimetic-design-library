---
title: G2 Review Package — P1 Audit Results
status: ready_for_review
date: 2026-06-19
author: claude-code (coordinator)
baseline_commit: 8578ff3
---

# G2 Review Package

## 1. Audit Overview

24 prototypes audited across 3 lanes. All findings are **candidates only** — no canon
changes applied.

| Lane | Prototypes | Findings | High | Medium | Low |
|------|-----------|----------|------|--------|-----|
| A | chitosan, PDA, mussel, fish-scale, bone, oyster, scallop, wood-xylem | 37 | 19 | 6 | 12 |
| B | diatom, biomineralization, coral, dna-aptamer, IOB, SRB, mycelium, mangrove | 10 | 5 | 3 | 2 |
| C | plant-tannin, silk, spider, chlorella, CMIC, lotus, shark, superhydrophobic | 17 | 9 | 7 | 1 |
| **Total** | **24** | **64** | **33** | **16** | **15** |

## 2. Findings by Type (Cross-Lane)

| Finding Type | Count | Priority |
|-------------|-------|----------|
| wrong-source | 45 | HIGH — scope contamination, refuted DOIs |
| label-contradiction | 12 | HIGH — source/verification_tier mismatch |
| ledger-inaccuracy | 24 | MEDIUM — provenance, quote quality |
| translation-scope | 6 | MEDIUM — cross-domain design_translation |
| data-quality | 1 | LOW — duplicates, formatting |

## 3. Top Findings by Prototype

### Critical (wrong-source contamination > 20 entries)

| Prototype | Issue | Entries Affected | Action Needed |
|-----------|-------|-----------------|---------------|
| fish-scale-hydroxyapatite | 7+ superhydrophobic/membrane review DOIs in mechanisms | ~87 mechanisms, 11 ec, 7 perf | Remove refuted entries |
| chitosan | Aramesh2021 dye review + 2 membrane reviews | ~24 mechanisms, 14 perf | Remove or scope-caveat |
| polydopamine-coating | 4 refuted reviews in mechanisms | ~53 mechanisms | Remove |
| mussel-foot-adhesion | Superhydrophobic review contamination | ~28 mechanisms, 4 ec | Remove |
| lotus-leaf | Remaining wrong-source after scope split | ~5 mechanisms | Remove |

### Moderate (wrong-source < 20 entries)

| Prototype | Issue | Action Needed |
|-----------|-------|---------------|
| diatom-frustule | R1-D introduced 2 mech duplicates + 13 perf duplicates | **Fix corruption first** |
| plant-tannin | Fluoropolymer membrane review in mechanisms | Remove 6 mechanisms |
| spider-silk | Superhydrophobic/femtosecond-laser spillover | Remove ~10 mechanisms |
| oyster-shell | Generic shell review data | Scope-caveat |
| scallop-shell | Zhang2024 generic shell review | Scope-caveat |

### Clean (0 findings)

| Prototype | Status |
|-----------|--------|
| wood-xylem | Clean |
| dna-aptamer | Clean |
| biomineralization-template | Clean |
| cell-membrane-ion-channel | Clean |

## 4. Label Contradictions (12 found)

The most common pattern: `source: "llm_inference"` with `verification: "verified"` or
`verification: "partial"`. These must be reconciled — either the source is wrong or
the verification level is wrong.

Affected prototypes: chitosan, polydopamine-coating, mussel-foot-adhesion,
fish-scale-hydroxyapatite, diatom-frustule, mycelium, iron-oxidizing-bacteria,
mangrove-root, plant-tannin, chlorella-cell-wall

## 5. Corrected Brief Preview (3 representative pollutants)

### BPA (Bisphenol A)

**Current state**: chitosan has 14 BPA perf rows from Aramesh2021 dye review (wrong source).

**Corrected brief**:
- Candidates: chitosan (scope-caveated), polydopamine-coating (PDA-coordinated chelation)
- Mechanisms: chitosan amino/hydroxyl chelation (from_source, verified)
- Performance leads: all marked `needs_review` with metric_type
- Honesty ledger: 1 fact (mechanism), 0 leads (no verified perf), 2 inferences (design translation)
- No wrong-source content

### Pb(II)

**Current state**: Multiple prototypes have Pb perf data, some from wrong sources.

**Corrected brief**:
- Candidates: bone-structure (HAp precipitation), oyster-shell (Ca-Al-LDH), fish-scale-HAp
- Remove: all fish-scale perf from refuted membrane/shell reviews
- Mechanisms: HAp Pb²⁺ exchange (from_source, partial)
- Performance leads: bone-structure Bambaeero2020 Cu(II) data (scope-caveated)
- Honesty ledger: facts from direct sources only

### Congo Red (dye)

**Current state**: scallop-shell has Wang2024 data but also generic shell review data.

**Corrected brief**:
- Candidates: scallop-shell (Wang2024 direct), chitosan (multiple sources)
- Remove: scallop perf from Zhang2024 generic shell review
- Mechanisms: electrostatic adsorption + hydrogen bonding (from_source)
- Performance leads: Wang2024 qmax 495.56 mg/g (single_source)
- Cautions: scope caveat for generic shell review data

## 6. Proposed Disposition Counts (ledger-v2 shape, NOT applied)

| Disposition | Count | Description |
|------------|-------|-------------|
| removed | ~180 | wrong-source entries to be removed |
| scope_caveat | ~30 | keep with scope caveat |
| corrective_downgrade | ~12 | verification level correction |
| needs_review | ~20 | label contradictions to reconcile |
| unchanged | ~4000 | entries that pass audit |

## 7. Critical Issue: R1-D Data Corruption

The R1-D commit (`382bb91`) introduced unintended duplicates in `diatom-frustule.json`:
- 2 mechanism name duplicates (15 mechanisms instead of 13)
- 13 performance row duplicates (42 instead of 29)

**This must be corrected before G1 can pass.** The correct action is to revert
diatom-frustule.json to the R1-C state and re-apply only the 9 verification
downgrades.

## 8. Files Produced

| File | Description |
|------|-------------|
| `audit-candidates-v3/lane-a-summary.md` | Lane A findings summary |
| `audit-candidates-v3/lane-b-summary.md` | Lane B findings summary |
| `audit-candidates-v3/lane-c-summary.md` | Lane C findings summary |
| `audit-candidates-v3/<prototype>.md` | 24 individual prototype audits |
| `g1-signoff-evidence.md` | G1 evidence package (includes R1-D corruption finding) |
| `g2-review-package.md` | This file |

## 9. Next Steps (require G1 resolution first)

1. Fix R1-D diatom-frustule.json corruption (revert + re-apply verification only)
2. G1 independent review + sign-off
3. P1a scope/wrong-source removal (180 entries)
4. P1b label contradiction reconciliation (12 entries)
5. P1c honesty_ledger correction
6. P1d design_translation scope cleanup
