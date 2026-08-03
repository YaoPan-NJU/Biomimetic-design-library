---
id: bug-family-carboxylate-pincer
name: Bug 家族羧酸夹钳底物结合蛋白（Bug-Family Carboxylate-Pincer Solute-Binding Protein）
category: 微生物
organism: Bordetella pertussis
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 几何识别
adsorption_mechanisms:
  - 羧酸夹钳初始锚定与第二结构域生产性占位判别
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 1 papers, 4 verified, 0 unverified
# coverage: full
# status: active
---
# Bug 家族羧酸夹钳底物结合蛋白（Bug-Family Carboxylate-Pincer Solute-Binding Protein）

## 1. 生物原型简介

Bordetella pertussis 的 Bug27 属于 Bug 家族周质底物结合蛋白，采用双结构域 Venus flytrap 折叠。家族的两个保守模体以直接和水介导氢键形成“羧酸夹钳”。Bug27 的开态与配体结合结构进一步显示，羧酸头基可以先由第一结构域锚定，但只有配体其余部分与第二结构域形成合适接触时，闭合构象才被稳定。该原型的可迁移价值是“头基命中 + 第二位点生产性占位”的串联判别，而不是泛化的羧酸吸附。GenX 仅共享羧酸头基，故其材料映射保留为低权重 exploratory。

## 2. 吸附机制详解

### 机制1：羧酸夹钳初始锚定与第二结构域生产性占位判别

**描述**：Bug 家族底物结合蛋白采用 Venus flytrap 双域折叠。来自两结构域的保守 β-strand–β-turn–α-helix 模体通过直接和水介导氢键形成羧酸夹钳。Bug27 的开态结构表明，配体羧酸可先由第一结构域的一半夹钳锚定；只有与第二结构域形成合适接触时，闭合构象才被稳定，从而区分生产性与非生产性结合。
**关键官能团**：['主链酰胺 NH', '保守极性侧链', '保守水分子']
**来源**：DOI 10.1016/j.jmb.2007.08.006

## 3. 结构特征与结构-功能关系

| 结构层级 | 已接地特征 | 功能含义 |
|---|---|---|
| 蛋白整体 | 双结构域 Venus flytrap 折叠 | 为开态捕获和闭态判别提供构象基础 |
| 第一检查点 | 一半羧酸夹钳先与配体头基形成氢键 | 提供初始锚定，但单独不足以定义生产性结合 |
| 第二检查点 | 第二结构域与配体其余部分建立合适接触 | 稳定闭合并区分生产性与非生产性配体 |

合成转译的判决指标应是第二位点相对“只有头基位点”的选择性增量；若没有可复现增量，就不能宣称实现 Bug 式识别。

## 4. 已报道性能数据

本条没有材料去除性能记录。`performance_data` 为空；天然蛋白的配体识别不能换算为 GenX 吸附性能。

## 5. 适用场景

**约束条件**：
- 双位点空间耦合：合成材料必须让羧酸头基位点与第二占位位点保持确定的相对位置；随机混合两类官能团不能复现 Bug 的闭合判别。
- 水相氢键竞争：天然羧酸夹钳位于可闭合蛋白裂隙；暴露在体相水中的孤立氢键给体不能假定具有同等作用。

**探索性材料映射**：在刚性孔腔内耦合羧酸氢键位点与第二形状位点，用头基单点受体、第二位点失活体和线性 PFCA 对照检验 GenX 的差分识别。无直接 GenX-Bug27 结合证据。

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling

## 参考文献

[1] Herrou J, et al. *Journal of Molecular Biology*. 2007;373:954-964. DOI: 10.1016/j.jmb.2007.08.006. PDB: 2QPQ.
