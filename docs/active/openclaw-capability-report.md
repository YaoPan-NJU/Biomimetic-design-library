---
title: R0 OpenClaw Capability Report
status: gate_g0_pending_review
date: 2026-06-19
author: claude-code (coordinator)
baseline_commit: e66f674
---

# R0 OpenClaw Capability Qualification Report (v3 — real multimodal)

## Summary

**Result: PASS** — both key slots independently confirmed with genuine pixel-based
mimo-v2.5 inspection on a real scanned patent page. No OCR preprocessing, no Tesseract,
no pdftotext — image sent as base64 directly to mimo-v2.5 API.

## Multimodal Verification (Real Patent OCR)

**Fixture**: CN114849640A (鱼鳞提取羟基磷灰石吸附剂), page 1, 200 DPI PNG
- Image SHA-256: `ff687ab658005d4eb85ef577273f7d9194b2dc8235bc9cc0d562884aab75aca6`
- Source PDF: `仿生文献库/专利/2022-CN114849640A-羟基磷灰石-吸附-染料 2.pdf`

### Test Results

| Test | Key Slot | Model | Method | Prompt | Expected | Observed | Result | Fallback |
|------|----------|-------|--------|--------|----------|----------|--------|----------|
| G0-T1 | xiaomi | mimo-v2.5 | direct API base64 | "What is the number after (21)?" | 202210352494.4 | 202210352494.4 | ✅ PASS | false |
| G0-T2 | xiaomi-2 | mimo-v2.5 | direct API base64 via exec | "What is the number after (21)?" | 202210352494.4 | 202210352494.4 | ✅ PASS | false |

### Execution Metadata

**G0-T1 (key_slot_1, direct API)**:
- provider: xiaomi
- model: mimo-v2.5 (confirmed from API response)
- reasoning_tokens: 1427
- total_tokens: 5508
- elapsed: 16.8s
- fallbackUsed: false
- method: `requests.post` to MIMO `/v1/chat/completions` with base64 image

**G0-T2 (key_slot_2, via OpenClaw exec)**:
- provider: xiaomi-2 (via XIAOMI_API_KEY_2)
- model: mimo-v2.5 (confirmed from API response)
- reasoning_tokens: 930
- fallbackUsed: false
- method: OpenClaw yang-s-clawedbot agent → exec tool → Python script → MIMO API

### Why This Is Genuine Multimodal

1. **No OCR preprocessing**: Image sent as base64 directly to mimo-v2.5 API — no
   Tesseract, pdftotext, or any text extraction before the model
2. **Pixel-only field**: Application number `202210352494.4` can only be read from
   pixels — it's not in any text layer
3. **Both key slots**: xiaomi and xiaomi-2 independently confirmed
4. **API response metadata**: model=mimo-v2.5 confirmed from response, not config
5. **No fallback**: direct API calls, no provider switching

## Previous Test Results (v1/v2, retained for completeness)

| Test | Slot | Model | Result | Fallback |
|------|------|-------|--------|----------|
| R0-T1 | xiaomi | mimo-v2.5-pro | ✅ text | false |
| R0-T2 | xiaomi-2 | mimo-v2.5-pro | ✅ text | false |
| R0-T5 | xiaomi | mimo-v2.5-pro | ✅ workspace | false |
| R0-T6-T8 | xiaomi | mixed | ✅ 3 concurrent | false |
| R0-T8b | xiaomi-2 | mimo-v2.5-pro | ✅ text | false |

## Pass Criteria

| Criterion | Status |
|-----------|--------|
| Both MIMO key slots independently | ✅ |
| mimo-v2.5-pro text reasoning on each | ✅ |
| Genuine pixel-based mimo-v2.5 on each (base64 direct, no OCR) | ✅ |
| Per-dispatch model switching | ✅ |
| Zero unintended fallback | ✅ |
| Workspace file access | ✅ |
| Max 3 concurrent isolated workers | ✅ |

## Gate G0 Recommendation

**PASS** — R0 qualification complete with genuine base64-direct multimodal verification.
Safe to proceed to R1 pending independent review.
