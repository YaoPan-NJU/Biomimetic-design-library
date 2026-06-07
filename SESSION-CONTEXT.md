# 项目会话上下文（2026-06-07 02:00）

> 本文件记录当前项目状态、已完成工作、待办事项，用于跨会话恢复。

---

## 当前状态总览

### 提参进度

| 分类 | 总数 | 已提取 | 进度 | 位置 |
|------|------|--------|------|------|
| 论文 | 302 | 275 | 91% | `tools/litextract/outputs/extractions/论文/json/` |
| 专利 | 33 | 37 | 100% | `tools/litextract/outputs/extractions/专利/json/` |
| 标准 | 6 | 3 | 50% | `tools/litextract/outputs/extractions/标准/json/` |
| **总计** | **341** | **315** | **92%** | |

### 原型进度

| 指标 | 数值 | 位置 |
|------|------|------|
| 已生成 prototype.md | 42 个 | `prototypes/*/prototype.md` |
| 有实质内容 | 35 个 | |
| 有 [待补充] 占位符 | 7 个 | |

### Git 状态

| 仓库 | 分支 | 最新提交 | 链接 |
|------|------|----------|------|
| Biomimetic-design-library | `feature/extraction-results` | `2946791` | [GitHub](https://github.com/YaoPan-NJU/Biomimetic-design-library/tree/feature/extraction-results) |
| Literature-extracting | `feature/biomimetic-extraction` | `c0e8749` | [GitHub](https://github.com/YaoPan-NJU/Literature-extracting/tree/feature/biomimetic-extraction) |

---

## 已完成任务（10/12）

| 任务 | 状态 | 说明 |
|------|------|------|
| 任务 0 | ✅ | LitExtract 提参基础设施搭建 |
| 任务 1 | ✅ | 论文全量提取 (275/302, 91%) |
| 任务 2 | ✅ | 专利重跑 (33/33, 100%) |
| 任务 3 | ✅ | 标准重跑 (3/6, 50%) |
| 任务 3.5 | ✅ | 清理重复 JSON |
| 任务 4 | ✅ | 后处理 + 合并结果 |
| 任务 5 | ✅ | 推送到 GitHub |
| 任务 6 | ✅ | 桥接管道 (3个脚本) |
| 任务 7 | ✅ | 清理 5 个手工标杆 |
| 任务 8 | ✅ | provenance 模板 + 双层校验 |
| 任务 9 | ✅ | 用桥接管道重建 5 个标杆 |
| 任务 10 | ✅ | 批量深化剩余原型 (42个) |

---

## 待办任务（2/12）

| 任务 | 状态 | 说明 |
|------|------|------|
| 任务 11 | 待启动 | 核查设计规则 |
| 任务 12 | 待启动 | 扩到 100 |

---

## 主要产出

### 产出一：提参结果（JSON 文件）

- 位置：`tools/litextract/outputs/extractions/`
- 数量：315 个（论文 275 + 专利 37 + 标准 3）
- 内容：参数级知识条目、仿生元数据、仿生叙事

### 产出二：原型文件（prototype.md）

- 位置：`prototypes/*/prototype.md`
- 数量：42 个（35 个有实质内容，7 个有占位符）
- 内容：性能数据表、吸附机制、工程约束

### 产出三：桥接管道脚本

- `tools/litextract/scripts/map_to_prototypes.py` - JSON → 原型映射
- `tools/litextract/scripts/aggregate_per_prototype.py` - 聚合 knowledge_items
- `tools/litextract/scripts/generate_prototype_md.py` - 渲染 prototype.md

### 产出四：校验脚本

- `tools/validate_consistency.py` - 校验一致性（断链、孤儿、占位符）

---

## 关键文件路径

```
/Users/panyao/Desktop/Biomimetic-design-library/
├── prototypes/                        # 42 个原型目录
│   ├── chitosan/prototype.md          # 有实质内容
│   ├── lotus-leaf/prototype.md        # 有实质内容
│   └── ...
├── tools/litextract/                  # 提参工具（子模块）
│   ├── outputs/extractions/           # 提取结果 JSON
│   │   ├── 论文/json/ (275 个)
│   │   ├── 专利/json/ (37 个)
│   │   └── 标准/json/ (3 个)
│   ├── scripts/                       # 桥接管道脚本
│   │   ├── map_to_prototypes.py
│   │   ├── aggregate_per_prototype.py
│   │   └── generate_prototype_md.py
│   └── prompts/                       # 提示词
│       ├── biomimetic_extraction_prompt.md (v1)
│       └── biomimetic_extraction_prompt_v2.md (v2)
├── tools/validate_consistency.py      # 校验脚本
├── feature-mapping.json               # 特征-原型映射表
├── 下一步执行计划_本地AI.md            # 执行计划
└── SESSION-CONTEXT.md                 # 本文件
```

---

## 已知问题

| 问题 | 状态 | 说明 |
|------|------|------|
| 仿生文献库在项目内 | ⚠️ 待处理 | 需移出项目目录，否则 git 历史会包含大文件 |
| 7 个原型有占位符 | ⚠️ 待补充 | 需要补充数据 |
| 标准只提取了 3/6 | ⚠️ 待完成 | 另外 3 个标准需要提取 |

---

## 下一步工作

### 立即

1. **任务 11：核查设计规则**
   - 核查 design-rules.json 的 40 条规则
   - 验收：超过 80% 规则有真实证据支撑

2. **任务 12：扩到 100**
   - 补充文献，扩展原型到 100
   - 验收：原型约 100，每个过基线与双层校验

### 后续

3. **合并到 main 分支**
   - 当前在 `feature/extraction-results` 分支
   - 最终需要合并到 main

4. **与 ADRMATS 系统对接**
   - 仿生设计库作为 ADRMATS 的仿生检索模块
   - 需要提供 BiomimeticContext 接口

---

## 恢复命令

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

# 5. 检查提取进度
echo "论文: $(ls tools/litextract/outputs/extractions/论文/json/ | wc -l)"
echo "专利: $(ls tools/litextract/outputs/extractions/专利/json/ | wc -l)"
echo "标准: $(ls tools/litextract/outputs/extractions/标准/json/ | wc -l)"

# 6. 检查原型进度
echo "原型: $(ls prototypes/*/prototype.md | wc -l)"
```

---

## 重要提醒

1. **不要上传仿生文献库**（PDF 原始文件）到 GitHub
2. **不要上传 .env 文件**（API keys）到 GitHub
3. **使用 v2 提示词**进行新提取（`biomimetic_extraction_prompt_v2.md`）
4. **桥接管道**是核心，用于从 JSON 生成 prototype.md
5. **校验脚本**用于检查一致性，每次更改后运行

---

*最后更新：2026-06-07 02:00*
