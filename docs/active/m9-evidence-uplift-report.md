# M9 Evidence Uplift Report

**Date**: 2026-06-21
**HEAD**: 44eff95
**Branch**: review

## Executive Summary

M9 evidence uplift assessment for 12 ADRMATS-visible priority candidates. 191 causal chains identified as upgradeable from llm_inferred to from_source (have DOI but lack quote/locator). PDF access needed for actual upgrades. Current state documented honestly.

## Evidence State — Priority Candidates

| Prototype | Mechs | Perf | SV | SBI | GI | Perf Quotes | Perf DOIs |
|-----------|-------|------|-----|------|-----|-------------|-----------|
| chitosan | 110 | 99 | 2 | 90 | 18 | 62 | 76 |
| mussel-foot-adhesion | 55 | 41 | 2 | 44 | 9 | 41 | 23 |
| polydopamine-coating | 35 | 42 | 1 | 28 | 6 | 42 | 27 |
| plant-tannin | 7 | 15 | 1 | 6 | 0 | 15 | 15 |
| fish-scale-hydroxyapatite | 3 | 22 | 1 | 1 | 1 | 22 | 7 |
| oyster-shell | 2 | 6 | 1 | 1 | 0 | 6 | 6 |
| diatom-frustule | 6 | 20 | 0 | 6 | 0 | 20 | 20 |
| silk-fibroin | 17 | 18 | 2 | 15 | 0 | 18 | 18 |
| chlorella-cell-wall | 13 | 18 | 13 | 0 | 0 | 0 | 18 |
| lotus-leaf | 33 | 4 | 0 | 30 | 3 | 0 | 4 |
| superhydrophobic-artificial | 60 | 8 | 0 | 42 | 18 | 7 | 0 |
| water-strider-leg | 52 | 0 | 0 | 52 | 0 | 0 | 0 |

## Upgradeable Causal Chains

| Prototype | Upgradeable (SBI→SV) | Barrier |
|-----------|---------------------|---------|
| chitosan | 90 | Need PDF quote/locator verification |
| mussel-foot-adhesion | 44 | Need PDF quote/locator verification |
| polydopamine-coating | 28 | Need PDF quote/locator verification |
| silk-fibroin | 15 | Need PDF quote/locator verification |
| plant-tannin | 6 | Need PDF quote/locator verification |
| diatom-frustule | 6 | Need PDF quote/locator verification |
| fish-scale-hydroxyapatite | 1 | Need PDF quote/locator verification |
| oyster-shell | 1 | Need PDF quote/locator verification |
| **Total** | **191** | PDF access required |

## DOI Overlap (Perf ↔ Mechs)

| Prototype | Perf DOIs | Mech DOIs | Overlap |
|-----------|-----------|-----------|---------|
| chitosan | 28 | 32 | 23 |
| mussel-foot-adhesion | 12 | 15 | 8 |
| polydopamine-coating | 15 | 18 | 12 |
| plant-tannin | 5 | 6 | 5 |

Overlap DOIs indicate mechanisms that share references with performance data having quotes. These are the highest-priority upgrade targets.

## Honest Assessment

### What M9 Achieved
- Documented evidence state for all 12 priority candidates
- Identified 191 upgradeable causal chains with DOI references
- Mapped DOI overlap between perf quotes and mechanism references

### What M9 Cannot Do Without PDF Access
- Actual quote/locator extraction for causal chain upgrades
- Verification that specific mechanism claims are supported by specific perf quotes
- Upgrade llm_inferred to from_source basis

### Evidence Quality by Domain
- **Heavy metals (Pb, Cu, Cr)**: Strongest — chitosan, mussel, PDA, fish-scale have perf quotes
- **Dye (MB)**: Good — silk-fibroin, chlorella-cell-wall, chitosan have data
- **Organic micropollutants (BPA, SMX, PFOA)**: Weak — mostly inference, limited direct evidence
- **Oil-water separation**: Weak — no adsorption evidence, physical separation only

## Recommendation

1. Use OpenClaw for PDF extraction on top 20 high-impact causal chains (chitosan, mussel, PDA)
2. Upgrade where quote/locator supports the claim
3. Demote to inference where no supporting quote found
4. This is M10 work (full QA) or a dedicated evidence extraction sprint

## Validation Results

All validators pass (same as M8 final state).
