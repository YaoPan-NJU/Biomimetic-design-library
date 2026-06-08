# 生物原型知识库 / Biological Prototype Knowledge Base

水处理仿生吸附材料开发智能体系统的核心组件。

## 简介

本知识库为"水处理仿生吸附材料开发智能体系统"提供生物原型的结构化数据支撑。当用户输入目标污染物和水质条件后，需求解析Agent从本知识库检索匹配的生物原型，获取其吸附机制和结构特征信息。

## 架构

```
Biomimetic-design-library/
├── README.md                    # 本文件
├── feature-mapping.json         # 特征-原型映射表（四层结构）
├── prototypes_db/               # 正典数据（33个JSON）
├── prototypes/                  # 渲染产物（36个prototype.md）
├── taxonomy/                    # 分类体系
│   ├── organisms.md             # 生物分类
│   ├── mechanisms.md            # 吸附机制分类
│   └── pollutants.md            # 污染物分类
├── templates/
│   └── prototype-template.md    # 原型条目模板
└── docs/
    └── design.md                # 设计文档
```

## feature-mapping.json 结构

四层结构，支持三层匹配机制：

| 层级 | 字段 | 作用 |
|------|------|------|
| Layer 1 条件预筛 | `prototype_metadata[id].applicability` | 按 pH、温度、盐度过滤 |
| Layer 2 污染物匹配 | `pollutant_prototype_map[污染物]` | 按污染物检索 + weight 排序 |
| Layer 2 特征匹配 | `feature_prototype_map[特征]` | 按特征检索（无明确污染物时） |
| Layer 3 机制解释 | `mechanism_feature_bridge` | 特征↔机理桥接 |

**设计原则**：库只做匹配响应，不负责推理。约束识别归前置推理模块，组合推理归下游模块。

**weight 定义**：0-1 连续值，表示该原型对某个污染物/特征的匹配强度。

## ID 命名规范

所有原型 ID 统一使用**英文小写 + 连字符**：

| ID | 原型 |
|----|------|
| `lotus-leaf` | 荷叶表面 |
| `mussel-foot-adhesion` | 贻贝足丝 |
| `sulfate-reducing-bacteria` | 硫酸盐还原菌 |
| `polydopamine-coating` | 聚多巴胺(PDA)涂层 |
| ... | ... |

完整列表见 `feature-mapping.json` 中的 `prototype_metadata`。

## 三层匹配机制

1. **条件预筛**：根据 pH、温度、浓度等工况约束排除不适用的原型
2. **加权特征匹配**：按 weight×匹配强度计算综合得分
3. **组合推理**：LLM 读取 top 原型详情，提出跨原型的组合方案

## 覆盖范围

- **生物类别**：微生物、植物、动物、仿生材料
- **仿生维度**：分子仿生、结构仿生、形态仿生、过程仿生、功能仿生、系统仿生
- **吸附机制**：配位螯合、超疏水分离、多孔吸附、生物矿化、纤维结构、功能仿生

## 如何使用

本知识库通过 `feature-mapping.json` 提供检索接口：

1. **按污染物检索**：查询 `pollutant_prototype_map[污染物名]` 获取匹配原型及权重
2. **按特征检索**：查询 `feature_prototype_map[特征名]` 获取匹配原型
3. **条件预筛**：根据工况条件（pH、温度等）过滤不适用的原型
4. **机制桥接**：通过 `mechanism_feature_bridge` 理解特征与机理的对应关系

详细设计见 `docs/design.md`。

## 相关专利

隶属于《一种水处理仿生吸附材料开发智能体系统》
