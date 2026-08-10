#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge per-prototype part files into one translations/<pid>.json
(also used to build dry-run previews)."""
import json, glob, os, sys

PARTS = '/tmp/bmdl_en_backfill/parts'
TRANS = '/tmp/bmdl_en_backfill/translations'

def merge(pid):
    d = os.path.join(PARTS, pid)
    files = sorted(glob.glob(os.path.join(d, 'part_*.json')))
    if not files:
        return None
    mechanisms = []
    organism = None
    seen = set()
    for fp in files:
        p = json.load(open(fp, encoding='utf-8'))
        if p.get('organism_scientific_en'):
            organism = p['organism_scientific_en']
        for m in p.get('mechanisms', []):
            mechanisms.append(m)
    mechanisms.sort(key=lambda m: m.get('idx', 0))
    for m in mechanisms:
        i = m.get('idx')
        if i in seen:
            sys.stderr.write(f'[dup idx] {pid} idx={i}\n')
        seen.add(i)
    return {'proto_id': pid, 'organism_scientific_en': organism, 'mechanisms': mechanisms}

if __name__ == '__main__':
    os.makedirs(TRANS, exist_ok=True)
    pids = sys.argv[1:] or [os.path.basename(p) for p in glob.glob(os.path.join(PARTS, '*'))]
    n = 0
    for pid in sorted(pids):
        t = merge(pid)
        if not t:
            print(f'[{pid}] NO PARTS')
            continue
        with open(os.path.join(TRANS, pid + '.json'), 'w', encoding='utf-8') as f:
            json.dump(t, f, ensure_ascii=False, indent=1)
        n += 1
        print(f'[{pid}] merged {len(t["mechanisms"])} mechanisms -> translations/{pid}.json')
    print(f'\n== merged {n}/{len(pids)} ==')