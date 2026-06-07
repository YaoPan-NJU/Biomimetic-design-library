---
id: polydopamine-coating
name: 聚多巴胺涂层（Polydopamine Coating）
category: 仿生材料
organism: Mytilus edulis（贻贝，聚多巴胺仿生来源）
biomimetic_dimension: 分子仿生
features:
  - 邻苯二酚基团
  - 金属配位能力
  - π电子体系
  - 湿态粘附
pollutants:
  - 无机磷
adsorption_mechanisms:
  - 沙漠甲虫仿生灵感与设计原理 Desert beetle biomimetic inspiration and design principle
  - 水滴'生长-跳跃'排液机制 Water droplet 'growing-jumping' discharge mechanism
  - 油滴捕获的'捕获-聚并-脱离'机制 Oil capture 'capture-coalescence-detachment' mechanism
  - 制备方法概述(绿色制备/废弃PET再利用) Preparation method overview (green/waste PET reuse)
  - 吸附机制 — 配位螯合
  - PDA吸附机制-姜黄素
  - PDA吸附机制-番茄红素
qmax_range: "12.6-159.8 mg/g"
applicability:
  pH_range: [7.0, 7.0]
  temp_range: null
  salinity: moderate
evidence_level: low
# provenance: 4 papers, 0 verified, 12 unverified
# coverage: normal
# status: active
---
# 聚多巴胺涂层（Polydopamine Coating）

## 1. 生物原型简介

**问题定义**：脂溶性色素（姜黄素、番茄红素）具有抗肿瘤、抗氧化等广泛药理作用，但难溶于水、口服不易吸收、存在肝脏首过效应、体内代谢清除快、生物利用率低、稳定性差、见光易分解，需要合适的药物递送系统解决这些问题。

**生物策略**：聚多巴胺（PDA）是天然生物色素黑色素的主要成分，通过多巴胺的氧化自聚合反应得到，具有良好的稳定性、生物可降解性、生物相容性和光热转换特性。PDA表面具有大量邻苯二酚和氨基功能基团，具有很强的粘附性（仿贻贝足丝蛋白机制），可包覆在多种材料表面。壳聚糖是由氨基葡萄糖组成的天然阳离子聚合物，具有良好的生物相容性、低毒性和可生物降解性，且具有肠粘膜粘附特性。

## 2. 吸附机制详解

### 机制1：沙漠甲虫仿生灵感与设计原理 Desert beetle biomimetic inspiration and design principle

**描述**：受Stenocara beetle背部交替亲水突起+超疏水壳面微结构启发，构建反向甲虫结构：超疏水Al₂O₃突起(捕油)+超亲水PDA/PET底层(排水)，通过表面能梯度(Fd≈γ_oil(cosθ₁-cosθ₂))驱动油滴聚集
**来源**：DOI 10.1016/j.seppur.2023.123547

### 机制2：水滴'生长-跳跃'排液机制 Water droplet 'growing-jumping' discharge mechanism

**描述**：两阶段机制：'生长'阶段(水滴在微腔中核化生长→Laplace压力梯度∇P~2σ/d_eq(1/R₁-1/R₂)驱动水滴变形自导向)→'跳跃'阶段(合并后表面能释放触发自发跳跃运动，低粘附力确保跳跃)
**来源**：DOI 10.1016/j.seppur.2023.123547

### 机制3：油滴捕获的'捕获-聚并-脱离'机制 Oil capture 'capture-coalescence-detachment' mechanism

**描述**：三阶段机制：'捕获'(超疏水Al₂O₃突起作为油吸收器捕获微小油滴，不平衡力Fd=γ_oil(cosθ₁-cosθ₂)驱动)→'聚并'(被捕获油滴作为油储库，小油滴聚并成大油滴)→'脱离'(水下超疏油PDA/PET表面+Al₂O₃突起表面张力排斥大油滴)
**来源**：DOI 10.1016/j.seppur.2023.123547

### 机制4：制备方法概述(绿色制备/废弃PET再利用) Preparation method overview (green/waste PET reuse)

**描述**：三步法：静电纺丝制备PET纤维膜→DA-HCl原位聚合PDA修饰→真空抽滤涂覆Al₂O₃突起；原料为废弃可口可乐PET瓶
**来源**：DOI 10.1016/j.seppur.2023.123547

### 机制5：吸附机制 — 配位螯合

**描述**：La与磷酸根配位生成磷酸镧化合物

### 机制6：PDA吸附机制-姜黄素

**描述**：None

### 机制7：PDA吸附机制-番茄红素

**描述**：None

## 3. 结构特征与结构-功能关系

必须保留：中空介孔聚多巴胺纳米粒（HPDA）作为核心载体（高比表面积、纳米孔道、中空结构、pH敏感性、邻苯二酚/氨基官能团）、聚乙二醇改性壳聚糖作为外层包覆（肠粘膜粘附、减少巨噬细胞摄取、被动靶向）。可灵活调整：HPDA与脂溶性色素质量比（5-8:1）、壳聚糖与PEG质量比（1:0.2-0.3）、冻干条件。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| 无机磷 | BC/PDA/La(OH)3-1 | 159.8 | 7.0 | patent: CN114887602A | ❓ |
| 无机磷 |  | 159.8 vs 91.2 vs 12. | 7.0 | patent: CN114887602A | ❓ |
| 无机磷 | BC/PDA/La(OH)3-1 | 110 | - | patent: CN114887602A | ❓ |
| 无机磷 | BC/PDA/La(OH)3-1 | 143.4 | - | patent: CN114887602A | ❓ |
|  |  | >72 | - | patent: CN115055171A | ❓ |

## 5. 适用场景

**约束条件**：
- APP3膜的循环稳定性 Cycle stability of APP3 membrane: 25次循环后分离效率达99.86%，通量>2121 L·m⁻²·h⁻¹，表面形貌保持稳定无结构坍塌 None
- APP3膜的酸碱稳定性 Acid and alkali stability of APP3 membrane: 在不同pH溶液中浸泡24h后保持稳定(图9c-d) None
- 循环稳定性 — 5次循环后吸附容量保持: 110 mg/g
- 镧泄漏量 — 5次循环: 5 mg/L
- 番茄红素光稳定性提升: 97.98 %
- 循环吸附稳定性-重金属去除率保持: >72 %
- 循环吸附稳定性-材料回收率: >82 %

## 6. 相关原型

- alginate
- chitosan
- metal-organic-framework
- mussel-foot-adhesion
- plant-tannin

## 参考文献

[1] 专利: CN114887602A
[2] 专利: CN115055171A
