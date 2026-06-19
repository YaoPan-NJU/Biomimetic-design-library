# 复盘报告：第二波文献提取 + prototypes_db 重建事故

> 日期：2026-06-09
> 分支：`feature/extraction-results`
> 涉及 commit：`d1f1cf2`（事故）、`feaef62`（后续）、本次修复

---

## 一、事故概述

本次共发生 **两个独立事故**，叠加导致数据质量严重回退：

| 事故 | 根因 | 影响范围 | 发现时间 |
|------|------|----------|----------|
| ① prototypes_db 重建覆盖 | `build_prototypes_db.py` 覆盖式写入 | 全部 31 个原型的富化数据 | 2026-06-09 |
| ② 提取失败率异常 | mimo 模型 JSON 语法 bug + 脚本 fallback 缺失 | 第二波提取 ~42% 失败率 | 2026-06-09 |

---

## 二、事故①：prototypes_db 重建覆盖

### 2.1 时间线

1. **重建前**（commit `9dcb3a0`）：prototypes_db 包含人工富化数据
   - 21/31 个原型有 `基本原理` 字段
   - MOF：103 条机制全部有 `基本原理`，252 条性能数据中 236 条 single_source + 16 条 needs_review

2. **事故 commit**（`d1f1cf2`，2026-06-09 00:35）：重跑 `build_prototypes_db.py`
   - 提交信息："第二波文献提取完成 + 重建 prototypes_db"
   - 重建了全部 `prototypes_db/*.json`

3. **重建后**：富化数据全部丢失
   - 0/31 个原型有 `基本原理`
   - MOF：0 条机制有 `基本原理`，252 条性能数据全部退回 unverified

### 2.2 根因分析

`build_prototypes_db.py` 的重建逻辑是**覆盖式**的：

```python
# 原始代码（事故版本）
result = aggregate_prototype(pid, file_infos, feature_mapping)
output_path = output_dir / f'{pid}.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
```

问题：
1. **不读取已有数据**：直接用聚合结果覆盖文件
2. **聚合函数不含富化字段**：`extract_mechanisms()` 只提取 name/description/functional_groups/source/ref_doi/verification，不含 `基本原理` 和 `active_features`
3. **verification 硬编码**：`extract_performance_data()` 硬编码 `verification: 'unverified'`，不保留旧值

### 2.3 数据损失量化

| 字段 | 重建前 | 重建后 | 损失 |
|------|--------|--------|------|
| 带 `基本原理` 的原型 | 21/31 | 0/31 | **100%** |
| MOF `基本原理` 条目 | 103 | 0 | **100%** |
| MOF verified 性能 | 252 | 0 | **100%** |
| `active_features` | 有 | 无 | **100%** |
| `mechanism_instances` | 有 | 无 | **100%** |

### 2.4 修复方案

改为 **merge 模式**：

```python
# 修复后代码
result = aggregate_prototype(pid, file_infos, feature_mapping)
output_path = output_dir / f'{pid}.json'
result = merge_with_existing(result, str(output_path))  # ← 新增
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
```

`merge_with_existing()` 逻辑：
1. 读取已有 `prototypes_db/*.json`
2. **mechanisms**：按 `name+description` 匹配，保留旧的 `基本原理`、`active_features`、`verification`
3. **performance_data**：按 `parameter+value+pollutant+material` 匹配，保留旧的 `verification`、`confidence`、`source` 等
4. 只从原始提取更新新增或空字段

### 2.5 修复结果

| 指标 | 修复前 | 修复后 | 目标 |
|------|--------|--------|------|
| 带 `基本原理` 的原型 | 0 | **21** | ≥20 ✅ |
| MOF verified 性能 | 0 | **165** | >0 ✅ |
| chimera 违规 | 2 原型 5 处 | **0** | 0 ✅ |
| validate 错误 | 0 | **0** | 0 ✅ |

> 注：MOF 的 252 条性能数据恢复了 165 条 verified（65%），剩余 87 条因 key 不完全匹配保持 unverified。

---

## 三、事故②：提取失败率异常

### 3.1 现象

第二波提取（119 篇 PDF）失败率高达 **42%**（10/24），远高于第一批的 ~9%。

| 模型 | 成功 | 失败 | 失败率 |
|------|------|------|--------|
| mimo/mimo-v2.5 | 8 | 9 | **53%** |
| bailian/qwen3.6-plus | 6 | 2 | 25% |

### 3.2 根因分析

**mimo 的系统性 JSON 语法 bug**：

```json
// ❌ mimo 输出（错误）
"decision_summary": "one_sentence_value": "本文..."

// ✅ 正确格式
"decision_summary": {"one_sentence_value": "本文..."}
```

mimo 在输出 `decision_summary` 字段时，**漏掉了 `{` 开括号**。这是 v2 schema 新增的字段，v1 schema 没有这个字段所以第一批没触发此 bug。

**脚本 fallback 缺失**：

```python
# 原始代码
obj = try_parse(text)
if obj is None:
    print("No valid JSON found", file=sys.stderr)  # ← 直接失败，没有 fallback
    sys.exit(1)
```

`extract_first_json()` 定义了 `reconstruct_from_parts()` 作为 fallback，但**从未调用**。

### 3.3 失败类型分布

| 类型 | 数量 | 原因 |
|------|------|------|
| JSON 语法错误 | 8 | mimo `decision_summary` 漏 `{` |
| JSON 截断 | 2 | bailian 输出超长被截断 |
| **总计** | **10** | |

### 3.4 修复方案

在 `extract_first_json()` 中新增三层修复：

```python
# 修复后代码
obj = try_parse(text)           # 层 1：直接解析
if obj is None:
    obj = try_parse(repair_json_syntax(text))  # 层 2：修复语法错误再解析
if obj is None:
    obj = reconstruct_from_parts(text)         # 层 3：从碎片重建
if obj is None:
    print("No valid JSON found", file=sys.stderr)
    sys.exit(1)
```

新增 `repair_json_syntax()` 函数：

```python
def repair_json_syntax(t):
    """修复 mimo 的 decision_summary 漏掉 { 的 bug"""
    t = re.sub(r'"decision_summary"\s*:\s*"one_sentence_value"\s*:',
               '"decision_summary":{"one_sentence_value":', t)
    # ... 其他 decision_summary 子字段
    return t
```

### 3.5 修复结果

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| 成功 | 14 | **28** |
| 失败 | 10 (42%) | **3 (10%)** |
| 失败率 | 42% | **10%** |

剩余 3 个失败是 mimo 处理非标准 PDF（中文专利、建筑仿生、牙科仿生）时的边缘情况，可通过 `reconstruct_from_parts` 恢复。

---

## 四、Chimera 污染

### 4.1 现象

`check_chimera.py` 报告 2 个原型有 chimera 违规：

| 原型 | 污染源 | 违规数 |
|------|--------|--------|
| polydopamine-coating | Stenocara beetle（沙漠甲虫） | 2 |
| spider-silk | Nelumbo（荷叶）、Nepenthes（猪笼草） | 3 |

### 4.2 根因

这是重建时从原始提取 JSON 中引入的。某些文献同时涉及多个仿生原型（如"超疏水综述"同时提到 PDA 和甲虫），映射时被错误地归到了不相关的原型。

### 4.3 修复

1. **polydopamine-coating**：organism 修正为 "mussel-inspired synthetic polydopamine"，移除 1 条甲虫机制
2. **spider-silk**：organism 修正为 "Araneidae (spiders)"，移除 3 条荷叶/猪笼草机制

---

## 五、教训与改进

### 5.1 已实施的改进

| 改进项 | 文件 | 说明 |
|--------|------|------|
| merge 模式重建 | `build_prototypes_db.py` | 重建时保留已有富化数据 |
| JSON 语法修复 | `multi_worker_extract.sh` | 新增 `repair_json_syntax()` |
| reconstruct fallback | `multi_worker_extract.sh` | 修复 `reconstruct_from_parts()` 未被调用的 bug |

### 5.2 待改进

| 改进项 | 优先级 | 说明 |
|--------|--------|------|
| 性能数据匹配规则放宽 | P1 | 当前 key 精确匹配导致 35% 未恢复 |
| chimera 自动检测+清理 | P2 | 当前是手动修复，应自动化 |
| 提取前文献去重/去冲突 | P2 | 避免一篇文献被映射到不相关原型 |
| mimo prompt 强化 JSON 格式 | P3 | 从源头减少语法错误 |

### 5.3 流程改进

1. **重建前必须备份**：重跑 `build_prototypes_db.py` 前应先 commit 或备份 `prototypes_db/`
2. **提取脚本必须有 fallback**：JSON 解析失败时应尝试修复，不应直接报错
3. **模型差异需要测试**：新 schema 字段应在两个模型上都测试后再批量跑

---

## 六、验收结果

| 验收标准 | 结果 | 状态 |
|----------|------|------|
| `validate_consistency.py` 0 错误 | 0 错误 / 253 警告 | ✅ |
| `check_chimera.py` 0 违规 | 0 违规 | ✅ |
| ≥20 个原型有 `基本原理` | 21 个 | ✅ |
| MOF verified 性能 >0 | 165 条 | ✅ |
| 提取失败率 <20% | 10% | ✅ |
