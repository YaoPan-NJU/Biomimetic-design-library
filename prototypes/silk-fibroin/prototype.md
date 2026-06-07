---
id: silk-fibroin
name: 丝素蛋白（Silk Fibroin）
category: 动物
organism: Bombyx mori
biomimetic_dimension: 结构仿生
features:
  - 纤维状
  - 层状
pollutants:
  - Cu²⁺
  - MB
  - chloroform
  - methyl orange (MO)
  - methylene blue (MB)
adsorption_mechanisms:
  - 吸附机制
  - BS/SF/PUF三元协同设计
  - 结晶紫吸附机制
  - 静电纺丝工艺参数
  - 木质素疏水性来源
  - MO吸附机制
  - Cu²⁺吸附机制
  - 丝素蛋白分子结构与力学性能
  - 丝素蛋白极性官能团——吸附活性位点
  - Na₂CO₃脱胶丝纤维——超疏水油水分离
qmax_range: "2.0-811.3 mg/g"
applicability:
  pH_range: [4.2, 4.2]
  temp_range: null
  salinity: low
evidence_level: low
# provenance: 5 papers, 0 verified, 20 unverified
# coverage: normal
# status: active
---
# 丝素蛋白（Silk Fibroin）

## 1. 生物原型简介

**问题定义**：自然界重金属离子对水生生态的毒性累积 vs 传统吸附剂容量低、难再生；对应水处理中需开发高容量、可循环的绿色吸附材料以高效去除Cu²⁺与Cr⁶⁺。

**生物策略**：生物进化出硅质骨架与蛋白基质协同调控离子的策略；关键机制为生物硅提供高比表面积介孔骨架，丝纤蛋白暴露-NH与C=O极性基团实现金属螯合；成功案例为BS/SF/PUF三元复合材料实现Cu²⁺(331.69 mg/g)与Cr⁶⁺(201.56 mg/g)超高吸附量。

## 2. 吸附机制详解

### 机制1：吸附机制

**描述**：多重机制协同: 静电作用+离子交换+范德华力+交联+氢键
**关键官能团**：-OH, -NH, C=O on biocomposite surface
**来源**：DOI 10.1016/j.eti.2022.102741

### 机制2：BS/SF/PUF三元协同设计

**描述**：BS(生物硅高比表面积)+SF(极性基团螯合)+PUF(多孔弹性基底)→三元协同→综合性能优于单一组分
**来源**：DOI 10.1016/j.eti.2022.102741

### 机制3：结晶紫吸附机制

**描述**：π-π共轭 + 氢键 + 阴阳离子结合
**来源**：DOI 10.1016/j.ijbiomac.2023.126863

### 机制4：静电纺丝工艺参数

**描述**：SF: 2μL/min, 18kV, 15cm, 90rpm, 4h/层; Lignin/PAN: 3μL/min, 18kV, 15cm, 90rpm, 2h/层
**来源**：DOI 10.1016/j.ijbiomac.2023.126863

### 机制5：木质素疏水性来源

**描述**：木质素疏水性: 酚环+甲氧基; SF疏水性: 疏水嵌段
**来源**：DOI 10.1016/j.ijbiomac.2023.126863

### 机制6：MO吸附机制

**描述**：主导：PEI质子化氨基(-NH₃⁺)与阴离子染料MO静电吸引；辅助(GO部分)：MO芳香环与GO的π-π堆叠
**来源**：DOI 10.1002/admi.202001892

### 机制7：Cu²⁺吸附机制

**描述**：PEI氨基(-NH₂)螯合Cu²⁺→化学吸附；中心发散孔道→快速扩散→活性位点可及；低密度+高孔隙→快速传质
**来源**：DOI 10.1002/admi.202001892

### 机制8：丝素蛋白分子结构与力学性能

**描述**：β-sheet结晶区提供机械强度，极限强度300-740 MPa；丝素为嵌段共聚物：疏水重复区(Gly/Ala/Ser 43-46%/25-30%/12%) + 亲水非重复区
**来源**：DOI 10.1007/s10924-022-02741-6

## 3. 结构特征与结构-功能关系

必须保留：生物硅介孔骨架、丝纤蛋白极性螯合位点、戊二醛交联网络；可灵活调整：PUF基底孔隙率、BS与SF质量配比、交联密度以适配不同水质。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
|  | BS/SF/PUF biocomposi | Cu2+: 331.69 mg/g; C | - | literature: 10.1016/j.eti.2022 | ❓ |
|  | BS/SF/PUF biocomposi | Cu2+ 89.8% (pH 5); C | - | literature: 10.1016/j.eti.2022 | ❓ |
| Cu²⁺ | SF-PEI-2 millimetric | 186.7 | 4.2 | literature: 10.1002/admi.20200 | ❓ |
| Cu²⁺ | SF-PEI-2@GO core-she | 171.6 | 4.2 | literature: 10.1002/admi.20200 | ❓ |
| methyl orange ( | SF-PEI-2 millimetric | 811.3 | - | literature: 10.1002/admi.20200 | ❓ |
| chloroform | SF-PEI-2@GO aerogel  | 1138 | - | literature: 10.1002/admi.20200 | ❓ |
| methylene blue  |  | SF: 235.84 mg/g; SF/ | 6-10 | literature: 10.1039/d1va00047k | ❓ |
| MB |  | SF: 86.24% (24h); SF | room temperature | literature: 10.1039/d1va00047k | ❓ |

## 5. 适用场景

**约束条件**：
- 循环再生性能: EDTA脱附→4次连续吸附/脱附循环后仍可高效再用 cycles
- TGA热稳定性: BS: 总失重仅9%(至800°C); 复合材料: 第一阶段8.6%(150°C失水)→第二阶段35.4%(380°C SF酰胺分解)→第三阶段28.3%(400-800°C PUF碳骨架分解)→73%总失重 %
- Cu²⁺再生循环: EDTA(0.1M)洗脱→蓝变白→可循环；但首次循环后容量有损失(EDTA残留) None
- 再生丝素膜——酸性染料吸附: 酸性黄11 Qe=88.50 mg/g(b=1.06); 萘酚橙74.63 mg/g(b=0.30); 直接橙S 76.34 mg/g(b=0.12) mg/g

## 6. 相关原型

- cellulose-nanocrystal
- lobster-exoskeleton
- mycelium
- oyster-shell
- scallop-shell

## 参考文献

[1] DOI: 10.1002/admi.202001892
[2] DOI: 10.1016/j.eti.2022.102741
[3] DOI: 10.1039/d1va00047k
