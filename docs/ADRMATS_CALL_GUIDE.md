# ADRMATS 调用说明

> 版本：v0.1
> 日期：2026-06-08
> 状态：已验收

---

## 1. 快速开始

```python
from tools.biomimetic_context import BiomimeticContext

# 初始化
ctx = BiomimeticContext()

# 查询
result = ctx.query(
    pollutant="Pb(II)",
    water_quality={"pH": 6.0, "temperature": 25, "salinity": "low"},
    engineering_constraints=["水稳定性", "可回收性"]
)

# 获取 brief
brief = result['brief']
```

---

## 2. 接口说明

### 2.1 query() 方法

**参数**：
- `pollutant` (str): 污染物名称，支持别名自动归一
- `water_quality` (dict): 水质条件
  - `pH` (float): pH 值
  - `temperature` (float): 温度 (°C)
  - `salinity` (str): 盐度 ("low", "medium", "high")
- `engineering_constraints` (list): 工程约束列表

**返回**：
```json
{
  "brief": {
    "context": {},
    "candidates": [],
    "honesty_ledger": {}
  }
}
```

### 2.2 污染物别名支持

以下别名会自动归一到 canonical name：

| 输入 | 归一到 |
|------|--------|
| Pb(II), Pb²⁺, Pb2+, Pb, lead ion | Pb(II) |
| Cd(II), Cd²⁺, Cd2+, Cd | Cd(II) |
| Hg(II), Hg²⁺, Hg2+, Hg | Hg(II) |
| PFOA, Perfluorooctanoic acid, 全氟辛酸 | PFOA |
| SMX, Sulfamethoxazole, 磺胺甲恶唑 | SMX |
| BPA, Bisphenol A, 双酚A | BPA |

详见 `pollutant_aliases.json`

---

## 3. 输出结构

### 3.1 brief.context

```json
{
  "water_quality": {"pH": 6.0, "temperature": 25, "salinity": "low"},
  "removal_target": {"污染物": "Pb(II)"},
  "pollutant_profile": {
    "canonical_name": "Pb(II)",
    "pollutant_class": "重金属",
    "molecular_features": ["二价阳离子", "软酸", "高电荷密度"],
    "likely_interactions": ["配位", "静电吸引", "离子交换"],
    "profile_basis": "database"
  },
  "engineering_constraints": ["水稳定性"]
}
```

### 3.2 brief.candidates[]

```json
{
  "prototype_id": "chitosan",
  "organism": "Crustacea",
  "match": {
    "reason": "壳聚糖对Pb(II)有直接实验数据",
    "weight": 0.80,
    "applicability_fit": "pH 3-9, 温度 0-80°C",
    "match_basis": "direct_pollutant_evidence",
    "direct_evidence": true
  },
  "mechanism": {
    "name": "氨基/羟基配位吸附",
    "基本原理": "壳聚糖的氨基和羟基可与Pb(II)形成配位键",
    "key_structures": ["氨基", "羟基"],
    "functional_groups": ["-NH₂", "-OH"],
    "molecular_feature_links": ["Pb(II)的软酸特性与氨基的软碱特性匹配"],
    "attribution": {
      "source": "literature",
      "ref": "DOI",
      "verification_tier": "single_source"
    }
  },
  "design_translation": {
    "idea": "采用壳聚糖为基体，通过交联提高机械强度",
    "material_realization_examples": [],
    "source_tier": "literature"
  },
  "evidence_context": {
    "performance_leads": []
  }
}
```

### 3.3 brief.honesty_ledger

```json
{
  "facts": ["有 10 个原型对 Pb(II) 有直接实验数据"],
  "leads": ["chitosan: 有直接实验数据，但未经独立核实"],
  "inferences": ["alginate: 基于分子特征推断，非直接证据"]
}
```

---

## 4. 匹配逻辑

### 4.1 Direct Evidence（直接证据）

当污染物在 `pollutant_prototype_map` 中有记录时，返回 `direct_evidence=true`。

**当前支持 direct evidence 的污染物**：
- 重金属：Pb(II), Cd(II), Hg(II), Cu(II), Cr(VI), As(V), U(VI)
- 染料：MB, MO, RhB, CR
- 其他：PO₄³⁻, NH₄⁺, NO₃⁻

### 4.2 Feature-based Inspiration（特征推断）

当污染物没有直接证据时，基于分子特征匹配：

**匹配规则**：
- 分子特征 → 原型（如"芳香环" → polydopamine-coating）
- 相互作用 → 原型（如"配位" → chitosan, alginate）
- 污染物类别 → 原型（如"重金属" → chitosan, alginate）

**当前支持的分子特征**：
- 芳香环、疏水性、羧酸基团、酚羟基
- 长链全氟烷基、二价阳离子、软酸
- 正电荷、负电荷、磺酰胺基、酰胺基

详见 `feature_matching_rules.json`

---

## 5. 验证等级

### 5.1 verification_tier

| 等级 | 含义 | 说明 |
|------|------|------|
| verified | 已验证 | 开 PDF 确认数值存在 |
| corroborated | 已印证 | ≥2 个独立来源 |
| single_source | 单一来源 | 有 ref，未开 PDF |
| unverified | 未验证 | 有 source，未建立接地 |
| needs_review | 待审查 | 存在缺陷 |

### 5.2 source_tier

| 等级 | 含义 |
|------|------|
| literature | 来自文献 |
| llm_inference | LLM 外推 |

---

## 6. 当前支持范围

### 6.1 支持

- 25 个污染物的分子特征画像
- 28 个污染物的别名归一
- 13 个原型能出 brief
- direct evidence 和 feature-based inspiration 两种匹配模式
- honesty_ledger 区分事实、线索、推断

### 6.2 不支持

- 需要开 PDF 核实的 verified 数据
- 超出 25 个污染物画像的污染物
- 超出 13 个原型的候选

### 6.3 未验证风险

- verified=0，所有性能数据未经开 PDF 核实
- 196 个警告（主要是 R14 机制含实例级数据）

---

## 7. 示例查询

### 7.1 PFOA 查询

```python
result = ctx.query(
    pollutant="PFOA",
    water_quality={"pH": 7, "temperature": 25, "salinity": "medium"},
    engineering_constraints=["水稳定性", "可再生", "低二次污染"]
)
# 返回：7 个候选，全部 direct_evidence=false
```

### 7.2 Pb(II) 查询

```python
result = ctx.query(
    pollutant="Pb(II)",
    water_quality={"pH": 6, "temperature": 25, "salinity": "low"},
    engineering_constraints=[]
)
# 返回：10 个候选，部分 direct_evidence=true
```

---

## 8. 文件清单

| 文件 | 用途 |
|------|------|
| `tools/biomimetic_context.py` | ADRMATS 接口 |
| `pollutant_profiles.json` | 污染物画像 |
| `pollutant_aliases.json` | 污染物别名 |
| `feature_matching_rules.json` | 匹配规则 |
| `feature-mapping.json` | 原型-污染物映射 |
| `prototypes_db/` | 正典数据 |
| `tools/verify_adrmats_delivery.py` | 验收脚本 |
| `examples/adrmats_briefs/` | 示例 brief |

---

*本文档是 ADRMATS 调用的唯一说明。*
