# Biomimetic Design Library — 全面盘点报告

> QoderWork 替代 Codex 角色后的首次全量盘点 | 2026-06-17

---

## 一、项目总体健康度

| 指标 | 数值 | 备注 |
|---|---|---|
| JSON 文件解析 | 58/58 | 0 错误，132 warnings |
| active 原型 | 24 | + 4 materials_reference + 5 separation + 1 parked |
| 决策队列 pending_yao | **0** | Tasks 46-51 已全部清零 |
| 决策队列 resolved | 136 | 另有 10 项 deferred 至 v0.2 |
| 边界寄存器 | 105 条 | 45 applied / 14 guard / 38 gap / 8 approved-unapplied |

**好消息**：Claude Code 在第 11 轮（Tasks 46-51）完成了决策队列清零，chiptosan 14 行 Aramesh2021 引文、alginate 27 行 Dong2025 引文、silk-fibroin 工程约束验证均已提交。验证脚本 chimera check 通过，build 也成功跑过。

---

## 二、验证覆盖率（核心差距）

这是当前最大的短板。所有性能行零 verified，绝大多数机制停在 needs_review。

### 2.1 机制（mechanisms）— 主 24 原型

| 验证状态 | 数量 | 占比 |
|---|---:|---:|
| verified | 16 | 3.0% |
| needs_review | 412 | 77.7% |
| unverified | 101 | 19.1% |
| partial | 1 | 0.2% |
| **合计** | **530** | |

Top 5 机制大户：chitosan (132)、fish-scale (89)、mussel-foot (88)、PDA-coating (65)、spider-silk (31)

**14 个原型零 verified 机制。**

### 2.2 性能数据（performance_data）— 主 24 原型

| 验证状态 | 数量 | 占比 |
|---|---:|---:|
| **verified** | **0** | **0.0%** |
| unverified | 361 | 86.2% |
| needs_review | 42 | 10.0% |
| partial | 16 | 3.8% |
| **合计** | **419** | |

Top 5 性能行大户：chitosan (117)、PDA-coating (44)、mussel-foot (43)、diatom-frustule (42)、fish-scale (29)

**全库零 verified 性能行**——这是与 ADRMATS 对接的最大信任瓶颈。

### 2.3 零性能行原型（5 个）

| 原型 | 状况 |
|---|---|
| biomineralization-template | 空 enrichment |
| coral-skeleton | 空 enrichment，无本地 PDF |
| dna-aptamer | 有 1 条机制但无性能 |
| magnetic-bacteria | 空 enrichment |
| sulfate-reducing-bacteria | 有 1 条机制但无性能 |

### 2.4 Enrichment 因果链

| 指标 | 数值 |
|---|---|
| 总 enrichment 条目 | 478 |
| causal_chain 已填充 | **1**（dna-aptamer） |
| causal_chain 空 | 477（99.8%） |
| 空 {} enrichment 文件 | 3（biomineralization / coral / magnetic-bacteria） |

---

## 三、剩余工作分类

### 类别 A：已审批但未写入 JSON 的边界规则（8 项）

需要定向写入 JSON 的 `engineering_constraints` 或添加 scope caveat。

| 边界 ID | 原型 | 类型 | 待执行操作 |
|---|---|---|---|
| B01-CHI-002 | chitosan | soft_boundary | 写 pH 5 Cu 吸附约束到 engineering_constraints |
| B01-PDA-003 | PDA-coating | hard_do_not | 移除 enrichment 中残留的疏水膜/抗菌综述机制 |
| B03-CHL-001 | chlorella | hard_do_not | 移除 Cheng2021 Pb2+ 错误机制 |
| B03-CMIC-001 | cell-membrane | soft_boundary | 添加 scope caveat "separation/desalination, not adsorption" |
| B04-SHART-003 | superhydrophobic/lotus | soft_boundary | CN114874407A TiO2/氟硅烷海绵行归属决策 |
| B05-MATREF-001 | materials_ref 集合 | soft_boundary | 添加 review-table 归一化 caveat |
| B07-REG-002 | namib-beetle | soft_boundary | 标注 "generic fog-harvesting review, background only" |
| B13-PDA-OCR-002 | PDA-coating | soft_boundary | CN114570339A ~8.2 mg/g 排除 qmax 排名 |

**工作量**：中等，可一次性批量执行。

### 类别 B：知识缺口（38 项已登记）

按子类型分布：

| 子类型 | 数量 | 典型示例 |
|---|---:|---|
| PDF 缺失 | 5 | CN114887602A（可从 git 恢复）、Vo2023 龙虾、Dong2025 海藻酸盐 |
| 仅推断无引文 | 9 | 边界条件全为 llm_inferred |
| 需 Yao 决策 | 5 | 淀粉极端值、重复提取映射、扫描专利 OCR |
| 空/弱原型 | 6 | shark-skin / water-strider / cactus / coral / magnetic-bacteria 零性能 |
| Enrichment 结构 | 4 | 因果链全空、计数不匹配、diatom 路径 |
| 其他 | 9 | MOF single_source、纤维素范围、DNA aptamer 无性能 |

### 类别 C：协作协议待办目标（8 项）

| # | 目标 | 分配给 | 状态 |
|---|---|---|---|
| 2 | 决策队列清除项更新为 applied_wrong_source_removal | Qoder(Codex) | 已由 Task 49 完成 |
| 3 | Enrichment mirror gap fill | Claude Code | 待执行 |
| 4 | Missing PDF 路径验证（chitosan 99 项） | Claude Code | 待执行 |
| 5 | lotus-leaf 355 机制分类 | Claude Code | Task 10/15 已部分完成 |
| 6 | cellulose-nanocrystal 材料分类 | Claude Code | 待执行 |
| 7 | 第二层 scope 决策提交 Yao | Qoder(Codex) | 待执行 |
| 8 | Apply Package B 剩余 | Qoder(Codex) | 待执行 |
| 9 | Apply Package C 排序安全标注 | Qoder(Codex) | 待执行 |
| 10 | Apply Package D 边界注册 | Qoder(Codex) | 待执行 |

### 类别 D：验证升级（最大工作量）

按优先级排序的逐原型 PDF 引文验证计划：

**Tier 1 — 高优先级（PDF 齐全、数据密度高）**

| 原型 | 性能行数 | 核心 PDF | 已验证 | 待验证 |
|---|---:|---|---|---|
| chitosan | 117 | Bambaeero2020 + 多专利 | Task 46 做了 14 行 | ~103 行 |
| PDA-coating | 44 | CN114887602A(已恢复) + 2 专利 | 部分 | ~35 行 |
| mussel-foot | 43 | 多篇论文 | 0 | 43 行 |
| fish-scale | 29 | CN114849640A | Task 12 部分 | ~20 行 |
| diatom-frustule | 42 | Du2021/Guo2022/Qin2024 | 0 | 42 行 |

**Tier 2 — 中优先级**

| 原型 | 性能行数 | 备注 |
|---|---:|---|
| plant-tannin | ~20 | Mao2024/Tan2023，Task 12 部分处理 |
| wood-xylem | ~8 | Kumar2021/Mo2021 |
| silk-fibroin | ~15 | Task 48 验证了 1 条约束 |
| scallop-shell | ~7 | Wang2024 |
| oyster-shell | ~6 | Qiu2021/Xu2022 |
| iron-oxidizing-bacteria | ~7 | Luo2021 |

**Tier 3 — 低优先级/特殊处理**

| 原型 | 状况 |
|---|---|
| bone-structure | Task 12 已处理 |
| cell-membrane-ion-channel | 需 metric_type 分离 |
| starch-granule | 121 行但大量 review-sourced |
| MOF | materials_reference，single_source 需特殊处理 |

### 类别 E：工具/校验问题（5 项）

| 问题 | 详情 |
|---|---|
| validate_consistency.py | 132 warnings（非 error），需判断是否需修复 |
| check_boundary_guardrail.py | 60 soft / 0 hard；diatom-frustule 无合格边界 |
| check_repo_hygiene.py | CLAUDE.md 不在 allowlist |
| check_causal_chain.py | 27/432 合格卡；diatom-frustule 无 |
| confidence 字段 | 全库统一 0.8，未校准 |

---

## 四、优先级建议（从 Codex/Qoder 视角）

### P0 — 立即执行（1-2 天）

1. **写入 8 项 approved-but-unapplied 边界规则**到 JSON。这是 Yao 已审批的决策，属于纯机械执行。
2. **修复 diatom-frustule 因果链缺失**——唯一无合格因果链卡的 active 原型。需要 OpenClaw 读 PDF 提取。
3. **更新 COLLABORATION-PROTOCOL.md 目标列表**——标记 Task 49 已完成的目标，同步最新状态。

### P1 — 短期推进（1 周内）

4. **启动 Tier 1 验证升级**——给 OpenClaw 分配 chitosan 剩余 103 行、PDA-coating 35 行、mussel-foot 43 行的逐行 PDF 引文验证。这是提升库可信度的核心工作。
5. **Enrichment 因果链批量填充**——从已验证的主 JSON 机制中提取，不需要重新读 PDF。可交给 OpenClaw 批量执行。
6. **CN114887602A 从 git 恢复**——已知在 git object `9ee5da0`，提取到本地后更新 PDA 的 source_file。

### P2 — 中期推进（2-4 周）

7. **Tier 2 验证升级**——plant-tannin、wood-xylem、scallop-shell 等中等密度原型。
8. **OCR 扫描专利处理**——CN113244898A、CN114570339A、CN113275374A 需要多模态模型。
9. **零性能原型评估**——5 个零性能原型是否需要补数据还是标注为 background-only。

### P3 — 长期/v0.2

10. **Enrichment schema 统一**——因果链格式对齐、计数匹配。
11. **confidence 字段校准**——从统一 0.8 改为逐行评分。
12. **materials_reference 验证**——MOF/CNC/starch/alginate 的 single_source 处理。
13. **build_prototypes_db.py 全跑**——审计期间不运行，收尾阶段再做。

---

## 五、角色确认

### QoderWork（替代 Codex）职责

- 范围控制、验收 spot-check
- 决策队列 / 边界寄存器维护
- worklog 更新、GitHub checkpoint
- 给 OpenClaw 分配任务、审查产出
- 向 Yao 提交决策建议

### OpenClaw 职责

- 批量 PDF 证据提取和验证
- OCR 扫描件处理
- 审计草稿输出（review-clcode-*.md）

### Yao 职责

- 最终审批 scope 决策和边界规则
- 确认空/弱原型的去留

---

## 六、关键数字速览

| 维度 | 已完成 | 剩余 | 完成率 |
|---|---:|---:|---:|
| 决策队列 | 136 | 10 (deferred) | 93% |
| 边界规则 | 59 applied+guard | 8 unapplied + 38 gap | 61% |
| 机制验证 | 16 verified | 514 待升级 | 3% |
| 性能验证 | 0 verified | 419 待升级 | 0% |
| 因果链 | 27 qualified | 405 待建 | 6% |
| Enrichment 填充 | 1/478 | 477 空 | 0.2% |

**结论**：决策和边界治理已基本收官（93%+61%），但证据层的验证覆盖率极低（机制 3%、性能 0%）。下一阶段的核心工作是逐原型的 PDF 引文验证，这是让库从"看着广"变成"每条可信"的关键一步。
