# Worker Relay Protocol

**Created**: 2026-06-21
**Status**: Active

## Architecture

```
Codex ──directive──▶ codex-outbox ──poll──▶ CC (this session)
  ▲                                           │
  │                                           ├── text/mechanism/scope tasks → execute directly
  │                                           ├── PDF/OCR tasks → delegate to OpenClaw (if available)
  │                                           └── results ──▶ cc-outbox ──▶ Codex
  │
  └─────────────────────── review/accept ──────┘
```

## Mailbox Convention

| Mailbox | Direction | Contents |
|---------|-----------|----------|
| `codex-outbox/` | Codex → CC | DIRECTIVE files from Codex |
| `cc-outbox/` | CC → Codex | REVIEW_REQUEST, STATUS files from CC |

CC must NOT write REVIEW_REQUEST into `codex-outbox/`.

## Polling Schedule

- **Interval**: 120 seconds (2 min)
- **Cron ID**: `53aa270d`
- **Target**: `runtime/codex-outbox/`
- **Protocol**: Read latest JSON → if unprocessed DIRECTIVE → execute → send REVIEW_REQUEST to `cc-outbox/`

## Task Routing

| Task Type | Executor | Model |
|-----------|----------|-------|
| JSON edits, mechanism fixes, scope decisions | CC (this session) | mimo-v2.5 |
| Text audit, validator runs | CC (this session) | mimo-v2.5 |
| PDF extraction, OCR | OpenClaw worker (if available) | mimo-v2.5 (multimodal) |
| Verification quote extraction | CC (this session) | mimo-v2.5 |

## Constraints

- Max 3 parallel subagents (API key limit)
- No new prototypes, no 60-80 expansion
- No prototype delete/merge/park/rename without ASK_YAO
- No git push without explicit user request
