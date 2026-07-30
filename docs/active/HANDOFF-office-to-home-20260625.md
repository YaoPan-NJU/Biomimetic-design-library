---
title: 交接 — 办公室(Windows/CC) → 家里(mac mini/Codex)
date: 2026-06-25
branch: review
status: v0.2 已验收并 push → 家里继续 v1.0
head: d4e923d
prepared_by: Cowork（acting reviewer，代 Yao 复核）
---

# 交接：v0.2 验收完成 → 家里 mac mini 继续

## 1. 一句话状态

**v0.2 已达成验收：G1–G8 全绿，证据更诚实（149 处降级、0 膨胀，已由 Cowork 独立核验）。** 办公室 CC 在 auto/goal 模式下跑完，本次改动验证无误，授权 push 到 `origin/review`。家里 mac mini `git pull` 后即可在干净状态上继续 v1.0。

## 2. 本会话落地了什么

- **证据诚实化**：151 处问题修复 → boundary guardrail 152→0。其中 **108 个伪 from_source 降级为 llm_inferred**（无 quote 或 quote 仅关键词凑数、撑不起 claim）、41 个非法 basis→llm_inferred、1 个 inferred hard DO-NOT→soft。
- **ADRMATS 适配器有用性**：query↔机制绑定（新 validator `check_brief_mechanism_binding.py`）、DO-NOT 硬门、候选级 boundary/honesty surface、有机域 gating。
- **PFOA 诚实切片**：3/3 inference/exploratory，弱域不过度承诺。
- **Phase E（20 种新污染物）**：21 个 pollutant_profile + aliases 入库、21 个有机查询进 gold-set（全部 exploratory）、证据获取 backlog 产出。
- **silk-fibroin↔亚甲基蓝** 真绑定（DOI 10.1039/d1va00047k，带 quote+locator）。
- **2 个 validator 脚本崩溃 bug 修复**；DT 缺失/格式修复 8 原型。
- **dogfood**：有机域 3.0→6.0/10，重金属 6.6–6.8/10。

## 3. Cowork 独立复核结论（不是只听 CC 报）

- **反膨胀 ✅**：from_source 3148→3040（按全部 basis 节点计），**0 个元素升进 from_source、0 个 literature_backed→from_source、basis 节点总数 5785=5785（只 relabel、未删数据）**。账目闭合：llm_inferred +144 = 108 from_source + 36 literature。
- **验证器 ✅**：Cowork 重跑 11 个 validator 全 exit 0（G1 10/10、G2 7/7、gold-set 7/7、from_source_integrity、fact_requires_locator、DO-NOT behavior 等）。
- **降级抽查 ✅**：方向全部保守（往下降、可逆）；抽样既有真无 quote、也有"quote 仅关键词凑数撑不起 claim"（如 cell-membrane 用 RO 膜脱盐泛泛句凑 from_source）——降级正确。
- **silk-fibroin/MB ✅**：真来源 + 真 quote+locator。

> 注意口径：from_source 头条数会从 59.6% 降到 **~54%**，这是**变诚实、非退步**——之前混入了伪 from_source。v0.2 验收看诚实+gold-set 结果门，不看百分比。

## 4. 关于 push：提交了什么、刻意排除了什么

办公室 Windows 工作树有 **大面积行尾(CRLF)/权限位(mode)漂移**——`git diff` 显示整文件重写、`docs/archive` 显示 100644→100755 模式翻转，**但都不是语义改动**（内容已按解析后的 JSON 核过）。因此本次 push 用**白名单 + 守卫**，只提交真实交付物：

**提交（allowlist）**：`prototypes_db/`、`pollutant_profiles.json`、`pollutant_aliases.json`、`feature_matching_rules.json`、CC 改过的 `tools/*.py`（含新 `check_brief_mechanism_binding.py`）、`examples/adrmats_briefs/`、`docs/active/` 下的 v0.2 交付文件（gold-set、emerging-pollutants-20.*、acceptance/、本计划、dogfood scorecard、本交接、execution-state.json）。

**刻意排除**：
- 受保护/本地：`.claude/settings.local.json`、`.gitmodules`、`.gitignore`、`tools/litextract`（submodule 指针，勿动）。
- 纯漂移噪声：`docs/archive/`（模式翻转）、`docs/imported/`、`docs/registries/`、`prototypes/**/*.md`（CRLF 整文件重写，非语义）。
- 运行时/排除目录：`runtime/`、`docs/optimization-v1/`。

> 遗留清理项（v1.0）：加一个 `.gitattributes`（统一 LF）消除 Windows↔macOS 的行尾漂移，否则两边 git 会反复把整库标成 modified。

## 5. stash@{0} 必须保留（DQ-6 未决）

Phase 0 用 `git stash push -u` 暂存了办公室的脏文件；**已保留，未 pop、未 drop**。内容 = 上一会话的 prototype_db scope caveats/metadata 改动 + 原始脏文件（`.claude/settings.local.json`、`README.md` 等）。逐 hunk 处置见 `docs/active/acceptance/dq6-stash-review-20260625.md`。**家里决定是否选择性应用，别整体 pop。**

## 6. 家里 mac mini 下一步

1. `git fetch origin && git checkout review && git pull --ff-only`（路径：`/Users/panyao/Desktop/Biomimetic-design-library`）。
2. 读 `docs/active/acceptance/v0.2-acceptance-20260625.md`（验收）+ 本交接 + `v0.2-change-digest-20260625.md`。
3. 处理 stash@{0}（见 §5）。
4. 若进 v1.0：从 `docs/active/acceptance/emerging-pollutant-evidence-backlog-20260625.md` 起步——**联网取文献**给 21 种新污染物补 source-backed 证据（这是 v1.0 的活，本会话刻意未做）。

## 7. 已知遗留/待办

- 21 种新污染物的证据获取 backlog（需联网，v1.0）。
- `.gitattributes` 行尾统一（消除跨平台漂移）。
- change-digest 里"108 个无 quote"措辞偏窄，实际含"quote 凑数撑不起 claim"——仅文字精度问题，动作已正确。
- mechanism binding 的 15 个空字段 warning（数据完整性，非阻断）。
- push 后请把 origin/review 新 HEAD sha 回填到本文件 §1。

## 8. 关键文件

- 验收：`docs/active/acceptance/v0.2-acceptance-20260625.md`
- 变更摘要：`docs/active/acceptance/v0.2-change-digest-20260625.md`
- 决策队列（已清零）：`docs/active/acceptance/v0.2-decision-queue-20260625.md`
- PFOA 切片：`docs/active/acceptance/pfoa-honest-slice-20260625.md`
- 新污染物 backlog：`docs/active/acceptance/emerging-pollutant-evidence-backlog-20260625.md`
- stash 评审：`docs/active/acceptance/dq6-stash-review-20260625.md`
- 执行计划：`docs/active/v0.2-acceptance-plan-officecc-20260625.md`
- 两批指令：`docs/active/acceptance/v0.2-directive-batch1/2-20260625.md`
