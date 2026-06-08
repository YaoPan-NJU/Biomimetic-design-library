# ADRMATS 交付计划

> 唯一执行入口
> 创建日期：2026-06-08
> 目标：ADRMATS 可以稳定调用本库生成合格 biomimetic design brief

---

## 1. 交付目标

本库必须作为 ADRMATS 的仿生启发检索模块，接受上游约束智能体传来的污染物、水质条件、去除需求、工程约束，返回一个可被后续对抗设计模块消费的 brief。

**核心要求**：
- brief 必须由 `tools/biomimetic_context.py` 的真实接口生成
- 不允许手写示例 JSON 冒充接口产物
- 必须清楚标注 direct evidence 与 feature-based inspiration 的区别

---

## 2. 最终接口输出格式

```json
{
  "brief": {
    "context": {
      "water_quality": {},
      "removal_target": {},
      "pollutant_profile": {
        "canonical_name": "",
        "pollutant_class": "",
        "molecular_features": [],
        "likely_interactions": [],
        "profile_basis": ""
      },
      "engineering_constraints": []
    },
    "candidates": [
      {
        "prototype_id": "",
        "organism": "",
        "match": {
          "reason": "",
          "weight": 0.0,
          "applicability_fit": "",
          "match_basis": "",
          "direct_evidence": false
        },
        "mechanism": {
          "name": "",
          "基本原理": "",
          "key_structures": [],
          "functional_groups": [],
          "molecular_feature_links": [],
          "attribution": {
            "source": "",
            "ref": "",
            "verification_tier": ""
          }
        },
        "design_translation": {
          "idea": "",
          "material_realization_examples": [],
          "source_tier": ""
        },
        "evidence_context": {
          "performance_leads": []
        }
      }
    ],
    "honesty_ledger": {
      "facts": [],
      "leads": [],
      "inferences": []
    }
  }
}
```

---

## 3. 验收标准

### 3.1 接口验收

1. `tools/biomimetic_context.py` 必须能正常运行
2. 接口输出必须符合上述 schema
3. 不允许手写 brief 示例作为通过依据

### 3.2 污染物标准化验收

1. Pb(II)、Pb²⁺、Pb2+、lead ion 必须归一到 Pb(II)
2. PFOA、SMX、BPA 必须有分子特征画像
3. canonical name 必须在 pollutant_profile 中正确返回

### 3.3 匹配逻辑验收

1. PFOA/SMX/BPA 不允许伪装成 direct evidence
2. 如果没有直接实验数据，必须标 `direct_evidence=false`，`match_basis=molecular_feature_inference`
3. Pb(II) 如果有 direct evidence，可以标 `direct_evidence=true`，但每条 evidence 必须带 `verification_tier`
4. `needs_review` 条目不得进入强排序

### 3.4 质量验收

1. `validate_consistency.py` 必须 0 error
2. `check_chimera.py` 必须 0 violation
3. README/HANDOFF 中的 commit、状态数字、当前风险必须和实测结果一致

### 3.5 查询验收

验收脚本必须测试以下查询：
- PFOA，pH=7，中等盐度，痕量吸附去除，约束：水稳定性、可再生、低二次污染
- SMX，pH=7，低盐度，抗生素吸附去除
- BPA，pH=7，中等盐度，内分泌干扰物去除
- Pb(II)，pH=6，低盐度，重金属离子去除

---

## 4. 工作顺序

### Milestone 0：交付计划与状态收敛

- [x] 新增 docs/ADRMATS_DELIVERY_PLAN.md
- [ ] 更新 README.md 和 docs/HANDOFF.md，只保留入口和当前真实状态
- [ ] 修复 Windows 默认编码下 validate/check 脚本报错
- [ ] 运行 validate_consistency.py、check_chimera.py
- [ ] commit 并 push
- [ ] 回报 commit hash、命令结果、剩余风险

### Milestone 1：接口契约收敛

- [ ] 修改 BiomimeticContext.query()，让真实返回结构与文档 schema 一致
- [ ] 新增自动 schema 验收
- [ ] 不允许手写 brief 示例作为通过依据
- [ ] commit 并 push

### Milestone 2：污染物标准化与画像数据化

- [ ] 把 pollutant profiles 和 aliases 从 Python 代码迁出到 JSON 数据文件
- [ ] Pb(II)、Pb²⁺、Pb2+、lead ion 必须归一
- [ ] PFOA、SMX、BPA 必须有分子特征画像
- [ ] commit 并 push

### Milestone 3：真实 ADRMATS 查询闭环

- [ ] 用 verify_adrmats_delivery.py 生成并验证 PFOA/SMX/BPA/Pb(II) 的真实接口 brief
- [ ] 每个 brief 必须通过 honesty 标注检查
- [ ] 输出 examples/adrmats_briefs/ 下的生成样例
- [ ] commit 并 push

### Milestone 4：v0.1 交付包

- [ ] 形成 ADRMATS 调用说明
- [ ] 列出当前支持范围、不能支持的范围、未验证风险
- [ ] 所有验收脚本通过
- [ ] 打 tag 或至少提交 final delivery commit
- [ ] push GitHub

---

## 5. 禁止事项

- 禁止用"Phase 完成"代替验收通过
- 禁止继续批量扩库
- 禁止自评报告作为通过依据
- 禁止手写 brief 冒充接口输出
- 禁止把 feature-based inspiration 写成 direct evidence
- 禁止 README、HANDOFF、ADRMATS_INTEGRATION 三处维护互相矛盾的状态

---

## 6. 当前状态

**最新 commit**：f47a3af
**分支**：feature/extraction-results

**已完成**：
- 校验错误：0
- chimera 违规：0
- 污染物名称：已统一
- 匹配规则：已数据化
- 五个金标准：10/10 通过

**待完成**：
- Milestone 0-4

---

*本文档是唯一执行入口，所有工作以本文档为准。*
