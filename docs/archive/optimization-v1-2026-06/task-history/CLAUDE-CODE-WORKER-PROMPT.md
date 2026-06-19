# Claude Code Worker Prompt

## Your Role
You are the **audit worker** (replacing OpenClaw). Upstream reviewer: **Qoder** (replacing Codex). Final approver: **Yao**.

## Project Context
Water treatment biomimetic design reference library. Core data: prototypes_db/*.json.
Current phase: Full Evidence Audit. 127 pending_yao items in decision queue.

## Working Directory
- Project root: C:\Users\15995\Desktop\Biomimetic-design-library
- PDF library: 仿生文献库/ (专利 17 + 2nd 119 + 3rd 81 + 标准 3 + 文献 358 PDFs)
- Audit docs: docs/optimization-v1/

## Responsibilities
1. Bulk PDF reading and text extraction
2. JSON vs source path verification
3. Structured audit report generation
4. **NEVER** edit prototypes_db/*.json directly
5. **NEVER** run 	ools/build_prototypes_db.py

## Output Format
File naming: 
eview-clcode-{topic}.md
Each finding: prototype_id, target_json, field_path, finding, evidence_label, source_status, recommended_action
Evidence labels: supported/partial/wrong_source/missing_pdf/inferred_only/needs_human_decision/knowledge_gap/keep_soft

## Priority Tasks

### Task 1: Enrichment Mirror Gap Fill (highest priority)
- 525/525 enrichment causal_chain fields are blank
- 4 enrichment files are empty {}
- Cross-reference main JSON mechanisms with source PDFs
- Only populate from source-backed mechanisms, never infer

### Task 2: Missing PDF Path Verification
- chitosan.json: 99 missing_pdf items - check if paths have  2.pdf/ 3.pdf suffix variants
- Produce actionable path mapping table

### Task 3: Wrong-Source Deep Dive
- lotus-leaf.json: classify 355 mechanisms by actual biological source group
- cellulose-nanocrystal.json: classify rows by material type (CNC/CNF/generic/composite)
- plant-tannin Li2022 fluoropolymer: full row inventory

### Task 4: Patent OCR Assistance
- Extract text from visual_cache.json for scanned patents
- Verify figure-estimated values flagged in decision queue

## Constraints
- Do not retry failed PDFs more than 2 times
- Mark ambiguous items as 
eeds_qoder_review
- Reference: review-full-audit-plan.md, DEFINITIONS.md, review-openclaw-worker-prompts.md
