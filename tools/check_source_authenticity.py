#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validator: check_source_authenticity.py

补 check_from_source_integrity.py 未覆盖的"来源真实性"盲区。检查四类问题：

1. 标签膨胀（ERROR）：honesty_ledger 计数式 schema 里 from_source_mechanisms 与
   causal_chain 实际标 from_source 的机制数矛盾（尤其 ledger=0 却存在 from_source）。
2. from_source 来源非可引标识（ERROR）：basis=from_source 的 causal_chain 要素，其 source
   为空或不含 DOI / PDB 号 / 专利号 / 标准号（例如只填了 PDF 文件名或自由文本）。
3. DOI 格式非法（WARNING）：任何以 "10." 开头的 DOI 字段含尾部标点、空格或不合规。
4. 疑似泛引（WARNING）：quote 形如参考文献列表碎片（[J] / 期刊缩写尾 / et al. 年份 等）。

仅对计数式 ledger（含 from_source_mechanisms 键，即 V1-B 新批次）做第 1 类硬检查，
避免对第一批 facts/leads/inferences schema 误报。PDB 结构号（含 RCSB DOI 10.2210/...）
视为合法一手来源。
"""
import json
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(REPO, 'prototypes_db')

CC_KEYS = ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']

DOI_RE = re.compile(r'^10\.\d{4,9}/\S+$')
DOI_ANYWHERE_RE = re.compile(r'10\.\d{4,9}/\S+')
PDB_RE = re.compile(r'\bPDB[\s:]*[0-9][A-Za-z0-9]{3}\b', re.IGNORECASE)
PATENT_RE = re.compile(r'^(CN|US|EP|WO|JP|KR)\s?\d{6,}', re.IGNORECASE)
STANDARD_RE = re.compile(r'^(GB|ISO|ASTM|HJ|SN|NY|DL|IEC|EN|Q/)\s?[\d\.\-T/]+', re.IGNORECASE)

# 参考文献列表碎片 / 非实质正文引文的高置信特征
SUSPICIOUS_QUOTE_RE = re.compile(
    r'\[[JCMN]\]'                    # GB 文献类型标识 [J] [C] [M]
    r'|:\s*a review\b'               # "...: a review"
    r'|\bet al\.,?\s*\d{4}'          # "Smith et al., 2021"
    r'|,\s*(Environ|J\.|Sci\.|Water|Chem\.|Mater\.)\b'  # 期刊缩写尾巴
    r'|\bdoi:\s*10\.',               # 引文里嵌 doi:
    re.IGNORECASE
)


def looks_like_doi(s):
    return isinstance(s, str) and s.strip().lower().startswith('10.')


def doi_format_issue(s):
    """返回 DOI 格式问题描述；合规返回 None。"""
    if s != s.strip():
        return 'leading/trailing whitespace'
    if re.search(r'\s', s):
        return 'contains whitespace'
    if s[-1] in '.,;':
        return f'trailing punctuation "{s[-1]}"'
    if not DOI_RE.match(s):
        return 'does not match 10.NNNN/suffix'
    return None


def is_citable_identifier(s):
    """source 只要含 DOI / PDB 号 / 专利号 / 标准号即视为可引来源。"""
    if not isinstance(s, str) or not s.strip():
        return False
    s = s.strip()
    return bool(
        DOI_ANYWHERE_RE.search(s)
        or PDB_RE.search(s)
        or PATENT_RE.match(s)
        or STANDARD_RE.match(s)
    )


def count_mechs_with_from_source(mechs):
    n = 0
    for m in mechs:
        if not isinstance(m, dict):
            continue
        cc = m.get('causal_chain', {})
        if not isinstance(cc, dict):
            continue
        if any(isinstance(cc.get(k), dict) and cc[k].get('basis') == 'from_source' for k in CC_KEYS):
            n += 1
    return n


def check():
    errors = []
    warnings = []

    for f in sorted(glob.glob(os.path.join(DB, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        pid = d.get('id', os.path.basename(f).replace('.json', ''))
        mechs = d.get('mechanisms', []) or []

        # ---- 1. 标签膨胀（仅计数式 ledger）----
        hl = d.get('honesty_ledger')
        if isinstance(hl, dict) and isinstance(hl.get('from_source_mechanisms'), int):
            declared = hl['from_source_mechanisms']
            actual = count_mechs_with_from_source(mechs)
            if declared == 0 and actual > 0:
                errors.append(f'{pid}: honesty_ledger from_source_mechanisms=0 但 {actual} 个机制的 causal_chain 标 from_source（证据标签膨胀）')
            elif declared != actual:
                warnings.append(f'{pid}: ledger from_source_mechanisms={declared} 与 causal_chain from_source 机制数 {actual} 不一致')

        # ---- 逐机制 / 逐 causal_chain 要素 ----
        for mi, m in enumerate(mechs):
            if not isinstance(m, dict):
                continue
            cc = m.get('causal_chain', {})
            if not isinstance(cc, dict):
                continue
            for k in CC_KEYS:
                el = cc.get(k)
                if not isinstance(el, dict):
                    continue
                src = el.get('source', '')
                quote = el.get('quote', '')

                if el.get('basis') == 'from_source':
                    # 2. from_source 来源必须是可引标识
                    if not src or not str(src).strip():
                        errors.append(f'{pid}[{mi}].{k}: from_source 但 source 为空（DOI 缺失）')
                    elif not is_citable_identifier(str(src)):
                        errors.append(f'{pid}[{mi}].{k}: from_source 但 source 非 DOI/PDB/专利/标准："{str(src)[:60]}"')

                # 3. DOI 格式（任何 basis）
                if looks_like_doi(str(src)):
                    issue = doi_format_issue(str(src))
                    if issue:
                        warnings.append(f'{pid}[{mi}].{k}: DOI 格式非法（{issue}）："{src}"')

                # 4a. 疑似泛引 quote
                if quote and SUSPICIOUS_QUOTE_RE.search(str(quote)):
                    warnings.append(f'{pid}[{mi}].{k}: 疑似泛引/参考文献碎片 quote："{str(quote)[:60]}"')

        # ---- DOI 格式：机制/性能/约束层的 ref_doi、source_doi ----
        for coll_name in ('mechanisms', 'performance_data', 'engineering_constraints'):
            for i, item in enumerate(d.get(coll_name, []) or []):
                if not isinstance(item, dict):
                    continue
                for fld in ('ref_doi', 'source_doi', 'doi'):
                    v = item.get(fld)
                    if looks_like_doi(str(v)):
                        issue = doi_format_issue(str(v))
                        if issue:
                            warnings.append(f'{pid}.{coll_name}[{i}].{fld}: DOI 格式非法（{issue}）："{v}"')

    # ---- 跨原型 DOI 复用：已取消（综述合法地支撑多个原型≠缺陷，噪声过高）----
    return errors, warnings


def main():
    errors, warnings = check()

    print('=== 来源真实性检查 check_source_authenticity ===')
    print(f'错误(ERROR): {len(errors)}')
    print(f'警告(WARNING): {len(warnings)}')

    if warnings:
        print(f'\n⚠️ WARNING ({len(warnings)}):')
        for w in warnings[:30]:
            print(f'  {w}')
        if len(warnings) > 30:
            print(f'  ... 另有 {len(warnings) - 30} 条')

    if errors:
        print(f'\n❌ ERROR ({len(errors)}):')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)

    print('\n✅ 无 from_source 标签膨胀 / DOI 缺失类硬错误')
    sys.exit(0)


if __name__ == '__main__':
    main()
