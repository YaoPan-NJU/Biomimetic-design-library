# Full Audit: Starch Granule — Extreme Value Sanity Check

status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-16 19:28:51 CST

---

## Executive Summary

**Scope:** `prototypes_db/materials_reference/starch-granule.json`
**Total performance_data rows:** 121
**Extreme values (>1000 mg/g):** 11 rows
**Concentration-dependent range entries:** 6 rows
**Review summary entries (cross-material maxima):** 2 rows
**Mixed unit entries (mmol/g alongside mg/g):** 3 rows
**Missing source_file / no page:** 1 row (index 77)
**All 10 source PDFs present locally:** ✅ Yes (in various subdirectories)

**Key findings:**
1. The **24,375 mg/g Crystal Violet** entry (Ihsanullah2022, index 53) is a **concentration-dependent capacity range** (50→250 mg/L), NOT a general qmax — must be demoted or split.
2. The **13,000 mg/g oil** entry (Khoo2023, index 72) is a **review maximum** from Table 3 (rice straw-cationic starch aerogel) — a cross-material superhydrophobic extreme that does not represent typical starch granule performance.
3. The **25,000 mg/g dye** and **2,000 mg/g heavy metal** in Khoo2023 abstract (index 66) are **review-wide maxima across all starch-based adsorbents**, not starch-granule-specific.
4. The **2,967 mg/g MB** (Chen2021, index 120) and **2,276 mg/g MB** (Khoo2023, index 70) are from highly engineered hydrogels — legitimate qmax but at the extreme end.
5. One row (index 77) has **no source_file and no page** — needs human decision.
6. Three rows use **mmol/g** (indices 20, 21, 23) — potential unit inconsistency with the rest of the dataset.

---

## 1. Extreme-Value Table

| idx | value | unit | pollutant | material | source_file | page | locator | metric_type | risk |
|-----|-------|------|-----------|----------|-------------|------|---------|-------------|------|
| 8 | 2000 | mg/g | Pb2+ | Fe2O3 NPs/starch nanocomposite | 2023-Abu-separation-starch-adsorption-adsorbent-review.pdf | 5 | Starch-Based Polymer Nanocomposites | qmax | ⚠️ EXTREME — review-cited qmax from single study; cross-verification needed |
| 53 | "4999 to 24,375" | mg/g | CV (crystal violet) | Zn CFst (starch-derived zinc-based carbon foam) | 2022-Ihsanullah-starch-adsorption-adsorbent-heavy-metal-review.pdf | 20 | Section 5.5 | concentration-derived capacity | 🚨 CRITICAL — concentration-dependent range, NOT qmax |
| 56 | "1455.76 to 1918.81" | mg/g | MB | starch-g-PAAc/CNWs5% | 2022-Ihsanullah-starch-adsorption-adsorbent-heavy-metal-review.pdf | 20 | Section 5.5 | concentration-derived capacity | ⚠️ EXTREME — concentration-dependent range (1500→2000 mg/L) |
| 66 | "油13000, 染料25000, 重金属2000, 药物782" | mg/g | multiple | (review summary) | 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review.pdf | 1 | Abstract | review summary | 🚨 CRITICAL — cross-material review maxima, not starch-granule specific |
| 69 | 1917 | mg/g | MB | CS-g-PAM hydrogel (50% cassava starch) | 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review.pdf | 17 | Section 4.4 | qmax | ⚠️ EXTREME — legitimate but extreme hydrogel qmax |
| 70 | 2276 | mg/g | MB | catecholamine-functionalized starch-g-(AA-co-AM) superabsorbent hydrogel | 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review.pdf | 17 | Section 4.4 | qmax | ⚠️ EXTREME — legitimate but extreme hydrogel qmax |
| 72 | 13000 | mg/g | oil | rice straw-cationic starch aerogel | 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review.pdf | 11 | Table 3 | review maximum | 🚨 CRITICAL — cross-material review maximum for superhydrophobic sorbent |
| 73 | 7780 | mg/g | chloroform | superhydrophobic starch/Fe3O4/SiO2 cryogel | 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review.pdf | 11 | Table 3 | review maximum | ⚠️ EXTREME — legitimate but cross-material superhydrophobic extreme |
| 113 | 1246.40 | mg/g | Crystal violet | CMS-SS (silica-sand/anionized starch composite) | 2021-Khan-bone-starch-adsorption-adsorbent-review.pdf | 2 | Starch-Based Composites | qmax | ⚠️ EXTREME — legitimate but from review table, single-source |
| 120 | 2967.66 | mg/g | MB | STAH20 (20 min NaOH pre-treated starch) | 2021-Chen-hydrogel-dye-methylene-blue-adsorption.pdf | 1 | Highlights | qmax | ⚠️ EXTREME — legitimate qmax from primary research, C₀ up to 5000 mg/L |

---

## 2. Metric-Type Sanity Table

| metric_type | count | risk_level | action |
|-------------|-------|------------|--------|
| qmax (single-value) | ~90 | LOW-MED | keep if value < 1000 mg/g; investigate if >1000 |
| concentration-derived capacity | 6 | HIGH | Must not be treated as qmax; demote or split |
| review summary (cross-material maxima) | 2 | CRITICAL | Must not be used as starch-granule performance; demote |
| review maximum (single pollutant) | 2 | HIGH | May be legitimate single-study qmax but from review context |
| removal% | 18 | LOW | Keep; note that % values depend on initial concentration |
| qualitative trend | 3 | LOW | Keep as qualitative evidence |
| range (unit mix: mmol/g) | 3 | MED | Convert to mg/g or split; note unit mismatch |

### Sub-analysis: concentration-derived capacity entries

| idx | material | pollutant | value range | concentration range | source |
|-----|----------|-----------|-------------|---------------------|--------|
| 52 | hydrolyzed PAN grafted starch composite | BB9 | 198–296 mg/g | 200–300 mg/L | Ihsanullah2022 p20 |
| 53 | Zn CFst | CV | 4,999–24,375 mg/g | 50–250 mg/L | Ihsanullah2022 p20 |
| 54 | Zn CFst | MG | 83–404 mg/g | 25–125 mg/L | Ihsanullah2022 p20 |
| 55 | Zn CFst | CR | 83–400 mg/g | 25–125 mg/L | Ihsanullah2022 p20 |
| 56 | starch-g-PAAc/CNWs5% | MB | 1,456–1,919 mg/g | 1,500–2,000 mg/L | Ihsanullah2022 p20 |
| 58 | CS50 hydrogel | MB | 14.9–417 mg/g | 50–4,000 mg/L | Ihsanullah2022 p21 |

**Assessment:** These are concentration-dependent qe values (equilibrium uptake at different C₀), NOT Langmuir qmax. They show how capacity scales with concentration. The 24,375 mg/g value for CV is particularly misleading because the concentration range is narrow (50→250 mg/L) yet the capacity jump is enormous, suggesting either an error in the review or a material with extreme concentration sensitivity. These should be labeled as `concentration-derived capacity` and NOT used in comparative rankings.

### Sub-analysis: review summary entries

| idx | description | source | risk |
|-----|-------------|--------|------|
| 66 | "油/有机溶剂13000, 农药66, 重金属2000, 染料25000, 药物782 mg/g" | Khoo2023 Abstract | 🚨 These are cross-material review maxima from ALL starch-based adsorbents (not just granules), taken from the abstract's summary statement |
| 59 | "higher concentration increases adsorption capacity due to enhanced driving force" | Ihsanullah2022 p20 | LOW — qualitative mechanism, not a numerical claim |

---

## 3. Source Path / PDF Availability Table

| source_file (as listed in JSON) | PDF exists locally | actual_path | notes |
|----------------------------------|--------------------|-------------|-------|
| 2023-Abu-separation-starch-adsorption-adsorbent-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2023-Abu-separation... 2.pdf + tools/litextract/missing_26_pdf_dir/ | Primary source |
| 2022-Ihsanullah-starch-adsorption-adsorbent-heavy-metal-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2022-Ihsanullah... 2.pdf + 3.pdf + tools/litextract/missing_26_pdf_dir/ | Primary source |
| 2022-Akinterinwa-starch-adsorption-adsorbent-heavy-metal-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2022-Akinterinwa... 2.pdf + 3.pdf + tools/litextract/missing_26_pdf_dir/ | Present |
| 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2023-Khoo... 2.pdf + tools/litextract/missing_26_pdf_dir/ | Present |
| 2021-Gupta-starch-adsorption-adsorbent-heavy-metal-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2021-Gupta... 2.pdf + tools/litextract/missing_26_pdf_dir/ | Present |
| 2021-Khan-bone-starch-adsorption-adsorbent-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2021-Khan... 2.pdf + 3.pdf + tools/litextract/missing_26_pdf_dir/ | Present |
| 2022-Fang-magnetic-starch-adsorption-adsorbent-review.pdf | ✅ | 仿生文献库/论文/第8组-仿生材料/2022-Fang... 2.pdf + 3.pdf | Present |
| 2022-Li-porous-hierarchical-starch-adsorption.pdf | ✅ | 仿生文献库/论文/第3组-多孔结构/2022-Li... 2.pdf | Note: path mismatch (missing "2" suffix in JSON source_file) |
| 2021-Chen-hydrogel-dye-methylene-blue-adsorption.pdf | ✅ | 仿生文献库/3rd/第D组-再生循环/2021-Chen... | Note: stored in 3rd batch, not in 第8组 |
| 2021-Hasan-dye-adsorption-water-treatment.pdf | ✅ | 仿生文献库/3rd/第D组-再生循环/2021-Hasan... | Note: stored in 3rd batch, not in 第8组 |

**Missing source_file:** Row 77 has `source_file: null`, `page: null`.

---

## 4. Candidate Queue Items Table

These are the high-risk entries that need human review or demotion.

| candidate_id | target_json | field_path | pollutant | value + unit | source_file | locator | quote (from DB) | evidence_label | metric_type | recommended_action | notes |
|--------------|-------------|------------|-----------|--------------|-------------|---------|-----------------|----------------|-------------|-------------------|-------|
| CQ-01 | starch-granule.json | performance_data[53] | CV | 4999–24,375 mg/g | 2022-Ihsanullah...review.pdf p20 | Section 5.5 | "4999 to 24,375 mg/g when CV concentration increased from 50 to 250 mg/L" | concentration-dependent capacity | concentration-derived | **demote** | Not a qmax; shows concentration-dependent uptake. Upper bound (24,375) is misleading as a "capacity." Must not be used in rankings. Consider splitting into range annotation or removing. |
| CQ-02 | starch-granule.json | performance_data[56] | MB | 1,456–1,919 mg/g | 2022-Ihsanullah...review.pdf p20 | Section 5.5 | "1455.76 to 1918.81 mg/g when MB concentration increased from 1500 to 2000 mg/L" | concentration-dependent capacity | concentration-derived | **demote** | At extremely high C₀ (1500–2000 mg/L); not representative of typical treatment scenarios. |
| CQ-03 | starch-granule.json | performance_data[66] | multiple | 油13000/染料25000/重金属2000/药物782 mg/g | 2023-Khoo...review.pdf p1 | Abstract | "油/有机溶剂13000, 农药66, 重金属2000, 染料25000, 药物782" | review summary | review summary | **demote** | Cross-material review maxima from abstract. These are the HIGHEST values found across ALL starch-based adsorbents in the entire review, not starch-granule specific. Should be annotated as "review-wide maximum" at minimum. |
| CQ-04 | starch-granule.json | performance_data[72] | oil | 13,000 mg/g | 2023-Khoo...review.pdf p11 | Table 3 | "rice straw-cationic starch aerogel" | review maximum | review maximum | **demote** | This is the cross-material oil maximum from Khoo2023 Table 3. While the specific material (rice straw-cationic starch aerogel) may be real, it represents a superhydrophobic aerogel, not a starch granule. Should be flagged as "cross-material review maximum" or removed from starch-granule material entry. |
| CQ-05 | starch-granule.json | performance_data[73] | chloroform | 7,780 mg/g | 2023-Khoo...review.pdf p11 | Table 3 | "superhydrophobic starch/Fe3O4/SiO2 nanoparticles/cryogel" | review maximum | review maximum | **needs_human_decision** | Legitimate single-material value but represents a highly engineered superhydrophobic cryogel. Is this truly "starch granule" or should it be classified as a different material class? |
| CQ-06 | starch-granule.json | performance_data[77] | (四环素) | 169.7 mg/g (initial), 89.5 mg/g (3 cycles) | null | null | "初始169.7 mg/g, 3次循环后89.5 mg/g（降低47%）" | incomplete provenance | other | **needs_human_decision** | No source_file, no page, no DOI. Cannot verify. Needs source identification or removal. |
| CQ-07 | starch-granule.json | performance_data[8] | Pb2+ | 2000 mg/g | 2023-Abu...review.pdf p5 | Starch-Based Polymer Nanocomposites | "淀粉/Fe2O3纳米复合材料对Pb2+的最大吸附容量" | single-source from review | qmax | **needs_human_decision** | 2000 mg/g is extremely high for a starch-based material. The Abu2023 review cites this from a single study. Cross-verification with primary source recommended. Gupta2021 (index 89) reports 200 mg/g for starch-iron oxide — a 10× discrepancy suggests index 8 may be a different material class or an error. |
| CQ-08 | starch-granule.json | performance_data[120] | MB | 2,967.66 mg/g | 2021-Chen...adsorption.pdf p1 | Highlights | "STAH20最大吸附容量qmax" | single primary study | qmax | **keep_with_note** | From primary research (Chen2021, DOI: 10.1016/j.cej.2020.126953). Legitimate qmax for STAH20 at very high C₀ (5000 mg/L). Extreme but from a real experiment. |
| CQ-09 | starch-granule.json | performance_data[70] | MB | 2,276 mg/g | 2023-Khoo...review.pdf p17 | Section 4.4 | "邻苯二酚胺功能化淀粉水凝胶对MB的最大吸附容量" | review-cited single study | qmax | **keep_with_note** | From Khoo2023 Table/Section citing a specific study. Legitimate but extreme. |

---

## 5. Boundary / DO-NOT Candidate Table

These entries are at the boundary of what should be included in starch-granule performance_data.

| boundary_id | target_json | field_path | current_value | issue | recommendation | rationale |
|-------------|-------------|------------|---------------|-------|----------------|-----------|
| BN-01 | starch-granule.json | performance_data[52] | "198 to 296.49 mg/g" | Concentration-dependent range (BB9, 200→300 mg/L) | **split** | Not a qmax. At 200 mg/L, qe=198; at 300 mg/L, qe=296. The upper bound is concentration-limited. Should be annotated as concentration-dependent uptake, not maximum capacity. |
| BN-02 | starch-granule.json | performance_data[54] | "83 to 404 mg/g" | Concentration-dependent range (MG, 25→125 mg/L) | **split** | Same pattern — capacity scales with concentration. Not a saturation qmax. |
| BN-03 | starch-granule.json | performance_data[55] | "83 to 400 mg/g" | Concentration-dependent range (CR, 25→125 mg/L) | **split** | Same pattern as BN-02. |
| BN-04 | starch-granule.json | performance_data[58] | "14.9 to 417 mg/g" | Concentration-dependent range (MB, 50→4000 mg/L) | **split** | Very wide concentration range; at 4000 mg/L the qe is 417. This is extreme loading. |
| BN-05 | starch-granule.json | performance_data[69] | 1917 mg/g | CS-g-PAM hydrogel at 50% cassava starch | **needs_human_decision** | This is a specific hydrogel composition, not "starch granule." Is it appropriate to include in this material class? The material is 50% starch, 50% chitosan+PAM. |
| BN-06 | starch-granule.json | performance_data[102] | 912 mg/g | starch-3-chloro-2-hydroxypropyltriethyl ammonium chloride + micro silica-sand composite | **needs_human_decision** | The material is a silica-sand composite with starch modifier. Is this "starch granule" or a silica-sand composite? |
| BN-07 | starch-granule.json | performance_data[20,21,23] | 2.33, 1.25, 1.36 mmol/g | Mixed units (mmol/g vs mg/g for all other entries) | **split / convert** | Three entries use mmol/g while all others use mg/g. For Cu2+ (MW 63.5): 2.33 mmol/g = 148 mg/g. For Pb2+ (MW 207.2): 1.25 mmol/g = 259 mg/g. These should be converted to mg/g for consistency, or clearly annotated. |
| BN-08 | starch-granule.json | performance_data[57] | qualitative text | "初始染料浓度对吸附容量的影响机制" — no numeric value | **keep as qualitative** | This is a mechanism description, not a performance metric. Should be in mechanisms[], not performance_data[]. |

---

## 6. Specific Focus: Ihsanullah2022 Crystal Violet 24,375 mg/g

**Entry:** performance_data[53]
**Claim:** "Zn CFst对CV的极高吸附容量 = 4999 to 24,375 mg/g when CV concentration increased from 50 to 250 mg/L"

**Analysis:**
- The value is described as a **concentration-dependent range**, not a Langmuir qmax
- The concentration range is narrow (50→250 mg/L, only 5× increase)
- The capacity range is enormous (4,999→24,375 mg/g, nearly 5× increase)
- This pattern suggests the material has not reached saturation even at 250 mg/L
- The value is from Ihsanullah2022 Section 5.5, which discusses "Effect of Initial Dye Concentration"
- The Ihsanullah2022 paper is a **review**, so this value is cited from another study
- **Critical concern:** 24,375 mg/g is physically implausible for most adsorption systems (would require the adsorbent to absorb ~24× its own weight in dye)
- **Recommendation:** Label as `concentration-derived capacity` with range annotation. Do NOT use as qmax in rankings. The upper bound should be marked as `needs_human_decision` pending primary source verification.

**Locator:** Ihsanullah2022, Section 5.5, p20
**Quote from DB:** "4999 to 24,375 mg/g when CV concentration increased from 50 to 250 mg/L"
**Evidence label:** concentration-derived capacity (from review, citing primary study)
**Recommended action:** demote — do not use in comparative rankings; annotate as concentration-dependent

---

## 7. Specific Focus: Khoo2023 Oil 13,000 mg/g and Pharmaceutical Maxima

**Entry A:** performance_data[72]
**Claim:** "淀粉基超疏水吸附剂对油类的最大吸附容量 = 13,000 mg/g"
**Material:** rice straw-cationic starch aerogel
**Source:** Khoo2023 Table 3, p11

**Analysis:**
- This is from Khoo2023's Table 3, which compiles oil adsorption capacities from multiple studies
- The material (rice straw-cationic starch aerogel) is a superhydrophobic aerogel, not a starch granule
- Oil adsorption capacities are typically much higher than aqueous pollutant capacities because oils are pure liquids (not dilute solutions)
- 13,000 mg/g means the material absorbs 13× its weight in oil — plausible for superhydrophobic aerogels
- **However:** This is a cross-material review maximum included in a starch-granule database. The material class (superhydrophobic aerogel) is very different from starch granules.
- **Recommendation:** Demote. This value skews starch-granule rankings. If kept, must be annotated as "cross-material review maximum, superhydrophobic aerogel class."

**Entry B:** performance_data[66] (review summary)
**Claim:** "淀粉基吸附剂对六类污染物的最大吸附容量汇总 = 油/有机溶剂13000, 农药66, 重金属2000, 染料25000, 药物782 mg/g"
**Source:** Khoo2023 Abstract, p1

**Analysis:**
- This is the abstract's summary of maximum capacities across ALL starch-based adsorbents
- These are the absolute highest values found in the entire review
- They are NOT starch-granule-specific — they span all modified starch materials
- **Recommendation:** Demote. This entry is a review summary, not a performance data point for any specific material.

**Entry C:** performance_data[71]
**Claim:** "磁性MOF-淀粉水凝胶对氟伐他汀的最大吸附容量 = 782.05 mg/g"
**Source:** Khoo2023 Section 4.5, p21

**Analysis:**
- This is a specific material (magnetic MOF-starch hydrogel) for a specific pollutant (fluvastatin)
- The material is a MOF-hydrogel composite, not a starch granule
- 782 mg/g for a pharmaceutical is high but plausible for MOF-based adsorbents
- **Recommendation:** needs_human_decision — is this "starch granule" or "MOF composite"?

---

## 8. Unit Inconsistency Analysis

Three entries use **mmol/g** while all others use **mg/g**:

| idx | value | unit | pollutant | material | conversion |
|-----|-------|------|-----------|----------|------------|
| 20 | 2.33 | mmol/g | Cu2+ | polyamine-type corn starch/GMA grafted copolymer | 2.33 × 63.5 = **148.0 mg/g** |
| 21 | 1.25 | mmol/g | Pb2+ | polyamine-type corn starch/GMA | 1.25 × 207.2 = **259.0 mg/g** |
| 23 | 1.36 | mmol/g | Cu2+ | grafted starch hydrogel (itaconic acid/acrylamide) | 1.36 × 63.5 = **86.4 mg/g** |

**Recommendation:** Convert to mg/g for database consistency, or add a note that these are in different units. The converted values (86–259 mg/g) are reasonable and do not trigger extreme-value flags.

---

## 9. Missing Provenance Analysis

**Row 77:** CSMB对四环素的吸附容量及循环稳定性
- `source_file: null`
- `page: null`
- `ref_doi: null`
- Value: "初始169.7 mg/g, 3次循环后89.5 mg/g（降低47%）"
- **Recommendation:** needs_human_decision — cannot verify without source. Either identify the source or remove.

---

## 10. Summary of Recommendations

### High-priority demotions (prevent ranking errors):

| idx | action | reason |
|-----|--------|--------|
| 53 | **demote** | Concentration-derived capacity range (4999–24,375 mg/g), NOT qmax |
| 66 | **demote** | Review summary cross-material maxima, not starch-granule specific |
| 72 | **demote** | Cross-material review maximum for superhydrophobic sorbent |
| 56 | **demote** | Concentration-dependent range at extreme C₀ (1500–2000 mg/L) |

### Needs human decision:

| idx | action | reason |
|-----|--------|--------|
| 77 | **needs_human_decision** | No source file, no page, no DOI |
| 8 | **needs_human_decision** | 2000 mg/g Pb2+ — 10× discrepancy with Gupta2021 (200 mg/g for same material class) |
| 73 | **needs_human_decision** | Superhydrophobic cryogel — is this "starch granule"? |
| 69 | **needs_human_decision** | 50% starch + 50% chitosan/PAM hydrogel — material class boundary |
| 71 | **needs_human_decision** | MOF-starch hydrogel — material class boundary |
| 102 | **needs_human_decision** | Silica-sand composite — material class boundary |

### Recommended splits:

| idx | action | reason |
|-----|--------|--------|
| 52 | **split** | Concentration-dependent range (BB9) |
| 54 | **split** | Concentration-dependent range (MG) |
| 55 | **split** | Concentration-dependent range (CR) |
| 58 | **split** | Concentration-dependent range (MB, 50→4000 mg/L) |

### Unit conversion needed:

| idx | action | reason |
|-----|--------|--------|
| 20 | **convert** | mmol/g → 148 mg/g |
| 21 | **convert** | mmol/g → 259 mg/g |
| 23 | **convert** | mmol/g → 86 mg/g |

### Keep with notes:

| idx | action | reason |
|-----|--------|--------|
| 120 | **keep_with_note** | Legitimate qmax (2967 mg/g) from primary research, but extreme |
| 70 | **keep_with_note** | Legitimate qmax (2276 mg/g) from review-cited study |
| 113 | **keep_with_note** | Legitimate qmax (1246 mg/g) from review table |

---

## 11. Verification Methodology

- **PDF availability:** Checked all 10 unique source files against local filesystem (仿生文献库/, tools/litextract/missing_26_pdf_dir/)
- **Value extraction:** Parsed all 121 performance_data rows for numeric values > 1000 mg/g
- **Metric classification:** Categorized each entry by metric_type (qmax, removal%, concentration-derived, review summary, etc.)
- **Cross-reference:** Compared entries from Ihsanullah2022 and Gupta2021 for duplicate/overlapping claims (e.g., Pb2+ starch-iron oxide: 2000 vs 200 mg/g)
- **Unit audit:** Identified mmol/g entries requiring conversion
- **Provenance check:** Flagged entries with missing source_file or page

**Note:** This audit is evidence-based. No database files were modified. All recommendations are for human review before any changes are made to starch-granule.json.
