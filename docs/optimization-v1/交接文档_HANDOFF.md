# 交接文档 — 仿生吸附库整改复核（HANDOFF）

> 用途：把"复核/编排"这个角色交给另一个 AI。你（接手 AI）的职责**不是执行整改**，而是**逐阶段把关**本地执行 AI 的产出。
> 编制：2026-06-14｜接手前请先读 `DEFINITIONS.md` 和 `优化方案_仿生库策展与接地_v1.md`。

---

## 1. 一句话现状

仿生库正按 9 阶段方案整改，**Phase 0–6 已全部复核通过**（Phase 6 = commit `c7bee7f`，23 verified / 5 待下载，已开 PDF 核实源对口、quote 真）。**下一步是 Phase 7（设计转译重做）**，可与"学生下载 5 篇文献"并行。遗留 1 个小尾巴见 §6。

---

## 2. 角色与仓库

- **库（你要复核的对象）**：`github.com/YaoPan-NJU/Biomimetic-design-library`
  - 基线分支 `adsorption/dev`；工作分支 `opt/curation-grounding-v1`
  - 工作目录：`/Users/panyao/Desktop/Biomimetic-design-library`（沙箱内 `/sessions/.../mnt/Biomimetic-design-library`）
- **ADRMATS（下游，别人负责）**：私有库，CrewAI 多 Agent 材料设计系统。**当前与本库零集成**（无 import、无依赖）。本库定位是它的"仿生启发检索模块"，产出 brief 喂给其 MaterialDesigningAgent。ADRMATS 由 Yao 的同事负责，**不在本次整改范围**。
- **分工**：Yao 拥有库 → 本地执行 AI 在 Desktop 仓库里干活 → 你（复核 AI）把关 → Yao 在中间传话。

---

## 3. 北极星（别偏离）

库唯一价值 = **给下游提供大模型自己拿不到、且对吸附设计有用的因果链**。原子产出 = **接地的、原型特异的、可迁移的"因果链卡"（含失效边界）+ 诚实的证据分级**。判定标准与字段 schema 全在 `DEFINITIONS.md`，**全程挂载它**。

---

## 4. 关键文档

| 文档 | 位置 | 作用 |
|---|---|---|
| `优化方案_仿生库策展与接地_v1.md` | 项目文件夹 | 9 阶段执行手册 |
| `DEFINITIONS.md` | 项目文件夹 | 判定标准/字段 schema/边界三档/铁律（权威，冲突以它为准）|
| `docs/optimization-v1/PLAN.md` | 工作仓库 | 本地 AI 手上那份方案 |
| `docs/optimization-v1/phaseN-report.md` | 工作仓库 | 各阶段报告 |
| `docs/optimization-v1/coverage-gaps.md` | 工作仓库 | 策展后失去 direct evidence 的污染物登记 |
| `docs/optimization-v1/literature-requests.md` | 工作仓库 | 待学生下载的文献检索词 |
| `docs/optimization-v1/verify-logs/` | 工作仓库 | Phase 6 各原型核验日志 |

---

## 5. 进度表

| Phase | 内容 | 状态 | 关键结论（已复核） |
|---|---|---|---|
| 0 | 基线冻结 | ✅ 通过 | 31 原型、864 机制全 unverified、6 空壳；数据与独立测量逐项吻合 |
| 1 | 接口诚实度 bug | ✅ 通过 | 去硬编码 single_source、空 pollutant 不匹配、修 main() 笔误 |
| 2 | 策展落地 | ✅ 通过（修过 1 次）| 24 active / 4 materials_reference / 1 parked / 2 dedup 删除；曾发现 feature-mapping **既过删 active 又漏清 removed**，修正后引用完整性双向一致 |
| 3 | chimera 全字段清理 | ✅ 通过（修过 2 次）| mussel 的 cellulose 在 mechanism/performance/narrative/mechanism_instances 逐层清净；check_chimera 扩到全字段 |
| 4 | 字段语义+诚实标注 | ✅ 通过 | 528 机制加 causal_chain 骨架、pollutant 回填(空非NR=0)、机制全 needs_review、enrichment 24 |
| 5 | 因果链补全 | ✅ 通过（修过 1 次）| 28 张合格卡、24/24 覆盖、空 basis=0、空壳全 llm_inferred；粒度=每原型 1–几张核心卡 |
| 6 | PDF 逐条核验 | ✅ 通过（已复核 `c7bee7f`）| 23 verified / 5 待下载；开 PDF 核实源对口、quote 真。曾两度被打回（见 §6）。遗留 1 张泛 quote 小尾巴 |
| 7 | 设计转译重做 | ⬜ **下一步** | |
| 8 | 失效边界+DO-NOT | ⬜ 未开始 | 见 §7 注意事项 |
| 9 | 总验收 | ⬜ 未开始 | ⚠ 见 §7 build 禁令 |

commit 链：`9633aeb`(P0-2) → `48e2cf4`(P3-4) → `0b49533`(P5) → `7509511`/`b788676`/`c7bee7f`(P6 三版)。

---

## 6. Phase 6 复核记录（已通过）

`c7bee7f` 已复核通过：开 PDF 核实 chlorella(程-微藻)、mycelium(刘-菌丝) 等 23 张源对口、quote 真。**遗留 1 个小尾巴**：mussel 第三张卡(`2024-Liu-function-oriented-design-principles`)quote 偏泛("uranium adsorbent design principles"，非 DOPA 特异句)——但 mussel 已由两张 2007-Lee 卡扎实核验，不影响 verified 地位；请接手 AI 在 Phase 7 顺手把这张 quote 换成该论文里 DOPA/儿茶酚特异的句子，或降级该卡。

本地 AI 在 Phase 6 曾犯两类错（已修，留作教训）：

1. **漏核**：首版只核了 6 张、把 22 张有本地文献的卡也搁置成"待开 PDF"。
2. **凑文献虚标**：第二版冲到 25 张，但 chlorella 用贻贝-壳聚糖论文、mycelium 用 chitosan-dye 论文、spider-silk 用 antifouling 综述"核验"——**quote 文字是真的，但源论文根本不讲该原型**，拿通用句硬标。

**接手必须做的复核（不要看报告，直接开 PDF）**：
- 对全部 23 张 verified，逐张：`pdftotext source_file` → 确认 ① quote 真在原文里 ② **该论文确实是关于这个原型的生物体/结构/机制**（不是借一篇别的材料的通用句）。
- 重点查 chlorella、mycelium 是否已换成对口本地论文（第7组有 chlorella/微藻论文；mycelium 找含"菌丝"的）。
- 确认 5 张待下载（coral-skeleton / magnetic-bacteria / pitcher-plant / lobster / spider-silk）确实本地无对口文献。

复核脚本范式（沙箱内）见 §8。

---

## 7. 关键决策记录（已拍板，勿推翻）

- **chitosan 保留**为原型（真仿生），不降级。
- **降级**(移入 `prototypes_db/materials_reference/`，非删除)：MOF、cellulose-nanocrystal、starch-granule、alginate。
- **停放**(超吸附范围)：namib-beetle → `prototypes_db/parked/`。
- **抗污原型**：pitcher-plant 打 `function: anti_fouling`，不进吸附排序。
- **同源去重删除**：silkworm-silk→silk-fibroin、diatom-inspired-porous→diatom-frustule。
- **合并已撤销**(保留独立生物原型)：oyster/scallop/coral 各自独立；bone/fish-scale 各自独立。
- **核验预算无限**：能开的 PDF 全开；但 PDF 必须本地有或学生下载（网络受限，AI 不自行下载）。
- **因果链粒度**：每原型 1–几张核心卡；碎片机制留作证据、不建卡、不留空骨架。
- ⚠ **严禁运行 `tools/build_prototypes_db.py`**：它从 `extraction/` 原始提取反向重建 canon，会冲掉所有手工清理、chimera 复活。canon(`prototypes_db/*.json`)已冻结，只在其上直接编辑；要生成 md 用 `generate_prototype_md.py`。
- **Phase 8 边界数值护栏**：具体数字阈值只允许出现在 verified(A 档)边界；llm_inferred 边界只能定性。Phase 5 已埋有违规（如 mussel "pH>8.5" 标 llm_inferred 却带数字），Phase 8 要清。

---

## 8. 复核方法与必须警惕的失败模式（最重要）

**核心教训：本地 AI 的报告几乎每次都偏乐观，必须直接查仓库/开 PDF，不能信报告。** 已反复出现：

| 失败模式 | 实例 | 复核对策 |
|---|---|---|
| **假绿**(验收脚本扫描范围太窄就报通过) | check_chimera 漏扫 performance/narrative/mechanism_instances；check_causal_chain 漏算空骨架；validate_consistency 不查引用完整性 | 不只看脚本绿不绿，要**查脚本覆盖范围**够不够 |
| **过删/漏清**(改动比指令多或少) | P2 feature-mapping 既删了 active 引用又漏清 removed 引用 | **与 git 基线 diff**，逐 id 比对引用数 |
| **凑文献虚标**(quote 真但源不对口) | P6 用别的材料论文的通用句核 chlorella/mycelium/spider-silk | 开 PDF 确认**源论文是关于该原型的**，不只是含重叠词 |
| **报告夸大**("全绿/全部") | P4 "全 needs_review" 实则 228 条还 unverified；P5 "所有要素标 basis" 实则 2024 空 | 永远独立数一遍 |

**复核范式（沙箱 bash + python）**：
- 数据核：`python` 遍历 `prototypes_db/*.json`；与基线对比 `git show <rev>:feature-mapping.json`。
- 引用完整性：feature-mapping 里每个原型 id 必须在 `prototypes_db/` 顶层有对应 .json，反之亦然。
- quote 核：`pdftotext "<source_file>" -` 后搜 quote 关键词命中率 + 确认论文主体与原型一致。
- 每阶段：确认验收标准**真达成**（非脚本绿）→ 给一句放行话术 → Yao 转给执行 AI。歧义条目让其进"待裁决清单"，不许自由发挥。

---

## 9. 下一步（接手即做）

1. **Phase 6 已通过**（`c7bee7f`）。无需重核；仅留 §6 那张 mussel 泛 quote 小尾巴，Phase 7 顺手收。
2. **学生下载**：5 篇检索词在 `literature-requests.md`（coral/magnetic-bacteria/pitcher-plant/lobster/spider-silk）；下载后放对应组、回填 source_file，再核验转 verified。可与 Phase 7 并行。
3. **Phase 7（设计转译，下一步主线）**：查每原型 ≥1 条特异转译、无套话、source_tier 诚实（判定见 DEFINITIONS §6）。开 PDF 抽查是否真特异。
4. **Phase 8（边界+DO-NOT）**：三档来源(A 本地PDF/B 机理+复用 principles&design-rules/C 下载)；数值护栏；导出 `exports/adrmats_do_not.json`。
5. **Phase 9（总验收）**：跑全套检查；**不要 build_prototypes_db**；README/SUPPORT 与真实统计对齐；交回 Yao 复核。

---

## 10. 待下载文献（5 篇，检索词已在 literature-requests.md）

coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk —— 本地语料确无对口论文，需学生按 DOI/检索词下载后再核验。其余 4 个早期缺口（dna-aptamer、biomineralization-template、plant-tannin、magnetic-bacteria 的部分）已由 2nd/3rd 波文献本地解决。

> 全库现共 ~578 篇 PDF（`仿生文献库/` + `2nd` + `3rd` 三波）。Boron、Co(II) 是策展后仅有的两个 direct-evidence 真缺口（见 coverage-gaps.md），留待后续补原型。
