# Full Audit Batch 01: wood-xylem

status: codex_reviewed

## Scope

- **Prototype JSON:** `prototypes_db/wood-xylem.json`
- **Enrichment JSON:** `prototypes_db/enrichment/wood-xylem.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local PDF text audit (`pdftotext` + PyMuPDF), used because the OpenClaw worker failed under rate/path errors.
- **Papers in scope:** Kumar2021 wood apple shell biochar; Mo2021 wood-inspired nanocellulose aerogel.
- **PDFs found:** 2/2, but actual filenames have ` 2.pdf` suffixes while DB source_file values omit them.

## Audit Summary

- All 3 `performance_data` values are supported by local PDFs.
- `performance_data[*].pollutant` fields are empty even though pollutants are explicit in the papers.
- `mechanisms[0]` is the main issue: the phenol/chlorophenol pH mechanism is supported by Kumar2021, but the DB points `source_file` and `verification_quote` to Mo2021 wood nanocellulose. This is a source mismatch, not a numerical failure.
- `mechanisms[1-3]` are supported by Mo2021 but need real locators/quotes and causal_chain population.
- Enrichment `wood-xylem.json` mirrors four mechanisms with empty causal_chain fields.
- No `prototypes_db/*.json` changes were made.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_path | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WX-PF-01 | wood-xylem.json | performance_data[0] | performance | Langmuir qmax: phenol 102.71, 4-CPh 172.24, 2,4-DCPh 226.55 mg/g; pH 6.0; 30 +/- 1 deg C | 2021-Kumar-wood-shell-biochar-wastewater.pdf | 10.1038/s41598-021-82277-2 | 仿生文献库/论文/第4组-生物矿化/2021-Kumar-wood-shell-biochar-wastewater 2.pdf | Y | p1 Abstract; p14 Conclusions | "maximum uptake of phenol, 4-CPh, and 2,4-DCPh was 102.71, 172.24, and 226.55 mg/g" | supported | add_quote_locator | Value supported. DB source_file omits ` 2.pdf`; pollutant field is empty and should list phenol, 4-CPh, 2,4-DCPh. |
| WX-PF-02 | wood-xylem.json | performance_data[1] | performance | Chlorinated phenol capacity order: 2,4-DCPh > 4-CPh > phenol | same | same | same | Y | p14 Conclusions | "Q0(max) achieved for phenol, 4-CPh, and 2,4-DCPh was 102.71, 172.24, and 226.55 mg/g" | supported | add_quote_locator | Order and values supported. Pollutant field empty. |
| WX-PF-03 | wood-xylem.json | performance_data[2] | performance | TCTGAs qmax: Pb 571, Cu 462, Zn 361, Cd 263, Mn 208 mg/g | 2021-Mo-cellulose-nanocellulose-wood-adsorption.pdf | 10.1016/j.jhazmat.2021.125612 | 仿生文献库/论文/第3组-多孔结构/2021-Mo-cellulose-nanocellulose-wood-adsorption 2.pdf | Y | p1 Abstract; p7 Conclusions | "Pb(II), Cu(II), Zn(II), Cd(II), and Mn(II) of 571 mg g-1, 462 mg g-1, 361 mg g-1, 263 mg g-1, and 208 mg g-1" | supported | add_quote_locator | Value supported. DB source_file omits ` 2.pdf`; pollutant field is empty and should list five metals. |
| WX-MC-01 | wood-xylem.json | mechanisms[0] | mechanism | Phenol/chlorophenol pH mechanism: molecular phenols at lower pH; phenolate repulsion at high pH | currently points to Mo2021 2nd copy | 10.1038/s41598-021-82277-2 | Kumar2021 PDF exists | Y | Kumar p6 Section Effect of pH | "dominant form is molecular state phenols"; "electrostatic repulsion...between...WAS-BC and phenolate anions" | partial | fix_source_and_quote | Mechanism content is supported by Kumar2021, but source_file/verification_quote in DB point to Mo2021 and quote is not the right evidence. Also causal_chain locators say Mo2021 p1, which is wrong. |
| WX-MC-02 | wood-xylem.json | mechanisms[1] | mechanism | XPS C 1s C-N bond confirms TMPTAP crosslinking | Mo2021 | 10.1016/j.jhazmat.2021.125612 | Mo2021 PDF exists | Y | p4 Section 3.1 | "A new peak corresponding to C-N bond appeared" | supported | add_quote_locator | Supports covalent crosslink network claim. Causal_chain missing. |
| WX-MC-03 | wood-xylem.json | mechanisms[2] | mechanism | Amino coordination/chelation with metal ions via N 1s shift | Mo2021 | same | same | Y | p6 XPS discussion | "N 1s core level was shifted to higher binding energy upon metal loading" | supported | add_quote_locator | Supports N donor coordination; O 1s/Pb coordination also supported but should be quoted separately if retained. |
| WX-MC-04 | wood-xylem.json | mechanisms[3] | mechanism | TCNF/GO/TMPTAP composition and directional freezing to wood-inspired honeycomb microchannels | Mo2021 | same | same | Y | p3-4 Section 3.1 | "wood-inspired honeycomb macropore structure with aligned channels" | supported | add_quote_locator | Material/synthesis supported. DB currently has no causal_chain. |
| WX-EC-01 | wood-xylem.json | engineering_constraints[0] | engineering | WAS-BC thermal stability: 500 deg C only about 10 wt% mass loss | Kumar2021 | 10.1038/s41598-021-82277-2 | Kumar2021 PDF exists | Y | p5 TGA analysis | "If biochar is heated to 500 deg C, only approximately a 10-wt% mass loss is observed" | supported | add_quote_locator | Supports the specific 500 deg C stability claim. DB wording also says biomass 200-750 deg C mainly pyrolyzes; use source quote if retained. |
| WX-EC-02 | wood-xylem.json | engineering_constraints[1] | engineering | Regeneration: 0.05 mol/L EDTA-2Na, 25 deg C, 3 h; five cycles | Mo2021 | 10.1016/j.jhazmat.2021.125612 | Mo2021 PDF exists | Y | p3 Methods; p7 Regeneration | "0.05 mol L-1 EDTA-2Na solution and shaken at 25 C for 3 h" | supported | add_quote_locator | Five-cycle performance supported separately: high regeneration efficiency of 90% over five cycles. |
| WX-EC-03 | wood-xylem.json | engineering_constraints[2] | engineering | Underwater/cyclic mechanical stability and compression filter relevance | Mo2021 | same | same | Y | p5 mechanical; p7 regeneration | "height retention of ~90% after 20 compression cycles" | supported | add_quote_locator | Supports mechanical stability; DB comparison to ordinary freezing aerogels needs exact source wording before keeping. |
| WX-NV-01 | wood-xylem.json | narrative.entries[0] | narrative | Kumar2021 narrative on wood apple shell biochar for phenols | extraction JSON | 10.1038/s41598-021-82277-2 | PDF exists | Y | extraction-derived | N/A | keep_soft | keep_soft | Narrative aligns with extraction and paper, but source is wood apple fruit shell biochar, not anatomical wood xylem. Treat as biomass-shell/biochar adjacent evidence. |
| WX-NV-02 | wood-xylem.json | narrative.entries[1] | narrative | Mo2021 narrative on wood-inspired nanocellulose aerogel | extraction JSON | 10.1016/j.jhazmat.2021.125612 | PDF exists | Y | extraction-derived | N/A | supported | add_quote_locator | This is the strongest wood-xylem structural biomimicry evidence. |
| WX-EN-01 | enrichment/wood-xylem.json | mechanisms[*].causal_chain | mechanism_causal_chain | Four enrichment mechanisms have empty causal_chain fields | enrichment file | N/A | N/A | N/A | N/A | N/A | inferred_only | populate_or_keep_unverified | Same placeholder pattern seen in other enrichment files. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| WX-BD-01 | wood-xylem.json | mechanisms[0] | soft_boundary | Phenol/chlorophenol adsorption is best around pH 6 and below pKa; high pH increases phenolate repulsion. | Do not generalize Kumar phenol qmax to alkaline wastewater without pH evidence. | Kumar2021 PDF | p6 pH discussion | "electrostatic repulsion...between...WAS-BC and phenolate anions" | supported | This is a real operating boundary for phenolic pollutants, not a universal xylem boundary. |
| WX-BD-02 | wood-xylem.json | performance_data[0-1], narrative.entries[0] | knowledge_gap | Kumar2021 uses ball-milled wood apple shell biochar, not preserved xylem anatomy. | It supports biomass/biochar phenol adsorption, but not direct xylem-channel structural biomimicry. | Kumar2021 PDF | p1 Abstract | "wood apple fruit shell waste biochar" | supported | Keep as adjacent biomass evidence or move/narrow under biochar/shell-derived adsorbent. |
| WX-BD-03 | wood-xylem.json | engineering_constraints[1] | soft_boundary | Mo2021 regeneration evidence is five Pb(II) adsorption/desorption cycles. | Long-term or all-metal regeneration is not proven by this field. | Mo2021 PDF | p7 | "90% over five consecutive Pb(II) ions adsorption/desorption cycles" | supported | Good evidence, but scope is Pb(II) and five cycles. |
| WX-BD-04 | enrichment/wood-xylem.json | mechanisms[*].causal_chain | knowledge_gap | Empty causal_chain fields in enrichment. | Enrichment mechanisms should not be used as causal evidence until populated. | N/A | N/A | N/A | inferred_only | Placeholder-only enrichment file. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| Kumar2021 DOI 10.1038/s41598-021-82277-2 | performance_data[0-1], mechanisms[0], engineering_constraints[0], narrative.entries[0] | PDF exists as `...wastewater 2.pdf`; DB source_file omits suffix. Mechanism[0] content belongs to Kumar, but DB source_file/verification_quote currently point to Mo2021. | Fix source_file path and replace mechanism[0] quote/locators with Kumar p6 evidence. |
| Mo2021 DOI 10.1016/j.jhazmat.2021.125612 | performance_data[2], mechanisms[1-3], engineering_constraints[1-2], narrative.entries[1] | PDF exists as `...adsorption 2.pdf` and duplicate 2nd-path PDF. DB source_file omits suffix for performance, while mechanism[0] incorrectly points to Mo. | Normalize path and use Mo only for TCTGA heavy-metal, honeycomb, crosslink, and regeneration claims. |
| performance_data[*].pollutant | performance_data[0-2] | Empty pollutant fields despite explicit pollutants in PDFs. | Fill pollutants after approval: phenol, 4-CPh, 2,4-DCPh; Pb(II), Cu(II), Zn(II), Cd(II), Mn(II). |
| enrichment/wood-xylem.json | mechanisms[*].causal_chain | Four empty causal_chain placeholders. | Populate from Kumar/Mo evidence or keep unverified. |

## Audit Statistics

- performance_data audited: 3/3 supported.
- mechanisms audited: 3 supported, 1 partial/source-mismatch.
- engineering_constraints audited: 3 supported, with scope narrowing needed for regeneration and mechanical comparison wording.
- narrative entries audited: 1 supported, 1 keep_soft due biomass-shell/biochar adjacency.
- critical fixes queued: source/quote mismatch in `mechanisms[0]`, empty pollutant fields, source_file suffix normalization, enrichment causal_chain placeholders.
