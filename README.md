# 生物原型知识库 / Biological Prototype Knowledge Base

水处理仿生吸附材料开发智能体系统（ADRMATS）的仿生启发检索模块。

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

## 当前状态（整改中 · 2026-06-14）

> 工作分支：`opt/curation-grounding-v1`｜整改主题：**策展 + 接地 + 诚实分级**（把"看着广、其实是叙事"的库，收敛为"窄但每条可信、可溯源"的库）。

| 指标 | 数值 |
|------|------|
| active 原型（参与检索）| 24 |
| materials_reference（降级，不检索）| 4（MOF / 纤维素纳米晶 / 淀粉 / 海藻酸盐）|
| parked（超范围停放）| 1（namib-beetle）|
| 机制总数 | 534 |
| 因果链卡（核心、可迁移原理）| 28 张（覆盖 24/24 原型）|
| 其中 PDF 已核验 verified | 23 张 |
| 仍待下载文献核验 | 5 张（coral / magnetic-bacteria / pitcher-plant / lobster / spider-silk）|
| 校验错误 / chimera 违规 | 0 / 0 |

**整改进度**：Phase 0–6 已完成并复核（基线、接口诚实度、策展、去污染、字段语义、因果链补全、PDF 核验）；Phase 7（设计转译）/ 8（失效边界 + DO-NOT）/ 9（总验收）进行中。详见 `docs/optimization-v1/`。

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
| `docs/optimization-v1/PLAN.md`（即 `优化方案_仿生库策展与接地_v1.md`）| 9 阶段执行手册 |
| `docs/optimization-v1/DEFINITIONS.md` | 判定标准 / 字段 schema / 边界护栏 / 铁律（权威）|
| `docs/optimization-v1/交接文档_HANDOFF.md` | 复核角色交接（含当前进度与失败模式教训）|
| `docs/optimization-v1/coverage-gaps.md` | 策展后失去 direct evidence 的污染物（Boron / Co(II) 为真缺口）|
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
- `direct_pollutant_evidence`：有直接实验数据
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
├── docs/                          # 项目文档
│   ├── design.md                  # 设计规范
│   ├── ADRMATS_DELIVERY_PLAN.md   # 交付计划
│   ├── ADRMATS_CALL_GUIDE.md      # 调用说明
│   └── archive/                   # 归档文档
├── examples/adrmats_briefs/       # 真实接口输出示例
├── templates/                     # 模板
├── taxonomy/                      # 分类体系
└── tools/                         # 工具脚本
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
# ADRMATS 验收
python -X utf8 tools/verify_adrmats_delivery.py

# 校验一致性
python -X utf8 tools/validate_consistency.py

# 检查 chimera
python -X utf8 tools/check_chimera.py

# 检查仓库治理
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
