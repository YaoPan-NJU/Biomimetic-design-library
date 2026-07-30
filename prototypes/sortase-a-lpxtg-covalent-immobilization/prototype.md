---
id: sortase-a-lpxtg-covalent-immobilization
name: Sortase A LPXTG 位点特异性共价固定转肽酶（Sortase A LPXTG Site-Specific Covalent Immobilization Transpeptidase）
category: 微生物
organism: Staphylococcus aureus（金黄色葡萄球菌 sortase A，SrtA，LPXTG 特异性转肽酶）
biomimetic_dimension: 分子仿生
features:
  - 位点特异性共价固定
adsorption_mechanisms:
  - LPXTG 分选基序在活性位裂谷的位点特异性识别
  - 活性位 Cys184 亲核转肽与氨基受体的共价锚定结点
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 1 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# Sortase A LPXTG 位点特异性共价固定转肽酶（Sortase A LPXTG Site-Specific Covalent Immobilization Transpeptidase）

## 1. 生物原型简介

**问题定义**：革兰氏阳性菌须将多种表面蛋白稳定展示于细胞壁以介导与宿主的相互作用。这些蛋白分泌后须被锚定于细胞壁肽聚糖，而非随机释放或随机偶联。金黄色葡萄球菌 sortase A（SrtA）承担这一任务：识别表面蛋白 C 端的 LPXTG 分选基序，并经转肽反应将蛋白共价连接于细胞壁肽聚糖交联桥。这是自然界中成熟且通用的位点特异性共价固定机制。本条目关注该机制作为'蛋白在固体表面取向化共价固定'工具的可转译性，而非 sortase A 对某一污染物的直接识别。

**生物策略**：金黄色葡萄球菌 sortase A 为β桶转肽酶。Zong 等测定了天然 SrtA（PDB 1T2P，ΔN59 催化域，残基 61-206）、活性位突变体及其与 LPETG 底物肽复合物（PDB 1T2W，C184A）的晶体结构：活性位以疏水接触定位 LPXTG 中高度保守的 Pro 与 Thr，X 位残基（LPETG 中为 Glu）指向溶剂（SITE AC3 记 LPETG 接触残基 Glu105/Ser116/Ile182/Arg197）。催化装置由 Cys184（亲核体）、His120、Arg197 组成：Thr-Gly 切割键置于 Cys184 与 Arg197 之间、远离 His120 咪唑鎓；Cys184 亲核攻击该键形成硫酯中间体，随后细胞壁肽聚糖五甘氨酸交联桥的氨基解离中间体，在底物蛋白 C 端 Thr 与细胞壁之间形成酰胺键，将蛋白共价锚定于细胞壁（摘要：surface proteins are covalently linked to the cell wall ... LPXTG motif）。PDB 1T2P 链 A 中 Cys184 为唯一半胱氨酸；1T2W 将该位突变为 Ala（SEQADV：ALA A 184 对应 UniProt Q9S446 CYS 184）以捕获 LPETG 底物，反向证明 Cys184 为野生型活性位亲核体。His120、Cys184、Arg197 在革兰氏阳性菌 sortase 中保守。

## 2. 吸附机制详解

### 机制1：LPXTG 分选基序在活性位裂谷的位点特异性识别

**描述**：金黄色葡萄球菌 sortase A 以β桶催化域的活性位裂谷识别底物表面蛋白 C 端的 LPXTG 五肽分选基序：高度保守的 Pro 与 Thr 经疏水接触被预组织定位，X 位残基（LPETG 中为 Glu）指向溶剂；PDB 1T2W（C184A 底物捕获突变体）中 LPETG 肽（链 D，Leu331-Pro332-Glu333-Thr334-Gly335）结合于 Glu105/Ser116/Ile182/Arg197 构成的口袋（SITE AC3），使 Thr-Gly 切割键摆向催化残基
**关键官能团**：['LPXTG 识别口袋残基（Ile182、Arg197、Glu105、Ser116）', '疏水接触面（识别 LPXTG 保守 Pro/Thr）']
**来源**：DOI 10.1074/jbc.M401374200

### 机制2：活性位 Cys184 亲核转肽与氨基受体的共价锚定结点

**描述**：活性位 Cys184 硫醇盐亲核攻击 LPXTG 的 Thr-Gly 肽键，形成硫酯（thioacyl）中间体；天然条件下细胞壁肽聚糖五甘氨酸交联桥的氨基亲核解离该中间体，在底物蛋白 C 端 Thr 与细胞壁之间形成酰胺键，将表面蛋白共价锚定于细胞壁。催化装置 Cys184（亲核体）、His120、Arg197 在革兰氏阳性菌 sortase 中保守；Thr-Gly 切割键置于 Cys184 与 Arg197 之间、远离 His120 咪唑鎓（PDB 1T2W）
**关键官能团**：['活性位亲核半胱氨酸 Cys184', '催化残基 His120、Arg197', 'β桶催化域骨架']
**来源**：DOI 10.1074/jbc.M401374200

## 3. 结构特征与结构-功能关系

必须保留：① 识别短肽标签 LPXTG 的活性位裂谷（保守 Pro/Thr 经疏水接触定位，X 位可变并暴露溶剂）；② 以活性位半胱氨酸（Cys184）为亲核体的转肽催化装置（Cys184/His120/Arg197），形成可被外源氨基解离的硫酯中间体；③ 以共价酰胺结点完成不可逆锚定。可灵活调整：氨基受体由天然细胞壁肽聚糖替换为人工载体表面手柄（伯胺/甘氨酸/五甘氨酸），标签蛋白的种类与其识别功能（含 PFOA 识别蛋白）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶催化域形态: sortase A 全长 206 aa 含 N 端跨膜段；工程使用 ΔN59/Δ59 可溶催化域（残基约 61/62-206，约 16.4 kDa），需重组表达纯化后使用 None
- 酶身份与活性单位门（SORTASE-ID-01）: 冻结 S. aureus sortase A Δ59-His6；SDS-PAGE 纯度≥90%、intact LC-MS 与理论质量相差≤0.02%；定义 1 U 为 25 °C、pH 7.5 下每分钟生成 1 nmol 转肽产物，水解不计活性；任一身份字段缺失禁止固定化 None
- 转肽对水解的化学选择性门: 以同一 LPETG/甘氨酸底物测定，转肽/水解摩尔比须≥10 None
- 共价结点验证门: 靶向 LC-MS/MS 须检出跨结点 LPET-GGGK 肽并量化水解副产物；8 M 尿素 + 1 M NaCl 室温 1 h 变性/竞争洗涤后共价蛋白保留须≥90%；结点不可检出、水解/非特异吸附主导或酶残留超限即整批报废 None
- 取向/活性增量不自动成立: 生物来源不证明 C 端单点共价固定优于随机固定，故不以固定方式本身主张取向增量；取向与活性增量须由随机偶联对照（B-RAND，仅作可选探索）、单位固定蛋白活性分数 factive 与失活对照（如 D56N）分别验证 None
- Ca2+ 依赖与酶残留清除: sortase A 转肽需 Ca2+（工程反应液 50 mM Tris、150 mM NaCl、10 mM CaCl2、pH 7.5、25 °C）；酶为可溶 His6 融合体，反应后须经 Ni-NTA 清除至 sortase 特征肽低于方法定量限 None

## 6. 相关原型

[待补充]

## 参考文献

[待补充]
