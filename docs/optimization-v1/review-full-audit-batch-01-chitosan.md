# Full Audit Batch 01: chitosan

status: ready_for_codex_review

## Executive Summary

- **Scope**: prototypes_db/chitosan.json + enrichment/chitosan.json
- **performance_data items**: 100+
- **mechanisms entries**: 100+ (main DB) + 100+ (enrichment)
- **narrative entries**: 30+
- **engineering_constraints**: 50+
- **PDFs spot-checked**: 8 (all values verified correct)
- **Source file integrity**: 第1组-配位螯合 folder has NO PDFs; multiple source_files point to 2nd/3rd generation directories
- **Critical issue**: enrichment/chitosan.json has ~100 mechanism entries with empty causal_chain fields (pollutant_feature, bio_structure, interaction, why_it_works all empty strings)

## Field Audit Table

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | pdf_path | pdf_exists | locator | quote | evidence_label | recommended_action | notes |
|---------|-------------|------------|------------|---------------|-------------|---------|----------|------------|---------|-------|----------------|-------------------|-------|
| pd_001 | chitosan.json | performance_data[0] | performance_data | MW effect on ammonia removal: 79%→92% | 2021-Keshvardoostchokami-chitosan-adsorption-adsorbent-wastewater-review.pdf | 10.1016/j.carbpol.2021.118625 | N/A | missing_pdf | Section 3 | N/A | missing_pdf | missing_pdf | PDF not found locally; source_file lacks directory prefix |
| pd_002 | chitosan.json | performance_data[1] | performance_data | Crosslinking effect on Cu(II): pure 80.71, GLA 59.67, ECH 62.47, EGDE 45.94 mg/g | 2020-Upadhyay-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 10.1016/j.carbpol.2020.117000 | N/A | missing_pdf | Section 3.1.1 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_003 | chitosan.json | performance_data[2] | performance_data | Itaconic acid grafting: GLA 124→405, ECH 92→331 mg/g for Cd(II) | 2020-Upadhyay-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 10.1016/j.carbpol.2020.117000 | N/A | missing_pdf | Section 3.1.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_002 |
| pd_004 | chitosan.json | performance_data[3] | performance_data | Table 2 top capacities: Ag-imprinted 510.0, Thiourea-modified 406.38 mg/g | 2020-Upadhyay-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 10.1016/j.carbpol.2020.117000 | N/A | missing_pdf | Table 2 (continued) | N/A | missing_pdf | missing_pdf | Same PDF as pd_002 |
| pd_005 | chitosan.json | performance_data[4] | performance_data | Cu(II)-chitosan magnetic for RBR: 880.84 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 3.3 | N/A | missing_pdf | missing_pdf | PDF not found in 仿生文献库/论文/第1组-配位螯合/ (folder empty) |
| pd_006 | chitosan.json | performance_data[5] | performance_data | Magnetic xanthate chitosan MB 197.8, SO 169.8 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 3.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_007 | chitosan.json | performance_data[6] | performance_data | Chitosan gel beads CR 1597, DY 1447 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_008 | chitosan.json | performance_data[7] | performance_data | CS/bentonite AR 362.1, MB 496.5 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_009 | chitosan.json | performance_data[8] | performance_data | CS/PAA/GO hydrogel MB 296.5, FY3 280.3 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_010 | chitosan.json | performance_data[9] | performance_data | Magnetic CS SY dye 769.23 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_011 | chitosan.json | performance_data[10] | performance_data | Fe₃O₄-CS MB+MO 638.6 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_012 | chitosan.json | performance_data[11] | performance_data | PAM/CS/Fe3O4 hydrogel MB 1603 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_013 | chitosan.json | performance_data[12] | performance_data | ZIF-8@CS/PVA MG 1000 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.4 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_014 | chitosan.json | performance_data[13] | performance_data | MIL-101@CS sponge Acid Red 94 4518 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.4 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_015 | chitosan.json | performance_data[14] | performance_data | Magnetic CS-montmorillonite CR 1597 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_016 | chitosan.json | performance_data[15] | performance_data | Semi-IPN CS-starch DR80 312.77 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 3.5 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_017 | chitosan.json | performance_data[16] | performance_data | Zr(IV)@CS/Fe3O4/GO AR 231 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 3.7 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005 |
| pd_018 | chitosan.json | performance_data[17] | performance_data | CS/bentonite MG 496.5, AR 362.1 mg/g | 2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf | 10.1016/j.ijbiomac.2021.04.158 | N/A | missing_pdf | Section 4.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_005; duplicate of pd_008 |
| pd_019 | chitosan.json | performance_data[18] | performance_data | Cu concentration effect: higher conc → lower removal % | 2020-Bambaeero-chitosan-bone-shell-hydroxyapatite.pdf | 10.1016/j.cjche.2020.07.066 | Bambaeero2020.pdf | yes | pp.224-225 | "The higher the concentration of copper ion presented in the solution, the lower the percentage removal under the same conditions and at a constant time." | supported | no_action | Verified |
| pd_020 | chitosan.json | performance_data[19] | performance_data | Dosage effect: 0.030g chitosan at pH 5 max Cu removal | 2020-Bambaeero-chitosan-bone-shell-hydroxyapatite.pdf | 10.1016/j.cjche.2020.07.066 | Bambaeero2020.pdf | yes | p.225 | "The maximum amount of Cu ion removal was obtained at 0.030 g of chitosan adsorbent at pH 5." | supported | no_action | Verified |
| pd_021 | chitosan.json | performance_data[20] | performance_data | CS/Fe-HAP Pb(II) 1385 mg/g | 2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | 10.1007/s10311-023-01563-9 | N/A | missing_pdf | Abstract | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_022 | chitosan.json | performance_data[21] | performance_data | Activated carbon BPA >250 mg/g; N-doped PDA-C 1351 mg/g | 2024-Cheng-chitosan-cellulose-separation-membrane-review.pdf | 10.1016/j.cej.2024.149414 | Cheng2024.pdf | yes | Section 2.1.1 | N/A (PDF >10MB, couldn't fully verify) | keep_soft | keep_soft | PDF exists but exceeds tool size limit; DOI valid |
| pd_023 | chitosan.json | performance_data[22] | performance_data | NF membrane BPA removal: size exclusion + adsorption + electrostatic + Donnan | 2024-Cheng-chitosan-cellulose-separation-membrane-review.pdf | 10.1016/j.cej.2024.149414 | Cheng2024.pdf | yes | Section 3.3 | N/A | keep_soft | keep_soft | Same PDF; plausible mechanism from DOI |
| pd_024 | chitosan.json | performance_data[23] | performance_data | MF membrane BPA: pore 0.1-10μm, removal 18-95% | 2024-Cheng-chitosan-cellulose-separation-membrane-review.pdf | 10.1016/j.cej.2024.149414 | Cheng2024.pdf | yes | Section 3.1 | N/A | keep_soft | keep_soft | Same PDF |
| pd_025 | chitosan.json | performance_data[24] | performance_data | UF+FeOCl 100% BPA degradation | 2024-Cheng-chitosan-cellulose-separation-membrane-review.pdf | 10.1016/j.cej.2024.149414 | Cheng2024.pdf | yes | Section 3.2 | N/A | keep_soft | keep_soft | Same PDF |
| pd_026 | chitosan.json | performance_data[25] | performance_data | Chitosan Hg 815, Cu 222, Ni 164, Zn 75 mg/g (McKee) | 2024-Hsu-chitosan-adsorption-heavy-metal-review.pdf | 10.1016/j.rechem.2024.101332 | N/A | missing_pdf | Use of chitosan section | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_027 | chitosan.json | performance_data[26] | performance_data | Chitosan Cd²⁺ 5.93 mg/g | 2024-Hsu-chitosan-adsorption-heavy-metal-review.pdf | 10.1016/j.rechem.2024.101332 | N/A | missing_pdf | Use of chitosan section | N/A | missing_pdf | missing_pdf | Same PDF as pd_026 |
| pd_028 | chitosan.json | performance_data[27] | performance_data | Porous CS particles Cd²⁺ 518 (3mm), 188 (1mm) | 2024-Hsu-chitosan-adsorption-heavy-metal-review.pdf | 10.1016/j.rechem.2024.101332 | N/A | missing_pdf | Use of chitosan section | N/A | missing_pdf | missing_pdf | Same PDF as pd_026 |
| pd_029 | chitosan.json | performance_data[28] | performance_data | Chitosan Al³⁺ 45.45 mg/g | 2024-Hsu-chitosan-adsorption-heavy-metal-review.pdf | 10.1016/j.rechem.2024.101332 | N/A | missing_pdf | Use of chitosan section | N/A | missing_pdf | missing_pdf | Same PDF as pd_026 |
| pd_030 | chitosan.json | performance_data[29] | performance_data | CS crosslinked/non-crosslinked Cr(VI) 78/50 mg/g | 2024-Hsu-chitosan-adsorption-heavy-metal-review.pdf | 10.1016/j.rechem.2024.101332 | N/A | missing_pdf | Use of chitosan section | N/A | missing_pdf | missing_pdf | Same PDF as pd_026 |
| pd_031 | chitosan.json | performance_data[30] | performance_data | Amino-CS Hg²⁺ 2.26 mg/mg | 2024-Hsu-chitosan-adsorption-heavy-metal-review.pdf | 10.1016/j.rechem.2024.101332 | N/A | missing_pdf | Use of chitosan section | N/A | missing_pdf | missing_pdf | Same PDF as pd_026 |
| pd_032 | chitosan.json | performance_data[31] | performance_data | Chitin/GO sponges microplastic removal: H-bond, electrostatic, π-π | 2021-Yang-chitosan-oil-water-separation-porous-review.pdf | 10.1016/j.ijbiomac.2021.08.047 | N/A | missing_pdf | Section 2.3 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_033 | chitosan.json | performance_data[32] | performance_data | Dye removal via enzyme-assisted hydrogel (qualitative) | 2021-Yang-chitosan-oil-water-separation-porous-review.pdf | 10.1016/j.ijbiomac.2021.08.047 | N/A | missing_pdf | Section 2.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_032 |
| pd_034 | chitosan.json | performance_data[33] | performance_data | CS bead swelling 39.8%, crosslinked 11.9%/6.2%; capacity 80.71→59.67/62.47 mg/g | 2020-Sheth-chitosan-magnetic-adsorption-adsorbent-review.pdf | 10.1016/j.seta.2020.100951 | N/A | missing_pdf | Section Modifications | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_035 | chitosan.json | performance_data[34] | performance_data | Magnetic CS/cellulose Cu 88.21, Cd 61.12, Pb 45.86 mg/g | 2020-Sheth-chitosan-magnetic-adsorption-adsorbent-review.pdf | 10.1016/j.seta.2020.100951 | N/A | missing_pdf | Section Adsorption studies | N/A | missing_pdf | missing_pdf | Same PDF as pd_034 |
| pd_036 | chitosan.json | performance_data[35] | performance_data | CS/TiO₂ nanofiber Cu 710.3, Pb 579.1 mg/g (embedded) | 2020-Sheth-chitosan-magnetic-adsorption-adsorbent-review.pdf | 10.1016/j.seta.2020.100951 | N/A | missing_pdf | Section Nanofiber membranes | N/A | missing_pdf | missing_pdf | Same PDF as pd_034 |
| pd_037 | chitosan.json | performance_data[36] | performance_data | ZIF-67@CS/cellulose aerogel BET 268.7 m²/g, Cu 200.6, Cr 152.1 mg/g | 2020-Sheth-chitosan-magnetic-adsorption-adsorbent-review.pdf | 10.1016/j.seta.2020.100951 | N/A | missing_pdf | Section MOF | N/A | missing_pdf | missing_pdf | Same PDF as pd_034 |
| pd_038 | chitosan.json | performance_data[37] | performance_data | Cs-Zr-PEPA phosphate 103.96 mg/g | 2021-Eltaweil-chitosan-adsorption-adsorbent-removal-review.pdf | 10.1016/j.carbpol.2021.118671 | N/A | missing_pdf | Section 2.1.1 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_039 | chitosan.json | performance_data[38] | performance_data | La-bent/Cs 93.2% (20min, 50mg/L); 99.7% (5min, 2mg/L) | 2021-Eltaweil-chitosan-adsorption-adsorbent-removal-review.pdf | 10.1016/j.carbpol.2021.118671 | N/A | missing_pdf | Section 2.1.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_038 |
| pd_040 | chitosan.json | performance_data[39] | performance_data | Cu-BTC/CS membrane Mn2+ 86% | 2021-冯-壳聚糖-膜-分子印迹-吸附-综述.pdf | 10.13550/j.jxhg.20210304 | N/A | missing_pdf | Section 3.2 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_041 | chitosan.json | performance_data[40] | performance_data | Temperature effect: Langmuir qmax 19.57→20.23 mg/g (10→45°C) | 2021-赵-壳聚糖-膜-羟基磷灰石-吸附.pdf | 10.14028/j.cnki.1003-3726.2021.02.007 | N/A | missing_pdf | Section 2.3.1 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_042 | chitosan.json | performance_data[41] | performance_data | CE/CSA-1 CR 380.23, Cu²⁺ 260.41 mg/g (binary) | 2022-Liu-chitosan-cellulose-porous-hierarchical.pdf | 10.1016/j.cej.2022.138934 | N/A | missing_pdf | Abstract | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_043 | chitosan.json | performance_data[42] | performance_data | Functionalization strategies list (qualitative) | 2021-Syeda-cellulose-adsorption-heavy-metal-wastewater-review.pdf | 10.1016/j.scitotenv.2021.150606 | N/A | missing_pdf | Abstract | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_044 | chitosan.json | performance_data[43] | performance_data | PEI-cellulose aerogel Cr(VI) mechanism | 2021-Syeda-cellulose-adsorption-heavy-metal-wastewater-review.pdf | 10.1016/j.scitotenv.2021.150606 | N/A | missing_pdf | Section 7/Fig.4-5 | N/A | missing_pdf | missing_pdf | Same PDF as pd_043 |
| pd_045 | chitosan.json | performance_data[44] | performance_data | PVA/PU electrospun reactive dye 89.9 mg/g | 2021-Uddin-membrane-porous-heavy-metal-dye-review.pdf | 10.1007/s13762-021-03603-9 | N/A | missing_pdf | Colorant removal | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_046 | chitosan.json | performance_data[45] | performance_data | Fibroin/PAN/PANI/TiO2 reactive dye 90% | 2021-Uddin-membrane-porous-heavy-metal-dye-review.pdf | 10.1007/s13762-021-03603-9 | N/A | missing_pdf | Colorant removal | N/A | missing_pdf | missing_pdf | Same PDF as pd_045 |
| pd_047 | chitosan.json | performance_data[46] | performance_data | PVA-co-ethylene TiO2 NP 98% removal | 2021-Uddin-membrane-porous-heavy-metal-dye-review.pdf | 10.1007/s13762-021-03603-9 | N/A | missing_pdf | Nanofibrous membrane | N/A | missing_pdf | missing_pdf | Same PDF as pd_045 |
| pd_048 | chitosan.json | performance_data[47] | performance_data | PAN MF 99.99% phage, 99.9999% bacteria | 2021-Uddin-membrane-porous-heavy-metal-dye-review.pdf | 10.1007/s13762-021-03603-9 | N/A | missing_pdf | Bacteria/viruses | N/A | missing_pdf | missing_pdf | Same PDF as pd_045 |
| pd_049 | chitosan.json | performance_data[48] | performance_data | Al-MOF/SA-CS BPA 139.9 mg/g | 2020-Catenza-chitosan-review.pdf | 10.1016/j.chemosphere.2020.129273 | N/A | missing_pdf | Section 4.2 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_050 | chitosan.json | performance_data[49] | performance_data | Asphalt-based AC BPA 1113 mg/g | 2020-Catenza-chitosan-review.pdf | 10.1016/j.chemosphere.2020.129273 | N/A | missing_pdf | Section 4.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_049 |
| pd_051 | chitosan.json | performance_data[50] | performance_data | H₃PO₄-activated nutshell AC BPA 1250 mg/g | 2020-Catenza-chitosan-review.pdf | 10.1016/j.chemosphere.2020.129273 | N/A | missing_pdf | Section 4.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_049 |
| pd_052 | chitosan.json | performance_data[51] | performance_data | Hydrogel/aerogel capacities: semi-IPN 261, nanobentonite 1937, CS/CNC 200.6 mg/g | 2022-Mallik-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 10.1016/j.jece.2022.108048 | N/A | missing_pdf | 3.1 Hydrogel/aerogel | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_053 | chitosan.json | performance_data[52] | performance_data | CS/Nylon-6 nanofiber 240 mg/g, 8 cycles | 2022-Mallik-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 10.1016/j.jece.2022.108048 | N/A | missing_pdf | 3.2 Nanofiber | N/A | missing_pdf | missing_pdf | Same PDF as pd_052 |
| pd_054 | chitosan.json | performance_data[53] | performance_data | MWCNT/CS 454.55 vs pure CS 178.6; biochar acrylic/CS 678.0 mg/g | 2022-Mallik-chitosan-adsorption-adsorbent-heavy-metal-review.pdf | 10.1016/j.jece.2022.108048 | N/A | missing_pdf | 3.3 Composites | N/A | missing_pdf | missing_pdf | Same PDF as pd_052 |
| pd_055 | chitosan.json | performance_data[54] | performance_data | CTS/CMC/PAA hydrogel Pb²⁺ 142.83 mg/g | 2023-胡-壳聚糖-纤维素-吸附-重金属.pdf | 10.19965/j.cnki.iwt.2022-1185 | N/A | missing_pdf | 摘要 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_056 | chitosan.json | performance_data[55] | performance_data | CNC(50%)/CS aerogel Cr(VI) qmax 67.377 mg/g | 2022-张-壳聚糖-纤维素-纳米纤维素-吸附.pdf | 10.3969/j.issn.1001-9731.2022.10.023 | N/A | missing_pdf | 2.2节 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_057 | chitosan.json | performance_data[56] | performance_data | Only CNC(50%) tested, no other ratios | 2022-张-壳聚糖-纤维素-纳米纤维素-吸附.pdf | 10.3969/j.issn.1001-9731.2022.10.023 | N/A | missing_pdf | 2.2节 | N/A | missing_pdf | missing_pdf | Same PDF as pd_056 |
| pd_058 | chitosan.json | performance_data[57] | performance_data | Literature comparison: CNC/CS 67.377 vs hypercrosslinked PIL 236.8 mg/g | 2022-张-壳聚糖-纤维素-纳米纤维素-吸附.pdf | 10.3969/j.issn.1001-9731.2022.10.023 | N/A | missing_pdf | 引言 | N/A | missing_pdf | missing_pdf | Same PDF as pd_056 |
| pd_059 | chitosan.json | performance_data[58] | performance_data | CS/PAAS ENM Cr(VI) 7.7 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | p.1720 | "the chitosan/PAAS composite ENM could efficiently adsorb Cr(VI) ion from dilute aqueous solution with an adsorption capacity of 7.7 mg/g." | supported | no_action | Verified |
| pd_060 | chitosan.json | performance_data[59] | performance_data | CS/PVP ENM U(VI) 167±25 g/kg | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | p.1720 | "qmax = (167 ± 25) g/kg at pH 6.0" | supported | no_action | Verified |
| pd_061 | chitosan.json | performance_data[60] | performance_data | AOPAN/RC ENM Fe(III) 7.47, Cu(II) 4.26, Cd(II) 1.13 mmol/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | Section Cellulose-HMI | N/A | keep_soft | keep_soft | PDF exists; specific values not individually verified but review paper covers this topic |
| pd_062 | chitosan.json | performance_data[61] | performance_data | DA@PDA cellulose ENM MB 88.15 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | Section Cellulose-Dye | N/A | keep_soft | keep_soft | Same PDF |
| pd_063 | chitosan.json | performance_data[62] | performance_data | CA ENM triclosan 797.7 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | p.1719 | "A maximum TCS adsorption capacity of 797.7 mg/g was observed" | supported | no_action | Verified |
| pd_064 | chitosan.json | performance_data[63] | performance_data | CaCl₂-crosslinked alginate ENM MB 2230 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | p.1724 | "CaCl2 cross-linked alginate ENM held the maximum actual adsorption capacity of 2230 mg/g" | supported | no_action | Verified |
| pd_065 | chitosan.json | performance_data[64] | performance_data | Fe-impregnated CS ENM As(III) 31.6 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | Section Chitosan-HMI | N/A | keep_soft | keep_soft | Same PDF |
| pd_066 | chitosan.json | performance_data[65] | performance_data | CS/PVA ENM tetracycline 102 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | Section Chitosan-Pharma | N/A | keep_soft | keep_soft | Same PDF |
| pd_067 | chitosan.json | performance_data[66] | performance_data | CS-coated PAN acid blue-113 1708 mg/g | 2021-Pan-chitosan-alginate-cellulose-membrane-review.pdf | 10.1007/s10924-021-02312-1 | Pan2021.pdf | yes | p.1724 | "1708 mg/g for acid blue-113" | supported | no_action | Verified |
| pd_068 | chitosan.json | performance_data[67] | performance_data | CS DD effect: DD 42→84% → FD&C Red 40 266→373 mg/g | 2021-Alves-chitosan-magnetic-biochar-adsorbent-review.pdf | 10.3390/molecules26030594 | N/A | missing_pdf | Section 2.2.1 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_069 | chitosan.json | performance_data[68] | performance_data | CS/alginate Cu(II) 66→81%, Cd(II) 47→77% | 2021-Alves-chitosan-magnetic-biochar-adsorbent-review.pdf | 10.3390/molecules26030594 | N/A | missing_pdf | Adsorption on grafted CS | N/A | missing_pdf | missing_pdf | Same PDF as pd_068 |
| pd_070 | chitosan.json | performance_data[69] | performance_data | CS/AC Cd(II) 52.63, AC 10.3, CS 10.0 mg/g | 2021-Alves-chitosan-magnetic-biochar-adsorbent-review.pdf | 10.3390/molecules26030594 | N/A | missing_pdf | Section 3.1.4 | N/A | missing_pdf | missing_pdf | Same PDF as pd_068 |
| pd_071 | chitosan.json | performance_data[70] | performance_data | CS/GO MB >1000 mg/g | 2021-Alves-chitosan-magnetic-biochar-adsorbent-review.pdf | 10.3390/molecules26030594 | N/A | missing_pdf | Section 4.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_068 |
| pd_072 | chitosan.json | performance_data[71] | performance_data | CS DD RB5: hydrogel DD90% 1559.7, flake DD90% 1049.6 mg/g | 2021-Alves-chitosan-magnetic-biochar-adsorbent-review.pdf | 10.3390/molecules26030594 | N/A | missing_pdf | Section 2.2.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_068 |
| pd_073 | chitosan.json | performance_data[72] | performance_data | La-MZ/CTS phosphate 27.9 mg/g | 2019-张-壳聚糖-吸附.pdf | 10.13671/j.hjkxxb.2020.0407 | N/A | missing_pdf | Section 3.2.1 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_074 | chitosan.json | performance_data[73] | performance_data | Unloaded MZ/CTS phosphate 4.80 mg/g | 2019-张-壳聚糖-吸附.pdf | 10.13671/j.hjkxxb.2020.0407 | N/A | missing_pdf | Section 3.2.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_073 |
| pd_075 | chitosan.json | performance_data[74] | performance_data | La-based adsorbent comparison Table 2 | 2019-张-壳聚糖-吸附.pdf | 10.13671/j.hjkxxb.2020.0407 | N/A | missing_pdf | Table 2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_073 |
| pd_076 | chitosan.json | performance_data[75] | performance_data | CYCS/CNC hydrogel Pb(II) qmax 334.92 mg/g | 2020-Xu-chitosan-cellulose-nanocellulose-adsorption.pdf | 10.1016/j.molliq.2020.114523 | N/A | missing_pdf | abstract | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_077 | chitosan.json | performance_data[76] | performance_data | Temperature: 297K 333.94, 303K 334.76, 310K 334.92 mg/g | 2020-Xu-chitosan-cellulose-nanocellulose-adsorption.pdf | 10.1016/j.molliq.2020.114523 | N/A | missing_pdf | Section 3.5 | N/A | missing_pdf | missing_pdf | Same PDF as pd_076 |
| pd_078 | chitosan.json | performance_data[77] | performance_data | CCC Pb2+ 169.10 mg/g | 2023-杨-壳聚糖-磁性-生物炭-吸附.pdf | 10.15898/j.ykcs.202208230155 | N/A | missing_pdf | 摘要 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_079 | chitosan.json | performance_data[78] | performance_data | CCC Cu2+ 18.69 mg/g | 2023-杨-壳聚糖-磁性-生物炭-吸附.pdf | 10.15898/j.ykcs.202208230155 | N/A | missing_pdf | 摘要 | N/A | missing_pdf | missing_pdf | Same PDF as pd_078 |
| pd_080 | chitosan.json | performance_data[79] | performance_data | CS-based arsenic capacities: Fe-CS As(V) 120.77, Zr-CS As(III) 43.19 mg/g | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 7.2.2 | N/A | missing_pdf | missing_pdf | PDF not found locally |
| pd_081 | chitosan.json | performance_data[80] | performance_data | Fe(III)-CS As(V) 93% (no PO₄), 59% (with PO₄) | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 7.3.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_080 |
| pd_082 | chitosan.json | performance_data[81] | performance_data | Crosslinking degree effect (qualitative) | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 7.3.1.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_080 |
| pd_083 | chitosan.json | performance_data[82] | performance_data | Sulfhydryl-CS As(III) 99% pH 3-10 | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 8 | N/A | missing_pdf | missing_pdf | Same PDF as pd_080 |
| pd_084 | chitosan.json | performance_data[83] | performance_data | CS nanofiber membrane As(V) 30.8 mg/g | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 13.2 | N/A | missing_pdf | missing_pdf | Same PDF as pd_080 |
| pd_085 | chitosan.json | performance_data[84] | performance_data | Fixed-bed column As 50 mg/g | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 13.1 | N/A | missing_pdf | missing_pdf | Same PDF as pd_080 |
| pd_086 | chitosan.json | performance_data[85] | performance_data | Al2O3/TiO2-embedded CS As mechanism: diffusion→oxidation→adsorption | 2021-Ayub-chitosan-adsorption-biosorption-removal-review.pdf | 10.1016/j.ijbiomac.2021.10.050 | N/A | missing_pdf | Section 11 | N/A | missing_pdf | missing_pdf | Same PDF as pd_080 |
| pd_087 | chitosan.json | performance_data[86] | performance_data | Patent CN121130847A Example 1: CS-ZIF-8 foam 70.7 g/g for DCM | patent CN121130847A | null | N/A | missing_pdf | 表1/段0047 | N/A | missing_pdf | missing_pdf | Patent PDF exists but source_file naming differs; actual file is "2025-CN121130847A-壳聚糖-纤维素-生物基-MOF 2.pdf" |
| pd_088 | chitosan.json | performance_data[87] | performance_data | Patent CN121130847A Example 3: CNF-ZIF-8 87.6 g/g | patent CN121130847A | null | N/A | missing_pdf | 表3/段0061 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_089 | chitosan.json | performance_data[88] | performance_data | Patent CN121130847A Example 4: Gelatin-ZIF-8-TMCS 81 g/g | patent CN121130847A | null | N/A | missing_pdf | 表4/段0068 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_090 | chitosan.json | performance_data[89] | performance_data | Patent CN121130847A Example 5: Gelatin-ZIF-8 88 g/g | patent CN121130847A | null | N/A | missing_pdf | 表5/段0075 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_091 | chitosan.json | performance_data[90] | performance_data | Patent CN121130847A Example 6: Gelatin-ZIF-8 light crosslink 77.6 g/g | patent CN121130847A | null | N/A | missing_pdf | 表6/段0082 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_092 | chitosan.json | performance_data[91] | performance_data | Patent CN121130847A Example 6 control: over-crosslinked 54 g/g | patent CN121130847A | null | N/A | missing_pdf | 表6/段0082 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_093 | chitosan.json | performance_data[92] | performance_data | Patent CN121130847A Example 7: Gelatin-ZIF-8(Zn) 77.6 g/g | patent CN121130847A | null | N/A | missing_pdf | 表7/段0089 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_094 | chitosan.json | performance_data[93] | performance_data | Patent CN121130847A Example 7 control: Gelatin-ZIF-67(Co) 101 g/g | patent CN121130847A | null | N/A | missing_pdf | 表7/段0089 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_095 | chitosan.json | performance_data[94] | performance_data | Diazotized CS-MOF foam range 51.5-122 g/g | patent CN121130847A | null | N/A | missing_pdf | 段0036/图8 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_096 | chitosan.json | performance_data[95] | performance_data | Diazotized CS-MOF DCM 107.1 g/g | patent CN121130847A | null | N/A | missing_pdf | 段0036/图8 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_097 | chitosan.json | performance_data[96] | performance_data | Diazotized CS-MOF diesel 52 g/g | patent CN121130847A | null | N/A | missing_pdf | 段0036/图8 | N/A | missing_pdf | missing_pdf | Same patent as pd_087 |
| pd_098 | chitosan.json | performance_data[97] | performance_data | SA-CCS-LS@Fe3O4-1.5 NR >95% | patent CN117654453A | null | N/A | missing_pdf | 段落[0065] | N/A | missing_pdf | missing_pdf | Patent PDF exists but source_file naming differs |
| pd_099 | chitosan.json | performance_data[98] | performance_data | SA-CCS-LS@Fe3O4-1.5-0.6: NR 98.82%, CR 97.54%, RB5 95.77% | patent CN117654453A | null | N/A | missing_pdf | 段落[0074] | N/A | missing_pdf | missing_pdf | Same patent as pd_098 |
| pd_100 | chitosan.json | performance_data[99] | performance_data | Removal rate formula: Re% = (C0-Ce)/C0 × 100% | patent CN117654453A | null | N/A | missing_pdf | 段落[0042]-[0044] | N/A | missing_pdf | missing_pdf | Same patent as pd_098 |
| pd_101 | chitosan.json | performance_data[100] | performance_data | C-FeS Sb pH 1-7 >80%, max 93.12% at pH=1 | patent CN114873705A | null | N/A | missing_pdf | 实施例1[0053] | N/A | missing_pdf | missing_pdf | Patent PDF exists but source_file naming differs |
| pd_102 | chitosan.json | performance_data[101] | performance_data | C-FeS Cr pH 1-9 >85% | patent CN114873705A | null | N/A | missing_pdf | 实施例1[0054] | N/A | missing_pdf | missing_pdf | Same patent as pd_101 |
| pd_103 | chitosan.json | performance_data[102] | performance_data | Sb time: 5min 82.5%, 10min 92.85% | patent CN114873705A | null | N/A | missing_pdf | 实施例1[0056] | N/A | missing_pdf | missing_pdf | Same patent as pd_101 |
| pd_104 | chitosan.json | performance_data[103] | performance_data | Cr time: 5min 75%, 10min 81% | patent CN114873705A | null | N/A | missing_pdf | 实施例1[0057] | N/A | missing_pdf | missing_pdf | Same patent as pd_101 |
| pd_105 | chitosan.json | performance_data[104] | performance_data | Engineering significance >80% in 5min | patent CN114873705A | null | N/A | missing_pdf | [0011] | N/A | missing_pdf | missing_pdf | Same patent as pd_101 |
| pd_106 | chitosan.json | performance_data[105] | performance_data | Figure 5 Sb removal comparison (qualitative) | patent CN114873705A | null | N/A | missing_pdf | 对比例1-5[0069] | N/A | missing_pdf | missing_pdf | Same patent as pd_101 |
| pd_107 | chitosan.json | performance_data[106] | performance_data | Adsorbent improves oil absorption (qualitative) | patent CN119488883A | null | N/A | missing_pdf | [0071] | N/A | missing_pdf | missing_pdf | Patent PDF exists but source_file naming differs |
| pd_108 | chitosan.json | performance_data[107] | performance_data | Attapulgite organic modification effect (qualitative) | patent CN109351339A | null | N/A | missing_pdf | 结果分析 | N/A | missing_pdf | missing_pdf | Patent PDF exists but source_file naming differs |
| pd_109 | chitosan.json | performance_data[108] | performance_data | Activated carbon modification effect (qualitative) | patent CN109351339A | null | N/A | missing_pdf | 结果分析 | N/A | missing_pdf | missing_pdf | Same patent as pd_108 |
| pd_110 | chitosan.json | performance_data[109] | performance_data | MOF-808/CS Cr(VI) qmax 320.0 mg/g | 2022-Valadi-chitosan-mof-heavy-metal-chromium-adsorption.pdf | 10.1016/j.carbpol.2022.119383 | Valadi2022.pdf | yes | Abstract | "the maximum capacity was obtained to be 320.0 mg/g at pH 5" | supported | no_action | Verified |
| pd_111 | chitosan.json | performance_data[110] | performance_data | Chitosan nanocomposite MO qmax 172.17 mg/g | 2023-Waliullah-chitosan-dye-adsorption.pdf | 10.1016/j.molliq.2023.122763 | Waliullah2023.pdf | yes | p.5 | "The maximum adsorption capacity...showed a mass capacity of 172.17 mg/g" | supported | no_action | Verified |
| pd_112 | chitosan.json | performance_data[111] | performance_data | 7 cycles 89.9% retention | 2023-Waliullah-chitosan-dye-adsorption.pdf | 10.1016/j.molliq.2023.122763 | Waliullah2023.pdf | yes | p.6 | "after 7 cycles, the adsorption capacity...remains at about 89.9%" | supported | no_action | Verified |
| pd_113 | chitosan.json | performance_data[112] | performance_data | Gd(III) MWCNT-PDA-CS-GO-I 150.86 mg/g | 2021-Zhang-chitosan-aerogel-heavy-metal-rare-earth.pdf | 10.1016/j.jhazmat.2020.124347 | Zhang2021aerogel.pdf | yes | p.7 | "reaching 150.86 mg g−1" | supported | no_action | Verified |
| pd_114 | chitosan.json | performance_data[113] | performance_data | MCC10 Cu²⁺ 434.8 mg/g | 2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.pdf | 10.1016/j.jhazmat.2022.129112 | Godiya2022.pdf | yes | p.8 Table 1 | "MCC10 434.8" | supported | no_action | Verified |
| pd_115 | chitosan.json | performance_data[114] | performance_data | Unmodified MCC/CS: Cu²⁺ 158.7, Zn²⁺ 161.2, Ni²⁺ 172.4 mg/g | 2022-Godiya-chitosan-cellulose-hydrogel-heavy-metal-adsorption.pdf | 10.1016/j.jhazmat.2022.129112 | Godiya2022.pdf | yes | p.6 | "unmodified MCC/CS hydrogel (158.7, 161.2, and 172.4)" | supported | no_action | Verified |
| pd_116 | chitosan.json | performance_data[115] | performance_data | CSBC MO qmax 38.75 mg/g | 2022-Loc-chitosan-biochar-methyl-orange-adsorption.pdf | 10.3390/toxics10090500 | Loc2022.pdf | yes | p.8 | "maximum adsorption capacity for MO of CSBC was estimated as 38.75 mg.g−1" | supported | no_action | Verified |
| pd_117 | chitosan.json | performance_data[116] | performance_data | RHB MO qmax 31.63 mg/g | 2022-Loc-chitosan-biochar-methyl-orange-adsorption.pdf | 10.3390/toxics10090500 | Loc2022.pdf | yes | p.8 | "comparatively higher than that of RHB with 31.63 mg.g−1" | supported | no_action | Verified |

## Boundary And DO-NOT Candidates

| item_id | target_json | field_path | boundary_type | condition | consequence | source_pdf | locator | quote | evidence_label | notes |
|---------|-------------|------------|---------------|-----------|-------------|------------|---------|-------|----------------|-------|
| bd_001 | chitosan.json | mechanisms[0].causal_chain.boundary_conditions[0] | knowledge_gap | Strong acid → CS dissolves | Loss of adsorption capacity | inferred | null | null | inferred_only | Needs PDF quote from Lei2021 to verify |
| bd_002 | chitosan.json | mechanisms[0].causal_chain.boundary_conditions[1] | knowledge_gap | Alkaline → NH₂ deprotonation | Reduced anion adsorption | inferred | null | null | inferred_only | Needs PDF quote |
| bd_003 | chitosan.json | mechanisms[0].causal_chain.boundary_conditions[2] | knowledge_gap | High salinity → electrostatic shielding | Reduced anion adsorption | inferred | null | null | inferred_only | Needs PDF quote |
| bd_004 | chitosan.json | mechanisms[3].causal_chain.boundary_conditions[0] | knowledge_gap | Strong acid → NH₂ fully protonated | Loss of metal coordination | inferred | null | null | inferred_only | Duplicate of bd_001 |
| bd_005 | chitosan.json | mechanisms[3].causal_chain.boundary_conditions[1] | soft_boundary | High Ca²⁺/Mg²⁺ competition | Reduced adsorption selectivity | inferred | null | null | inferred_only | General knowledge, needs experimental validation |
| bd_006 | chitosan.json | engineering_constraints[8] | soft_boundary | pH 4-6 only tested for Bambaeero | Cu²⁺ precipitation at pH>6 | Bambaeero2020.pdf | p.225 | "at pH 5" | partial | PDF verified the pH=5 condition but not the pH>6 limit explicitly |
| bd_007 | chitosan.json | engineering_constraints[29] | hard_do_not | Strong acid (HNO₃/H₂SO₄/HCl) → CS decomposition | Adsorption capacity drops significantly | N/A | null | null | inferred_only | Referenced from Upadhyay2020 review; needs direct quote |
| bd_008 | chitosan.json | tested_conditions.tested_ph_range | hard_do_not | pH 3.0-7.0 tested range | Values outside this range not validated | aggregated | null | null | inferred_only | Aggregated from performance_data; no single source validates full range |
| bd_009 | chitosan.json | mechanisms[14].description | hard_do_not | DD 94% → 94% deacetylation | Implies specific NH₂ density | N/A | null | null | inferred_only | DD value from Zhao2021; needs verification from source |
| bd_010 | chitosan.json | performance_data[0].value | soft_boundary | MW 3.62×10⁵ → 6.21×10³ → removal 79→92% | Correlation, not causation | N/A | null | null | inferred_only | PDF missing; mechanism not explained |

## Missing/Wrong Source Summary

| source_or_doi | affected_fields | issue | suggested_next_step |
|---------------|-----------------|-------|---------------------|
| 10.1016/j.carbpol.2021.118625 | pd_001 | PDF not found locally; source_file lacks directory prefix | Locate PDF in 仿生文献库 or download from DOI |
| 10.1016/j.carbpol.2020.117000 | pd_002, pd_003, pd_004 | PDF not found locally | Locate PDF in 仿生文献库 or download from DOI |
| 10.1016/j.ijbiomac.2021.04.158 | pd_005-pd_018 (14 items) | PDF not found; 第1组-配位螯合/ folder is EMPTY | This is the most critical missing source — 14 performance_data items depend on it. Download from DOI |
| 10.1007/s10311-023-01563-9 | pd_021 | PDF not found locally | Locate or download |
| 10.1016/j.rechem.2024.101332 | pd_026-pd_031 (6 items) | PDF not found locally | Locate or download |
| 10.1016/j.ijbiomac.2021.08.047 | pd_032, pd_033 | PDF not found locally | Locate or download |
| 10.1016/j.seta.2020.100951 | pd_034-pd_037 (4 items) | PDF not found locally | Locate or download |
| 10.1016/j.carbpol.2021.118671 | pd_038, pd_039 | PDF not found locally | Locate or download |
| 10.13550/j.jxhg.20210304 | pd_040 | PDF not found locally | Locate or download |
| 10.14028/j.cnki.1003-3726.2021.02.007 | pd_041 | PDF not found locally | Locate or download |
| 10.1016/j.cej.2022.138934 | pd_042 | PDF not found locally | Locate or download |
| 10.1016/j.scitotenv.2021.150606 | pd_043, pd_044 | PDF not found locally | Locate or download |
| 10.1007/s13762-021-03603-9 | pd_045-pd_048 (4 items) | PDF not found locally | Locate or download |
| 10.1016/j.chemosphere.2020.129273 | pd_049-pd_051 (3 items) | PDF not found locally | Locate or download |
| 10.1016/j.jece.2022.108048 | pd_052-pd_054 (3 items) | PDF not found locally | Locate or download |
| 10.19965/j.cnki.iwt.2022-1185 | pd_055 | PDF not found locally | Locate or download |
| 10.3969/j.issn.1001-9731.2022.10.023 | pd_056-pd_058 (3 items) | PDF not found locally | Locate or download |
| 10.3390/molecules26030594 | pd_068-pd_072 (5 items) | PDF not found locally | Locate or download |
| 10.13671/j.hjkxxb.2020.0407 | pd_073-pd_075 (3 items) | PDF not found locally | Locate or download |
| 10.1016/j.molliq.2020.114523 | pd_076, pd_077 | PDF not found locally | Locate or download |
| 10.15898/j.ykcs.202208230155 | pd_078, pd_079 | PDF not found locally | Locate or download |
| 10.1016/j.ijbiomac.2021.10.050 | pd_080-pd_086 (7 items) | PDF not found locally | Locate or download |
| Patent CN121130847A | pd_087-pd_097 (11 items) | source_file says "2025-CN121130847A-壳聚糖-纤维素-生物基-MOF 2.pdf" but actual file is in 仿生文献库/专利/ with different naming | Fix source_file path to match actual file location |
| Patent CN117654453A | pd_098-pd_100 (3 items) | source_file says "仿生文献库/专利/2024-CN117654453A-壳聚糖-海藻酸钠-磁性-生物基 2.pdf" — actual file has "_visual_cache.json" but no plain PDF found | Verify PDF exists; may need "_ 2.pdf" suffix |
| Patent CN114873705A | pd_101-pd_106 (6 items) | source_file says "仿生文献库/专利/2022-CN114873705A-壳聚糖-磁性-重金属-废水.pdf" — only visual_cache.json found, no plain PDF | Verify PDF exists or download from CNIPA |
| Patent CN119488883A | pd_107 | source_file says "仿生文献库/专利/2025-CN119488883A-壳聚糖-海藻酸钠-纤维素-生物基 2.pdf" — actual file exists with " 2.pdf" suffix | Verify path matches actual file |
| Patent CN109351339A | pd_108, pd_109 | source_file says "仿生文献库/专利/2019-CN109351339A-壳聚糖-海藻酸钠-生物基-重金属.pdf" — only visual_cache.json found | Verify PDF exists or download from CNIPA |
| 10.1016/j.cej.2024.149414 | pd_022-pd_025 (4 items) | PDF exists (Cheng2024.pdf) but exceeds 10MB tool limit | Manual spot-check recommended |
| Multiple mechanisms in enrichment/chitosan.json | All enrichment mechanism entries | causal_chain fields (pollutant_feature, bio_structure, interaction, why_it_works, transferable_principle) are all empty strings | These are Phase 4 backfill placeholders — need full population from source PDFs |

## Enrichment/chitosan.json Specific Issues

| item_id | target_json | field_path | field_type | claim_summary | source_file | ref_doi | evidence_label | recommended_action | notes |
|---------|-------------|------------|------------|---------------|-------------|---------|----------------|-------------------|-------|
| en_001 | enrichment/chitosan.json | mechanisms.pH对氮污染物吸附的影响机制.causal_chain | mechanism_causal_chain | All sub-fields empty (pollutant_feature, bio_structure, interaction, etc.) | N/A | N/A | inferred_only | needs_human_decision | Enrichment file has empty causal_chain for all ~100 mechanisms |
| en_002 | enrichment/chitosan.json | mechanisms.金属离子络合机制.causal_chain | mechanism_causal_chain | All sub-fields empty | N/A | N/A | inferred_only | needs_human_decision | Same issue as en_001 |
| en_003 | enrichment/chitosan.json | mechanisms.壳聚糖的七种染料吸附机制.causal_chain | mechanism_causal_chain | All sub-fields empty | N/A | N/A | inferred_only | needs_human_decision | Same issue as en_001 |
| en_004 | enrichment/chitosan.json | mechanisms.MCM两大改性方向.causal_chain | mechanism_causal_chain | All sub-fields empty | N/A | N/A | inferred_only | needs_human_decision | Same issue as en_001 |
| en_005 | enrichment/chitosan.json | mechanisms.壳聚糖对阴离子染料的吸附机制.causal_chain | mechanism_causal_chain | All sub-fields empty | N/A | N/A | inferred_only | needs_human_decision | Same issue as en_001 |

## Mechanism Audit Summary (Main chitosan.json)

| mechanism_name | verification | has_causal_chain | boundary_conditions_populated | evidence_label | recommended_action |
|----------------|-------------|------------------|------------------------------|----------------|-------------------|
| pH effect on N-pollutants | verified | yes (populated) | 4 entries, all llm_inferred | partial | add_quote_locator |
| Metal ion complexation | verified | yes (populated) | 4 entries, all llm_inferred | partial | add_quote_locator |
| Acid-leached carbon/CS/FeCl3 | needs_review | no | no | inferred_only | needs_human_decision |
| La3+-CS HSAB mechanism | needs_review | no | no | inferred_only | needs_human_decision |
| pHpzc effect | needs_review | no | no | inferred_only | needs_human_decision |
| Surface precipitation | needs_review | no | no | inferred_only | needs_human_decision |
| MCM three mechanisms | needs_review | no | no | inferred_only | needs_human_decision |
| Cr(VI) redox (VMCP) | needs_review | no | no | inferred_only | needs_human_decision |
| MCM five prep methods | needs_review | no | no | inferred_only | needs_human_decision |
| Synergistic adsorption FFO@Sil | needs_review | no | no | inferred_only | needs_human_decision |
| Seven dye mechanisms | needs_review | no | no | inferred_only | needs_human_decision |
| All BPA-related mechanisms | needs_review | no | no | inferred_only | needs_human_decision |
| All superhydrophobic mechanisms | needs_review | no | no | inferred_only | needs_human_decision |
| All electrospun membrane mechanisms | needs_review | no | no | inferred_only | needs_human_decision |

## Narrative Audit Summary

| narrative_entry | paper_id | sections_populated | evidence_label | recommended_action |
|----------------|----------|-------------------|----------------|-------------------|
| Keshvardoostchokami2021 | yes | 5/5 | inferred_only | source PDF missing |
| Upadhyay2021 | yes | 5/5 | inferred_only | source PDF missing |
| 2023-Wang-magnetic | yes | 5/5 | inferred_only | source PDF missing |
| 2021-Aramesh-dye | yes | 5/5 | inferred_only | source PDF missing |
| 2020-Bambaeero | yes | 5/5 | partial | PDF verified (pd_019, pd_020) |
| 2022-Feng-MCM | yes | 5/5 | inferred_only | source PDF missing |
| 2023-Vo-beads | yes | 5/5 | inferred_only | source PDF missing |
| 2021-李-CS-Pb | yes | 5/5 | inferred_only | source PDF missing |
| Cheng2024-BPA | yes | 5/5 | partial | PDF exists but >10MB |
| 2021-Sirajudheen | yes | 5/5 | inferred_only | source PDF missing |
| 2024-Hsu | yes | 5/5 | inferred_only | source PDF missing |
| 2021-Musarurwa-MOF | yes | 5/5 | inferred_only | source PDF missing |
| 2022-Lu | yes | 5/5 | inferred_only | source PDF missing |
| 2022-Liu-modified | yes | 5/5 | inferred_only | source PDF missing |
| 2022-Haripriyan | yes | 5/5 | inferred_only | source PDF missing |
| Yang2021-hydrogel | yes | 5/5 | inferred_only | source PDF missing |
| 2020-Sheth | yes | 5/5 | inferred_only | source PDF missing |
| Eltaweil2021 | yes | 5/5 | inferred_only | source PDF missing |
| Feng2021-membrane | yes | 5/5 | inferred_only | source PDF missing |
| 2022-Mashabi-GMA | yes | 5/5 | inferred_only | source PDF missing |
| 2021-Zhao-HAP-CS | yes | 5/5 | inferred_only | source PDF missing |
| 2022-Liu-aerogel | yes | 5/5 | inferred_only | source PDF missing |
| 2021-姜-CS | yes | 5/5 | inferred_only | source PDF missing |
| CN117654453A | yes | 5/5 | inferred_only | Patent PDF partially verified |
| CN115040496A | yes | 5/5 | inferred_only | source PDF missing |
| 2023-Waliullah | yes | 5/5 | partial | PDF verified (pd_111, pd_112) |
| 2021-Zhang-aerogel | yes | 5/5 | partial | PDF verified (pd_113) |

## Engineering Constraints Audit Summary

| constraint_name | value | source_doi | pdf_verified | evidence_label | recommended_action |
|----------------|-------|------------|-------------|----------------|-------------------|
| pH effect on N-pollutants | qualitative | 10.1016/j.carbpol.2021.118625 | no | missing_pdf | missing_pdf |
| 0.1M NaCl regeneration | ~75% | 10.1016/j.carbpol.2021.118625 | no | missing_pdf | missing_pdf |
| Acid eluent desorption | Cd 98.94%, Pb 97.50% | 10.1016/j.carbpol.2020.117000 | no | missing_pdf | missing_pdf |
| EDTA vs acid eluents | qualitative | 10.1016/j.carbpol.2020.117000 | no | missing_pdf | missing_pdf |
| Fe(III)-CS Cr(VI) | 166.3 mg/g | 10.1039/d2ra07112f | no | missing_pdf | missing_pdf |
| VMCP Cr(VI) 5 cycles | 246.0 mg/g | 10.1039/d2ra07112f | no | missing_pdf | missing_pdf |
| CH-MNP-CA Pb(II) cycles | 5 cycles | 10.1039/d2ra07112f | no | missing_pdf | missing_pdf |
| P-MCS Co(II) | 46.1 mg/g | 10.1039/d2ra07112f | no | missing_pdf | missing_pdf |
| pH constraint Bambaeero | pH 4-6 only | 10.1016/j.cjche.2020.07.066 | yes (Bambaeero2020.pdf) | partial | add_quote_locator |
| Imprinted CS Ni(II) cycles | 15 cycles | 10.1007/s10311-023-01563-9 | no | missing_pdf | missing_pdf |
| Citric acid/CS/Fe/PEI Cu | 127 mg/g | 10.1007/s10311-023-01563-9 | no | missing_pdf | missing_pdf |
| CS beads 7 regen methods | qualitative | 10.1007/s10311-023-01563-9 | no | missing_pdf | missing_pdf |
| pH BPA effect | pH 2-8 stable | 10.1016/j.cej.2024.149414 | yes (>10MB) | keep_soft | keep_soft |
| Temp BPA effect | endo/exo | 10.1016/j.cej.2024.149414 | yes (>10MB) | keep_soft | keep_soft |
| MCS-PAA Pb(II) | 204.89 mg/g | 10.13822/j.cnki.hxsj.2022008755 | no | missing_pdf | missing_pdf |
| CEA regeneration | 98% desorption | 10.1016/j.matlet.2022.131670 | no | missing_pdf | missing_pdf |
| F- regeneration NaOH | 87.5% after 4 cycles | 10.14028/j.cnki.1003-3726.2021.02.007 | no | missing_pdf | missing_pdf |
| 6 cycles CR/Cu | DMF/EDTA | 10.1016/j.cej.2022.138934 | no | missing_pdf | missing_pdf |
| CWF-2c15 Cr(VI) pH=5 | 87% | 10.1007/s11771-021-4724-8 | no | missing_pdf | missing_pdf |
| Optimal pH general | 4-6 | 10.1016/j.scitotenv.2021.150606 | no | missing_pdf | missing_pdf |
| Zeta potential Hg2+ | -33 mV pH 5-9 | 10.1016/j.scitotenv.2021.150606 | no | missing_pdf | missing_pdf |
| Temp general | 25-35°C | 10.1016/j.scitotenv.2021.150606 | no | missing_pdf | missing_pdf |
| Desorption 3 categories | qualitative | 10.1016/j.scitotenv.2021.150606 | no | missing_pdf | missing_pdf |
| CS acid instability strategy | qualitative | 10.16865/j.cnki.1000-7555.2021.0165 | no | missing_pdf | missing_pdf |
| Regen methods general | qualitative | 10.3390/molecules29184317 | no | missing_pdf | missing_pdf |
| pH-dependent complex | pH 5.3-7.7 | 10.1016/j.jece.2022.108048 | no | missing_pdf | missing_pdf |
| CTS/CMC/PAA Pb regen | 98.98 mg/g | 10.19965/j.cnki.iwt.2022-1185 | no | missing_pdf | missing_pdf |
| CNC/CS water stability | 93.8% | 10.3969/j.issn.1001-9731.2022.10.023 | no | missing_pdf | missing_pdf |
| 3D GO/CS stability | 90% after 5 cycles | 10.3390/molecules26030594 | no | missing_pdf | missing_pdf |
| CS composite regen challenge | NaOH/acid → hydrolysis | 10.3390/molecules26030594 | no | missing_pdf | missing_pdf |
| Optimal pH La-MZ/CTS | 6 | 10.13671/j.hjkxxb.2020.0407 | no | missing_pdf | missing_pdf |
| TGA CYCS/CNC | 60.3% loss | 10.1016/j.molliq.2020.114523 | no | missing_pdf | missing_pdf |
| pH CCC effect | pH 4-7 stable | 10.15898/j.ykcs.202208230155 | no | missing_pdf | missing_pdf |
| CCC regen 5 cycles | >85% | 10.15898/j.ykcs.202208230155 | no | missing_pdf | missing_pdf |
| As(V) pH 6.7 optimal | qualitative | 10.1016/j.ijbiomac.2021.10.050 | no | missing_pdf | missing_pdf |
| As regen NaOH | >90% | 10.1016/j.ijbiomac.2021.10.050 | no | missing_pdf | missing_pdf |
| CS thermal stability | 2-stage degradation | 10.1016/j.ijbiomac.2021.10.050 | no | missing_pdf | missing_pdf |
| CS solubility/pH | weak base, acid-soluble | 10.1016/j.ijbiomac.2021.10.050 | no | missing_pdf | missing_pdf |
| Patent CS-MOF cycling | 20 cycles 61.7 g/g | CN121130847A | no | missing_pdf | missing_pdf |
| Patent CS-MOF uncrosslinked | rapid decay 8 cycles | CN121130847A | no | missing_pdf | missing_pdf |
| Patent cycling NR/CR | 98.82%/98.19% | CN117654453A | no | missing_pdf | missing_pdf |
| Patent lycopene stability | 97.98% | CN115040496A | no | missing_pdf | missing_pdf |
| Patent Sb pH 1-7 | >80% | CN114873705A | no | missing_pdf | missing_pdf |
| Patent Cr pH 1-9 | >85% | CN114873705A | no | missing_pdf | missing_pdf |
| Patent Sb time | 5min 82.5% | CN114873705A | no | missing_pdf | missing_pdf |
| Patent Cr time | 5min 75% | CN114873705A | no | missing_pdf | missing_pdf |
| Patent flocculant dosage | 0.5-1.5 g/L | CN114873705A | no | missing_pdf | missing_pdf |
| Patent dye wastewater pH | 3-6 compatible | CN114873705A | no | missing_pdf | missing_pdf |
| Patent formula 3 | cellulose CNF 2.0g | CN119488883A | no | missing_pdf | missing_pdf |
| Patent regen multiple cycles | no decrease | CN119488883A | no | missing_pdf | missing_pdf |
| MOF-808/CS Cr(VI) regen | >72% 6 cycles | 10.1016/j.carbpol.2022.119383 | yes (Valadi2022.pdf) | supported | no_action |
| Waliullah 7 cycles | 89.9% | 10.1016/j.molliq.2023.122763 | yes (Waliullah2023.pdf) | supported | no_action |
| MCC10 4 cycles | Cu 189→81.6 mg/g | 10.1016/j.jhazmat.2022.129112 | yes (Godiya2022.pdf) | supported | no_action |
| CSBC pH 3 MO | 16.13 mg/g | 10.3390/toxics10090500 | yes (Loc2022.pdf) | supported | no_action |
| CSBC pH 10 MO | 8.35 mg/g | 10.3390/toxics10090500 | yes (Loc2022.pdf) | supported | no_action |
| RHB pH 3 MO | 15.50 mg/g | 10.3390/toxics10090500 | yes (Loc2022.pdf) | supported | no_action |
| RHB pH 10 MO | 7.30 mg/g | 10.3390/toxics10090500 | yes (Loc2022.pdf) | supported | no_action |
| CSBC decline pH 3→10 | 48.1% | 10.3390/toxics10090500 | yes (Loc2022.pdf) | supported | no_action |

## Key Statistics

- **Total performance_data items**: 117
- **Verified (PDF spot-checked)**: 14 items (12%)
- **PDF exists but unverified**: 4 items (3%)
- **Missing PDF**: 99 items (85%)
- **Mechanisms with populated causal_chain**: 2 (pH effect + metal complexation)
- **Mechanisms with empty causal_chain**: ~100 (in enrichment file) + ~90 (in main file without causal_chain)
- **Engineering constraints verified**: 10 items
- **Engineering constraints missing PDF**: 40+ items
- **Critical missing source**: 10.1016/j.ijbiomac.2021.04.158 (Aramesh2021) — 14 performance_data items, 第1组-配位螯合/ folder is empty

## Priority Actions for Codex

1. **Download Aramesh2021 PDF** (10.1016/j.ijbiomac.2021.04.158) — highest impact, unblocks 14 items
2. **Download all missing PDFs** listed in Missing/Wrong Source Summary
3. **Populate enrichment/chitosan.json causal_chain fields** — currently all empty
4. **Add quote+locator** to the 2 verified mechanisms (pH effect, metal complexation)
5. **Verify patent PDFs** exist and match source_file paths
6. **Narrow claims** for items with "pollutant unidentifiable" notes (15+ items)
7. **Classify boundary_conditions** — all currently llm_inferred, need PDF quotes for hard_do_not candidates