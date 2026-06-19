# 证据增强 Review · 文献索引与原型证据对照表

> 分支：`adsorption/dev` | HEAD：`bf592e4` | 日期：2026-06-15
> 约束：不修改任何 JSON/项目文件；recommended_action 仅建议，由 Yao/Codex 决策。

---

## 数据总览

| 类别 | 数量 |
|------|------|
| extraction JSON（litextract/outputs） | 558 |
| PDF 文件（仿生文献库/） | 578 |
| PDF 文件（tools/litextract/workspace） | 6 |
| **PDF 总计** | **584** |
| active 原型 | 24 |
| 优先 review 原型 | 5 |

---

## 表 A：全量文献索引表（extraction JSON ↔ PDF 对照）

### A.1 总体匹配统计

| extraction 目录 | JSON 数 | 有 PDF_REF 字段 | 匹配到本地 PDF | missing_pdf |
|---|---|---|---|---|
| 论文/json/ | 308 | 308 | ~290 | ~18 |
| 第二波/json/ | 110 | 110 | ~105 | ~5 |
| 第三波/json/ | 63 | 63 | ~58 | ~5 |
| 专利/json/ | 40 | 40 | 40 | 0 |
| 标准/json/ | 3 | 3 | 3 | 0 |
| 中文文献/ | 2 | 2 | 2 | 0 |
| 英文文献/ | 1 | 1 | 1 | 0 |
| outputs/extractions/ | 2 | 2 | 2 | 0 |
| **合计** | **~558** | **~558** | **~530** | **~28** |

> 匹配规则：extraction JSON 的 `bibliographic_metadata.file_name` 或 `routing.pdf_ref` 字段 → 与 `仿生文献库/` 下 PDF 文件名 stem 匹配。大部分 PDF_REF 直接对应文件名（可能带 ` 2.pdf` / ` 3.pdf` 后缀）。

### A.2 PDF 目录结构

```
仿生文献库/
├── 论文/          358 PDFs（第1-8组）
│   ├── 第1组-配位螯合/
│   ├── 第2组-超疏水/         46
│   ├── 第3组-多孔结构/       37
│   ├── 第4组-生物矿化/       59
│   ├── 第5组-纤维结构/       56
│   ├── 第6组-功能仿生/       44
│   ├── 第7组-系统仿生/       55
│   └── 第8组-仿生材料/       61
├── 2nd/           119 PDFs（第9-12组 + 全局综述）
│   ├── 全局综述（补充）/     20
│   ├── 第9组-仿生方法论/     30
│   ├── 第10组-设计原则/      27
│   ├── 第11组-跨原型比较/    15
│   └── 第12组-仿生案例/      27
├── 3rd/           81 PDFs
│   ├── 第A组-贻贝仿生/       12
│   ├── 第B组-新方向/         25（B1-DNA适配体10, B2-生物矿化9, B3-蚕丝6）
│   ├── 第C组-零数据原型/     26（C1-仿硅藻6, C2-铁氧化菌9, C3-植物单宁5, C4-扇贝壳6）
│   ├── 第D组-再生循环/       8
│   └── 第三波-仿生吸附专利/  10
├── 专利/          17 PDFs
├── 标准/          3 PDFs
└── 2nd/ 第12组-仿生案例/ 含 _visual_cache.json（非 PDF）
```

### A.3 与 5 个优先原型相关的 extraction JSON 完整列表

以下列出与 coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk 直接相关的全部 extraction JSON 及其 PDF 匹配情况：

#### coral-skeleton 相关

| extraction_json_path | paper_id | title | doi | matched_pdf_path | pdf_confidence |
|---|---|---|---|---|---|
| `tools/litextract/outputs/extractions/论文/json/2020-Han-antifouling-review.json` | 2020-Han-antifouling-review | （防污综述，非珊瑚骨骼对口文献） | — | 有 PDF（综述类） | **low**（非对口） |

> ⚠️ coral-skeleton 的 narrative 来源是防污综述，不是珊瑚骨骼吸附文献。Phase 6 已标记：**本地无珊瑚骨骼文献**。

#### magnetic-bacteria 相关

| extraction_json_path | paper_id | title | doi | matched_pdf_path | pdf_confidence |
|---|---|---|---|---|---|
| `tools/litextract/outputs/extractions/论文/json/2022-Mtb-biomineralization-magnetic-heavy-metal-review.json` | 2022-Goswami-magnetotactic-bacteria-review | （磁细菌综述） | — | 有 PDF | **medium**（综述，非原始实验数据） |

> ⚠️ Phase 6 已标记：**本地无磁细菌对口文献**。此综述可提供背景但不能提供 verified 实验数据。

#### pitcher-plant-slippery-surface 相关

| extraction_json_path | paper_id | title | doi | matched_pdf_path | pdf_confidence |
|---|---|---|---|---|---|
| `论文/json/2021-Zeng-antifouling-porous-review.json` | Zeng2021_SLIPS_Review | SLIPS 防污多孔膜综述 | 10.1007/s42242-021-00133-8 | `仿生文献库/论文/` 有匹配 | **high** |
| `论文/json/2021-Penetration-separation-membrane-hierarchical-review.json` | 2021-Penetration-separation-membrane-hierarchical-review | 层级分离膜综述 | — | 有 PDF | **medium** |
| `论文/json/2022-Progress-review.json` | Yu2022_Fog_Harvesting_Devices_Multiple_Creatures_Review | 集水仿生器件综述 | — | 有 PDF | **low**（集水非吸附） |
| `论文/json/2022-Progress-review 2.json` | yu2022_fog_harvesting_biomimetic_review | 集水仿生综述 | — | 有 PDF | **low**（集水非吸附） |
| 机制 DOI: 10.1007/s42242-021-00133-8 | — | Zeng SLIPS 综述 | 同上 | 同上 | **high** |
| 机制 DOI: 10.1007/s40242-021-0010-4 | — | （超疏水膜综述） | — | 需查 | **medium** |
| 机制 DOI: 10.1002/adfm.202200359 | — | HHNCM 仿生铜网 | — | 需查 | **medium** |
| 性能数据 PDF: `2021-Zeng-antifouling-porous-review.pdf` | — | 同 Zeng2021 | 10.1007/s42242-021-00133-8 | 有 | **high** |

> ⚠️ Phase 6 已标记：**本地无猪笼草 SLIPS 对口文献**。现有来源是综述类，可提供背景但不能 verified SLIPS 失效边界。

#### lobster-exoskeleton 相关

| extraction_json_path | paper_id | title | doi | matched_pdf_path | pdf_confidence |
|---|---|---|---|---|---|
| `论文/json/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.json` | 2023-Vo-chitosan-beads-wastewater-review | 壳聚糖/羟基磷灰石废水综述 | 10.1007/s10311-023-01563-9 | `仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf` | **high** |

> ✅ 有对口 PDF。但注意：此文献是壳聚糖 beads 综述，龙虾外骨骼本身无独立实验文献。

#### spider-silk 相关

| extraction_json_path | paper_id | title | doi | matched_pdf_path | pdf_confidence |
|---|---|---|---|---|---|
| `论文/json/2021-Li-silk-hierarchical-shell-review.json` | 2022-Li-spider-silk-hierarchical-review | 蜘蛛丝层级结构综述 | — | 有 PDF | **medium** |
| `论文/json/2021-Zhang-silk-separation-membrane-porous.json` | 2021-Zhang-spider-silk-nanoemulsion-separation | 蜘蛛丝仿生纳米乳液分离 | 10.1016/j.seppur.2021.119824 | `仿生文献库/论文/第5组-纤维结构/2021-Zhang-silk-separation-membrane-porous.pdf` | **high** |
| `论文/json/2021-Zhou-cellulose-silk-nanofiber-adsorption.json` | 2021-Zhou-spider-silk-amphoteric-bionic-fibers | 蜘蛛丝仿生两性纤维除重金属 | 10.1016/j.cej.2021.128670 | `仿生文献库/论文/第5组-纤维结构/2021-Zhou-cellulose-silk-nanofiber-adsorption.pdf` | **high** |
| `论文/json/2023-Li-antifouling-separation-porous-adsorption-review.json` | 2023-Li-antifouling-separation-porous-adsorption-review | 抗污分离多孔膜综述 | — | 有 PDF | **medium** |
| 机制 DOI: 10.1002/advs.202103965 | — | 蜘蛛丝增强策略 | — | 需查 | **unknown** |
| 机制 DOI: 10.34133/2022/9895418 | — | 飞秒激光超润湿表面 | — | 需查 | **low**（非蜘蛛丝对口） |
| 机制 DOI: 10.1016/j.ccr.2023.215234 | — | 铀酰配位化学 | — | 需查 | **low**（铀提取非吸附） |

> ✅ spider-silk 有 3 篇对口 PDF（Zhou2021 重金属、Zhang2021 分离、Li2021 综述），可尝试从 PDF 中核验性能数据和部分机制。

---

## 表 B：5 个优先原型 claim/provenance/evidence 对照表

### B.1 coral-skeleton（珊瑚骨骼）

| 字段 | 值 |
|---|---|
| **prototype_id** | coral-skeleton |
| **mechanisms 总数** | 1 |
| **有 causal_chain 的机制** | 1 |
| **performance_data** | 0 条 |
| **narrative entries** | 1 |

| claim_id | claim_text | current_verif | current_basis | boundary_text | source_hint | extraction_json | paper_id | doi | matched_pdf | pdf_conf | page/section | candidate_quote | quote_supports | source_on_topic | needs_multimodal | rec_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mech-1 | 珊瑚骨骼 CaCO₃ 可通过离子交换/沉淀去除重金属和磷酸盐 | needs_review | llm_inferred | "待文献确定具体失效边界" ×2 | source_file: null, ref_doi: null | — | — | — | — | — | — | — | — | — | — | **missing_pdf** | 无任何对口 PDF，需 C 档下载 |
| narr-1 | （防污综述，非吸附机制） | needs_review | — | — | 2020-Han-antifouling-review | `论文/json/2020-Han-antifouling-review.json` | 2020-Han | — | 有 PDF | low | — | — | — | **No**（防污非吸附） | No | **wrong_source** | narrative 来源与原型身份不对口 |

**coral-skeleton 总结**：0 条 verified / 0 条可核验 / 1 条 wrong_source / 1 条 missing_pdf。**完全依赖 C 档文献下载**。

---

### B.2 magnetic-bacteria（趋磁细菌）

| 字段 | 值 |
|---|---|
| **prototype_id** | magnetic-bacteria |
| **mechanisms 总数** | 1 |
| **有 causal_chain 的机制** | 1 |
| **performance_data** | 0 条 |
| **narrative entries** | 1 |

| claim_id | claim_text | current_verif | current_basis | boundary_text | source_hint | extraction_json | paper_id | doi | matched_pdf | pdf_conf | page/section | candidate_quote | quote_supports | source_on_topic | needs_multimodal | rec_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mech-1 | 趋磁细菌磁小体可作为磁性吸附剂实现磁分离回收 | needs_review | llm_inferred | "待文献确定具体失效边界" ×2 | source_file: null, ref_doi: null | — | — | — | — | — | — | — | — | — | — | **missing_pdf** | 无对口实验 PDF |
| narr-1 | MTB 生物矿化合成磁铁矿纳米晶体 → 仿生磁性纳米链吸附材料 | needs_review | — | — | 2022-Mtb-biomineralization | `论文/json/2022-Mtb-biomineralization-magnetic-heavy-metal-review.json` | 2022-Goswami | — | 有 PDF | medium | — | — | — | **Yes**（综述覆盖磁细菌） | No | **keep_soft** | 综述可提供背景支撑，但不能 verified 实验数据 |

**magnetic-bacteria 总结**：0 条 verified / 1 条 keep_soft（综述背景） / 1 条 missing_pdf。**核心机制需 C 档下载**。

---

### B.3 pitcher-plant-slippery-surface（猪笼草滑面）

| 字段 | 值 |
|---|---|
| **prototype_id** | pitcher-plant-slippery-surface |
| **mechanisms 总数** | 22 |
| **有 causal_chain 的机制** | 1（仅 mech-22: Nepenthes SLIPS） |
| **performance_data** | 1 条 |
| **narrative entries** | 4 |

| claim_id | claim_text | current_verif | current_basis | boundary_text | source_hint | extraction_json | paper_id | doi | matched_pdf | pdf_conf | page/section | candidate_quote | quote_supports | source_on_topic | needs_multimodal | rec_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mech-22 | Nepenthes SLIPS 抗污机制：微结构锁液 + 低表面能 | needs_review | llm_inferred | "润滑液高流速下可能被冲刷流失" / "润滑液与被分离介质不互溶是前提" | source_file: null | — | — | — | — | — | — | — | — | — | — | **missing_pdf** | 核心 SLIPS 机制无对口 PDF |
| mech-1 | Hydrophobic threshold contact angle (Young's model) | needs_review | — | — | ref_doi: 10.1007/s42242-021-00133-8 | `论文/json/2021-Zeng-antifouling-porous-review.json` | Zeng2021 | 10.1007/s42242-021-00133-8 | 有 PDF | high | 需定位 | 需从 PDF 提取 | 待查 | **Yes**（SLIPS 综述） | No | **upgrade_candidate** | 有对口综述 PDF，可尝试定位 Young 模型段落 |
| mech-4 | Nepenthes pitcher plant trapping mechanism | needs_review | — | — | ref_doi: 10.1007/s42242-021-00133-8 | 同上 | 同上 | 同上 | 同上 | high | 需定位 | 需从 PDF 提取 | 待查 | **Yes** | No | **upgrade_candidate** | 同一来源，可定位 Nepenthes 段落 |
| mech-10 | Lubricant loss mechanisms | needs_review | — | — | ref_doi: 10.1007/s42242-021-00133-8 | 同上 | 同上 | 同上 | 同上 | high | 需定位 | 需从 PDF 提取 | 待查 | **Yes** | No | **upgrade_candidate** | 润滑液流失正是边界条件核心 |
| mech-11 | 仿荷叶 PS 纳米纤维超疏水表面接触角 | needs_review | — | — | ref_doi: 10.1007/s40242-021-0010-4 | 需查 | — | 10.1007/s40242-021-0010-4 | 需查 | unknown | — | — | — | 待查 | No | **needs_human_decision** | DOI 需确认是否有本地 PDF |
| mech-20 | HHNCM 亲水-疏水纳米纤维铜网 | needs_review | — | — | ref_doi: 10.1002/adfm.202200359 | 需查 | — | 10.1002/adfm.202200359 | 需查 | unknown | — | — | — | 待查 | No | **needs_human_decision** | 仿生铜网，非核心 SLIPS 机制 |
| perf-1 | Mg alloy SLIPS ice removal force reduction 6× | needs_review | — | — | source_file: Zeng2021 | `论文/json/2021-Zeng-antifouling-porous-review.json` | Zeng2021 | 10.1007/s42242-021-00133-8 | 有 PDF | high | 需定位 | 需从 PDF 提取 | 待查 | **Yes** | No | **upgrade_candidate** | 冰去除力数据可在 PDF 中定位 |
| narr-1 | Zeng2021 SLIPS 防污多孔膜综述 | needs_review | — | — | — | 同上 | 同上 | 同上 | 有 PDF | high | — | — | — | **Yes** | No | **keep_soft** | 综述类，提供背景 |
| narr-2 | 2021-Penetration 分离膜综述 | needs_review | — | — | — | `论文/json/2021-Penetration-separation-membrane-hierarchical-review.json` | — | — | 有 PDF | medium | — | — | — | **Yes** | No | **keep_soft** | 层级膜综述 |
| narr-3 | Yu2022 集水仿生器件综述 | needs_review | — | — | — | `论文/json/2022-Progress-review.json` | Yu2022 | — | 有 PDF | low | — | — | — | **No**（集水非吸附） | No | **wrong_source** | 集水文献不对口 |

**pitcher-plant 总结**：0 条 verified / 4 条 upgrade_candidate（Zeng2021 PDF 可定位） / 1 条 missing_pdf（核心 SLIPS） / 2 条 needs_human_decision / 1 条 wrong_source。**Zeng2021 综述是最有价值的已有 PDF**。

---

### B.4 lobster-exoskeleton（龙虾外骨骼）

| 字段 | 值 |
|---|---|
| **prototype_id** | lobster-exoskeleton |
| **mechanisms 总数** | 1 |
| **有 causal_chain 的机制** | 1 |
| **performance_data** | 1 条 |
| **narrative entries** | 1 |

| claim_id | claim_text | current_verif | current_basis | boundary_text | source_hint | extraction_json | paper_id | doi | matched_pdf | pdf_conf | page/section | candidate_quote | quote_supports | source_on_topic | needs_multimodal | rec_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mech-1 | Chitosan beads 六种吸附机制：-NH₂/-OH 配位螯合 | needs_review | llm_inferred | "与壳聚糖相同的 pH 限制" / "酸性下溶解" | ref_doi: 10.1016/j.polymer.2020.123316 | — | — | 10.1016/j.polymer.2020.123316 | 需查（此 DOI 不在 litextract 中） | unknown | — | — | — | 待查 | No | **needs_human_decision** | 此 DOI 是壳聚糖聚合物综述，需确认是否有本地 PDF |
| narr-1 | Vo2023 壳聚糖/羟基磷灰石废水综述：CS/Fe-HAp beads 对 Pb(II) 1385 mg/g | needs_review | — | — | `论文/json/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.json` | `论文/json/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.json` | 2023-Vo | 10.1007/s10311-023-01563-9 | `仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf` | **high** | 需定位 | 需从 PDF 提取 Pb(II) 1385 mg/g 数据 | 待查 | **Yes** | No | **upgrade_candidate** | 有对口 PDF，可核验性能数据 |
| perf-1 | CS/Fe-HAp beads 对 Pb(II) 最大吸附容量 1385 mg/g | unverified | — | — | source_file: `仿生文献库/论文/第1组-配位螯合/2023-Vo-...pdf` | 同上 | 同上 | 10.1007/s10311-023-01563-9 | 同上 PDF | **high** | 需定位表格/数据 | 1385 mg/g 数值 | 待查 | **Yes** | No | **upgrade_candidate** | 性能数据可在 PDF 中定位 |

**lobster-exoskeleton 总结**：0 条 verified / 2 条 upgrade_candidate（Vo2023 PDF 可核验） / 1 条 needs_human_decision。**Vo2023 是最有价值的已有 PDF**。

---

### B.5 spider-silk（蜘蛛丝）

| 字段 | 值 |
|---|---|
| **prototype_id** | spider-silk |
| **mechanisms 总数** | 31 |
| **有 causal_chain 的机制** | 1（仅 mech-2: 抗污染机制） |
| **performance_data** | 4 条（Cd/Cr/Cu/Pb，均 unverified） |
| **narrative entries** | 4 |

| claim_id | claim_text | current_verif | current_basis | boundary_text | source_hint | extraction_json | paper_id | doi | matched_pdf | pdf_conf | page/section | candidate_quote | quote_supports | source_on_topic | needs_multimodal | rec_action | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mech-2 | 蜘蛛丝抗污染机制：亲水+弹性组合 | needs_review | llm_inferred | "干燥环境下蜘蛛丝失去亲水性" ×2 | ref_doi: 10.1016/j.seppur.2021.119824 | `论文/json/2021-Zhang-silk-separation-membrane-porous.json` | 2021-Zhang | 10.1016/j.seppur.2021.119824 | `仿生文献库/论文/第5组-纤维结构/2021-Zhang-silk-separation-membrane-porous.pdf` | **high** | 需定位 | 需从 PDF 提取抗污机制段落 | 待查 | **Yes** | No | **upgrade_candidate** | 有对口 PDF，可核验抗污机制 |
| mech-12 | Cr(VI) XPS 吸附机制 | needs_review | — | — | ref_doi: 10.1016/j.cej.2021.128670 | `论文/json/2021-Zhou-cellulose-silk-nanofiber-adsorption.json` | 2021-Zhou | 10.1016/j.cej.2021.128670 | `仿生文献库/论文/第5组-纤维结构/2021-Zhou-cellulose-silk-nanofiber-adsorption.pdf` | **high** | 需定位 XPS 数据 | 需从 PDF 提取 Cr(VI) 机理 | 待查 | **Yes** | No | **upgrade_candidate** | 有对口 PDF |
| mech-13 | Cd(II) XPS 吸附机制 | needs_review | — | — | 同上 | 同上 | 同上 | 同上 | 同上 | **high** | 需定位 | 需从 PDF 提取 | 待查 | **Yes** | No | **upgrade_candidate** | 同一 PDF |
| mech-15 | 专化-协同机制 Specialization and cooperation | needs_review | — | — | 同上 | 同上 | 同上 | 同上 | 同上 | **high** | 需定位 | 需从 PDF 提取 | 待查 | **Yes** | No | **upgrade_candidate** | 同一 PDF |
| mech-17 | 铀酰离子配位化学 | needs_review | — | — | ref_doi: 10.1016/j.ccr.2023.215234 | 需查 | — | 10.1016/j.ccr.2023.215234 | 需查 | unknown | — | — | — | 待查 | No | **needs_human_decision** | 铀提取文献，非核心吸附 |
| perf-1 | Cd(II) 100% 去除，20min 达 EPA 标准 | unverified | — | — | source_file: Zhou2021 PDF | 同上 | 2021-Zhou | 10.1016/j.cej.2021.128670 | 同上 PDF | **high** | 需定位数据表 | "100% removal" 数值 | 待查 | **Yes** | No | **upgrade_candidate** | 性能数据可在 PDF 定位 |
| perf-2 | Cr(VI) 100% 去除，20min 达 EPA 标准 | unverified | — | — | 同上 | 同上 | 同上 | 同上 | 同上 | **high** | 需定位 | 同上 | 待查 | **Yes** | No | **upgrade_candidate** | 同一 PDF |
| perf-3 | Cu(II) 100% 去除，30min 达安全标准 | unverified | — | — | 同上 | 同上 | 同上 | 同上 | 同上 | **high** | 需定位 | 同上 | 待查 | **Yes** | No | **upgrade_candidate** | 同一 PDF |
| perf-4 | Pb(II) 100% 去除，40min 达 EPA 标准 | unverified | — | — | 同上 | 同上 | 同上 | 同上 | 同上 | **high** | 需定位 | 同上 | 待查 | **Yes** | No | **upgrade_candidate** | 同一 PDF |
| narr-1 | Li2021 蜘蛛丝层级结构综述 | needs_review | — | — | `论文/json/2021-Li-silk-hierarchical-shell-review.json` | `论文/json/2021-Li-silk-hierarchical-shell-review.json` | 2022-Li | — | 有 PDF | medium | — | — | — | **Yes** | No | **keep_soft** | 综述类 |
| narr-3 | Zhou2021 两性纤维仿蜘蛛丝除重金属 | needs_review | — | — | 同 Zhou2021 | 同上 | 2021-Zhou | 10.1016/j.cej.2021.128670 | 同上 PDF | **high** | — | — | — | **Yes** | No | **keep_soft** | 核心实验文献 |
| narr-4 | Li2023 抗污分离多孔膜综述 | needs_review | — | — | `论文/json/2023-Li-antifouling-separation-porous-adsorption-review.json` | 同上 | 2023-Li | — | 有 PDF | medium | — | — | — | **Yes** | No | **keep_soft** | 综述类 |

**spider-silk 总结**：0 条 verified / **10 条 upgrade_candidate**（Zhou2021 + Zhang2021 两篇 PDF 可核验） / 1 条 needs_human_decision / 2 条 keep_soft。**spider-silk 是 5 个原型中证据最丰富的**。

---

## 综合决策汇总

### 按 recommended_action 统计

| action | 数量 | 说明 |
|---|---|---|
| **missing_pdf** | 4 | coral-skeleton 全部 + magnetic-bacteria 核心 + pitcher-plant SLIPS 核心 |
| **upgrade_candidate** | 16 | 有对口 PDF，可尝试定位 quote/locator |
| **keep_soft** | 6 | 综述类背景，可保持 soft caution |
| **wrong_source** | 2 | narrative 来源与原型不对口 |
| **needs_human_decision** | 4 | DOI 需确认是否有本地 PDF |

### 优先处理建议（按 ROI 排序）

| 优先级 | 原型 | 动作 | 原因 |
|---|---|---|---|
| **1** | **spider-silk** | 核验 Zhou2021 PDF（4 条 perf + 3 条 mechanism） | 有 2 篇对口 PDF，一次核验可覆盖最多 claim |
| **2** | **lobster-exoskeleton** | 核验 Vo2023 PDF（1 条 perf + 1 条 mechanism） | 有 1 篇对口 PDF，Pb(II) 1385 mg/g 可定位 |
| **3** | **pitcher-plant** | 核验 Zeng2021 PDF（3 条 mechanism + 1 条 perf） | 有 SLIPS 综述 PDF，可定位 Young 模型/Nepenthes/润滑液流失 |
| **4** | **magnetic-bacteria** | 保持 soft（综述背景），等待 C 档下载 | 无对口实验 PDF |
| **5** | **coral-skeleton** | 完全依赖 C 档下载 | 无任何对口来源 |

### 需要 Yao 决策的事项

1. **coral-skeleton narrative wrong_source**：当前 narrative 来源是防污综述（2020-Han），与珊瑚骨骼吸附完全不对口。是否删除此 narrative entry？
2. **pitcher-plant mech-11/20 的 DOI**（10.1007/s40242-021-0010-4 / 10.1002/adfm.202200359）：这两个 DOI 在 litextract 中未找到 extraction JSON，需确认是否有本地 PDF。
3. **spider-silk mech-17 铀酰配位**（DOI: 10.1016/j.ccr.2023.215234）：铀提取文献是否属于蜘蛛丝原型的对口来源？
4. **lobster-exoskeleton mech-1 的 DOI**（10.1016/j.polymer.2020.123316）：壳聚糖聚合物综述，需确认是否有本地 PDF。

---

## 附录：Phase 6 已确认的 23 张 verified 卡（对照参考）

| 原型 | 机制 | 来源 PDF | 核验要点 |
|------|------|---------|---------|
| mussel-foot-adhesion | PDA涂层粘附 | Lee2007 Science | DOPA+lysine in byssal plaque |
| mussel-foot-adhesion | PDA自聚合 | Lee2007 Science | dopamine self-polymerization |
| mussel-foot-adhesion | 铀酰配位 | Liu2024 设计原则 | uranium adsorbent design |
| chitosan | pH效应 | Lei2021 Polymer | -NH2/-OH groups on chitosan |
| chitosan | 金属络合 | Lei2021 Polymer | chelation, H-bonds, van der Waals |
| chlorella-cell-wall | 藻类吸附 | 程2021 环境科技 | Chlorella pyrenoidosa Pb²⁺ adsorption |
| diatom-frustule | Pb²⁺ XPS | Guo2022 环境工程 | diatomite electrostatic adsorption |
| polydopamine-coating | PDA补充 | Lei2021 Polymer | catechol/amino/imine groups |
| sulfate-reducing-bacteria | SRB机理 | Kumar2021 J Environ Man | SO4²⁻→S²⁻→metal sulfide precipitation |
| iron-oxidizing-bacteria | 施氏矿物 | Luo2021 环境化学 | schwertmannite arsenic removal |
| bone-structure | HAp重金属 | Bambaeero2021 CJChE | HAP removes Sr, Zn, Co, Cd |
| oyster-shell | 牡蛎壳 | 李2017 牡蛎壳生物炭 | oyster shell biochar |
| scallop-shell | 吸附三步骤 | Wang2024 海洋科学 | scallop shell CaCO₃ + Congo Red |
| fish-scale-hydroxyapatite | 八重协同 | Balasooriya2022 HA review | hydroxyapatite heavy metal review |
| mangrove-root | 人工湿地 | 刘2022 红树林 | mangrove constructed wetland |
| mycelium | 菌丝体 | 刘2021 现代盐化工 | 真菌菌丝体细胞壁多糖吸附重金属 |
| wood-xylem | 酚+静电 | Mo2021 木纳米纤维 | wood nanocellulose aerogel |
| silk-fibroin | 吸附×2 | Prasad2022 ETI | SF/PUF biocomposite Cu²⁺/Cr⁶⁺ |
| dna-aptamer | 适配体 | Li2021 分析测试学报 | aptamer SELEX for metals |
| biomineralization | 矿化模板 | Wang2025 CEJ | LanM@ZIF-8 REE adsorption |
| plant-tannin | 单宁配位 | Zhu2022 Ind Crops | ortho-phenolic hydroxyl chelation |
| cell-membrane | 仿生膜 | BerattoRamos2022 | aquaporin biomimetic membrane |
| plant-tannin | 单宁配位 | Zhu2022 Ind Crops | catechol/pyrogallol chelation |

## 附录：Phase 8 C 档文献检索请求清单（8 条）

| prototype_id | 待支撑的断言 | 为何高风险 | 检索词（English 布尔式） | 期望证据 |
|---|---|---|---|---|
| coral-skeleton | 珊瑚骨骼 CaCO₃ 可通过离子交换/沉淀去除重金属和磷酸盐 | 若机制不成立，ADRMATS 可能选出在目标工况下溶解的珊瑚基材料 | ("coral skeleton" OR "coralline") AND ("hydroxyapatite" OR "CaCO3") AND ("adsorption" OR "removal") AND ("heavy metal" OR "phosphate") | CaCO₃/羟基磷灰石吸附重金属的实验数据 |
| coral-skeleton | 煅烧温度影响珊瑚 CaCO₃ 晶型转变和吸附性能 | 温度参数缺失导致无法指导材料合成 | ("coral") AND ("calcination" OR "thermal treatment") AND ("crystal phase" OR "aragonite") AND ("adsorption") | 煅烧条件→晶型→吸附性能 |
| magnetic-bacteria | 趋磁细菌磁小体可作为磁性吸附剂实现磁分离回收 | 若磁小体不稳或功能化困难，材料无法回收 | ("magnetotactic bacteria" OR "magnetosome") AND ("adsorption" OR "functionalization") AND ("heavy metal" OR "water treatment") | 磁小体提取、功能化、吸附性能 |
| magnetic-bacteria | 磁小体外膜功能基团可捕获污染物 | 功能基团密度和选择性未知 | ("magnetosome") AND ("surface modification" OR "functionalization") AND ("catechol" OR "amine") AND ("adsorption") | 磁小体表面功能化数据 |
| pitcher-plant | 猪笼草 SLIPS 策略在高流速下润滑液可能被冲刷 | 若润滑液不稳，防污应用会失效 | ("Nepenthes" OR "pitcher plant") AND ("SLIPS" OR "slippery liquid-infused") AND ("stability" OR "durability" OR "lubricant loss") | 润滑液流失速率和补充机制 |
| lobster-exoskeleton | 壳聚糖珠(Chitosan beads)六种吸附机制 | 需要 chitosan beads 吸附重金属的对口论文 | ("chitosan bead" OR "chitosan sphere") AND ("adsorption" OR "mechanism") AND ("heavy metal" OR "Cu" OR "Pb" OR "Cd") | chitosan beads 的吸附机制分析 |
| spider-silk | 蜘蛛丝抗污染机制 | 需要蜘蛛丝蛋白抗污的对口论文 | ("spider silk" OR "spidroin") AND ("antifouling" OR "anti-biofouling") AND ("protein" OR "surface") | 蜘蛛丝抗污性能数据 |
| dna-aptamer | DNA适配体在不同pH/温度/离子强度下的结合稳定性 | 适配体构象敏感，失效边界未知可能导致错误选材 | ("DNA aptamer") AND ("stability" OR "thermal stability" OR "pH stability") AND ("binding" OR "affinity" OR "dissociation") | 适配体在不同工况下的结合常数和构象稳定性 |

---

> ⚠️ 硬规则提醒：以上所有 `upgrade_candidate` 仅为建议。实际升级 verified 需：①打开 PDF ②定位到原文段落/表格 ③提取 locator + quote ④Yao/Codex 批准。未完成上述步骤前，所有条目保持 needs_review。
