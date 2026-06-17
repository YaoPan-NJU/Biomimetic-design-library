# Dispatch 启动简报 — 仿生吸附库证据审计

> 用途：给 Dispatch 窗口的 AI 接替 Codex 当**编排/验收官**。开工先读本文件 + `DEFINITIONS.md`。
> 编制：2026-06-17｜状态基准：`origin/review = ef5defe`（本地已同步）

---

## 你的角色

接替 Codex 当**编排/验收官**：选批次、给本地 OpenClaw（mimo-v2.5）写任务包、开 PDF 抽查、判定是否 decision-ready、维护决策队列、把需拍板项交 Yao。OpenClaw 干批量证据活，Yao 终审。**你不直接改库。**

## 项目

`~/Desktop/Biomimetic-design-library`，对 24 个仿生吸附原型做全量证据审计——每条性能/机制/边界都要有 PDF 级文献支撑，且**源论文必须真正是讲该原型的**（不能拿别的材料的通用句来凑）。北极星：**窄但每条可信、可溯源、诚实分级。**

## 当前状态（已同步 `origin/review = ef5defe`）

- 24 active / 4 materials_reference / 1 parked
- 因果链卡：**18 verified / 9 needs_review**
- 边界 60 条，DO-NOT 62 条**全是 soft（0 硬约束）**
- `validate_consistency` 0 error、`check_chimera` 0 violation
- **决策队列：~118 pending_yao + ~19 wrong_source 待批，26 已应用** ← 当前瓶颈在 Yao
- ⚠ 工作区残留 3 个协议禁改文件（`phase5-chains.md` / `verify_adrmats_delivery.py` / `litextract`），开工前 `git restore` 掉，勿误提交

## 硬规则

- 不改 `prototypes_db/*.json`（除非 Yao 已批对应队列项）；不跑 `tools/build_prototypes_db.py`；不擅自 commit/push
- 不升级 `verification` / `hard_do_not` / `soft_boundary`（需 Yao 批）
- 缺 PDF / 扫描专利 / OCR 不确定 / LLM 推断 → 标 `missing_pdf` / `needs_human_decision` / `knowledge_gap` / `inferred_only`
- 只有明确源错配或直接文献支持 → 才建议 `wrong_source` / `hard_do_not`
- OpenClaw 只用 `mimo-v2.5`；最多并行 3 个 worker（超了触发 429）

## 现在按顺序干

1. **先清存货（最高优先）**：把 `review-full-audit-decision-queue.md` 的 ~118+19 条按"建议批准 / 建议驳回 / 需 Yao 定"分类，做成 Yao 过一遍就能批的清单。批完才应用——OpenClaw 已攒一堆等批的，先清存货再产新的。
2. **OpenClaw 新批次**：剩余 preflight（batch 03 微生物/细胞、06 enrichment 交叉核）+ 5 个待补原型（coral / lobster / magnetic-bacteria / spider / pitcher）证据复核——多数本地缺对口文献，需下载或降级/收窄结案。
3. 队列清空后 → 重跑总验收、**重生成 `FINAL-report.md`**（现有那份是 6-15 旧版，verified 写 23，实际已降到 18）、`review` 合回 `adsorption/dev`。

## 关键文件（`docs/optimization-v1/`）

`PLAN.md`（9 阶段手册）、`DEFINITIONS.md`（判定标准/schema/铁律，权威）、`交接文档_HANDOFF.md`、`review-full-audit-decision-queue.md`（待批队列）、`review-boundary-do-not-register.md`、`review-openclaw-coordination.md` + `-worker-prompts.md` + `-next-tasks.md`（OpenClaw 派活格式）、`coverage-gaps.md`、`literature-requests.md`、`verify-logs/`；根目录 `CLAUDE.md`（编排约定）。

## 血泪教训（别信报告，直接查仓库 / 开 PDF）

1. **假绿**：check 脚本扫描范围太窄就报"通过"（check_chimera 曾漏扫 performance/narrative/mechanism_instances）。看脚本绿不绿之外，先看它扫的范围够不够。
2. **凑文献**：quote 文字真，但**源论文根本不讲该原型**——上一轮 chlorella 用贻贝-壳聚糖论文、mycelium 用 chitosan-dye 论文、spider 用 antifouling 综述都犯过。verified 的源必须真正关于该原型。
3. **报告夸大**："全绿/全部"，实际有出入（曾出现"全 needs_review"实则一堆 unverified、"所有要素标 basis"实则大片空）。独立数一遍。
4. **数值阈值**只允许出现在 verified（A 档）的边界里；llm_inferred 边界只能定性。
