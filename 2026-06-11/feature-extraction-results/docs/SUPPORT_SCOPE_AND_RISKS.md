# 支持范围与风险

> 版本：v1.1
> 日期：2026-06-08

---

## 1. 当前支持范围

### 1.1 污染物支持

| 类别 | 数量 | 说明 |
|------|------|------|
| 有分子特征画像 | 25 | 详见 pollutant_profiles.json |
| 有别名映射 | 28 | 详见 pollutant_aliases.json |
| 有 direct evidence | 15+ | 详见 pollutant_prototype_map |

**支持的污染物类型**：
- 重金属：Pb(II), Cd(II), Hg(II), Cu(II), Cr(VI), As(V), As(III), U(VI), Zn(II), Ni(II)
- PFASs：PFOA, PFOS
- 内分泌干扰物：BPA
- 抗生素：SMX, TC, CIP
- 卤代烃：TCE
- 染料：MB, MO, RhB, CR, CV, MG
- 无机非金属：PO₄³⁻, NH₄⁺, NO₃⁻, F⁻

### 1.2 原型支持

| 类别 | 数量 | 说明 |
|------|------|------|
| 能出 brief | 13 | 有性能数据 + 机制 + 设计转译 |
| 有 direct evidence | 25+ | 在 pollutant_prototype_map 中 |

**能出 brief 的原型**：
- 金标准（5）：MOF, Chitosan, Alginate, CNC, Starch
- 新验收（8）：bone-structure, chlorella-cell-wall, diatom-frustule, lobster-exoskeleton, mycelium, oyster-shell, silk-fibroin, wood-xylem

### 1.3 匹配模式

| 模式 | 说明 | 标记 |
|------|------|------|
| direct_pollutant_evidence | 有直接实验数据 | direct_evidence=true |
| molecular_feature_inference | 基于分子特征推断 | direct_evidence=false |
| mechanism_feature_bridge | 基于机制-特征桥接 | direct_evidence=false |

---

## 2. 不支持的范围

### 2.1 污染物

- 超出 25 个画像的污染物（需要新增 pollutant_profiles.json）
- 未知污染物（返回 llm_inference 默认画像）

### 2.2 原型

- 18 个不能出 brief 的原型：
  - 低覆盖（5）：cell-membrane-ion-channel, fish-scale-hydroxyapatite, mangrove-root, pitcher-plant-slippery-surface, polydopamine-coating
  - 需补文献（5）：coral-skeleton, magnetic-bacteria, namib-beetle, plant-tannin, sulfate-reducing-bacteria
  - 需补文献（8）：biomineralization-template, diatom-inspired-porous, dna-aptamer, iron-oxidizing-bacteria, mussel-foot-adhesion, scallop-shell, silkworm-silk, spider-silk

### 2.3 数据

- verified 数据（需开 PDF 核实）
- 实时水质数据
- 动态权重调整

---

## 3. 未验证风险

### 3.1 高风险

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| verified=0 | 所有性能数据未经开 PDF 核实 | 标记为 single_source/unverified |
| 191 条缺 pollutant | 无法按污染物匹配 | 标记为 needs_review |

### 3.2 中风险

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| 196 个 R14 警告 | 机制含实例级数据 | 不影响匹配，但需清理 |
| 602 条缺 active_features | 无法精细桥接 | 不影响基本匹配 |

### 3.3 低风险

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| 5 个断链原型 | 分离簇原型已停放 | 不影响吸附匹配 |
| 1 个 chimera 已修复 | polydopamine-coating | 已删除不相关机制 |

---

## 4. 质量保证

### 4.1 验收脚本

```bash
# 运行验收
python tools/verify_adrmats_delivery.py

# 验证校验
python tools/validate_consistency.py
python tools/check_chimera.py
```

### 4.2 验收标准

- ✅ PFOA/SMX/BPA 必须 direct_evidence=false
- ✅ Pb(II) 可以 direct_evidence=true
- ✅ validate_consistency.py: 0 error
- ✅ check_chimera.py: 0 violation
- ✅ 所有 brief 由接口真实生成

---

## 5. 后续改进

### 5.1 短期（v0.2）

- 补充更多污染物画像
- 清理 R14 警告
- 补充 active_features

### 5.2 中期（v1.0）

- 开 PDF 核实 verified 数据
- 扩展到 100 个原型
- 实现动态权重调整

### 5.3 长期

- 实时水质数据接入
- 机器学习优化匹配

---

*本文档描述当前支持范围和已知风险。*
