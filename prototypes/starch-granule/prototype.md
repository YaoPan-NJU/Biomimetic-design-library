---
id: starch-granule
name: 淀粉颗粒（Starch Granule）
category: 植物
organism: 
biomimetic_dimension: 分子仿生
features:
  - 微孔
pollutants:
  - Cd(II)
  - methylene blue (MB)
adsorption_mechanisms:
  - MSAs对污染物的主要吸附机制汇总
  - CMCS-2@Fe3O4对Dox吸附机制
  - 四环素(TC)在羧甲基淀粉改性磁膨润土上的吸附机制
  - Cu(II)在WSA/starch/Fe3O4上的吸附机制
  - 淀粉-磁性颗粒结合方式
  - pH对吸附容量的影响
  - MB吸附机制——静电+π-π
qmax_range: "0.0-930.0 mg/g"
applicability:
  pH_range: [6.0, 6.0]
  temp_range: null
  salinity: low
evidence_level: low
# provenance: 2 papers, 0 verified, 13 unverified
# coverage: normal
# status: active
---
# 淀粉颗粒（Starch Granule）

## 1. 生物原型简介

**问题定义**：自然界中生物体需在复杂流体环境中高效捕获目标分子并维持快速物质交换；对应水处理中染料废水吸附容量低、传质动力学慢及再生能耗高的工程挑战。

**生物策略**：借鉴生物组织“功能分区”进化策略，构建微孔(高密度吸附位点)与介孔(快速传质通道)协同的层级网络；结合表面静电吸引与π-π堆积机制实现高效捕获，并通过pH调控表面电荷实现低能耗可逆脱附；成功案例为淀粉衍生Starbons®经冻干-碳化-CO₂活化实现MB吸附qmax 891 mg/g且5min达平衡。

## 2. 吸附机制详解

### 机制1：MSAs对污染物的主要吸附机制汇总

**描述**：electrostatic attraction, π-π stacking, π-cations interaction, intraparticle dispersion, van der Waals interaction, H-bonding, physical adsorption, chemical adsorption
**来源**：DOI 10.1016/j.ijbiomac.2022.07.175

### 机制2：CMCS-2@Fe3O4对Dox吸附机制

**描述**：electrostatic attraction, π-π stacking interplay, H-bonding
**来源**：DOI 10.1016/j.ijbiomac.2022.07.175

### 机制3：四环素(TC)在羧甲基淀粉改性磁膨润土上的吸附机制

**描述**：ionic exchange process + ion bridge (synergism effects)
**来源**：DOI 10.1016/j.ijbiomac.2022.07.175

### 机制4：Cu(II)在WSA/starch/Fe3O4上的吸附机制

**描述**：pore saturation, electrostatic interplay, surface interplay, H bonds, chemical deposition, ionic exchange, complex forming
**来源**：DOI 10.1016/j.ijbiomac.2022.07.175

### 机制5：淀粉-磁性颗粒结合方式

**描述**：hydrophobic effect, complexing, H bonding force, electrostatic attractions
**来源**：DOI 10.1016/j.ijbiomac.2022.07.175

### 机制6：pH对吸附容量的影响

**描述**：pH 3: qe~830 mg/g, Re~83%。pH 9-11: qe~930 mg/g, Re~96%。Zeta电位：pH 3 +12mV→pH 5 零点→pH 11 -30mV。pH>5时材料表面带负电→静电吸引阳离子MB
**来源**：DOI 10.1016/j.jhazmat.2022.129174

### 机制7：MB吸附机制——静电+π-π

**描述**：XPS证据：C1s峰偏移(286.6→286.1, 288.3→287.8, 289.8→289.2 eV)→静电吸引(Starbon®负电含氧基团↔MB正电二甲基亚胺基团)。π-π*峰强度降低→π-π堆积(MB共轭体系↔Starbon®芳香环)。C-N增加4.2-7.1%→MB沉积
**来源**：DOI 10.1016/j.jhazmat.2022.129174

## 3. 结构特征与结构-功能关系

必须保留：微-介-大孔层级协同结构、qmax与SSA/微孔体积的强线性构效关系、pH-swing可逆再生机制；可灵活调整：生物质前驱体类型(纤维素/木质素/壳聚糖等)、活化剂种类(CO₂/KOH/O₂)、表面官能团密度以适配不同污染物。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| Cd(II) | ball-milled starch m | 121-187 | 6 | literature: 10.1016/j.ijbiomac | ❓ |
|  | CMS-g-PVI/PVA/Fe3O4  | Pb(II): 65.00, Cu(II | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | eggshell/starch/Fe3O | Cd2+: 48.544, Pb2+:  | - | literature: 10.1016/j.ijbiomac | ❓ |
| methylene blue  | S950C90 (starch-deri | 891 mg/g(298K, C₀=50 | - | literature: 10.1016/j.jhazmat. | ❓ |
|  |  | MB饱和吸附容量与BET SSA线性相关 | - | literature: 10.1016/j.jhazmat. | ❓ |
|  |  | pH 3: qe~830 mg/g, R | - | literature: 10.1016/j.jhazmat. | ❓ |

## 5. 适用场景

**约束条件**：
- MSAs再生性能汇总: MB: ≤15% reduction after 8 cycles (90.5% after 5 cycles); ibuprofen: 73.56% after 5 cycles %
- 4次循环再生性能: 循环1: 吸附~800→脱附~760。循环2: ~660→~650。循环3: ~600→~590。循环4: ~610→~580 mg/g。脱附剂：乙醇/乙酸(20:1 v/v)+超声5min。pH-swing脱附 mg/g
- pH-swing脱附机制: MB吸附容量随pH升高而增大→可利用pH降低脱附。脱附剂：乙醇/乙酸(20:1 v/v)+超声5min→重复3次→高效脱附。酸性条件下Starbon®表面带正电→排斥阳离子MB→脱附 None

## 6. 相关原型

- metal-organic-framework

## 参考文献

[1] DOI: 10.1016/j.ijbiomac.2022.07.175
[2] DOI: 10.1016/j.jhazmat.2022.129174
