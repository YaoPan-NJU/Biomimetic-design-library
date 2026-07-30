# Full Audit Batch 03: microbes-cells preflight

status: codex_preflight_reviewed

## Scope

- **Batch ID:** `full-audit-03-microbes-cells`
- **Prototype JSONs:** `chlorella-cell-wall.json`, `iron-oxidizing-bacteria.json`, `sulfate-reducing-bacteria.json`, `mycelium.json`, `cell-membrane-ion-channel.json`
- **Enrichment JSONs:** corresponding `prototypes_db/enrichment/*.json`
- **Audit date:** 2026-06-16
- **Worker:** Codex local JSON and PDF text audit (`jq`, `rg --files -uuu`, `pdftotext`)
- **Reason for preflight:** this batch spans several large or cross-domain prototypes. The main risk is wrong-source and scope contamination, not lack of literature. No `prototypes_db/*.json` files were modified.

## Prototype Coverage

| prototype_id | performance_data | mechanisms | engineering_constraints | provenance_summary | enrichment_status |
|---|---:|---:|---:|---|---|
| chlorella-cell-wall | 24 | 13 | 3 | 8 papers, 21 verified, 16 unverified | 13 enrichment mechanisms, causal_chain mostly empty |
| iron-oxidizing-bacteria | 23 | 6 | 23 | 7 papers, 11 verified, 18 unverified | 6 enrichment mechanisms, causal_chain empty |
| sulfate-reducing-bacteria | 0 | 1 | 4 | 12 papers, 0 verified, 1 unverified | 1 enrichment mechanism, causal_chain empty |
| mycelium | 6 | 4 | 1 | 2 papers, 6 verified, 4 unverified | 4 enrichment mechanisms, causal_chain empty |
| cell-membrane-ion-channel | 14 | 13 | 5 | 7 papers, 12 verified, 15 unverified | 13 enrichment mechanisms, causal_chain empty |

## Audit Summary

- `chlorella-cell-wall` contains valid algae and Chlorella-adjacent sources, but many fields are generic algae, algal biochar, polymer-immobilized microalgae, or unrelated wastewater technology review rows. `mechanisms[0]` is a clear quote mismatch: the row title describes synthetic dye removal, while the verified quote/source is a Pb2+ microalgae adsorption paper.
- `iron-oxidizing-bacteria` has strong schwertmannite and jarosite evidence from Luo2021 and Jhariya2024, but pollutant fields and source paths need normalization. CN113275374A-derived rows are scanned patent/MICP evidence and should not be treated as iron-oxidizing-bacteria evidence without visual verification and scope approval.
- `sulfate-reducing-bacteria` has a supported SRB sulfide-precipitation mechanism, but `performance_data` is empty despite many local SRB papers and extraction outputs. Current iron-cycle constraints are wrong-source for SRB.
- `mycelium` has one useful fungal biosorption review source, but most Zhang2022 biomass/nanocellulose rows are cellulose, lignin, nanocellulose, or soil bioremediation evidence rather than mycelium adsorption.
- `cell-membrane-ion-channel` is primarily a membrane/separation or desalination prototype, not a direct adsorption prototype. The AQP/AWC/ion-channel mechanism sources are useful, but generic heavy-metal membrane performance rows from Shaeli, Pachaiappan, and Foorginezhad should not be used as cell-membrane-ion-channel adsorption evidence without a scope caveat and local PDF verification.

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHL-MC-01 | chlorella-cell-wall.json | mechanisms[0] | mechanism | Synthetic dye removal mechanism with cationic/anionic dyes | Cheng2021 microalgae Pb PDF | 10.19824/j.cnki.cn32-1786/x.2021.0078 | Y | abstract and results | "Pb2+...5 ~ 10 min" | wrong_source | retitle_or_replace_quote | Source supports freshwater microalgae Pb adsorption, not dye removal. |
| CHL-MC-02 | chlorella-cell-wall.json | mechanisms[11] | mechanism | Two-stage Pb adsorption by microalgae | Cheng2021 microalgae Pb PDF | 10.19824/j.cnki.cn32-1786/x.2021.0078 | Y | results discussion | "5 ~ 10 min...被动吸附过程" | supported | add_quote_locator | Strongest direct Chlorella/Pb mechanism item. |
| CHL-PF-01 | chlorella-cell-wall.json | performance_data[6-7] | performance | Chlorella-derived magnetic biochar removes RhB, qmax 286.4 mg/g | Peng2022 PDF | 10.3390/nano12132271 | Y | abstract and isotherm section | "maximum adsorption capacity of 286.4 mg/g" | supported | keep_soft_or_split | Final adsorbent is nano iron oxide modified biochar, not Chlorella cell wall. |
| CHL-PF-02 | chlorella-cell-wall.json | performance_data[0-5], [8-15], mechanisms[1-10], engineering_constraints[0-2] | performance/mechanism/engineering | Generic algae, immobilized microalgae, and algal biochar review evidence | multiple PDFs | multiple | Y | review sections | generic review support | keep_soft | add_scope_caveat | Useful background, but not Chlorella cell-wall-specific evidence. |
| CHL-PF-03 | chlorella-cell-wall.json | performance_data[16-21] | performance | CaO, Ca-P precipitation, nZVI, magnetic graphene, silica nanoparticle wastewater values | Technology2021 wastewater review | 10.1007/s10311-021-01239-2 | Y | sections on chemical/nanotechnology methods | not Chlorella cell wall | wrong_source | remove_or_reassign | These rows are method-review contamination for this prototype. |
| CHL-PF-04 | chlorella-cell-wall.json | performance_data[22-23], mechanisms[12] | performance/mechanism | Algal biopolymer and PANI-ODOB dye adsorption | Kartik2021 biopolymer review | 10.1016/j.biortech.2021.124868 | Y | abstract and section 4.1 | "PANI-ODOB...786 mg/g" | keep_soft | split_or_caveat | PANI-ODOB uses Oscillatoria biomass and polyaniline, not Chlorella cell wall. |
| IOB-PF-01 | iron-oxidizing-bacteria.json | performance_data[0-6], engineering_constraints[0-12], mechanisms[0] | performance/mechanism/engineering | Schwertmannite As removal, pH and reuse effects | Luo2021 PDF | 10.7524/j.issn.0254-6108.2020070302 | Y | section 2.1.1 and 2.1.2 | "As(V)...95.3% and 63.9%" | supported | fill_pollutants_and_normalize_path | Pollutant fields are empty; JSON source_file omits actual directory path. |
| IOB-PF-02 | iron-oxidizing-bacteria.json | performance_data[7-10], mechanisms[1] | performance/mechanism | CN113275374A mixed bacteria Cd/Pb removal and MICP chemistry | CN113275374A patent | none | scanned | N/A | N/A | needs_human_decision | OCR_or_reassign | Same scanned patent seen in Batch 02; not iron-oxidizing-bacteria-specific. |
| IOB-PF-03 | iron-oxidizing-bacteria.json | performance_data[11-14], mechanisms[5] | performance/mechanism | BKFM bacteria/kaolin/Fe-Mn oxide removes Sb and As | Xu2022 PDF | 10.1016/j.clay.2021.106392 | Y | abstract | qmax values for Sb and As | supported | add_full_source_path_quote | Supported as bacteria/Fe-Mn composite evidence, needs scope caveat and path normalization. |
| IOB-PF-04 | iron-oxidizing-bacteria.json | performance_data[15-22], engineering_constraints[13-19] | performance/engineering | Biogenic jarosite and schwertmannite Se(VI) removal and stability | Jhariya2024 PDF | 10.1016/j.jhazmat.2024.136256 | Y | section 3.3 | Se(VI) removal by J-2.5/S-2.5 | supported | add_quote_locator | Good IOB-adjacent biomineral evidence. |
| IOB-EC-01 | iron-oxidizing-bacteria.json | engineering_constraints[20-22] | engineering | Iron-cycle microbial remediation constraints | Qian2021 iron cycling review | 10.7524/j.issn.0254-6108.2020050901 | Y | review sections | iron cycling, not IOB adsorption | keep_soft | demote_to_background | Useful background, not direct IOB adsorption performance. |
| SRB-MC-01 | sulfate-reducing-bacteria.json | mechanisms[0] | mechanism | SRB reduces sulfate to sulfide and precipitates metals | Kumar2020 PDF | 10.1016/j.jenvman.2020.111555 | Y | abstract and section 2 | "sulfide products are responsible for metal precipitation" | supported | add_locator_and_keep | Mechanism source is strong. |
| SRB-PF-01 | sulfate-reducing-bacteria.json | performance_data | performance | No performance_data rows despite 12-paper provenance and local SRB extraction outputs | multiple SRB PDFs | multiple | Y | N/A | N/A | knowledge_gap | run_targeted_row_build_after_approval | Do not use narrative/extraction values as performance until row-level verification. |
| SRB-EC-01 | sulfate-reducing-bacteria.json | engineering_constraints[1-3] | engineering | Iron-cycle microbial remediation constraints | Qian2021 iron cycling review | 10.7524/j.issn.0254-6108.2020050901 | Y | review sections | iron cycle, not SRB | wrong_source | remove_or_reassign | Same row family appears in IOB and is wrong for SRB. |
| SRB-EC-02 | sulfate-reducing-bacteria.json | engineering_constraints[0] | engineering | Sulfur cycle coupling with C/N/P cycles | PSEP2024 DOI | 10.1016/j.psep.2024.01.103 | N in current path scan | N/A | N/A | missing_pdf | locate_pdf_or_demote | Source was not found in local PDF scan. |
| MYC-PF-01 | mycelium.json | performance_data[0], mechanisms[3], engineering_constraints[0] | performance/mechanism/engineering | Fungal biosorption review supports mycelium cell wall polysaccharides and pH 6 Cd boundary | Liu2021 PDF | 10.19465/j.cnki.2095-9710.2021.04.005 | Y | p.10 and pH section | "80%~90%的多糖" | supported | add_quote_locator_and_fix_scope | Mechanism title says CMC hydrogel but quote supports filamentous fungal cell wall. |
| MYC-PF-02 | mycelium.json | performance_data[1-5], mechanisms[0-2] | performance/mechanism | Spinifex nanocellulose, CNF/PVA dye, TOCNF, lignin, PFAS, nanocellulose foam, Ganoderma soil anthracene | Zhang2022 PDF | 10.1016/j.tibtech.2022.09.011 | Y | review sections | biomass/nanocellulose review | wrong_source | remove_reassign_or_scope_split | Mostly cellulose/nanocellulose/biomass material evidence, not mycelium adsorption. |
| CMIC-MC-01 | cell-membrane-ion-channel.json | mechanisms[0] | mechanism | AQP/biomimetic membrane concept and desalination challenge | Beratto-Ramos2022 PDF | none in JSON row | Y | abstract | "Aquaporin biomimetic membranes" | supported | narrow_to_membrane_separation | Good source, but supports desalination/filtration, not adsorption. |
| CMIC-MC-02 | cell-membrane-ion-channel.json | mechanisms[1-3], engineering_constraints[4] | mechanism/engineering | C14lyso artificial water channel RO membrane | Chen2021 PDF | 10.1016/j.cej.2021.133878 | Y | abstract, stability section | "NaCl rejection of 98.6%" | supported | add_source_file_quote_locator | Source_file fields are blank or missing actual paths. |
| CMIC-MC-03 | cell-membrane-ion-channel.json | mechanisms[4-11] | mechanism | Ion-selective NF mechanisms using biomimetic ion channels, crown ether, graphene, MOF, liquid crystal, GO | Lu2022 PDF | 10.1016/j.advmem.2022.100032 | Y | abstract and mechanism sections | "biomimetic ion channels" | supported | add_source_file_quote_locator | Useful for ion-selective separation, not adsorption capacity. |
| CMIC-PF-01 | cell-membrane-ion-channel.json | performance_data[0-13] | performance | Generic modified membrane, heavy-metal membrane, and AQP/AWC desalination performance rows | Shaeli/Pachaiappan/Foorginezhad reviews | multiple | mixed | review sections | generic membrane review evidence | keep_soft | separate_membrane_performance_from_adsorption | Most rows are membrane retention/permeance or generic adsorbent reviews, not cell membrane ion channel adsorption. |
| CMIC-EC-01 | cell-membrane-ion-channel.json | engineering_constraints[0-3] | engineering | AWC and graphene nanopore membrane stability | Vincenzo2020 and Liu2022 PDFs | 10.1038/s41565-020-00796-x; 10.1002/adfm.202200199 | Y | stability sections | "maintained their selectivity" | supported | add_source_file_quote_locator | Good membrane boundary evidence, not adsorption boundary. |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| CHL-BD-01 | chlorella-cell-wall.json | mechanisms[0] | hard_do_not | Cheng2021 must not be used as evidence for synthetic dye removal mechanisms. | It supports Pb2+ adsorption by freshwater microalgae, not dye removal. | 2021-程-微藻-小球藻-吸附-重金属 2.pdf | abstract | "Pb2+...5 ~ 10 min" | wrong_source | Retitle to Pb adsorption or replace source. |
| CHL-BD-02 | chlorella-cell-wall.json | performance_data[16-21] | hard_do_not | CaO, nZVI, magnetic graphene, and silica nanoparticle wastewater rows must not be reported as Chlorella cell-wall evidence. | Would import unrelated treatment technologies into a cell-wall prototype. | Technology2021 review | method sections | chemical/nanotechnology methods, not Chlorella | wrong_source | Remove/reassign after approval. |
| CHL-BD-03 | chlorella-cell-wall.json | performance_data[6-7] | soft_boundary | Peng2022 supports Chlorella-derived magnetic biochar, not intact cell-wall biosorption. | Keep only as derived-biochar evidence or split to algal biochar. | Peng2022 PDF | abstract | "modified biochar...Chlorella vulgaris" | supported | Scope decision needed. |
| IOB-BD-01 | iron-oxidizing-bacteria.json | performance_data[0-6], engineering_constraints[0-12] | soft_boundary | Luo2021 schwertmannite values are arsenic- and pH-specific. | Do not generalize to all heavy metals or neutral wastewater without extra evidence. | Luo2021 PDF | section 2.1.1 | "pH 3.0...pH 7.0" | supported | Fill pollutants as As(III)/As(V). |
| IOB-BD-02 | iron-oxidizing-bacteria.json | performance_data[7-10], mechanisms[1] | knowledge_gap | CN113275374A is scanned and MICP/mixed-bacteria oriented, not IOB-specific. | Do not use Cd/Pb values until OCR and scope decision. | CN113275374A PDF | N/A | N/A | needs_human_decision | Same patent is unresolved in Batch 02. |
| SRB-BD-01 | sulfate-reducing-bacteria.json | performance_data | knowledge_gap | Prototype has no verified performance rows. | Do not convert narrative/extraction claims into performance without row-level PDF verification. | multiple SRB PDFs | N/A | N/A | knowledge_gap | Strong source pool exists, but table is empty. |
| SRB-BD-02 | sulfate-reducing-bacteria.json | engineering_constraints[1-3] | hard_do_not | Iron-cycle microbial remediation rows must not be used as SRB-specific constraints. | Would mix Fe-cycle and sulfate-reduction mechanisms. | Qian2021 iron cycling review | title/domain check | iron cycling microbial remediation | wrong_source | Remove/reassign after approval. |
| MYC-BD-01 | mycelium.json | performance_data[1-5], mechanisms[0-2] | hard_do_not | Cellulose, nanocellulose, lignin, and PFAS/oil rows must not be used as mycelium adsorption evidence without explicit scope expansion. | Would make mycelium prototype depend on non-mycelium biomass material evidence. | Zhang2022 biomass review | review sections | biomass/nanocellulose examples | wrong_source | Keep only Ganoderma row if scope is soil bioremediation, not adsorption. |
| MYC-BD-02 | mycelium.json | engineering_constraints[0] | soft_boundary | Liu2021 fungal Cd adsorption optimum is pH 6 and drops at too low or too high pH. | Treat as fungal biosorption operating condition, not universal mycelium rule. | Liu2021 PDF | pH section | "pH为6.0时...56.17%" | supported | Add locator after approval. |
| CMIC-BD-01 | cell-membrane-ion-channel.json | entire prototype | soft_boundary | The literature base supports membrane separation/desalination and ion selectivity more than adsorption. | Keep in library only with separation/filtration scope caveat or split from adsorption prototypes. | Beratto-Ramos2022, Chen2021, Lu2022 | abstracts | membrane/desalination/ion-selective NF | supported | Needs Yao scope decision. |
| CMIC-BD-02 | cell-membrane-ion-channel.json | performance_data[0-13] | knowledge_gap | Generic membrane performance rows mix adsorption capacity, rejection, permeance, and desalination values. | Do not compare these values directly with adsorption qmax fields. | mixed review sources | mixed | N/A | partial | Normalize metric type before any ranking use. |
| CMIC-BD-03 | cell-membrane-ion-channel.json | mechanisms[0].causal_chain.boundary_conditions | knowledge_gap | Current high-salt/high-pressure membrane failure boundaries are inferred in JSON. | Do not upgrade to hard boundary until directly sourced. | N/A | N/A | N/A | inferred_only | Supported stability evidence exists, but wording needs source-specific replacement. |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---|---|---|---|
| Cheng2021 DOI 10.19824/j.cnki.cn32-1786/x.2021.0078 | chlorella mechanisms[0], mechanisms[11] | Source supports Pb2+ adsorption, not synthetic dye mechanism. | Retitle/split Pb mechanism or replace dye source after approval. |
| Technology2021 DOI 10.1007/s10311-021-01239-2 | chlorella performance_data[16-21] | Generic wastewater technology rows, not Chlorella. | Remove/reassign after approval. |
| Luo2021 DOI 10.7524/j.issn.0254-6108.2020070302 | IOB performance_data[0-6], constraints[0-12] | Strong evidence but missing pollutant and local source path. | Fill As species and normalize path after approval. |
| CN113275374A | IOB performance_data[7-10]; SRB/fish-scale related unresolved rows | Scanned patent and non-IOB-specific MICP evidence. | OCR/visual verify and decide reassignment. |
| Kumar2020 DOI 10.1016/j.jenvman.2020.111555 | SRB mechanisms[0] | Strong mechanism evidence, but no performance_data rows exist. | Keep mechanism; build verified performance rows separately after approval. |
| Zhang2022 DOI 10.1016/j.tibtech.2022.09.011 | mycelium performance_data[1-5], mechanisms[0-2] | Mostly cellulose/nanocellulose/biomass examples, not mycelium adsorption. | Remove/reassign or split to biomass/cellulose after approval. |
| Foorginezhad2025 DOI 10.1039/d4va00378k | cell-membrane-ion-channel performance_data[5-13], mechanisms[12] | Local PDF not found in path scan; rows are generic membrane performance. | Locate PDF or demote to missing_pdf/keep_soft. |
| Shaeli2022 DOI 10.1016/j.scitotenv.2022.156014 | cell-membrane-ion-channel performance_data[0-2] | PDF exists under `2nd/全局综述（补充）`, while JSON source path points to a non-existing global-review path. | Normalize source path if kept. |

## Audit Statistics

- performance_data preflighted: 67 rows across five prototypes.
- mechanisms preflighted: 37 main JSON mechanisms and 37 enrichment mechanism mirrors.
- engineering_constraints preflighted: 36 rows.
- critical wrong-source groups queued: Chlorella Technology rows; IOB CN113275374A/MICP rows; SRB iron-cycle rows; mycelium Zhang2022 cellulose/nanocellulose rows; cell-membrane generic membrane performance rows.
- highest-value supported evidence to preserve: Cheng2021 Pb microalgae adsorption, Peng2022 Chlorella-derived magnetic biochar with scope caveat, Luo2021 schwertmannite arsenic removal, Jhariya2024 jarosite/schwertmannite Se(VI), Kumar2020 SRB sulfide precipitation, Liu2021 fungal biosorption, Beratto-Ramos/Chen/Lu/Vincenzo membrane separation mechanisms.
