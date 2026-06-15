#!/usr/bin/env python3
"""
Phase 7: 为所有 active 原型写 design_translation。

规则（DEFINITIONS §2, §6）：
1. 每条必须包含三要素：specific_functional_group / material_handle / target_interaction
2. 不得命中禁用泛词
3. source_tier: literature（有 DOI）或 llm_inference
"""

import json
import os
import sys
from pathlib import Path

BANNED_PHRASES = [
    '良好的吸附性能', '优异的', '广泛的应用前景', '具有潜力',
    '提高效率', '绿色环保', '多种污染物', '协同效应'
]

# 每个原型的 translation 定义
TRANSLATIONS = {
    'mussel-foot-adhesion': [
        {
            'idea': '利用贻贝足丝蛋白 DOPA 的邻苯二酚基团进行表面功能化，通过双齿配位捕获软金属离子',
            'specific_functional_group': '邻苯二酚（catechol）基团，pKa ~9.5',
            'material_handle': '聚多巴胺（PDA）涂层或多巴胺改性聚合物',
            'target_interaction': '与 Pb²⁺、Cu²⁺、UO₂²⁺ 等软金属离子形成五元螯合环（log K 10-20）',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1126/science.1145492']
        },
        {
            'idea': '利用酰胺肟基团对铀酰离子的高选择性配位，实现海水中 ppb 级铀的捕获',
            'specific_functional_group': '酰胺肟基团（-C(=NOH)NH₂），η2 配位模式',
            'material_handle': '聚丙烯腈（PAN）接枝酰胺肟化，或 PDA 前驱体合成',
            'target_interaction': '与 UO₂²⁺ 形成 η2 配位络合物，在海水 pH 8.3 下稳定',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.ccr.2023.215234']
        }
    ],
    'polydopamine-coating': [
        {
            'idea': '利用 PDA 涂层的邻苯二酚和胺基双功能基团进行表面改性，实现普适性粘附和污染物捕获',
            'specific_functional_group': '邻苯二酚 + 胺基（-NH₂）双官能团',
            'material_handle': '多巴胺在弱碱性（pH 8.5）条件下自聚成 PDA 涂层',
            'target_interaction': '邻苯二酚配位金属离子，胺基捕获阴离子污染物',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1126/science.1145492']
        }
    ],
    'chitosan': [
        {
            'idea': '利用壳聚糖的氨基和羟基进行络合吸附，pH 响应控制吸附/脱附',
            'specific_functional_group': '氨基（-NH₂）和羟基（-OH），pKa ~6.3',
            'material_handle': '壳聚糖直接使用或交联改性（如戊二醛、环氧氯丙烷）',
            'target_interaction': '氨基质子化后静电吸引阴离子，羟基配位金属离子',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.ijbiomac.2019.01.010']
        }
    ],
    'chlorella-cell-wall': [
        {
            'idea': '利用小球藻细胞壁的多糖和蛋白质进行重金属吸附',
            'specific_functional_group': '羧基（-COOH）、氨基（-NH₂）、磷酸基',
            'material_handle': '小球藻生物质直接使用或固定化处理',
            'target_interaction': '羧基和氨基配位重金属离子，磷酸基增强结合',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'diatom-frustule': [
        {
            'idea': '利用硅藻土的多孔结构和表面硅羟基进行吸附和过滤',
            'specific_functional_group': '硅羟基（Si-OH），高比表面积（20-200 m²/g）',
            'material_handle': '硅藻土直接使用或酸活化/改性处理',
            'target_interaction': '硅羟基通过氢键和静电作用吸附污染物',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.jhazmat.2022.128658']
        }
    ],
    'bone-structure': [
        {
            'idea': '利用羟基磷灰石的钙磷结构进行重金属和氟离子吸附',
            'specific_functional_group': '羟基磷灰石（HAp）的 Ca²⁺ 和 PO₄³⁻ 位点',
            'material_handle': '合成羟基磷灰石粉末或涂层',
            'target_interaction': 'Ca²⁺ 位点配位 F⁻、Pb²⁺，PO₄³⁻ 位点捕获阳离子',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.jece.2021.106072']
        }
    ],
    'oyster-shell': [
        {
            'idea': '利用牡蛎壳的方解石结构进行重金属固定和pH缓冲',
            'specific_functional_group': '方解石/文石型 CaCO₃',
            'material_handle': '牡蛎壳粉碎、煅烧或酸活化',
            'target_interaction': 'CaCO₃ 溶解提供 CO₃²⁻ 和 Ca²⁺，沉淀重金属碳酸盐',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.jenvman.2017.06.047']
        }
    ],
    'scallop-shell': [
        {
            'idea': '利用扇贝壳的层状结构和 CaCO₃ 进行污染物固定',
            'specific_functional_group': '方解石型 CaCO₃，层状有机基质',
            'material_handle': '扇贝壳粉碎、热处理或复合改性',
            'target_interaction': 'CaCO₃ 溶解沉淀重金属，层状结构提供物理吸附位点',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'fish-scale-hydroxyapatite': [
        {
            'idea': '利用鱼鳞羟基磷灰石的多孔结构和 Ca/P 位点进行吸附',
            'specific_functional_group': '鱼鳞衍生 HAp 的 Ca²⁺ 和 PO₄³⁻ 位点',
            'material_handle': '鱼鳞热处理转化为羟基磷灰石',
            'target_interaction': 'Ca²⁺ 配位 F⁻ 和重金属，PO₄³⁻ 捕获阳离子',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.jclepro.2022.132234']
        }
    ],
    'mangrove-root': [
        {
            'idea': '利用红树林根系的多孔结构和表面官能团进行污染物过滤和吸附',
            'specific_functional_group': '木质素衍生的酚羟基和羧基',
            'material_handle': '红树林生物质碳化或直接使用',
            'target_interaction': '酚羟基和羧基配位重金属离子，多孔结构物理截留',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'mycelium': [
        {
            'idea': '利用真菌菌丝体的几丁质和葡聚糖进行重金属吸附',
            'specific_functional_group': '几丁质的氨基和羟基，β-葡聚糖的羟基',
            'material_handle': '真菌菌丝体培养、固定化或改性',
            'target_interaction': '氨基和羟基配位重金属离子，生物降解性好',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.biortech.2021.125015']
        }
    ],
    'wood-xylem': [
        {
            'idea': '利用木材木质部的纤维素和木质素进行吸附和过滤',
            'specific_functional_group': '纤维素的羟基，木质素的酚羟基',
            'material_handle': '木材切片、碳化或化学改性',
            'target_interaction': '羟基通过氢键吸附极性污染物，多孔结构物理过滤',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'silk-fibroin': [
        {
            'idea': '利用丝素蛋白的 β-折叠结构和氨基酸侧链进行吸附',
            'specific_functional_group': '丝氨酸（Ser）的羟基，酪氨酸（Tyr）的酚羟基',
            'material_handle': '丝素蛋白提取、再生或交联成型',
            'target_interaction': '羟基和酚羟基配位金属离子，β-折叠提供结构稳定性',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.ijbiomac.2022.05.184']
        }
    ],
    'spider-silk': [
        {
            'idea': '利用蜘蛛丝的高强度和表面官能团进行污染物捕获',
            'specific_functional_group': '丝蛋白的酰胺基和羧基',
            'material_handle': '重组蜘蛛丝蛋白或仿生纺丝',
            'target_interaction': '酰胺基和羧基配位金属离子，高强度支撑过滤应用',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'dna-aptamer': [
        {
            'idea': '利用 DNA 适配体的特异性识别和结合能力进行目标污染物检测和捕获',
            'specific_functional_group': '适配体的碱基序列形成的三维构象',
            'material_handle': '化学合成适配体，固定化在载体上',
            'target_interaction': '适配体与目标分子的特异性结合（Kd 纳摩尔级）',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1021/acs.analchem.1c02364']
        }
    ],
    'biomineralization-template': [
        {
            'idea': '利用生物矿化模板控制无机材料的形貌和晶相',
            'specific_functional_group': '有机基质的官能团（羧基、磷酸基）',
            'material_handle': '有机模板（蛋白质、多糖）引导矿化',
            'target_interaction': '有机基质的官能团控制无机相的成核和生长',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'plant-tannin': [
        {
            'idea': '利用植物单宁的多酚结构进行金属离子络合和蛋白质沉淀',
            'specific_functional_group': '邻苯二酚和没食子酰基（galloyl）',
            'material_handle': '单宁酸直接使用或固定化在载体上',
            'target_interaction': '多酚基团与金属离子形成配位络合物，与蛋白质形成氢键',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.cej.2022.136395']
        }
    ],
    'cell-membrane-ion-channel': [
        {
            'idea': '利用细胞膜离子通道的选择性传输机制设计分离膜',
            'specific_functional_group': '通道蛋白的亲水孔道和电荷选择性滤器',
            'material_handle': '仿生纳米通道膜或离子印迹聚合物',
            'target_interaction': '基于尺寸和电荷的离子选择性传输',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'sulfate-reducing-bacteria': [
        {
            'idea': '利用硫酸盐还原菌的代谢产物（H₂S）沉淀重金属',
            'specific_functional_group': 'H₂S/HS⁻ 的硫基（-S²⁻）',
            'material_handle': 'SRB 培养、固定化或生物反应器',
            'target_interaction': 'S²⁻ 与重金属形成难溶硫化物（如 CuS、PbS）',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.jhazmat.2021.126058']
        }
    ],
    'iron-oxidizing-bacteria': [
        {
            'idea': '利用铁氧化菌生成的施氏矿物进行重金属吸附和共沉淀',
            'specific_functional_group': '施氏矿物（schwertmannite）的 Fe-O/OH 位点',
            'material_handle': 'IOB 培养生成施氏矿物，或合成类似结构',
            'target_interaction': 'Fe-O/OH 位点吸附 As(V)、Cr(VI) 等阴离子重金属',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1016/j.watres.2021.117201']
        }
    ],
    'coral-skeleton': [
        {
            'idea': '利用珊瑚骨骼的文石结构进行重金属固定',
            'specific_functional_group': '文石型 CaCO₃ 的 Ca²⁺ 位点',
            'material_handle': '珊瑚骨骼粉末或合成文石',
            'target_interaction': 'Ca²⁺ 位点吸附和共沉淀重金属碳酸盐',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'magnetic-bacteria': [
        {
            'idea': '利用磁性细菌的磁小体进行磁分离和污染物吸附',
            'specific_functional_group': '磁小体（magnetosome）的 Fe₃O₄ 核心',
            'material_handle': '磁性细菌培养提取磁小体，或仿生合成磁性纳米粒子',
            'target_interaction': 'Fe₃O₄ 表面羟基吸附重金属，磁性实现快速分离',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ],
    'pitcher-plant-slippery-surface': [
        {
            'idea': '利用猪笼草的滑溜表面设计防污和自清洁材料',
            'specific_functional_group': '光滑蜡质表面的低表面能基团',
            'material_handle': 'SLIPS 液体灌注多孔表面',
            'target_interaction': '超滑表面阻止污染物附着，实现自清洁',
            'source_tier': 'literature',
            'examples': ['DOI: 10.1038/nature10856']
        }
    ],
    'lobster-exoskeleton': [
        {
            'idea': '利用龙虾外骨骼的几丁质-蛋白质复合结构设计高强度吸附材料',
            'specific_functional_group': '几丁质的乙酰氨基和羟基',
            'material_handle': '几丁质提取、脱乙酰化或复合改性',
            'target_interaction': '乙酰氨基和羟基配位重金属，层状结构提供机械强度',
            'source_tier': 'llm_inference',
            'examples': []
        }
    ]
}

def validate_translation(pid: str, t: dict) -> list:
    """验证单条 translation 是否合格。"""
    issues = []

    # 检查三要素
    required = ['specific_functional_group', 'material_handle', 'target_interaction']
    for field in required:
        if not t.get(field):
            issues.append(f'缺少字段: {field}')

    # 检查禁用泛词
    idea = t.get('idea', '')
    for phrase in BANNED_PHRASES:
        if phrase in idea:
            issues.append(f'命中禁用泛词: "{phrase}"')

    # 检查 source_tier
    if t.get('source_tier') == 'literature' and not t.get('examples'):
        issues.append('source_tier=literature 但无 examples/DOI')

    return issues


def main():
    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = repo_dir / 'prototypes_db'

    results = []
    total_written = 0
    total_qualified = 0
    total_unqualified = 0

    # 遍历所有 active 原型
    for fname in sorted(os.listdir(db_dir)):
        if not fname.endswith('.json'):
            continue
        pid = fname.replace('.json', '')

        # 跳过非 active 原型
        if pid in ['materials_reference', 'parked']:
            continue

        fpath = db_dir / fname
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 获取 translation 定义
        translations_def = TRANSLATIONS.get(pid)
        if not translations_def:
            results.append({'pid': pid, 'status': 'NO_DEFINITION', 'issues': ['无 translation 定义']})
            continue

        # 写入 translation
        data['design_translation'] = translations_def

        # 验证
        qualified = 0
        unqualified = 0
        for i, t in enumerate(translations_def):
            issues = validate_translation(pid, t)
            if issues:
                unqualified += 1
                results.append({'pid': pid, 'index': i, 'status': 'UNQUALIFIED', 'issues': issues})
            else:
                qualified += 1

        # 写回文件
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        total_written += len(translations_def)
        total_qualified += qualified
        total_unqualified += unqualified

        status = 'OK' if unqualified == 0 else 'PARTIAL'
        results.append({'pid': pid, 'status': status, 'qualified': qualified, 'unqualified': unqualified})

    # 输出报告
    print('\n=== Phase 7 Translation 写入报告 ===\n')

    for r in results:
        if r['status'] == 'NO_DEFINITION':
            print(f'⚠️ {r["pid"]}: 无 translation 定义')
        elif r['status'] == 'UNQUALIFIED':
            print(f'❌ {r["pid"]}[{r["index"]}]: {" | ".join(r["issues"])}')
        else:
            icon = '✅' if r.get('unqualified', 0) == 0 else '⚠️'
            print(f'{icon} {r["pid"]}: {r.get("qualified", 0)} 合格, {r.get("unqualified", 0)} 不合格')

    print(f'\n=== 总结 ===')
    print(f'写入条数: {total_written}')
    print(f'合格: {total_qualified}')
    print(f'不合格: {total_unqualified}')

    if total_unqualified > 0:
        print(f'\n❌ 存在不合格 translation')
        sys.exit(1)
    else:
        print(f'\n✅ 全部合格')
        sys.exit(0)


if __name__ == '__main__':
    main()
