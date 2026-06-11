# 生物原型知识库 / Biological Prototype Knowledge Base

水处理仿生吸附材料开发智能体系统的核心组件。

## 项目状态

**框架已就绪，原型条目待填充。**

- 已完成：taxonomy、template、feature-mapping.json、检索方案
- 待完成：35个原型的 prototype.md 文件（需按检索方案查文献后用 LLM 提取填充）

## 简介

本知识库为"水处理仿生吸附材料开发智能体系统"提供生物原型的结构化数据支撑。当用户输入目标污染物和水质条件后，需求解析Agent从本知识库中检索匹配的生物原型，获取其吸附机制和结构特征信息。

## 架构

```
Biomimetic-design-library/
├── README.md                    # 本文件
├── feature-mapping.json         # 特征-原型映射表（四层结构）
├── prototypes/                  # 生物原型条目（每个原型一个目录）
│   ├── lotus-leaf/
│   │   └── prototype.md
│   ├── mussel-foot-adhesion/
│   │   └── prototype.md
│   └── ...（共33个原型目录）
├── taxonomy/                    # 分类体系定义
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

## 如何开始

### 新会话/新 AI 上手流程

1. 读取本 README 了解项目全貌
2. 读取 `docs/design.md` 了解详细设计
3. 读取 `SESSION-SUMMARY.md`（如存在）了解跨会话上下文
4. 查看 `feature-mapping.json` 了解当前映射状态
5. 查看 `templates/prototype-template.md` 了解条目格式

### 建库工作流

1. 按检索方案（见项目根目录的检索词清单）在 Web of Science 下载文献
2. 用 LLM 提取 Prompt 从文献中提取结构化数据
3. 按模板填写 `prototypes/[id]/prototype.md`
4. 同步更新 `feature-mapping.json` 中的三个映射表
5. 每完成一批原型就 git commit + push

## 相关专利

隶属于《一种水处理仿生吸附材料开发智能体系统》
