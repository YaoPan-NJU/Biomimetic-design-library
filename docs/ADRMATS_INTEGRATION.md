# ADRMATS 集成文档 — 分层检索策略

> **唯一执行入口：[ADRMATS_DELIVERY_PLAN.md](ADRMATS_DELIVERY_PLAN.md)**
> 适用项目：Biomimetic-design-library（ADRMATS 的仿生**启发**检索模块）
> 编制日期：2026-06-08
> 配合阅读：`docs/design.md`（库定位与 brief 结构）

---

## 1. 定位

本库是 ADRMATS 系统的**仿生启发检索模块**，不是材料设计器、不是事实库。

**链路**：`水质约束智能体 → 仿生设计智能体（推理 + 调库）→ 仿生设计 brief → 对抗设计模块（真正设计材料）`

库的唯一职责：让每个原型都能干净、可溯源、标注诚实地供出 brief 的三件套（match + mechanism + design_translation）。

---

## 2. 分层检索策略

### 2.1 核心原则

**新污染物匹配原则**：`pollutant_prototype_map` 只作为 direct evidence 层，不能作为唯一入口。

对 PFOA、SMX、BPA 等痕量有机污染物，必须：
1. 先做污染物分子特征画像（长链/芳香环/羧基/磺酰胺/酚羟基/电荷/pH 形态等）
2. 再由分子特征推可能吸附相互作用
3. 最后匹配仿生机制/结构/特征和候选原型

### 2.2 三层检索架构

```
查询输入
    ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 0: 污染物标准化 + 分子特征画像                         │
│   - canonical_name: 标准化污染物名                           │
│   - pollutant_class: 污染物类别（重金属/染料/PPCPs/PFASs等） │
│   - molecular_features: 分子特征列表                         │
│   - likely_interactions: 可能的吸附相互作用                   │
│   - profile_basis: database | rule | inference | llm_inference │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: 条件预筛（applicability）                           │
│   - 按 pH、温度、盐度等工况约束过滤不适用的原型              │
│   - 数据来源：各原型测试工况聚合                             │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 2a: Direct Evidence 匹配                              │
│   - 查询 pollutant_prototype_map[canonical_name]            │
│   - 返回：有该污染物直接实验数据的原型 + weight              │
│   - 标记：direct_evidence=true, match_basis=direct_pollutant_evidence │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 2b: Feature-Based Retrieval（新污染物必需）            │
│   - 按 molecular_features 匹配 mechanism_feature_bridge     │
│   - 按 likely_interactions 匹配机制/结构/特征                │
│   - 标记：direct_evidence=false, match_basis=molecular_feature_inference │
│   - 必须说明：哪些分子特征连接到哪些机制/结构/特征           │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: 组装 brief                                         │
│   - 合并 direct evidence + feature-based candidates         │
│   - 每个 candidate 带 match_basis + direct_evidence 标记    │
│   - 生成 honesty_ledger（区分 facts / leads / inferences）  │
└─────────────────────────────────────────────────────────────┘
    ↓
brief 输出
```

### 2.3 match_basis 枚举

| match_basis | 含义 | direct_evidence |
|-------------|------|-----------------|
| `direct_pollutant_evidence` | 有该污染物的直接实验数据 | true |
| `pollutant_class_evidence` | 有同类污染物的直接实验数据 | true（同类别） |
| `molecular_feature_inference` | 靠分子特征匹配机制 | false |
| `mechanism_feature_bridge` | 靠机制-特征桥接 | false |
| `llm_suggested_low_confidence` | LLM 低置信度建议 | false |

### 2.4 关键规则

1. **direct evidence 优先**：有直接实验数据的原型优先排序
2. **feature-based inspiration 可以下传**：但必须标 `direct_evidence=false`，不能伪装成文献直接证据
3. **PFOA/SMX/BPA 等新污染物**：不能只查污染物名，必须有画像 + match_basis
4. **把 feature-based inspiration 写成 direct evidence → D6 风险，必须改**

---

## 3. 接口契约（BiomimeticContext）

### 3.1 接口必须暴露的字段

```json
{
  "brief": {
    "context": {
      "pollutant_profile": {
        "canonical_name": "string",
        "pollutant_class": "string",
        "molecular_features": ["string"],
        "likely_interactions": ["string"],
        "profile_basis": "database | rule | chemical_knowledge_inference | llm_inference"
      }
    },
    "candidates": [{
      "match": {
        "match_basis": "direct_pollutant_evidence | pollutant_class_evidence | molecular_feature_inference | mechanism_feature_bridge | llm_suggested_low_confidence",
        "direct_evidence": "boolean"
      },
      "mechanism": {
        "molecular_feature_links": ["string"],
        "attribution": {
          "verification_tier": "verified | corroborated | single_source | unverified | needs_review"
        }
      },
      "design_translation": {
        "source_tier": "literature | llm_inference"
      }
    }],
    "honesty_ledger": {
      "facts": ["string"],
      "leads": ["string"],
      "inferences": ["string"]
    }
  }
}
```

### 3.2 下游消费门控

| 用途 | 可消费等级 |
|------|-----------|
| 强排序 / 候选打分 / 事实性解释 | 仅 `verified` + `corroborated` |
| 假设播种 / 设计灵感 / 探索方向 | `verified` + `corroborated` + `single_source` + `unverified`（均作**线索**，不得断言为事实） |
| 完全排除 | `needs_review`（直到缺陷解决） |
| 设计提示采纳 | `llm_inference` 提示可下传，但需在产出中保留"推断"标记 |
| 新污染物召回 | direct evidence 优先；无直接证据时允许 feature-based inspiration，但必须保留 `direct_evidence=false` 与 `match_basis` |

**强制方式**：契约写进接口 schema，不是写进文档共识。下游做任何定量排序时，若上游某条无 verification 等级或为 `needs_review`，接口直接拒绝该字段进入排序输入。

---

## 4. 与旧文档的关系

- **本文件是分层检索策略的唯一真相源**
- 旧文档（README、HANDOFF、SESSION-CONTEXT、旧优化方案、旧审计报告）中关于"污染物名查表"的理解已过时
- 若有冲突，以本文件和《任务布置》《分层核查标准》《评分卡》三份 v1.1 文档为准

---

*本文档由任务布置 Phase 0 要求创建，作为 ADRMATS 集成的分层检索策略说明。*
