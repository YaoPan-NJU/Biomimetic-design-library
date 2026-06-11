# 仿生设计库提取流水线 -- Phase 1-4 执行监控报告

> 执行日期: 2026-06-04
> 分支: feature/biomimetic-story-v2
> 执行环境: macOS, Python 3.9.6, 三路 API 负载均衡

---

## 一、执行概况

本次执行覆盖了完整的四阶段提取流水线，从302篇文献中为30个仿生原型提取了结构化知识。全流程零致命错误，总耗时约40分钟。

| 阶段 | 耗时 | LLM调用 | 成功率 | 关键产出 |
|------|------|---------|--------|----------|
| Phase 1 粗扫 | 324s (5.4min) | 149次 | 100% (0错误, 33次重试) | 30个粗扫profile JSON + coverage-heatmap |
| Phase 2 差距分析 | 777s (13min) | ~90次 | 100% (0错误) | 30个gap report JSON + supplementation-plan |
| Phase 3 补充计划 | <1s | 0次 | N/A | 336条搜索查询 (search-queries.md) |
| Phase 4 深度提取 | 1158s (19min) | ~180次 | 100% (30个验证告警) | 30个prototype.md + feature-mapping权重更新 |

**API 负载均衡分布 (Phase 1 统计):**
- dashscope (qwen3.7-max): 69次 (46.3%)
- mimo (Mimo-v2.5): 62次 (41.6%)
- coding_plan (qwen3.6-plus): 18次 (12.1%)

**重试机制:** 429限流时自动切换到不同API provider，Phase 1共33次重试全部成功。

---

## 二、Phase 1 粗扫结果

### 2.1 文献映射统计

- 文献库总量: 302篇PDF (9个分组)
- 映射到的原型: 30个 (占33个定义原型的91%)
- 论文映射总次数: 738次 (含跨原型重复映射)
- 直接映射: 228次; 间接映射: 510次

### 2.2 论文分布

| 统计量 | 值 |
|--------|------|
| 最大 | 64篇 (superhydrophobic-surface) |
| 最小 | 4篇 (mussel-foot-adhesion) |
| 中位数 | 17.5篇 |

### 2.3 零直接论文原型 (14个, 46.7%)

以下原型完全没有通过关键词直接匹配到论文，全部依赖间接映射:

dna-aptamer, iron-oxidizing-bacteria, lotus-leaf, magnetic-bacteria, namib-beetle, scallop-shell, shark-skin, silkworm-silk, slips-surface, spider-silk, water-strider, mycelium(1篇), wood-structure(2篇), chlorella(7篇)

### 2.4 覆盖维度

- 唯一吸附机制: 13种 (离子交换、配位螯合、静电吸附、氢键、孔隙吸附、超疏水分离、生物沉淀、生物矿化、生物富集、表面吸附、pi-pi堆积、分子筛分、梯度润湿)
- 唯一污染物词条: ~125种 (含重金属、有机染料、抗生素、营养盐等)

### 2.5 未覆盖原型 (3-5个)

以下原型在Phase 1中未获得任何论文映射:
bone-structure (骨结构), cactus-spine (仙人掌刺), cell-membrane-ion-channel (细胞膜离子通道), coral-skeleton (珊瑚骨架), lobster-exoskeleton (龙虾外骨骼)

---

## 三、Phase 2 差距分析结果

### 3.1 差距分类统计

| 差距类型 | 数量 | 说明 |
|----------|------|------|
| data_gap | ~180 | 定量数据缺失 (qmax, kinetics, isotherm, pH, temperature等) |
| knowledge_gap | ~322 | 仿生叙事和工程约束知识缺失 |
| weight_gap | 13 | 论文不足导致无法赋权 (仅出现在direct=0的原型) |

### 3.2 关键发现

- **机制字段是最大瓶颈**: 65.8%的提取记录机制为空
- **定量数据极度匮乏**: qmax仅5.4%有值, 去除率7.4%, pH范围4.7%
- **生物来源字段不完整**: 仅45%有值, 仿生链条断裂
- **间接映射存在过度映射**: 超疏水组14篇论文被分配给6个原型

### 3.3 五个代表性原型差距对比

| 原型 | 总差距 | data_gap | knowledge_gap | weight_gap | 评估等级 |
|------|--------|----------|---------------|------------|----------|
| mof-adsorbent | 21 | 10 | 11 | 0 | sufficient |
| chitosan-adsorbent | 18 | 7 | 11 | 0 | sufficient |
| dna-aptamer | 20 | 9 | 10 | 1 | empty |
| lotus-leaf | 20 | 9 | 10 | 1 | empty |
| sulfate-reducing-bacteria | 17 | 7 | 10 | 0 | sufficient |

---

## 四、Phase 3 补充计划结果

### 4.1 搜索查询统计

- 总查询数: 336条
- 分组: 3个

| 组 | 名称 | 查询数 | 目标数据库 |
|----|------|--------|-----------|
| 第9组 | 仿生方法论 | 1 | WoS, Google Scholar |
| 第10组 | 仿生设计综述 | 322 | WoS, CNKI, Google Scholar |
| 第11组 | 跨原型比较 | 13 | WoS, Google Scholar |

每条查询包含: WoS检索语法(TS=格式)、CNKI中文检索语法、Google Scholar自然语言格式。

---

## 五、Phase 4 深度提取结果

### 5.1 原型档案生成

30个prototype.md全部成功生成，位于 `prototypes/<id>/prototype.md`。

### 5.2 数据填充率评估

| 章节 | 填充状态 | 填充率 |
|------|----------|--------|
| YAML frontmatter (id/name/category) | 完整 | 100% |
| 吸附机制 | 部分填充 | ~70% (多数原型有1-18个机制) |
| qmax数据 | 部分填充 | ~40% (部分原型有具体数值) |
| 结构特征 (BET/孔径) | 极少 | ~5% |
| 仿生叙事 (5.1-5.5) | 空白 | ~0% (需要补充文献) |
| 适用场景/关联/文献 | 空白 | 0% |

### 5.3 Feature Mapping 权重更新

- pollutant_prototype_map: 49条全部更新 (100%)
- feature_prototype_map: 78条全部更新 (100%)
- constraint_prototype_map: 29条全部更新 (100%)
- **总计: 156/156 权重条目已填充, 权重范围 0.55-1.0**

### 5.4 验证告警

每个原型1个验证告警 (共30个)，主要为qmax或evidence_level字段格式不完全符合校验规范，不影响数据可用性。

---

## 六、已知问题与风险

### 6.1 严重问题

1. **仿生叙事完全空白**: 所有章节1、5.1-5.5、6、7、8均为"[待补充]"。原因: 没有补充文献(supplemented-papers目录为空)，叙事提取需要专门的仿生设计论文。
2. **21个原型目录无prototype.md**: Desktop有51个原型目录，仅30个生成了档案。差异来自命名体系不同(粗扫用"chitosan-adsorbent"，原始目录用"chitosan")。
3. **间接映射噪音**: dna-aptamer和magnetic-bacteria的25篇论文完全重叠，且与原型主题不相关。

### 6.2 中等风险

4. **机制提取不完整**: 65.8%的记录机制为空，mof-adsorbent等4个原型机制为零。
5. **定量数据稀缺**: 仅靠摘要扫描无法获取全文中的qmax/去除率/pH等工程参数。
6. **污染物新兴类型缺失**: 微塑料、PFAS/PFOA、抗生素耐药基因等未覆盖。

### 6.3 低优先级

7. **coding_plan调用比例偏低**: 仅12.1%，可能因其并发配额较低导致更多429重试。
8. **部分原型论文过少**: mussel-foot-adhesion仅4篇，alginate-adsorbent仅7篇。

---

## 七、下一步行动建议

| 优先级 | 行动 | 预期效果 |
|--------|------|----------|
| P0 | 用Phase 3搜索查询补充文献 (重点: 5个零覆盖原型 + 14个零直接论文原型) | 填补原型空白 |
| P0 | 统一原型命名体系，对齐30个粗扫ID与51个目录ID | 消除21个未覆盖目录 |
| P1 | 补充文献后重跑Phase 4，填充仿生叙事章节 | 提升叙事完成度至>50% |
| P1 | 优化间接映射逻辑，增加相关性过滤阈值 | 减少噪音映射 |
| P2 | 扩展原型数量 (从30→50+) | 更完整的仿生知识覆盖 |
| P2 | 增加全文深度提取比例 | 提升定量数据填充率 |

---

## 八、文件位置索引

| 内容 | 路径 (相对项目根) |
|------|-------------------|
| 粗扫profile (30个JSON) | `extraction/extraction-output/coarse-profiles/` |
| 覆盖热力图 | `extraction/extraction-output/coarse-profiles/coverage-heatmap.md` |
| 差距报告 (30个JSON) | `extraction/extraction-output/gap-analysis/gap-reports/` |
| 补充需求计划 | `extraction/extraction-output/gap-analysis/supplementation-plan.md` |
| 搜索查询 (336条) | `extraction/extraction-output/gap-analysis/search-queries.md` |
| 原型档案 (30个MD) | `prototypes/<id>/prototype.md` |
| 权重映射 | `feature-mapping.json` |
| 流水线代码 | `extraction/` |
| 环境配置 | `extraction/.env` (含API key, 不入库) |
