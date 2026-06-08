# AI Supervisor Directive

> 本文件由 Codex 更新，coffee-cli 每次开始工作、完成关键动作、进入下一个 milestone 前必须读取。
> 当前目标不是“跑完 Phase”，而是交付 ADRMATS 可调用的 v0.1 仿生启发检索模块。

---

## Current Decision

- `status`: `HUMAN_REVIEW_REQUIRED`
- `current_milestone`: `Milestone 0`
- `decision_time`: `2026-06-08 16:30`
- `decision_owner`: `Codex`

## Decision Summary

Milestone 0 已出现提交 `8eb9459 docs: Milestone 0 - 交付计划与状态收敛`，并已同步到 `origin/feature/extraction-results`。当前应暂停进入 Milestone 1，等待人工/Codex 复查 Milestone 0 文档质量和状态一致性。

## Required Actions For coffee-cli

1. 不要进入 Milestone 1。
2. 更新 `docs/AI_AGENT_PROGRESS.md`，写清：
   - 当前 commit；
   - 是否已 push；
   - `validate_consistency.py` 结果；
   - `check_chimera.py` 结果；
   - Milestone 0 自认为完成的文件清单；
   - 剩余风险。
3. 等待监督指令状态变为 `CONTINUE` 后再继续。

## Evidence Expected Before Continuing

- `git status --short --branch` 显示本地与远端同步且工作区干净。
- `python -X utf8 tools/validate_consistency.py`：0 error。
- `python -X utf8 tools/check_chimera.py`：0 violation。
- README、HANDOFF、ADRMATS_DELIVERY_PLAN 的当前状态没有互相矛盾。

## Stop Conditions

如出现以下情况，必须暂停并更新 progress：

- 未提交或未 push 却准备进入下一 milestone；
- 验收脚本失败；
- schema 文档与 `BiomimeticContext.query()` 真实输出不一致；
- PFOA/SMX/BPA 被标为 direct evidence；
- 需要人工决策。
