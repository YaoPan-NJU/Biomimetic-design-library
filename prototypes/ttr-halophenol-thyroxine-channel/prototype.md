---
id: ttr-halophenol-thyroxine-channel
name: 甲状腺素转运蛋白甲状腺素/卤酚结合通道（Transthyretin Thyroxine / Halophenol Binding Channel）
category: 动物
organism: Homo sapiens（人源甲状腺素转运蛋白 TTR）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 疏水性
adsorption_mechanisms:
  - 甲状腺素通道中酚羟基氢键锚簇与碘取代疏水容纳
  - 卤代酚与 PCB 羟基代谢物对 T4 通道的竞争性结合（内分泌干扰机制）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 甲状腺素转运蛋白甲状腺素/卤酚结合通道（Transthyretin Thyroxine / Halophenol Binding Channel）

## 1. 生物原型简介

**问题定义**：甲状腺素（T4）疏水且低溶解度，血浆需要专一载体将其从甲状腺运至靶组织。TTR（甲状腺素转运蛋白，旧称前白蛋白）以四聚体承担该转运功能，其识别卤代酚型激素的分子机制也是理解卤代芳香污染物甲状腺毒性的结构基础。

**生物策略**：人源 TTR 四聚体在二聚体-二聚体界面形成两条甲状腺激素通道。Wojtczak 等解析了人 TTR-T4 复合物晶体结构（PDB 2ROX，分辨率 2.0 Å）：T4（配体 T44）位于通道内，结合位点残基含 Lys15、Leu17、Glu54、Ala108、Ala109、Leu110（SITE AC2/AC3 记录）。Purkey 等解析了人 TTR 与 OH-PCB 代谢物（PCQ，3,5,3',5'-四氯联苯-4,4'-二醇）的复合物（PDB 2G5U）：两个 PCQ 分子分别占据两条通道（PCQ A 240 与 PCQ B 239），位点残基含 Lys15、Ser117、Thr119 极性锚簇与 Leu17/Ala108/Leu110 疏水壁，表明卤代酚型外源物以与 T4 相同的锚簇-口袋模式竞争性占据通道。Meerts 等体外竞争实验显示五氯苯酚、溴代酚及 PBDE 羟基代谢物与 T4 强力竞争结合人 TTR，印证'酚羟基 + 卤素取代'是通道识别的充分基序。

## 2. 吸附机制详解

### 机制1：甲状腺素通道中酚羟基氢键锚簇与碘取代疏水容纳

**描述**：人源 TTR 四聚体在二聚体-二聚体界面（AC/BD）形成两条甲状腺激素通道。在人 TTR-T4 复合物（PDB 2ROX）中，配体甲状腺素（T44，3,5,3',5'-四碘-L-甲状腺原氨酸）位于通道内，其结合位点（SITE AC2/AC3）含 Lys15、Leu17、Glu54、Ala108、Ala109、Leu110；在人 TTR-OH-PCB 复合物（PDB 2G5U）同一通道的位点（SITE AC1/AC2）中另见 Ser117、Thr119，Lys15/Ser117/Thr119 构成通道口酚羟基极性锚簇，Leu17/Ala108/Ala109/Leu110 疏水壁容纳碘取代
**关键官能团**：['阳离子/氢键给体锚簇（Lys15、Ser117、Thr119 侧链）', '疏水通道壁（Leu17、Ala108、Ala109、Leu110）']
**来源**：DOI 10.1107/S0907444996003046

### 机制2：卤代酚与 PCB 羟基代谢物对 T4 通道的竞争性结合（内分泌干扰机制）

**描述**：羟基化多氯联苯（OH-PCB）等卤代酚型外源物模拟 T4 的酚羟基 + 卤素取代模式，竞争性结合同一 TTR 通道并置换 T4，是既有文献记载的内分泌干扰分子机制。PDB 2G5U 示 OH-PCB 配体 PCQ（3,5,3',5'-四氯联苯-4,4'-二醇）同时占据两条通道（PCQ A 240 与 PCQ B 239），位点残基含 Lys15/Ser117/Thr119 锚簇与疏水壁
**关键官能团**：['酚羟基氢键锚簇（Lys15/Ser117/Thr119 型极性残基）', '卤素/疏水口袋（Leu17/Ala108/Leu110 型疏水壁）']
**来源**：DOI 10.1016/j.chembiol.2004.10.009

## 3. 结构特征与结构-功能关系

必须保留：① 通道口与酚羟基几何互补的阳离子/氢键给体锚簇（Lys15/Ser117/Thr119 型）；② 按形状容纳卤素取代联芳骨架的疏水口袋（Leu17/Ala108/Leu110 型）；③ 锚簇与口袋的预组织相对几何。可灵活调整：载体骨架、锚定基团化学（胍基/脲/硫脲/酰胺）、孔壁疏水与卤亲修饰程度、腔深与孔径。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 四级结构依赖: TTR 为血浆可溶性四聚体（单体约 13.9 kDa、128 残基），甲状腺激素通道由二聚体-二聚体界面围成；四聚体解离或蛋白变性使通道几何与锚簇排布丧失，用作吸附须固定化并维持通道构象 None
- 锚簇质子化状态依赖: 酚羟基锚定依赖 Lys15 ε-氨基等极性残基的质子化状态与氢键能力；极端 pH 下锚簇质子化改变将削弱酚羟基结合（定性，机理推断） None
- 模式识别非特异性: TTR 通道识别'卤代酚羟基'基序，不区分 T4、OH-PCB、卤代酚与 BPA 本身；对某一目标污染物的特异选择性须在材料设计层另行构建（如 BPA 双酚几何的二次约束） None

## 6. 相关原型

- cactus-spine
- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- errg-bpa-endocrine-receptor

## 参考文献

[待补充]
