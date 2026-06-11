#!/usr/bin/env python3
"""
用 pollutant_aliases.json 标准化 pollutant 名称
"""

import json
import os

def load_aliases():
    """加载 pollutant 别名映射"""
    with open('pollutant_aliases.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 构建别名到标准名的映射
    alias_map = {}
    for canonical, info in data.get('aliases', {}).items():
        for alias in info.get('aliases', []):
            alias_map[alias.lower()] = canonical
    
    return alias_map

def standardize_pollutant(pollutant, alias_map):
    """标准化 pollutant 名称"""
    if not pollutant:
        return pollutant
    
    # 尝试精确匹配
    lower_pollutant = pollutant.lower()
    if lower_pollutant in alias_map:
        return alias_map[lower_pollutant]
    
    # 尝试部分匹配
    for alias, canonical in alias_map.items():
        if alias in lower_pollutant or lower_pollutant in alias:
            return canonical
    
    return pollutant

def standardize_prototype(filepath, alias_map):
    """标准化单个原型的 pollutant"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    perf = data.get('performance_data', [])
    standardized_count = 0
    
    for p in perf:
        old_pollutant = p.get('pollutant', '')
        if old_pollutant:
            new_pollutant = standardize_pollutant(old_pollutant, alias_map)
            if new_pollutant != old_pollutant:
                p['pollutant'] = new_pollutant
                standardized_count += 1
    
    if standardized_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    return standardized_count

def main():
    """主函数"""
    alias_map = load_aliases()
    print(f'加载 {len(alias_map)} 个别名映射')
    
    top_level_dir = 'prototypes_db'
    top_files = [f for f in os.listdir(top_level_dir) if f.endswith('.json') and os.path.isfile(os.path.join(top_level_dir, f))]
    
    total_standardized = 0
    
    for f in sorted(top_files):
        filepath = os.path.join(top_level_dir, f)
        try:
            standardized = standardize_prototype(filepath, alias_map)
            if standardized > 0:
                print(f'✓ {f}: 标准化 {standardized} 条 pollutant')
                total_standardized += standardized
        except Exception as e:
            print(f'❌ {f}: 处理失败: {e}')
    
    print(f'\n总计标准化 {total_standardized} 条 pollutant')

if __name__ == '__main__':
    main()
