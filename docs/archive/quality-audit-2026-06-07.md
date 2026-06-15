# 项目质量审计报告（2026-06-07）

检查范围：Biomimetic-design-library 全部已完成任务（0-10）的产出质量
检查方式：只读，未修改任何文件

---

## 一、总体结论

**42 个原型中完全满足质量基线的数量：0。** 主要原因是 verification=verified 全线缺失（0%），这是设计上的预期——verification 由任务 8 的第二层 agentic 核查产生。但如果暂排除 verification 这一条，仅看其余 8 条基线，估计仅约 **10-14 个唯一原型（~24-33%）** 可满足或接近满足要求。

**桥接管道存在 3 个严重 bug**，导致产出数据有系统性偏差，需要修复后重新生成。

---

## 二、提取阶段质量

### 2.1 论文（275 篇）

| 维度 | 结果 |
|------|------|
| schema_version | 全部 biomimetic-v1 |
| knowledge_items 结构 | 抽查 3 篇无孤儿泄漏，无 routing 嵌套重复 |
| biomimetic_metadata | 3/3 覆盖（v1 中已有基础字段） |
| biomimetic_narrative | 3/3 覆盖，5 子节均有实质内容 |
| prototype_targets | 在 routing 子字段中有 |
| evidence 质量 | ~97-100% reliable，仅 1 条 suspicious |
| ref_doi 覆盖率 | 100% |

**评价：提取质量扎实。** 核心数据（knowledge_items 粒度、provenance、evidence）可靠，可以作为下游消费的数据基础。

### 2.2 专利（33 篇去重后）

| 维度 | 结果 |
|------|------|
| schema_version | v1: 19 (58%), v2: 14 (42%) |
| biomimetic_metadata | 7/33 (21%)，全来自 v2 |
| biomimetic_narrative | 6/33 (18%)，全来自 v2 |
| patent_number | 19/33 (58%)，**14 个文件缺失** |
| evidence 质量 | reliable 46%, needs_review 54% |

**问题：** v1/v2 混合，patent_number 缺失严重，evidence 质量明显低于论文（needs_review 超半数）。

### 2.3 标准（3 篇，仅 2 篇有效）

| 维度 | 结果 |
|------|------|
| standard_number | 3/3 覆盖（GB 3838-2002, HJ/T 154-2004, GB 5749-2006） |
| knowledge_items | 33 + 35 + **0**（生活饮用水卫生标准提取失败，PDF 预处理为空） |
| 限值数据 | 2 篇有效，参数覆盖全面 |

**问题：** 生活饮用水卫生标准提取失败需重跑；标准只完成了 3/6（50%）。

### 2.4 残留清理

- 专利目录下 4 个 "*2.json" 重复文件未清理
- git 对象库仍 1.40 GiB（2 个 stash 未删除）

---

## 三、桥接管道质量（任务 6）—— 发现 3 个严重 bug

### Bug 1：原型 ID 分裂（严重）

`map_to_prototypes.py` 的关键词/生物体回退映射使用了与 `feature-mapping.json` 不同的 ID，导致同一生物原型的文献被分散到两个原型：

| v2 LLM 路由的 ID | 回退映射的 ID | feature-mapping.json 中的 ID |
|------------------|-------------|------------------------------|
| mof-adsorbent | metal-organic-framework | metal-organic-framework |
| alginate-adsorbent | alginate | alginate |
| starch-adsorbent | starch-granule | starch-granule |
| chlorella | chlorella-cell-wall | chlorella-cell-wall |
| wood-structure | wood-xylem | wood-xylem |
| superhydrophobic-surface | superhydrophobic-artificial | superhydrophobic-artificial |

**后果：** 6 对完全重复的 prototype.md（内容一样，只有标题不同），同一原型的文献和数据被分裂，查询结果不完整。

### Bug 2：generate_prototype_md.py 完全忽略模板（严重）

函数签名接受了 `template_path` 参数，但函数体内从未读取模板文件。实际渲染完全靠硬编码的 Markdown 拼接，输出格式与 `templates/prototype-template.md` 完全不兼容：

- 模板要求 YAML frontmatter（id, name, category, organism 等）→ 脚本输出无 frontmatter
- 模板要求 6 个标准章节 → 脚本输出的章节结构完全不同
- 如果下游 ADRMATS 系统依赖 YAML 解析或特定章节名，将全部无法读取

### Bug 3：biomimetic_narrative 合并时静默覆盖（严重）

`aggregate_per_prototype.py` 用 `dict.update()` 合并多篇论文的 narrative，当两篇论文有相同 key 时后者直接覆盖前者，**丢失数据**。`biomimetic_metadata` 同样存在此问题。

### 其他问题

- v1 备份目录 `json_backup_v1/` 被递归扫描，导致 23 条重复映射
- 多关键词匹配导致同文件重复入映射（mof-adsorbent 下 11 个文件重复）
- 性能数据仅渲染前 20 条、机制仅前 10 条，截断无提示
- provenance 中的 `_source_file` 路径未输出到 Markdown
- `engineering_constraints` 关键词中 'ph' 过于宽泛，误匹配 phosphorus、graphene 等

---

## 四、Prototype.md 产出质量

### 4.1 总体统计

| 类别 | 数量 |
|------|------|
| 总原型 | 42 |
| 占位符（全空） | 7 |
| 完全重复副本 | 6 对（12 个文件） |
| 有实质内容的唯一原型 | ~28 |

### 4.2 6 个抽样原型的基线达标情况

| 原型 | 仿生叙事≥3节 | 污染物≥3种 | 机制≥2个 | 约束≥5项 | 四尺度≥2 | provenance | verification | 综合 |
|------|-------------|-----------|---------|---------|---------|------------|-------------|------|
| chlorella-cell-wall (19KB) | **缺失** | 达标 | 达标 | 部分 | 达标 | 达标 | 缺失 | 不达标 |
| metal-organic-framework (18KB) | 达标 | 达标 | 达标(有重复) | 达标 | 部分 | 达标 | 缺失 | 部分达标 |
| polydopamine-coating (9KB) | 达标(主题偏离) | **不达标**(仅1种) | 达标(有重复) | 达标(有重复) | 达标 | 部分 | 缺失 | 部分达标 |
| oyster-shell (5KB) | 达标 | **不达标**(仅1种) | **不达标**(仅1个) | 部分 | 部分 | 达标 | 缺失 | 部分达标 |
| mangrove-root (2KB) | **缺失** | 不达标 | 不达标 | 不达标 | 不达标 | 部分 | 缺失 | 不达标 |
| coral-skeleton (4KB) | 达标(主题偏离) | **零数据** | **零机制** | 部分 | 不达标 | 部分 | 缺失 | 不达标 |

### 4.3 系统性问题

1. **verification=verified 全线 0%**：42 个原型无一例外。这是预期行为（由 agentic 核查产生），但意味着基线中这一条目前 100% 不满足。

2. **6 对完全重复的原型**：alginate/alginate-adsorbent、chlorella/chlorella-cell-wall、MOF/mof-adsorbent、starch-adsorbent/starch-granule、superhydrophobic-artificial/superhydrophobic-surface、wood-structure/wood-xylem。内容是复制粘贴，仅标题不同。

3. **文件内重复条目**：MOF 中 Cu-MOF 配位驱动机理重复 3 次；polydopamine-coating 中性能数据 4 条完全重复。

4. **无 YAML frontmatter**：全部 42 个文件。如果下游系统依赖 YAML 解析将全部失败。

5. **主题偏离**：polydopamine-coating 的仿生叙事聚焦药物递送（非水处理）；coral-skeleton 全篇是海洋防污涂层（非吸附）。

6. **provenance 不完整**：部分来源仅写 `patent` 无具体专利号，无法追溯。

---

## 五、校验脚本（任务 8）

计划定义了 6 条校验规则，实际仅实现 **1.5 条**：

| 规则 | 状态 |
|------|------|
| feature-mapping 断链检查 | 部分实现（仅检查文件存在性） |
| 孤儿目录检查 | 已实现 |
| frontmatter 必填字段 + category 枚举 | **未实现** |
| source 标识符完整性 | **未实现** |
| llm_inference 约束（ref_doi=null） | **未实现** |
| verification=verified 可解析性 | **未实现** |

---

## 六、feature-mapping.json 一致性

- prototype_metadata: 33 个原型
- 孤儿目录（有目录无 mapping）: **9 个**
- constraint_prototype_map: **完全缺失**
- mechanism_feature_bridge: 16 条（有内容）

---

## 七、design-rules.json

**不存在。** 仓库中没有设计规则文件，任务 11（核查 40 条规则）无数据基础。

---

## 八、优先级排序的修复建议

### P0（必须立即修复，否则后续任务全部建立在有偏数据上）

1. **修复原型 ID 分裂**：统一 map_to_prototypes.py 的映射 ID 与 feature-mapping.json 的 prototype_metadata，消除 6 对重复。
2. **修复 generate_prototype_md.py 使用模板**：让脚本读取并遵循 prototype-template.md 的格式，输出 YAML frontmatter。
3. **修复 narrative 合并覆盖**：改为 list append 或按来源论文分组，不丢数据。
4. **修复后重新运行桥接管道**：用修复后的三件套重新生成全部 prototype.md。

### P1（影响数据完整性）

5. 清理 4 个专利重复 JSON + 23 个 v1 备份文件的递归扫描
6. 补全 14 个专利的 patent_number
7. 重跑生活饮用水卫生标准
8. 将 9 个孤儿原型纳入 feature-mapping.json
9. 校验脚本补全规则 3-6

### P2（影响质量但不阻塞）

10. 处理 7 个占位符原型（补充文献或标注为低覆盖）
11. 修复主题偏离（polydopamine-coating、coral-skeleton）
12. 文件内重复条目去重
13. provenance 中 "patent" 无具体号的问题
14. git 对象库清理（删 stash + gc）
