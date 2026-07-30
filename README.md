# Biomimetic Design Library（BMDL）

BMDL 是面向水质风险控制与吸附材料设计的仿生原型知识库。它把生物原型、作用机制、污染物特征、材料转译原则和失效边界组织为可查询、可审计的数据，为设计智能体提供有证据等级的仿生启发。

本库不是材料性能排行榜，也不把生物结合、传感响应或规则命中当作已验证的材料去除性能。下游系统应依据证据 lane 使用候选，并在真实水体、竞争离子、再生和制造条件下继续验证。

## 项目职责

BMDL 接收目标污染物、水质条件和工程约束，返回结构化的 `BiomimeticDesignBrief`。它负责检索、证据分级、机制解释和材料转译提示，不直接给出最终材料配方，也不替代下游的组合设计与实验验证。

```text
结构化需求
  → BMDL 条件预筛与特征/污染物匹配
  → 原型、绑定机制、材料转译与边界
  → BiomimeticDesignBrief
  → 下游材料设计与验证
```

## 库中有什么

- 100 个根原型，覆盖微生物、植物、动物和人工仿生体系。
- 630 条机制卡，包含因果链、可转译原则、来源定位和边界条件。
- 501 条性能记录，用于区分严格事实、待核验线索和一般启发。
- 污染物画像、别名、特征—机制规则和原型映射。
- `BiomimeticContext` 查询接口与 ADRMATS 可直接消费的导出快照。

## 权威数据与功能

| 路径 | 作用 |
|---|---|
| `prototypes_db/*.json` | 原型与机制正典数据，是内容权威来源 |
| `prototypes/` | 面向人工阅读的原型文档 |
| `feature-mapping.json` | 污染物、特征与原型的策展映射 |
| `feature_matching_rules.json` | 分子特征到机制的规则词表 |
| `pollutant_profiles.json` | 污染物分子特征与相互作用画像 |
| `tools/biomimetic_context.py` | 查询、证据分级、机制绑定和 brief 生成 |
| `adrmats_export/` | 下游系统使用的匹配快照 |

## 匹配架构

| 匹配面 | 主要数据 | 作用 |
|---|---|---|
| 条件预筛 | `prototype_metadata[id].applicability`、`tested_conditions` | 根据 pH、温度、盐度和工程约束识别适用边界 |
| 污染物匹配 | `pollutant_prototype_map`、性能证据 | 返回有污染物专项依据的候选，并区分 `fact` 与 `lead` |
| 特征匹配 | `pollutant_profiles.json`、`feature_prototype_map` | 在专项证据不足时，以分子特征和可能相互作用寻找启发 |
| 机制解释 | `mechanism_feature_bridge`、`prototypes_db/*.json` | 绑定具体机制，给出因果链、材料转译和边界条件 |

`weight` 只表示检索相关性。库先按证据 lane 区分事实、线索和启发，再在同一 lane 内使用相关性排序。

查询流程为：

```text
污染物与工况
  → 名称归一化与污染物画像
  → 材料去除性能证据
  → 污染物专项映射
  → 特征—机制—原型检索
  → 机制绑定、边界检查与证据分级
  → BiomimeticDesignBrief
```

## 证据分级

| lane | 判定与用途 |
|---|---|
| `fact` | 污染物特异材料去除性能具备来源、定位、原文引文和严格核验，且展示机制已核验；可作为事实依据 |
| `lead` | 性能记录具备来源、定位和原文引文但仍为 `partial`，或性能严格而展示机制仍待核验；可作为优先验证线索 |
| `exploratory` | 生物结合、传感、规则映射或机制类比；只用于生成假设 |

`direct_evidence=true` 只表示严格的污染物特异材料去除性能。`weight` 表示同一 lane 内的检索相关性，不是实验置信度，也不应跨 lane 直接比较。

## 快速开始

```python
from tools.biomimetic_context import BiomimeticContext

ctx = BiomimeticContext()
result = ctx.query(
    pollutant="PFOA",
    water_quality={"pH": 7.0, "temperature": 25, "salinity": "low"},
    engineering_constraints=["真实二级出水", "可再生"],
)

for candidate in result["brief"]["candidates"]:
    print(
        candidate["prototype_id"],
        candidate["lane"],
        candidate["mechanism"]["mechanism_id"] or candidate["mechanism"]["name"],
    )
```

返回结果包含：

- 被选中的原型及其匹配原因；
- 与本次查询绑定的具体机制（优先使用 ID，旧机制以完整名称绑定）；
- `fact / lead / exploratory` 证据 lane；
- 可转译的材料设计原则；
- 已知边界、DO-NOT 和性能线索来源。

## ADRMATS 导出

重新生成匹配快照：

```bash
python -X utf8 tools/export_adrmats_snapshot.py
```

下游集成应优先读取 `adrmats_export/match_export.json`。其中保留 `lane`、`direct_evidence`、`performance_evidence_tier`、`candidate_honesty`、`bound_mechanism_id` 和 `bound_mechanism`；五列 CSV 仅用于兼容旧导入器。

BioADRMATS 侧需要完成的导入与适配改动见 [BioADRMATS 集成指南](docs/handoff/BIOADRMATS_INTEGRATION_GUIDE.md)。

## 验证

```bash
python -m pytest
python -X utf8 tools/validate_consistency.py --strict
python -X utf8 tools/check_chimera.py --strict
python -X utf8 tools/check_causal_chain.py
python -X utf8 tools/check_source_authenticity.py
python -X utf8 tools/check_repo_hygiene.py
python -X utf8 tools/verify_adrmats_delivery.py
```

`check_source_authenticity.py` 的 `0 ERROR` 只表示来源标识符和字段结构通过检查，不等于 DOI、定位页和具体声明已经逐条人工复核。

## 文档

- [设计与 brief 结构](docs/design.md)
- [证据与字段定义](docs/references/definitions.md)
- [ADRMATS 调用说明](docs/ADRMATS_CALL_GUIDE.md)
- [BioADRMATS 集成指南](docs/handoff/BIOADRMATS_INTEGRATION_GUIDE.md)
- [支持范围与风险](docs/SUPPORT_SCOPE_AND_RISKS.md)
- [仓库治理规范](docs/REPOSITORY_HYGIENE.md)

## 数据修改原则

1. 原型、机制和性能记录必须能追溯到明确来源；缺失定位或引文时不得升级证据等级。
2. 生物结合、传感和材料去除性能必须分开表述。
3. 映射命中只表示设计相关性，不能自动升级为直接证据。
4. 原型的生物机制与材料转译必须显式分层，避免把工程材料行为倒写成天然机制。
5. 被否决、缺失或存在范围冲突的证据应保留审计状态，不得静默改写为已验证事实。
