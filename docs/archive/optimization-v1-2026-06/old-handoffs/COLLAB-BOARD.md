# COLLAB-BOARD

> 读 COLLABORATION-PROTOCOL.md 了解协作规则。
> Qoder 分配任务，Claude Code 执行并更新 status。

## TASK-001: Enrichment Mirror Gap Fill
- status: assigned
- priority: high
- assigned_to: clcode
- input: prototypes_db/enrichment/*.json + prototypes_db/*.json (主库) + 仿生文献库/ PDF
- output: docs/optimization-v1/review-clcode-enrichment-audit.md
- notes: |
    525/525 enrichment causal_chain 为空。4个enrichment文件为空{}。
    只从主JSON中有source-backed的mechanism提取causal_chain。
    不要机械同步。产出每个原型的enrichment填充建议表。

## TASK-002: Missing PDF Path Verification (chitosan)
- status: assigned
- priority: high
- assigned_to: clcode
- input: prototypes_db/chitosan.json + 仿生文献库/ PDF 目录
- output: docs/optimization-v1/review-clcode-missing-pdf-paths.md
- notes: |
    chitosan 有99个missing_pdf项。逐一检查source_file路径是否在本地存在。
    注意 2.pdf/ 3.pdf 后缀变体。产出路径映射表：JSON路径 -> 实际本地路径 或 confirmed_missing。

## TASK-003: Lotus-Leaf Mechanism Classification
- status: assigned
- priority: medium
- assigned_to: clcode
- input: prototypes_db/separation/lotus-leaf.json
- output: docs/optimization-v1/review-clcode-lotus-classification.md
- notes: |
    355个mechanisms按实际生物/材料来源分组：
    lotus-specific / water-strider / shark-skin / gecko / rose-petal / Janus-membrane / MOF / artificial-sponge / generic-wetting / other。
    每类列出source DOI和条数。

## TASK-004: Cellulose-Nanocrystal Material Classification
- status: assigned
- priority: medium
- assigned_to: clcode
- input: prototypes_db/materials_reference/cellulose-nanocrystal.json
- output: docs/optimization-v1/review-clcode-cnc-classification.md
- notes: |
    按材料类型分组：CNC / CNF / general-cellulose / chitosan-cellulose / cellulose-MOF / oil-sorbent / membrane / diatomite-composite / tannin-cellulose。
    每类列出条目数和代表性source。
