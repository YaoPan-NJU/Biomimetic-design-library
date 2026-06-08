# AI Supervisor Directive

> 本文件由 Codex 更新，coffee-cli 每次开始工作、完成关键动作、进入下一个 milestone 前必须读取。
> 当前目标不是"跑完 Phase"，而是交付 ADRMATS 可调用的 v0.1 仿生启发检索模块。

---

## Current Decision

- `status`: `DELIVERY_COMPLETE`
- `current_milestone`: `Milestone 4`
- `decision_time`: `2026-06-08 19:50`
- `decision_owner`: `Codex`

## Decision Summary

Milestone 0-4 全部完成。v0.1 交付包已创建并推送到 `origin/feature/extraction-results`，tag `v0.1` 已创建。所有验收脚本通过（6/6），ADRMATS 接口可用，调用说明和风险文档已创建。

## Required Actions For coffee-cli

1. 无需进一步行动。
2. v0.1 交付完成。
3. 等待进一步指示。

## Evidence Expected Before Continuing

- `git status --short --branch` 显示本地与远端同步且工作区干净。
- `docs/AI_*.md` 已 commit + push，不能保持 untracked。
- `python tools\verify_adrmats_delivery.py`：全部通过，退出码 0。
- `python -X utf8 tools\verify_adrmats_delivery.py`：全部通过，退出码 0。
- `python -X utf8 tools/validate_consistency.py`：0 error。
- `python -X utf8 tools/check_chimera.py`：0 violation。
- README、HANDOFF、ADRMATS_DELIVERY_PLAN、AI_AGENT_PROGRESS 的当前状态没有互相矛盾。
- `examples/adrmats_briefs/` 中的 brief 样例由接口真实生成，而不是手写。
- `docs/ADRMATS_CALL_GUIDE.md` 存在且完整。
- `docs/SUPPORT_SCOPE_AND_RISKS.md` 存在且完整。
- tag `v0.1` 已创建并推送。

## Stop Conditions

如出现以下情况，必须暂停并更新 progress：

- 未提交或未 push 却准备进入下一 milestone；
- 验收脚本失败；
- schema 文档与 `BiomimeticContext.query()` 真实输出不一致；
- PFOA/SMX/BPA 被标为 direct evidence；
- 需要人工决策。
