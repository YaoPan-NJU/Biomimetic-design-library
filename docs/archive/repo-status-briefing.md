## Biomimetic-design-library 现状核实报告

分支：`feature/extraction-results`，HEAD = `feaef62`，核实时间 2026-06-09

---

### 一、回归事实（已通过跑脚本 + git 对比确认）

**罪魁祸首：commit `d1f1cf2`**（2026-06-09 00:35，"第二波文献提取完成 + 重建 prototypes_db"）。

这次提交重跑了 `build_prototypes_db.py`，重建了全部 `prototypes_db/*.json`。重建脚本不感知富化层，导致以下数据在重建过程中被丢弃或重置：

| 指标 | 重建前 (`9dcb3a0`) | 重建后 (`d1f1cf2` / HEAD) | 变化 |
|------|---------------------|---------------------------|------|
| 带 `基本原理` 的原型数 | **21** / 31 | **0** / 31 | 全部丢失 |
| MOF 机制数 | 103 条（全有 `基本原理`） | 129 条（0 条有 `基本原理`） | 富化字段清除 |
| MOF performance verification | 236 single_source + 16 needs_review | 252 条**全部 unverified** | 溯源状态重置 |
| 缺 pollutant 的性能条目 | — | **226 条** | — |
| chimera 违规 | — | 2 个原型、5 处违规（polydopamine-coating, spider-silk） | — |
| 校验警告 | — | 254 条（主要是 R14 机制含实例级数据） | — |

**技术细节**：重建前机制条目的 key 是中文 `基本原理`，还带有 `active_features` 字段。重建后 schema 变成了纯英文（`name` / `description` / `functional_groups` / `source` / `ref_doi` / `verification`），这两个富化字段没有被保留。

后续 commit `feaef62` 只改了 README，无实质数据变化。

---

### 二、校验脚本实际输出

```
validate_consistency.py:  错误 0,  警告 254
check_chimera.py:         违规 2 个原型（polydopamine-coating, spider-silk），共 5 处
```

主要警告类型：R14（机制含实例级数据如 mg/g、接触角、去除率等），R10（source=literature 但无 ref_doi 且无 source_file），frontmatter organism 为空，prototype.md 含 `[待补充]` 占位符。

---

### 三、与同事 review 文档的数据差异

同事的 v2 review 文档中有几处描述与实测不符：

| 文档描述 | 实测结果 | 偏差方向 |
|----------|----------|----------|
| "带基本原理的原型从 26 掉到 6" | 从 **21 掉到 0** | 文档严重低估了回退程度 |
| "191 条性能数据缺 pollutant" | 实际 **226 条** | 文档低估了 35 条 |
| "752 条 performance 全部退回 unverified" | **确认**，752 条全部 unverified | 一致 |
| "chimera 重新冒头" | **确认**，2 原型 5 处违规 | 一致 |

---

### 四、根因诊断

`build_prototypes_db.py`（577 行）的重建逻辑是从原始提取 JSON（311+ 个文献提取文件）聚合到 `prototypes_db/`。但它的重建过程是**覆盖式**的：

1. 它不读取已有的 `prototypes_db/*.json` 中的富化数据（`基本原理`、`active_features`、`verification` 状态）
2. 它只从原始提取文件中取数据，而原始提取文件不含这些富化字段
3. 因此每次重跑 = 富化层清零

这就是同事 review 中"门槛 2（富化层与原始提取分离）"要解决的核心问题。

---

### 五、你需要做的事（Step 1 修 canon 的完成判据）

同事 review 定的判据：

1. `validate_consistency.py` → 0 错误（当前已满足，但 254 警告需要处理）
2. `check_chimera.py` → 0 违规（当前 2 原型 5 处违规）
3. 至少 20 个活跃原型有 `基本原理` 字段且 verification_tier 不为 unverified（当前 0 个）

要达到判据，核心工作是修复 `build_prototypes_db.py` 的重建逻辑，使其在重建时保留或合并已有的富化数据，然后重跑重建恢复 `基本原理`、`active_features` 和 verification 状态。

---

### 六、跟本地 AI 沟通时可以给它的关键上下文

1. 仓库路径和分支：`feature/extraction-results`，HEAD = `feaef62`
2. 回退发生在 `d1f1cf2`，可以通过 `git diff 9dcb3a0..d1f1cf2 -- prototypes_db/` 查看具体丢了什么
3. `git show 9dcb3a0:prototypes_db/*.json` 可以拿到回退前的富化数据
4. 核心修改目标：`tools/build_prototypes_db.py` 需要在重建时做 merge（保留已有富化字段），而非覆盖
5. 验收标准：上面第五节的三条判据
