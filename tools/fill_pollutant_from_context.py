#!/usr/bin/env python3
"""
从 context 中回填 pollutant 字段
"""

import json
import os
import re

# 常见污染物关键词
POLLUTANT_KEYWORDS = {
    'Pb': ['Pb(II)', 'Pb2+', 'lead', '铅'],
    'Cd': ['Cd(II)', 'Cd2+', 'cadmium', '镉'],
    'Cr': ['Cr(VI)', 'Cr(III)', 'Cr6+', 'chromium', '铬'],
    'Cu': ['Cu(II)', 'Cu2+', 'copper', '铜'],
    'Ni': ['Ni(II)', 'Ni2+', 'nickel', '镍'],
    'Zn': ['Zn(II)', 'Zn2+', 'zinc', '锌'],
    'Hg': ['Hg(II)', 'Hg2+', 'mercury', '汞'],
    'As': ['As(III)', 'As(V)', 'arsenic', '砷'],
    'MB': ['Methylene Blue', '亚甲基蓝', 'MB'],
    'RhB': ['Rhodamine B', '罗丹明B', 'RhB'],
    'MO': ['Methyl Orange', '甲基橙', 'MO'],
    'Cr(VI)': ['Cr(VI)', 'Cr6+', 'hexavalent chromium', '六价铬'],
    'U': ['U(VI)', 'uranyl', '铀'],
}

def extract_pollutant_from_context(context):
    """从 context 中提取 pollutant"""
    if not context:
        return ''
    
    context_str = json.dumps(context, ensure_ascii=False).lower()
    
    # 尝试从 context 中提取 pollutant
    for pollutant, keywords in POLLUTANT_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in context_str:
                return pollutant
    
    return ''

def fill_pollutant_for_prototype(filepath):
    """为单个原型填充 pollutant"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    perf = data.get('performance_data', [])
    filled_count = 0
    
    for p in perf:
        if not p.get('pollutant'):
            # 尝试从 context 中提取
            context = p.get('context', {})
            pollutant = extract_pollutant_from_context(context)
            
            if pollutant:
                p['pollutant'] = pollutant
                filled_count += 1
    
    if filled_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    return filled_count

def main():
    """主函数"""
    top_level_dir = 'prototypes_db'
    top_files = [f for f in os.listdir(top_level_dir) if f.endswith('.json') and os.path.isfile(os.path.join(top_level_dir, f))]
    
    total_filled = 0
    
    for f in sorted(top_files):
        filepath = os.path.join(top_level_dir, f)
        try:
            filled = fill_pollutant_for_prototype(filepath)
            if filled > 0:
                print(f'✓ {f}: 填充 {filled} 条 pollutant')
                total_filled += filled
        except Exception as e:
            print(f'❌ {f}: 处理失败: {e}')
    
    print(f'\n总计填充 {total_filled} 条 pollutant')

if __name__ == '__main__':
    main()
