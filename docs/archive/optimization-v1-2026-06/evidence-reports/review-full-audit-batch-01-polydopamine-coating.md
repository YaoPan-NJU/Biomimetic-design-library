# Full Audit Batch 01: polydopamine-coating

status: ready_for_codex_review

## Scope

- **Prototype JSON:** `prototypes_db/polydopamine-coating.json`
- **Enrichment JSON:** `prototypes_db/enrichment/polydopamine-coating.json`
- **Audit date:** 2026-06-16
- **Worker:** lit-extract (mimo-v2.5)

## Audit Summary

- **Total performance_data entries:** 45
- **Total mechanisms:** 57 (base JSON) + 57 (enrichment JSON, empty causal_chains)
- **Total narrative entries:** 10
- **Total engineering_constraints:** 22
- **PDFs found locally:** 13 of 15 unique source files
- **PDFs verified against:** 11 sources (text extraction)
- **Scanned PDFs (no text layer):** 2 (CN113244898A, CN114570339A)
- **Missing PDF:** 1 (CN114887602A)

---

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_path | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---------|-------------|------------|------------|---------------|-------------|---------|----------|------------|---------|-------|----------------|-------------------|-------|
| PD-01 | polydopamine-coating.json | performance_data[0] | performance | qmax 159.8 mg/g BC/PDA/La(OH)3-1 for inorganic P | 仿生文献库/专利/2022-CN114887602A-聚多巴胺-纤维素-吸附-除磷.pdf | null | N/A | **NO (PDF missing)** | 说明书[0147]-[0148]段 | — | missing_pdf | missing_pdf | Patent PDF not found in library; extraction JSON empty (0 records) |
| PD-02 | polydopamine-coating.json | performance_data[1] | performance | Adsorption comparison: 159.8 vs 91.2 vs 12.6 vs 0 mg/g | 同上 | null | N/A | **NO** | 说明书[0147]段，图2 | — | missing_pdf | missing_pdf | Same missing PDF |
| PD-03 | polydopamine-coating.json | performance_data[2] | performance | 5-cycle retention: 110 mg/g | 同上 | null | N/A | **NO** | 说明书[0149]段，图7 | — | missing_pdf | missing_pdf | Same missing PDF |
| PD-04 | polydopamine-coating.json | performance_data[3] | performance | Real water adsorption: 143.4 mg/g | 同上 | null | N/A | **NO** | 说明书[0149]段，图11 | — | missing_pdf | missing_pdf | Same missing PDF |
| PD-05 | polydopamine-coating.json | performance_data[4] | performance | Heavy metal cycling stability >72% | 2022-CN115055171A-聚多巴胺-磁性-重金属-吸附 2.pdf | null | workspace copy | YES | 说明书第0036段 | "Fe3O4@PDA@CSH复合磁性吸附材料对上述重金属去除率仍能保持在72％以上" | **supported** | add_quote_locator | PDF is scanned but text layer present; quote verified. Locators are patent paragraph numbers. |
| PD-06 | polydopamine-coating.json | performance_data[5] | performance | Pb(II) qmax 196.67 mg/g at 300K | 2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf | 10.1016/j.apsusc.2020.148379 | workspace copy | YES | Section 3.3.3, p.4 | "The maximum adsorption capacity (Qm) was 196.67, 200.45 and 205.07 mg/g at 300 K, 308 K and 318 K" | **supported** | no_action | Exact match. Material confirmed as MnO2/PDA/Fe3O4 fibers, pH 5.0. |
| PD-07 | polydopamine-coating.json | performance_data[6] | performance | Pb(II) qmax 200.45 mg/g at 308K | 同上 | 同上 | 同上 | YES | Section 3.3.3, p.4 | 同上引用 | **supported** | no_action | |
| PD-08 | polydopamine-coating.json | performance_data[7] | performance | Pb(II) qmax 205.07 mg/g at 318K | 同上 | 同上 | 同上 | YES | Section 3.3.3, p.4 | 同上引用 | **supported** | no_action | |
| PD-09 | polydopamine-coating.json | performance_data[8] | performance | MB max adsorption 1372.32 mg/g | 2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf | 10.1016/j.apsusc.2022.154338 | workspace copy | YES | Abstract, p.1 | "the maximum adsorption capacities of PDA/MGO/CA-CD towards MB, MG, and CV were 1372.32, 822.39, and 570.79 mg/g" | **supported** | no_action | Exact match. |
| PD-10 | polydopamine-coating.json | performance_data[9] | performance | MG 822.39, CV 570.79 mg/g | 同上 | 同上 | 同上 | YES | Abstract, p.1 | 同上引用 | **supported** | no_action | |
| PD-11 | polydopamine-coating.json | performance_data[10] | performance | COF@PDA Fe2+ qmax 204.9 mg/g | 2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf | 10.1016/j.cej.2020.127837 | workspace copy | YES | Section 3.2.3, p.7 | "the calculated capture capacities of COF@PDA for Fe2+, Co2+ and Ni2+ equal 204.9, 194.2, and 207.5 mg/g" | **supported** | no_action | Exact match. |
| PD-12 | polydopamine-coating.json | performance_data[11] | performance | COF@PDA Co2+ qmax 194.2 mg/g | 同上 | 同上 | 同上 | YES | Section 3.2.3 | 同上引用 | **supported** | no_action | |
| PD-13 | polydopamine-coating.json | performance_data[12] | performance | COF@PDA Ni2+ qmax 207.5 mg/g | 同上 | 同上 | 同上 | YES | Section 3.2.3 | 同上引用 | **supported** | no_action | |
| PD-14 | polydopamine-coating.json | performance_data[13] | performance | 5-cycle retention: Fe2+ ~98%, Co2+ ~97.1%, Ni2+ ~97.3% | 同上 | 同上 | 同上 | YES | Section 3.2.5, p.7 | "only a 2% decrease for Fe2+, a 2.9% decrease for Co2+ and a 2.7% decrease for Ni2+" | **supported** | add_quote_locator | Values derived from 2%/2.9%/2.7% decrease → 98%/97.1%/97.3% retention. Consistent. |
| PD-15 | polydopamine-coating.json | performance_data[14] | performance | COF Fe2+ qmax 55.4 mg/g | 同上 | 同上 | 同上 | YES | Section 3.2.3 | "The maximum adsorption capacities of COF towards Fe2+, Co2+ and Ni2+ are only 55.4, 31.4 and 56.5 mg g−1" | **supported** | no_action | |
| PD-16 | polydopamine-coating.json | performance_data[15] | performance | COF Co2+ qmax 31.4 mg/g | 同上 | 同上 | 同上 | YES | Section 3.2.3 | 同上引用 | **supported** | no_action | |
| PD-17 | polydopamine-coating.json | performance_data[16] | performance | COF Ni2+ qmax 56.5 mg/g | 同上 | 同上 | 同上 | YES | Section 3.2.3 | 同上引用 | **supported** | no_action | |
| PD-18 | polydopamine-coating.json | performance_data[17] | performance | Pb2+ best removal 96.31% | 2021-CN113244898A-polydopamine-kaolin-lead.pdf | null | workspace copy | YES (scanned) | 摘要 | — | **needs_human_decision** | needs_human_decision | Scanned patent, no text layer. Cannot verify via text extraction. Value likely correct per extraction JSON but unverifiable. |
| PD-19 | polydopamine-coating.json | performance_data[18] | performance | Initial concentration effect: C0 4-70 mg/L | 同上 | null | 同上 | YES (scanned) | 应用实施例3, p.10 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-20 | polydopamine-coating.json | performance_data[19] | performance | Adsorbent dose effect: 5mg Re max 95.68% | 同上 | null | 同上 | YES (scanned) | 应用实施例4, p.10 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-21 | polydopamine-coating.json | performance_data[20] | performance | Gd(III) qmax 150.86 mg/g | 2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf | 10.1016/j.jhazmat.2020.124347 | workspace copy | YES | Abstract, p.1 | "the maximum adsorption capacity of aerogel for Gd(III) reached 150.86 mg g⁻¹" | **supported** | no_action | |
| PD-22 | polydopamine-coating.json | performance_data[21] | performance | Cu2+ qmax ~434.8 mg/g on MCC10 | 2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.pdf | 10.1016/j.jhazmat.2022.129112 | workspace copy | YES | Abstract, p.1 | "the MCC-PDA-PEI/CS-PDA-PEI hydrogel showed excellent Cu2+, Zn2+, and Ni2+ adsorbabilities of ~434.8, ~277.7, and ~261.8 mg/g" | **supported** | no_action | |
| PD-23 | polydopamine-coating.json | performance_data[22] | performance | Unmodified MCC/CS: Cu2+ 158.7, Zn2+ 161.2, Ni2+ 172.4 mg/g | 同上 | 同上 | 同上 | YES | Section 3.3, p.5 | "as compared to the unmodified MCC/CS hydrogel (158.7, 161.2, and 172.4, respectively)" | **supported** | no_action | |
| PD-24 | polydopamine-coating.json | performance_data[23] | performance | Cr(VI) Qm 456.62 mg/g | 2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf | 10.1016/j.seppur.2024.127979 | workspace copy | YES | Abstract, p.1 | "rapid and excellent adsorption performance for Cr(VI), Cu(II), and Congo red (CR), with the Qm of 456.62, 289.86, and 3429.23 mg/g" | **supported** | no_action | |
| PD-25 | polydopamine-coating.json | performance_data[24] | performance | Cu(II) Qm 289.86 mg/g | 同上 | 同上 | 同上 | YES | Abstract | 同上引用 | **supported** | no_action | |
| PD-26 | polydopamine-coating.json | performance_data[25] | performance | CR Qm 3429.23 mg/g | 同上 | 同上 | 同上 | YES | Abstract | 同上引用 | **supported** | no_action | |
| PD-27 | polydopamine-coating.json | performance_data[26] | performance | H-PDA-SO qmax 96.5 mg/g at 298K (abstract) | 2022-CN114570339A-polydopamine-uranium-adsorbent.pdf | null | workspace copy | YES (scanned) | 摘要 | — | **needs_human_decision** | needs_human_decision | Scanned patent, no text layer. Cannot verify. |
| PD-28 | polydopamine-coating.json | performance_data[27] | performance | H-PDA-SO qmax 103 mg/g (implementation) | 同上 | null | 同上 | YES (scanned) | 有益效果(2), p.4 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-29 | polydopamine-coating.json | performance_data[28] | performance | H-PDA-SO qmax 81.25 mg/g at 288K | 同上 | null | 同上 | YES (scanned) | 实施例10, 图6, p.7 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-30 | polydopamine-coating.json | performance_data[29] | performance | H-PDA-SO qmax 132.25 mg/g at 308K | 同上 | null | 同上 | YES (scanned) | 实施例10, 图6, p.7 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-31 | polydopamine-coating.json | performance_data[30] | performance | H-PDA-SO ~38 mg/g at pH 6.0 | 同上 | null | 同上 | YES (scanned) | 图4b, p.10 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-32 | polydopamine-coating.json | performance_data[31] | performance | H-PDA ~36 mg/g at pH 6.0 | 同上 | null | 同上 | YES (scanned) | 图4a, p.10 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-33 | polydopamine-coating.json | performance_data[32] | performance | H-PDA-SO ~8.2 mg/g (Fig 7) | 同上 | null | 同上 | YES (scanned) | 图7, p.12 | — | **needs_human_decision** | needs_human_decision | Same scanned patent |
| PD-34 | polydopamine-coating.json | performance_data[33] | performance | Hg(II) qmax 51.73 mg/g | 2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf | 10.1016/j.jece.2021.105709 | workspace copy | YES | Abstract, p.1 | "The highest elimination capacity (qm) for Hg(II), Co(II), and Ni(II) was set at 51.73 mg/g, 49.32 mg/g, and 48.09 mg/g" | **supported** | no_action | |
| PD-35 | polydopamine-coating.json | performance_data[34] | performance | Co(II) qmax 49.32 mg/g | 同上 | 同上 | 同上 | YES | Abstract | 同上引用 | **supported** | no_action | |
| PD-36 | polydopamine-coating.json | performance_data[35] | performance | Ni(II) qmax 48.09 mg/g | 同上 | 同上 | 同上 | YES | Abstract | 同上引用 | **supported** | no_action | |
| PD-37 | polydopamine-coating.json | performance_data[36] | performance | 25°C Hg(II) removal 94.36% | 同上 | 同上 | 同上 | YES | Section 3.4, p.7 | "the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36%" | **supported** | no_action | |
| PD-38 | polydopamine-coating.json | performance_data[37] | performance | 25°C Co(II) removal 93.66% | 同上 | 同上 | 同上 | YES | Section 3.4 | 同上引用 | **supported** | no_action | |
| PD-39 | polydopamine-coating.json | performance_data[38] | performance | 25°C Ni(II) removal 92.36% | 同上 | 同上 | 同上 | YES | Section 3.4 | 同上引用 | **supported** | no_action | |
| PD-40 | polydopamine-coating.json | performance_data[39] | performance | 50°C Hg(II) removal 90.14% | 同上 | 同上 | 同上 | YES | Section 3.4 | "to 90.14%, 88.84%, and 87.46%" | **supported** | no_action | |
| PD-41 | polydopamine-coating.json | performance_data[40] | performance | 50°C Co(II) removal 88.84% | 同上 | 同上 | 同上 | YES | Section 3.4 | 同上引用 | **supported** | no_action | |
| PD-42 | polydopamine-coating.json | performance_data[41] | performance | 50°C Ni(II) removal 87.46% | 同上 | 同上 | 同上 | YES | Section 3.4 | 同上引用 | **supported** | no_action | |
| PD-43 | polydopamine-coating.json | performance_data[42] | performance | Ge(IV) ~0.33 mmol/g at pH 6 | 2023-Xiang-polydopamine-amine-germanium-adsorption.pdf | 10.13373/j.cnki.cjrm.XY21060036 | workspace copy | YES | 图8描述, p.7 | "适宜的溶液pH为6左右" (pH 6 optimal); kinetics qe=0.127 mmol/g | **partial** | narrow_claim | Text confirms pH 6 is optimal but does NOT state 0.33 mmol/g explicitly. Value likely estimated from Figure 8 y-axis. Kinetics shows qe=0.127 mmol/g. The 0.33 mmol/g may be the isotherm qm from Table 3 (Sips model) but not directly quoted. |
| PD-44 | polydopamine-coating.json | performance_data[43] | performance | PDA/DCS carmine qmax 1194.4 mg/g | 2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf | 10.13550/j.jxhg.20220633 | workspace copy | YES | 摘要, p.371 | "PDA/DCS 最大单分子层吸附量可达到 1194.4 mg/g" | **supported** | no_action | |
| PD-45 | polydopamine-coating.json | performance_data[44] | performance | Regeneration 5-cycle: 616.90 mg/g | 同上 | 同上 | 同上 | YES | — | — | **needs_human_decision** | add_quote_locator | Value 616.90 mg/g for 5-cycle retention not found in abstract; may be in results section. Need figure/table verification. |

---

## Mechanism Audit

| item_id | target_json | field_path | mechanism_name | source_file | ref_doi | pdf_exists | verification_status | causal_chain_populated | evidence_label | recommended_action | notes |
|---------|-------------|------------|----------------|-------------|---------|------------|--------------------|-----------------------|----------------|-------------------|-------|
| M-01 | enrichment/polydopamine-coating.json | mechanisms["PDA吸附机制补充"] | PDA adsorption mechanism (π-π interaction) | 2021-Lei-mussel-magnetic-carboxymethyl-chitosan-aerogel-cationic.pdf | 10.1016/j.polymer.2020.123316 | YES | verified | YES (partially: some llm_inferred) | **supported** | keep_soft | Verification quote confirmed: "PDA has been regarded as a promising bio-sorbent due to its large number of reactive groups containing catechol, amino, imine groups". Causal chain has 2 boundary_conditions with gate_level=soft and basis=llm_inferred → keep_soft. |
| M-02 | enrichment/polydopamine-coating.json | mechanisms["Teflon AF 2400涂层PVDF膜VMD性能"] | Teflon AF 2400 coating PVDF membrane VMD | polym14245439 | 10.3390/polym14245439 | **NO (review paper PDF not found locally)** | needs_review | NO (empty) | **wrong_source** | needs_human_decision | This mechanism is about hydrophobic PVDF membranes, NOT polydopamine coating. Appears misplaced from a different prototype. No local PDF to verify. |
| M-03 | enrichment/polydopamine-coating.json | mechanisms["疏水改性三大方法"] | Three hydrophobic modification methods | polym14245439 | 10.3390/polym14245439 | NO | needs_review | NO (empty) | **wrong_source** | needs_human_decision | Same issue — hydrophobic membrane review, not PDA-related |
| M-04 | enrichment/polydopamine-coating.json | mechanisms["水滴'生长-跳跃'排液机制"] | Water droplet growing-jumping discharge | seppur.2023.123547 | 10.1016/j.seppur.2023.123547 | **NO** | needs_review | NO (empty) | **wrong_source** | needs_human_decision | Membrane separation mechanism, not PDA |
| M-05 | enrichment/polydopamine-coating.json | mechanisms["油滴捕获的'捕获-聚并-脱离'机制"] | Oil capture mechanism | seppur.2023.123547 | 10.1016/j.seppur.2023.123547 | NO | needs_review | NO (empty) | **wrong_source** | needs_human_decision | Oil-water separation membrane, not PDA |
| M-06 | enrichment/polydopamine-coating.json | mechanisms["制备方法概述"] | Preparation method overview | seppur.2023.123547 | 10.1016/j.seppur.2023.123547 | NO | needs_review | NO (empty) | **wrong_source** | needs_human_decision | Electrospun PET membrane, not PDA |
| M-07 | enrichment/polydopamine-coating.json | mechanisms["特殊润湿性分类"] | Special wettability classification | acsami.0c18794 | 10.1021/acsami.0c18794 | **NO** | needs_review | NO (empty) | **wrong_source** | needs_human_decision | Superhydrophobic membrane review, not PDA |
| M-08 | enrichment/polydopamine-coating.json | mechanisms["荷叶效应仿生原理"] | Lotus leaf effect | acsami.0c18794 | 10.1021/acsami.0c18794 | NO | needs_review | NO (empty) | **wrong_source** | needs_human_decision | General superhydrophobic review |
| M-09 | enrichment/polydopamine-coating.json | mechanisms["超疏水抗菌表面'双重保险'原理"] | Superhydrophobic antibacterial dual insurance | jxhg.20201035 | 10.13550/j.jxhg.20201035 | **NO** | needs_review | NO (empty) | **wrong_source** | needs_human_decision | Antibacterial coating review, not PDA-specific |
| M-10 | enrichment/polydopamine-coating.json | mechanisms["吸附机制 — 配位螯合"] | Adsorption mechanism — coordination chelation | patent (CN114887602A) | null | **NO (PDF missing)** | needs_review | NO (empty) | **missing_pdf** | missing_pdf | Source is missing patent |
| M-11 | enrichment/polydopamine-coating.json | mechanisms["PDA吸附机制-姜黄素"] | PDA adsorption - curcumin | patent (CN115040496A) | null | YES (patent exists locally) | needs_review | NO (empty) | **partial** | add_quote_locator | Patent exists but mechanism description is null; needs content verification |
| M-12 | enrichment/polydopamine-coating.json | mechanisms["PDA吸附机制-番茄红素"] | PDA adsorption - lycopene | patent (CN115040496A) | null | YES | needs_review | NO (empty) | **partial** | add_quote_locator | Same as above |
| M-13 | enrichment/polydopamine-coating.json | mechanisms["吸附机制"] | Adsorption mechanism (surface complexation) | 2021-Shi | 10.1016/j.apsusc.2020.148379 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | PDF exists; mechanism description is "surface complexation and ion exchange" but causal_chain empty |
| M-14 | enrichment/polydopamine-coating.json | mechanisms["pHpzc和pH影响"] | pHpzc and pH effect | 2022-Yan | 10.1016/j.apsusc.2022.154338 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | pHpzc=4.32 confirmed in PDF |
| M-15 | enrichment/polydopamine-coating.json | mechanisms["吸附机理六重协同"] | Six-fold synergistic mechanism | 2022-Yan | 10.1016/j.apsusc.2022.154338 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | Needs verification against PDF Section 3 |
| M-16 | enrichment/polydopamine-coating.json | mechanisms["吸附机制-酚羟基参与"] | Phenolic hydroxyl participation | 2021-Xiao | 10.1016/j.cej.2020.127837 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | PDF exists; XPS data likely present |
| M-17 | enrichment/polydopamine-coating.json | mechanisms["pH对吸附的影响机制"] | pH effect on adsorption | CN113244898A | null | YES (scanned) | needs_review | NO (empty) | **needs_human_decision** | needs_human_decision | Scanned patent |
| M-18 | enrichment/polydopamine-coating.json | mechanisms["XPS分析-吸附机理"] | XPS analysis mechanism | 2021-Zhang | 10.1016/j.jhazmat.2020.124347 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | PDF exists |
| M-19 | enrichment/polydopamine-coating.json | mechanisms["吸附活性基团协同"] | Active group synergy | 2021-Zhang | 10.1016/j.jhazmat.2020.124347 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | |
| M-20 | enrichment/polydopamine-coating.json | mechanisms["XPS吸附机理"] | XPS adsorption mechanism | 2022-Godiya | 10.1016/j.jhazmat.2022.129112 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | |
| M-21 | enrichment/polydopamine-coating.json | mechanisms["Cr(VI)吸附机制总结"] | Cr(VI) adsorption mechanism | 2024-Yuan | 10.1016/j.seppur.2024.127979 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | |
| M-22 | enrichment/polydopamine-coating.json | mechanisms["Cu(II)吸附机制总结"] | Cu(II) adsorption mechanism | 2024-Yuan | 10.1016/j.seppur.2024.127979 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | |
| M-23 | enrichment/polydopamine-coating.json | mechanisms["CR吸附机制总结"] | CR adsorption mechanism | 2024-Yuan | 10.1016/j.seppur.2024.127979 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | |
| M-24 | enrichment/polydopamine-coating.json | mechanisms["吸附机理-pH依赖性"] | pH-dependent mechanism | CN113244898A | null | YES (scanned) | needs_review | NO (empty) | **needs_human_decision** | needs_human_decision | Scanned patent |
| M-25 | enrichment/polydopamine-coating.json | mechanisms["吸附机制类型"] | Mechanism type (physical) | 2021-Foroutan | 10.1016/j.jece.2021.105709 | YES | needs_review | NO (empty) | **partial** | add_quote_locator | |

**Mechanism summary:** 56 of 57 mechanisms have empty causal_chains and needs_review verification. Only 1 (PDA π-π mechanism) has a populated causal_chain. ~10 mechanisms appear to be from unrelated prototypes (hydrophobic membranes, antibacterial coatings) — these are **wrong_source** candidates.

---

## Narrative Audit

| item_id | target_json | field_path | source_file | pdf_exists | evidence_label | recommended_action | notes |
|---------|-------------|------------|-------------|------------|----------------|-------------------|-------|
| N-01 | polydopamine-coating.json | narrative.entries[0] | 2022-Li-hydrophobic-separation-membrane-porous-review | YES (2 PDFs in library) | **partial** | keep_soft | Narrative references extraction JSON, not original PDF. Content is about hydrophobic PVDF membranes — may be misplaced for PDA prototype. |
| N-02 | polydopamine-coating.json | narrative.entries[1] | 2023-景-超疏水-油水分离-膜-综述 | YES (PDF in library) | **partial** | keep_soft | Oil-water separation membrane review — same concern about relevance to PDA coating |
| N-03 | polydopamine-coating.json | narrative.entries[2] | 2021-高-超疏水-油水分离-综述-研究进展 | YES (PDF in library) | **partial** | keep_soft | Superhydrophobic antibacterial review — relevance to PDA coating unclear |
| N-04 | polydopamine-coating.json | narrative.entries[3] | 2022-CN115040496A-聚多巴胺-壳聚糖-吸附 | YES (patent in library) | **partial** | keep_soft | PDA hollow mesoporous nanoparticles for fat-soluble pigments — relevant to PDA |
| N-05 | polydopamine-coating.json | narrative.entries[4] | 2022-Yan-polydopamine-magnetic-dye-adsorption | YES | **partial** | keep_soft | PDA/MGO/CA-CD for cationic dyes — relevant |
| N-06 | polydopamine-coating.json | narrative.entries[5] | 2021-CN113244898A-polydopamine-kaolin-lead | YES (scanned) | **needs_human_decision** | needs_human_decision | Scanned patent, cannot verify text |
| N-07 | polydopamine-coating.json | narrative.entries[6] | 2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth | YES | **partial** | keep_soft | Chitosan aerogel for Gd(III) — relevant |
| N-08 | polydopamine-coating.json | narrative.entries[7] | 2024-Yuan-tannic-acid-cellulose-aerogel | YES | **partial** | keep_soft | CNF-TA-PMMT-PEI for Cr(VI)/Cu(II)/CR — relevant |
| N-09 | polydopamine-coating.json | narrative.entries[8] | 2022-CN114570339A-polydopamine-uranium | YES (scanned) | **needs_human_decision** | needs_human_decision | Scanned patent |
| N-10 | polydopamine-coating.json | narrative.entries[9] | 2023-Jin-polydopamine-chitosan-carmine | YES | **partial** | keep_soft | PDA/DCS for carmine — relevant |

---

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---------|-------------|------------|---------------|-----------|-------------|-------------|---------|-------|----------------|-------|
| B-01 | polydopamine-coating.json | mechanisms["PDA吸附机制补充"].causal_chain.boundary_conditions[0] | **soft_boundary** | Alkaline conditions: catechol oxidizes to quinone, metal coordination lost | PDA loses metal adsorption ability at high pH | 2021-Lei (inferred) | null | null | **inferred_only** | Basis=llm_inferred, no PDF quote. Chemically plausible but needs experimental citation. |
| B-02 | polydopamine-coating.json | mechanisms["PDA吸附机制补充"].causal_chain.boundary_conditions[1] | **soft_boundary** | Weakly acidic: DOPA self-polymerization too slow, coating hard to form | PDA coating cannot be formed below certain pH | CM-002: catechol-low-ph-suppression | null | null | **inferred_only** | Basis=llm_inferred, source_asset referenced but no PDF quote. Known chemistry but needs citation. |
| B-03 | polydopamine-coating.json | performance_data[0-4] | **hard_do_not** | CN114887602A patent PDF missing | 4 performance claims (159.8, 91.2, 12.6, 110, 143.4 mg/g) cannot be verified | N/A | N/A | N/A | **missing_pdf** | Must locate original patent PDF before any design decisions based on these values |
| B-04 | polydopamine-coating.json | performance_data[17-19] | **hard_do_not** | CN113244898A scanned patent | Pb2+ removal claims (96.31%, 95.68%, dose/concentration effects) unverifiable via text | CN113244898A (scanned) | N/A | N/A | **needs_human_decision** | Scanned patent requires OCR or visual reading to verify |
| B-05 | polydopamine-coating.json | performance_data[26-32] | **hard_do_not** | CN114570339A scanned patent | 7 U(VI) adsorption claims (96.5, 103, 81.25, 132.25 mg/g etc.) unverifiable | CN114570339A (scanned) | N/A | N/A | **needs_human_decision** | Scanned patent requires OCR or visual reading |
| B-06 | polydopamine-coating.json | performance_data[42] | **soft_boundary** | Ge(IV) 0.33 mmol/g at pH 6 | Value not explicitly stated in text; may be figure estimate | 2023-Xiang | 图8 | "适宜的溶液pH为6左右" | **partial** | pH 6 confirmed optimal, but 0.33 mmol/g value not in text. Kinetics shows 0.127 mmol/g. |
| B-07 | enrichment/polydopamine-coating.json | mechanisms["Teflon AF 2400"] through mechanisms["无机-有机复合策略优势"] (~10 mechanisms) | **knowledge_gap** | Mechanisms from unrelated prototypes (hydrophobic membranes, antibacterial) | If used in PDA design decisions, would be fundamentally wrong | Various (polym14245439, acsami.0c18794, seppur.2023.123547, jxhg.20201035) | N/A | N/A | **wrong_source** | These mechanisms belong to different prototypes and should not inform PDA coating design |

---

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---------------|-----------------|-------|-------------------|
| CN114887602A (patent) | performance_data[0-3], mechanisms["吸附机制 — 配位螯合"] | **PDF missing** from library; extraction JSON is empty (0 records) | Locate original patent PDF at CNKI or patent database; re-extract |
| 10.3390/polym14245439 (Li 2022 review) | mechanisms["Teflon AF 2400"], ["疏水改性三大方法"], ["PVDF-co-HFP/POTS"], ["PVDF-co-HFP/F-POSS"], ["Cassie-Baxter"], ["P(VDF-co-CTFE)"] | **Wrong prototype** — hydrophobic PVDF membrane review, not PDA coating | Review whether these mechanisms belong in polydopamine-coating; consider moving to a membrane-related prototype |
| 10.1021/acsami.0c18794 (ACS AMI review) | mechanisms["特殊润湿性"], ["荷叶效应"], ["荷叶上下表面"], ["壁虎脚"], ["玫瑰花瓣"], ["浸涂法"], ["溶胶-凝胶"], ["Table 1"], ["TiO2光催化"], ["CeO2"], ["pH响应PDMS"], ["双刺激UV"] | **Wrong prototype** — superhydrophobic membrane/surface review | Same as above |
| 10.1016/j.seppur.2023.123547 | mechanisms["水滴排液"], ["油滴捕获"], ["制备方法"] | **Wrong prototype** — oil-water separation membrane | Same |
| 10.16490/j.cnki.issn.1001-3660.2023.02.015 | mechanisms["荷叶超疏水仿生"], ["超浸润膜分离"], ["超疏水/超亲油"], ["超亲水/水下超疏油"], ["TiO2纳米线"], ["PVDF/PDMS"], ["F-SiO2"], ["pH响应PMMA"], ["热响应PNIPAAm"], ["超浸润膜四大类型"] | **Wrong prototype** — Chinese membrane review | Same |
| 10.13550/j.jxhg.20201035 | mechanisms["超疏水抗菌"], ["分类体系"], ["铜基"], ["铜纳米粒子"], ["CuO/SiO2"], ["纳米Ag棉织物"], ["中空多孔碳球"], ["含氟季铵盐"], ["纳米Ag/硅烷"], ["树枝状纳米银"], ["Cu纳米线"], ["ZIF-8/PVDF"], ["pH响应型抗菌"], ["超疏水医用纱布"], ["多巴胺黏附"], ["未来发展方向"], ["无机-有机复合"] | **Wrong prototype** — antibacterial coating review | Same |
| CN113244898A (scanned patent) | performance_data[17-19], mechanisms["pH对吸附"], ["pH依赖性"] | **Scanned PDF**, no text layer — cannot verify claims | OCR or visual reading needed |
| CN114570339A (scanned patent) | performance_data[26-32] | **Scanned PDF**, no text layer — cannot verify 7 claims | OCR or visual reading needed |
| 10.13373/j.cnki.cjrm.XY21060036 (Xiang 2023) | performance_data[42] | Value ~0.33 mmol/g not explicitly in text; may be figure estimate | Verify against Table 3 isotherm parameters or Figure 8 y-axis |

---

## Verification Statistics

| Category | Count | % |
|----------|-------|---|
| **supported** (PDF quote confirmed) | 28 | 62% |
| **partial** (value found but locator/quote incomplete) | 2 | 4% |
| **needs_human_decision** (scanned PDF or ambiguous) | 12 | 27% |
| **missing_pdf** (source PDF not in library) | 4 | 9% |
| **wrong_source** (mechanism from unrelated prototype) | ~47 mechanisms | 82% of mechanisms |
| **needs_review** (causal_chain empty) | 56 mechanisms | 98% of mechanisms |

---

## Key Recommendations for Codex

1. **Critical: Locate CN114887602A patent PDF** — 4 performance claims depend on it; extraction failed
2. **Critical: Audit mechanism relevance** — ~47 mechanisms (from 5 review papers) appear to belong to hydrophobic membrane/antibacterial prototypes, not PDA coating. These should be relocated or removed.
3. **Scanned patents need OCR** — CN113244898A (3 claims) and CN114570339A (7 claims) need visual reading
4. **Ge(IV) value needs confirmation** — 0.33 mmol/g not explicitly stated; verify against Table 3
5. **Boundary conditions are inferred** — Both soft_boundary candidates have basis=llm_inferred, no PDF quotes
6. **Most enrichment mechanisms are shell-only** — 56/57 have empty causal_chains; only the PDA π-π mechanism has populated chain
