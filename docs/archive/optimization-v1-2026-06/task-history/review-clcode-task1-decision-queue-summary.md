# Task 1 — Decision Queue Summary for Yao Approval

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Overview

The full evidence audit decision queue contains **163 items** across 15 batches (F01–F15).

| status | count | meaning |
|--------|-------|---------|
| pending_yao | 126 | Awaiting Yao decision |
| applied_package_a1–a9 | 14 | Low-risk mechanical cleanup already applied |
| partially_applied_package_* | 7 | Partial cleanup applied, remaining needs approval |
| accepted_codex | 2 | Accepted as-is by Codex |
| resolved_codex | 1 | Resolved by Codex local audit |

**126 items remain pending_yao.** This document categorizes them for efficient batch approval.

## Category A: wrong_source — Source-Domain Mismatch (Recommended: Remove/Reassign)

These rows cite literature from a completely different domain. **23 items.** Recommend removing or reassigning after approval.

| id | prototype | finding summary |
|---|---|---|
| F01-PDA-002 | polydopamine-coating | Enrichment hydrophobic/superhydrophobic/antibacterial mechanisms from membrane reviews, not PDA adsorption |
| F01-PLT-001 | plant-tannin | Li2022 fluoropolymer membrane review contaminates 6 mechanisms + 1 constraint + 1 narrative |
| F02-BONE-001 | bone-structure | Chen2021 MOF dye/Cr(VI) review rows in bone/HAp |
| F02-FISH-001 | fish-scale-hydroxyapatite | Large superwetting/membrane/Janus block (mechanisms[0-53,56-86], constraints[0-10]) |
| F02-FISH-007 | fish-scale-hydroxyapatite | Wang2021 abalone HA + Zhang2024 shell-powder + MICP rows |
| F03-CHL-001 | chlorella-cell-wall | Mechanisms[0] title=dye removal but source=Pb2+ microalgae |
| F03-CHL-003 | chlorella-cell-wall | CaO, nZVI, magnetic graphene, silica nanoparticle rows |
| F03-MYC-001 | mycelium | Cellulose, nanocellulose, lignin, PFAS, oil rows |
| F03-SRB-003 | sulfate-reducing-bacteria | Iron-cycle microbial remediation constraints |
| F04-LOTUS-003 | lotus-leaf | Non-lotus examples (shark, gecko, rose-petal, membrane, MOF, sponge) |
| F05-MOF-002 | metal-organic-framework | Aramesh2021 chitosan dye-removal rows [23-30,33-36] |
| F05-MOF-003 | metal-organic-framework | Cheng2024 membrane/catalytic BPA rows [77-80] |
| F07-MOF-002 | metal-organic-framework | Pure Aramesh chitosan rows (12 rows, Codex confirmed) |
| F07-MOF-004 | metal-organic-framework | Cheng2024 activated-carbon/NF/MF/UF-AOP BPA rows |
| F07-MOF-006 | metal-organic-framework | Yan2022 PDA/MGO/CA-CD polydopamine composite rows |
| F09-DIAT-004 | diatom-frustule | Mechanisms[0] Pb2+ XPS cites wrong Guo2022 tetracycline DOI |
| F09-DIAT-005 | diatom-frustule | Mechanisms[1,3] use microalgae cell-wall template text for diatomite |
| F11-FISH-005 | fish-scale-hydroxyapatite | Wang2021 abalone + Zhang2024 shell-powder rows |
| F11-FISH-006 | fish-scale-hydroxyapatite | Superwetting/membrane/Janus mechanism ranges [0-53,56-86] |

**Recommended action:** Batch-approve removal or reassignment. No value judgments needed — these are clear domain mismatches.

## Category B: missing_pdf — Source PDF Not Found (Recommended: Acquire or Demote)

**9 items.** Local PDF is missing; claims cannot be verified.

| id | prototype | finding summary |
|---|---|---|
| F01-CHI-001 | chitosan | 99/117 performance items unverified; Aramesh2021 affects 14 items |
| F01-CHI-004 | chitosan | Patent source_file paths mismatched to actual local filenames |
| F01-PDA-001 | polydopamine-coating | CN114887602A PDF missing; 4 phosphorus claims depend on it |
| F01-SILK-005 | silk-fibroin | Chinese article DOI 10.16375/j.cnki.cn45-1395 has no local PDF |
| F04-LOTUS-002 | lotus-leaf | Several lotus performance PDFs missing or path-mismatched |
| F05-ALG-001 | alginate | Dong2025 alginate review PDF missing; drives 26+ rows |
| F15-B09-001 | lobster-exoskeleton | 2023-Vo extraction JSON exists but source PDF missing |

**Recommended action:** Acquire missing PDFs where possible, or demote affected rows to knowledge_gap.

## Category C: needs_human_decision — Requires Yao Judgment (Recommended: Review Individually)

**~30 items.** These involve scope decisions, suspicious values, scanned patents, or prototype boundary questions.

### High-impact scope decisions
| id | prototype | question |
|---|---|---|
| F03-CMIC-001 | cell-membrane-ion-channel | Keep as separation/filtration or split from adsorption? |
| F05-MANG-001 | mangrove-root | System-level wetland evidence — keep with metric caveat? |
| F12-PDA-MU-001 | mussel-foot-adhesion | 32 duplicate rows: who owns PDA/mussel overlap? |
| F02-FISH-002 | fish-scale-hydroxyapatite | Dou2021 biochar: expand prototype scope or split? |
| F08-DNA-005 | dna-aptamer | CN121588773A figure-derived ~35 mg/g: accept or reject? |

### Suspicious/OCR values
| id | prototype | question |
|---|---|---|
| F01-PLT-005 | plant-tannin | Yuan2024 Congo Red 3429.23 mg/g — physically unusual |
| F01-PDA-003 | polydopamine-coating | CN113244898A + CN114570339A scanned patents need OCR |
| F13-PDA-OCR-002 | polydopamine-coating | CN114570339A H-PDA-SO pH6 figure mismatch (~10 vs ~38 mg/g) |
| F13-PDA-OCR-003 | polydopamine-coating | CN113244898A Pb removal 95.68% vs 96.31% discrepancy |
| F10-STARCH-006 | starch-granule | Pb2+ 2000 mg/g extreme value needs primary source check |
| F10-STARCH-005 | starch-granule | Chloroform 7780 mg/g — material-class boundary decision |

### Prototype retirement candidates
| id | prototype | question |
|---|---|---|
| F14-B08-003 | coral-skeleton, magnetic-bacteria | Zero performance rows — keep, park, or retire? |
| F07-REG-001 | namib-beetle | Zero performance, scope overlap — keep parked or retire? |

**Recommended action:** Review individually or batch by sub-category.

## Category D: partial — Needs Fix But Keep (Recommended: Approve Metadata Fixes)

**~25 items.** Evidence is real but metadata needs correction (path, quote, locator, precision).

| id | prototype | fix needed |
|---|---|---|
| F01-SILK-002 | silk-fibroin | False precision 86.24%→86%, 96.29%→96% |
| F01-SILK-003 | silk-fibroin | verification_quote is paper title, not text excerpt |
| F01-SILK-004 | silk-fibroin | Carboxyl group not in quoted source |
| F02-BMT-001 | biomineralization-template | Provenance says n_verified=0 but Wang2025 is real |
| F02-BMT-003 | biomineralization-template | Causal chain broader than evidence |
| F02-BONE-004 | bone-structure | HAp mechanism partially inferred |
| F02-OYS-002 | oyster-shell | Mechanism quote is title-like |
| F02-OYS-003 | oyster-shell | Abalone HA vs oyster species ambiguity |
| F02-FISH-006 | fish-scale-hydroxyapatite | Mechanism[54] DOI/source label mismatch |
| F03-IOB-003 | iron-oxidizing-bacteria | Mixed supported/keep_soft rows need locators |
| F05-MOF-001 | metal-organic-framework | single_source ≠ full verification semantics |
| F10-STARCH-001–003 | starch-granule | Concentration-derived ranges, review maxima, unit mismatches |

**Recommended action:** Batch-approve metadata corrections (path normalization, quote insertion, precision narrowing).

## Category E: supported / keep_soft — Ready to Use (No Action Needed)

**~12 items.** Already applied or accepted. No further Yao decision required.

Includes: applied_package_a1 (7), accepted_codex (2), resolved_codex (1), and some applied_package_a8/a9 items.

## Category F: inferred_only / knowledge_gap — Placeholders

**~10 items.** Empty enrichment mirrors, placeholder boundary conditions, empty causal chains.

**Recommended action:** Keep as-is until source-backed evidence is built. No removal needed.

## Priority Recommendation for Yao

1. **Batch-approve Category A (wrong_source)** — 23 items, no judgment needed, pure domain mismatch
2. **Batch-approve Category D (partial metadata fixes)** — 25 items, mechanical corrections
3. **Review Category B (missing_pdf)** — decide acquire vs demote per prototype
4. **Review Category C individually** — especially PDA/mussel ownership and prototype retirement candidates

## Statistics by Prototype (pending_yao only)

| prototype | pending count | top issue |
|---|---|---|
| fish-scale-hydroxyapatite | 12 | wrong_source superwetting block |
| metal-organic-framework | 9 | wrong_source chitosan/membrane rows |
| starch-granule | 9 | extreme values, unit mismatches |
| polydopamine-coating | 7 | scanned patents, wrong_source enrichment |
| diatom-frustule | 7 | path/dedup, wrong_source mechanisms |
| dna-aptamer | 6 | biosensor scope, missing performance |
| wood-xylem | 5 | source mismatch, biochar scope |
| plant-tannin | 4 | fluoropolymer contamination |
| silk-fibroin | 4 | precision, missing PDF |
| chitosan | 3 | 99/117 missing PDFs |
| oyster-shell | 3 | species ambiguity |
| bone-structure | 3 | MOF contamination |
| chlorella-cell-wall | 3 | wrong_source rows |
| scallop-shell | 2 | scope mismatch |
| iron-oxidizing-bacteria | 2 | scanned patent |
| sulfate-reducing-bacteria | 2 | wrong_source constraints |
| mycelium | 1 | wrong_source biomass rows |
| cell-membrane-ion-channel | 2 | scope decision |
| lotus-leaf | 2 | overaggregated scope |
| superhydrophobic-artificial | 1 | WCA classification |
| mangrove-root | 1 | system-level evidence |
| lobster-exoskeleton | 1 | missing PDF |
| coral-skeleton | 1 | zero performance |
| magnetic-bacteria | 1 | zero performance |
| namib-beetle | 1 | parked, no evidence |
| pitcher-plant | 1 | anti-icing scope |
| spider-silk | 1 | broad mechanism scope |
| mussel-foot-adhesion | 1 | 32-row duplicate ownership |
| enrichment mirrors | 5 | empty/placeholder schemas |
