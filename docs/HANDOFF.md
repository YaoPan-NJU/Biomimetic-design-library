# HANDOFF — 换设备续工作入口

> 最后更新：2026-06-08 08:15
> 当前分支：`feature/extraction-results`
> 最新 commit：`9495f3a` (feat: MOF 金标准验证 - pollutant 补全 + verification 状态更新)

---

## 项目目标（一句话）

结构化 store 为正典、prototype.md 是视图、feature-mapping 三层匹配、ADRMATS **严格做吸附**。

## 当前进度

| 步骤 | 状态 | 说明 |
|------|------|------|
| Step 1: 自检 | ✅ 完成 | 36 原型，22 有数据，774 条 perf，0 verified |
| Step 2: 建校验脚本 | ✅ 完成 | validate_consistency.py (R10-R14) + check_chimera.py |
| Step 3: 清理 chimera + 停放分离簇 | ✅ 完成 | 分离簇停放 separation/，PDA/mussel 去重 |
| Step 4: 机制建模重构 | ✅ 完成 | 第一批 (mussel/PDA/MOF) 已重构 |
| Step 5: 金标准验证 | ⏳ 进行中 | MOF 验证完成：236 条 pending_manual_check, 16 条 needs_review |

## 已定关键决定

1. **质量七条准则**：质量为上、可溯源、单一身份、unverified 不当事实、空白优于错配、有引用不等于可信、拿不准就问
2. **Gating 1**：超疏水/分离簇停放 `separation/`，标 `parked_separation`，从吸附匹配排除
3. **Gating 2**：PDA 与 mussel 分立，加 `inspired_by` / `material_realization` 互链，去重
4. **Gating 3**：核查用混合策略，verification 五级（verified/corroborated/single_source/unverified/needs_review）

## 当前在用计划

`docs/优化方案_v4.md`（也存在于 `.claude/plans/dynamic-dreaming-lighthouse.md`）

## 下一步任务

1. **人工核查 MOF 的 236 条数据**（开 PDF 确认数值）
   - 有 28 个唯一 DOI，29 个唯一 source_file
   - 每条需确认：数值在 PDF 指定页/表出现、材料、污染物、条件一致
   - 通过 → 标 verified，不通过 → 标 needs_review 或删除

2. **处理 16 条 needs_review**（无 pollutant/无 DOI/通用比较）

3. **其余 4 个金标准验证**（chitosan, alginate, cellulose-nanocrystal, starch-granule）

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `tools/validate_consistency.py` | 校验脚本（14 条规则）|
| `tools/check_chimera.py` | chimera 检测 |
| `tools/build_prototypes_db.py` | 构建正典 |
| `prototypes_db/` | 正典数据（36 个 JSON）|
| `feature-mapping.json` | 四层映射 |
| `docs/优化方案_v4.md` | 当前计划 |

## 怎么续上

先读 `docs/优化方案_v4.md`，再做 Step 3。

## 已知问题

- 774 条性能数据全部 unverified
- 511 个校验警告（主要是 R14 机制含实例级数据）
- 5 个 chimera 原型需清理
- 12 个有数据原型未进 pollutant_prototype_map

## 最近 Changelog

- `9495f3a` feat: MOF 金标准验证 - pollutant 补全 + verification 状态更新
- `cc1b89d` docs: 更新 HANDOFF.md - MOF 核查脚本完成
- `58a29f6` feat: Step 5 - 金标准核查脚本 + MOF 核查报告
- `a42ab53` docs: 更新 HANDOFF.md - mussel 无数据，改用 MOF 作为金标准
- `0f96073` feat: Step 5 准备 - mussel 清理 + 标 needs_literature
