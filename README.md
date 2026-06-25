# 生物原型知识库 / Biological Prototype Knowledge Base

水处理仿生吸附材料开发智能体系统（ADRMATS）的仿生启发检索模块。

---

## v0.2 交付状态（2026-06-25）

> **分支：`v0.2`**｜已验收并推送｜下一版本：`v1.0`（证据获取 + 原型扩展）

### 数据规模

| 指标 | 值 |
|------|-----|
| 活跃原型 | **44** |
| 机制总数 | **520**（520/520 因果链合格） |
| 性能数据 | **502** |
| from_source 元素 | **1277/2080 (61.4%)** |
| 边界规则 | 546 条（21 hard DO-NOT + 525 soft caution） |
| 污染物画像 | 28 种（7 重金属 + 21 新兴有机污染物） |

### G1–G8 验收门

| Gate | 状态 | 详情 |
|------|------|------|
| **G1** Validator | ✅ **10/10 PASS** | 所有数据层 validator 绿色 |
| **G2** 机制绑定 | ✅ **7/7 PASS** | 0 errors, 0 warnings |
| **G3** DO-NOT 硬门 | ✅ **PASS** | 0 inferred hard DO-NOT |
| **G4** Gold-set 结果 | ✅ **7/7 PASS** | 28 queries |
| **G5** Dogfood 评分 | ✅ **PASS** | 有机 6.0/10, 重金属 6.6-6.8/10 |
| **G6** PFOA 诚实切片 | ✅ **3/3 inference** | +21 有机污染物全部 exploratory |
| **G7** 验收报告 | ✅ **Done** | acceptance/ 下完整文档 |
| **G8** Phase E | ✅ **21/21** | 污染物画像 + 别名 + gold-set + backlog |

### 证据诚实化

- **149 条降级**（108 from_source→llm_inferred + 41 basis→llm_inferred），**0 膨胀**
- 所有降级方向保守（向下、可逆），由 Cowork 独立核验
- `literature_backed→from_source = 0`（反膨胀确认）

### 核心能力

- **ADRMATS brief 生成**：7 个 gold-set brief，0 errors, 0 warnings
- **机制绑定**：15 个原型的 `functional_groups`/`key_structures`/`molecular_feature_links` 已补全
- **因果链质量**：520/520 机制有合格因果链卡片（含有意义的结构-功能描述）
- **跨平台兼容**：`.gitattributes` 统一 LF 行尾

### 原则

- 诚实优先、scope 正确、不复活 refuted
- 不用结构绿灯替代结果级有用性
- 不把 LLM inference 伪装成 PDF/source verified fact
- hard DO-NOT 只允许 source-backed 边界

### v1.0 路线

1. **新兴污染物文献获取**：为 7 种高优先级污染物（BPA/PFOA/BDE-209/DDT/PCP/Nonylphenol/TCDD）获取 source-backed 吸附证据
2. **原型扩展**：从 44 向 60–80 推进，按真实证据缺口驱动
3. **因果链深度**：757 条文本已从占位符升级为结构描述，需进一步从 PDF 提取精确引文

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

## v0.2 验收报告

完整的验收报告、变更摘要、决策队列见 `docs/active/acceptance/` 目录。

### 关键文档

| 文档 | 内容 |
|------|------|
| `docs/active/acceptance/v0.2-acceptance-20260625.md` | G1–G8 验收门全绿 |
| `docs/active/acceptance/v0.2-change-digest-20260625.md` | 149 条降级详情 |
| `docs/active/acceptance/v0.2-decision-queue-20260625.md` | 决策队列清零 |
| `docs/active/acceptance/pfoa-honest-slice-20260625.md` | PFOA 诚实切片 |
| `docs/active/acceptance/emerging-pollutant-evidence-backlog-20260625.md` | 21 种新兴污染物 backlog |
| `docs/active/HANDOFF-office-to-home-20260625.md` | 办公室→家里交接文档 |

### v1.0 已完成改进（本分支额外包含）

| 改进项 | 前 | 后 |
|--------|----|----|
| 机制绑定 (G2) | 15 warnings | 0 errors, 0 warnings |
| 因果链合格率 | 467/520 | 520/520 |
| 因果链文本质量 | 757 条占位符 | 0 占位符（全部有意义描述） |
| from_source 诚实重分类 | 1239/2080 | 1277/2080 (+38) |
| 跨平台行尾 | 缺失 | `.gitattributes` LF 统一 |

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
