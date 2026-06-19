---
title: R0 OpenClaw Capability Report
status: gate_g0_pending_review
date: 2026-06-19
author: claude-code (coordinator)
baseline_commit: 32843b4
cloud_baseline: origin/review@e4dc2d0
---

# R0 OpenClaw Capability Qualification Report

## Summary

**Result: PASS** — all 9 tests passed. Both MIMO key slots, both model routes (text +
multimodal), genuine pixel-based image inspection, per-dispatch model switching via agent
selection, zero unintended fallback, workspace file access, and 3-worker concurrent
orchestration all verified.

## Environment

- OpenClaw 2026.6.8 (844f405)
- macOS Darwin 25.4.0
- `/opt/homebrew/bin/openclaw`
- `--local` embedded path (gateway path not tested)

## Key Slots

| Slot | Provider | Agent Tested | Primary Model |
|------|----------|-------------|---------------|
| key_slot_1 | xiaomi | main | mimo-v2.5-pro |
| key_slot_2 | xiaomi-2 | yang-s-clawedbot | mimo-v2.5-pro |

Both slots authenticated independently. MIMO API keys loaded from `tools/litextract/.env`.

## Test Results

| Test | Slot | Model | Modality | Result | Fallback |
|------|------|-------|----------|--------|----------|
| R0-T1 | xiaomi | mimo-v2.5-pro | text | ✅ PASS | false |
| R0-T2 | xiaomi-2 | mimo-v2.5-pro | text | ✅ PASS | false |
| R0-T3 | xiaomi | mimo-v2.5 | multimodal | ✅ PASS | false |
| R0-T4 | xiaomi-2 | mimo-v2.5 | multimodal | ✅ PASS | false |
| R0-T5 | xiaomi | mimo-v2.5-pro | workspace access | ✅ PASS | false |
| R0-T6 | xiaomi | mimo-v2.5-pro | text (concurrent) | ✅ PASS | false |
| R0-T7 | xiaomi | mimo-v2.5 | multimodal (concurrent) | ✅ PASS | false |
| R0-T8 | xiaomi | mimo-v2.5-pro | text (concurrent) | ✅ PASS | false |
| R0-T8b | xiaomi-2 | mimo-v2.5-pro | text | ✅ PASS | false |

### Multimodal Fixture

50×50 pixel pure-red PNG. Both xiaomi and xiaomi-2 slots correctly identified "red"
via the `process` tool — confirming genuine pixel-based image processing, not a text-only
ping.

### Concurrency

Three workers dispatched simultaneously (R0-T6/T7/T8), each with unique task IDs and
isolated workspaces. All completed without interference.

## Model Routing

- **Text tasks**: `mimo-v2.5-pro` via `xiaomi` and `xiaomi-2` providers
- **Multimodal tasks**: `mimo-v2.5` via `xiaomi` and `xiaomi-2` providers
- **Per-dispatch switching**: achieved via agent selection (each agent has a fixed
  primary model; different agents = different models)
- **Fallback providers configured**: openai/gpt-5.5, qwen-cloud/qwen3.6-plus,
  moonshot/kimi-k2.5 — **none triggered** in any test

## Agents Used

| Agent | Model | Purpose | Status |
|-------|-------|---------|--------|
| main | xiaomi/mimo-v2.5-pro | Pre-existing, text | Production |
| yang-s-clawedbot | xiaomi-2/mimo-v2.5-pro | Pre-existing, text | Production |
| bmdl-text | xiaomi/mimo-v2.5-pro | Created for R0, text | Test artifact |
| bmdl-visual | xiaomi/mimo-v2.5 | Created for R0, multimodal | Test artifact |
| bmdl-visual-2 | xiaomi-2/mimo-v2.5 | Created for R0, multimodal slot 2 | Test artifact |
| lit-extract | mimo/mimo-v2.5-pro | tools/litextract config, broken agentDir | Non-functional |

## Diagnostics

### Model Override Restriction

`openclaw agent --model <override>` is **not allowed** for existing agents. Workaround:
create separate agents with different primary models. This is the intended architecture
per RECOVERY-EXECUTION-V2-DESIGN §5.1.

### lit-extract Agent

The `lit-extract` agent in `tools/litextract/openclaw.json` references an agentDir at
`/Users/panyao/Qoder/JJJ_Literature/agents/lit-extract/agent` which no longer exists.
This agent is non-functional and should not be used for R1+ work.

## Residual Risks

1. **Model override not per-dispatch**: switching models requires pre-configured
   agents, not a runtime flag. This is an architectural constraint, not a bug.
2. **Fallback providers**: configured but never triggered. They could activate on MIMO
   outage — the no-fallback guarantee holds only when MIMO is available.
3. **lit-extract broken path**: needs repair or replacement before production use.
4. **Test agents cleanup**: bmdl-text, bmdl-visual, bmdl-visual-2 are test artifacts
   that should be removed or promoted to production before R1.
5. **No stress test**: both slots were not tested under simultaneous high load.

## Pass Criteria

| Criterion | Status |
|-----------|--------|
| Both MIMO key slots independently | ✅ |
| mimo-v2.5-pro text reasoning on each | ✅ |
| Genuine pixel-based mimo-v2.5 on each | ✅ |
| Per-dispatch model switching | ✅ |
| Zero unintended fallback | ✅ |
| Workspace file access | ✅ |
| Max 3 concurrent isolated workers | ✅ |

## Gate G0 Recommendation

**PASS** — R0 qualification complete. Safe to proceed to R1 (recovery machinery
correction) pending independent review of this report.

Exact commit: `32843b4`
Report hash: (see .json companion)
