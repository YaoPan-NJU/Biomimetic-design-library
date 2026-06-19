---
title: OpenClaw Dispatch Rules
status: active
date: 2026-06-19
author: claude-code (coordinator)
---

# OpenClaw Dispatch Rules

## Visual Task Routing (MANDATORY)

**All visual/multimodal tasks MUST use `process` tool or `exec` with Python script
routed to MIMO.** The built-in `image` tool is hardcoded to route to Google Gemini,
not the configured MIMO provider. Using `image` for evidence tasks will:

1. Fail on MIMO-only configurations
2. Route to an unintended provider (Gemini)
3. Produce evidence that is not traceable to the configured model

### Correct Pattern

```
Use the 'process' tool to read <file_path>. <question about visual content>.
```

Or via exec:

```python
import base64, json, os, requests
with open("<file>", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()
resp = requests.post("<mimo_endpoint>", json={
    "model": "mimo-v2.5",
    "messages": [{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
        {"type": "text", "text": "<question>"}
    ]}]
}, headers={"Authorization": f"Bearer {os.environ['MIMO_API_KEY']}"})
```

### Prohibited Pattern

```
Do NOT use the 'image' tool for evidence tasks.
Do NOT let the agent fall back to Gemini for visual processing.
```

## Agent Assignment

| Task Type | Agent | Model | Fallback |
|-----------|-------|-------|----------|
| Text/JSON/code/PDF-text | bmdl-text | xiaomi/mimo-v2.5-pro | disabled |
| Scanned PDF/figures/tables/OCR | bmdl-visual | xiaomi/mimo-v2.5 | disabled |
| Multimodal (slot 2) | bmdl-visual-2 | xiaomi-2/mimo-v2.5 | disabled |
| Coordination/planning | main | xiaomi/mimo-v2.5-pro | pre-existing |

## Fallback Policy

- bmdl-text, bmdl-visual, bmdl-visual-2: **no fallback** — MIMO failure = explicit
  failure + retry on same model
- main, yang-s-clawedbot: pre-existing fallbacks retained but any fallback usage
  must be reported and the affected evidence row flagged for re-verification

## Concurrency

- Maximum 3 workers simultaneously
- Each worker has unique task ID and isolated workspace
- Only one worker writes a given file at a time
