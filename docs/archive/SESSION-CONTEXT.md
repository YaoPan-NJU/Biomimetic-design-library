# 项目会话上下文（2026-06-07 · 更新）

> 本文件记录当前项目状态、已完成工作、待办事项，用于跨会话恢复。

---

## 一、当前状态总览

### 结构化存储（正典）

| 指标 | 数值 | 说明 |
|------|------|------|
| 原型总数 | 33 | active=29, needs_literature=4, deprecated=3 |
| 性能数据 | 415 条 | verified=394 (94.9%), needs_review=21 (5.1%) |
| 机制描述 | 773 条 | |
| 工程约束 | 258 条 | |
| 叙事条目 | 188 条 | |
| 位置 | `prototypes_db/*.json` | **正典数据源** |

### 提参进度

| 分类 | 总数 | 已提取 | 进度 | 位置 |
|------|------|--------|------|------|
| 论文 | 302 | 275 | 91% | `tools/litextract/outputs/extractions/论文/json/` |
| 专利 | 33 | 33 | 100% | `tools/litextract/outputs/extractions/专利/json/` |
| 标准 | 6 | 3 | 50% | `tools/litextract/outputs/extractions/标准/json/` |
| **总计** | **341** | **311** | **91%** | |

### 核查状态

| 状态 | 数量 | 占比 |
|------|------|------|
| ✅ verified | 394 | 94.9% |
| ⚠️ needs_review | 21 | 5.1% |
| ❓ unverified | 0 | 0% |

### Git 状态

| 仓库 | 分支 | 最新提交 |
|------|------|----------|
| Biomimetic-design-library | `feature/extraction-results` | `3bbe4e4` |
| Literature-extracting | `feature/biomimetic-extraction` | `c0e8749` |

---

## 二、架构决策

### 正典是结构化 JSON，不是 markdown

**决策**：`prototypes_db/*.json` 为正典数据源，`prototypes/*/prototype.md` 由它渲染生成。

**理由**：
- 315 个提取 JSON 是有接地、可查询、带 provenance 的资产
- markdown 是有损投影（截断、覆盖、丢 source_file）
- ADRMATS 系统需要结构化接口

### 数据判定规则

| 条件 | 处理 |
|------|------|
| `source∈{literature,patent,standard}` + ref 可解析 + 数值在来源中确实出现 | → `verified` |
| 来源查无此文，或数值在来源中找不到 | → 删除 |
| 有来源但缺页码/引用过短/精度不一致 | → `needs_review` |
| 任何字段缺来源 | → 留空，不编造 |

### 七条最高准则

1. 质量高于进度与数量。宁可 30 个真原型，不要 100 个掺假的。
2. 每条数值必须可溯源到一篇真实文献的具体位置。
3. 一个原型 = 一个仿生身份。不混入其他生物的叙事。
4. 未经独立核查的数据标 `unverified`，ADRMATS 不得当事实用。
5. 空白优于错配。没把握就留空。
6. 有引用不等于可信。
7. 拿不准就停下问人。

---

## 三、已完成任务

### 优化计划 Phase 0-3（全部完成）

| Phase | 任务 | 产出 |
|-------|------|------|
| Phase 0 | 清理残留 + 补跑标准 | 删 4 个重复 JSON、17 个备份、42 个旧 prototype.md；手动录入 GB 5749-2006 18 项限值 |
| Phase 1 P0-1 | 结构化存储架构 | `prototypes_db/` 33 个 JSON，schema 含 tested_conditions |
| Phase 1 P0-2 | 语义 chimera 重建 | 7 个原型 organism 修正、错配数据清除 |
| Phase 1 P0-3 | 六对重复合并 | 6 个非 canonical 目录删除，ID_ALIASES 归一化 |
| Phase 1 P0-4 | 行级溯源补全 | 14 个专利补 patent_number，0 个标识符缺失 |
| Phase 1.5 | 全量核查 | 394/415 verified (94.9%)，用 PDF + raw output 核查 |
| Phase 2 P1-1 | tested_conditions 导出 | 导出到 feature-mapping.json + Layer 1 软降权规则 |
| Phase 2 P1-2 | 权重导出 | 165 个权重（中位数公式），不再手拍 |
| Phase 2 P1-3 | frontmatter 生成 | 36 个 prototype.md 全部有 YAML frontmatter |
| Phase 2 P1-4 | 校验脚本补齐 | 9 条规则，校验通过（0 错误） |
| Phase 3 P2-1 | 孤儿归并 | 3 个孤儿标 deprecated 并入 feature-mapping |
| Phase 3 P2-2 | 去重 | 6 条重复数据删除 |

### 原始任务（10/12）

| 任务 | 状态 |
|------|------|
| 任务 0-10 | ✅ 已完成 |
| 任务 11（核查设计规则） | ⏳ 待启动（design-rules.json 不存在） |
| 任务 12（扩到 100） | ⏳ 待启动（需先补文献） |

---

## 四、待办任务

### 近期（第三波文献到货后）

| 任务 | 说明 | 优先级 |
|------|------|--------|
| 第三波文献提取 | ~70 篇新文献用 v2 提示词提取 | 🔴 |
| 重建 prototypes_db | 新数据合入结构化存储 | 🔴 |
| 重新核查 | 新数据需核查 | 🔴 |
| 发 v1.0 | 基于当前状态打 tag | 🔴 |

### 中期

| 任务 | 说明 |
|------|------|
| 补充空原型文献 | diatom-inspired-porous、iron-oxidizing-bacteria、plant-tannin、scallop-shell（第三波覆盖） |
| 重新激活 deprecated 原型 | dna-aptamer、biomineralization-template、silkworm-silk（第三波覆盖） |
| 21 条 needs_review 人工复核 | 用户待查看后决定 |
| 补全 27 篇论文提取 | 当前 275/302 (91%) |
| 补全 3 个标准提取 | 当前 3/6 (50%) |

### 长期

| 任务 | 说明 |
|------|------|
| 任务 11：核查设计规则 | design-rules.json 需新建 |
| 任务 12：扩到 100 | 需要大量新文献（~500 篇） |
| 创建干净分支交付 ADRMATS | 基于 main 创建交付分支 |
| 与 ADRMATS 系统对接 | 提供 BiomimeticContext 接口 |

---

## 五、主要产出

### 产出一：结构化存储（正典）

- 位置：`prototypes_db/*.json`
- 数量：33 个
- Schema：id, name, organism, features, tested_conditions, performance_data, mechanisms, narrative, engineering_constraints, provenance_summary, coverage, status

### 产出二：提取结果（JSON 文件）

- 位置：`tools/litextract/outputs/extractions/`
- 数量：311 个（论文 275 + 专利 33 + 标准 3）
- 内容：参数级知识条目、仿生元数据、仿生叙事

### 产出三：渲染文件（prototype.md）

- 位置：`prototypes/*/prototype.md`
- 数量：36 个（全部有 YAML frontmatter）
- 由 `tools/generate_prototype_md.py` 从 prototypes_db 渲染生成

### 产出四：映射与权重

- 位置：`feature-mapping.json`
- 内容：36 个 prototype_metadata（33 active + 3 deprecated）、165 个 pollutant→prototype 权重、tested_conditions、constraint_prototype_map（5 类别）、layer1_scoring 软降权规则

### 产出五：工具脚本

| 脚本 | 用途 |
|------|------|
| `tools/build_prototypes_db.py` | 从提取 JSON 构建 prototypes_db |
| `tools/generate_prototype_md.py` | 从 prototypes_db 渲染 prototype.md |
| `tools/verify_data.py` | 批量核查性能数据（PDF + raw output） |
| `tools/validate_consistency.py` | 9 条规则校验 |
| `tools/litextract/scripts/map_to_prototypes.py` | JSON → 原型映射（含 ID 归一化） |
| `tools/litextract/scripts/aggregate_per_prototype.py` | 聚合 knowledge_items |
| `tools/litextract/scripts/generate_prototype_md.py` | 旧版渲染脚本（已被 tools/ 版本替代） |

---

## 六、关键文件路径

```
/Users/panyao/Desktop/Biomimetic-design-library/
├── prototypes_db/                    # ⭐ 正典数据（33 个 JSON）
├── prototypes/                       # 渲染产物（36 个 prototype.md）
├── feature-mapping.json              # 映射 + 权重 + 条件
├── tools/
│   ├── build_prototypes_db.py        # 构建正典
│   ├── generate_prototype_md.py      # 渲染 prototype.md
│   ├── verify_data.py                # 核查脚本
│   └── validate_consistency.py       # 校验脚本
├── tools/litextract/                 # 提参工具（子模块）
│   ├── outputs/extractions/          # 提取结果 JSON（311 个）
│   ├── scripts/                      # 桥接管道脚本
│   └── prompts/                      # 提示词（v1/v2）
├── templates/prototype-template.md   # 模板
├── 文献检索指令_第三波.md            # 第三波检索指令（~70 篇）
├── quality-audit-2026-06-07.md       # 质量审计报告
├── 架构审查与优化建议_2026-06-07.md  # 架构审查报告
├── REVIEW-GUIDE.md                   # 第三方审查指南
└── SESSION-CONTEXT.md                # 本文件
```

---

## 七、已知问题

| 问题 | 状态 | 说明 |
|------|------|------|
| 仿生文献库在项目内 | ⚠️ 待处理 | 需移出项目目录，否则 git 历史会包含大文件 |
| 21 条 needs_review | ⚠️ 待用户复核 | 有提取但 PDF/raw output 中未找到数值 |
| 4 个空原型 | ⚠️ 待补充 | diatom-inspired-porous、iron-oxidizing-bacteria、plant-tannin、scallop-shell |
| 3 个 deprecated 原型 | ⚠️ 待激活 | dna-aptamer、biomineralization-template、silkworm-silk（第三波覆盖） |
| 标准只提取了 3/6 | ⚠️ 待完成 | 另外 3 个标准需要提取 |
| design-rules.json 不存在 | ⚠️ 待创建 | 任务 11 的数据基础 |

---

## 八、下一步工作

### 立即（新会话启动后）

1. **第三波文献到货后提取**
   - 学生正在下载 ~70 篇文献（文献检索指令_第三波.md）
   - 到货后用 v2 提示词提取，重建 prototypes_db

2. **发 v1.0**
   - 第三波提取完成后，打 `v1.0.0-alpha.1` tag
   - 推送到 GitHub

3. **创建干净交付分支**
   - 基于 main 创建 `release/v1.0` 分支
   - 只包含仿生库内容（prototypes_db、feature-mapping、templates、prototype.md）
   - 不包含：工具脚本、进度跟踪文档、文献检索指令、质量审计报告等
   - 目的：交付给 ADRMATS 的干净版本

### 后续

4. **补全提参**：27 篇论文 + 3 个标准
5. **任务 11**：设计规则库
6. **任务 12**：扩到 100（需 ~500 篇新文献）
7. **ADRMATS 对接**：BiomimeticContext 接口

---

## 九、恢复命令

```bash
# 1. 进入项目目录
cd /Users/panyao/Desktop/Biomimetic-design-library

# 2. 切换到工作分支
git checkout feature/extraction-results

# 3. 拉取最新代码
git pull origin feature/extraction-results

# 4. 检查状态
git status
git log --oneline -5

# 5. 检查结构化存储
python3 -c "import json, glob; files=glob.glob('prototypes_db/*.json'); print(f'prototypes_db: {len(files)} files')"

# 6. 检查核查状态
python3 -c "
import json, glob
v=n=0
for f in glob.glob('prototypes_db/*.json'):
    d=json.load(open(f))
    for p in d.get('performance_data',[]):
        if p.get('verification')=='verified': v+=1
        else: n+=1
print(f'verified: {v}/{v+n} ({v/(v+n)*100:.1f}%)')
"

# 7. 校验
python3 tools/validate_consistency.py
```

---

## 十、重要提醒

1. **正典是 `prototypes_db/*.json`**，不是 prototype.md
2. **不要上传仿生文献库**（PDF 原始文件）到 GitHub
3. **不要上传 .env 文件**（API keys）到 GitHub
4. **使用 v2 提示词**进行新提取（`biomimetic_extraction_prompt_v2.md`）
5. **质量为上**：宁可 30 个真原型，不要 100 个掺假的
6. **未经核查的数据标 unverified**，ADRMATS 不得当事实用

---

*最后更新：2026-06-07*
