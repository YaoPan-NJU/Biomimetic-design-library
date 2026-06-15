## adsorption/dev 分支现状 & ADRMATS 对接分析

---

### 一、adsorption/dev 分支当前状态

这个分支是你做了大量修复工作后的**最新最成熟版本**，比之前 `feature/extraction-results` 进步了很多。核心数据指标：

| 指标 | 值 |
|------|-----|
| 活跃原型 | 31 个 |
| 带 `基本原理` 的原型 | 21 个 |
| 性能数据总条数 | 963 条（之前 752，第三波 + 中文文献新增 199 条） |
| 机制条目 | 864 条 |
| 工程约束 | 363 条 |
| non-unverified 性能条目 | 252 条 |
| enrichment 文件 | 21 个（已分离） |
| chimera 违规 | 0 |
| validate 错误 | 0（254 警告，主要是 R14） |
| 污染物别名 | 28 个 |
| 污染物分子特征画像 | 25 个 |

相比 `feature/extraction-results` 的主要进步：

- **富化层分离已完成**：`prototypes_db/enrichment/` 有 21 个文件，`build_prototypes_db.py` 支持 merge 和 `--export-enrichment`
- **chimera blocklist 已加入**：polydopamine-coating 和 spider-silk 的污染源在 merge 时被自动过滤
- **污染物字段大幅改善**：从 226 条缺 pollutant 降到 63 条（smart fill + 标准化）
- **导入了 library-enhancement 资产**：`design-rules.json`（条件-机制规则）+ 41 篇原理 markdown（design-strategies / mechanisms / trade-offs），但全部标记为 `pending_validation`
- **`BiomimeticContext` 新增 `find_applicable_rules` 方法**：可以根据水质条件匹配 design rules

**尚未完成的事项**：
- 导入的 design-rules 和 principles 全部 `pending_validation`，未经文献验证
- 63 条性能数据仍缺 pollutant 字段
- 254 条 R14 警告未处理（机制名含实例级数据）
- `litextract` 子模块未初始化
- `feature/extraction-results` 远程分支已不存在，`adsorption/dev` 是唯一的活跃开发分支

---

### 二、ADRMATS 系统概览

ADRMATS 是一个基于 **CrewAI 1.10.1 + LangChain** 的多智能体系统，用于设计水处理吸附材料。它有 7 个 Agent，按 6 个阶段顺序执行：

```
用户自然语言输入
    ↓
T: TaskOrchestrationAgent（意图分类，路由到 5 种工作流之一）
    ↓ full_workflow:
1. A: AdaptiveConstrainingAgent → 水质预处理、DO NOT list、7 维权重
2. M: MaterialDesigningAgent（对抗式双提案 + Reviewer 迭代）
3. A: AssessmentScreeningAgent（三专家并行 + 一致性检查）
4. S: SynthesisGuidingAgent（对抗式合成路线）
5. D: DesignExplainingAgent（思维链 + 置信度评分）
6. R: RegenerationSuggestionAgent（再生方法 + 生命周期建议）
```

模型配置：Qwen3.6-Plus（主力）、DeepSeek V4 Flash（Reviewer / 第二提案者）、Qwen3.6-Flash（轻量）、GLM-5.1（质量门控）。

外部工具：PubChem、Materials Project、Name2CAS、DataValidator、PNEC、EPA CompTox、本地 PG（水厂统计数据）。

---

### 三、对接分析：库能不能支撑 ADRMATS 调用？

**结论：接口设计完备，但对接代码完全没有写。两个系统各自就绪，中间的桥梁不存在。**

#### 已具备的条件

1. **`BiomimeticContext.query()` 接口稳定**，输入输出格式明确：
   - 输入：`pollutant`（str）+ `water_quality`（dict）+ `engineering_constraints`（list）
   - 输出：`BiomimeticDesignBrief`（context + candidates + applicable_rules + honesty_ledger）

2. **ADRMATS 的 Stage 1（ConstraintAgent）输出与库的输入高度兼容**：
   - `WaterQualityProfile`（ph_range / temperature_range / salinity_level）→ 可映射为 `{"pH": float, "temperature": float, "salinity": str}`
   - `PollutantCharacteristic.name` → 直接传给 `query(pollutant=...)`
   - `DesignGuidelines.mandatory_requirements` → 直接传给 `engineering_constraints`

3. **库的 brief 输出正好适合喂给 Stage 2（对抗式设计）的提案者**：candidates 提供了仿生原型、吸附机制、设计转译思路和诚实声明，这些是提案者需要的设计灵感。

#### 缺失的 6 个对接环节

| # | 缺失项 | 说明 | 工作量 |
|---|--------|------|--------|
| 1 | **桥接模块** | ADRMATS 中需要一个 adapter，从 `ConstraintPreprocessOutput` 提取参数，调用 `BiomimeticContext.query()`，将 brief 注入下游 | 中等 |
| 2 | **依赖管理** | 库没有 `pyproject.toml`，ADRMATS 无法通过 pip 安装。需要加 `setup.py` 或作为 git submodule | 小 |
| 3 | **设计提案 prompt 改造** | `adversarial_design_flow.py` 的 `_build_proposer_prompt()` 当前不接受 brief 输入，需要增加 biomimetic context slot | 中等 |
| 4 | **优雅降级** | 当库返回空结果（不支持的污染物）时，ADRMATS 需要能继续运行而不报错 | 小 |
| 5 | **verification 感知** | brief 中的 honesty_ledger 标注了 facts/leads/inferences，ADRMATS 的设计 Agent 需要在 prompt 中被要求尊重这些声明 | 小 |
| 6 | **design-rules 验证** | 导入的 41 篇原理文档和 design-rules.json 全部 `pending_validation`，在被 ADRMATS 用于实际设计前需要文献验证 | 大 |

#### 数据层面的风险

- **verified = 0**：所有性能数据最高只到 `single_source`，没有独立验证。ADRMATS 如果把这些当"硬事实"用，设计结果的可信度会打折扣。
- **覆盖有限**：25 种污染物画像 + 13 个能产出完整 brief 的原型。用户问到库不支持的污染物时会返回空 brief。
- **R14 警告**：196+ 条机制名混入了实验级数据（如"Cu(II)配位壳聚糖磁性材料对RBR的吸附容量"），作为机制名传给设计 Agent 可能造成误解。

---

### 四、下一步建议

按优先级排序：

#### P0：写桥接模块（让 ADRMATS 能调通库）

在 ADRMATS 的 `src/tools/` 下新建 `biomimetic_library_tool.py`：

```python
# 伪代码
class BiomimeticLibraryTool:
    def query(self, pollutant: str, water_quality: dict, engineering_constraints: list) -> dict:
        # 1. 初始化 BiomimeticContext（需要知道库的安装路径）
        ctx = BiomimeticContext(library_path="/path/to/Biomimetic-design-library")
        # 2. 调用 query
        brief = ctx.query(pollutant, water_quality, engineering_constraints)
        # 3. 如果 brief 为空（不支持的污染物），返回 graceful fallback
        if not brief.get("candidates"):
            return {"status": "no_biomimetic_match", "fallback": "proceed_without_bioinspiration"}
        return brief
```

在 `src/orchestrator.py` 中，Stage 1 完成后调用这个 tool，把 brief 传入 Stage 2。

#### P1：改造对抗式设计 prompt

在 `adversarial_design_flow.py` 的 `_build_proposer_prompt()` 中增加 biomimetic brief 输入：

```
现有 prompt 结构：
  - user_input: 用户需求
  - constraint_output: 水质约束 + DO NOT list + 权重

需要增加：
  - biomimetic_brief: 仿生原型候选列表（top 3-5）
  - 每个 candidate 的 mechanism + design_translation + honesty tier
  - 指令：「以下仿生原型可作为设计灵感，注意尊重 honesty_ledger 的声明」
```

#### P2：库的打包和依赖管理

给 Biomimetic-design-library 加 `pyproject.toml` 或 `setup.py`，让 ADRMATS 可以通过 `pip install git+https://...` 安装。或者作为 git submodule 引入。

#### P3：验证 design-rules

导入的 41 篇原理文档需要逐篇对照文献验证，把 `pending_validation` 改为 `validated` 或 `rejected`。这是一个大工程，但直接影响 design-rules 的可信度。

#### P4：处理 R14 警告 + 补全 pollutant 字段

254 条 R14 警告和 63 条缺 pollutant 的数据需要清理，提升库的整体数据质量。

---

### 五、一句话总结

**库的接口和数据已经 ready，ADRMATS 的流水线也已经 ready，但中间差一个桥接模块（约 100-200 行代码）+ prompt 改造。这是一个 1-2 天可以完成的集成工作。design-rules 的文献验证是更大的后续工程。**
