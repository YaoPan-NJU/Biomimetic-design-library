#!/usr/bin/env python3
"""
修复 organism 映射错误
建立 organism 修正表
"""

import json
import os

# organism 修正表
ORGANISM_CORRECTIONS = {
    'cellulose-nanocrystal': {
        'scientific': 'Cellulose sources (纤维素来源)',
        'category': '植物'
    },
    'namib-beetle': {
        'scientific': 'Stenocara gracilipes (纳米布甲虫)',
        'category': '动物'
    },
    'metal-organ框架-framework': {
        'scientific': 'Synthetic material (合成材料)',
        'category': '仿生材料'
    },
    'fish-scale-hydroxyapatite': {
        'scientific': 'Fish scales (鱼鳞)',
        'category': '动物'
    },
    'biomineralization-template': {
        'scientific': 'Biomineralization organisms (生物矿化生物)',
        'category': '仿生材料'
    },
    'bone-structure': {
        'scientific': 'Mammalian bone (哺乳动物骨骼)',
        'category': '动物'
    },
    'coral-skeleton': {
        'scientific': 'Corallium (珊瑚)',
        'category': '动物'
    },
    'diatom-inspired-porous': {
        'scientific': 'Bacillariophyta (硅藻门)',
        'category': '微生物'
    },
    'dna-aptamer': {
        'scientific': 'Synthetic DNA (合成DNA)',
        'category': '仿生材料'
    },
    'lobster-exoskeleton': {
        'scientific': 'Homarus americanus (美洲龙虾)',
        'category': '动物'
    },
    'silkworm-silk': {
        'scientific': 'Bombyx mori (家蚕)',
        'category': '动物'
    }
}

def fix_organism_mapping():
    """修复 organism 映射"""
    top_level_dir = 'prototypes_db'
    fixed_count = 0
    
    for filename, correction in ORGANISM_CORRECTIONS.items():
        filepath = os.path.join(top_level_dir, f'{filename}.json')
        if not os.path.exists(filepath):
            print(f'⚠️ {filepath} 不存在，跳过')
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            old_organism = data.get('organism', {})
            data['organism'] = correction
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f'✓ {filename}: {old_organism.get("scientific", "空")} -> {correction["scientific"]}')
            fixed_count += 1
        except Exception as e:
            print(f'❌ {filename}: 修复失败: {e}')
    
    print(f'\n总计修复 {fixed_count} 个原型')

if __name__ == '__main__':
    fix_organism_mapping()
