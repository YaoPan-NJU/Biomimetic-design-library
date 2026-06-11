#!/usr/bin/env python3
"""
批量核查 prototypes_db 中的性能数据。

核查方法：
1. 找到每条 performance_data 对应的 PDF 文件
2. 用 pdftotext 提取 PDF 全文
3. 在全文中搜索关键数值（qmax、去除率等）
4. 找到 → verified，未找到 → needs_review

依赖：pdftotext（poppler-utils）
"""

import json
import os
import re
import glob
import subprocess
from pathlib import Path
from collections import defaultdict


def find_pdf(source_file: str, pdf_cache: dict) -> str:
    """根据 source_file 找到实际 PDF 路径。"""
    if not source_file:
        return None

    basename = source_file.split('/')[-1]

    # 精确匹配
    if basename in pdf_cache:
        return pdf_cache[basename]

    # 加" 2"后缀
    with_suffix = basename.replace('.pdf', ' 2.pdf')
    if with_suffix in pdf_cache:
        return pdf_cache[with_suffix]

    # 加" 3"后缀
    with_suffix3 = basename.replace('.pdf', ' 3.pdf')
    if with_suffix3 in pdf_cache:
        return pdf_cache[with_suffix3]

    # 模糊匹配（文件名包含 basename 的核心部分）
    core = basename.replace('.pdf', '').replace(' 2', '').replace(' 3', '')
    for cache_name, cache_path in pdf_cache.items():
        if core[:30] in cache_name:
            return cache_path

    return None


def extract_text(pdf_path: str) -> str:
    """用 pdftotext 提取 PDF 文本。"""
    try:
        result = subprocess.run(
            ['pdftotext', pdf_path, '-'],
            capture_output=True, text=True, timeout=30
        )
        return result.stdout
    except Exception as e:
        return ''


def extract_numbers(value_str: str) -> list:
    """从 value 字符串中提取数值。"""
    if not value_str:
        return []

    numbers = []
    # 匹配各种数值格式
    patterns = [
        r'(\d+\.?\d*)\s*mg/g',
        r'(\d+\.?\d*)\s*%',
        r'(\d+\.?\d*)\s*mg/L',
        r'(\d+\.?\d*)\s*g/g',
        r'=\s*(\d+\.?\d*)',
        r'(\d+\.?\d+)',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, str(value_str))
        for m in matches:
            try:
                val = float(m)
                if 0.01 < val < 100000:  # 合理范围
                    numbers.append(val)
            except:
                pass

    return list(set(numbers))


def verify_item(text: str, item: dict) -> dict:
    """验证单条性能数据是否在 PDF 文本中出现。"""
    numbers = extract_numbers(item.get('value', ''))
    param = item.get('parameter', '')

    found_numbers = []
    missing_numbers = []

    for num in numbers:
        # 搜索数值（允许小的格式差异）
        num_str = f'{num:.2f}' if num != int(num) else str(int(num))
        num_str_int = str(int(num))

        if num_str in text or num_str_int in text:
            found_numbers.append(num)
        else:
            # 尝试搜索整数部分
            if re.search(rf'\b{int(num)}\b', text):
                found_numbers.append(num)
            else:
                missing_numbers.append(num)

    # 也搜索关键词
    param_keywords = []
    if 'qmax' in param.lower() or 'adsorption capacity' in param.lower():
        param_keywords.append('qmax')
    if 'removal' in param.lower() or '去除率' in param:
        param_keywords.append('removal')

    keyword_found = True
    for kw in param_keywords:
        if kw.lower() not in text.lower():
            keyword_found = False

    # 判定
    if numbers:
        if len(found_numbers) >= len(numbers) * 0.5:  # 至少一半数值找到
            return {'status': 'verified', 'found': found_numbers, 'missing': missing_numbers}
        elif found_numbers:
            return {'status': 'partial', 'found': found_numbers, 'missing': missing_numbers}
        else:
            return {'status': 'needs_review', 'found': [], 'missing': missing_numbers}
    elif keyword_found and param_keywords:
        return {'status': 'verified', 'found': [], 'missing': []}
    else:
        return {'status': 'needs_review', 'found': [], 'missing': []}


def main():
    import argparse
    parser = argparse.ArgumentParser(description='批量核查性能数据')
    parser.add_argument('--db-dir', default=None, help='prototypes_db 目录')
    parser.add_argument('--prototype', default=None, help='只核查指定原型')
    parser.add_argument('--dry-run', action='store_true', help='只统计不更新')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = Path(args.db_dir) if args.db_dir else repo_dir / 'prototypes_db'

    # 构建 PDF 索引
    print('构建 PDF 索引...')
    pdf_cache = {}
    for root, dirs, files in os.walk(str(repo_dir / '仿生文献库')):
        for fname in files:
            if fname.lower().endswith('.pdf'):
                pdf_cache[fname] = os.path.join(root, fname)

    print(f'PDF 文件: {len(pdf_cache)}')

    # PDF 文本缓存（避免重复读取）
    text_cache = {}

    # 核查每个原型
    targets = sorted(glob.glob(str(db_dir / '*.json')))
    if args.prototype:
        targets = [str(db_dir / f'{args.prototype}.json')]

    total_items = 0
    verified = 0
    needs_review = 0
    partial = 0
    no_pdf = 0
    updated = 0

    for jf in targets:
        with open(jf, 'r', encoding='utf-8') as f:
            d = json.load(f)

        pid = d['id']
        items = d.get('performance_data', [])

        if not items:
            continue

        print(f'\n=== {pid} ({len(items)} items) ===')

        proto_verified = 0
        proto_needs_review = 0
        proto_partial = 0
        proto_no_pdf = 0

        for item in items:
            total_items += 1
            sf = item.get('source_file', '')
            pdf_path = find_pdf(sf, pdf_cache)

            if not pdf_path:
                proto_no_pdf += 1
                no_pdf += 1
                if not args.dry_run:
                    item['verification'] = 'needs_review'
                continue

            # 缓存 PDF 文本
            if pdf_path not in text_cache:
                text_cache[pdf_path] = extract_text(pdf_path)
            text = text_cache[pdf_path]

            if not text:
                proto_no_pdf += 1
                no_pdf += 1
                if not args.dry_run:
                    item['verification'] = 'needs_review'
                continue

            result = verify_item(text, item)

            if result['status'] == 'verified':
                proto_verified += 1
                verified += 1
                if not args.dry_run:
                    item['verification'] = 'verified'
            elif result['status'] == 'partial':
                proto_partial += 1
                partial += 1
                if not args.dry_run:
                    item['verification'] = 'needs_review'
            else:
                proto_needs_review += 1
                needs_review += 1
                if not args.dry_run:
                    item['verification'] = 'needs_review'

        print(f'  verified: {proto_verified}, partial: {proto_partial}, needs_review: {proto_needs_review}, no_pdf: {proto_no_pdf}')

        # 保存更新
        if not args.dry_run:
            d['provenance_summary']['n_verified'] = sum(
                1 for p in d.get('performance_data', []) if p.get('verification') == 'verified'
            )
            d['provenance_summary']['n_unverified'] = sum(
                1 for p in d.get('performance_data', []) if p.get('verification') != 'verified'
            )
            with open(jf, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            updated += 1

    # 总结
    print(f'\n{"="*50}')
    print(f'核查完成')
    print(f'  总条目: {total_items}')
    print(f'  verified: {verified} ({verified/total_items*100:.1f}%)')
    print(f'  partial: {partial} ({partial/total_items*100:.1f}%)')
    print(f'  needs_review: {needs_review} ({needs_review/total_items*100:.1f}%)')
    print(f'  no_pdf: {no_pdf} ({no_pdf/total_items*100:.1f}%)')
    if not args.dry_run:
        print(f'  更新文件: {updated}')
    print(f'  PDF 缓存: {len(text_cache)} files')


if __name__ == '__main__':
    main()
