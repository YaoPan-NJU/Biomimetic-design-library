status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-16T15:45:00+08:00

# Batch 07: Parked And Registry Consistency Audit

## 1. Parked Item Audit — namib-beetle

### 1.1 Why Is namib-beetle Parked?

**Root cause: scope overlap + evidence weakness + no performance_data.**

| Factor | Evidence | Severity |
|--------|----------|----------|
| **Zero performance_data** | `performance_data: []` — no quantified adsorption/separation metrics exist | HIGH |
| **Scope duplication** | Namib beetle / fog-harvesting evidence already exists in `separation/cactus-spine.json` (mechanisms[9], mechanisms[10], narrative.entries[1-2]) | HIGH |
| **Scope duplication** | Same Janus mechanism cited in `lotus-leaf.json` (mechanisms[Namib beetle Janus…]), `fish-scale-hydroxyapatite.json`, `spider-silk.json`, `cellulose-nanocrystal.json` | MEDIUM |
| **Single-source mechanism dump** | All 16 mechanisms cite only 2 papers (DOI 10.1007/s11783-021-1515-2 and 10.1002/adfm.202200359), all `verification: unverified` | HIGH |
| **Mechanism content mismatch** | 13 of 16 mechanisms are generic membrane/fog-harvesting knowledge from the Halim2022 review (DOI 10.1007/s11783-021-1515-2), not Namib-beetle-specific experimental data | HIGH |
| **No PDF identified** | Neither `10.1007/s11783-021-1515-2` nor `10.1002/adfm.202200359` found as local PDF files; only extraction JSONs exist | MEDIUM |

**Conclusion:** `namib-beetle` was parked because (a) it has no unique performance evidence, (b) its mechanism content is a general membrane-review dump not specific to the organism, and (c) the same evidence is already better placed in `cactus-spine.json` and `separation/superhydrophobic-artificial.json`.

### 1.2 Parked Item Audit Table

| item | target_json | field_path | source_file / missing_pdf | locator | quote | evidence_label | recommended_action | notes |
|------|------------|------------|--------------------------|---------|-------|----------------|-------------------|-------|
| namib-beetle: no performance_data | `prototypes_db/parked/namib-beetle.json` | `performance_data` | missing_pdf — no dedicated Namib beetle experimental PDF found in 仿生文献库 | N/A | N/A | knowledge_gap | **keep_parked** — no action until dedicated fog-harvesting experimental paper is sourced | 唯一引用的综述 (Halim2022) 不提供甲虫专属实验数据 |
| namib-beetle: generic membrane mechanisms | `prototypes_db/parked/namib-beetle.json` | `mechanisms[0-14]` | `tools/litextract/outputs/extractions/论文/json/2018-Halim-cellulose-superhydrophobic-hydrophobic-oil-water-review.json` | review sections | "纤维素基表面相互作用分离膜分为三类" | inferred_only | **demote_to_review_material** — mechanisms 0-14 are review-table knowledge, not Namib-beetle-specific | 13/16 mechanisms are generic membrane science, not beetle data |
| namib-beetle: fog-harvesting mechanism | `prototypes_db/parked/namib-beetle.json` | `mechanisms[15]` | `tools/litextract/outputs/extractions/论文/json/2022-Progress-review 2.json` | narrative | "亲水凸起捕获雾滴，疏水凹槽定向运输" | partial | **merge_candidate** — same content exists in cactus-spine.json mechanisms[9] | 与 cactus-spine.json 重复，建议合并 |
| namib-beetle: narrative Halim2022 | `prototypes_db/parked/namib-beetle.json` | `narrative.entries[0]` | `tools/litextract/outputs/extractions/论文/json/2018-Halim-cellulose-superhydrophobic-hydrophobic-oil-water-review.json` | paper sections | "自然界中生物面临泥水污染附着…" | inferred_only | **keep_parked** — narrative is from a membrane review, not beetle-specific | 叙事来自综述，非甲虫实验文献 |
| namib-beetle: narrative yu2022 | `prototypes_db/parked/namib-beetle.json` | `narrative.entries[1]` | `tools/litextract/outputs/extractions/论文/json/2022-Progress-review 2.json` | paper sections | "进化策略：通过体表微纳形貌…" | partial | **merge_candidate** — same narrative in cactus-spine.json narrative.entries[2] | 与 cactus-spine 完全重复 |
| namib-beetle: engineering_constraints | `prototypes_db/parked/namib-beetle.json` | `engineering_constraints[0-3]` | `tools/litextract/outputs/extractions/论文/json/2018-Halim-cellulose-superhydrophobic-hydrophobic-oil-water-review.json` | review sections | "Kymene 557H…" / "SiO2/PDMS涂层…" | inferred_only | **demote_to_review_material** — all 4 constraints are generic membrane stability data | 通用膜稳定性数据，非甲虫特有 |

---

## 2. Cross-Prototype Namib Beetle / Fog-Harvesting / Cactus / Honeycomb / Pitcher Evidence Map

| prototype_id | DOI | field_path | evidence present | overlap with namib-beetle |
|---|---|---|---|---|
| `separation/cactus-spine` | 10.1002/adfm.202200359 | mechanisms[9] | 纳米布沙漠甲虫雾水收集机制 | **直接重复** — namib-beetle mechanisms[15] 引用相同 DOI 和内容 |
| `separation/cactus-spine` | 10.1007/s40242-021-0010-4 | mechanisms[4] | 仿生集水生物原型及机制（含甲虫/仙人掌/蜘蛛丝/猪笼草） | 内容重叠 — namib-beetle 无独立数据 |
| `separation/cactus-spine` | 10.1002/adfm.202200359 | narrative.entries[1-2] | 雾水收集综述叙事 | **直接重复** — namib-beetle narrative.entries[1] |
| `separation/lotus-leaf` | 10.1007/s11783-021-1515-2 | mechanisms[Namib beetle Janus…] | 沙漠甲虫Janus双面润湿仿生机制 | 相同 DOI 和机制描述 |
| `fish-scale-hydroxyapatite` | 10.1007/s11783-021-1515-2 | mechanisms[Namib beetle Janus…] | 沙漠甲虫Janus双面润湿仿生机制 | 相同 DOI 和机制描述 |
| `spider-silk` | 10.1002/adfm.202200359 | mechanisms[30] | 纳米布沙漠甲虫雾水收集机制 | 相同 DOI |
| `cellulose-nanocrystal` | 10.1007/s11783-021-1515-2 | mechanisms[Namib beetle Janus…] | 沙漠甲虫Janus双面润湿仿生机制 | 相同 DOI |
| `pitcher-plant-slippery-surface` | 10.1002/adfm.202200359 | mechanisms[19-20] | 雾水收集相关综述 | 相同 DOI，但焦点是猪笼草 |

**结论：** `namib-beetle` 的所有证据内容（2个DOI）已分散在至少5个现有prototype中，无需独立维护。

---

## 3. Duplicate / Cross-Directory Source Table

### 3.1 Extraction JSON Duplicates (Same Paper, Multiple Extraction Files)

| paper basename | extraction file A | extraction file B | difference |
|---|---|---|---|
| `2022-Progress-review` | `tools/litextract/outputs/extractions/论文/json/2022-Progress-review.json` | `tools/litextract/outputs/extractions/论文/json/2022-Progress-review 2.json` | 不同 extraction run（` 2.json` 为后续提取） |
| `2020-Almomani-adsorbent-biosorption-wastewater-removal` | `tools/litextract/outputs/extractions/论文/json/2020-Almomani-…json` | `仿生文献库/论文/第7组-系统仿生/2020-Almomani-…_visual_cache.json` | extraction JSON vs visual cache |
| `2020-Cui-heavy-metal-review` | `tools/litextract/outputs/extractions/论文/json/2020-Cui-heavy-metal-review.json` | `仿生文献库/论文/第7组-系统仿生/2020-Cui-heavy-metal-review_visual_cache.json` | extraction JSON vs visual cache |

### 3.2 PDF Variants (Base + " 2.pdf" + " 3.pdf" Without Original)

| PDF variant | directory | has original base? | count of variants |
|---|---|---|---|
| `2020-Almomani-adsorbent-biosorption-wastewater-removal 2.pdf` + ` 3.pdf` | 仿生文献库/论文/第7组-系统仿生/ | YES | 2 variants |
| `2020-Cui-heavy-metal-review 2.pdf` + ` 3.pdf` | 仿生文献库/论文/第7组-系统仿生/ | YES | 2 variants |
| `2022-Progress-review 2.pdf` + ` 3.pdf` | 仿生文献库/论文/第2组-超疏水/ | NO (base missing) | 2 orphan variants |
| `2020-杨-超疏水-油水分离 2.pdf` + ` 3.pdf` | 仿生文献库/论文/第2组-超疏水/ | NO | 2 orphan variants |
| `2020-李-超疏水-油水分离-综述-研究进展 2.pdf` | 仿生文献库/论文/第2组-超疏水/ | NO | 1 orphan variant |

**关键发现：** `仿生文献库/论文/第2组-超疏水/` 中的 " 2.pdf"/" 3.pdf" 是 orphan variants — 原始 `base.pdf` 不存在。这些可能是扫描件分页文件（Part 1, Part 2, Part 3）。

### 3.3 Missing-26-PDF-to-Library Variants

以下文件在 `tools/litextract/missing_26_pdf_dir/` 中有无后缀版本，同时在 `仿生文献库/论文/第8组-仿生材料/` 中有 ` 2.pdf` 变体：

| 文件名 | missing_26_pdf_dir | 仿生文献库 variant |
|---|---|---|
| 2022-Adil-separation-mof-adsorption-heavy-metal-review | ✅ | ` 2.pdf` |
| 2022-Akinterinwa-starch-adsorption-adsorbent-heavy-metal-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2023-Abu-separation-starch-adsorption-adsorbent-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2021-Sriram-mof-metal-organic-adsorption-adsorbent-review | ✅ | ` 2.pdf` |
| 2021-Tchinsa-hierarchical-magnetic-mof-metal-organic-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2021-Khan-bone-starch-adsorption-adsorbent-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2021-Gupta-starch-adsorption-adsorbent-heavy-metal-review | ✅ | ` 2.pdf` |
| 2021-Khan-diatom-wastewater-review | ✅ | ` 2.pdf` (第3组) |
| 2022-Mo-mof-adsorption-heavy-metal-wastewater-review | ✅ | ` 2.pdf` |
| 2023-鲁-金属有机框架-MOF-吸附-去除-综述 | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2023-Liu-porous-adsorbent-removal-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2023-Wang-separation-magnetic-mof-metal-organic-review | ✅ | ` 2.pdf` |
| 2023-Zadehahmadi-separation-magnetic-mof-adsorption-review | ✅ | ` 2.pdf` |
| 2022-Liu-separation-membrane-mof-metal-organic-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2024-Costa-hydrophobic-starch-adsorption-adsorbent-review | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2023-Khoo-cellulose-nanocellulose-starch-adsorbent-review | ✅ | ` 2.pdf` |
| 2023-Lin-mof-metal-organic-adsorption-adsorbent-review | ✅ | ` 2.pdf` |
| 2021-娄-MOF-吸附-染料-废水 | ✅ | ` 2.pdf` |
| 2020-范-金属有机框架-MOF-吸附-染料-综述 | ✅ | ` 2.pdf` |
| 2022-李-MOF-吸附-水处理-去除-综述 | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2021-陈-多孔-MOF-重金属-铬-综述 | ✅ | ` 2.pdf` + ` 3.pdf` |
| 2022-Ahmadijokani-separation-membrane-porous-nanofiber-review | ✅ | ` 2.pdf` |
| 2022-Jeong-separation-porous-mof-metal-organic-review | ✅ | ` 2.pdf` + ` 3.pdf` |

**含义：** `missing_26_pdf_dir/` 中的无后缀文件可能是单页扫描件或 OCR 中间产物，而 `仿生文献库/` 中的 ` 2.pdf` / ` 3.pdf` 才是完整论文。数据库中引用的 bare filename 指向的是 `missing_26_pdf_dir/` 中的文件。

---

## 4. Original PDF Path → Extraction JSON Mapping Table

| extraction JSON | local PDF (if found) | PDF variant(s) | status |
|---|---|---|---|
| `tools/litextract/outputs/extractions/论文/json/2018-Halim-…review.json` | ❌ 无本地 PDF | N/A | **missing_pdf** — 引用在 namib-beetle, fish-scale, lotus-leaf, CNC |
| `tools/litextract/outputs/extractions/论文/json/2022-Progress-review.json` | `仿生文献库/论文/第2组-超疏水/2022-Progress-review 2.pdf` (?) | ` 2.pdf`, ` 3.pdf` | **ambiguous** — 需确认哪个 PDF 对应哪个 extraction |
| `tools/litextract/outputs/extractions/论文/json/2022-Progress-review 2.json` | `仿生文献库/论文/第2组-超疏水/2022-Progress-review 2.pdf` | ` 2.pdf`, ` 3.pdf` | **ambiguous** — 同上 |
| `tools/litextract/outputs/extractions/论文/json/2021-Penetration-…review.json` | ❌ 无本地 PDF | N/A | **missing_pdf** — 引用在 cactus-spine |

---

## 5. Candidate Queue Items Table

| priority | candidate_action | target_json | field_path | reason | evidence_label |
|---|---|---|---|---|---|
| P1 | **retire_parked** | `prototypes_db/parked/namib-beetle.json` | entire file | 所有证据已分散在 cactus-spine / lotus-leaf / fish-scale / spider-silk / CNC 中；零 performance_data；机制内容为综述通用知识 | knowledge_gap + scope_overlap |
| P2 | **deduplicate_extraction** | `tools/litextract/outputs/extractions/论文/json/2022-Progress-review.json` & `…Progress-review 2.json` | narrative | 同一论文两个 extraction 文件，需确认是否合并 | needs_human_decision |
| P3 | **resolve_bare_filenames** | `prototypes_db/separation/lotus-leaf.json` | `performance_data[2]` | `source_file: "2021-Usman-…review.pdf"` 是 bare filename，本地有对应 PDF 但无路径 | needs_path_resolution |
| P4 | **resolve_orphan_variants** | `仿生文献库/论文/第2组-超疏水/` | N/A | `2022-Progress-review 2.pdf` + ` 3.pdf` 是 orphan variants（无 base），需确认是扫描分页还是独立文件 | needs_human_decision |
| P5 | **resolve_missing_26_mapping** | `tools/litextract/missing_26_pdf_dir/` | N/A | 24 个文件同时存在于 missing_26 和仿生文献库（` 2.pdf` 变体），需确认哪个是完整版本 | needs_human_decision |

---

## 6. Boundary / DO-NOT Candidate Table

| item | target_json | field_path | boundary_type | reason | evidence_label | recommended_action |
|---|---|---|---|---|---|---|
| namib-beetle → cactus-spine merge | `prototypes_db/parked/namib-beetle.json` → `prototypes_db/separation/cactus-spine.json` | mechanisms[15] → mechanisms[9] | scope_overlap | 相同 DOI (10.1002/adfm.202200359)，相同内容（纳米布沙漠甲虫雾水收集机制） | partial | **merge** — namib-beetle mechanism 应合并到 cactus-spine，然后删除 parked |
| namib-beetle → lotus-leaf overlap | `prototypes_db/parked/namib-beetle.json` → `prototypes_db/separation/lotus-leaf.json` | mechanisms[3] → mechanisms[Namib beetle Janus…] | scope_overlap | 相同 DOI (10.1007/s11783-021-1515-2)，Janus 机制 | inferred_only | **keep_lotus_leaf_as_primary** — lotus-leaf 已有完整 Janus 机制 |
| generic membrane mechanisms in namib-beetle | `prototypes_db/parked/namib-beetle.json` | mechanisms[0-14] | wrong_domain | 13/16 mechanisms 是纤维素膜综述知识，与 Namib beetle 无关 | inferred_only | **DO_NOT_PROMOTE** — 不应升级为 verified 或 hard_do_not |
| 2022-Progress-review dual extraction | `tools/litextract/outputs/extractions/论文/json/2022-Progress-review.json` & `…2.json` | entire files | duplicate_source | 同一论文的两次提取，可能覆盖不同页面或使用不同方法 | needs_human_decision | **DO_NOT_MODIFY_DB** — 先确认哪个 extraction 覆盖哪些页面 |
| Halim2022 review scope creep | `prototypes_db/parked/namib-beetle.json` | mechanisms + engineering_constraints + narrative | scope_mismatch | Halim2022 (10.1007/s11783-021-1515-2) 是纤维素膜综述，不是 Namib beetle 研究 | inferred_only | **DO_NOT_PROMOTE** — 综述来源不应升级为实验验证 |

---

## 7. Summary Of Findings

### 7.1 namib-beetle Parked Reason

**Primary:** Scope duplication — all evidence content already exists in `cactus-spine.json`, `lotus-leaf.json`, `fish-scale-hydroxyapatite.json`, `spider-silk.json`, and `cellulose-nanocrystal.json`.

**Secondary:** Zero performance_data — no quantified adsorption/separation metrics for Namib beetle.

**Tertiary:** Mechanism content mismatch — 13/16 mechanisms are generic membrane review knowledge (from Halim2022, DOI 10.1007/s11783-021-1515-2), not Namib-beetle-specific experimental data.

### 7.2 Recommendation

**Retire `namib-beetle` from parked.** The single unique mechanism (fog-harvesting, mechanisms[15]) is already present in `cactus-spine.json`. The rest is review material that does not belong in a prototype database entry. No Codex action needed — this is a keep_parked / retire decision for Yao.

### 7.3 High-Impact Bare Filename Issues

- `lotus-leaf.json` performance_data[2]: `source_file: "2021-Usman-…review.pdf"` — bare filename, no directory
- Multiple `performance_data` entries across prototypes reference bare filenames (see section 3.3 full list)
- 24 papers exist in both `missing_26_pdf_dir/` (no suffix) and `仿生文献库/` (with ` 2.pdf` suffix) — path ambiguity needs resolution

### 7.4 Extraction File Duplication

- `2022-Progress-review.json` and `2022-Progress-review 2.json` are dual extractions of the same paper
- Both are referenced by `cactus-spine.json` and `pitcher-plant-slippery-surface.json`
- `namib-beetle.json` references only `…Progress-review 2.json`
- Codex should determine if these should be merged or if they cover different page ranges
