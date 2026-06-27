# 提参质量审计报告

日期: 2026-06-27
范围: 2879 篇论文, 27592 条 KI, 20 种污染物

## 总体质量评分

- 论文总数: 2879
- KI 总数: 27592
- 空结果论文: 360 (12.5%)
- 平均 KI/论文: 9.6

## 按污染物质量热力图

| 污染物 | 论文 | KI | 空论文 | DD异常修复 | conf<0.5 |
|--------|------|-----|--------|-----------|----------|
| 2,3,7,8-四氯二苯并-p-二噁英（TCDD） | 122 | 1221 | 2 | 见dd_fix_log | 1 |
| 2,6-二氯苯酚 | 13 | 188 | 0 | 见dd_fix_log | 0 |
| β-六氯环己烷 | 9 | 94 | 0 | 见dd_fix_log | 0 |
| 三氯甲烷 | 26 | 254 | 1 | 见dd_fix_log | 0 |
| 五氯苯酚 | 171 | 1812 | 1 | 见dd_fix_log | 2 |
| 全氟丁烷磺酸（PFBS） | 67 | 872 | 0 | 见dd_fix_log | 1 |
| 全氟己烷磺酸（PFHxS） | 33 | 428 | 0 | 见dd_fix_log | 0 |
| 全氟辛酸（PFOA） | 275 | 3185 | 10 | 见dd_fix_log | 3 |
| 六氟环氧丙烷二聚酸 | 32 | 440 | 0 | 见dd_fix_log | 0 |
| 六氯丁二烯 | 4 | 61 | 0 | 见dd_fix_log | 0 |
| 十溴二苯醚 | 236 | 2660 | 1 | 见dd_fix_log | 1 |
| 双酚A（BPA） | 1416 | 11800 | 286 | 见dd_fix_log | 12 |
| 壬基酚 | 152 | 1764 | 5 | 见dd_fix_log | 3 |
| 多氯联苯-209（PCB-209） | 2 | 19 | 0 | 见dd_fix_log | 0 |
| 奥克立林 | 8 | 78 | 0 | 见dd_fix_log | 0 |
| 滴滴伊（DDE） | 12 | 152 | 0 | 见dd_fix_log | 0 |
| 滴滴涕（DDT） | 230 | 1754 | 54 | 见dd_fix_log | 7 |
| 狄氏剂（Dieldrin） | 53 | 579 | 0 | 见dd_fix_log | 1 |
| 硫丹 | 8 | 98 | 0 | 见dd_fix_log | 0 |
| 罗红霉素 | 10 | 133 | 0 | 见dd_fix_log | 0 |

## domain_direction 分布

| domain_direction | KI 数 | 占比 |
|---|---|---|
| D1_adsorption_performance | 8241 | 29.9% |
| D4_adsorption_mechanism | 4767 | 17.3% |
| D11_pollutant_property | 3620 | 13.1% |
| D5_engineering_constraint | 3080 | 11.2% |
| D2_material_structure | 2899 | 10.5% |
| D12_occurrence_pattern | 2368 | 8.6% |
| D6_pollutant_application | 1371 | 5.0% |
| D8_characterization | 621 | 2.3% |
| D7_synthesis_method | 519 | 1.9% |
| D9_comparison_review | 106 | 0.4% |

## confidence 分布

| 范围 | KI 数 | 占比 | 处理方式 |
|---|---|---|---|
| >= 0.8 | 27005 | 97.9% | 正常参与聚合 |
| 0.5 - 0.79 | 556 | 2.0% | 参与聚合,标记low_confidence |
| < 0.5 | 31 | 0.1% | 不参与聚合,记录审计报告 |

## 已修复异常

- domain_direction 拼写错误: 25 条 KI 已修复 (见 audit/dd_fix_log.json)
- 修复映射: D1_engineering_constraint→D5 (12), D1_pollutant_application→D6 (5), D11_pollutant_application→D6 (4), 其他 (4)

## 数据完整性

- 字段缺失率: <0.1% (title 3, doi 4, abstract 9, year 4)
- KI 字段缺失: parameter 2, value 11, evidence 3, confidence 9
- 总体完整性评分: **99.9%**