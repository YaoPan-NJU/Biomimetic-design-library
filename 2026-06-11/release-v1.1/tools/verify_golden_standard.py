#!/usr/bin/env python3
"""
金标准核查脚本（P0-3）。

对 performance_data 逐条核查：
1. 解析 ref_doi (Crossref/web) → 确认文献存在
2. 检查 source_file 是否存在
3. 标记 verification 状态

verification 取值：
- verified: 完整开 PDF 核对通过（需人工确认）
- corroborated: ≥2 篇独立报道同一值
- single_source: 仅 1 篇报道
- unverified: 未核实
- needs_review: 有疑点

本脚本只做自动检查（DOI 在场、source_file 存在），
真正的"开 PDF 核对数值"需要人工或 agentic 核查。
"""

import json
import os
import sys
import re
import argparse
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError
import time


def check_doi_exists(doi: str) -> bool:
    """检查 DOI 是否可解析（Crossref API）。"""
    if not doi:
        return False

    # 清理 DOI
    doi = doi.strip()
    if doi.startswith('http'):
        doi = doi.split('doi.org/')[-1] if 'doi.org/' in doi else doi

    try:
        url = f'https://api.crossref.org/works/{doi}'
        req = urlopen(url, timeout=10)
        return req.status == 200
    except:
        return False


def check_source_file(source_file: str, repo_root: str) -> bool:
    """检查 source_file 是否存在。"""
    if not source_file:
        return False

    # 尝试多种路径
    candidates = [
        source_file,
        os.path.join(repo_root, source_file),
        os.path.join(repo_root, 'tools', 'litextract', source_file),
        os.path.join(repo_root, '仿生文献库', '论文', source_file),
        os.path.join(repo_root, '仿生文献库', '专利', source_file),
        os.path.join(repo_root, '仿生文献库', '标准', source_file),
    ]

    # 也尝试在子目录中查找（包括 " 2" / " 3" 后缀）
    lit_dir = os.path.join(repo_root, '仿生文献库')
    if os.path.exists(lit_dir):
        for root, dirs, files in os.walk(lit_dir):
            if source_file in files:
                return True
            # 检查 " 2" / " 3" 后缀
            stem = source_file.replace('.pdf', '')
            for suffix in [' 2.pdf', ' 3.pdf']:
                if stem + suffix in files:
                    return True

    for path in candidates:
        if os.path.exists(path):
            return True

    return False


def verify_entry(entry: dict, repo_root: str, check_doi: bool = False) -> dict:
    """核查单条性能数据。"""
    result = {
        'pollutant': entry.get('pollutant', ''),
        'value': entry.get('value', ''),
        'material': entry.get('material', ''),
        'ref_doi': entry.get('ref_doi', ''),
        'source_file': entry.get('source_file', ''),
        'issues': [],
    }

    # 检查 ref_doi
    ref_doi = entry.get('ref_doi')
    has_doi = bool(ref_doi and ref_doi.strip())

    # 检查 source_file
    source_file = entry.get('source_file')
    has_sf = check_source_file(source_file, repo_root)

    # 检查 pollutant
    has_pollutant = bool(entry.get('pollutant') and entry.get('pollutant').strip())

    # 检查 value
    has_value = bool(entry.get('value') and str(entry.get('value')).strip())

    # 判定 verification
    if not has_doi and not has_sf:
        result['verification'] = 'needs_review'
        result['issues'].append('无 ref_doi 且无 source_file')
    elif not has_pollutant:
        result['verification'] = 'needs_review'
        result['issues'].append('无 pollutant')
    elif not has_value:
        result['verification'] = 'needs_review'
        result['issues'].append('无 value')
    elif has_doi and has_sf:
        # 有 DOI 和 source_file，可以进一步核查
        if check_doi:
            doi_ok = check_doi_exists(ref_doi)
            if doi_ok:
                result['verification'] = 'pending_manual_check'
                result['issues'].append('DOI 可解析，需人工确认 PDF 数值')
            else:
                result['verification'] = 'needs_review'
                result['issues'].append('DOI 无法解析')
        else:
            result['verification'] = 'pending_manual_check'
            result['issues'].append('有 DOI 和 source_file，需人工确认 PDF 数值')
    elif has_doi:
        result['verification'] = 'pending_manual_check'
        result['issues'].append('有 DOI 但无 source_file，需补充')
    else:
        result['verification'] = 'needs_review'
        result['issues'].append('仅有 source_file，无 DOI')

    return result


def verify_prototype(db_path: str, repo_root: str, check_doi: bool = False) -> dict:
    """核查单个原型。"""
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    perf = data.get('performance_data', [])
    results = []

    for entry in perf:
        result = verify_entry(entry, repo_root, check_doi)
        results.append(result)

    # 统计
    stats = {
        'total': len(results),
        'verified': sum(1 for r in results if r['verification'] == 'verified'),
        'pending': sum(1 for r in results if r['verification'] == 'pending_manual_check'),
        'needs_review': sum(1 for r in results if r['verification'] == 'needs_review'),
        'has_doi': sum(1 for r in results if r.get('ref_doi')),
        'has_sf': sum(1 for r in results if r.get('source_file')),
    }

    return {
        'prototype_id': data.get('id', '?'),
        'stats': stats,
        'results': results,
    }


def main():
    parser = argparse.ArgumentParser(description='金标准核查')
    parser.add_argument('--db-dir', default=None)
    parser.add_argument('--prototype', default='metal-organic-framework')
    parser.add_argument('--check-doi', action='store_true', help='联网检查 DOI')
    parser.add_argument('--limit', type=int, default=0, help='限制核查数量')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = args.db_dir or str(repo_dir / 'prototypes_db')
    db_path = os.path.join(db_dir, f'{args.prototype}.json')

    if not os.path.exists(db_path):
        print(f'ERROR: {db_path} 不存在')
        sys.exit(1)

    print(f'=== 金标准核查: {args.prototype} ===')
    print(f'模式: {"联网 DOI 检查" if args.check_doi else "本地检查"}')
    if args.limit:
        print(f'限制: 前 {args.limit} 条')
    print()

    result = verify_prototype(db_path, str(repo_dir), args.check_doi)
    stats = result['stats']

    print(f'统计:')
    print(f'  总数: {stats["total"]}')
    print(f'  有 ref_doi: {stats["has_doi"]}')
    print(f'  有 source_file: {stats["has_sf"]}')
    print(f'  verified: {stats["verified"]}')
    print(f'  pending_manual_check: {stats["pending"]}')
    print(f'  needs_review: {stats["needs_review"]}')
    print()

    # 输出需要人工核查的条目
    pending = [r for r in result['results'] if r['verification'] == 'pending_manual_check']
    needs_review = [r for r in result['results'] if r['verification'] == 'needs_review']

    if pending:
        print(f'=== 需要人工核查 ({len(pending)} 条) ===')
        for i, r in enumerate(pending[:20]):
            print(f'{i+1}. {r["pollutant"]}: {r["value"]} ({r["material"][:30]})')
            print(f'   问题: {", ".join(r["issues"])}')
        if len(pending) > 20:
            print(f'   ... 还有 {len(pending) - 20} 条')
        print()

    if needs_review:
        print(f'=== needs_review ({len(needs_review)} 条) ===')
        for i, r in enumerate(needs_review[:10]):
            print(f'{i+1}. {r["pollutant"]}: {r["value"]} ({r["material"][:30]})')
            print(f'   问题: {", ".join(r["issues"])}')
        if len(needs_review) > 10:
            print(f'   ... 还有 {len(needs_review) - 10} 条')

    # 输出报告
    report_path = os.path.join(repo_dir, 'tools', f'verify_report_{args.prototype}.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'\n报告已保存: {report_path}')


if __name__ == '__main__':
    main()
