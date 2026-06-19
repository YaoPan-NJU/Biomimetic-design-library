---
status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-16T19:12:00+08:00
scope: Targeted Sub-Batch B — Diatom Source Path & Dedup Cleanup
json_files:
  - prototypes_db/diatom-frustule.json
  - prototypes_db/enrichment/diatom-frustule.json
pdf_dirs:
  - 仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/
  - 仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf
---

# Diatom Source Path & Dedup Cleanup — Evidence Audit

## 1. JSON source_file → Actual Local PDF Path Mapping

| # | JSON source_file | Actual PDF Path | Status | Notes |
|---|-----------------|----------------|--------|-------|
| 1 | `仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属.pdf` | `仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf` | **path_mismatch** | JSON missing trailing " 2" (space-two); PDF exists with " 2" suffix. DOI 10.11862/CJIC.2021.025 confirmed correct. |
| 2 | `2024-Qin-diatomite-heavy-metal-adsorption.pdf` (bare) | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2024-Qin-diatomite-heavy-metal-adsorption.pdf` | **bare_filename** | PDF found; JSON lacks directory prefix. |
| 3 | `2022-Guo-diatomite-tetracycline-adsorption.pdf` (bare) | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Guo-diatomite-tetracycline-adsorption.pdf` | **bare_filename** | PDF found; JSON lacks directory prefix. |
| 4 | `2025-Abou-Elanwar-diatomite-diatom-lead-methylene-blue-adsorption.pdf` (bare) | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2025-Abou-Elanwar-diatomite-diatom-lead-methylene-blue-adsorption.pdf` | **bare_filename** | PDF found; JSON lacks directory prefix. |
| 5 | `2021-Wu-diatomite-diatom-magnetic-nickel-adsorption.pdf` (bare) | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2021-Wu-diatomite-diatom-magnetic-nickel-adsorption.pdf` | **bare_filename** | PDF found; JSON lacks directory prefix. |
| 6 | `2022-Radjai-cellulose-diatomite-diatom-dye-adsorption.pdf` (bare) | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Radjai-cellulose-diatomite-diatom-dye-adsorption.pdf` | **bare_filename** | PDF found; JSON lacks directory prefix. |
| 7 | `2022-Sriram-methyl-orange-adsorption.pdf` (bare) | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Sriram-methyl-orange-adsorption.pdf` | **bare_filename** | PDF found; JSON lacks directory prefix. |

### C1 Folder Note
Folder title says "4 篇" but contains **6 PDFs** (Wu, Guo, Radjai, Sriram, Qin, Abou-Elanwar). Folder name is stale metadata.

---

## 2. PDF → Extraction JSON Mapping

| PDF Filename | Extraction JSON Path | Exists | Notes |
|-------------|---------------------|--------|-------|
| 2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf | `tools/litextract/outputs/extractions/论文/json/2021-杜-硅藻-硅藻土-吸附-重金属.json` | ✅ | Full path; narrative references this correctly. |
| 2024-Qin-diatomite-heavy-metal-adsorption.pdf | `tools/litextract/outputs/extractions/第三波/json/2024-Qin-diatomite-heavy-metal-adsorption.json` | ✅ | Full path in narrative. |
| 2022-Guo-diatomite-tetracycline-adsorption.pdf | `tools/litextract/outputs/extractions/第三波/json/2022-Guo-diatomite-tetracycline-adsorption.json` | ✅ | Full path in narrative. |
| 2025-Abou-Elanwar-diatomite-diatom-lead-methylene-blue-adsorption.pdf | `tools/litextract/outputs/extractions/第三波/json/2025-Abou-Elanwar-diatomite-diatom-lead-methylene-blue-adsorption.json` | ✅ | Full path in narrative. |
| 2021-Wu-diatomite-diatom-magnetic-nickel-adsorption.pdf | — | ❌ No narrative entry | Only appears in performance_data as bare filename. |
| 2022-Radjai-cellulose-diatomite-diatom-dye-adsorption.pdf | — | ❌ No narrative entry | Only appears in performance_data as bare filename. |
| 2022-Sriram-methyl-orange-adsorption.pdf | — | ❌ No narrative entry | Only appears in performance_data as bare filename. |
| 2022-于-硅藻-硅藻土-吸附-综述 | `tools/litextract/outputs/extractions/论文/json/2022-于-硅藻-硅藻土-吸附-综述.json` | ✅ | Review paper; narrative present, no performance_data rows. |
| 2022-Roychoudhury-diatom-biosilica-review | `tools/litextract/outputs/extractions/论文/json/2022-Roychoudhury-diatom-biosilica-porous-shell-review.json` | ✅ | Review paper; narrative present. |
| 2022-Selmeczy-diatom-review | `tools/litextract/outputs/extractions/论文/json/2022-Selmeczy-diatom-review.json` | ✅ | Review paper; narrative present. |
| 2022-杨-硅藻-硅藻土-吸附-水处理-综述 | `tools/litextract/outputs/extractions/论文/json/2022-杨-硅藻-硅藻土-吸附-水处理-综述.json` | ✅ | Review paper; narrative present. |
| 2023-CNKI-基于蛛网藻结构的轮毂仿生轻量化设计及优化 | `tools/litextract/outputs/extractions/中文文献/2023-CNKI-基于蛛网藻结构的轮毂仿生轻量化设计及优化.json` | ✅ | **Unrelated**: Arachnoidiscus wheel hub design, not diatom adsorption. See §5. |

---

## 3. Duplicated Performance Rows

### 3a. Exact Duplicate Rows (identical param + value + source_file + page + locator)

| Keep Index | Remove Index | Parameter | Value | Source | Reason |
|-----------|-------------|-----------|-------|--------|--------|
| [7] | [8] | 去除率（最优条件下） | ~93 % | 2024-Qin | exact dup |
| [9] | [10] | Langmuir最大吸附容量qmax | 15°C: 103.1; 25°C: 154.9; 35°C: 211.2 | 2022-Guo | exact dup |
| [11] | [14] | Pb(II)最大吸附容量（单体系） | 178.57 | 2025-Abou-Elanwar | exact dup |
| [12] | [15] | MB最大吸附容量（单体系） | 392.16 | 2025-Abou-Elanwar | exact dup |
| [13] | [16] | 混合体系吸附容量 | Pb(II) 149.25; MB 354.61 | 2025-Abou-Elanwar | exact dup |
| [26] | [34] | 原始硅藻土MO去除率 | 15.5 % | 2022-Sriram | exact dup |
| [27] | [35] | 原始膨润土MO去除率 | 4.9 % | 2022-Sriram | exact dup |
| [28] | [36] | NFD最大MO去除率 | 94.7 % | 2022-Sriram | exact dup |
| [29] | [37] | NFB最大MO去除率 | 92.6 % | 2022-Sriram | exact dup |
| [30] | [38] | NFD最大吸附容量qmax | 246.9 | 2022-Sriram | exact dup |
| [31] | [39] | NFB最大吸附容量qmax | 215.9 | 2022-Sriram | exact dup |
| [32] | [40] | 原始硅藻土MO吸附容量 | 13.6 | 2022-Sriram | exact dup |
| [33] | [41] | pH影响（NFD去除率范围） | pH 4-10: 91.9-82.5% | 2022-Sriram | exact dup |

**Summary**: 42 rows → 29 unique after dedup. Remove 13 exact duplicates.

### 3b. Duplicate Mechanism Entries

| Keep Index | Remove Index | Name | DOI | Reason |
|-----------|-------------|------|-----|--------|
| [10] | [11] | 吸附机制（物理吸附为主） | 10.3969/j.issn.1000-6532.2024.04.015 | exact dup |
| [12] | [13] | 离子强度影响 | 10.13205/j.hjgc.202205007 | exact dup |

**Summary**: 15 → 13 unique. Remove 2.

### 3c. Duplicate Engineering Constraints

| Keep Index | Remove Index | Constraint | DOI | Reason |
|-----------|-------------|-----------|-----|--------|
| [4] | [5] | 再生性能 | 10.13205/j.hjgc.202205007 | exact dup |
| [6] | [7] | 再生循环性能 | 10.1016/j.jwpe.2025.107334 | exact dup |
| [14] | [15] | NFD和NFB循环再生性能 | 10.1016/j.chemosphere.2021.131976 | exact dup |

**Summary**: 16 → 13 unique. Remove 3.

### 3d. Duplicate Narrative Entries

| Keep Index | Remove Index | paper_id | Reason |
|-----------|-------------|----------|--------|
| [5] | [6] | qin2024_modified_diatomite_pb_adsorption | exact dup |
| [7] | [8] | guo2022_carbonized_diatomite_tetracycline | exact dup |
| [9] | [10] | abou_elanwar2025_sulfonated_diatomite_mb_pb | exact dup |
| [11] | [12] | 2020_CNKI_Arachnoidiscus_bionic_wheel_hub | exact dup |

**Summary**: 13 → 9 unique. Remove 4.

---

## 4. Diatom / Frustule / Diatomite vs Unrelated Structural-Design Evidence

| paper_id | Content Topic | Belongs to diatom-frustule? | Classification | Notes |
|----------|--------------|---------------------------|----------------|-------|
| 2022-Yu (综述) | 改性硅藻土吸附有机污染物综述 | ✅ diatomite + structural review | **review** | Review paper, no raw performance data; good for design translation. |
| 2021-Du | 巯基/羧基修饰硅藻土吸附 Pb²⁺/Cd²⁺ | ✅ diatomite modification | **primary** | Core performance paper; 485 mg/g Pb²⁺. |
| 2022-Roychoudhury (综述) | 硅藻生物硅壳体综述 | ✅ diatom frustule biology | **review** | Biological review; describes frustule structure. |
| 2022-Selmeczy (综述) | 硅藻生态系统服务综述 | ⚠️ diatom ecology, not materials | **review_marginal** | Ecology/biogeochemistry focus; Si cycling data useful, adsorption data minimal. |
| 2022-Yang (综述) | 硅藻土吸附水处理综述 | ✅ diatomite structural review | **review** | Materials-focused review. |
| 2024-Qin | 改性硅藻土吸附 Pb²⁺ | ✅ diatomite modification | **primary** | Fe₃O₄/diatomite composite; ~93% Pb removal. |
| 2022-Guo | 碳化硅藻土吸附四环素 | ✅ diatomite carbonization | **primary** | CD300 carbonized diatomite; TC adsorption. |
| 2025-Abou-Elanwar | 磺化硅藻土吸附 Pb²⁺/MB | ✅ diatomite sulfonation | **primary** | DE-SO₃; dual Pb/MB adsorption. |
| 2021-Wu | 磁性硅藻土吸附 Ni(II) | ✅ diatomite magnetic composite | **primary** | DECFASEs; Ni²⁺ adsorption. |
| 2022-Radjai | 纤维素/硅藻土复合材料吸附染料 | ✅ diatomite-cellulose composite | **primary** | A-CNF/DT; IC/MB dye adsorption. |
| 2022-Sriram | Ni-Fe LDH/硅藻土吸附甲基橙 | ✅ diatomite LDH composite | **primary** | NFD/NFB; MO removal. |
| **2023-CNKI-Arachnoidiscus** | **蛛网藻→汽车轮毂仿生轻量化** | ❌ **unrelated structural design** | **wrong_domain** | Mechanical engineering (wheel hub), not water treatment/adsorption. See §5. |

---

## 5. Source Mismatch: Pb²⁺ XPS Mechanism Cites Wrong DOI

**Target JSON**: `prototypes_db/diatom-frustule.json`
**Field path**: `mechanisms[0]` — "Pb²⁺吸附机理(XPS证据)"
**Current ref_doi**: `10.13205/j.hjgc.202205007` (Guo2022 — tetracycline paper)
**Actual source**: `10.11862/CJIC.2021.025` (Du2021 — Pb²⁺/Cd²⁺ paper)

**Evidence**:
- The mechanism description says: "XPS证实：-NH₂与Pb²⁺形成配位键(RNH₂-Mⁿ⁺, 406.73 eV)"
- Guo2022 (DOI 10.13205/j.hjgc.202205007) is about tetracycline (TC) adsorption on carbonized diatomite. It does NOT contain XPS data, Pb²⁺, or NH₂ references.
- Du2021 (DOI 10.11862/CJIC.2021.025) explicitly contains XPS analysis of Pb²⁺ on CA/DE with N1s and O1s spectra.
- The causal_chain locators reference "Guo2022 p.45 / Sec.0 + Abstract" — this is wrong; should be Du2021.
- The verification_quote ("electrostatic interaction is dominant in adsorption") is a generic diatomite statement, not XPS evidence.

**Recommended action**: `wrong_source` — Change ref_doi from `10.13205/j.hjgc.202205007` to `10.11862/CJIC.2021.025`. Update all causal_chain locators from "Guo2022" to "Du2021". The description text is correct (Du2021 content), only the attribution is wrong.

---

## 6. Wrong-Source "微藻" Text in Mechanisms

**Target JSON**: `prototypes_db/diatom-frustule.json`
**Affected mechanisms**: "MPTS接枝机理(硅烷偶联)" [index 1] and "文献对比：有机改性硅藻土吸附容量" [index 4]
**Current 基本原理**: "微藻细胞壁上的多糖、蛋白质和脂质可通过静电吸引、配位作用或氢键结合污染物"
**Correct source**: Du2021 (10.11862/CJIC.2021.025) — describes MPTS/APTES silane coupling on diatomite Si-OH, not microalgae cell wall polysaccharides/proteins.

**Evidence**: Du2021 is a chemistry paper about inorganic diatomite surface modification. The "微藻细胞壁" text is biological background that doesn't apply to mineral diatomite. The enrichment file (`prototypes_db/enrichment/diatom-frustule.json`) has the same wrong text for these two mechanisms.

**Recommended action**: `wrong_source` — The 基本原理 field contains template text from a different evidence domain (microalgae biology vs mineral diatomite chemistry). Should be replaced with diatomite-specific chemistry descriptions or marked as needs_human_decision if unsure what the correct text should be.

---

## 7. Unrelated Paper in diatom-frustule.json

**Target JSON**: `prototypes_db/diatom-frustule.json`
**Field path**: `narrative.entries[11]` and `narrative.entries[12]` (duplicates of same)
**Paper**: 2023-CNKI-基于蛛网藻结构的轮毂仿生轻量化设计及优化
**paper_id**: 2020_CNKI_Arachnoidiscus_bionic_wheel_hub

**Evidence**: This paper is about automotive wheel hub design inspired by Arachnoidiscus (蛛网藻) shell structure — mechanical engineering, not water treatment/adsorption. While it involves a diatom species (Arachnoidiscus), the "仿生" dimension is mechanical load distribution, not chemical adsorption.

**Recommended action**: `needs_human_decision` — This paper is a legitimate diatom-仿生 paper but in a different domain (structural mechanics vs adsorption materials). Should it stay in diatom-frustule.json (which is adsorption-focused) or move to a separate prototype?

---

## 8. Candidate Actions Summary

### 8a. normalize_path (7 items)

| target_json | field_path | current_value | recommended_value | reason |
|------------|-----------|---------------|-------------------|--------|
| diatom-frustule.json | performance_data[0-6].source_file | `仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属.pdf` | `仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf` | PDF has " 2" suffix |
| diatom-frustule.json | performance_data[7-8].source_file | `2024-Qin-diatomite-heavy-metal-adsorption.pdf` | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2024-Qin-diatomite-heavy-metal-adsorption.pdf` | Bare filename → full path |
| diatom-frustule.json | performance_data[9-10].source_file | `2022-Guo-diatomite-tetracycline-adsorption.pdf` | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Guo-diatomite-tetracycline-adsorption.pdf` | Bare filename → full path |
| diatom-frustule.json | performance_data[11-16].source_file | `2025-Abou-Elanwar-...pdf` | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2025-Abou-Elanwar-...pdf` | Bare filename → full path |
| diatom-frustule.json | performance_data[17].source_file | `2021-Wu-...pdf` | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2021-Wu-...pdf` | Bare filename → full path |
| diatom-frustule.json | performance_data[18-25].source_file | `2022-Radjai-...pdf` | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Radjai-...pdf` | Bare filename → full path |
| diatom-frustule.json | performance_data[26-41].source_file | `2022-Sriram-...pdf` | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Sriram-...pdf` | Bare filename → full path |

### 8b. deduplicate (18 items)

| target_json | field_path | indices_to_remove | count |
|------------|-----------|-------------------|-------|
| diatom-frustule.json | performance_data | [8,10,14,15,16,34,35,36,37,38,39,40,41] | 13 |
| diatom-frustule.json | mechanisms | [11,13] | 2 |
| diatom-frustule.json | engineering_constraints | [5,7,15] | 3 |
| diatom-frustule.json | narrative.entries | [6,8,10,12] | 4 |

**Total rows to remove: 22** (42→29 perf, 15→13 mech, 16→13 eng, 13→9 narr)

### 8c. wrong_source (2 items)

| target_json | field_path | current_ref_doi | correct_ref_doi | reason |
|------------|-----------|----------------|-----------------|--------|
| diatom-frustule.json | mechanisms[0].ref_doi | 10.13205/j.hjgc.202205007 | 10.11862/CJIC.2021.025 | Pb²⁺ XPS evidence is from Du2021, not Guo2022 |
| diatom-frustule.json | mechanisms[1].基本原理, mechanisms[4].基本原理 | "微藻细胞壁上的多糖..." (template text) | needs replacement | Wrong biology domain; diatomite chemistry ≠ microalgae cell walls |

### 8d. needs_human_decision (2 items)

| target_json | field_path | issue | question |
|------------|-----------|-------|----------|
| diatom-frustule.json | narrative.entries[11-12] | Arachnoidiscus wheel hub paper is structural-mechanical, not adsorption | Should this paper remain in diatom-frustule.json (adsorption prototype) or move elsewhere? |
| diatom-frustule.json | design_translation[0].source_tier | Currently `llm_inference` with empty examples | Is this inference acceptable or should it be upgraded to literature-backed? |

### 8e. keep_soft (1 item)

| target_json | field_path | note |
|------------|-----------|------|
| diatom-frustule.json | mechanisms[0].verification_quote | Generic diatomite statement ("electrostatic interaction is dominant in adsorption"); not XPS-specific. Keep but flag for future quote replacement from Du2021. |

### 8f. knowledge_gap (1 item)

| target_json | field_path | note |
|------------|-----------|------|
| diatom-frustule.json | provenance_summary | Lists n_papers=18, n_verified=21, n_unverified=36. Actual unique papers ≈ 11 (after removing unrelated Arachnoidiscus). Counts may be inflated by duplicates. |

---

## 9. Candidate Queue Items (for future batches)

| Queue Item | Priority | Batch | Notes |
|-----------|----------|-------|-------|
| Verify Wu2021 Ni(II) performance data against PDF | medium | C | Single source_file row; no narrative entry |
| Verify Radjai2022 IC/MB performance data against PDF | medium | C | 8 rows from single PDF; no narrative entry |
| Verify Sriram2022 MO performance data against PDF | medium | C | 16 rows (8 unique) from single PDF; no narrative entry |
| Enrichment file causal_chain population | low | D | All enrichment mechanisms have empty causal_chain fields |
| Replace 基本原理 template text in 7 mechanisms | medium | B | 7 mechanisms have generic "材料表面的活性基团..." or "微藻细胞壁..." template |
| Verify Qin2024 narrative content matches PDF | medium | C | Duplicate narrative entries exist; verify content before dedup |

---

## 10. Boundary / DO-NOT Candidate Table

| Item | Current Status | Boundary Reason | Action |
|------|---------------|-----------------|--------|
| 2023-CNKI-Arachnoidiscus narrative entries | present in diatom-frustule.json | Different仿生 domain (mechanical vs adsorption) | **needs_human_decision**: reclassify or remove |
| design_translation[0] source_tier=llm_inference | unverified inference | Not from literature, no examples | **needs_human_decision**: is this acceptable for the prototype? |
| Mechanism 基本原理 template text | generic template | Wrong biology domain (microalgae vs diatomite) | **wrong_source**: replace or mark needs_human_decision |
| verification_quote in mechanism[0] | generic diatomite statement | Not XPS-specific evidence | **keep_soft**: acceptable as contextual note, not hard evidence |
| Review papers (Yu, Roychoudhury, Selmeczy, Yang) | in narrative | Review papers provide design translation, not primary data | **keep_soft**: appropriate for narrative; no performance_data expected |

---

## Appendix: Source File Resolution Reference

```
diatom-frustule.json performance_data[0-6]  → "2021-杜-硅藻-硅藻土-吸附-重金属.pdf"
  Actual: "仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf"
  Extraction JSON: "tools/litextract/outputs/extractions/论文/json/2021-杜-硅藻-硅藻土-吸附-重金属.json"
  DOI: 10.11862/CJIC.2021.025 ✓

diatom-frustule.json performance_data[7-8]  → "2024-Qin-...pdf" (bare)
  Actual: "仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2024-Qin-...pdf"
  Extraction JSON: "tools/litextract/outputs/extractions/第三波/json/2024-Qin-...json"
  DOI: 10.3969/j.issn.1000-6532.2024.04.015 ✓

diatom-frustule.json performance_data[9-10] → "2022-Guo-...pdf" (bare)
  Actual: "仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Guo-...pdf"
  Extraction JSON: "tools/litextract/outputs/extractions/第三波/json/2022-Guo-...json"
  DOI: 10.13205/j.hjgc.202205007 ✓

diatom-frustule.json performance_data[11-16]→ "2025-Abou-Elanwar-...pdf" (bare)
  Actual: "仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2025-Abou-Elanwar-...pdf"
  Extraction JSON: "tools/litextract/outputs/extractions/第三波/json/2025-Abou-Elanwar-...json"
  DOI: 10.1016/j.jwpe.2025.107334 ✓

diatom-frustule.json performance_data[17]   → "2021-Wu-...pdf" (bare)
  Actual: "仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2021-Wu-...pdf"
  DOI: 10.1016/j.jcis.2020.08.119 ✓

diatom-frustule.json performance_data[18-25]→ "2022-Radjai-...pdf" (bare)
  Actual: "仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Radjai-...pdf"
  DOI: 10.1016/j.molliq.2022.119670 ✓

diatom-frustule.json performance_data[26-41]→ "2022-Sriram-...pdf" (bare)
  Actual: "仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2022-Sriram-...pdf"
  DOI: 10.1016/j.chemosphere.2021.131976 ✓
```
