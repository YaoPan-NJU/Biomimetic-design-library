# Audit: polydopamine-coating.json

**File**: `prototypes_db/polydopamine-coating.json` (2162 lines)
**Date**: 2026-06-19

## Counts

| Category | Count |
|----------|-------|
| mechanisms | 65 |
| performance_data | 44 |
| design_translation | 1 |
| narrative entries | 10 |
| engineering_constraints | 21 |
| mechanism_instances | 19 |
| **Total fields audited** | **160** |

**Verification coverage**:
- mechanisms: 1 verified, 64 needs_review, 0 unverified
- performance_data: 44 verified/partial, 0 needs_review, 0 unverified
- provenance_summary claims: n_verified=44, n_unverified=66 (does not sum to mechanism+perf total of 109; unclear what n_unverified=66 counts)

---

## Findings

### [F1] Superhydrophobic membrane review (acsami.0c18794) — 12 mechanisms, 0 perf
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[0-11]
- **Evidence**: 12 mechanisms reference `ref_doi: "10.1021/acsami.0c18794"` — a superhydrophobic/superoleophilic oil-water separation membrane review (Chen et al., ACS AMI 2021). Topics include lotus effect, gecko adhesion, rose petal effect, TiO2 photocatalysis, CeO2 nanoparticles, PDMS-bP4VP electrospun membranes, UV+pH switchable wettability.
- **Cross-ref**: Refuted DOI #4 on the provided list. This review belongs to the superhydrophobic-artificial or lotus-leaf prototype scope, not PDA coating.
- **Recommended disposition**: Remove all 12 mechanisms. None reference PDA or mussel-inspired chemistry. Corresponding mechanism_instances [5-6] (lines 2053, 2060) should also be removed.

### [F2] Superhydrophobic antibacterial review (jxhg.20201035) — 16 mechanisms, 8 instances
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[12-28], mechanism_instances[11-18]
- **Evidence**: 16 mechanisms reference `ref_doi: "10.13550/j.jxhg.20201035"` — a review of superhydrophobic antibacterial surfaces (Gao et al., J. Soc. Coat. Technol. 2020). Topics include Cu2O nanoparticles, Cu nanoparticles, CuO/SiO2 coatings, nano-Ag cotton fabrics, ZIF-8/PVDF coatings, fluorinated quaternary ammonium salts, medical gauze. Only mechanism [26] mentions dopamine as an adhesion strategy ("多巴胺黏附固定无机抗菌剂策略"), which is tangentially relevant.
- **Cross-ref**: This DOI is not on the refuted list but is a scope contamination candidate — superhydrophobic antibacterial surface reviews do not describe PDA coating adsorption mechanisms.
- **Recommended disposition**: Remove 15 of 16 mechanisms. Keep mechanism [26] ("多巴胺黏附固定无机抗菌剂策略") if its content genuinely describes PDA-mediated adhesion for antimicrobial applications. Remove all 8 corresponding mechanism_instances [11-18].

### [F3] PVDF fluoropolymer membrane distillation review (polym14245439) — 6 mechanisms, 5 instances, 1 constraint
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[29-34], mechanism_instances[0-4], engineering_constraints[0]
- **Evidence**: 6 mechanisms + 5 mechanism_instances reference `ref_doi: "10.3390/polym14245439"` — a PVDF fluoropolymer membrane review for membrane distillation (Li et al., Polymers 2023). Topics include Teflon AF 2400, PVDF-co-HFP/POTS, PVDF-co-HFP/F-POSS, Cassie-Baxter equation, P(VDF-co-CTFE) FOMA. Engineering constraint [0] ("P(VDF-co-HFP) VMD稳定性") from the same DOI.
- **Cross-ref**: Refuted DOI #7 on the provided list. This review belongs to the superhydrophobic-artificial prototype scope.
- **Recommended disposition**: Remove all 6 mechanisms, 5 mechanism_instances, and 1 engineering constraint. None reference PDA.

### [F4] Superwetting membrane separation review (cnki.issn.1001-3660) — 10 mechanisms, 4 instances
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[38-47], mechanism_instances[7-10]
- **Evidence**: 10 mechanisms + 4 mechanism_instances reference `ref_doi: "10.16490/j.cnki.issn.1001-3660.2023.02.015"` — a superwetting membrane separation review (Jing et al., Surface Technology 2023). Topics include lotus effect, W/O emulsion separation, O/W emulsion separation, TiO2 nanowire meshes, PVDF/PDMS nanofiber membranes, Janus membranes, PMMA-b-P4VP fibers, PNIPAAm thermoresponsive nylon.
- **Cross-ref**: Refuted DOI #6 on the provided list. This review belongs to the superhydrophobic-artificial prototype scope.
- **Recommended disposition**: Remove all 10 mechanisms and 4 mechanism_instances. None reference PDA.

### [F5] PDA/MGO/CA-CD dye adsorption (apsusc.2022.154338) — 2 mechanisms, 2 perf, 2 constraints
- **Type**: wrong-source / scope question
- **Severity**: medium
- **Location**: mechanisms[59-60], performance_data[37-38], engineering_constraints[15-16]
- **Evidence**: This DOI is on the refuted list. However, the content (Yan et al., Appl. Surf. Sci. 2022) is about PDA/magnetic graphene oxide/cyclodextrin composites for cationic dye removal — a PDA-based material. The 2 mechanisms describe pH effects and a six-fold adsorption synergy (electrostatic, hydrogen bonding, Yoshida H-bonding, pi-pi conjugation, n-pi, beta-CD host-guest). Performance rows show MB 1372.32 mg/g, MG 822.39 mg/g, CV 570.79 mg/g.
- **Cross-ref**: Refuted DOI #12 on the provided list. The material IS PDA-based, so this may be a borderline scope case rather than pure wrong-source.
- **Recommended disposition**: If the DOI was refuted because the paper's content does not support the extracted claims, remove all 6 entries. If the DOI was refuted for a different reason (e.g., source quality), consider keeping with a caveat. Needs Yao decision.

### [F6] Narrative entries reference superhydrophobic membrane reviews
- **Type**: translation-scope
- **Severity**: high
- **Location**: narrative.entries[0-2]
- **Evidence**: Three narrative entries reference non-PDA, non-adsorption review papers:
  - [0] `gao2021_superhydrophobic_antibacterial_review` — superhydrophobic antibacterial surface review
  - [1] `2022-Li-hydrophobic-separation-membrane-porous-review` — hydrophobic membrane porous review
  - [2] `jing2023_superwetting_oil_water_separation_membrane_review` — superwetting oil-water membrane review
  All three describe oil-water separation membrane design, not PDA coating adsorption. They belong to the superhydrophobic-artificial prototype.
- **Cross-ref**: These narrative entries correspond to the refuted DOIs in [F1], [F2], [F3], [F4].
- **Recommended disposition**: Remove narrative entries [0-2]. Keep entries [3-9] which describe PDA-based adsorption materials (patents CN115040496A, CN113244898A, CN114570339A and literature on PDA-chitosan, PDA-cellulose, PDA-MGO composites).

### [F7] Mechanism [22] Cu nanowire/PDMS — null DOI, unverifiable
- **Type**: label-contradiction
- **Severity**: low
- **Location**: mechanisms[22]
- **Evidence**: `ref_doi: null`, `source: "literature"`, `verification: "needs_review"`. The mechanism describes Cu nanowire/PDMS superhydrophobic surface with stretch/twist/sandpaper durability. No DOI means the claim cannot be traced to a specific paper.
- **Cross-ref**: No specific decision-queue item.
- **Recommended disposition**: Either find the source DOI and verify, or remove. Currently an orphan claim.

### [F8] Provenance summary n_unverified=66 is stale
- **Type**: ledger-inaccuracy
- **Severity**: low
- **Location**: provenance_summary (line 2006-2010)
- **Evidence**: `n_unverified: 66` but actual audit shows 0 needs_review + 0 unverified performance_data, and 64 needs_review mechanisms. The 66 figure likely counted mechanisms with needs_review + some other criteria from an earlier state. The current state is: mechanisms all needs_review except [39] which is needs_review (not verified as the JSON structure might imply from its causal_chain), performance_data all verified/partial.
- **Cross-ref**: No specific decision-queue item.
- **Recommended disposition**: Recount and update provenance_summary to reflect current verification states.

### [F9] Mechanism [39] "PDA吸附机制补充" — causal_chain has llm_inferred fields
- **Type**: label-contradiction
- **Severity**: low
- **Location**: mechanisms[39].causal_chain
- **Evidence**: The mechanism has `verification: "needs_review"` (not verified), but has a full causal_chain with `pollutant_feature.basis: "llm_inferred"` and `why_it_works.basis: "llm_inferred"`. The bio_structure and interaction fields are `basis: "from_source"` with Lei2021 locator. This is internally consistent — needs_review with partial source backing and partial LLM inference.
- **Cross-ref**: No specific decision-queue item.
- **Recommended disposition**: No action needed. The labeling is consistent: needs_review with llm_inferred portions clearly marked.

---

## Clean Areas

### performance_data — generally clean
- 44 rows, all with verification "verified" or "partial"
- All performance_data rows have `verification_quote` fields
- Sources are from legitimate patents (CN114887602A, CN115055171A, CN113244898A, CN114570339A) and literature (Foroutan 2021, Shi 2021, Xiao 2021, Zhang 2021, Godiya 2022, Yan 2022, Jin 2023, Xiang 2023, Yuan 2024)
- Exception: performance_data[37-38] from refuted DOI 10.1016/j.apsusc.2022.154338 (see [F5])

### PDA-relevant mechanisms (clean subset)
- mechanisms[22]: Cu nanowire/PDMS (null DOI, orphan claim — see [F7])
- mechanisms[35-37]: PDA/PET membrane mechanisms from 10.1016/j.seppur.2023.123547 (PDA/PET oil-water separation)
- mechanisms[48-51, 57]: Patent-sourced mechanisms (coordination chelation, curcumin/lycopene adsorption, pH effects) — null DOI but patent-backed
- mechanisms[52-56, 58]: Literature mechanisms from Foroutan 2021, Shi 2021, Xiao 2021, Zhang 2021, Godiya 2022 (adsorption mechanisms, XPS analysis, functional group synergy)
- mechanisms[61-64]: Literature mechanisms from Jin 2023, Yuan 2024 (PDA pi-pi, Cr(VI)/Cu(II)/CR adsorption synergy)
- Total: 19 clean mechanisms

### design_translation — clean
- 1 entry describing PDA catechol + amine dual-functional groups for surface modification, referencing the foundational 2007 Mesmos science paper (DOI: 10.1126/science.1145492)
- No cross-domain contamination

### mechanism_instances — fully contaminated
- All 19 instances reference refuted DOIs. None are clean. These should all be removed or rebuilt from the surviving mechanisms.

### engineering_constraints — mostly clean
- 18 of 21 constraints from legitimate PDA patent/literature sources (8 from patents with null DOI, 10 from literature with clean DOIs)
- 3 constraints from refuted DOIs: [0] from polym14245439, [15-16] from apsusc.2022.154338 (see [F3], [F5])

---

## Summary of Refuted DOI Impact

| Refuted DOI | Fields affected | Total entries |
|-------------|----------------|---------------|
| 10.1021/acsami.0c18794 | mechanisms[0-11], instances[5-6] | 14 |
| 10.13550/j.jxhg.20201035 (scope) | mechanisms[12-28], instances[11-18] | 24 |
| 10.3390/polym14245439 | mechanisms[29-34], instances[0-4], EC[0] | 12 |
| 10.16490/j.cnki.issn.1001-3660.2023.02.015 | mechanisms[38-47], instances[7-10] | 14 |
| 10.1016/j.apsusc.2022.154338 | mechanisms[59-60], perf[37-38], EC[15-16] | 6 |
| **Total** | | **70 entries** |

**Net impact**: 70 out of 160 audited entries (44%) are affected by refuted DOIs or scope contamination. If all are removed, the prototype would retain 87 entries (19 mechanisms with clean DOIs, 42 performance_data, 1 design_translation, 7 narrative entries, 18 engineering constraints, 0 mechanism_instances — all 19 instances reference refuted DOIs and would be removed).

---

## Disposition Requested

The following need Yao decision:
1. **[F5]** Yan2022 (apsusc.2022.154338): Remove or keep with caveat? Material IS PDA-based.
2. **[F2]** mechanism [26] "多巴胺黏附固定无机抗菌剂策略": Keep (PDA-relevant) or remove (from refuted/scope-contaminated review)?
3. **[F8]** provenance_summary: Update n_unverified to match current state?
