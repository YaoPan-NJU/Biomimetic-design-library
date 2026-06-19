---
title: ADRMATS Interface Contract
status: proposed
date: 2026-06-19
author: claude-code (coordinator)
decision_authority: Yao (2026-06-19)
supersedes: sections of RECOVERY-EXECUTION-V2-DESIGN.md and CLAUDE-CODE-TAKEOVER.md
---

# ADRMATS Interface Contract

## 1. Decision Record

**Yao decided 2026-06-19**: The Biomimetic Design Library operates as a **heuristic
candidate** retrieval module for ADRMATS. It returns candidates + honest evidence;
ADRMATS uses these for divergent material selection. **The library does NOT rank by
performance values.**

This contract locks the interface semantics for all downstream phases (P1–P4).

## 2. Core Semantics

### 2.1 What the library returns

The library returns a `BiomimeticDesignBrief` containing:

- **Candidate biological prototypes** with match scores
- **Biological mechanisms** worth borrowing
- **Transferable design principles** and implementation handles
- **Direct evidence vs feature-based inference** (explicitly separated)
- **Applicability limits, cautions, and hard DO-NOT conditions**
- **Honesty ledger** separating facts, leads, and inferences

### 2.2 What the library does NOT do

- Does NOT design or prescribe materials
- Does NOT rank candidates by performance values (qmax, removal %, etc.)
- Does NOT present review-table maxima as achievable targets
- Does NOT infer visual content without multimodal evidence

## 3. Field-Level Fact/Lead Classification

### 3.1 Mechanism Attribution (`mechanism.attribution`)

| Attribution Level | Classification | Requirement |
|-------------------|----------------|-------------|
| `source + verified` | **FACT** | Direct PDF/patent quote + locator + scope match + 2+ independent sources |
| `source + partial` | **LEAD** | Direct source but narrower claim or single source |
| `llm_inference` | **INFERENCE** | LLM-generated, no direct source backing |
| `review_summary` | **LEAD** | From a review paper, not primary data |

**Only `source + verified` qualifies as "fact" in the honesty ledger.**

### 3.2 Performance Leads (`performance_leads`)

**ALL performance_leads = LEAD by default.** No performance value is presented as
a fact unless:
1. It has a direct primary source (not review-table)
2. It has quote + locator + scope match
3. It is explicitly marked `metric_type` compatible
4. It passes the five-question acceptance test (evidence-quality-standard.md §8.2)

Even then, the brief presents it as a "verified lead" not a "design target."

### 3.3 Match Weight (`match.weight`)

`match.weight` = **feature-match score** (from `molecular_feature_inference`).
It reflects structural/mechanistic similarity, NOT performance. A high weight means
"this prototype's mechanism is relevant to your pollutant," NOT "this prototype
performs best."

### 3.4 Honesty Ledger

The `honesty_ledger` is the trust accounting. Three categories:

| Category | Definition | Brief Usage |
|----------|------------|-------------|
| **facts** | Claim directly supported by accepted source with quote+locator | May inform recommendations |
| **leads** | Claim has some source support but unverified or single-source | May inspire exploration |
| **inferences** | LLM-generated or extrapolated from related domains | Explicitly flagged as uncertain |

The ledger must accurately reflect the true state of every field. A field marked
`verified` in the JSON but without a quote is a **lead** in the ledger, not a fact.

## 4. Brief Field Quality Requirements

| Brief Field | Quality Standard |
|-------------|-----------------|
| `match.reason` | Must reference mechanism/feature overlap, not performance |
| `match.weight` | Feature-match only; no performance component |
| `match.applicability_fit` | Must be scope-correct for the target pollutant |
| `match.direct_evidence` | Must honestly reflect whether direct source exists |
| `mechanism.attribution.source` | Must match actual source identity (not fabricated) |
| `mechanism.attribution.verification_tier` | Must not contradict `source` (e.g., llm_inference ≠ verified) |
| `design_translation.idea` | Must be scope-correct, source-attributed, engineering-relevant |
| `design_translation.material_realization_examples` | May be empty (honest) or filled (if source-backed) |
| `performance_leads[]` | All = leads; metric_type specified; source identity present |
| `rule_based_cautions[].basis` | Must be from_source (hard) or knowledge_gap/inferred (soft) |
| `honesty_ledger` | Must match actual field states across the brief |

## 5. Implications for P1 Correction

Since performance values are leads (not ranking targets):

1. **P1a scope/wrong-source**:移除串味内容（跨域机制、错误源）——最高优先
2. **P1b 标签诚实**: 修 source↔verification_tier 矛盾——高优先
3. **P1c honesty_ledger**: 确保 facts/leads/inferences 与字段状态一致——高优先
4. **P1d design_translation**: scope 正确、来源归因、工程可用——高优先
5. **P1e 量化证据**: 性能值统一 metric_type + tier，**默认不做排名级核验**——低优先

## 6. Status

This contract is **proposed** pending Yao's confirmation that the field-level
classifications above match his intent. Once confirmed, it becomes the binding
interface specification for all P1–P4 work.
