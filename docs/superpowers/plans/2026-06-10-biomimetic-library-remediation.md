# Biomimetic Library Stabilization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将当前仿生设计库从“多分支、多来源、可试用但证据不稳”的状态，整理为一个可审计、可重建、可被 ADRMATS 稳定调用的知识库主线。

**Architecture:** 以 `feature/extraction-results` 作为 canon 和 ADRMATS 调用主线，以 `feature/library-enhancement` 作为待审知识资产来源。所有外部分支资产先隔离导入、标注来源和验证状态，只有通过一致性、chimera、证据层级和 ADRMATS 查询验收后，才能进入正式消费路径。

**Tech Stack:** Git/GitHub, Python scripts under `tools/`, JSON canon in `prototypes_db/`, Markdown knowledge docs in `prototypes/`, ADRMATS interface in `tools/biomimetic_context.py`.

---

## 0. 当前基线判断

### 当前推荐主线

- 主线：`feature/extraction-results`
- 稳定回滚点：`release/v1.1`
- 知识资产来源：`feature/library-enhancement`
- 归档或暂不合并：`main`, `feature/biomimetic-story-v2`, `project/tracking`, `release/v1.0`, `wastewater-treatment-universal`

### 已确认状态

- 远端 `feature/extraction-results` 最新头为 `7bceb3b12fba0a9829283c50d42d99479d5762c3`。
- 本地工作区当前仍在 `dc705bce5dc18bd13e7e7a4027ef101f3c8a52ec`，本地远端引用落后。
- 顶层主 canon 有 31 个 `prototypes_db/*.json`。
- 加上 `prototypes_db/separation/` 的 5 个停放原型，全目录共有 36 个 JSON。
- 全目录约 764 条性能数据、1325 条机制；顶层主 canon 为 752 条性能数据、789 条机制。
- `verify_adrmats_delivery.py` 目前能通过，但它证明的是接口冒烟，不证明数据质量可靠。

---

## 1. 问题清单

| ID | 严重度 | 问题 | 已观察证据 | 对 ADRMATS 的影响 |
| --- | --- | --- | --- | --- |
| P0-01 | 阻断 | 子模块疑似提交了 token | `Literature-extracting` 的 `203b0cfd` 中 `openclaw.json` 新增 `auth.token` 字段 | 安全风险，必须先处理 |
| P0-02 | 阻断 | 本地与远端分支头不一致 | 本地 `feature/extraction-results` 为 `dc705bc`，远端为 `7bceb3b` | 后续整改可能基于旧代码，造成重复劳动 |
| P0-03 | 阻断 | “三批提参完成”和“主库完整入库”没有闭环 | 子模块进度文档显示第三波输出，但主仓库最新 diff 没有大规模 canon 更新 | 无法证明第三批已经进入 ADRMATS 可消费事实层 |
| P0-04 | 阻断 | chimera 残留仍存在 | `mussel-foot-adhesion.json` 含 cellulose/nanocellulose 性能和机制；`check_chimera.py` 未捕获 | 候选解释会把错误机制交给 ADRMATS |
| P0-05 | 阻断 | `polydopamine-coating` 与沙漠甲虫/超疏水机制仍有污染风险 | `7bceb3b` diff 中 polydopamine 新增 Stenocara/desert beetle 机制；任务文档又要求 blocklist 过滤 | 同一提交既引入污染又要求过滤，说明流程未闭合 |
| P1-01 | 高 | `organism.scientific` 大面积错误 | MOF 为 `Bombyx mori`，cellulose-nanocrystal 为 `Lotus leaf`，namib-beetle 为 `Lotus leaf` 等 | 原型身份不可信，影响检索解释和文档输出 |
| P1-02 | 高 | 大量 `performance_data.pollutant` 为空 | 顶层 226/752 条为空，chitosan 53/109，cellulose 41/99，mangrove-root 5/5 | direct evidence 召回不足，且空字符串可能误匹配 |
| P1-03 | 高 | 证据层级不可信且过度集中 | 全库没有真正 `verified`；非 `unverified` 基本集中于 MOF 的 252 条 | ADRMATS 无法按证据强度做可靠门控 |
| P1-04 | 高 | ADRMATS 接口会夸大证据 | `tools/biomimetic_context.py` 硬编码 mechanism `verification_tier='single_source'`；空 pollutant 可能匹配任意查询 | 下游会把弱证据或脏数据当成强线索 |
| P1-05 | 高 | enrichment 层尚未真正分离 | `prototypes_db/enrichment/` 不存在；`--export-enrichment` 未实现 | 重建时仍可能丢失人工富化和验证状态 |
| P1-06 | 高 | 分支知识资产断裂 | `feature/library-enhancement` 有 `design-rules.json` 和 `principles/`，但 `feature/extraction-results` 没有 | 高价值规则无法被 ADRMATS 检索消费 |
| P2-01 | 中 | 空壳原型数量较多 | 顶层 8 个原型零性能、零机制，包括 `dna-aptamer`, `scallop-shell` 等 | 检索覆盖看似广，实际可用知识不足 |
| P2-02 | 中 | 机制字段混入实例级性能数据 | `validate_consistency.py` 有 254 warning，主要是 R14 | 机制解释质量差，容易生成混乱 brief |
| P2-03 | 中 | `feature_matching_rules.json` 覆盖不足 | 当前规则引用约 13/31 个原型，约 18 个原型缺失 | feature-based inference 覆盖不完整 |
| P2-04 | 中 | README 与真实状态漂移 | README 仍以第二波/v1.1 口径描述，未反映当前事故与第三波状态 | 人和 AI 都容易误判当前状态 |
| P2-05 | 中 | provenance 不够规范 | `source_file` 存在绝对路径、批次信息不稳定、无统一 manifest 入 canon | 难以回溯每条事实来自哪批、哪篇、哪次提取 |

---

## 2. 总体整改原则

1. 不直接合并整个 `feature/library-enhancement`。
2. 不直接覆盖 `prototypes_db/`, `feature-mapping.json`, `tools/`, `README.md`。
3. 任何外部分支内容先作为 `pending_validation` 资产导入。
4. ADRMATS 只能消费通过 canon 校验的数据。
5. 先修安全和数据污染，再接入高价值规则。
6. 每个阶段都要有可运行验收命令，不能只看提交信息。

---

## 3. 推荐整改路线

### Phase 0: 冻结现场和安全处理

**目标:** 确认唯一工作主线，先消除 token 风险。

**预计工作量:** 0.5 到 1 天。

**文件范围:**

- `tools/litextract` submodule pointer
- `Literature-extracting/openclaw.json`
- `docs/archive/` 或新建状态报告

**任务:**

- [ ] 创建新的整改分支，基于远端最新 `feature/extraction-results`。
- [ ] 移除 `Literature-extracting/openclaw.json` 中的 token。
- [ ] 轮换该 token，不能只从 Git 历史里删除。
- [ ] 记录当前分支头、子模块头、统计指标。

**验收标准:**

- [ ] `git ls-remote origin refs/heads/feature/extraction-results` 显示工作基线为 `7bceb3b...`。
- [ ] GitHub 上不再有新增 token 字段。
- [ ] 形成一份 baseline 统计：顶层 JSON 数、全目录 JSON 数、performance 数、mechanism 数、warning 数、chimera 数。

---

### Phase 1: 建立 canon 入库闭环

**目标:** 明确三批提参结果到底哪些进入了主库，哪些只停留在子模块。

**预计工作量:** 1 到 2 天。

**文件范围:**

- `tools/build_prototypes_db.py`
- `tools/litextract/docs/extraction-progress-tracker.md`
- `tools/litextract/outputs/extractions/manifests/`
- `docs/post-mortem-20260609.md`

**任务:**

- [ ] 从子模块导出或提交 `success.tsv`, `remaining_queue.tsv`, `progress.json`。
- [ ] 为每条入库数据保留 `batch`, `source_file`, `source_id`, `extraction_model`, `extraction_time`。
- [ ] 检查 `build_prototypes_db.py` 是否实际扫描了第二波、第三波输出，或是否已经合并到 `论文/json`, `专利/json`, `标准/json`。
- [ ] 生成入库差异报告：每批新增多少 performance、mechanism、constraints，分别进入哪些 prototype。

**验收标准:**

- [ ] 能回答“第三波 63 个 JSON 中有多少被入库，分别进了哪些原型”。
- [ ] 每条新增 fact 可以回溯到批次和源文件。
- [ ] `prototypes_db` 重建后统计可复现。

---

### Phase 2: 清理最高风险数据污染

**目标:** 先清掉会直接误导 ADRMATS 的脏数据。

**预计工作量:** 2 到 4 天。

**文件范围:**

- `prototypes_db/mussel-foot-adhesion.json`
- `prototypes_db/polydopamine-coating.json`
- `prototypes_db/spider-silk.json`
- `prototypes_db/separation/*.json`
- `tools/check_chimera.py`
- `tools/build_prototypes_db.py`

**任务:**

- [ ] 扩展 `check_chimera.py`，覆盖 mussel/cellulose、PDA/desert beetle、spider/lotus/pitcher 等已知污染对。
- [ ] 从 `mussel-foot-adhesion.json` 移除 cellulose/nanocellulose 性能和机制，或迁移到 `cellulose-nanocrystal`。
- [ ] 从 `polydopamine-coating.json` 移除 Stenocara/desert beetle 类机制，除非明确是 PDA 材料直接仿生设计文献。
- [ ] 对 `separation/` 维持 parked 状态，不参与吸附主库排序。
- [ ] 把 chimera blocklist 写入重建流程，防止重跑后污染复发。

**验收标准:**

- [ ] `python -X utf8 tools/check_chimera.py` 为 0 violation。
- [ ] 新增针对 mussel/cellulose 的检查样例。
- [ ] Pb(II) 查询不再因为 cellulose 空 pollutant 数据把 mussel 排到不合理位置。

---

### Phase 3: 修复结构字段和证据语义

**目标:** 让 direct evidence、organism、verification tier 具备最低可信度。

**预计工作量:** 3 到 5 天。

**文件范围:**

- `prototypes_db/*.json`
- `pollutant_aliases.json`
- `tools/biomimetic_context.py`
- 新增或修改后处理脚本

**任务:**

- [ ] 建立 `organism` 修正表，先修 31 个顶层原型。
- [ ] 从 `parameter`, `value`, `material`, `source_file` 中回填 `pollutant`。
- [ ] 用 `pollutant_aliases.json` 标准化 `Pb2+`, `Pb(II)`, `lead ion` 等别名。
- [ ] 修复 `_get_performance_leads`：空 pollutant 不参与匹配。
- [ ] 修复 mechanism attribution：使用条目真实 `verification`，不能硬编码 `single_source`。
- [ ] 重新定义 `verified`, `corroborated`, `single_source`, `needs_review`, `unverified` 的消费规则。

**验收标准:**

- [ ] 顶层空 pollutant 数量从 226 显著下降，目标小于 50。
- [ ] organism 明显错误项清零。
- [ ] `verify_adrmats_delivery.py` 仍通过。
- [ ] `honesty_ledger` 不把 `unverified` 或空污染物数据写成事实。

---

### Phase 4: enrichment 层分离

**目标:** 让 canon 可重建，人工富化不再被重建覆盖。

**预计工作量:** 2 到 3 天。

**文件范围:**

- `tools/build_prototypes_db.py`
- `prototypes_db/enrichment/*.json`
- `docs/fix-perf-key-and-enrichment-separation.md`

**任务:**

- [ ] 实现 `--export-enrichment`。
- [ ] 导出 `prototypes_db/enrichment/<id>.json`，只保存非默认富化字段。
- [ ] 改 `merge_with_existing`，从 enrichment 文件读富化，而不是从旧 canon JSON 读。
- [ ] 重建前后对比 `基本原理`, `active_features`, non-unverified performance 数量。

**验收标准:**

- [ ] `prototypes_db/enrichment/` 下有 31 个 JSON。
- [ ] 重建前后富化字段零丢失。
- [ ] non-unverified performance 数量与预期一致。
- [ ] `validate_consistency.py` 为 0 error。

---

### Phase 5: 导入 `library-enhancement` 高价值资产

**目标:** 最大保留有价值知识，但不让未验证内容污染主线。

**预计工作量:** 2 到 4 天。

**文件范围:**

- `design-rules.json`
- `principles/`
- `docs/adrmats-integration.md`
- `docs/design-decisions.md`
- `prototypes/*/prototype.enhancement.md`

**任务:**

- [ ] 从 `feature/library-enhancement` 导入 `design-rules.json` 和 `principles/`。
- [ ] 给导入资产统一标注 `source_branch: feature/library-enhancement` 和 `validation_status: pending_validation`。
- [ ] 不覆盖正式 `prototype.md`，先保存为 `prototype.enhancement.md` 或 `docs/imported/library-enhancement/`。
- [ ] 建立 prototype ID 对照表，记录 library-enhancement 与 extraction-results 的命名差异。

**验收标准:**

- [ ] 导入后 ADRMATS 查询结果不发生自动排序变化。
- [ ] `design-rules.json` 可被程序读取，但默认不参与决策。
- [ ] 所有导入内容都有来源和待验证状态。

---

### Phase 6: 接入 design-rules 到 ADRMATS 检索

**目标:** 让条件-机制规则真正服务工况查询，而不是只存在文档里。

**预计工作量:** 3 到 5 天。

**文件范围:**

- `tools/biomimetic_context.py`
- `design-rules.json`
- `feature-mapping.json`
- `examples/adrmats_briefs/*.json`

**任务:**

- [ ] 增加规则加载器，读取 `condition_mechanism_rules`。
- [ ] 根据 pH、salinity、temperature、ionic strength 匹配适用规则。
- [ ] 规则只作为 weight modifier 或 caution，不直接制造 direct evidence。
- [ ] 在 brief 输出中新增 `applicable_rules` 和 `rule_based_cautions`。
- [ ] 对 Pb(II)、PFOA、SMX、BPA 四个查询更新 golden examples。

**验收标准:**

- [ ] 低 pH 查询能返回 catechol/carboxyl 相关 caution。
- [ ] 高盐查询能返回竞争离子或离子强度相关规则。
- [ ] 无规则匹配时接口行为与旧版兼容。
- [ ] `verify_adrmats_delivery.py` 覆盖规则输出。

---

### Phase 7: 最终验收和交付

**目标:** 形成唯一可信工作分支和 ADRMATS 可调用版本。

**预计工作量:** 1 到 2 天。

**验收命令:**

```powershell
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_chimera.py
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\check_repo_hygiene.py
```

**验收标准:**

- [ ] 一致性 0 error。
- [ ] chimera 0 violation，且覆盖 mussel/cellulose 污染。
- [ ] ADRMATS 四个代表查询通过。
- [ ] README 状态与真实统计一致。
- [ ] 文档说明哪些数据是 direct evidence，哪些只是 inference。
- [ ] 明确标出当前版本适用范围：可用于候选启发和 brief，不直接替代实验验证。

---

## 4. 推荐执行顺序

1. Phase 0：安全和基线。
2. Phase 1：入库闭环。
3. Phase 2：chimera 清理。
4. Phase 3：pollutant、organism、evidence 语义修复。
5. Phase 4：enrichment 分层。
6. Phase 5：导入 library-enhancement 资产。
7. Phase 6：规则接入 ADRMATS。
8. Phase 7：最终验收。

不要把 Phase 5 提前到 Phase 2 之前，否则会把更多未验证叙事混进已经污染的 canon。

---

## 5. 给本地 AI 的第一批任务

优先执行以下四件事：

1. 基于远端最新 `feature/extraction-results` 建立新整改分支。
2. 处理 `Literature-extracting/openclaw.json` token 泄露风险。
3. 扩展 `check_chimera.py`，先抓住 mussel/cellulose 污染。
4. 输出 `baseline-stats-2026-06-10.md`，记录整改前所有关键统计。

第一批完成后再进入数据清洗，不要直接合并 `feature/library-enhancement`。

---

## 6. 风险控制

- 若本地 Git 不能 fetch，先用 `git ls-remote` 和 GitHub 页面确认远端头，再在干净目录重新 clone。
- 所有 JSON 大规模改动前，先保存统计快照。
- 所有自动清洗脚本必须输出 dry-run 报告，再执行写入。
- 不允许把 `pending_validation` 内容直接标为 `verified`。
- 不允许让 `design-rules` 直接制造 direct evidence。
- 不允许把 `separation/` 原型直接放回吸附主库排序，除非明确查询是油水分离或润湿控制。

