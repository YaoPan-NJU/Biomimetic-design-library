# 通用仿生水处理设计参考库 / General Biomimetic Water Treatment Design Library

面向整个水处理过程的通用仿生设计参考库。覆盖仿生材料、微生物设计、反应器设计、元件设计，可指导材料和微生物的设计合成，以及基于流场、生化反应、微生物功能、污染物迁移转化等规律设计仿生智慧水处理装备和污水厂提标改造方案。

## 项目状态

**骨架已搭建；自 2026-06-10 起按"先验证后扩展（prove-then-scale）"推进。**

- 已完成：目录结构、原型模板（多尺度）、分类体系、领域索引、入口路由骨架、设计文档
- 当前方向（2026-06-10 评估修订）：先聚焦"反应器/系统设计"消费者，完整做实一条端到端纵切片——**A²/O 进水波动分区自适应（移动氧化还原锋面）**；验证该场景模式成立后再横向扩展，13 领域同时铺开转为后续待办。
- 详见 `docs/2026-06-10-assessment-and-revised-plan.md`（评估与修订计划）、`docs/2026-06-10-vertical-slice-a2o-spec.md`（样板切片）、`docs/design-decisions.md`（DD-013~019）。

## 架构

```
├── prototypes/                 # 共享原型池（所有生物原型）
│   ├── _index.json             # 原型索引
│   └── [prototype-id]/
│       └── prototype.md        # 多尺度原型条目
├── domains/                    # 领域路由层（13个领域）
│   ├── _index.json             # 领域列表
│   └── [domain-id]/
│       ├── domain-profile.md   # 领域概况
│       ├── taxonomy.md         # 领域专属分类
│       ├── mapping.json        # 领域内原型映射
│       └── design-patterns.md  # 领域设计模式
├── shared/                     # 跨领域共享
│   ├── taxonomy/               # 全局分类体系
│   └── cross-domain-links.json # 跨域关系
├── entrypoints/                # 多入口路由（5种）
│   ├── pollutant-router.json   # 污染物入口
│   ├── process-router.json     # 工艺入口
│   ├── problem-router.json     # 设计问题入口
│   ├── retrofit-router.json    # 改造场景入口
│   └── operation-router.json   # 运行调控入口
├── templates/                  # 模板文件
└── docs/                       # 设计文档
```

## 核心特色

### 多尺度设计启示
每个原型描述四个尺度的设计启示：
- **材料尺度**（nm-mm）：表面化学、微观结构、功能涂层
- **组件尺度**（mm-m）：填料几何、膜结构、曝气头
- **反应器尺度**（m）：流场布局、内构件、接触方式
- **系统尺度**（m-km）：多级串联、循环回路、冗余设计

> 注：按 DD-014（2026-06-10），四尺度由"全部必填"松绑为"相关尺度必填、其余显式标注 N/A"，以避免低证据尺度产出占位或被包装的猜测。

### 五种用户入口
| 入口 | 典型问题 |
|------|----------|
| 污染物 | "去除 NH₄⁺-N 有什么仿生方案？" |
| 工艺 | "我在做 MBR，有什么仿生优化思路？" |
| 设计问题 | "曝气效率低，怎么仿生改进？" |
| 改造场景 | "现有 A²/O 池想优化流场" |
| 运行调控 | "DO 偏低，怎么调曝气？" |

### 13 个领域
流体力学、生化反应、分离/过滤、微生物群落、生物膜、代谢路径、传质与流场、固液分离、抗冲击与自恢复、资源化、能源/驱动、系统/群落、吸附

## 聚焦范围

以**生化处理段**为核心（80%+），覆盖活性污泥法、生物膜法、厌氧处理及其组合工艺。

## 上手流程

1. 读取本 README 了解项目全貌
2. 读取 `docs/general-library-design.md` 了解详细设计
3. 读取 `domains/_index.json` 了解领域列表
4. 查看 `templates/prototype-template.md` 了解原型格式
5. 查看感兴趣的领域目录（如 `domains/mass-transfer/`）

> 最新方向、样板切片与领域分析见 `docs/2026-06-10-*` 系列文档。

## 建库工作流

1. 选择目标领域，查阅文献确定候选生物原型
2. 按 `templates/prototype-template.md` 填写原型条目
3. 同步更新对应领域的 `mapping.json`
4. 更新 `prototypes/_index.json` 索引
5. 每完成一批就 git commit + push
