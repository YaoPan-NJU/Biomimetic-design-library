#!/usr/bin/env python3
"""
修复 chimera 违规
从 mussel-foot-adhesion.json 移除 cellulose/nanocellulose 相关性能和机制
"""

import json
import os

def fix_mussel_foot_adhesion():
    """修复 mussel-foot-adhesion.json 中的 chimera 违规"""
    filepath = 'prototypes_db/mussel-foot-adhesion.json'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # cellulose 相关关键词
    cellulose_keywords = [
        'cellulose', 'nanocellulose', 'CNF', 'CNC', 'BC', 'bacterial cellulose',
        'carboxymethyl', 'CMC', 'hydroxyethyl', 'HEC', 'methylcellulose',
        'nanofibril', 'nanocrystal', 'fibril'
    ]
    
    # 移除 cellulose 相关性能数据
    original_perf_count = len(data.get('performance_data', []))
    cleaned_perf = []
    removed_perf = []
    
    for p in data.get('performance_data', []):
        param = (p.get('parameter', '') or '').lower()
        material = (p.get('material', '') or '').lower()
        pollutant = (p.get('pollutant', '') or '').lower()
        
        is_cellulose = False
        for kw in cellulose_keywords:
            if kw.lower() in param or kw.lower() in material:
                is_cellulose = True
                break
        
        if is_cellulose:
            removed_perf.append(p)
        else:
            cleaned_perf.append(p)
    
    data['performance_data'] = cleaned_perf
    
    # 移除 cellulose 相关机制
    original_mech_count = len(data.get('mechanisms', []))
    cleaned_mechs = []
    removed_mechs = []
    
    for m in data.get('mechanisms', []):
        name = (m.get('name', '') or '').lower()
        desc = (m.get('description', '') or '').lower()
        
        is_cellulose = False
        for kw in cellulose_keywords:
            if kw.lower() in name or kw.lower() in desc:
                is_cellulose = True
                break
        
        if is_cellulose:
            removed_mechs.append(m)
        else:
            cleaned_mechs.append(m)
    
    data['mechanisms'] = cleaned_mechs
    
    # 保存修复后的文件
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f'修复 {filepath}:')
    print(f'  性能数据: {original_perf_count} -> {len(cleaned_perf)} (移除 {len(removed_perf)})')
    print(f'  机制: {original_mech_count} -> {len(cleaned_mechs)} (移除 {len(removed_mechs)})')
    
    return removed_perf, removed_mechs

if __name__ == '__main__':
    removed_perf, removed_mechs = fix_mussel_foot_adhesion()
    
    if removed_perf:
        print('\n移除的性能数据:')
        for p in removed_perf[:5]:
            print(f'  - {p.get("parameter", "")}: {p.get("value", "")}')
    
    if removed_mechs:
        print('\n移除的机制:')
        for m in removed_mechs[:5]:
            print(f'  - {m.get("name", "")}')
