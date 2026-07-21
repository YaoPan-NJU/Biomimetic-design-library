---
id: fcrn-ph-dependent-fc-recycling
name: 新生 Fc 受体 FcRn pH 依赖结合-释放回收（Neonatal Fc Receptor (FcRn) pH-Dependent Binding-Release Recycling）
category: 动物
organism: Rattus norvegicus（大鼠新生 Fc 受体 FcRn/FCGRT，MHC I 类相关受体，与 β2-微球蛋白结合，识别 IgG Fc）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - pH 响应
adsorption_mechanisms:
  - 组氨酸质子化介导的 pH 门控可逆结合-释放（分子开关）
  - 内体-循环 pH 双区室回收循环（吸附-再生循环原型）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 4 papers, 9 verified, 0 unverified
# coverage: partial
# status: active
---
# 新生 Fc 受体 FcRn pH 依赖结合-释放回收（Neonatal Fc Receptor (FcRn) pH-Dependent Binding-Release Recycling）

## 1. 生物原型简介

**问题定义**：新生哺乳动物需从初乳选择性吸收母源 IgG，并保护 IgG 免于溶酶体分解代谢以维持长血清半衰期。受体如何在酸性内体捕获 IgG、又在中性血液释放，实现可逆结合-释放的回收循环，是分子识别与动态响应的基础问题。

**生物策略**：新生 Fc 受体 FcRn（MHC I 类相关，与 β2-微球蛋白结合）以 pH 依赖方式识别 IgG Fc 的 Cγ2-Cγ3 界面（PDB 1I1A，2.8 Å 大鼠 FcRn/异二聚 Fc 复合物，标题 'CRYSTAL STRUCTURE OF THE NEONATAL FC RECEPTOR COMPLEXED WITH A HETERODIMERIC FC'；PDB 1FRT，大鼠 FcRn-Fc 复合物，Burmeister 1994）。该界面两侧分布可滴定组氨酸：IgG Fc His310、His433 位于 CH2-CH3 交界，FcRn 重链 His250、His251（Raghavan 1995）。酸性内体（pH 6.0-6.5）下组氨酸质子化形成可滴定盐桥，高亲和结合；中性血液（pH 7.0-7.5）下去质子化、盐桥断裂，亲和力下降约两个数量级并释放（Raghavan 1995 SPR；Martin 2001 揭示三个 confer pH 依赖结合的可滴定盐桥）。功能上，FcRn 作为 β2-微球蛋白依赖性保护受体，在胞吞空泡结合 IgG 并重定向回循环，保护 IgG 免于溶酶体分解代谢（Junghans & Anderson 1996），从而延长血清半衰期。

## 2. 吸附机制详解

### 机制1：组氨酸质子化介导的 pH 门控可逆结合-释放（分子开关）

**描述**：FcRn 经其 α2 与 β2-微球蛋白结构域界面识别 IgG Fc 的 Cγ2-Cγ3 界面；该界面两侧分布可滴定组氨酸（IgG Fc His310、His433 位于 CH2-CH3 交界，FcRn 重链 His250、His251）。酸性内体（pH 6.0-6.5）下组氨酸质子化形成可滴定盐桥，高亲和结合 Fc；中性血液（pH 7.0-7.5）下去质子化、盐桥断裂，亲和力下降约两个数量级并释放 Fc，构成 pH 门控的结合-释放分子开关
**关键官能团**：['可滴定组氨酸（咪唑基，质子化盐桥）', '酸性残基（Asp/Glu，盐桥对侧）', 'α2/β2-微球蛋白界面']
**来源**：DOI 10.1021/bi00045a005

### 机制2：内体-循环 pH 双区室回收循环（吸附-再生循环原型）

**描述**：FcRn 作为 β2-微球蛋白依赖性保护受体，在胞吞空泡（酸性）结合 IgG，将其重定向回循环、避免溶酶体分解代谢；饱和时未结合 IgG 进入溶酶体降解。酸性内体结合、中性血液释放的 pH 依赖门控驱动 IgG 回收循环并延长血清半衰期
**关键官能团**：['可滴定组氨酸（pH 门控回收）', 'β2-微球蛋白依赖性受体界面']
**来源**：DOI 10.1073/pnas.93.11.5512

## 3. 结构特征与结构-功能关系

必须保留：① 含 pKa 落于捕获 pH 与再生 pH 之间的可滴定基团（天然为组氨酸咪唑基）；② 质子化态形成、去质子化态断裂的可逆盐桥/氢键相互作用；③ 捕获 pH（酸性）与再生 pH（中性）之间的双区室 pH 摆动。可灵活调整：载体骨架、可滴定基团种类与排布、识别内核（针对具体靶标的结合位点）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 膜受体/可溶形态与三级结构依赖: FcRn 为与 β2-微球蛋白非共价结合的 I 型 MHC I 类相关受体，其 pH 门控识别依赖完整 α2/β2-微球蛋白三级结构界面；用作吸附须将识别界面移植/固定于固体载体 None
- pH 摆动幅度决定脱附: 结合-释放需跨越约 pH 6.0→7.0 区间（亲和力变化约两个数量级）；再生阶段 pH 摆动幅度直接决定吸附-脱附循环效率 pH
- 区室化/操作模式依赖: 天然回收依赖酸性内体-中性血液双区室与胞吞-再循环途径；体外须以批次 pH 摆动或双区室流动操作复现捕获-再生循环 None

## 6. 相关原型

- hsa-fatty-acid-pfas-binding
- kcsa-potassium-channel-selectivity-filter
- lanmodulin-lanthanide-coordination
- ntcp-bile-acid-pfas-transporter
- psts-phosphate-binding-protein

## 参考文献

[待补充]
