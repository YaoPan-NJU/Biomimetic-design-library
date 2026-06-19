# OpenClaw Review Coordination Protocol

status: active

Last updated: 2026-06-16

## Role Split

### OpenClaw owns bulk evidence work

OpenClaw should do the high-volume work:

- read local PDFs and extraction JSONs;
- normalize source paths and find matching PDFs;
- OCR or visual-read scanned patents where needed;
- verify claims row by row;
- draft batch audit files with field paths, quotes, locators, and evidence labels;
- build literature-to-file/path mapping tables;
- propose candidate fixes, boundaries, and DO-NOT items.

### Codex owns control and acceptance

Codex should not be the main bulk extractor. Codex owns:

- batch selection and scope control;
- OpenClaw task prompts and acceptance criteria;
- spot-checking fragile or high-impact claims against PDFs;
- deciding whether OpenClaw output is decision-ready;
- adding only accepted findings to `review-full-audit-decision-queue.md`;
- adding only evidence-graded boundaries to `review-boundary-do-not-register.md`;
- maintaining worklog/sync summary and GitHub checkpoints;
- escalating unclear items to Yao instead of silently editing the database.

## Hard Rules

- Do not modify `prototypes_db/*.json` before Yao approves queued actions.
- Do not run `tools/build_prototypes_db.py` during review.
- Do not upgrade `verification`, `hard_do_not`, or `soft_boundary` status without Yao approval.
- Treat missing PDFs, scanned patents, single-source review rows, and inferred-only boundaries as `knowledge_gap` or `needs_human_decision`.
- Use `hard_do_not` only for clear source-domain mismatch or directly quoted literature constraints.
- Preserve unrelated dirty changes, especially:
  - `docs/optimization-v1/phase5-chains.md`
  - `tools/litextract`
  - `tools/verify_adrmats_delivery.py`

## OpenClaw Batch Output Contract

Each OpenClaw batch must produce one Markdown file under `docs/optimization-v1/` using this naming pattern:

`review-full-audit-openclaw-batch-XX-<scope>.md`

The file must include:

- batch id and prototype/material ids;
- target JSON path for every item;
- exact field path, such as `performance_data[7]` or `mechanisms[3].causal_chain`;
- local PDF path or explicit `missing_pdf`;
- locator: page, paragraph, section, table, figure, patent paragraph, or OCR page;
- short quote, copied exactly enough to verify the claim;
- evidence label: `supported`, `partial`, `keep_soft`, `missing_pdf`, `wrong_source`, `inferred_only`, `needs_human_decision`;
- recommended action;
- notes on duplicates, scope mismatch, unit mismatch, and metric-type mismatch.

## Codex Acceptance Gate

Codex only accepts an OpenClaw item into the decision queue when it has:

- real target JSON path;
- real field path;
- source path or explicit missing-source status;
- locator;
- quote or explicit reason quote is impossible;
- evidence label;
- recommended action;
- no direct change to `prototypes_db`.

Codex should spot-check:

- all `wrong_source` and `hard_do_not` candidates;
- all high-capacity or top-ranking performance values;
- all scanned patent/OCR-derived values;
- all metric-type conversions, especially `%`, `mg/g`, `g/g`, rejection, permeance, and system-removal rows;
- any claim that would materially affect ranking or DO-NOT decisions.

## Current Priority Queue For OpenClaw

1. Commit/push checkpoint after Git write access is available: Batch 04, 05, and 06 docs are complete locally.
2. Start OpenClaw bulk verification for Batch 07 parked/registry consistency:
   - `prototypes_db/parked/namib-beetle.json`
   - duplicate/cross-directory source consistency
   - file/path mapping for original PDFs and extraction JSONs
3. Run targeted OpenClaw sub-batches:
   - `dna-aptamer`: build evidence from local aptamer PDFs/extractions.
   - `diatom-frustule`: deduplicate and normalize source paths before quote insertion.
   - `materials_reference/metal-organic-framework.json`: verify `single_source` semantics and wrong-source rows.
   - `materials_reference/starch-granule.json`: sanity-check extreme/mixed-unit values before ranking.

## Default OpenClaw Prompt

Use this prompt when starting a worker:

```text
你是 OpenClaw evidence-audit worker。项目路径：
/Users/panyao/Desktop/Biomimetic-design-library

只使用 mimo-v2.5。不要使用 mimo-v2.5-pro。

任务目标：
对指定 batch 的本地 JSON、PDF、extraction JSON 做证据审计。你负责批量读取原始文献、定位 PDF、核对字段、建立文献内容和文件路径/文件名的对应关系，并输出一个 Markdown 审计批次文件。

硬性限制：
- 不要修改 prototypes_db/*.json。
- 不要运行 tools/build_prototypes_db.py。
- 不要改变 verification 或 hard/soft 状态。
- 不要提交 git。
- 缺 PDF、扫描专利、OCR 不确定、只来自综述表或 LLM 推断的内容，标为 missing_pdf / needs_human_decision / knowledge_gap / inferred_only，不要升级成 hard_do_not。
- 只有明确来源错配或直接文献支持的边界，才可以建议 wrong_source 或 hard_do_not。

输出文件：
docs/optimization-v1/review-full-audit-openclaw-batch-XX-<scope>.md

每个候选项必须包含：
- prototype_id 或 material_id
- target_json
- field_path
- claim_summary
- local source_file 或 missing_pdf
- locator（页码/段落/表/图/专利段落/OCR页）
- quote（可短，但必须足以核对）
- evidence_label
- recommended_action
- notes

不要直接改数据库。最终决策由 Yao 批准，Codex 只负责验收和排队。
```

## Reporting Cadence

- OpenClaw writes batch output.
- Codex reviews batch output and either accepts items into the queue or sends correction instructions.
- After each accepted batch, Codex updates worklog/sync summary and pushes branch `review` when Git write access is available.
