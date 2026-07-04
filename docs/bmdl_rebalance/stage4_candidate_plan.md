# Stage 4 候选计划

**日期：** 2026-07-04
**配额基准：** primary canon = 487 performance_data
**目标：** 活性炭+生物炭相关 evidence 达到 ~15%（73 条），需新增约 50 条

---

## 一、当前状态

| 指标 | primary canon (487) | fresh ETL visible primary (762) |
|------|:-:|:-:|
| AC+BC 现有 | 23 (4.7%) | 26 (3.4%) |
| 15% 目标 | 73 | 114 |
| 需新增 | **~50** | ~88 |

## 二、身份门槛（硬约束）

root prototype 必须是**生物来源/仿生机制/自然结构**。
- ❌ 不造 `biochar.json` / `activated-carbon.json`
- ✅ 借生物机制指导活性炭/生物炭的孔道工程和表面官能团改性

## 三、候选新原型（3 个方向）

### 候选 1：木质素-纤维素碳化仿生原型

- **id**: `lignocellulosic-carbon-architecture`
- **organism**: `{"scientific": "Lignocellulosic biomass (Oryza sativa/Camellia oleifera)", "category": "植物"}`
- **biomimetic_dimension**: `lignocellulosic_carbon_architecture`
- **仿生机制**: 植物木质纤维素的多级孔结构（导管→纤维→微纤丝）经碳化后保留为分级多孔碳，用于指导生物炭孔道工程
- **参考现有原型**: `plant-lignocellulosic-architecture`（已有，但 performance_data 仅 2 条）
- **material_realization_examples**: biochar, activated carbon, hydrochar
- **预期 performance_data**: ~20 条（生物炭/活性炭的吸附性能数据，含 DOI）
- **目标污染物**: PFOA、BPA、抗生素（补有机污染物方向）

### 候选 2：硅藻-植硅体生物硅仿生原型

- **id**: `biogenic-silica-carbon-composite`
- **organism**: `{"scientific": "Bacillariophyta + Oryza sativa (phytolith)", "category": "植物/硅藻"}`
- **biomimetic_dimension**: `biogenic_silica_carbon_composite`
- **仿生机制**: 硅藻硅壳和植物植硅体的生物硅与碳基质复合，提供高比表面积和硅-碳界面
- **参考现有原型**: `diatom-frustule`（已有 20 条 pd）、`rice-husk-phytolith`（已有 0 条 pd）
- **material_realization_examples**: silica-biochar composite, diatomite-AC composite
- **预期 performance_data**: ~15 条
- **目标污染物**: PFOA、重金属离子

### 候选 3：甲壳素-壳聚糖碳化仿生原型

- **id**: `chitin-derived-carbon-functionalization`
- **organism**: `{"scientific": "Crustacea (chitin source)", "category": "动物"}`
- **biomimetic_dimension**: `chitin_derived_carbon`
- **仿生机制**: 甲壳素经碳化后保留含氮官能团（氨基、酰胺基），用于指导活性炭的含氮表面功能化
- **参考现有原型**: `chitosan`（已有 99 条 pd，但偏壳聚糖本身而非碳化产物）
- **material_realization_examples**: N-doped biochar, chitosan-AC composite
- **预期 performance_data**: ~15 条
- **目标污染物**: BPA、抗生素、染料

## 四、执行计划

### 4a：文献证据抽取（Qwen3.7-Plus 多模态）

- 从 `仿生文献库/` 和 `污染物文献/` 提取生物炭/活性炭的吸附性能数据
- 每条必须附 DOI、页码、材料名
- 目标：抽取 ~50 条 performance_data
- 并发：≤2 个子智能体

### 4b：原型 JSON 撰写（GLM-5.2 串行）

- 逐个撰写 3 个新原型 JSON
- 每个需满足 V1-B 准入门槛：≥1 grounded mechanism、honesty ledger、boundary note、design_translation、engineering_constraints (high)
- 串行撰写 + 验收

### 4c：match_weights 准备

- 为新原型准备 match_weights 候选（Stage 5 正式重算）

## 五、验收标准

- [ ] 3 个新原型 JSON 通过 `validate_consistency.py`
- [ ] 每个原型 ≥1 grounded mechanism（DOI + quote + page）
- [ ] engineering_constraints 含 high 条目
- [ ] primary canon AC+BC 占比 ≥15%（73/487）
- [ ] 新原型覆盖有机污染物方向（PFOA/BPA/抗生素）

## 六、风险

| 风险 | 缓解 |
|------|------|
| 文献库 PDF 不足 | 先扫描 `仿生文献库/` 和 `污染物文献/` 确认有生物炭/活性炭相关文献 |
| 新原型机制链幻觉 | 强制 grounded mechanism，DOI + 页码 + 引文 |
| 15% 目标硬凑 | 如果文献不足，诚实报告缺口，不编造数据 |
| validator R14 机制含数值 | 机制描述不含 qmax/接触角等数值，数值放 performance_data |

## 七、待人工决策项

- 3 个候选原型的 ID 和 organism 是否可接受
- 是否允许从 `materials_reference/` 的现有数据中提取 performance_data 而非全部从 PDF 抽取
