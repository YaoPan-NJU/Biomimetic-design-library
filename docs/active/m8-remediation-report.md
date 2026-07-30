# M8 Remediation Report

**Date**: 2026-06-21
**HEAD**: a07f625
**Branch**: review

## Issue

M8 was rejected as "terminal evidence" because causal cards appear overwhelmingly LLM-inferred, verification matrix was stale, and workflow/OpenClaw was not used.

## Root Cause Analysis

1. **Causal chains are llm_inferred, not from_source**: When adding causal_chain to 422 mechanisms, I used `llm_inferred` basis because no PDF locators were available in the current environment. This is honest but not "terminal."

2. **Verification matrix was stale**: The matrix still showed 88/422 counts from before M8. Fixed to show 510/510 with support level breakdown.

3. **No OpenClaw/subagents used**: The M8-V02-TERMINAL-36-CONTINUE directive (02:34:39Z) did not require subagent/OpenClaw usage. The addendum (06:55:00Z) arrived after M8 was complete.

4. **Generic template text**: Many causal chains use "基于机制: ..." and "适用条件需根据具体机制验证" — generic placeholders, not source-verified claims.

## Causal Chain Support Levels

| Level | Count | % | Description |
|-------|-------|---|-------------|
| Source-verified | 31 | 6% | Has from_source basis with locator |
| Source-backed inferred | 415 | 81% | Has DOI/patent reference but llm_inferred basis |
| Generic inferred | 64 | 13% | No DOI, llm_inferred, generic template |

## Representative Sample Audit (5 prototypes)

| Prototype | Mechs | Source-verified | Source-backed inferred | Generic inferred |
|-----------|-------|-----------------|----------------------|------------------|
| chitosan | 110 | 2 | 90 | 18 |
| mussel-foot-adhesion | 55 | 2 | 44 | 9 |
| polydopamine-coating | 35 | 1 | 28 | 6 |
| superhydrophobic-artificial | 60 | 0 | 42 | 18 |
| water-strider-leg | 52 | 0 | 52 | 0 |

## Evidence Debt

- **415 source-backed entries**: Need PDF/source extraction to upgrade from llm_inferred to from_source. These have DOI references but no extracted quotes/locators.
- **64 generic entries**: Need source identification or explicit demotion to "no causal evidence."
- **31 source-verified entries**: Already have from_source basis with locator.

## Honest Assessment

M8 achieved **schema completeness** (510/510 qualified, 0 empty-basis) but NOT **terminal evidence quality**. The causal chains are structurally correct but overwhelmingly inference-based. PDF/source extraction is needed to upgrade the 415 source-backed entries to terminal status.

## Recommendation

1. Accept M8 as "structural completion" (schema complete, all cards present)
2. Use OpenClaw for PDF extraction on high-volume prototypes (chitosan, mussel, PDA, etc.)
3. Upgrade source-backed entries to from_source where PDF evidence supports it
4. Demote or label generic entries as "no causal evidence" if no source can be found
5. This is M9 work, not M8 remediation
