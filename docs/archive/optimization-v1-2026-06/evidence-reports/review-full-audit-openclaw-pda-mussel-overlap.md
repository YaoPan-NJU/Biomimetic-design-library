status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-17T00:20:35+08:00

# PDA–Mussel-Foot Overlap, Path, and Source-Domain Cleanup Audit

## Scope

- **prototypes_db/polydopamine-coating.json** (44 performance_data rows, 57 mechanisms, 10 narrative entries)
- **prototypes_db/mussel-foot-adhesion.json** (43 performance_data rows, 34 mechanisms)
- **prototypes_db/enrichment/polydopamine-coating.json** (65 enrichment mechanisms)
- **prototypes_db/enrichment/mussel-foot-adhesion.json** (88 enrichment mechanisms)
- **docs/optimization-v1/review-full-audit-batch-01-polydopamine-coating.md** (previous batch-01 audit)
- **docs/optimization-v1/review-full-audit-decision-queue.md** (F01-PDA-* items)
- **docs/optimization-v1/review-boundary-do-not-register.md** (B01-PDA-* items)

## Executive Summary

**32 performance_data rows are exact character-for-character duplicates across polydopamine-coating and mussel-foot-adhesion** (parameter + value + locator + source_file identical). These 32 rows span 9 source files shared between both prototypes. The overlap is caused by a single root cause: both prototypes were populated from the same extraction pipeline without deduplication or scope-specific filtering.

Of the 9 overlapping source files:
- **3 are legitimate PDA adsorption studies** (Shi2021, Xiao2021, Yan2022) — these are PDA-based materials used for adsorption, fitting both "PDA coating" and "mussel-inspired adhesive chemistry"
- **3 are PDA+chitosan/composite studies** (Zhang2021, Jin2023, Xiang2023) — borderline; chitosan is not mussel-specific
- **2 are scanned patents** (CN114570339A, CN115055171A) — both PDA-centric, not mussel-specific
- **1 is a tannic-acid study** (Foroutan2021) — uses PDA but not mussel-inspired

**Enrichment files have 65/88 and 65/65 mechanisms respectively, ALL with populated causal_chain structure but 0 with actual text content in the chain fields** — i.e., structurally populated but semantically empty. 12 overlapping enrichment mechanism names are wrong_source for polydopamine-coating (hydrophobic membrane/superhydrophobic reviews).

---

## Literature And File Mapping

| source_family | local_pdf_or_cache_path | extraction_json_path | appears_in | scope_class | unique_path_confidence | notes |
|---|---|---|---|---|---|---|
| CN114887602A (PDA-cellulose-phosphorus patent) | **MISSING** | — | PDA only | PDA coating (composite) | high (name match) | PDF not found in library; 4 performance_data rows depend on it |
| Shi2021 (PDA-magnetic-Pb adsorption) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf` | `tools/litextract/outputs/extractions/第三波/json/2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.json` | PDA + Mussel | PDA adsorption | high | 3 exact-dup rows; legitimate overlap — PDA coating for Pb adsorption |
| Foroutan2021 (PDA-magnetic-Hg/Co/Ni) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf` | `tools/litextract/outputs/extractions/第三波/json/2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.json` | PDA + Mussel | PDA adsorption | high | 9 exact-dup rows; legitimate overlap |
| Xiao2021 (COF@PDA adsorption) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf` | `tools/litextract/outputs/extractions/第三波/json/2021-Xiao-cof-adsorption-water-treatment-regeneration.json` | PDA + Mussel | COF composite (PDA-modified) | high | 7 exact-dup rows; COF is not mussel-specific — belongs in PDA coating only |
| Zhang2021 (chitosan-PDA-Gd aerogel) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf` | `tools/litextract/outputs/extractions/第三波/json/2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.json` | PDA + Mussel | Chitosan-PDA composite | high | 1 exact-dup row; chitosan is not mussel-specific |
| CN114570339A (PDA-uranium patent, scanned) | `仿生文献库/3rd/第三波-仿生吸附专利/2022-CN114570339A-polydopamine-uranium-adsorbent.pdf` | `tools/litextract/outputs/extractions/第三波/json/2022-CN114570339A-polydopamine-uranium-adsorbent.json` | PDA + Mussel | PDA adsorption (scanned) | high | 7 exact-dup rows; scanned patent, cannot verify text |
| CN115055171A (PDA-magnetic-heavy metal, scanned) | `仿生文献库/专利/2022-CN115055171A-聚多巴胺-磁性-重金属-吸附 2.pdf` | (text layer present) | PDA + Mussel | PDA adsorption | high | 1 exact-dup row; text verified in batch-01 audit |
| Yan2022 (PDA/MGO/CA-CD dye adsorption) | `仿生文献库/3rd/第D组-再生循环/2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf` | `tools/litextract/outputs/extractions/第三波/json/2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.json` | PDA + Mussel | PDA adsorption | high | 2 exact-dup rows |
| Godiya2022 (chitosan-cellulose-PDA hydrogel) | `仿生文献库/3rd/第A组-贻贝仿生/2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.pdf` | `tools/litextract/outputs/extractions/第三波/json/2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.json` | PDA only | Chitosan-cellulose-PDA composite | high | 2 rows; chitosan is not mussel-specific |
| Yuan2024 (tannic acid-cellulose-Cr/Cu/CR) | `仿生文献库/3rd/第A组-贻贝仿生/2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf` | `tools/litextract/outputs/extractions/第三波/json/2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.json` | PDA only | Tannic acid composite (not PDA-core) | high | 3 rows; TA is not PDA/mussel — **wrong_source candidate** |
| Jin2023 (PDA-chitosan-carmine) | `仿生文献库/3rd/第A组-贻贝仿生/2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf` | `tools/litextract/outputs/extractions/第三波/json/2023-Jin-polydopamine-chitosan-carmine-adsorption.json` | PDA + Mussel | PDA-chitosan composite | high | 1 exact-dup row |
| Xiang2023 (PDA-PEI-Ge adsorption) | `仿生文献库/3rd/第A组-贻贝仿生/2023-Xiang-polydopamine-amine-germanium-adsorption.pdf` | `tools/litextract/outputs/extractions/第三波/json/2023-Xiang-polydopamine-amine-germanium-adsorption.json` | PDA + Mussel | PDA adsorption | high | 1 exact-dup row |
| CN113244898A (PDA-kaolin-Pb, scanned) | `仿生文献库/3rd/第三波-仿生吸附专利/2021-CN113244898A-polydopamine-kaolin-lead.pdf` | `tools/litextract/outputs/extractions/第三波/json/2021-CN113244898A-polydopamine-kaolin-lead.json` | PDA only | PDA adsorption (scanned) | high | 3 rows; scanned, needs OCR |
| CN113042006A (PDA-CS-magnetic, PDF missing) | **MISSING** (visual_cache exists) | `tools/litextract/outputs/extractions/专利/json/2021-CN113042006A-聚多巴胺-壳聚糖-磁性-仿生.json` | Mussel only | PDA-chitosan composite | high | 4 rows; PDF not found, visual_cache used |
| CN114849661A (PDA-membrane-U, PDF missing) | **MISSING** (visual_cache exists) | `tools/litextract/outputs/extractions/专利/json/2022-CN114849661A-聚多巴胺-吸附-膜.json` | Mussel only | PDA membrane | high | 3 rows; PDF not found, visual_cache used |
| CN105413659B (PDA-magnetic-biomimetic-U, PDF missing) | **MISSING** | — | Mussel only | PDA magnetic | high | 3 rows; PDF not found |
| Tang2023 (MI-PDA molecularly imprinted, PDF missing) | **MISSING** | — | Mussel only | PDA molecular imprinting | high | 1 row; PDF not found |

---

## Overlap Matrix

| source_file | polydopamine_rows | mussel_rows | same_claim_or_distinct_use | recommended_owner | rationale |
|---|---|---|---|---|---|
| 2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf | 9 (Hg/Co/Ni qmax + removal rates at 25/50°C) | 9 (identical) | **exact_dup** — same claims | **PDA coating** | Material is HAp/Fe₃O₄/PDA; "PDA coating" is the functional layer. No mussel-foot adhesion mechanism involved. Remove from mussel-foot. |
| 2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf | 3 (Pb qmax at 300/308/318K) | 3 (identical) | **exact_dup** — same claims | **PDA coating** | Material is MnO₂/PDA/Fe₃O₄ fibers; PDA coating for Pb adsorption. No mussel-foot adhesion. Remove from mussel-foot. |
| 2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf | 7 (COF@PDA + bare COF qmax for Fe/Co/Ni + cycling) | 7 (identical) | **exact_dup** — same claims | **PDA coating** (or **neither**) | COF@PDA is a COF with PDA modification. Not mussel-foot adhesion. COF is not PDA-core either — consider scope move. |
| 2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf | 1 (Gd(III) qmax 150.86) | 1 (identical) | **exact_dup** — same claim | **PDA coating** (chitosan-PDA composite) | MWCNT-PDA-CS-GO aerogel; chitosan is not mussel-specific. Keep in PDA coating. |
| 2022-CN114570339A-polydopamine-uranium-adsorbent.pdf | 7 (H-PDA-SO U(VI) qmax at multiple T/pH) | 7 (identical) | **exact_dup** — same claims | **PDA coating** | PDA+oxime co-deposition for U(VI). Core chemistry is PDA surface functionalization. Remove from mussel-foot. |
| 2022-CN115055171A-聚多巴胺-磁性-重金属-吸附 2.pdf | 1 (cycling stability >72%) | 1 (identical) | **exact_dup** — same claim | **PDA coating** | PDA-magnetic composite for heavy metal adsorption. No mussel-foot adhesion. |
| 2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf | 2 (MB/MG/CV qmax) | 2 (identical) | **exact_dup** — same claims | **PDA coating** | PDA/MGO/CA-CD for dye adsorption. PDA is the functional coating layer. Remove from mussel-foot. |
| 2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf | 1 (PDA/DCS carmine qmax 1194.4) | 1 (identical) | **exact_dup** — same claim | **PDA coating** | PDA-chitosan composite for carmine. PDA coating is the key. |
| 2023-Xiang-polydopamine-amine-germanium-adsorption.pdf | 1 (Ge(IV) ~0.33 mmol/g) | 1 (identical) | **exact_dup** — same claim | **PDA coating** | Fe₃O₄@PDA-PEI for Ge. PDA coating is the functional layer. |

**Summary:** All 9 overlapping sources (32 rows) are **exact duplicates**. In every case, the material uses PDA as a surface coating/modification layer for adsorption. None involve mussel-foot biological adhesion (byssal thread, DOPA-mediated wet adhesion to substrates). **Recommended: keep all 32 rows in polydopamine-coating; remove all 32 from mussel-foot-adhesion.**

---

## PDA performance_data — Mechanical Normalization Candidates

Rows with source_path that can be mechanically normalized (bare filename → full local path):

| row_index | current source_file | normalized path | field |
|---|---|---|---|
| 5-7 | `2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Shi-...pdf` | source_file |
| 8-9 | `2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf` | `仿生文献库/3rd/第D组-再生循环/2022-Yan-...pdf` | source_file |
| 10-16 | `2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Xiao-...pdf` | source_file |
| 20 | `2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Zhang-...pdf` | source_file |
| 21-22 | `2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2022-Godiya-...pdf` | source_file |
| 23-25 | `2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2024-Yuan-...pdf` | source_file |
| 33-41 | `2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Foroutan-...pdf` | source_file |
| 42 | `2023-Xiang-polydopamine-amine-germanium-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2023-Xiang-...pdf` | source_file |
| 43 | `2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2023-Jin-...pdf` | source_file |
| 0-3 | `仿生文献库/专利/2022-CN114887602A-...pdf` | same (but PDF missing) | source_file |

---

## Package A Candidate Table

Low-risk mechanical items only. No semantic changes, no scope moves, no verification upgrades.

| candidate_id | target_json | field_path | current_value | proposed_value | evidence_for_mechanical_safety | recommended_action |
|---|---|---|---|---|---|---|
| PA-PDA-001 | polydopamine-coating.json | performance_data[5].source_file | `2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf` | `find` confirms file exists at normalized path; no semantic change | normalize source_file |
| PA-PDA-002 | polydopamine-coating.json | performance_data[6].source_file | `2021-Shi-...pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Shi-...pdf` | same | normalize source_file |
| PA-PDA-003 | polydopamine-coating.json | performance_data[7].source_file | `2021-Shi-...pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Shi-...pdf` | same | normalize source_file |
| PA-PDA-004 | polydopamine-coating.json | performance_data[8].source_file | `2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf` | `仿生文献库/3rd/第D组-再生循环/2022-Yan-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-005 | polydopamine-coating.json | performance_data[9].source_file | `2022-Yan-...pdf` | `仿生文献库/3rd/第D组-再生循环/2022-Yan-...pdf` | same | normalize source_file |
| PA-PDA-006 | polydopamine-coating.json | performance_data[10-16].source_file | `2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf` (7 rows) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Xiao-...pdf` | `find` confirms | normalize source_file (7 rows) |
| PA-PDA-007 | polydopamine-coating.json | performance_data[20].source_file | `2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2021-Zhang-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-008 | polydopamine-coating.json | performance_data[21-22].source_file | `2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.pdf` (2 rows) | `仿生文献库/3rd/第A组-贻贝仿生/2022-Godiya-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-009 | polydopamine-coating.json | performance_data[23-25].source_file | `2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf` (3 rows) | `仿生文献库/3rd/第A组-贻贝仿生/2024-Yuan-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-010 | polydopamine-coating.json | performance_data[33-41].source_file | `2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf` (9 rows) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Foroutan-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-011 | polydopamine-coating.json | performance_data[42].source_file | `2023-Xiang-polydopamine-amine-germanium-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2023-Xiang-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-012 | polydopamine-coating.json | performance_data[43].source_file | `2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf` | `仿生文献库/3rd/第A组-贻贝仿生/2023-Jin-...pdf` | `find` confirms | normalize source_file |
| PA-PDA-013 | polydopamine-coating.json | performance_data[8].pollutant | `""` (empty) | `"MB (亚甲基蓝)"` | Abstract states "maximum adsorption capacities of PDA/MGO/CA-CD towards MB" — pollutant is MB | fill empty pollutant |
| PA-PDA-014 | polydopamine-coating.json | performance_data[9].pollutant | `""` (empty) | `"MG (孔雀石绿) / CV (结晶紫)"` | Abstract states MG and CV values | fill empty pollutant |
| PA-PDA-015 | polydopamine-coating.json | performance_data[13].pollutant | `""` (ambiguous: `candidates=['Ni(II)', 'Co(II)']`) | `"Fe(II)/Co(II)/Ni(II) mixed"` | Section 3.2.5 states retention for all three metals | disambiguate pollutant |
| PA-PDA-016 | polydopamine-coating.json | performance_data[14].pollutant | `""` (empty) | `"Fe(II)"` | Section 3.2.3 states COF Fe2+ capacity | fill empty pollutant |
| PA-PDA-017 | polydopamine-coating.json | performance_data[15].pollutant | `""` (empty) | `"Co(II)"` | same | fill empty pollutant |
| PA-PDA-018 | polydopamine-coating.json | performance_data[16].pollutant | `""` (empty) | `"Ni(II)"` | same | fill empty pollutant |
| PA-MUSSEL-001 | mussel-foot-adhesion.json | performance_data[7].pollutant | `""` (empty) | `"重金属 (heavy metals)"` | Patent text confirms heavy metal removal cycling | fill empty pollutant |
| PA-MUSSEL-002 | mussel-foot-adhesion.json | performance_data[20].pollutant | `""` (ambiguous) | `"Fe(II)/Co(II)/Ni(II) mixed"` | Same as PDA PA-PDA-015 | disambiguate pollutant |
| PA-MUSSEL-003 | mussel-foot-adhesion.json | performance_data[21].pollutant | `""` (empty) | `"Fe(II)"` | same as PDA PA-PDA-016 | fill empty pollutant |
| PA-MUSSEL-004 | mussel-foot-adhesion.json | performance_data[22].pollutant | `""` (empty) | `"Co(II)"` | same | fill empty pollutant |
| PA-MUSSEL-005 | mussel-foot-adhesion.json | performance_data[23].pollutant | `""` (empty) | `"Ni(II)"` | same | fill empty pollutant |
| PA-MUSSEL-006 | mussel-foot-adhesion.json | performance_data[15].pollutant | `""` (empty) | `"MB (亚甲基蓝)"` | same as PDA PA-PDA-013 | fill empty pollutant |
| PA-MUSSEL-007 | mussel-foot-adhesion.json | performance_data[16].pollutant | `""` (empty) | `"MG (孔雀石绿) / CV (结晶紫)"` | same as PDA PA-PDA-014 | fill empty pollutant |

---

## Decision-Ready Candidate Table

Items requiring Yao or Codex decision. Each has target_json, field_path, source, locator, quote/quote-impossible reason, evidence_label, and recommended_action.

| candidate_id | target_json | field_path | claim_summary | local_source | locator | quote | evidence_label | recommended_action | yao_decision_needed |
|---|---|---|---|---|---|---|---|---|---|
| DR-PDA-MU-001 | mussel-foot-adhesion.json | performance_data[12-14] | Pb(II) qmax 196.67/200.45/205.07 mg/g at 300/308/318K (Shi2021) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf` | Section 3.3.3, p.4 | "The maximum adsorption capacity (Qm) was 196.67, 200.45 and 205.07 mg/g at 300 K, 308 K and 318 K" | supported | **Remove from mussel-foot-adhesion.** Material is MnO₂/PDA/Fe₃O₄ — a PDA-coated adsorbent, not mussel-foot adhesion. | Y: confirm removal from mussel |
| DR-PDA-MU-002 | mussel-foot-adhesion.json | performance_data[32-40] | Hg/Co/Ni qmax + removal rates at 25/50°C (Foroutan2021) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf` | Abstract, Section 3.4 | "The highest elimination capacity (qm) for Hg(II), Co(II), and Ni(II) was set at 51.73 mg/g, 49.32 mg/g, and 48.09 mg/g" | supported | **Remove from mussel-foot-adhesion.** HAp/Fe₃O₄/PDA composite — PDA coating for adsorption, not mussel-foot adhesion. | Y: confirm removal from mussel |
| DR-PDA-MU-003 | mussel-foot-adhesion.json | performance_data[17-23] | COF@PDA + bare COF qmax for Fe/Co/Ni + cycling (Xiao2021) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf` | Section 3.2.3-3.2.5 | "the calculated capture capacities of COF@PDA for Fe2+, Co2+ and Ni2+ equal 204.9, 194.2, and 207.5 mg/g" | supported | **Remove from mussel-foot-adhesion.** COF@PDA is a COF with PDA modification — not mussel-foot adhesion. Consider scope move to COF prototype. | Y: confirm removal from mussel |
| DR-PDA-MU-004 | mussel-foot-adhesion.json | performance_data[24] | Gd(III) qmax 150.86 mg/g (Zhang2021) | `仿生文献库/3rd/第A组-贻贝仿生/2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf` | Abstract, p.1 | "the maximum adsorption capacity of aerogel for Gd(III) reached 150.86 mg g⁻¹" | supported | **Remove from mussel-foot-adhesion.** MWCNT-PDA-CS-GO imprinted aerogel — chitosan is not mussel-specific. | Y: confirm removal from mussel |
| DR-PDA-MU-005 | mussel-foot-adhesion.json | performance_data[25-31] | H-PDA-SO U(VI) qmax at multiple T/pH (CN114570339A, scanned) | `仿生文献库/3rd/第三波-仿生吸附专利/2022-CN114570339A-polydopamine-uranium-adsorbent.pdf` | 摘要, 有益效果, 实施例, 图4-7 | **Scanned patent — quote impossible without OCR** | needs_human_decision | **Remove from mussel-foot-adhesion.** PDA+oxime for U(VI) — PDA surface functionalization, not mussel-foot adhesion. Scanned status unchanged. | Y: confirm removal from mussel |
| DR-PDA-MU-006 | mussel-foot-adhesion.json | performance_data[7] | Cycling stability >72% (CN115055171A) | `仿生文献库/专利/2022-CN115055171A-聚多巴胺-磁性-重金属-吸附 2.pdf` | 说明书第0036段 | "Fe3O4@PDA@CSH复合磁性吸附材料对上述重金属去除率仍能保持在72％以上" | supported | **Remove from mussel-foot-adhesion.** PDA-magnetic composite — not mussel-foot adhesion. | Y: confirm removal from mussel |
| DR-PDA-MU-007 | mussel-foot-adhesion.json | performance_data[15-16] | MB/MG/CV qmax (Yan2022) | `仿生文献库/3rd/第D组-再生循环/2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf` | Abstract, p.1 | "the maximum adsorption capacities of PDA/MGO/CA-CD towards MB, MG, and CV were 1372.32, 822.39, and 570.79 mg/g" | supported | **Remove from mussel-foot-adhesion.** PDA/MGO/CA-CD — PDA coating for dye adsorption. | Y: confirm removal from mussel |
| DR-PDA-MU-008 | mussel-foot-adhesion.json | performance_data[42] | PDA/DCS carmine qmax 1194.4 (Jin2023) | `仿生文献库/3rd/第A组-贻贝仿生/2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf` | 摘要, p.371 | "PDA/DCS 最大单分子层吸附量可达到 1194.4 mg/g" | supported | **Remove from mussel-foot-adhesion.** PDA-chitosan composite. | Y: confirm removal from mussel |
| DR-PDA-MU-009 | mussel-foot-adhesion.json | performance_data[41] | Ge(IV) ~0.33 mmol/g (Xiang2023) | `仿生文献库/3rd/第A组-贻贝仿生/2023-Xiang-polydopamine-amine-germanium-adsorption.pdf` | 图8描述, p.7 | "适宜的溶液pH为6左右" (pH 6 confirmed; 0.33 value from figure) | partial | **Remove from mussel-foot-adhesion.** Fe₃O₄@PDA-PEI — PDA coating. Value may be figure-estimated. | Y: confirm removal from mussel |
| DR-PDA-SC-001 | polydopamine-coating.json | performance_data[23-25] | Cr(VI)/Cu(II)/CR qmax (Yuan2024) | `仿生文献库/3rd/第A组-贻贝仿生/2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf` | Abstract, p.1 | "rapid and excellent adsorption performance for Cr(VI), Cu(II), and Congo red (CR), with the Qm of 456.62, 289.86, and 3429.23 mg/g" | supported | **Scope move candidate.** CNF-TA-PMMT-PEI is tannic-acid-centric, not PDA-core. TA is the primary crosslinker, not PDA. Consider moving to plant-tannin prototype. | Y: confirm scope move |
| DR-PDA-MU-010 | mussel-foot-adhesion.json | mechanisms["PDA涂层粘附机制"].causal_chain | PDA coating adhesion mechanism from Lee2007 | `仿生文献库/2nd/第12组-仿生案例/2007-Lee-mussel-inspired-surface-chemistry-coatings.pdf` | p.426-427, Fig.1 | "DOPA and lysine (amines) groups found in byssal plaque proteins...dopamine is a small-molecule compound that contains both functionalities" | verified | **Keep in mussel-foot-adhesion.** This is the foundational mussel-inspired PDA mechanism — legitimate mussel-foot content. But also exists in PDA enrichment with same causal_chain. No dedup needed (enrichment mirrors main). | N: no action needed |
| DR-PDA-MU-011 | mussel-foot-adhesion.json | mechanisms["PDA自聚合形成机制"].causal_chain | PDA self-polymerization mechanism from Lee2007 | `仿生文献库/2nd/第12组-仿生案例/2007-Lee-mussel-inspired-surface-chemistry-coatings.pdf` | p.427, Sec.1 | "dopamine self-polymerization into thin, surface-adherent polydopamine films onto a wide range of inorganic and organic materials" | verified | **Keep in mussel-foot-adhesion.** Foundational mussel-inspired chemistry. Also in PDA — legitimate overlap for this mechanism. | N: no action needed |
---

## Enrichment Cross-Check

### Enrichment Files Structure

Both enrichment files contain only a `mechanisms` dict (no performance_data, no narrative, no engineering_constraints). The dict keys are mechanism names matching the main JSON.

### Empty Causal Chain Audit

All enrichment mechanisms have **structurally populated** causal_chain objects (with keys: pollutant_feature, bio_structure, interaction, why_it_works, boundary_conditions, transferable_principle, verification_quote). However, **0 out of 65 (PDA) and 0 out of 88 (Mussel) have actual text content in the chain fields** — the text/basis/locator fields are all empty or `llm_inferred` with no locator.

This means the enrichment causal_chains are **template shells**, not populated evidence chains. They do not add verification value.

### Wrong-Source Mirror Audit (Enrichment)

12 overlapping enrichment mechanism names are wrong_source for polydopamine-coating (hydrophobic membrane/superhydrophobic reviews):

| mechanism_name | source_doi | scope mismatch |
|---|---|---|
| Teflon AF 2400涂层PVDF膜VMD性能 | 10.3390/polym14245439 | Hydrophobic PVDF membrane, not PDA |
| 疏水改性三大方法 | 10.3390/polym14245439 | Same |
| PVDF-co-HFP/POTS超疏水膜MD性能 | 10.3390/polym14245439 | Same |
| 特殊润湿性分类 | 10.1021/acsami.0c18794 | Superhydrophobic review |
| 荷叶效应仿生原理 | 10.1021/acsami.0c18794 | Same |
| 壁虎脚仿生特性 | 10.1021/acsami.0c18794 | Same |
| 玫瑰花瓣高黏附超疏水 | 10.1021/acsami.0c18794 | Same |
| 浸涂法制备超疏水表面 | 10.1021/acsami.0c18794 | Same |
| 溶胶-凝胶法制备超疏水纺织品 | 10.1021/acsami.0c18794 | Same |
| TiO2光催化降解机理 | 10.1021/acsami.0c18794 | Same |
| CeO2纳米粒子超疏水光催化膜 | 10.1021/acsami.0c18794 | Same |
| pH响应PDMS-bP4VP电纺膜 | 10.1021/acsami.0c18794 | Same |

**These are mirrored from the main JSON's wrong_source mechanisms into enrichment.** They should be flagged for removal from both main and enrichment.

### Main–Enrichment Consistency

- PDA: 57 mechanisms in main, 65 in enrichment → enrichment has **8 additional mechanisms** not in main. All 57 main mechanisms have matching enrichment entries. No missing mirrors.
- Mussel: 34 mechanisms in main, 88 in enrichment → enrichment has **54 additional mechanisms** not in main. All 34 main mechanisms have matching enrichment entries. No missing mirrors.

**Inconsistency:** Enrichment files are supersets of main, containing mechanisms that don't appear in main JSON. This is by design (enrichment adds mechanisms), but the extra mechanisms in enrichment should be validated for scope.

---

## Boundary / DO-NOT Candidate Table

| boundary_id | target_field | boundary_type_candidate | rationale | source | locator | quote | evidence_label | recommended_action |
|---|---|---|---|---|---|---|---|---|
| B01-PDA-MU-001 | mussel-foot-adhesion.json performance_data[12-42] (32 rows) | hard_do_not (scope) | 32 exact-duplicate rows belong in PDA coating, not mussel-foot adhesion. None involve mussel-foot biological adhesion (byssal thread, DOPA-mediated wet adhesion to substrates). All are PDA-coated adsorbents for pollutant removal. | All 9 overlapping sources | N/A | N/A | wrong_source | Remove 32 rows from mussel-foot-adhesion; keep in polydopamine-coating |
| B01-PDA-SC-001 | polydopamine-coating.json performance_data[23-25] | knowledge_gap (scope) | Yuan2024 (CNF-TA-PMMT-PEI) is tannic-acid-centric, not PDA-core. TA is the primary crosslinker. 3 rows may belong in plant-tannin prototype. | 2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf | Abstract | "CNF-TA-PMMT-PEI" — TA prefix dominant | partial | Scope move to plant-tannin after Yao confirmation |
| B01-PDA-ENR-001 | enrichment/polydopamine-coating.json mechanisms (12 entries) | wrong_source | 12 enrichment mechanisms from hydrophobic membrane/superhydrophobic reviews (polym14245439, acsami.0c18794) are wrong_source for PDA coating. Mirrored from main JSON wrong_source mechanisms. | Multiple review DOIs | N/A | N/A | wrong_source | Remove from enrichment after Yao confirmation |
| B01-PDA-ENR-002 | enrichment/polydopamine-coating.json (all 65 mechanisms) | knowledge_gap | All 65 enrichment causal_chains are structurally populated but semantically empty (no text in chain fields). They add no verification value. | N/A | N/A | N/A | knowledge_gap | Either populate chains or remove empty shells |
| B01-PDA-SC-002 | polydopamine-coating.json mechanisms (57 entries) | knowledge_gap | Main JSON mechanisms include ~10 wrong_source entries from hydrophobic/antibacterial reviews (same as batch-01 M-02 through M-09). | Multiple review DOIs | N/A | N/A | wrong_source | Remove or reassign after Yao confirmation |

---

## Open Questions

1. **Yao decision: Remove 32 exact-duplicate rows from mussel-foot-adhesion?**
   - All 32 rows are PDA-coated adsorbent data, not mussel-foot biological adhesion.
   - Recommendation: Remove from mussel; keep in PDA coating.
   - Risk: Mussel-foot-adhesion would drop from 43 to 11 performance_data rows.

2. **Yao decision: Scope move Yuan2024 (tannic acid) from PDA coating to plant-tannin?**
   - 3 rows (Cr(VI)/Cu(II)/CR qmax) from CNF-TA-PMMT-PEI; TA is primary crosslinker.
   - Recommendation: Move to plant-tannin prototype.

3. **Yao decision: Remove 12 wrong_source enrichment mechanisms from PDA enrichment?**
   - Hydrophobic membrane/superhydrophobic review mechanisms don't belong in PDA.
   - Also remove from main JSON mechanisms (batch-01 M-02 through M-09).

4. **Yao decision: Populate or remove empty enrichment causal_chains?**
   - All 65 PDA enrichment and 88 mussel enrichment causal_chains are template shells.
   - Options: (a) populate with evidence from batch-01 audit, (b) remove empty shells, (c) keep as placeholders.

5. **Scanned patents (CN113244898A, CN114570339A): OCR or visual reading needed?**
   - 3 rows (CN113244898A) + 7 rows (CN114570339A) = 10 rows in PDA with unverifiable claims.
   - Same 7 rows from CN114570339A also in mussel (to be removed per decision 1).

6. **Missing PDFs: CN114887602A, CN105413659B, CN113042006A, CN114849661A, Tang2023?**
   - CN114887602A: 4 PDA rows depend on it; PDF not in library.
   - CN105413659B, CN113042006A, CN114849661A, Tang2023: mussel-only rows; PDFs not in library (visual_caches exist for 2).

7. **Ge(IV) value verification: 0.33 mmol/g from Xiang2023?**
   - Value may be figure-estimated; text confirms pH 6 is optimal but not the exact qm.
   - Recommendation: Verify against Table 3 or Figure 8 y-axis before accepting.
