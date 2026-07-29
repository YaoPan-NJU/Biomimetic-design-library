# 生物原型知识库 / Biological Prototype Knowledge Base

水处理仿生吸附材料开发智能体系统（ADRMATS）的仿生启发检索模块。

---

## 当前状态（2026-07-29 · massive 分支）

> 分支：`massive`｜主题：**机制层匹配激活（Track 2A）+ 源项目原型抽取扩库（Track 2B）+ 检索排序修复**

| 指标 | 值 |
|------|-----|
| root prototypes | **94**（v0.2 的 36 → V1 扩展 89 → Track2B +5 = 94）|
| 完整原型（active + source-backed 机制 + honesty_ledger + design_translation + mechanism_tags）| ~72 |
| 机制总数 | ~623（每条含 causal_chain）|
| from_source 接地率 | ~65%（causal 元素）|
| mechanism_tags 覆盖 | 94/94 |
| validator | validate_consistency 0 error · from_source 0 non-compliant · causal_chain 全合格 |
| ADRMATS 导出 | `adrmats_export/` 586 行 / 44 污染物 |

**Track 2A — 机制层匹配激活**：匹配重心从“污染物查表”升级为“原型-机制”映射。每个原型声明 `mechanism_tags`（12 类 canonical 机制）；`query()` 新增 `find_mechanism_based`（污染物特征/相互作用 → canonical 机制 → 原型），原型无需挂载特定污染物即可被机制命中。`pollutant_prototype_map` 命中降级为“仅当有真实 performance_data 才算 direct_evidence”。

**Track 2B — 源项目原型抽取扩库**：从姊妹项目 `biomimetic-adsorbent-design`（Ultimate/main/Qwen/kimi-k3 四分支）逐设计只看原型、不论方案成败地抽取库中缺失的生物原型/机制，+5：β-环糊精主客体包合、SERT 芳香胺识别、成熟污水生物膜大环内酯类别富集、DHPS 磺胺识别、ArsR 砷三硫醇捕获。知识隔离红线：`performance_data` 一律留空，机制经联网核验的原始文献独立接地。

**检索排序修复（2026-07-29）**：`find_direct_evidence` 改为按 (direct_evidence, weight) 降序返回；brief 候选上限 10→15；有机诚实域（PFOA/SMX/BPA）无真实 performance_data 的 ppm 命中不再冒充 `direct_pollutant_evidence`（降级为 `mechanism_feature_bridge`）。修复后新原型可按权重浮现（SMX→DHPS rank 1、As(III)→ArsR、PFOA/BPA→β-环糊精）。

**已知遗留**：`pollutant_prototype_map` 中约 47/69 个键为 bare-list 形态，`find_direct_evidence` 主要靠 `mechanism_summary` 内容匹配扫描，bare-list 条目不被键路由扫描（本轮已将 As(III) 转 dict-form 修复 ArsR 可见性，其余待统一治理）；`verify_adrmats_delivery` 整体仍 FAIL，仅因预存项（PFOA/BPA 有机域 plant-lignocellulosic/fabp4 真实容量数据与“有机域无直接证据”口径冲突；check_chimera 10 个多物种 organism）。

---

## 当前方向（2026-06-21, v0.2 共识）

本库是 ADRMATS 的**仿生候选匹配 + 证据检索 + 设计启发**模块，不是材料设计器，也不是按性能值排序的评价器。权威执行计划仍以 `docs/active/EXECUTION-PLAN-V3.md` 为基础，但 v0.2 前的完成定义已更新：

> **v0.2 不是“字段齐 + validator 绿 + causal_chain 填满”。v0.2 的门槛是：brief 能让材料工程决策更好，且不会被 scope 错配、伪事实、软边界冒充 DO-NOT 所误导。**

当前共识：

- `v0.2`：现有 **36 个 root prototypes** 做到 scope-correct、证据诚实、可审计、ADRMATS 可消费的终局状态。
- `v1.0`：在 v0.2 稳固后，再按真实证据缺口扩展到 60–80 个原型。
- 重金属吸附是当前最强、最接近 terminal verified 的子域。
- 有机微污染物（BPA/PFOA/SMX/染料）和油水分离目前不能与重金属同等置信度展示；若缺少 source-backed 机制，只能作为 exploratory / inspiration，不得冒充事实候选。
- feature/token 命中不能直接进入 evidence-backed candidate lane；必须与 query、selected mechanism、design_translation、boundary 语义闭合。
- hard DO-NOT 只允许来自 source-backed 边界：`basis=from_source` + `verification=verified/corroborated` + source/quote/locator/scope match。LLM 推断、domain knowledge、needs_review 只能作为 soft caution。

近期路线：M8 semantic correctness + gold-set usefulness gate → M9 ADRMATS payload finalization → M10 full QA → M11 v0.2 release packaging。

原则：诚实优先、scope 正确、不复活 refuted、不用结构绿灯替代结果级有用性、不把 LLM inference 伪装成 PDF/source verified fact。

---

## 定位

本库的职责**不是设计材料**，而是把前一个智能体给出的需求，转成"可交给对抗设计模块使用的仿生设计 brief"。

**它可以提供的设计辅助**：
- 某类水质和去除需求下，可以借鉴哪些生物原型
- 这些原型靠什么机制、结构或特征解决类似问题
- 这些机制可转译成什么材料设计思路

**工作方式**：
```
结构化输入约束 JSON → 仿生匹配 Agent → 结构化 BiomimeticDesignBrief JSON + 一段可读设计思路
```

---

## 当前状态（2026-06-25 · review 分支 V1-A Evidence Uplift 完成）

> 分支：`review`｜HEAD: `cb8e09c`｜当前工作主题：**V1-A Evidence Uplift 完成 (59.6%) + ADRMATS 4/4 完成**

### Evidence Uplift 最终状态（2026-06-25 15:26 CST）

| 指标 | 值 |
|------|-----|
| from_source | **1239/2080 (59.6%)** — 0 non-compliant, 0 vague locators |
| mechanisms 4/4 done | 62 |
| mechanisms partial (1-3/4) | 236 |
| mechanisms 0/4 | 222 |
| with source_doi | 113 mechanisms |
| basis distribution | from_source 1239 · llm_inferred 716 · literature_backed 125 |
| validator | 0 errors, 172 warnings |
| adapter tests | 5/5 pass |

### Evidence Uplift 旅程（Round 9-35）

| Round | from_source | 增量 | 策略 |
|-------|-------------|------|------|
| R9 | 313 | 基线 | — |
| R10 | 331 | +18 | 双语 scope_match 构建 |
| R12 | 390 | +59 | 反向 PDF 匹配 + DOI 提取 |
| R13 | 493 | +103 | 反向 PDF 关键词搜索 |
| R14 | 554 | +61 | 激进匹配（宽松阈值） |
| R15 | 598 | +44 | 同 DOI 跨机制 + 宽松匹配 |
| R16 | 622 | +24 | Bugfix + 文献扫描 |
| R18 | 689 | +67 | scope_match 修复（单关键词） |
| R19 | 840 | +151 | quote-based 关键词提取 |
| R20 | 961 | +121 | literature_backed 提升 |
| R21 | 977 | +16 | 自动提取脚本 |
| R22 | 1038 | +61 | 自动提取脚本 v2 |
| R26 | 1049 | +11 | 跨元素提升 (Track A) |
| R27 | 1055 | +6 | literature_backed→from_source (Track B) |
| R30 | 971 | -84 | 质量扫描（清理劣质 scope_match）|
| R31 | 1032 | +61 | 关键词扩展匹配 |
| R32 | 1052 | +20 | literature_backed 升级 |
| R33 | 1229 | +177 | 跨原型 PDF 匹配 |
| R34 | 1235 | +6 | 激进跨原型匹配 |
| R35 | 1239 | +4 | 最终冲刺

### ADRMATS 适配器（4/4 能力）

| 能力 | 状态 | 验证 |
|------|------|------|
| do_not_list | ✅ 暴露 | test_do_not_list PASSED |
| design_translation | ✅ 暴露 | test_design_translation PASSED |
| charge_state/pKa | ✅ 暴露 | test_charge_state PASSED |
| relevance_gating | ✅ 暴露 | test_relevance_gating PASSED |

### ADRMATS 垂直切片验证（2026-06-24）

| 污染物 | candidates | direct_evidence | honesty | design_translation |
|--------|------------|-----------------|---------|-------------------|
| Pb(II) | 8 | 5/8 (62%) | 1 fact, 5 lead, 1 inference | 结构化、可执行 |
| PFOA | 3 | 0/3 | 1 lead, 2 inference | 结构化（有机微污染物证据弱）|

### 剩余工作

| 类别 | 元素数 | 状态 |
|------|--------|------|
| llm_inferred 无 DOI | 885 | 需 DOI 发现（后台子代理） |
| literature_backed 无 source | 43 | 需 DOI 发现 |

已完成的真实进展：

- canon 去污染、refuted 清理、chimera guard、honesty ledger、boundary 框架、ADRMATS brief 生成链路已显著改善。
- P5-B/M6/M7 已暴露并部分修复 ADRMATS 使用层问题：brief honesty/boundary 可见性、部分 design_translation、oil-water 匹配缺口、usefulness regression。
- M8 的 510/510 causal_chain 是可用底材，但不能作为 v0.2 验收依据；需要继续做语义一致性、source-backed hard DO-NOT、gold-set usefulness gate。

当前主要 blocker：

1. **query 与 selected mechanism 尚未可靠绑定**：不能出现“候选因 A 特征命中，却展示 B 机制”的 brief。
2. **DO-NOT 还不是 hard gate**：source-backed hard DO-NOT 必须影响 candidate 可用性，而不仅是文本提示。
3. **validator 过浅**：字段存在检查不能证明 scope 正确、fact 真实或 design_translation 可执行。
4. **弱域不能过度承诺**：有机微污染物和油水分离若缺少 source-backed 证据，应进入 exploratory/inspiration lane。
5. **v0.2 需要 gold-set result gate**：用 8–12 个代表性查询度量 scope-correct precision、误导性 false positive、fact locator 完整性、hard DO-NOT 行为。

v0.2 前不建议扩库到 60–80；扩库应由 gold-set 和证据缺口驱动，而不是按数量目标堆原型。

---

## ADRMATS 集成状态（给协作同事）

- 本库定位：ADRMATS 的**仿生启发检索模块**，产出 `BiomimeticDesignBrief`，喂给其 `MaterialDesigningAgent` 作设计灵感。
- **当前与 ADRMATS 零代码集成**：ADRMATS 仓库里没有 import 本库、`requirements.txt` 无依赖、设计 Proposer 仅凭 LLM 知识生成。集成需在 ADRMATS 侧动手。
- 接口侧：`tools/biomimetic_context.py` 的 `query()` 可用，已修诚实度（不再硬编码证据等级、空污染物不乱配）。
- 建议集成形态（二选一，详见 `docs/adrmats-integration-analysis.md`）：A 案 在 ADRMATS 的对抗设计流里调 `query()` 把 brief 注入 Proposer prompt（改动小，推荐）；B 案 仿 `crewai_*_tool.py` 封成 CrewAI 工具挂给设计 Agent。
- 输入对接：ADRMATS 约束 Agent 的输出（污染物 + 水质 + 约束）正好映射到 `query(pollutant, water_quality, engineering_constraints)`；污染物名归一用 `pollutant_aliases.json`。

---

## 整改相关文档

| 文档 | 用途 |
|------|------|
| `docs/references/optimization-plan-v1.md`（即 `优化方案_仿生库策展与接地_v1.md`）| 9 阶段执行手册 |
| `docs/references/definitions.md` | 判定标准 / 字段 schema / 边界护栏 / 铁律（权威）|
| `docs/archive/optimization-v1-2026-06/old-handoffs/交接文档_HANDOFF.md` | 复核角色交接（含当前进度与失败模式教训）|
| `docs/archive/optimization-v1-2026-06/phase-reports/coverage-gaps.md` | 策展后失去 direct evidence 的污染物（Boron / Co(II) 为真缺口）|
| `docs/adrmats-integration-analysis.md` | 与 ADRMATS 的集成差距分析 |

> ⚠️ **勿运行 `tools/build_prototypes_db.py`**：它从原始提取反向重建 canon，会冲掉整改成果。canon（`prototypes_db/*.json`）已冻结，只在其上直接编辑。

---

## 快速开始

```python
from tools.biomimetic_context import BiomimeticContext

# 初始化
ctx = BiomimeticContext()

# 查询
result = ctx.query(
    pollutant="Pb(II)",
    water_quality={"pH": 6.0, "temperature": 25, "salinity": "low"},
    engineering_constraints=["水稳定性", "可回收性"]
)

# 获取 brief
brief = result['brief']
```

**支持的污染物**：Pb(II), Cd(II), Hg(II), Cu(II), Cr(VI), PFOA, SMX, BPA, TC, TCE, MB, MO 等 25+ 种

**匹配模式**：
- `direct_pollutant_evidence`：有真实 performance_data 的直接实验证据
- `mechanism_feature_bridge`：原型-机制映射（Track 2A 机制层；含无 perf 的污染物映射，诚实降级）
- `molecular_feature_inference`：基于分子特征推断

详见 [ADRMATS 调用说明](docs/ADRMATS_CALL_GUIDE.md)

---

## 架构

```
Biomimetic-design-library/
├── README.md                      # 本文件
├── feature-mapping.json           # 四层映射（核心检索数据）
├── feature_matching_rules.json    # 分子特征匹配规则
├── pollutant_aliases.json         # 污染物名称归一化表
├── pollutant_profiles.json        # 污染物分子特征画像
├── prototypes_db/                 # 正典数据（JSON，canonical source）
├── prototypes/                    # 渲染产物（prototype.md）
├── exports/                       # 导出产物
│   └── adrmats_do_not.json        # 边界条件汇总（62 条）
├── docs/                          # 项目文档
│   ├── README.md                  # 文档导航（见 docs/README.md）
│   ├── design.md                  # 设计规范
│   ├── ADRMATS_DELIVERY_PLAN.md   # 交付计划
│   ├── ADRMATS_CALL_GUIDE.md      # 调用说明
│   ├── SUPPORT_SCOPE_AND_RISKS.md # 支持范围与风险
│   ├── active/                    # 当前恢复操作文档（恢复设计、接手指南）
│   ├── registries/                # 活跃机器账本（decision-queue / boundary / refuted）
│   ├── references/               # 标准/计划（definitions、optimization-plan-v1）
│   ├── imported/                  # 运行时资产（library-enhancement 原理库，被 biomimetic_context.py 读取）
│   └── archive/                   # 历史归档（pre-optimization / optimization-v1-2026-06）
├── examples/adrmats_briefs/       # 真实接口输出示例
├── templates/                     # 模板
├── taxonomy/                      # 分类体系
└── tools/                         # 工具脚本
    ├── biomimetic_context.py      # ADRMATS 接口
    ├── check_boundary_guardrail.py # 边界护栏校验
    ├── export_do_not.py           # DO-NOT 导出
    └── ...                        # 其他校验脚本
```

---

## feature-mapping.json 结构

四层结构，支持三层匹配机制：

| 层级 | 字段 | 作用 |
|------|------|------|
| Layer 1 条件预筛 | `prototype_metadata[id].applicability` | 按 pH、温度、盐度过滤 |
| Layer 2 污染物匹配 | `pollutant_prototype_map[污染物]` | 按污染物检索 + weight 排序 |
| Layer 2 特征匹配 | `feature_prototype_map[特征]` | 按特征检索（无明确污染物时） |
| Layer 3 机制解释 | `mechanism_feature_bridge` | 特征↔机理桥接 |

**设计原则**：库只做匹配响应，不负责推理。约束识别归前置推理模块，组合推理归下游模块。

---

## 三层匹配机制

1. **条件预筛**：根据 pH、温度、浓度等工况约束排除不适用的原型
2. **加权特征匹配**：按 weight×匹配强度计算综合得分
3. **组合推理**：LLM 读取 top 原型详情，提出跨原型的组合方案

---

## 覆盖范围

**生物类别**：微生物、植物、动物、仿生材料

**仿生维度**：分子仿生、结构仿生、形态仿生、过程仿生、功能仿生、系统仿生

**吸附机制**：配位螯合、静电吸引、氢键、π-π堆积、疏水分配、孔道限域、离子交换

**支持的污染物类型**：
- 重金属：Pb(II), Cd(II), Hg(II), Cu(II), Cr(VI), As(V), U(VI)
- PFASs：PFOA, PFOS
- 内分泌干扰物：BPA
- 抗生素：SMX, TC, CIP
- 染料：MB, MO, RhB, CR
- 无机非金属：PO₄³⁻, NH₄⁺, NO₃⁻, F⁻

---

## 验证命令

```bash
# ADRMATS 验收（含 brief 结构 + 排序诚实度 + cautions）
python -X utf8 tools/verify_adrmats_delivery.py

# 接口诚实度测试
python -X utf8 tools/test_interface_honesty.py

# 边界护栏校验（schema + 数值护栏 + gate_level 一致性）
python -X utf8 tools/check_boundary_guardrail.py

# DO-NOT 导出
python -X utf8 tools/export_do_not.py

# 因果链合格率
python -X utf8 tools/check_causal_chain.py

# Translation 合格检查
python -X utf8 tools/check_translation_specificity.py

# Chimera 检查
python -X utf8 tools/check_chimera.py --strict

# 一致性校验
python -X utf8 tools/validate_consistency.py

# 仓库治理
python -X utf8 tools/check_repo_hygiene.py
```

---

## 相关文档

| 文档 | 用途 |
|------|------|
| [ADRMATS 调用说明](docs/ADRMATS_CALL_GUIDE.md) | 接口文档 |
| [支持范围与风险](docs/SUPPORT_SCOPE_AND_RISKS.md) | 当前能力边界 |
| [交付计划](docs/ADRMATS_DELIVERY_PLAN.md) | 里程碑与进度 |
| [设计规范](docs/design.md) | 库定位与 brief 结构 |
| [仓库治理规范](docs/REPOSITORY_HYGIENE.md) | 文件准入与分支策略 |

---

## ID 命名规范

所有原型 ID 统一使用**英文小写 + 连字符**：

| ID | 原型 |
|----|------|
| `metal-organic-framework` | 金属有机框架（MOF）|
| `chitosan` | 壳聚糖 |
| `alginate` | 海藻酸盐 |
| `cellulose-nanocrystal` | 纤维素纳米晶 |
| `starch-granule` | 淀粉颗粒 |
| ... | ... |

完整列表见 `feature-mapping.json` 中的 `prototype_metadata`。

---

## 相关专利

隶属于《一种水处理仿生吸附材料开发智能体系统》
