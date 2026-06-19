# OpenClaw Worker Prompt Pack

status: active

Last updated: 2026-06-16

Use these prompts with OpenClaw local workers. Run one worker at a time, or at most two, to avoid rate limits.

Always use `mimo-v2.5`. Do not use `mimo-v2.5-pro`.

## Shared Header

Paste this at the start of every worker message:

```text
你是 Biomimetic-design-library 的 OpenClaw evidence-audit worker。

项目路径：
/Users/panyao/Desktop/Biomimetic-design-library

模型要求：
- 只使用 mimo-v2.5。
- 不要使用 mimo-v2.5-pro。

硬性限制：
- 不要修改 prototypes_db/*.json。
- 不要运行 tools/build_prototypes_db.py。
- 不要提交 git。
- 不要修改 docs/optimization-v1/phase5-chains.md、tools/litextract、tools/verify_adrmats_delivery.py。
- 缺 PDF、扫描专利、OCR 不确定、只来自综述表或 LLM 推断的内容，标为 missing_pdf / needs_human_decision / knowledge_gap / inferred_only。
- 不要把 missing_pdf、扫描专利、single_source、inferred_only 升级为 verified 或 hard_do_not。
- 只有明确来源错配或直接文献支持的边界，才可以建议 wrong_source 或 hard_do_not。

输出要求：
- 写一个 Markdown 文件到 docs/optimization-v1/。
- 文件开头必须包含：
  status: ready_for_codex_acceptance
  worker: OpenClaw/mimo-v2.5
  completed_at: <本地时间>
- 每个候选项必须包含 target_json、field_path、source_file 或 missing_pdf、locator、quote、evidence_label、recommended_action、notes。
- 你只做证据审计和建议，不直接改数据库。
```

## Prompt 1: Batch 07 Parked/Registry

```text
执行 Task 07: Parked And Registry Consistency。

参考文件：
docs/optimization-v1/review-openclaw-coordination.md
docs/optimization-v1/review-openclaw-next-tasks.md

输出文件：
docs/optimization-v1/review-full-audit-openclaw-batch-07-parked-registry.md

审计范围：
- prototypes_db/parked/namib-beetle.json
- 全库 source_file / ref_doi / extraction JSON / PDF 路径一致性，优先覆盖已经审计的 Batch 01-06。

你要回答：
1. namib-beetle 为什么 parked：证据弱、范围重复、缺源、还是未完成策展？
2. 哪些现有 prototype 已包含 Namib beetle / fog-harvesting / cactus / honeycomb / pitcher 相关证据？
3. Batch 01-06 中有哪些源文件重复、路径不同、后缀不同、目录不同但指向同一文献？
4. 哪些高影响行仍然引用 bare filename，而本地存在 ` 2.pdf` 或 ` 3.pdf`？

必须输出这些表：
- parked item audit table
- duplicate/cross-directory source table
- original PDF path to extraction JSON mapping table
- candidate queue items table
- boundary/DO-NOT candidate table

优先给 Codex 决策用，不要做无关重构。
```

## Prompt 2: DNA Aptamer Evidence Build

```text
执行 Targeted Sub-Batch A: DNA Aptamer Evidence Build。

输出文件：
docs/optimization-v1/review-full-audit-openclaw-dna-aptamer-evidence-build.md

审计范围：
- prototypes_db/dna-aptamer.json
- prototypes_db/enrichment/dna-aptamer.json
- 仿生文献库/3rd/第B组-新方向/B1-DNA适配体/
- tools/litextract/outputs/extractions/第三波/json/ 中 aptamer 相关 JSON
- 仿生文献库/3rd/第三波-仿生吸附专利/2026-CN121588773A-aptamer-aflatoxin-adsorbent.pdf

目标：
先建立 source-grounded evidence map，不要直接建议写库。

必须区分：
- detection/biosensor only
- adsorption/capture/removal
- pathogen/toxin/heavy-metal/antibiotic target
- performance metric 类型：Kd、LOD、removal%、qmax、capture efficiency、recovery、regeneration

输出：
- literature-to-path mapping table
- biosensor-only vs adsorption/capture evidence table
- candidate performance table，仅限真实吸附/捕获/去除指标
- mechanism table，必须有 quote + locator
- boundary table，关注 target specificity、matrix effects、regeneration、immobilization、biosensor-vs-adsorbent scope

Codex 接受门槛：
没有 source path、locator、quote、metric type 的候选，不要放入 candidate queue。
```

## Prompt 3: Diatom Path/Dedup Cleanup

```text
执行 Targeted Sub-Batch B: Diatom Source Path And Dedup Cleanup。

输出文件：
docs/optimization-v1/review-full-audit-openclaw-diatom-path-dedup.md

审计范围：
- prototypes_db/diatom-frustule.json
- prototypes_db/enrichment/diatom-frustule.json
- 仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/
- 仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf

目标：
先做路径和去重，不要尝试一次性核完全部字段。

必须输出：
- current JSON source_file -> actual local PDF path mapping
- PDF -> extraction JSON mapping
- duplicated performance rows table
- diatom/frustule/diatomite vs unrelated structural-design evidence table
- candidate actions: normalize_path / deduplicate / keep_soft / missing_pdf / wrong_source / needs_human_decision

特别注意：
- 第三波 PDF 多数存在，但 JSON 往往只写 bare filename。
- 先 dedup，再决定是否插入 quote/locator。
```

## Prompt 4: MOF Verification Semantics

```text
执行 Targeted Sub-Batch C: MOF Verification Semantics。

输出文件：
docs/optimization-v1/review-full-audit-openclaw-mof-verification-semantics.md

审计范围：
- prototypes_db/materials_reference/metal-organic-framework.json

目标：
审计 verification 语义，而不是逐条升级。

必须回答：
1. 当前文件里 `verification = single_source` 实际意味着什么？
2. `provenance_summary.n_verified = 252` 是否等于 quote+locator verified？如果不是，如何降级或重新命名？
3. 哪些 rows 有本地 PDF 且可找到 quote/locator？
4. 哪些 rows 是明确 wrong_source？

必须重点核查 Codex 已怀疑的行：
- performance_data[23-36]：Aramesh2021 chitosan dye-removal review 是否污染 MOF？
- performance_data[77-80]：Cheng2024 membrane/catalytic BPA rows 是否污染 MOF？
- performance_data[88]：H2 storage wt% 是否不应进入 water-treatment adsorption ranking？

输出：
- verification semantics table
- suspicious row table
- wrong_source candidates table
- recommended queue items

不要提出 upgrade verified。只提出 downgrade/rename semantics、wrong_source、keep_soft、needs_human_decision。
```

## Prompt 5: Starch Extreme Value Sanity Check

```text
执行 Targeted Sub-Batch D: Starch Extreme Value Sanity Check。

输出文件：
docs/optimization-v1/review-full-audit-openclaw-starch-extreme-values.md

审计范围：
- prototypes_db/materials_reference/starch-granule.json

优先行：
- performance_data[52-59]
- performance_data[66-77]
- 任何 value > 1000 mg/g 的行
- 任何混合 `%`、`mg/g`、`g/g`、浓度依赖范围、review maximum 的行

目标：
防止极端综述表数值导致错误排名。

每个高风险值必须输出：
- target_json
- field_path
- pollutant
- value and unit
- source_file
- exact table/page/figure locator
- quote
- metric_type: qmax / removal% / concentration-derived capacity / range / review maximum / other
- experimental conditions if available
- recommendation: keep / demote / split / needs_human_decision / wrong_source

重点核查：
- Ihsanullah2022 starch review 中 Crystal Violet 24,375 mg/g 是否为浓度依赖容量范围而非通用 qmax。
- Khoo2023 中 oil 13,000 mg/g、pharmaceutical maxima 等是否为跨材料 review maximum，是否不应作为 starch-granule 直接 performance。
```
