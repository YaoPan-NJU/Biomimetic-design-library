# 支持范围与风险

> 版本：v2.0
> 日期：2026-06-15
> 分支：`opt/curation-grounding-v1`

---

## 1. 本库定位

本库是 ADRMATS（水处理仿生吸附材料开发智能体系统）的**仿生启发检索模块**。

- **本库能做**：把需求转成 `BiomimeticDesignBrief`，告诉下游可以借鉴哪些生物原型、靠什么机制、可转译成什么材料设计思路。
- **本库不做**：不直接设计材料，不做材料性能预测，不做工程放大。

---

## 2. 当前支持范围

### 2.1 数据统计（Phase 0–8 完成后）

| 指标 | 数值 | 说明 |
|------|------|------|
| active 原型（参与检索）| 24 | 有因果链卡 + 设计转译 |
| materials_reference（降级）| 4 | MOF / 纤维素纳米晶 / 淀粉 / 海藻酸盐 |
| parked（超范围）| 1 | namib-beetle（集水，非吸附）|
| 机制总数 | 534 | |
| 因果链卡（合格）| 28 张 | 覆盖 24/24 原型 |
| PDF 已核验 verified | 23 张 | 22 机制 + 1 翻译 |
| boundary_conditions | 62 条 | 覆盖所有 24 个 active 原型 |
| 硬 DO-NOT | **0 条** | 边界尚未从 PDF 逐条核验 |
| 软 caution | **62 条** | 全部为定性描述 |
| 校验错误 / chimera 违规 | 0 / 0 | |

### 2.2 支持的污染物

| 类别 | 数量 | 说明 |
|------|------|------|
| 有分子特征画像 | 25 | 详见 pollutant_profiles.json |
| 有别名映射 | 28 | 详见 pollutant_aliases.json |
| 有 direct evidence | 15+ | 详见 pollutant_prototype_map |

**支持的污染物类型**：
- 重金属：Pb(II), Cd(II), Hg(II), Cu(II), Cr(VI), As(V), U(VI)
- PFASs：PFOA, PFOS
- 内分泌干扰物：BPA
- 抗生素：SMX, TC, CIP
- 染料：MB, MO, RhB, CR
- 无机非金属：PO₄³⁻, NH₄⁺, NO₃⁻, F⁻

### 2.3 匹配模式

| 模式 | 说明 | 标记 |
|------|------|------|
| `direct_pollutant_evidence` | 有直接实验数据 | `direct_evidence=true` |
| `molecular_feature_inference` | 基于分子特征推断 | `direct_evidence=false` |

### 2.4 边界输出

brief 中的 `rule_based_cautions` 字段包含两种边界：

| 类型 | 字段 | 当前数量 | 说明 |
|------|------|----------|------|
| 硬 DO-NOT | `do_not` | **0** | 可参与门控排序，需 `basis=from_source` + `verification=verified` |
| 软 caution | `cautions` | **62** | 只提示，不门控，全部为 `llm_inferred` 定性描述 |

> ⚠️ **当前没有硬 DO-NOT**。所有边界条件均为 B 档（机理推理 + 复用库内资产），未从 PDF 中逐条核验。如需硬约束，需学生下载文献后按 A 档核验。

---

## 3. 不支持的范围

### 3.1 污染物

- 超出 25 个画像的污染物（需新增 `pollutant_profiles.json`）
- 未知污染物（返回 `llm_inference` 默认画像）
- Boron、Co(II) 为策展后仅有的两个 direct-evidence 真缺口

### 3.2 原型

- **parked**（1 个）：namib-beetle（集水，非吸附范围）
- **materials_reference**（4 个）：MOF、纤维素纳米晶、淀粉、海藻酸盐（非仿生，降级不检索）

### 3.3 数据

- 实时水质数据（不支持）
- 动态权重调整（不支持）
- 工程放大预测（不支持）

---

## 4. 已知风险

### 4.1 高风险

| 风险 | 影响 | 当前状态 | 缓解 |
|------|------|----------|------|
| 0 hard DO-NOT | 无法门控"在目标工况下会失效"的材料 | Phase 8 已识别 | 需从 PDF 逐条摘取边界，学生下载文献后核验 |
| 5 个原型无对口 PDF | coral/magnetic-bacteria/pitcher-plant/lobster/spider-silk 的边界为 placeholder | `literature-requests.md` 已写 8 条检索请求 | 待学生下载后按 A 档核验 |

### 4.2 中风险

| 风险 | 影响 | 当前状态 | 缓解 |
|------|------|----------|------|
| 512/534 机制仍为 needs_review | 大部分机制未经 PDF 逐条核验 | Phase 6 核验了 23 张 | 需持续核验 |
| needs_review 可进入候选 | 低置信候选仍会出现（标记 `confidence: low`）| Phase 7.5 已修复排序 | 不影响高置信候选 |

### 4.3 低风险

| 风险 | 影响 | 当前状态 | 缓解 |
|------|------|----------|------|
| silk-fibroin 重复机制 | 两个同名"吸附机制"带重复 BC | pre-existing | 后续清理 |
| 193 条 validate_consistency 警告 | 非关键警告 | 预存在 | 不影响功能 |

---

## 5. 验收命令

```bash
# 全套验收
python -X utf8 tools/verify_adrmats_delivery.py      # 6/6 PASS
python -X utf8 tools/test_interface_honesty.py        # 3/3 PASS
python -X utf8 tools/check_boundary_guardrail.py      # 8 项全绿
python -X utf8 tools/export_do_not.py                 # 导出 62 条
python -X utf8 tools/check_causal_chain.py            # 28/28 合格卡
python -X utf8 tools/check_translation_specificity.py # 25/25 合格
python -X utf8 tools/check_chimera.py --strict        # 0 违规
python -X utf8 tools/validate_consistency.py          # 0 error
python -X utf8 tools/check_repo_hygiene.py            # 治理检查
```

---

## 6. 后续改进路径

### 短期

- 学生下载 8 篇文献 → 按 A 档核验 → 升级为 hard DO-NOT
- 仓库治理已修复（`check_repo_hygiene.py` PASS），后续需保持合规
- 清理 silk-fibroin 重复机制

### 中期

- 从 PDF 逐条摘取更多 verified 边界
- 扩展到更多污染物画像
- ADRMATS 侧集成 `query()` 接口

---

*本文档描述当前支持范围和已知风险。数据截止 2026-06-15，分支 `opt/curation-grounding-v1`。*
