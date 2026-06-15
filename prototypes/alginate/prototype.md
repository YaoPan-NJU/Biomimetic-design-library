---
id: alginate
name: 海藻酸盐（Alginate）
category: 植物
organism: Phaeophyceae
biomimetic_dimension: 分子仿生
features:
  - 负电表面
  - 羧基
  - 金属配位能力
pollutants:
  - As(III)
  - Ciprofloxacin (CIP)
  - Co(II)
  - Cr(VI)
  - Crystal Violet (CV) dye
  - Cu(II)
  - Levofloxacin (S-FOX)
  - MB (methylene blue)
  - Pb(II)
  - Phosphate
  - U(VI)
  - acid blue-113 (anionic dye)
  - tetracycline
  - triclosan (TCS)
adsorption_mechanisms:
  - 海藻酸钠水凝胶的七种制备方法
  - 海藻酸钠水凝胶的吸附机制分类
  - Zeta电位验证
  - 吸附机制——化学吸附+静电作用
  - 海藻酸盐的吸附机制类型
  - 蠕动泵连续油水分离
  - FTIR化学表征——硅烷改性成功
  - 吸附机理——疏水亲油+毛细管力
  - 仿荷叶超疏水——硅烷改性
  - Adsorption mechanisms summary
qmax_range: "3.2-2887.0 mg/g"
applicability:
  pH_range: [3.0, 6.0]
  temp_range: null
  salinity: moderate
evidence_level: low
# provenance: 11 papers, 0 verified, 67 unverified
# coverage: normal
# status: active
---
# 海藻酸盐（Alginate）

## 1. 生物原型简介

**问题定义**：自然界中褐藻需要在海洋复杂离子环境中维持结构稳定并富集特定金属离子；水处理中面临多组分复杂水体（重金属、染料、抗生素等）的高效、选择性吸附及材料机械强度不足的挑战。

**生物策略**：褐藻通过分泌海藻酸钠，利用Egg-box模型与二价阳离子（如Ca²⁺）交联形成稳定的三维网络结构。进化策略包括通过丰富的羧基和羟基提供配位位点，以及形成多网络和'砖与mortar'结构增强力学性能。成功案例包括利用离子印迹技术实现Pb(II)的高选择性识别，以及构建吸附-光催化协同体系实现污染物降解与材料再生。

## 2. 吸附机制详解

### 机制1：海藻酸钠水凝胶的七种制备方法

**描述**：离子交联、共价交联、乳化、静电络合、自组装、微波辅助、超声辅助
**来源**：DOI 10.1016/j.ijbiomac.2025.140801

### 机制2：海藻酸钠水凝胶的吸附机制分类

**描述**：物理吸附（范德华力+氢键）和化学吸附（共价键+离子交换+表面络合）
**来源**：DOI 10.1016/j.ijbiomac.2025.140801

### 机制3：Zeta电位验证

**描述**：CNF-SA比纯SA水凝胶珠含有更多负电荷羧酸根离子→增强静电吸附Pb²⁺
**来源**：DOI 10.1016/j.molliq.2020.115122

### 机制4：吸附机制——化学吸附+静电作用

**描述**：准二级动力学+Langmuir→化学吸附为主；-COO⁻与Pb²⁺静电吸引+配位；CNF增加负电荷→增强静电吸附
**关键官能团**：['-COO⁻ (carboxylate)', '-OH (hydroxyl)']
**来源**：DOI 10.1016/j.molliq.2020.115122

### 机制5：海藻酸盐的吸附机制类型

**描述**：静电相互作用、离子交换、配位螯合、化学还原（Cr(VI)→Cr(III)）、光催化还原、氢键、范德华力
**来源**：DOI 10.5004/dwt.2022.28834

### 机制6：蠕动泵连续油水分离

**描述**：通过蠕动泵负压吸引→气凝胶疏水亲油+毛细管吸收力协同→连续选择性吸油
**来源**：DOI 10.1016/j.jhazmat.2022.129965

### 机制7：FTIR化学表征——硅烷改性成功

**描述**：改性后1206 cm⁻¹(Si-O-Si不对称伸缩)和722 cm⁻¹(C-Si不对称伸缩)特征峰出现; 疏水基团显著增强
**来源**：DOI 10.1016/j.jhazmat.2022.129965

### 机制8：吸附机理——疏水亲油+毛细管力

**描述**：疏水亲油性(硅烷改性)+气凝胶多孔结构的毛细管吸收力→协同选择性吸油
**来源**：DOI 10.1016/j.jhazmat.2022.129965

## 3. 结构特征与结构-功能关系

必须保留特征：Egg-box离子交联机制、丰富的含氧官能团（-COOH, -OH）提供基础吸附位点、三维多孔网络结构。可灵活调整特征：复合组分（如壳聚糖、PEI、MOF）以引入氨基或特定孔道、多网络交联密度、表面形貌（如蜂窝状、气凝胶、微球）。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| Pb(II) | CA/KCB composite aer | 664.6 | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | Graphene oxide/algin | Cr(III): 118.6, Pb(I | - | literature: 10.1016/j.ijbiomac | ❓ |
| Pb(II) | Alginate/melamine/ch | 1331.6 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Ciprofloxacin ( | ZIF-8/SC three-dimen | 2887 | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | NiFe₂O₄@Ca-alginate  | MB: 1243, Rh6G: 845 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Cr(VI) | Alginate@PEI core-sh | 431.6 | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | SA/PEI-0.25 three-di | Cr(VI): 678.67, Cd(I | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | Graphitic carbon nit | Pb(II): 383.4, Ni(II | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | Core/shell amine-mod | Pb(II): 535.6, Cr(VI | - | literature: 10.1016/j.ijbiomac | ❓ |
| Pb(II) | CaAlg/CPAN TFNC memb | 254.5 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Pb(II) | Defective MOF-801/so | 375.48 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Pb(II) | Lead ion-imprinted p | IIP: 357.4, NIP: 296 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Pb(II) | SA/PEI/三聚氰胺共功能化交联吸附剂 | 596.68 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Co(II) | Ca-Me/SA@0.75PEI (Me | 698.62 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Phosphate | SA/Zr hydrogel (Zr⁴⁺ | 256.79 | 3 | literature: 10.1016/j.ijbiomac | ❓ |
|  | MIL-121@CA thermores | Cu²⁺: 204.5, Cd²⁺: 8 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Levofloxacin (S | GA(SA-Al/Ca) seconda | 145.12 mg/g, 10分钟内达平 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Phosphate | SA-La@PEI phosphate  | 121.1 | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | Alginate-derived bio | MB: 99.61, BF: 86.83 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Cu(II) | SA/MX/CFO beads (sod | 234.3 | 5.3 | literature: 10.1016/j.ijbiomac | ❓ |
| Ciprofloxacin ( | κ-Carrageenan/sodium | 229 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Crystal Violet  | ALG-Aw (alginate-bas | 符合Redlich-Peterson模型 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Phosphate | Electrochemically mo | 169.89 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Phosphate | Porous alginate immo | 63.61 | - | literature: 10.1016/j.ijbiomac | ❓ |
| Phosphate | Ti₃C₂-MXene/Zr cross | 比表面积92.288 m²/g，形成Zr | - | literature: 10.1016/j.ijbiomac | ❓ |
|  | CA-MIL-53-AC (algina | DDT: 5.29, As(V): 4. | - | literature: 10.1016/j.ijbiomac | ❓ |
| Phosphate | Magnetic nanostructu | 1 mg-P/L: 96.1%, 10  | - | literature: 10.1016/j.ijbiomac | ❓ |
| Pb(II) | P-CNF-SA (porous cel | 318.47 | - | literature: 10.1016/j.molliq.2 | ❓ |
| Cr(VI) | chitosan/PAAS (polya | 7.7 | - | literature: 10.1007/s10924-021 | ❓ |
| U(VI) | chitosan/PVP (polyvi | 167 ± 25 | 6.0 | literature: 10.1007/s10924-021 | ❓ |
| ... | ... | ... | ... | ... | 共 43 条 |

## 5. 适用场景

**约束条件**：
- NH-SA-ZrBT对磷酸根的吸附容量和循环稳定性: 63.61 mg/g
- PASA水凝胶对铵氮的吸附-脱附循环稳定性: 9次循环后保持87%吸附容量 None
- SA-T/M₂固胺吸附剂对CO₂的循环稳定性: 2.10 mmol/g（30次循环后） mmol/g
- 再生循环性能: 5次循环后吸附率仍>80% %
- 海藻酸盐基吸附剂的再生性能: 多种再生体系：0.1 M HCl/0.05 M CaCl₂（5次循环Pb/Cu去除>70%/40%）、0.5 M HCl（4次循环）、1 M HNO₃（3次循环后损坏）、2 M NaCl（Cd/Hg/Pb再生）、0.5 M HNO₃（10次循环~70%容量） None
- 压缩循环稳定性: 50次循环(50%应变)后: CNF/SA-a应力保持率77.1%, 高度保持率83.56%; CNF/SA-b 60.6%/82.57%; CNF/SA-c 61.1%/81.97%; CNF/SA-c 10次循环后应力保持率85% %
- 循环吸油-挤出再生: 20次循环(50%压缩挤出)后仍保持吸附能力; 形状记忆功能→压缩后可恢复初始形状 None
- Mg–Al LDH–PVA/Alg stability: Deformation percentage = 7.8% (at 200 mg/L phosphate) percent
- Alg/a-FeOOH stability: Removal efficiency = 97.6% percent
- Phosphate species vs pH: H3PO4 (pH < 2), H2PO4- (pH 2–7), HPO42- (pH 7–11), PO43- (pH > 11) None

## 6. 相关原型

- cellulose-nanocrystal
- chitosan
- chlorella-cell-wall
- metal-organic-framework
- mussel-foot-adhesion

## 参考文献

[1] DOI: 10.1007/s10924-021-02312-1
[2] DOI: 10.1016/j.ijbiomac.2025.140801
[3] DOI: 10.1016/j.molliq.2020.115122
[4] 专利: CN109351339A
[5] 专利: CN117654453A
[6] 专利: CN119488883A
