# HANDOFF — 换设备续工作入口

> 最后更新：2026-06-08 01:15
> 当前分支：`feature/extraction-results`
> 最新 commit：`b6ab7df` (feat: Step 3 - 清理 chimera + 停放分离簇 + PDA/mussel 去重)

---

## 项目目标（一句话）

结构化 store 为正典、prototype.md 是视图、feature-mapping 三层匹配、ADRMATS **严格做吸附**。

## 当前进度

| 步骤 | 状态 | 说明 |
|------|------|------|
| Step 1: 自检 | ✅ 完成 | 36 原型，22 有数据，774 条 perf，0 verified |
| Step 2: 建校验脚本 | ✅ 完成 | validate_consistency.py (R10-R14) + check_chimera.py |
| Step 3: 清理 chimera + 停放分离簇 | ✅ 完成 | 分离簇停放 separation/，PDA/mussel 去重 |
| Step 4: 机制建模重构 | ⏳ 待启动 | 下一步 |
| Step 5: mussel 金标准 | ⏳ 待启动 | |

## 已定关键决定

1. **质量七条准则**：质量为上、可溯源、单一身份、unverified 不当事实、空白优于错配、有引用不等于可信、拿不准就问
2. **Gating 1**：超疏水/分离簇停放 `separation/`，标 `parked_separation`，从吸附匹配排除
3. **Gating 2**：PDA 与 mussel 分立，加 `inspired_by` / `material_realization` 互链，去重
4. **Gating 3**：核查用混合策略，verification 五级（verified/corroborated/single_source/unverified/needs_review）

## 当前在用计划

`docs/优化方案_v4.md`（也存在于 `.claude/plans/dynamic-dreaming-lighthouse.md`）

## 下一步任务

1. **Step 4**：机制建模重构
   - 修改 build_prototypes_db.py 支持新 schema（mechanisms + mechanism_instances + active_features）
   - 第一批：mussel-foot-adhesion、polydopamine-coating、metal-organic-framework（或 chitosan）
   - 分类机制（原理级 vs 实例级），实例级移入 mechanism_instances
   - 原理级去重 + 补 active_features

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

- `b6ab7df` feat: Step 3 - 清理 chimera + 停放分离簇 + PDA/mussel 去重
- `1c66310` docs: 创建 HANDOFF.md + 更新 README 状态
- `6223025` feat: 增强校验脚本 (R10-R14) + 新建 check_chimera.py
- `2656784` chore: 后处理流程 - 清理空值KI + 删除重复 + supplement补全 + 重建正典
- `2218d0a` feat: 完成26篇缺失论文提取 + 重建prototypes_db + 校验通过
