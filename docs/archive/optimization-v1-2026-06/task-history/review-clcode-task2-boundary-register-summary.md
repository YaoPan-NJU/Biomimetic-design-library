# Task 2 — Boundary Register Summary for Yao Approval

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Overview

The boundary register contains **105 items**, all `pending_yao`.

| boundary_type | count | meaning |
|---|---|---|
| soft_boundary | 43 | Literature-supported condition limits; do not block alone |
| knowledge_gap | 40 | Missing/inferred boundaries; must not be treated as hard rules |
| hard_do_not | 22 | Direct literature support for exclusion; must include locator/quote |

## hard_do_not — 22 Items (Recommended: Batch Approve)

These are clear source-domain mismatches with direct literature evidence. Approving them adds exclusion rules to the database.

### wrong_source domain mismatches (14 items)
| id | prototype | what must not be used |
|---|---|---|
| B01-PDA-003 | polydopamine-coating | Hydrophobic membrane/antibacterial mechanisms as PDA evidence |
| B01-PLT-001 | plant-tannin | Li2022 fluoropolymer membrane review as plant-tannin evidence |
| B02-BONE-002 | bone-structure | Chen2021 MOF dye/Cr(VI) review as bone/HAp evidence |
| B02-FISH-001 | fish-scale-hydroxyapatite | Superwetting/membrane mechanisms as fish-scale HAp evidence |
| B02-FISH-005 | fish-scale-hydroxyapatite | Marine-shell/abalone HA as fish-scale HAp evidence |
| B03-CHL-001 | chlorella-cell-wall | Cheng2021 Pb2+ as synthetic dye-removal mechanism |
| B03-CHL-002 | chlorella-cell-wall | CaO, nZVI, magnetic graphene, silica rows as Chlorella evidence |
| B03-MYC-001 | mycelium | Cellulose, nanocellulose, lignin, PFAS, oil rows as mycelium evidence |
| B03-SRB-002 | sulfate-reducing-bacteria | Iron-cycle constraints as SRB-specific constraints |
| B04-LOTUS-003 | lotus-leaf | Non-lotus examples as lotus-leaf-specific evidence |
| B05-MOF-002 | metal-organic-framework | Aramesh2021 chitosan rows as MOF evidence |
| B05-MOF-003 | metal-organic-framework | Cheng2024 membrane/BPA rows as MOF evidence |
| B07-MOF-002 | metal-organic-framework | Pure Aramesh chitosan rows (Codex confirmed) |
| B07-MOF-003 | metal-organic-framework | Cheng2024 activated-carbon/membrane BPA rows |
| B07-MOF-005 | metal-organic-framework | Yan2022 PDA/MGO/CA-CD rows as MOF evidence |
| B08-DNA-001 | dna-aptamer | Biosensor LOD/Kd as adsorption capacity evidence |
| B09-DIAT-003 | diatom-frustule | Guo2022 tetracycline as Pb2+ XPS mechanism |
| B09-DIAT-004 | diatom-frustule | Microalgae cell-wall text as diatomite surface chemistry |
| B11-FISH-002 | fish-scale-hydroxyapatite | CN113275374A MICP as fish-scale HAp evidence |

### Scope/value exclusions (3 items)
| id | prototype | what must not be done |
|---|---|---|
| B02-OYS-003 | oyster-shell | Report abalone HA qmax as oyster-shell qmax |
| B10-STARCH-001 | starch-granule | Treat concentration-dependent ranges as Langmuir qmax |
| B10-STARCH-002 | starch-granule | Use Khoo2023 review-wide maxima as starch-specific performance |

**Recommended action:** Batch approve all 22 hard_do_not items. Each has direct literature evidence.

## soft_boundary — 43 Items (Recommended: Batch Approve)

These are condition-specific limits supported by literature. They add caveats but don't block prototypes.

### By category
| category | count | examples |
|---|---|---|
| pH/condition limits | 12 | chitosan pH 4-6, plant-tannin pH 6, biomineralization pH 4, bone pH 4-6, oyster pH 4-10 |
| Scope/domain caveats | 15 | wood-xylem biochar scope, mangrove system-level, MOF H2 storage, membrane separation |
| Preparation-specific | 6 | silk Na2CO3 degumming, scallop 900°C calcination, starch superhydrophobic cryogel |
| Duplicate/ranking exclusion | 5 | PDA/mussel 32-row duplicate, diatom duplicate rows, starch oil/chloroform |
| Regeneration limits | 5 | plant-tannin 2 cycles, wood-xylem 5 cycles, silk beta-sheet disruption |

**Recommended action:** Batch approve. All have literature quotes.

## knowledge_gap — 40 Items (Recommended: Acknowledge, No Action)

These mark missing or inferred boundaries that should not be treated as hard rules.

### By category
| category | count | meaning |
|---|---|---|
| Inferred/placeholder boundaries | 15 | LLM-inferred limits with no PDF quote |
| Missing PDF | 8 | Source PDF not found; boundary cannot be verified |
| Scanned/OCR pending | 5 | Patent text not extractable; needs visual verification |
| Empty enrichment mirrors | 5 | Enrichment causal_chain fields are blank |
| Prototype scope undecided | 4 | coral, magnetic-bacteria, namib-beetle, lobster scope |
| Provenance inflated | 3 | Duplicate-inflated counts; MOF single_source semantics |

**Recommended action:** Acknowledge as knowledge gaps. No database changes until source evidence is built.

## Approval Strategy

| batch | boundary_type | count | action |
|---|---|---|---|
| Batch B-approve-1 | hard_do_not | 22 | Approve → add exclusion rules to DB |
| Batch B-approve-2 | soft_boundary | 43 | Approve → add condition caveats to DB |
| Batch B-acknowledge | knowledge_gap | 40 | Acknowledge → keep as gaps, no DB change |

Total: **105 boundary items** to process.
