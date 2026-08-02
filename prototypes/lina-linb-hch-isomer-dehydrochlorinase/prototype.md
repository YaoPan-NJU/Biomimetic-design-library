---
id: lina-linb-hch-isomer-dehydrochlorinase
name: LinA/LinB HCH 异构体脱氯化氢酶/水解脱卤酶（LinA/LinB HCH-Isomer Dehydrochlorinase/Haloalkane Dehalogenase）
category: 微生物
organism: Sphingobium japonicum UT26 / Sphingobium indicum B90A
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 几何识别
  - 催化降解
adsorption_mechanisms:
  - LinA 脱氯化氢酶对轴向氯的几何要求（β-HCH 全平伏氯→无活性）
  - LinB 水解脱卤酶对平伏 C-Cl 键的亲核取代（β-HCH 可被水解）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: medium
# provenance: 3 papers, 0 verified, 3 unverified
# coverage: partial
# status: active
---
# LinA/LinB HCH 异构体脱氯化氢酶/水解脱卤酶

## 1. 生物原型简介

**问题定义**：HCH 异构体（α/β/γ/δ）仅氯取向不同，β-HCH（全平伏氯）是最稳定/最持久的异构体。

**生物策略**：LinA（Okai 2010）要求 C-Cl 键轴向取向（E2 消除），β-HCH 全平伏氯不被催化；LinB（Okai 2013, PDB 4H77/1D07）以 SN2 水解平伏 C-Cl，可攻击 β-HCH。两酶组合提供完整的轴向/平伏氯几何区分判据。

## 2. 可转译原则

catalytic_function_translated_as_recognition_only：轴向 C-Cl 的 σ* 朝分子外侧（可被卤键受体接近），平伏 C-Cl 朝赤道（不易接近）；设计材料可以"轴向氯可及性"为判据区分 HCH 异构体。

## 3. 来源

- Okai 2010 (J Mol Biol, 被引 55)
- Okai 2013 (J Bacteriol, PMC3676048, PDB 4H77/1D07, 被引 36)
- Geueke 2013 (被引 54)
