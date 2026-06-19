---
status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-16T15:30:00+08:00
batch: Sub-Batch A — DNA Aptamer Evidence Build
---

# DNA Aptamer Evidence Audit — Sub-Batch A

## 1. Scope & Sources

### 1.1 Prototype Files Under Audit
| File | Path |
|------|------|
| Main DB | `prototypes_db/dna-aptamer.json` |
| Enrichment DB | `prototypes_db/enrichment/dna-aptamer.json` (empty `{}`) |

### 1.2 Literature Scope

| ID | Source File | Type | Primary Domain |
|----|------------|------|----------------|
| Li2021 | `B1-DNA适配体/2021-Li-aptamer-fluorescence-heavy-metal-review.pdf` | T5 Review | Biosensor — fluorescence |
| Wang2021 | `B1-DNA适配体/2021-Wang-aptamer-nanomaterials-heavy-metal-review.pdf` | T5 Review | Biosensor — nanomaterial |
| Bilibana2022 | `B1-DNA适配体/2022-Bilibana-aptamer-review.pdf` | T5 Review | Biosensor + decontamination (MC-LR) |
| Luo2021 | `B1-DNA适配体/2021-Luo-aptamer-microcystin.pdf` | T1 Article | Biosensor — SERS (MC-LR/RR) |
| Rahimizadeh2023 | `B1-DNA适配体/2023-Rahimizadeh-aptamer-biosensor-pathogens.pdf` | T5 Review | Biosensor — pathogen detection |
| Asmare2024 | `B1-DNA适配体/2024-Asmare-aptamer-biosensor-ciprofloxacin.pdf` | T1 Article | Biosensor — electrochemical |
| Vogiazi2021 | `B1-DNA适配体/2021-Vogiazi-aptamer-microcystin.pdf` | T1 Article | Biosensor (no extraction JSON) |
| Wu2023 | `B1-DNA适配体/2023-Wu-aptamer-heavy-metal-cadmium-water-treatment.pdf` | T1 Article | MD simulation — mechanism only |
| Herazo-Romero2025 | `B1-DNA适配体/2025-Herazo-Romero-magnetic-aptamer-pathogens.pdf` | T1 Article | Biosensor + magnetic separation (E. coli) |
| Yan2025 | `B1-DNA适配体/2025-Yan-heavy-metal-adsorption.pdf` | T1 Article | Biosensor — plasmonic |
| CN121588773A | `第三波-仿生吸附专利/2026-CN121588773A-aptamer-aflatoxin-adsorbent.pdf` | Patent | **Adsorption — AFB1 (in vivo)** |

### 1.3 Extraction JSON Files
All 9 aptamer-related extraction JSONs in `tools/litextract/outputs/extractions/第三波/json/` were read and cross-validated against the PDF visual caches. The patent CN121588773A has **no extraction JSON** — evidence extracted directly from the visual cache.

---

## 2. Literature-to-Path Mapping Table

| Literature ID | Target Pollutant | Domain | Adsorption/Capture Evidence? | Biosensor-Only? | Key Metric Types |
|---------------|-----------------|--------|------------------------------|-----------------|-----------------|
| Li2021 | Ag⁺, Hg²⁺, Pb²⁺, Cd²⁺, K⁺, Tl⁺, Cr³⁺, Cu²⁺ | Heavy metal | **NO** — 综述，无吸附数据 | ✅ Yes | LOD (fluorescence), aptamer sequences |
| Wang2021 | Pb²⁺, Hg²⁺, Cd²⁺, Ag⁺, As³⁺ | Heavy metal | **NO** — 综述，无吸附数据 | ✅ Yes | LOD (EC/fluorescence/color/SERS), Kd |
| Bilibana2022 | MC-LR, OA, STX, CYN, BTX, SPX G | Algal toxin | **YES** — RNA-GO for MC-LR (qmax 1.44 mg/g, >95% removal) | Partial | Kd, LOD, qmax, removal%, regeneration |
| Luo2021 | MC-LR, MC-RR | Algal toxin | **NO** — SERS signal-off detection | ✅ Yes | LOD (0.8 pM), Kd (50 nM) |
| Rahimizadeh2023 | E. coli, S. aureus, Salmonella, etc. | Pathogen | **NO** — 综述，传感检测 | ✅ Yes | LOD (CFU/mL), linear range |
| Asmare2024 | Ciprofloxacin | Antibiotic | **NO** — 电化学传感 | ✅ Yes | LOD (1.0 nM), linear range |
| Vogiazi2021 | Microcystin | Algal toxin | **NO** — 传感检测 (no extraction JSON) | ✅ Yes | LOD, linear range |
| Wu2023 | Cd²⁺ | Heavy metal | **NO** — MD simulation only | N/A | Binding energy (kJ/mol), distance (Å) |
| Herazo-Romero2025 | E. coli | Pathogen | **Partial** — magnetic pull-down (capture, not adsorption) | Partial | Capture efficiency (colony count), sensitivity (1:10,000) |
| Yan2025 | Pb²⁺, Cd²⁺, Hg²⁺ | Heavy metal | **NO** — plasmonic sensor | ✅ Yes | LOD (nM) |
| CN121588773A | AFB1 (黄曲霉毒素B1) | Mycotoxin | **YES** — DNA-GC adsorbent (Kd 0.25 nM, in vivo) | No | Kd, adsorption capacity (qualitative), in vivo efficacy |

---

## 3. Biosensor-Only vs Adsorption/Capture Evidence Table

### 3.1 Biosensor-Only Literature (CANNOT be used as adsorption evidence)

| Literature | Metric | Value | Unit | Why Biosensor-Only |
|-----------|--------|-------|------|--------------------|
| Li2021 | 无吸附性能数据 | — | — | 综述，明确标注"不涉及具体吸附材料的制备和性能数据" |
| Wang2021 | 无吸附性能数据 | — | — | 综述，明确标注"不涉及吸附去除或水处理应用" |
| Luo2021 | LOD (MC-LR) | 0.8 | pM | SERS signal-off检测，非吸附 |
| Luo2021 | Kd (MC-LR aptamer) | 50 ± 12 | nM | 传感器中的结合常数，非材料吸附容量 |
| Luo2021 | Kd (MC-RR aptamer) | 46 ± 7 | nM | 同上 |
| Asmare2024 | LOD (CFX) | 1.0 | nM | 电化学传感，非吸附 |
| Asmare2024 | MM/PBSA ΔG | -123.02 ± 2.14 | kJ/mol | 计算结合能，非材料吸附性能 |
| Yan2025 | LOD (Pb²⁺/Cd²⁺/Hg²⁺) | 0.007/0.012/0.005 | nM | 等离子体传感 |
| Rahimizadeh2023 | LOD (E. coli) | 10-10⁷ | CFU/mL | 综述，传感检测 |
| Wu2023 | 直接结合能垒 | 200-300 | kJ/mol | MD模拟，无实验吸附数据 |
| Herazo-Romero2025 | Capture (colony count) | 15-20 colonies at 1:1000 | — | 磁性pull-down，微生物检测，非溶解态污染物吸附 |

### 3.2 Adsorption/Capture Literature (Potential candidates for adsorption evidence)

| Literature | Material | Target | Key Adsorption Metrics | Evidence Quality |
|-----------|----------|--------|----------------------|-----------------|
| Bilibana2022 | RNA-GO nanosheets | MC-LR | qmax = 1.44 mg/g; removal >95%; selectivity >95% vs <12% for others; BET 2630 m²/g; regeneration 50°C/10min, 5 cycles → -10% | **Moderate** — 综述引用，非原创数据，但有明确数值 |
| CN121588773A | DNA-GC (DNA aptamer-loaded gelated cells) | AFB1 | Kd = 0.25 nM (SPR); qualitatively "largest adsorption capacity" vs Mon/PEI-Mon/CNT/sepiolite/MOF; in vivo efficacy (mouse models) | **High** — 原创专利数据，但qmax具体数值未给出（图4为对比图，无数值） |

---

## 4. Candidate Performance Table (Adsorption/Capture Only)

| Candidate | Source | Field Path | Metric Type | Value | Unit | Locator | Quote | Evidence Label |
|-----------|--------|-----------|-------------|-------|------|---------|-------|---------------|
| RNA-GO → MC-LR qmax | Bilibana2022 | `mechanisms[0].performance_data` (待填) | qmax | 1.44 | mg/g | Bilibana2022 p.11 §4 | "maximum adsorption capacity of 1.44 mg g⁻¹" | **single_source** (综述引用) |
| RNA-GO → MC-LR removal% | Bilibana2022 | — | removal% | >95 | % | Bilibana2022 p.11 §4 | "more than 95% of MC-LR was absorbed" | **single_source** |
| RNA-GO → MC-LR selectivity | Bilibana2022 | — | selectivity (removal%) | <12 | % (others) | Bilibana2022 p.11 §4 | "only less than 12% of the other toxins such as MC-LR, MC-RR, MC-LW, and nodularin were captured" | **single_source** |
| RNA-GO → BET | Bilibana2022 | — | BET surface area | 2630 | m²/g | Bilibana2022 p.11 §4 | "large surface area (2630 m2 g−1)" | **single_source** |
| RNA-GO → regeneration | Bilibana2022 | — | regeneration | 5 cycles, -10% | — | Bilibana2022 p.11 §4 | "adsorption capacity was diminished after five regeneration cycles, and the overall efficiency was reduced by 10%" | **single_source** |
| DNA-GC → AFB1 Kd | CN121588773A | — | Kd | 0.25 | nM | CN121588773A p.6 [0045] | "通过Biacore8000表面等离子体共振分析可确定DNA-GC与AFB1的亲和力低至0.25 nM" | **single_source** (scanned patent) |
| DNA-GC → AFB1 qmax (qualitative) | CN121588773A | — | qmax (qualitative) | "最大" vs 5 materials | — | CN121588773A p.6 [0045] | "结果显示DNA-GC拥有最大的毒素吸附能力" | **single_source** (no numerical qmax) |

---

## 5. Mechanism Table (with quote + locator)

### 5.1 Aptamer Molecular Recognition Mechanisms

| Mechanism | Target | Quote | Locator | Source | Evidence Label |
|-----------|--------|-------|---------|--------|---------------|
| T-Hg²⁺-T mismatch | Hg²⁺ | "T-T错配会选择性的捕获Hg2+以形成T-Hg2+-T复合物" | Wang2021 p.2 §1.2 | Wang2021 | verified |
| C-Ag⁺-C mismatch | Ag⁺ | "C-C错配只能识别Ag+形成C-Ag+-C复合物" | Wang2021 p.2 §1.2 | Wang2021 | verified |
| G-quadruplex formation | Pb²⁺ | "富含G的适配体容易从无规则卷曲转换成更稳定的G-4分体结构" | Wang2021 p.1 §1.1 | Wang2021 | verified |
| Induced-fit + hydrophobic + electrostatic | MC-LR/RR | "an induced-fit process... the MC phenyl groups may facilitate the hydrophobic effect via base stacking and the NH₂ groups most likely contribute to the electrostatic interactions" | Luo2021 p.6 | Luo2021 | verified |
| Shape complementarity + H-bond + electrostatic + stacking | Pathogens (general) | "Aptamers... adopt specific three-dimensional structures and interact with their targets through shape complementarity, hydrogen bonding, electrostatic interactions, and stacking interactions" | Rahimizadeh2023 p.2 §2.1 | Rahimizadeh2023 | verified |
| Direct coordination (Cd²⁺-O atoms) | Cd²⁺ | "the main binding of Cd2+ ion was on the O atoms of 7G, 8T, 12C, and 15T. And through IRI analysis, Cd2+-O was mainly a coordination bond." | Wu2023 p.13 §4 | Wu2023 | verified |
| π-π stacking + H-bond + hydrophobic | Ciprofloxacin | "π-π stacking interactions were observed between the aromatic ring of CFX and Guanine-58 (DG-58) and Guanine-60 (DG-60)" | Asmare2024 p.7 §3.3 | Asmare2024 | verified |
| AFB1 aptamer + gelated cell encapsulation | AFB1 | "DNA-GC吸附剂具有对AFB1的高亲和力与选择性，能够在复杂生物介质中精准识别并捕获AFB1分子" | CN121588773A p.6 [0021] | CN121588773A | **single_source** (scanned patent) |
| Aptamer-MNP electrostatic coupling | E. coli | "The surface of these MNPs allows aptamer binding through electrostatic interactions" | Herazo-Romero2025 p.10 §4 | Herazo-Romero2025 | verified |

### 5.2 Nanomaterial Roles (from reviews)

| Nanomaterial | Function | Source | Quote | Locator |
|-------------|----------|--------|-------|---------|
| GO (graphene oxide) | π-π stacking + fluorescence quenching + aptamer carrier | Li2021 | "单链DNA可通过核酸碱基和碳纳米材料之间的疏水和π-π堆积相互作用自发地吸附到碳纳米材料表面" | Li2021 p.6 §3.2 |
| AuNPs | SERS enhancement, colorimetric, peroxidase mimic | Rahimizadeh2023 | "Both metal-based NMs, like gold nanoparticles (AuNPs)... have been used to make sensitive aptasensors" | Rahimizadeh2023 p.3 §2.2 |
| Fe₃O₄ MNPs | Magnetic separation + aptamer carrier | Herazo-Romero2025 | "共沉淀法合成Fe3O4磁性纳米粒子（5-20nm）" | Herazo-Romero2025 p.3 §2.8 |
| Cu-TCPP(Pt) MOF | Molecular sieving + target enrichment | Yan2025 | "Cu-TCPP(Pt)的分子筛效应提高靶标富集并抑制背景干扰" | Yan2025 (extraction) |

---

## 6. Boundary Table

| Boundary Issue | Observation | Source | Recommendation | Evidence Label |
|---------------|-------------|--------|----------------|---------------|
| **Biosensor vs adsorbent scope** | 9 of 11 sources are biosensor-only. Only Bilibana2022 (RNA-GO) and CN121588773A (DNA-GC) report adsorption/capture metrics. | All | Do NOT conflate LOD/Kd from biosensors with adsorption capacity (qmax/removal%). Only RNA-GO and DNA-GC have adsorption evidence. | — |
| **Target specificity** | Aptamers are highly target-specific (single toxin/ion). Limited multi-target capability. | Wang2021, Rahimizadeh2023 | Specificity is a strength for point-source contamination but limits broad-spectrum water treatment. | verified |
| **Matrix effects** | Most studies use buffer/pure water. RNA-GO tested in "drinking water" but limited matrix diversity. DNA-GC tested in mouse serum (in vivo). | Bilibana2022, CN121588773A | Actual wastewater matrix performance is largely unknown. | **needs_human_decision** |
| **Regeneration** | RNA-GO: 50°C hot water, 5 cycles, -10% efficiency. DNA-GC: not tested (single-use in vivo). | Bilibana2022, CN121588773A | Regeneration is a critical gap for water treatment applications. | **needs_human_decision** |
| **Immobilization** | Aptamer orientation, density, and stability on solid supports are key engineering challenges. | Rahimizadeh2023, Herazo-Romero2025 | "To eliminate non-specific adsorption... ensure the orientation, accessibility, reactivity" — Rahimizadeh2023 p.3 | verified |
| **Biosensor-adsorbent conflation risk** | Current DB `dna-aptamer.json` has `verification: "verified"` for mechanism but `source: "llm_inference"`. No adsorption performance data exists in the prototype. | prototypes_db/dna-aptamer.json | The prototype needs clear delineation: mechanism (verified from Li2021) vs adsorption evidence (only from Bilibana2022 RNA-GO and CN121588773A DNA-GC). | — |
| **Patent as source** | CN121588773A is a scanned Chinese patent (OCR-dependent). Performance data from figures (图3/图4) not numerically extracted. | CN121588773A | Mark as `scanned_patent`. Kd (0.25 nM) from text is reliable. qmax is qualitative only ("最大"). | **scanned_patical** |
| **RNA vs DNA aptamer** | Bilibana2022's RNA-GO uses RNA aptamer; all other aptamer sources are DNA. RNA is less stable but has different folding. | Bilibana2022 | RNA aptamer stability is a concern for water treatment. DNA aptamers are more practical. | verified |
| **Kd interpretation** | Kd from biosensors (Luo2021: 50 nM for MC-LR) ≠ adsorption Kd. Adsorption Kd from CN121588773A (0.25 nM for AFB1) is from SPR on actual adsorbent material. | Luo2021, CN121588773A | Only CN121588773A's Kd is from an adsorption context. Luo2021's Kd is from sensor calibration. | — |
| **Inferred-only boundaries** | Existing DB `mechanisms[0].causal_chain.boundary_conditions` contains `llm_inferred` entries with no source. | prototypes_db/dna-aptamer.json | These must NOT be upgraded to `verified` without literature support. | **llm_inferred** |

---

## 7. Candidate Queue Items Table

### 7.1 Qualified Candidates (have source path + locator + quote + metric type)

| Queue ID | Source File | Field Path | Metric | Value | Quote | Locator | Evidence Label | Recommended Action |
|----------|------------|-----------|--------|-------|-------|---------|---------------|-------------------|
| CQ-01 | `2022-Bilibana-aptamer-review.pdf` | `mechanisms[?].performance_data` (new entry) | qmax | 1.44 mg/g | "maximum adsorption capacity of 1.44 mg g⁻¹" | p.11 §4 | **single_source** | Add to prototype with `source_tier: "single_source"` — needs independent replication |
| CQ-02 | `2022-Bilibana-aptamer-review.pdf` | — | removal% | >95% | "more than 95% of MC-LR was absorbed" | p.11 §4 | **single_source** | Add with caveat: 综述引用，非原创实验 |
| CQ-03 | `2022-Bilibana-aptamer-review.pdf` | — | selectivity | >95% vs <12% | "only less than 12% of the other toxins... were captured" | p.11 §4 | **single_source** | High-value selectivity evidence |
| CQ-04 | `2022-Bilibana-aptamer-review.pdf` | — | regeneration | 5 cycles, -10% | "adsorption capacity was diminished after five regeneration cycles" | p.11 §4 | **single_source** | Regeneration evidence — limited cycles |
| CQ-05 | `2026-CN121588773A-aptamer-aflatoxin-adsorbent.pdf` | — | Kd | 0.25 nM | "DNA-GC与AFB1的亲和力低至0.25 nM" | p.6 [0045] | **scanned_patent** | Strong affinity evidence; mark as scanned patent |
| CQ-06 | `2026-CN121588773A-aptamer-aflatoxin-adsorbent.pdf` | — | qmax (qualitative) | "最大" vs 5 materials | "结果显示DNA-GC拥有最大的毒素吸附能力" | p.6 [0045] | **scanned_patent** | Qualitative only — cannot use as numerical qmax |

### 7.2 Disqualified / Excluded Candidates

| Queue ID | Source | Reason for Exclusion |
|----------|--------|---------------------|
| — | Li2021 | Review — no adsorption data. Detection/biosensor only. |
| — | Wang2021 | Review — no adsorption data. Detection/biosensor only. |
| — | Luo2021 | SERS signal-off detection. LOD/Kd are sensor metrics, not adsorption. |
| — | Rahimizadeh2023 | Review — pathogen biosensor. No adsorption/capture performance. |
| — | Asmare2024 | Electrochemical biosensor for ciprofloxacin. No adsorption. |
| — | Wu2023 | MD simulation only. No experimental adsorption data. |
| — | Yan2025 | Plasmonic biosensor. LOD only. |
| — | Herazo-Romero2025 | Magnetic pull-down for E. coli detection. Microbial capture ≠ dissolved pollutant adsorption. |
| — | Vogiazi2021 | Biosensor. No extraction JSON available. |

---

## 8. Summary of Findings

### 8.1 Current Prototype Status

The existing `prototypes_db/dna-aptamer.json` has:
- **1 mechanism** with `source: "llm_inference"` and `verification: "verified"` — this is contradictory. The mechanism citation is from Li2021 (a review), but the `source_file` reference is correct. The mechanism itself (SELEX + molecular recognition) is well-established across multiple sources.
- **0 performance_data** entries — correct, as no adsorption data existed before this audit.
- **0 narrative entries** — should be populated.
- **`provenance_summary: n_papers: 0, n_verified: 0`** — needs update.
- **`enrichment/dna-aptamer.json`** is empty `{}`.

### 8.2 Evidence Landscape

| Category | Count | Sources |
|----------|-------|---------|
| Biosensor-only (LOD/Kd from sensors) | 9 | Li2021, Wang2021, Luo2021, Rahimizadeh2023, Asmare2024, Wu2023, Yan2025, Herazo-Romero2025, Vogiazi2021 |
| Adsorption/capture evidence | 2 | Bilibana2022 (RNA-GO), CN121588773A (DNA-GC) |
| Mechanism evidence (multi-source verified) | 5+ | Li2021, Wang2021, Wu2023, Rahimizadeh2023, Asmare2024, Herazo-Romero2025 |
| Adsorption performance (numerical qmax) | 1 | Bilibana2022 only (1.44 mg/g) |
| Adsorption performance (Kd from SPR on adsorbent) | 1 | CN121588773A only (0.25 nM) |
| In vivo adsorption evidence | 1 | CN121588773A only (mouse models) |

### 8.3 Critical Gaps

1. **No independent replication** of RNA-GC qmax (1.44 mg/g) — single_source from review
2. **No numerical qmax** for DNA-GC — qualitative "largest" comparison only
3. **No heavy metal adsorption data** — all heavy metal aptamer work is biosensor-only
4. **No antibiotic adsorption data** — ciprofloxacin aptamer is biosensor-only
5. **No pathogen adsorption data** — E. coli work is magnetic pull-down detection
6. **Regeneration data limited** — only RNA-GO has 5-cycle data
7. **Matrix effects unknown** — most data from buffer/pure water
8. **Patent is scanned** — OCR-dependent, needs human verification for figure data

### 8.4 Recommended Next Steps for Codex

1. **Update `prototypes_db/dna-aptamer.json`** mechanism `source` field from `"llm_inference"` to `"literature"` with proper multi-source citation
2. **Add `performance_data` entries** from CQ-01 through CQ-06 with appropriate `source_tier` labels
3. **Update `provenance_summary`** to reflect 2 adsorption-relevant papers + 9 biosensor-only papers
4. **Mark boundaries**: `needs_human_decision` for matrix effects and regeneration; `single_source` for RNA-GO qmax; `scanned_patent` for CN121588773A data
5. **Do NOT add** any biosensor LOD/Kd values as adsorption performance evidence
6. **Consider** whether the prototype scope should be narrowed to "aptamer-functionalized adsorbents" rather than "DNA aptamers" broadly

---

## 9. Compliance Checklist

- [x] No modification to `prototypes_db/*.json` (read-only audit)
- [x] No `tools/build_prototypes_db.py` execution
- [x] No git commits
- [x] No modification to `docs/optimization-v1/phase5-chains.md`, `tools/litextract`, `tools/verify_adrmats_delivery.py`
- [x] All missing/scanned/uncertain sources marked with appropriate labels
- [x] No `missing_pdf` upgraded to `verified`
- [x] No `scanned_patent` upgraded to `verified`
- [x] No `single_source` upgraded to `verified`
- [x] No `inferred_only` upgraded to `verified`
- [x] Only source-mismatched or directly-supported boundaries suggested as `wrong_source` or `hard_do_not`
- [x] Every candidate queue item has: source_file, locator, quote, metric_type
- [x] Biosensor literature NOT conflated with adsorption evidence
- [x] Output written to `docs/optimization-v1/review-full-audit-openclaw-dna-aptamer-evidence-build.md`
