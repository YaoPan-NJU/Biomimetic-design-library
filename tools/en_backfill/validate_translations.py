#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate translations against sources.
Checks: mechanism count alignment, idx continuity, field presence, no CJK,
empty-source -> empty-output, non-empty-source -> non-empty-output."""
import json, glob, os, re, sys

TRANS = '/tmp/bmdl_en_backfill/translations'
SRC = '/tmp/bmdl_en_backfill/sources'
MANIFEST = '/tmp/bmdl_en_backfill/manifest.json'

CJK = re.compile(r'[　-〿㐀-䶿一-鿿＀-￯‘’“”]')

def validate(pid, verbose=False):
    problems = []
    tp = os.path.join(TRANS, pid + '.json')
    if not os.path.exists(tp):
        return (pid, 1, ['MISSING_TRANSLATION'], [])
    t = json.load(open(tp, encoding='utf-8'))
    s = json.load(open(os.path.join(SRC, pid + '.json'), encoding='utf-8'))
    src_mechs = s['mechanisms']
    tr_mechs = t.get('mechanisms', [])
    n_src, n_tr = len(src_mechs), len(tr_mechs)
    if n_src != n_tr:
        problems.append(f'count mismatch: src={n_src} tr={n_tr}')
    # idx continuity
    idxs = [m.get('idx') for m in tr_mechs]
    if idxs != list(range(len(idxs))):
        problems.append(f'idx not 0..n-1: {idxs}')
    # per-mechanism checks
    tr_by_idx = {m.get('idx'): m for m in tr_mechs}
    for sm in src_mechs:
        i = sm['idx']
        tm = tr_by_idx.get(i)
        if tm is None:
            problems.append(f'idx {i} missing in translation')
            continue
        for k in ('name_en', 'description_en', 'transferable_principle_en'):
            tv = tm.get(k)
            if not isinstance(tv, str):
                problems.append(f'idx {i} {k}: not a string ({type(tv).__name__})')
                continue
            if CJK.search(tv):
                problems.append(f'idx {i} {k}: contains CJK -> {tv[:40]!r}')
            sv = {'name_en': sm['name'], 'description_en': sm['description'],
                  'transferable_principle_en': sm['transferable_principle']}[k]
            src_empty = (sv is None or str(sv).strip() == '')
            if src_empty and tv.strip() != '':
                problems.append(f'idx {i} {k}: src empty but output non-empty')
            if not src_empty and tv.strip() == '':
                problems.append(f'idx {i} {k}: src non-empty but output empty')
    # organism
    org_tr = t.get('organism_scientific_en')
    org_src = s.get('organism_scientific')
    if org_src and not org_tr:
        problems.append('organism_scientific_en: src non-empty but output empty/missing')
    if org_tr and CJK.search(str(org_tr)):
        problems.append(f'organism_scientific_en: contains CJK -> {org_tr[:40]!r}')
    return (pid, len(problems), problems, [m.get(i) for i in []])  # (pid, n_problems, problems, notes)

if __name__ == '__main__':
    manifest = json.load(open(MANIFEST, encoding='utf-8'))
    pids = sys.argv[1:] or [m['id'] for m in manifest]
    total_problems = 0
    ok, fail = [], []
    for pid in pids:
        pid0, n, problems, _ = validate(pid)
        if n == 0:
            ok.append(pid)
        else:
            fail.append(pid)
            total_problems += n
            print(f'[{pid}] {n} problems:')
            for p in problems:
                print(f'    - {p}')
    print(f'\n== VALIDATION: {len(ok)} OK / {len(fail)} FAIL / {total_problems} problems ==')
    if fail:
        print('FAILED:', ', '.join(fail))
        sys.exit(1)