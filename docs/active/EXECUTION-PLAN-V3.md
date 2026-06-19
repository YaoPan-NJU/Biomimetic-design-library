---
title: Execution Plan V3 — Correction, Increment, and Review (product-aligned)
status: proposed_for_yao_review
date: 2026-06-19
author: codex-replacement-supervisor (independent reviewer), at Yao's request
relationship:
  - R0 (Gate G0) and R1 (Gate G1) under RECOVERY-EXECUTION-V2-DESIGN.md were attempted but NOT PASSED; this plan does not redo them but requires them to be fixed first.
  - This plan SUPERSEDES the forward-looking M5+/expansion sections of RECOVERY-EXECUTION-V2-DESIGN.md.
  - It KEEPS unchanged: evidence-quality-standard.md, refuted-log.md discipline, identity rules, protected-asset rules, the gate model.
authority: Yao's explicit instruction > committed canon + live validation > this plan > V2 design > archived reports
---

# Execution Plan V3

> 写给 Claude Code 对照执行。每个 Phase 给出：目标 / 输入 / 允许改与禁止改 / 方法 / 交付物 / 验证 / 停止条件 / Gate。
> 本计划的核心改动：**按"对 ADRMATS 产品价值"的高低重排修正顺序**，把扩库与 review 一并纳入同一条门控流水线。

---

## 0. 怎么用这份文件

1. 每次启动先复算实测状态（HEAD / ahead / 校验），**不要相信任何报告里的旧数字**。
2. 只在到达 Gate 时停下接受独立审阅；Gate 之间连续自主推进，不为常规批准停顿。
3. 每一次 canon 字段改动 = 一条 `canon-recovery-ledger.jsonl`(v2) 处置，缺则不改。
4. 所有 Python 用 `python3 -X utf8`；不 `git add -A`；按 concern 小提交；不 push。
5. 受保护资产永不 stage/改写：`prototypes_db/**`（除已批准处置）、`tools/litextract/**`（含 .env）、`docs/optimization-v1/_w*_doi_map.json`。

---

## 1. 产品北极星（这决定一切优先级）

这个库是 **ADRMATS 的仿生"匹配 + 证据检索"模块**，不是材料设计器，也不是按性能数值排名的引擎。
依据：`feature-mapping.json` 自述"**库只做匹配响应，不负责推理**"；实测 `examples/adrmats_briefs/brief_BPA.json` 显示候选排序权重 `weight` 来自 `molecular_feature_inference`、`direct_evidence:false`，性能值放在 `performance_leads`（标 `needs_review`）里，信任面是 `honesty_ledger`(facts/leads/inferences) 与 `verification_tier`。

**因此产品价值的真正排序是：**
scope/来源正确 ＞ 标签诚实 ＞ honesty_ledger 正确 ＞ design_translation 可用 ＞＞ 把 qmax 核到"排名级"。

> **接口契约已锁定（Yao, 2026-06-19）= "启发候选"。** 库返回启发候选 + 诚实证据，ADRMATS
> 据此发散选型，**不按性能数值排名**。因此**所有性能值一律作"诚实标注的线索(lead)"呈现，
> 默认不做排名级 qmax 一手核验**；仅当某个值确实要在 brief 中作为"事实(fact)"暴露时，才按需
> 做一手核验。这把 P1e 大幅收窄，重心落在 scope/标签/ledger/design_translation。

**成功 = 诚实且有用**：一个全降级成 needs_review、brief 仍串味的库，是失败的。

---

## 2. 当前实测状态（2026-06-19）

| 项 | 值 |
|---|---|
| HEAD / 分支 | `8578ff3` / `review` |
| 领先 origin/review(`e4dc2d0`) | 25，behind 0，**未 push** |
| R0 / G0 | **已尝试，G0 未通过**（真多模态验收失败，修复前不作执行权威） |
| R1 / G1 | **已尝试，G1 未通过**（R1-D 腐化已修复至 8 条降级；其余部分待独立验证） |
| 根 canon | 36 原型；performance 418（verified-label 163 / partial 221 / 其余 34）；mechanisms 771（verified 13 / partial 22 / 其余 736） |
| 关键提醒 | "verified" 是**存储标签、非重验证据**：163 条 verified perf 中约 69 条无 quote，属过评（CODEX-CONTEXT §7） |

---

## 3. Gate G1 签核（先做，是进入下面所有阶段的前提）

由独立审阅者复核（不改仓库）。清单：
- R1-A：默认构建确为**仅写暂存**，"默认构建后 canon 树哈希不变"测试为真；invariant guard 真的拦截行/quote/locator/causal/translation/boundary 丢失。
- R1-B：真实 applier 对**零匹配和多匹配都拒绝**；无 "first strongest wins"。
- R1-C：ledger v2 schema 生效；**628 条 warning** 逐类归因（应为 v1 迁移缺口，不得当作已验收）；R1 起每个 canon 改动有处置。
- R1-D：`diatom-frustule.json` 必须做**语义级核对**——确认只有 8 条 M2-d `partial→needs_review` 状态变更 + JSON 重序列化，**没有**夹带内容/行数变化（按字段计数与行身份比对，不看行数）。
- R1-E：`validate_consistency.py --strict` 结果与那 **1 个预存 error**（separation render/orphan）归因；`execution-state.json` 存在且与提交对象一致；`execution-entry.md`/`SESSION-HANDOFF.md`/M4 报告**不再声称 M4 通过**。

**通过条件**：以上全部可复现，且 canon 只动了 R1-D。否则停在 G1，列必修项。

---

## 4. ADRMATS 可见字段清单（"必须 scope 干净 + 诚实标注"的范围）

修正工作**只对这些字段背负最高质量标准**（按 brief 结构）：

| brief 字段 | 质量要求 |
|---|---|
| `candidates[].match`（reason / weight / applicability_fit / match_basis / direct_evidence） | 匹配理由与原型 scope 一致；`direct_evidence` 真实反映是否有直接证据 |
| `candidates[].mechanism`（基本原理 / attribution） | 机理属于该原型；`attribution.source` 与 `verification_tier` **不得矛盾**（如 `llm_inference` 不可标 `verified`） |
| `candidates[].design_translation.idea` | **一等对象**：bio→材料映射正确、属于该原型、无跨域串味（禁止单宁/PDA 里出现含氟超疏水膜文本）、有来源 tier |
| `evidence_context.performance_leads[]` | 归属该原型；非该原型的一律移出或重指派；统一 `metric_type`；以"线索"呈现，标签真实 |
| `rule_based_cautions`（do_not / cautions） | `hard_do_not` 需直接来源+locator；其余 soft，`basis`/`verification` 真实 |
| `honesty_ledger`（facts/leads/inferences） | 三类划分准确，是产品的信任总账 |

内部/非可见字段（如未进 brief 的冗余镜像）不背负同等标准，登记即可。

---

## 5. 执行路线（Phase 与 Gate）

### Phase P0 — 接口契约锁定（**Yao 已定 2026-06-19 = 启发候选**）
- **结论（已锁定）**：ADRMATS 消费**启发候选**——库返回候选 + 诚实证据，ADRMATS 据此发散选型，**不按性能数值排名**。`match.weight` = feature-match 分（非性能）。字段定级：`verified` = 一份直接来源+quote+locator+scope match；`corroborated` = ≥2 独立源（双源是 Core 的 tier 门，不是 row-grade）；**所有 `performance_leads` = 线索**；`honesty_ledger` 为信任总账。
- **剩余动作**：CC 把上述写成 `docs/active/adrmats-interface-contract.md`（status proposed，记录 Yao 决策），作为 P1/§9 的依据。无需再等 Gate。
- **输入**：`docs/ADRMATS_CALL_GUIDE.md`、`ADRMATS_INTEGRATION.md`、`tools/biomimetic_context.py`、本计划 §1/§4。
- **Gate**：**G-contract = 已关闭（Yao 决策已记录）。**

### Phase P1 — 修正（重排顺序；替代旧 M5"证据接受"）
按产品价值从高到低，每个子阶段都是 pilot(3–10 项)→子 Gate→分批。canon 改动全部经 ledger v2 + 已批准 decision-queue。

| 子阶段 | 目标 | 主要执行 | 子 Gate |
|---|---|---|---|
| **P1a scope/wrong-source 清理** | 让 Core（及会进 brief 的 Extended）的 match/mechanism/design_translation/performance_leads/cautions **零串味**；移除/重指派 wrong-source；不复活 refuted-log 行 | 多为已 Yao 批准的 decision-queue 项；CC 直接做（文本判断） | G2 |
| **P1b 标签诚实** | 修 `source`↔`verification_tier` 矛盾；按 evidence-quality-standard 重算 grade（标签从证据重算，不照抄） | CC 直接做 | G2（与 P1a 合并审） |
| **P1c honesty_ledger 正确化** | facts/leads/inferences 三类划分与字段真实状态一致 | CC 直接做 | G2 |
| **P1d design_translation 一等化** | 每个 Core 原型的 design_translation.idea：scope 正确、来源归因、对工程可用；补 `material_realization_examples` 或诚实留空 | CC 主审；视觉/专利来源交 OpenClaw 取证 | G3 |
| **P1e 量化证据（已大幅收窄）** | 契约=启发候选 → 性能值**默认全作诚实 leads**（统一 `metric_type` + 真实 tier）；**默认不做排名级 qmax 一手核验**；仅当某值要作"事实"暴露时按需一手核验；缺源→`external-input-gaps.jsonl`，排除 | 视觉/扫描交 **OpenClaw(mimo-v2.5)**；按需文本核验 CC 分批 | G3 |

- **禁止**：任何无处置的 grade 升级；whole-file 替换；对 canon 跑破坏性 build；复活 refuted 行。
- **验证（每批后）**：JSON 解析；ledger 完整/歧义；count guard；`validate_consistency.py --strict`；`check_chimera --strict`；causal/boundary；**brief 级抽检**（生成代表性 brief，确认零 wrong-source、ledger 诚实）。
- **Gate G2 / G3（独立审阅）**：100% 复核高风险项（hard_do_not、跨原型归属、状态升级、视觉声明、进入"事实"的数值）；其余风险抽样。

### Phase P2 — ADRMATS Core v1 验收
- **目标**：Core 24 对 ADRMATS 既**诚实**又**有用**。
- **硬门（整合 §9 有用性门槛）**：
  - `validate_consistency.py --strict` = 0 error；`check_chimera --strict` = 0；
  - 每个 ADRMATS 可见 Core 推荐都有合格 causal card + 至少 1 条 scope 正确的已验证机理 + 正确的 design_translation；
  - boundary guard 绿；hard 规则均有直接来源；
  - 代表性 brief（≥本仓 examples 覆盖的污染物）**零 wrong-source、honesty_ledger 准确**；
  - 排名/事实值仅用已接受、metric 兼容的数据；未决/缺源行排除；
  - 文档与 execution-state 与提交对象一致。
- **Gate G4（Codex/独立 + Yao）**：v1 候选发布。

### Phase P3 — 分层增量扩库（INCREMENT）
- **前提**：P2 通过后才开始；全量审计可并行（走候选 artifact，不动已发布 Core）。
- **目标构成**：Core 24（默认推荐/feature-match 候选排序）＋ Extended 24–36（启发，逐行排序门）＋ Exploratory 12–24（仅发现，禁确定性性能），总 60–80。**count 不是质量指标**。**性能值永不参与排序**——排序仅基于 feature-match weight（分子结构/机制相似度）。
- **执行**：OpenClaw 做文献清点 + 候选证据包 + 候选卡；CC 强制 tier/晋级门；按波次提交。
- **晋级门**：Exploratory→Extended（≥1 直接来源 + 1 源链接机理 + 适用边界 + 归属去重）；Extended→Core（全 PDF 审计 + 合格 causal card + ≥1 证据级 boundary + 每个排序值一手来源 + Yao 批准）。
- **Gate G5（每波，Codex + Yao 管归属/tier）**；去重/合并/删除原型 = **仅 Yao**。

### Phase P4 — 全量审计收尾 + 发布
- 每条残余行有最终处置：接受 / 软背景 / 知识缺口(parked) / 移除(refuted-log)。
- 外部 office 资产未到前，相关行留 `external_source_pending`，排除出 ADRMATS 可见输出。
- **Gate G6（仅 Yao）**：push 到 `origin/review`。

---

## 6. 工作分配（OpenClaw / Claude Code 混合，基于第一性原理）

- **OpenClaw 做全部来源/PDF/OCR 阅读**：扫描件/专利 OCR、图表/曲线/表格/标题读取（`mimo-v2.5`，只走 process/exec→MIMO，**禁用内置 image 工具**，它路由到 Gemini）；纯文本批量抄录/抽取（`mimo-v2.5-pro`）；文献清点；候选证据包。**永不写 canon/mapping/ledger，不接受 grade，不 commit/push。**
- **Claude Code 只看 JSON/brief/scope/标签并负责最终 disposition**：scope/wrong-source 判定、标签诚实、honesty_ledger、design_translation 质量——CC **不亲自批量读源**（即使 API 配额无限），来源/PDF/OCR 全部由 OpenClaw 处理。
- 并发 ≤ 3；一个 artifact 一个 writer；每 worker 独立 task/workspace；reject `fallbackUsed=true` 或 provider/model 不符。

> 理由：本库约 36 原型 / ~1200 行，规模不大。视觉/扫描必须用 mimo-v2.5；但把"证据判断"整体外包给能力更弱的模型、再要 CC 100% 复核，并不省事且重蹈"盖章式接受"覆辙。故纯文本判断回归 CC，OpenClaw 专注取证。

---

## 7. 长期规约（standing rules，全程适用）

- **身份匹配**（见 CLAUDE-CODE-TAKEOVER / V2 §6.2）：performance = 原型+DOI/专利/标准+规范化参数+值+材料；mechanism = 原型+DOI+规范化名+描述指纹。**数组下标永不作身份**；零/多匹配 = 停下登记。
- **证据标准**：以 `evidence-quality-standard.md` 的五问与分级为准；关键词/DOI/标题/摘要/LLM 句子**不能单独**升到 partial/verified；metric 类型不可混比。
- **不可复活** `refuted-log.md` 任何行。
- **空不覆盖非空**；不 whole-file 替换；不对 canon 跑破坏性 build。
- **诚实计数**：所有统计从已提交 JSON 重算，不抄旧报告；diff 按字段计数/行身份看，不看行数。
- **双对象校验**：序列化工作树 + 提交对象都要过校验。
- **受保护资产**：同 §0.5。**不 push**，除非 Yao 在 G6 明确批准。

---

## 8. Review Gates（更新版）

| Gate | 触发 | 审阅者 | 决定 |
|---|---|---|---|
| G1 | R1 完成 | 独立审阅 | 机器/账本/纠正是否安全（**当前在此**） |
| G-contract | 接口契约 | **Yao** | **已定 2026-06-19 = 启发候选**（性能值=线索，默认不做排名级核验） |
| G2 | P1a/b/c 试点+首批 | 独立审阅 | scope/标签/ledger 修正质量 |
| G3 | P1d/e 试点+首批 | 独立审阅 | design_translation 与量化证据质量、模型路由 |
| G4 | Core v1 runbook 全绿 + 有用性门槛 | 独立 + Yao | v1 发布候选 |
| G5 | 每个扩库波次 | 独立 + Yao（归属/tier） | 晋级/park/拒绝 |
| G6 | 任何 push | **Yao** | 发布批准 |

Gate 之间 CC 连续自主推进，不就常规批量调度/缺源登记/报告/校验复跑征求批准。

---

## 9. 有用性验收指标（新增，与诚实并列）

v1 不仅要"诚实"，还要过：
1. **零串味**：代表性 brief 的 match/mechanism/design_translation/performance_leads 中**无 wrong-source / 跨域内容**。
2. **最低密度**：每个 Core 原型 ≥ 1 条 scope 正确的已验证机理 + 1 条正确 design_translation + 诚实的 performance leads（有则标注、无则诚实留空）。
3. **标签自洽**：全库无 `source=llm_inference` 却 `verification=verified` 一类矛盾。
4. **honesty_ledger 命中率**：brief 的 facts/leads/inferences 与字段真实状态一致（抽检可复现）。

---

## 10. 停止 / 升级条件

稳定身份零/多匹配；源与 claim 冲突；会复活 refuted；保护指标无处置下降；需 Yao 决定的归属/tier/去重/删除/外部来源；worker 用错模型/模态；校验恶化或同一失败重复 3 次；需 push/force-push/历史改写/分支级合并/破坏性清理 —— 任一发生即停下升级。例行缺源不停，登记并排除。

---

## 11. 相对 V2 的改动（给 CC/Codex 的 delta）

1. **新增 P0 接口契约锁定**为前置，且把它设为成本总开关（G-contract）。
2. **修正(M5) 重排**：scope/标签/honesty_ledger/design_translation 优先于穷尽式 qmax 核验。
3. **design_translation 升为一等被审对象**（V2 仅过格式关）。
4. **新增有用性验收门槛**（§9），与诚实并列。
5. **工作分配调整**：纯文本证据判断回归 CC 分批直做，OpenClaw 专注视觉/扫描/取证（V2 是"OpenClaw-first 全包"）。
6. 扩库与全量审计纳入同一门控流水线（P3/P4）；count 明确为非质量指标。
7. R0/R1 视为已完成，不重做。
