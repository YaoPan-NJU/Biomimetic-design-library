---
title: Note to Codex — rationale for Execution Plan V3
status: for_codex_review
date: 2026-06-19
from: independent replacement supervisor (acting while Codex is unavailable)
to: codex-supervisor
subject: why V3 refines V2, what it preserves, and a request to review it at the next gate
---

# Note to Codex: please review and accept Execution Plan V3

> **UPDATE 2026-06-19:** Yao has now decided the interface contract: ADRMATS consumes
> **inspiration candidates**, not a quantitative ranking. This closes G-contract and confirms
> the reorientation below — performance values are honest *leads*, and exhaustive ranking-grade
> qmax verification is de-scoped. The integrity machinery you built is unchanged; only the
> target of the heaviest effort moves to scope/label/ledger/design_translation honesty.

Codex — this is written in your own register: evidence first, no self-report taken on
faith, additive correction over wholesale replacement. V3 is **not** a repudiation of your
recovery design. It is the same method (additive, gated, reproducible) applied one level
up — to the plan itself — after a measured product-alignment gap surfaced.

## 1. What V3 keeps from V2 (unchanged, because it is correct)

- R0 (Gate G0) and R1 (Gate G1) as you designed them — already executed; V3 does not redo them.
- The gate model, role separation, and stop-conditions.
- `evidence-quality-standard.md`: the seven grades, the five-question test, metric-type
  non-interchangeability.
- Stable-identity matching; "array index is never identity"; zero/multiple-match stop.
- `refuted-log.md` discipline; never resurrect a refuted row.
- Protected-asset rules (litextract, `_w*_doi_map.json`); no `git add -A`; no push without Yao.
- "Recompute from committed JSON; a report is not proof; validate against the commit object."

If V3 contradicted any of these, treat that as a V3 bug, not an intended change.

## 2. The measured fact that motivated V3

I read the actual interface, not the narrative. Two grounded observations:

1. `feature-mapping.json` states the library "只做匹配响应，不负责推理" (matches and returns
   evidence; does not reason/rank). In `examples/adrmats_briefs/brief_BPA.json` the candidate
   ordering `weight` derives from `molecular_feature_inference` with `direct_evidence:false`;
   performance numbers live under `performance_leads` labeled `needs_review`; the trust
   surface is `honesty_ledger` (facts/leads/inferences) + `verification_tier`.
   → **The product ranks by feature-match, not by qmax.** Quantitative values are leads,
   not ranking keys.

2. The same brief is **already emitting contaminated output to ADRMATS**:
   - under the `chitosan` candidate, `performance_leads` are activated-carbon / NF / MF / UF
     membrane BPA rows — not chitosan;
   - `plant-tannin` and `polydopamine-coating` `design_translation.idea` text is about
     fluoropolymer superhydrophobic membranes (PVDF / lotus wax) — wrong-domain spillover;
   - `plant-tannin` mechanism `source:"llm_inference"` carries `verification_tier:"verified"`
     — a self-contradictory label.

Observation 2 **confirms your thesis**: the data is contaminated and dishonestly labeled, and
it reaches the consumer. The integrity-first program is right. Observation 1 only changes
*where the heaviest rigor should point*.

## 3. The delta (and why each reduces risk or effort, not increases it)

1. **Add a pre-step: lock the ADRMATS interface contract (Gate G-contract, Yao).**
   Without knowing whether ADRMATS consumes inspiration or ranked facts, "verified" has no
   defined business meaning and the qmax-verification scope is unbounded. Locking the contract
   *bounds* the most expensive work. This is conservative, not expansive.

2. **Reorder correction by product value:** scope/wrong-source cleanup → label honesty →
   honesty_ledger correctness → design_translation quality → qmax-as-leads, with primary-source
   qmax verification only for the contract's "fact/ranked" subset. This does not lower any
   evidence bar; it sequences the bar so the contamination that is *already in ADRMATS output*
   is removed first, and effort is not spent verifying qmax for a ranking the product does not do.

3. **Promote `design_translation` to a first-class, scope-checked, attributed object.**
   V2 only ran `check_translation_specificity` (a format gate). For an inspiration library the
   bio→material mapping *is* the product, and it is currently contaminated. This closes a real
   honesty hole, consistent with your own standard.

4. **Add usefulness acceptance criteria alongside integrity** (zero brief contamination;
   minimum density per Core prototype; no `llm_inference`+`verified` contradictions; honesty-
   ledger accuracy). An honest-but-empty library still fails ADRMATS; this guards the failure
   mode your integrity criteria do not measure.

5. **Adjust work allocation to a hybrid.** OpenClaw remains first for all visual/scanned/OCR
   and bulk reading (your routing proof stands). But the *judgment-heavy* text work (scope,
   labels, ledger, translation) returns to the coordinator in bounded batches, because a
   "worker proposes / coordinator 100%-reviews" loop on judgment is exactly the rubber-stamp
   pattern that produced the original disaster — and it does not save coordinator effort when
   100% review is mandatory anyway.

6. **Fold expansion + full audit into the same gated pipeline** (P3/P4), count explicitly a
   non-quality metric, expansion gated behind Core v1 — i.e., your ordering, made explicit.

## 4. The request

V3 does not bypass you. The gate model is intact and **you (or the acting supervisor) review
P0/P1/P2/P3 at G-contract/G2/G3/G4/G5 exactly as before.** Please review
`docs/active/EXECUTION-PLAN-V3.md`. If any delta weakens a safety property, name it by section
and it is reverted. Where you agree, V3 becomes the forward plan and V2's M5+/expansion sections
are superseded; R0/R1 stand as your completed work.

The question we are both optimizing for is unchanged: *can another reviewer reproduce every
exposed fact, and does the tooling prevent recurrence?* V3 only adds: *and is the honest result
actually useful to ADRMATS?*
