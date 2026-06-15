#!/usr/bin/env python3
"""
从 parameter, value, material 中智能提取 pollutant
"""

import json
import os
import re

# 污染物模式
POLLUTANT_PATTERNS = [
    # 重金属
    (r'Pb\(II\)|Pb2\+|lead|铅', 'Pb(II)'),
    (r'Cd\(II\)|Cd2\+|cadmium|镉', 'Cd(II)'),
    (r'Cr\(VI\)|Cr6\+|hexavalent chromium|六价铬', 'Cr(VI)'),
    (r'Cr\(III\)|Cr3\+|chromium|铬', 'Cr(III)'),
    (r'Cu\(II\)|Cu2\+|copper|铜', 'Cu(II)'),
    (r'Ni\(II\)|Ni2\+|nickel|镍', 'Ni(II)'),
    (r'Zn\(II\)|Zn2\+|zinc|锌', 'Zn(II)'),
    (r'Hg\(II\)|Hg2\+|mercury|汞', 'Hg(II)'),
    (r'As\(III\)|As3\+|arsenic|砷', 'As(III)'),
    (r'U\(VI\)|uranyl|铀', 'U(VI)'),
    (r'Ag\(I\)|Ag\+|silver|银', 'Ag(I)'),
    
    # 染料
    (r'Methylene Blue|亚甲基蓝|MB', 'Methylene Blue'),
    (r'Rhodamine B|罗丹明B|RhB', 'Rhodamine B'),
    (r'Methyl Orange|甲基橙|MO', 'Methyl Orange'),
    (r'Crystal Violet|结晶紫|CV', 'Crystal Violet'),
    (r'Congo Red|刚果红|CR', 'Congo Red'),
    (r'Reactive Red|活性红', 'Reactive Red'),
    (r'Reactive Blue|活性蓝', 'Reactive Blue'),
    (r'Reactive Yellow|活性黄', 'Reactive Yellow'),
    
    # 其他
    (r'ammonia|氨|NH3', 'Ammonia'),
    (r'phosphate|磷酸盐|PO4', 'Phosphate'),
    (r'nitrate|硝酸盐|NO3', 'Nitrate'),
    (r'fluoride|氟化物|F-', 'Fluoride'),
    (r'phenol|苯酚', 'Phenol'),
    (r'tetracycline|四环素|TC', 'Tetracycline'),
    (r'ciprofloxacin|环丙沙星|CIP', 'Ciprofloxacin'),
    (r'sulfamethoxazole|磺胺甲恶唑|SMX', 'Sulfamethoxazole'),
    (r'bisphenol A|双酚A|BPA', 'Bisphenol A'),
    (r'PFOA|全氟辛酸', 'PFOA'),
    (r'PFOS|全氟辛烷磺酸', 'PFOS'),
    (r'oil|油', 'Oil'),
    (r'dye|染料', 'Dye'),
]

def extract_pollutant_from_text(text):
    """从文本中提取 pollutant"""
    if not text:
        return ''
    
    text_lower = text.lower()
    
    for pattern, pollutant in POLLUTANT_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
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
            # 从 parameter, value, material 中提取
            text = f'{p.get("parameter", "")} {p.get("value", "")} {p.get("material", "")}'
            pollutant = extract_pollutant_from_text(text)
            
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
