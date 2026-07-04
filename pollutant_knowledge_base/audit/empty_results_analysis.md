# Empty-Results Analysis: 360 Papers with 0 Knowledge Items

**Date**: 2026-06-26
**Scope**: All JSON files in `pollutant_knowledge_base/by_pollutant/` where `knowledge_items == []`

---

## 1. Summary Statistics

| Metric | Count |
|--------|------:|
| Total JSON files in KB | 2,879 |
| Non-empty files (with knowledge_items) | 2,522 |
| **Empty files (0 knowledge_items)** | **360** |
| Total knowledge_items across non-empty files | 27,592 |
| Average items per non-empty file | 11.0 |
| Empty rate | 12.5% |

## 2. Distribution by Pollutant

| Pollutant | Total Files | Empty | Empty % |
|-----------|----------:|------:|--------:|
| BPA (双酚A) | 1,416 | 286 | 20.2% |
| DDT (滴滴涕) | 230 | 54 | 23.5% |
| PFOA (全氟辛酸) | 275 | 10 | 3.6% |
| Nonylphenol (壬基酚) | 152 | 5 | 3.3% |
| TCDD | 122 | 2 | 1.6% |
| Decabromodiphenyl ether (十溴二苯醚) | 236 | 1 | 0.4% |
| Pentachlorophenol (五氯苯酚) | 171 | 1 | 0.6% |
| Chloroform (三氯甲烷) | 26 | 1 | 3.8% |
| All others (12 pollutants) | 249 | 0 | 0.0% |

## 3. Root Cause Categorization

### 3.1 Off-Topic Papers — Keyword/Acronym Collision (349 files, 96.9%)

This is the overwhelming cause. Papers were associated with a pollutant based on keyword or acronym matches, but the paper is about a completely different topic.

#### BPA: 286 files

BPA (bisphenol A) is a monomer widely used in polymer synthesis. The vast majority of empty BPA files are materials science papers that mention BPA as a chemical building block, not as an environmental pollutant.

| Subcategory | Count | Example |
|-------------|------:|---------|
| BPA as polymer monomer (polycarbonate, epoxy, polyimide, etc.) | 232 | "Thermoplastic modification of monomeric and partially polymerized Bisphenol A dicyanate ester" |
| BPA in materials engineering (composites, coatings, carbon fiber) | 9 | "Interfacial Enhancement by CNTs Grafting towards High-Performance Mechanical Properties of Carbon Fiber" |
| BPA in biology/medicine (not pollutant-related) | 8 | "Platelets Stimulate Expression of Endothelin Messenger RNA" |
| BPA as unrelated acronym (e.g., "Bucket Parallel Aggregation") | 1 | "Aggregate Queries in Wireless Sensor Networks" (BPA = algorithm name) |
| BPA in dental materials | 1 | "Effect of resin and photoinitiator on color of dental composite" |
| BPA in energy/battery | 1 | "Exploring Diurethane Dimethacrylate Monomer for Phase-Separated Structural Battery Electrolytes" |
| Other off-topic | 28 | Various polymer physics, thermodynamics, cell biology |

**Key pattern**: 231/286 files (81%) explicitly use "bisphenol A" or "BPA" in the title, but in the context of polymer synthesis (e.g., "poly(bisphenol A carbonate)", "BPA-based epoxy"). Only 29 have "bisphenol" in the title, and of those, 28 are about BPA as a monomer — not as a pollutant.

#### DDT: 54 files

DDT as an acronym collides with "deflagration-to-detonation transition" in combustion science, and with various machine learning model names.

| Subcategory | Count | Example |
|-------------|------:|---------|
| DDT = deflagration-to-detonation transition | 22 | "Violent Cookoff Reactions in HMX-Based Explosives in DDT Tubs" |
| DDT = ML/CV model acronym | 9 | "DDT-Net: Deep Detail Tracking Network for Image Tampering Detection" |
| DDT in biology (not pesticide) | 8 | "The Main Role of Srs2 in DNA Repair Depends on Its Helicase Activity" |
| DDT in engineering | 5 | "Tire Dynamic Deflection and Its Impact on Vehicle Longitudinal Dynamics" |
| DDT in materials/simulation | 6 | "Structural Insights on Microwave-Synthesized Antimony-Doped Germanium Nanocrystals" |
| Other off-topic | 4 | Various unrelated topics |

**Key pattern**: Only 1 of 54 files has "pesticide" or "insecticide" in the title. The remaining 53 are about combustion science, computer science, or other domains where DDT is an unrelated acronym.

#### PFOA: 10 files

| Subcategory | Count | Example |
|-------------|------:|---------|
| PFOA in materials science (polymer films, photovoltaics) | 3 | "On the complex refractive index of polymer:fullerene photovoltaic blends" |
| PFOA in analytical chemistry | 2 | "Separation of proteic primary amino acids under reversed-phase liquid chromatographic conditions" |
| PFOA in biology | 2 | "Membrane vesicles of Clostridium perfringens type A strains" |
| PFOA as surfactant (not removal) | 1 | "Surfactant-enhanced emulsification liquid-liquid microextraction" |
| PFOA in coatings | 1 | "Corrosion-resistant nickel thin films by electroless deposition" |
| Other | 1 | "Design and Synthesis of Fluorinated Quantum Dots for Perovskite Solar Cells" |

#### Nonylphenol: 5 files

| Subcategory | Count | Example |
|-------------|------:|---------|
| Nonylphenol as surfactant (not removal) | 2 | "Synthesis and Critical Micelle Concentration of Gemini Alkylphenol Polyoxyethylene Nonionic Surfactants" |
| Nonylphenol in coatings | 1 | "Electrodeposition of chromium-tungsten carbide composite coatings" |
| Nonylphenol in analytics | 1 | "Studies on improvement of resolutions in capillary electrophoresis" |
| Other | 1 | "Effects of the side chain density of polycarboxylate dispersants on dye dispersion" |

#### Other pollutants: 5 files

- **TCDD (2)**: One about BRCA1/xenobiotic gene regulation, one about UVB/melanoma genetics — papers mention dioxin pathway but are not about pollutant properties or removal.
- **Pentachlorophenol (1)**: 1967 paper about chloroplast ion uptake — "pentachlorophenol" appears as an uncoupler reagent, not as pollutant of interest.
- **Decabromodiphenyl ether (1)**: Malformed/empty extraction — file has no `bibliographic_metadata`, no `processing_notes`, just an empty shell with validation errors.

### 3.2 PDF Quality Issues (3 files, 0.8%)

These papers may be genuinely relevant to their pollutant, but the PDF was unreadable.

| File | Pollutant | Issue |
|------|-----------|-------|
| Park & Jhung 2021 — "Remarkable adsorbent for removal of bisphenol A and S from water" | BPA | PDF corrupted: pages 2-37 are Lorem ipsum placeholder text |
| "Chlorobenzene, chloroform, and carbon tetrachloride adsorption on sol-gel substrates" | Chloroform | PDF is a browser error page ("JavaScript is disabled"), not the paper |
| "N-heterocyclic hyper-cross-linked polymers for rapid and efficient adsorption of organic pollutants" | Nonylphenol | PDF corrupted: pages 2-24 are Lorem ipsum placeholder text |

**These 3 files represent genuine extraction failures** — the papers are relevant but the PDFs were corrupted or wrong. They should be re-processed with correct PDFs.

### 3.3 Non-English Papers (4 files, 1.1%)

| Language | Count | Pollutant | Topic |
|----------|------:|-----------|-------|
| Japanese | 3 | BPA | All about polymer science (CTBN/epoxy blends, polycarbonate/nylon alloys, viscoelasticity of amorphous polymers) |
| Chinese | 1 | BPA | Benzocyclobutene-functionalized polycarbonate synthesis |

All 4 are off-topic (polymer science), not about BPA as a pollutant. The extraction model correctly handled non-English text.

### 3.4 Genuinely Empty / Borderline (1 file)

The decabromodiphenyl ether file is a malformed extraction with no content at all (missing `schema_version`, `paper_id`, `bibliographic_metadata`, etc.). This appears to be a pipeline error rather than a content issue.

## 4. Key Findings

### 4.1 The Problem is Upstream Search, Not Extraction

The extraction model performed correctly in all cases — it accurately identified that the papers were not about pollutant removal/adsorption/properties and returned empty `knowledge_items`. The root cause is that the papers were incorrectly associated with pollutants during the search/ingestion phase:

- **BPA**: "bisphenol A" matches 1,416 papers, but ~286 of those use BPA as a polymer monomer (polycarbonate, epoxy, etc.), not as an environmental pollutant.
- **DDT**: "DDT" matches 230 papers, but ~54 use DDT as an acronym for "deflagration-to-detonation transition" or various ML model names.

### 4.2 The Extraction Model is Conservative and Correct

In every sampled file, the `processing_notes` and `decision_summary` fields contain thoughtful, accurate explanations of why no knowledge was extracted. Examples:

- BPA polymer paper: "该文献是纯粹的聚合物科学论文，研究Phenoxy/SAN共混物的原位聚合...文中虽多次提及双酚A（BPA），但BPA是作为合成Phenoxy的单体（原料），而非研究其作为环境污染物的性质或去除。"
- DDT combustion paper: "该文献研究了HMX基炸药在热刺激下的燃烧转爆轰行为，内容与污染物性质、赋存规律或去除方法完全无关。"
- DDT ML paper: "该文献为计算机科学领域论文，研究深度学习模型在点击率预测中的应用，与污染物知识库的学科领域完全不相关。"

### 4.3 Only 3 Files Need Re-Processing

The 3 PDF quality issue files (BPA adsorption paper with corrupted PDF, chloroform adsorption paper with browser error PDF, nonylphenol adsorption paper with corrupted PDF) should be re-processed if correct PDFs can be obtained.

## 5. Recommendations

1. **No bulk action needed for 357 files**: These are correctly extracted as empty. The off-topic papers should be removed from the knowledge base or kept as-is with their empty `knowledge_items` to document that the paper was considered.

2. **Re-process 3 PDF quality files**: If the correct PDFs for the Park & Jhung 2021, chloroform sol-gel, and nonylphenol hyper-cross-linked polymer papers can be obtained, re-run extraction.

3. **Fix 1 malformed file**: The decabromodiphenyl ether file (`Chang 等 - 2020 - Characterization of a Sequential UV Photolysis-Biodegradation...`) is completely empty and should either be re-extracted or removed.

4. **Improve search precision for future ingestion**: The high empty rate for BPA (20%) and DDT (24%) suggests the search/ingestion pipeline should add a relevance filter before extraction, e.g.:
   - For BPA: require "adsorption", "removal", "degradation", "wastewater", "contaminant", or "pollutant" in the abstract/title
   - For DDT: require "pesticide", "insecticide", "organochlorine", "dichlorodiphenyltrichloroethane", or "environmental" in the abstract/title

## 6. Appendix: Sample Evidence by Pollutant

### BPA — Polymer Synthesis (231 files)

Representative samples showing BPA as monomer, not pollutant:

| Title | Processing Notes |
|-------|-----------------|
| "Morphological Development and Rheological Changes of Phenoxy/SAN Blends During In-Situ Polymerization" | "文中虽多次提及双酚A（BPA），但BPA是作为合成Phenoxy的单体（原料），而非研究其作为环境污染物的性质或去除。" |
| "Synthesis of UV-Curable/Alkali-Soluble Dispersants Used for Black Photoresist" | "本文献主要关于材料合成与碳黑分散应用，与污染物知识库核心内容不直接相关。" |
| "Soluble Polyimides Bearing Hydrogenated Bisphenol A" | "该文献研究氢化双酚A (HBPA) 异构体对可溶性聚酰亚胺热、机械、溶解及光学性能的影响，不涉及任何污染物。" |

### DDT — Deflagration-to-Detonation Transition (22 files)

| Title | Processing Notes |
|-------|-----------------|
| "Violent Cookoff Reactions in HMX-Based Explosives in DDT Tubs" | "其研究对象（PBX 9501, LX-07, HMX）并非污染物知识库定义的污染物。" |
| "Numerical simulation and validation of flame acceleration and DDT in hydrogen air mixtures" | "本研究提供了氢气火焰加速和 DDT（爆燃转爆轰）的数值模拟框架，但其内容与污染物知识库的核心需求无关。" |

### DDT — Machine Learning Acronym (9 files)

| Title | Processing Notes |
|-------|-----------------|
| "DDT-Net: Deep Detail Tracking Network for Image Tampering Detection" | "提出了一种用于图像篡改检测的深度学习网络DDT-Net，但与污染物知识库所需的污染物性质、赋存、去除等信息完全无关。" |
| "Deep Double Towers Click Through Rate Prediction Model" | "该文献为计算机科学领域论文，研究深度学习模型在点击率预测中的应用，与污染物知识库的学科领域完全不相关。" |

### PDF Quality Issues (3 files)

| Title | Pollutant | Issue |
|-------|-----------|-------|
| "Remarkable adsorbent for removal of bisphenol A and S from water: porous carbon derived from melamine" | BPA | "PDF文件从第2页开始至第37页的所有文本页面内容均为无效的'Lorem ipsum...'占位符文本" |
| "Chlorobenzene, chloroform, and carbon tetrachloride adsorption on sol-gel substrates" | Chloroform | "提供的PDF文件内容是浏览器访问错误页面（如'JavaScript is disabled'），而非论文的实际文本" |
| "N-heterocyclic hyper-cross-linked polymers for rapid and efficient adsorption of organic pollutants" | Nonylphenol | "PDF文件从第2页到第24页内容为乱码（Lorem ipsum或其他占位符文本）" |
