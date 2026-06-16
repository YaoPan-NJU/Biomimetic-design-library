status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-17T00:09:36+0800

---

# Fish-Scale HAp Cleanup Evidence Package

**Audit date:** 2026-06-17
**Worker:** OpenClaw/mimo-v2.5
**Scope:** `prototypes_db/fish-scale-hydroxyapatite.json` + enrichment mirror + preflight audit + decision queue + boundary register
**Hard limits:** No modification of `prototypes_db/*.json`. No `tools/build_prototypes_db.py` execution. No git commit.

---

## Literature And File Mapping

| source_family | local_pdf_or_cache_path | extraction_json_path | text_or_visual | rows_supported | scope_class | confidence | notes |
|---|---|---|---|---|---|---|---|
| fish-scale HAp patent (CN114849640A) | `仿生文献库/专利/2022-CN114849640A-羟基磷灰石-吸附-染料 2.pdf` + `_visual_cache.json` (stage0 only) | `tools/litextract/outputs/extractions/专利/json/2022-CN114849640A-羟基磷灰石-吸附-染料.json` | text (pdftotext pages 5-6) | performance_data[7-17] (11 rows) | fish-scale HAp adsorption — **primary evidence** | high | Pages 5-6 extracted via visual_cache stage0 pages_text; quotes verified against [0045]-[0063] paragraph locators. |
| biomineralization patent (CN113275374A) | `仿生文献库/3rd/第三波-仿生吸附专利/2021-CN113275374A-biomineralization-heavy-metal.pdf` + `_visual_cache.json` (visual_markdown pages 1-11) | `tools/litextract/outputs/extractions/第三波/json/2021-CN113275374A-biomineralization-heavy-metal.json` | visual (OCR/markdown pages 5-7) | performance_data[18-21] (4 rows) | MICP bacteria + HAP co-immobilization — **not fish-scale HAp alone** | medium | Visual cache contains full page OCR including Table 1 (page 6). This is MICP biomineralization, not fish-scale extracted HAp. |
| fish-scale biochar (Dou2021) | `仿生文献库/论文/第4组-生物矿化/2021-Dou-hydrophobic-porous-biochar-adsorption 2.pdf` + `_visual_cache 2.json` (pages 6-8) | `tools/litextract/outputs/extractions/论文/json/2021-Dou-hydrophobic-porous-biochar-adsorption.json` | text+visual | performance_data[0-1], mechanisms[54-55], engineering_constraints[11] | fish-scale-derived **porous biochar** for CIP — **not HAp adsorbent** | high | HAp removed during biochar preparation. Strong evidence but wrong prototype scope. |
| rice-husk HAp-biochar (Wu2022) | `仿生文献库/论文/第3组-多孔结构/2022-Wu-porous-hierarchical-hydroxyapatite-biochar 2.pdf` | `tools/litextract/outputs/extractions/论文/json/2022-Wu-porous-hierarchical-hydroxyapatite-biochar.json` | text | performance_data[2-6] (5 rows) | HAp-tailored hierarchical porous biochar for Cd/Pb — **rice husk feedstock** | high | DOI 10.1016/j.jhazmat.2022.129330. Biochar feedstock is rice husk, not fish scale. |
| marine-shell/abalone HA (Wang2021) | `仿生文献库/3rd/第C组-零数据原型/C4 - 扇贝壳（3 篇）/2021-Wang-shell-congo-red-adsorption.pdf` | N/A (row in prototypes_db only) | text | performance_data[22-23] (2 rows) | abalone HA microspheres for Congo Red — **marine-shell, not fish-scale** | high | DOI 10.1016/j.matlet.2021.130573. Source is abalone shell, not fish scale. |
| generic shell-powder review (Zhang2024) | `仿生文献库/3rd/第B组-新方向/B2-生物矿化模板/2024-Zhang-shell-powder-heavy-metal-review.pdf` | N/A | text | performance_data[24-28] (5 rows), mechanisms[88] | modified shell powder heavy-metal review — **generic shell, not fish-scale** | medium | DOI 10.3969/j.issn.1672-7304.2024.02.0011. Generic shell-powder review, not fish-scale-specific. |
| nano-HAp review (Balasooriya2022) | `仿生文献库/论文/第4组-生物矿化/2022-Balasooriya-hydroxyapatite-adsorption-adsorbent-heavy-metal-review 2.pdf` + `_visual_cache` | `tools/litextract/outputs/extractions/论文/json/2022-Balasooriya-hydroxyapatite-adsorption-adsorbent-heavy-metal-review.json` | text | mechanisms[54] causal_chain | general nano-HAp heavy-metal adsorption mechanisms | high | DOI 10.3390/ma14202324. Useful for HAp mechanism background, but not fish-scale-specific. |
| superwetting/membrane/Janus reviews (multiple) | multiple (10.1007/s10853-022-07945-8; 10.3390/membranes13080727; 10.1007/s11783-021-1515-2; 10.1021/acsami.0c18794; 10.34133/2022/9895418; 10.1002/smll.202204624; 10.16490/j.cnki.issn.1001-3660.2023.02.015) | multiple extraction JSONs | text | mechanisms[0-53], mechanisms[56-86], engineering_constraints[0-10] | **wrong_source** — superwetting/membrane/oil-water separation | high | ~85 mechanisms + 10 engineering constraints from membrane/superwetting literature. Not fish-scale HAp adsorption. |

---

## Decision-Ready Candidate Table

| candidate_id | target_json | field_path | claim_summary | local_source | locator | quote | evidence_label | recommended_action | yao_decision_needed |
|---|---|---|---|---|---|---|---|---|---|
| FISH-CD-001 | fish-scale-hydroxyapatite.json | performance_data[7] | Optimal acid fuchsin adsorption capacity: 478 mg/g by fish-scale extracted HAp | CN114849640A PDF p.5 | [0045] | "称取5.0mg鱼鳞羟基磷灰石吸附剂于含25mL，浓度为100mg/L的酸性品红溶液的锥形瓶中，30℃，180rpm条件下震荡24h后...酸性品红的吸附能力达478mg/g" | supported | **keep** — strongest fish-scale HAp evidence; condition-scoped (100 mg/L, 5 mg HAp, 25 mL, 30°C, 24 h) | no |
| FISH-CD-002 | fish-scale-hydroxyapatite.json | performance_data[8] | HCl 0.1 mol/L → 478 mg/g (duplicate of optimal) | CN114849640A PDF p.5 | [0045] | Same quote as FISH-CD-001: "酸性品红的吸附能力达478mg/g" | supported | **merge** into FISH-CD-001 as condition variant (same 实施例1, same 478 mg/g) | no |
| FISH-CD-003 | fish-scale-hydroxyapatite.json | performance_data[9] | HCl 0.5 mol/L → 386 mg/g | CN114849640A PDF p.5 | [0048] | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达386mg/g" | supported | **keep** as condition-variant row (HCl concentration effect) | no |
| FISH-CD-004 | fish-scale-hydroxyapatite.json | performance_data[10] | HCl 1 mol/L → 356 mg/g | CN114849640A PDF p.5 | [0051] | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达356mg/g" | supported | **keep** as condition-variant row | no |
| FISH-CD-005 | fish-scale-hydroxyapatite.json | performance_data[11] | NaOH step1 50°C → 423 mg/g | CN114849640A PDF p.5 | [0054] | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达423mg/g" | supported | **keep** as condition-variant row | no |
| FISH-CD-006 | fish-scale-hydroxyapatite.json | performance_data[12] | NaOH step1 70°C (optimal) → 478 mg/g | CN114849640A PDF p.5 | [0045] | Same quote as FISH-CD-001 (实施例1 is the 70°C optimal) | supported | **merge** into FISH-CD-001 (same 实施例1, same 478 mg/g) | no |
| FISH-CD-007 | fish-scale-hydroxyapatite.json | performance_data[13] | NaOH step1 100°C → 450 mg/g | CN114849640A PDF p.5 | [0057] | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达450mg/g" | supported | **keep** as condition-variant row | no |
| FISH-CD-008 | fish-scale-hydroxyapatite.json | performance_data[14] | Freeze-drying → 478 mg/g | CN114849640A PDF p.5 | [0045] | Same quote as FISH-CD-001 (实施例1 uses freeze-drying) | supported | **merge** into FISH-CD-001 (same 实施例1) | no |
| FISH-CD-009 | fish-scale-hydroxyapatite.json | performance_data[15] | Hot-air drying → 430 mg/g | CN114849640A PDF p.6 | [0060] | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达430mg/g" | supported | **keep** as condition-variant row | no |
| FISH-CD-010 | fish-scale-hydroxyapatite.json | performance_data[16] | Air-drying → 462 mg/g | CN114849640A PDF p.6 | [0063] | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达462mg/g" | supported | **keep** as condition-variant row | no |
| FISH-CD-011 | fish-scale-hydroxyapatite.json | performance_data[17] | Minimum capacity: 356 mg/g (HCl 1 mol/L) | CN114849640A PDF p.5 | [0051] | Same quote as FISH-CD-004 | supported | **remove** — redundant summary row already covered by FISH-CD-004 | no |
| FISH-CD-012 | fish-scale-hydroxyapatite.json | performance_data[0] | Fish-scale biochar DPBC: Langmuir qmax 1013.96 mg/g for CIP | Dou2021 PDF p.6 | 3.6节 | "Its BET-SSA and total pore volume (PV) were 3370 m² g⁻¹ and 1.91 cm³ g⁻¹" + isotherm data | supported | **needs_human_decision** — strong fish-scale-derived evidence, but material is biochar (HAp removed), not HAp | yes |
| FISH-CD-013 | fish-scale-hydroxyapatite.json | performance_data[1] | Fish-scale biochar DPBC: fixed-bed dynamic capacity 880.53 mg/g for CIP | Dou2021 PDF p.7 | 3.7节 | "the maximum adsorption capacity (880.53 mg g⁻¹) was found at the lowest flow rate" | supported | **needs_human_decision** — same scope issue as FISH-CD-012 | yes |
| FISH-CD-014 | fish-scale-hydroxyapatite.json | performance_data[2-6] | HA-3HPB (rice-husk biochar + HAp): Cd 88.1 mg/g, Pb 110.2 mg/g | Wu2022 PDF p.7 | Section 3.4, Table 1 | "Data modeling showed that the HA-3HPB showed higher adsorption capacity for Pb(II) (110.22 mg/g) compared to Cd(II) (88.06 mg/g)" | supported | **keep_soft_or_reassign** — HAp/biochar evidence but rice-husk feedstock, not fish-scale | yes |
| FISH-CD-015 | fish-scale-hydroxyapatite.json | performance_data[18-21] | MICP bacteria + HAP: Cd²⁺ 98.52%, Pb²⁺ 99.49% removal | CN113275374A visual_cache p.6 | [0042] Table 1 | "混合比例1:1:1, Cd²⁺初始浓度10mg/L, 去除率98.52%" / "Pb²⁺初始浓度100mg/L, 去除率99.49%" | needs_human_decision | **needs_human_decision** — values readable from visual cache, but this is MICP bacteria biomineralization, not fish-scale extracted HAp. Also pollutant fields empty in DB. | yes |
| FISH-CD-016 | fish-scale-hydroxyapatite.json | performance_data[22-23] | Abalone HA microspheres: Congo Red qmax 495.5626 mg/g | Wang2021 PDF | Abstract | "abalone HA microspheres...495.5626 mg/g" | wrong_source | **remove_or_reassign** — marine-shell/abalone, not fish-scale | yes |
| FISH-CD-017 | fish-scale-hydroxyapatite.json | performance_data[24-28] | Modified shell powder: Pb 57.79 mg/g, generic shell HAp | Zhang2024 PDF | Section 1.2, 2.1, 2.3 | Various shell-powder review values | wrong_source | **remove_or_reassign** — generic shell-powder review, not fish-scale | yes |
| FISH-CD-018 | fish-scale-hydroxyapatite.json | mechanisms[54] | "八重协同吸附机制" — HAp heavy-metal adsorption mechanisms | Balasooriya2022 + Dou2021 | Mixed sources | Mixed DOI/name in current JSON | partial | **narrow_and_fix_source** — mechanism is valid for general HAp but label mixes Dou2021 biochar mechanism with Balasooriya2022 HAp review; DOI currently points to Dou2021 not Balasooriya2022 | yes |
| FISH-CD-019 | fish-scale-hydroxyapatite.json | mechanisms[55] | Hydrophobic interaction evidence for CIP on DPBC | Dou2021 PDF p.7-8 | 3.8节 | "the dominant hydrophobic interaction, together with pore filling, cation exchange..." | supported | **needs_human_decision** — valid mechanism but belongs to biochar/CIP, not HAp/heavy-metal | yes |
| FISH-CD-020 | fish-scale-hydroxyapatite.json | engineering_constraints[11] | Regeneration: 5 cycles → 498 mg/g | Dou2021 PDF | regeneration section | "5次热处理再生后容量降至498 mg/g(仍较高水平)" | supported | **needs_human_decision** — valid but belongs to biochar/CIP regeneration, not HAp | yes |
| FISH-CD-021 | fish-scale-hydroxyapatite.json | mechanisms[87] | MICP urea hydrolysis / CaCO₃ precipitation | CN113275374A | [0027]-[0028] | "脲酶水解尿素...CO₃²⁻+Ca²⁺→CaCO₃↓" | wrong_source | **remove_or_reassign** — MICP mechanism, not fish-scale HAp adsorption | yes |
| FISH-CD-022 | fish-scale-hydroxyapatite.json | mechanisms[88] | Generic adsorption 3-step mechanism (film diffusion → intra-particle → surface reaction) | Zhang2024 PDF | Section 2.3 | "(1)膜扩散：重金属离子从液相扩散到改性贝壳粉外表面；(2)粒内扩散..." | wrong_source | **remove_or_reassign** — generic shell-powder review mechanism, not fish-scale specific | yes |

---

## CN114849640A Patent Locator Table

| row_index | parameter | value | unit | patent_locator | quote | duplicate_semantics | recommended_action |
|---|---|---|---|---|---|---|---|
| 7 | 鱼鳞羟基磷灰石对酸性品红最大吸附容量（最优） | 478 | mg/g | p.5, [0045], 实施例1 | "称取5.0mg鱼鳞羟基磷灰石吸附剂于含25mL，浓度为100mg/L的酸性品红溶液的锥形瓶中，30℃，180rpm条件下震荡24h后...酸性品红的吸附能力达478mg/g" | **canonical** — this is the optimal condition row | **keep** as primary row |
| 8 | 盐酸浓度对吸附容量的影响-0.1mol/L | 478 | mg/g | p.5, [0045], 实施例1 | "配制0.1mol/L的盐酸溶液...酸性品红的吸附能力达478mg/g" | **exact duplicate** of row 7 — same 实施例1, same 478 mg/g, same conditions. The value 478 mg/g is the baseline/optimal result that appears across multiple variable groups because 实施例1 is the control. | **merge** into row 7; reframe as "HCl 0.1 mol/L (baseline condition) → 478 mg/g" |
| 9 | 盐酸浓度对吸附容量的影响-0.5mol/L | 386 | mg/g | p.5, [0048], 实施例2 | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达386mg/g" | **unique** — different HCl concentration, different result | **keep** — condition-variant (HCl effect) |
| 10 | 盐酸浓度对吸附容量的影响-1mol/L | 356 | mg/g | p.5, [0051], 实施例3 | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达356mg/g" | **unique** — lowest capacity in HCl series | **keep** — condition-variant |
| 11 | 第一步NaOH处理温度对吸附容量的影响-50°C | 423 | mg/g | p.5, [0054], 实施例4 | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达423mg/g" | **unique** | **keep** — condition-variant (NaOH temp effect) |
| 12 | 第一步NaOH处理温度对吸附容量的影响-70°C（最优） | 478 | mg/g | p.5, [0045], 实施例1 | Same quote as row 7 | **exact duplicate** — 实施例1 is the 70°C condition; this is the same optimal result | **merge** into row 7; note is same 实施例1 |
| 13 | 第一步NaOH处理温度对吸附容量的影响-100°C | 450 | mg/g | p.5, [0057], 实施例5 | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达450mg/g" | **unique** | **keep** — condition-variant |
| 14 | 干燥方式对吸附容量的影响-冷冻干燥 | 478 | mg/g | p.5, [0045], 实施例1 | Same quote as row 7 | **exact duplicate** — 实施例1 uses freeze-drying | **merge** into row 7; note drying method |
| 15 | 干燥方式对吸附容量的影响-热风烘干 | 430 | mg/g | p.6, [0060], 实施例6 | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达430mg/g" | **unique** | **keep** — condition-variant (drying effect) |
| 16 | 干燥方式对吸附容量的影响-自然风干 | 462 | mg/g | p.6, [0063], 实施例7 | "本实施例中吸附条件与实施例1中条件相同。酸性品红的吸附能力达462mg/g" | **unique** | **keep** — condition-variant |
| 17 | 吸附容量最低值 | 356 | mg/g | p.5, [0051], 实施例3 | Same quote as row 10 | **redundant summary** — already covered by row 10 | **remove** — summary row adds no new information |

### Duplicate Semantics Analysis

The repeated 478 mg/g values (rows 7, 8, 12, 14) are **exact duplicates** — they all refer to 实施例1, which is the optimal condition (0.1 mol/L HCl, 70°C NaOH, freeze-drying). The patent structure is: each new "实施例" varies ONE variable while keeping others constant from 实施例1. When the variable being tested happens to match 实施例1's condition (e.g., 0.1 mol/L HCl, 70°C, freeze-drying), the result is identical (478 mg/g). This is NOT coincidence or different measurements — it's the same experiment referenced as the control baseline across three variable groups.

**Safe to consolidate into 8 unique rows:**
1. **Baseline/optimal** (实施例1): 478 mg/g — the canonical result
2. HCl 0.5 mol/L (实施例2): 386 mg/g
3. HCl 1 mol/L (实施例3): 356 mg/g
4. NaOH 50°C (实施例4): 423 mg/g
5. NaOH 100°C (实施例5): 450 mg/g
6. Hot-air drying (实施例6): 430 mg/g
7. Air-drying (实施例7): 462 mg/g
8. (Optional) Minimum capacity note: 356 mg/g at HCl 1 mol/L

---

## Wrong-Source / Reassign Range Table

| range_id | field_path_range | current_source_family | source_domain | why_wrong_or_soft | evidence_locator | quote | recommended_action |
|---|---|---|---|---|---|---|---|
| WS-001 | mechanisms[0-8] | Superwetting/membrane reviews (10.1007/s10853-022-07945-8) | Membrane science, oil-water separation | Mechanisms describe superhydrophobic surfaces, electrospun membranes, tannic-acid-metal complex membranes — not HAp adsorption | title/domain check | Source title: "Recent advances in superwetting materials..." | **remove** — entire block is membrane/superwetting domain |
| WS-002 | mechanisms[9-17] | Membrane distillation review (10.3390/membranes13080727) | Membrane science, MD/fouling | Mechanisms describe ZnO/PVDF membranes, POSS-rGO/PVDF, omniphobic membranes, Janus membranes for MD — not HAp | title/domain check | Source title includes "Membranes" journal | **remove** — membrane MD domain |
| WS-003 | mechanisms[18-30] | Cellulose superhydrophobic review (10.1007/s11783-021-1515-2) | Cellulose-based superhydrophobic membranes | Mechanisms describe cellulose support materials, polymer coatings, crosslinking, Janus membranes — not HAp | title/domain check | Source DOI: s11783 = Journal of Polymers and the Environment, cellulose membrane focus | **remove** — cellulose membrane domain |
| WS-004 | mechanisms[31-43] | ACS AMI superwetting review (10.1021/acsami.0c18794) | Superwetting surfaces for oil-water separation | Mechanisms describe PDMS coatings, ZnO nanorods, graphene aerogels, PANI/TiO₂ mesh, CeO₂ photocatalysis — not HAp | title/domain check | Source: ACS Applied Materials & Interfaces, special wettability focus | **remove** — superwetting surface domain |
| WS-005 | mechanisms[44-53] | Femtosecond laser superwettability review (10.34133/2022/9895418) | Femtosecond laser surface engineering | Mechanisms describe laser-structured silicon/PDMS/PTFE superhydrophobic surfaces — not HAp | title/domain check | Source: eLight, femtosecond laser focus | **remove** — laser surface engineering domain |
| WS-006 | mechanisms[56-72] | Small (WeChat) superwetting review (10.1002/smll.202204624) | Superwetting on-demand separation | Mechanisms describe bioinspired superwetting materials, Janus membranes, smart responsive membranes — not HAp | title/domain check | Source: Small journal, superwetting focus | **remove** — superwetting separation domain |
| WS-007 | mechanisms[73-86] | CNKI superwetting membrane review (10.16490/j.cnki.issn.1001-3660.2023.02.015) | 超浸润膜-油水分离 | Mechanisms describe superhydrophobic/superoleophilic membranes, pH/thermal responsive membranes — not HAp | title/domain check | Source DOI: CNKI surface coating journal, membrane focus | **remove** — membrane/oil-water separation domain |
| WS-008 | engineering_constraints[0-1] | Superwetting membrane reviews | Smart responsive membranes, PVDF-SiO₂ superhydrophobic | Constraints about TiO₂ photocatalysis, pH response, PVDF-SiO₂ cycles — not HAp | title/domain check | Source DOIs: 10.1007/s10853-022-07945-8 | **remove** — membrane domain |
| WS-009 | engineering_constraints[2] | Membrane MOF review (10.3390/membranes13080727) | MOF water stability for membranes | MOF ligand basicity/stability — not HAp | title/domain check | Source: Membranes journal | **remove** — MOF/membrane domain |
| WS-010 | engineering_constraints[3-6] | Cellulose superhydrophobic review (10.1007/s11783-021-1515-2) | Cellulose membrane crosslinking/stability | Crosslinking agents, dip-dry cycles, harsh condition testing for cellulose membranes — not HAp | title/domain check | Source: s11783 | **remove** — cellulose membrane domain |
| WS-011 | engineering_constraints[7-10] | ACS AMI superwetting review (10.1021/acsami.0c18794) | Superwetting fabric/mesh flux/stability | Fe-PA/OTMS/PI flux, PTFE cycles, PANI/TiO₂ mesh cycles, UV+pH switching — not HAp | title/domain check | Source: acsami.0c18794 | **remove** — superwetting surface domain |
| WS-012 | performance_data[22-23] | Wang2021 marine-shell HA | Abalone shell HA microspheres for Congo Red | Material is abalone (鲍鱼) shell, not fish-scale. DOI 10.1016/j.matlet.2021.130573 | Wang2021 PDF abstract | "abalone HA microspheres...495.5626 mg/g" | **remove_or_reassign** to oyster-shell or marine-shell prototype |
| WS-013 | performance_data[24-28] | Zhang2024 generic shell-powder review | Modified shell powder heavy-metal review | Generic shell-powder review values, not fish-scale specific. DOI 10.3969/j.issn.1672-7304.2024.02.0011 | Zhang2024 PDF Section 1.2, 2.1, 2.3 | Various shell-powder values | **remove_or_reassign** to shell-powder prototype |
| WS-014 | mechanisms[87] | CN113275374A MICP patent | MICP urea hydrolysis / CaCO₃ precipitation | MICP mechanism is about bacteria-induced CaCO₃, not fish-scale HAp adsorption | CN113275374A [0027]-[0028] | "脲酶水解尿素...CO₃²⁻+Ca²⁺→CaCO₃↓" | **remove_or_reassign** to iron-oxidizing-bacteria or biomineralization-template |
| WS-015 | mechanisms[88] | Zhang2024 generic shell-powder review | 3-step adsorption mechanism | Generic adsorption mechanism from shell-powder review, not fish-scale specific | Zhang2024 Section 2.3 | "(1)膜扩散... (2)粒内扩散... (3)表面吸附反应" | **remove_or_reassign** — too generic to be fish-scale specific |

---

## Boundary / DO-NOT Candidate Table

| boundary_id | target_field | boundary_type_candidate | rationale | source | locator | quote | evidence_label | recommended_action |
|---|---|---|---|---|---|---|---|---|
| B02-FISH-001 | mechanisms[0-53], mechanisms[56-86], engineering_constraints[0-10] | hard_do_not | ~85 mechanisms + 10 engineering constraints are from superwetting/membrane/Janus/oil-water separation literature. Using these as fish-scale HAp adsorption evidence would drive wrong design recommendations (oil-water separation, superhydrophobic coatings, Janus membranes). | multiple membrane/superwetting sources | title/domain check | Source domains are membrane/superwetting, not HAp adsorption | wrong_source | **keep as hard_do_not** — these must not be used as HAp adsorption evidence. Remove/reassign after Yao approval. |
| B02-FISH-002 | performance_data[0-1], mechanisms[55], engineering_constraints[11] | soft_boundary | Dou2021 supports fish-scale-derived porous biochar for CIP, not HAp as final adsorbent. HAp-based inorganics are removed during biochar preparation. | Dou2021 PDF | abstract; methods | "fish scale-based porous activated biochar" | supported | **keep as soft_boundary** — decide whether to expand prototype scope to include fish-scale biochar, or move to a separate prototype. |
| B02-FISH-003 | performance_data[7-17] | soft_boundary | CN114849640A acid-fuchsin values are condition-specific: 100 mg/L dye, 5 mg HAp, 25 mL solution, 30°C, 24 h. Do not generalize 478 mg/g to other dyes or contact times. | CN114849640A PDF | [0045]-[0063] | "100mg/L...酸性品红...30C...24h" | supported | **keep as soft_boundary** — strong fish-scale HAp evidence but condition-scoped |
| B02-FISH-004 | performance_data[18-21] | knowledge_gap | CN113275374A values are now readable from visual cache, but the patent describes MICP bacteria + HAP co-immobilization, not fish-scale extracted HAp alone. Also, DB has empty pollutant fields. | CN113275374A visual_cache p.6 | Table 1 | "混合比例1:1:1, Cd²⁺初始浓度10mg/L, 去除率98.52%" | needs_human_decision | **upgrade to needs_human_decision** — values are verified from OCR but scope is MICP, not fish-scale HAp alone. Decide: keep as biomineralization evidence, or remove. |
| B02-FISH-005 | performance_data[22-23] | hard_do_not | Marine-shell/abalone HA Congo Red values must not be used as fish-scale HAp evidence. | Wang2021 PDF | abstract | "abalone HA microspheres...495.5626 mg/g" | wrong_source | **keep as hard_do_not** — remove/reassign after Yao approval. |
| B02-FISH-006 | mechanisms[54].causal_chain.boundary_conditions | knowledge_gap | HAp pH dissolution boundary exists in general literature, but this JSON row has no direct quote for its specific wording. | Balasooriya2022 or Jaffar2024 | mechanism/pH sections | N/A | partial | **keep as knowledge_gap** — source and quote before converting into a boundary. |
| B02-FISH-007 | performance_data[24-28], mechanisms[88] | hard_do_not | Generic shell-powder review values and mechanisms must not be used as fish-scale HAp evidence. | Zhang2024 PDF | Section 1.2, 2.1, 2.3 | Generic shell-powder review values | wrong_source | **keep as hard_do_not** — remove/reassign after Yao approval. |
| B02-FISH-008 | mechanisms[87] | hard_do_not | MICP urea hydrolysis mechanism must not be used as fish-scale HAp adsorption evidence. | CN113275374A | [0027]-[0028] | "脲酶水解尿素...CO₃²⁻+Ca²⁺→CaCO₃↓" | wrong_source | **keep as hard_do_not** — remove/reassign to MICP prototype. |

---

## Source Family Classification for mechanisms[0-86] + engineering_constraints[0-11]

| index_range | source_family | domain | in_fish_scale_hap_scope | recommended_action |
|---|---|---|---|---|
| mechanisms[0-8] | 10.1007/s10853-022-07945-8 | Superwetting materials review | ❌ no | remove |
| mechanisms[9-17] | 10.3390/membranes13080727 | Membrane distillation/fouling review | ❌ no | remove |
| mechanisms[18-30] | 10.1007/s11783-021-1515-2 | Cellulose superhydrophobic membranes | ❌ no | remove |
| mechanisms[31-43] | 10.1021/acsami.0c18794 | Superwetting surfaces for oil-water separation | ❌ no | remove |
| mechanisms[44-53] | 10.34133/2022/9895418 | Femtosecond laser superwettability | ❌ no | remove |
| mechanisms[54] | Balasooriya2022 (10.3390/ma14202324) + Dou2021 (10.1016/j.chemosphere.2021.131962) | General HAp adsorption mechanisms + biochar CIP mechanism | ⚠️ partial — HAp mechanism valid, but label mixes biochar mechanism | narrow_and_fix_source |
| mechanisms[55] | Dou2021 (10.1016/j.chemosphere.2021.131962) | Hydrophobic interaction for CIP on biochar | ⚠️ scope — valid but biochar/CIP, not HAp/heavy-metal | needs_human_decision |
| mechanisms[56-72] | 10.1002/smll.202204624 | Superwetting on-demand separation (Small journal) | ❌ no | remove |
| mechanisms[73-86] | 10.16490/j.cnki.issn.1001-3660.2023.02.015 | 超浸润膜-油水分离 (CNKI) | ❌ no | remove |
| mechanisms[87] | CN113275374A | MICP urea hydrolysis / CaCO₃ | ❌ no | remove_or_reassign |
| mechanisms[88] | Zhang2024 (10.3969/j.issn.1672-7304.2024.02.0011) | Generic shell-powder adsorption mechanism | ❌ no | remove_or_reassign |
| engineering_constraints[0-1] | 10.1007/s10853-022-07945-8 | Smart responsive membranes | ❌ no | remove |
| engineering_constraints[2] | 10.3390/membranes13080727 | MOF water stability for membranes | ❌ no | remove |
| engineering_constraints[3-6] | 10.1007/s11783-021-1515-2 | Cellulose membrane crosslinking/stability | ❌ no | remove |
| engineering_constraints[7-10] | 10.1021/acsami.0c18794 | Superwetting fabric/mesh flux/stability | ❌ no | remove |
| engineering_constraints[11] | Dou2021 (10.1016/j.chemosphere.2021.131962) | Biochar/CIP regeneration | ⚠️ scope — valid but biochar, not HAp | needs_human_decision |

**Summary:** Of 89 mechanisms + 12 engineering constraints, only ~3 entries (mechanisms[54], mechanisms[55], engineering_constraints[11]) have any connection to fish-scale-derived materials, and even those are biochar/CIP evidence, not HAp heavy-metal evidence. The remaining ~98 entries are entirely wrong-source contamination from membrane/superwetting/oil-water-separation literature.

---

## Enrichment Cross-Check: enrichment/fish-scale-hydroxyapatite.json

The enrichment JSON mirrors the main JSON's mechanism entries. Key findings:

1. **Empty causal_chain fields:** All enrichment mechanism entries have empty `causal_chain` objects (empty text, basis, locator for all sub-fields). This is consistent with B06-ENR-001 (empty causal chains as placeholders).
2. **No wrong-source mirroring beyond main JSON:** The enrichment file mirrors the same source families as the main JSON. No additional wrong-source entries were found in enrichment that don't exist in the main file.
3. **Consistency with main JSON:** The enrichment mechanism names match the main JSON mechanism names 1:1. No orphan entries.
4. **No independent evidence:** Enrichment entries add no independent verification, quotes, or locators beyond what's in the main JSON.

**Recommendation:** Enrichment cleanup should follow main JSON cleanup. Do not use enrichment causal chains as evidence until populated.

---

## Open Questions

These are the items that require Yao or Codex decision:

1. **FISH-CD-012/013 (Dou2021 biochar scope):** Should fish-scale-derived porous biochar (CIP adsorption, qmax 1013.96 mg/g) be kept inside the fish-scale-hydroxyapatite prototype, moved to a separate fish-scale-biochar prototype, or removed entirely? The material is derived from fish scales but HAp is removed during preparation. **Decision: expand scope / split prototype / remove.**

2. **FISH-CD-014 (Wu2022 rice-husk HAp-biochar):** Should HAp-tailored hierarchical porous biochar (rice husk feedstock, Cd 88.1 / Pb 110.2 mg/g) be kept as soft background evidence, or reassigned to a general HAp-biochar prototype? **Decision: keep_soft / reassign.**

3. **FISH-CD-015 (CN113275374A MICP scope):** The patent values are now verified from visual cache (Cd²⁺ 98.52%, Pb²⁺ 99.49%), but this is MICP bacteria biomineralization with commercial HAP, not fish-scale extracted HAp. Should these rows be kept, reassigned to iron-oxidizing-bacteria or biomineralization-template, or removed? **Decision: keep / reassign / remove.**

4. **FISH-CD-016/017 (Wang2021 abalone + Zhang2024 shell-powder):** Confirm removal of abalone HA and generic shell-powder rows. These are clearly wrong-source. **Decision: approve removal.**

5. **FISH-CD-018 (mechanisms[54] source fix):** The "八重协同吸附机制" entry currently cites Dou2021 DOI but the mechanism content comes from Balasooriya2022. Should the DOI be corrected to Balasooriya2022 (10.3390/ma14202324) and the label narrowed to "nano-HAp heavy-metal adsorption mechanisms"? **Decision: fix source / keep as-is / remove.**

6. **FISH-CD-019/020 (Dou2021 mechanism/regeneration):** Should the hydrophobic interaction mechanism (mechanisms[55]) and regeneration constraint (engineering_constraints[11]) be kept inside fish-scale-hydroxyapatite with a scope caveat, or moved/removed with the biochar scope decision? **Decision depends on Q1 above.**

7. **Mechanism/constraint mass removal:** Approve removal of ~85 mechanisms (indices 0-53, 56-86) and ~10 engineering constraints (indices 0-10) that are entirely wrong-source (membrane/superwetting/oil-water separation). This is the single largest cleanup action. **Decision: approve bulk removal.**

8. **performance_data consolidation:** Approve merging of 4 duplicate CN114849640A rows (indices 8, 12, 14 into index 7) and removal of 1 redundant summary row (index 17), reducing 11 patent rows to 7 unique condition-variant rows. **Decision: approve consolidation.**

---

## Audit Statistics

- **performance_data rows:** 29 total → 7 keep (CN114849640A unique), 4 merge/dedup, 1 remove (redundant summary), 2 needs_human_decision (Dou2021 biochar), 5 keep_soft (Wu2022 rice-husk), 4 needs_human_decision (CN113275374A MICP), 2 wrong_source (Wang2021 abalone), 5 wrong_source (Zhang2024 shell-powder)
- **mechanisms:** 89 total → ~3 need source fix/scope decision (indices 54, 55, 87-88), ~85 wrong_source removal (indices 0-53, 56-86)
- **engineering_constraints:** 12 total → 1 needs scope decision (index 11), 10 wrong_source removal (indices 0-10), 1 not deeply audited
- **enrichment:** All causal chains empty; no independent evidence; follows main JSON cleanup
- **Total Yao decisions needed:** 8 items (see Open Questions)
