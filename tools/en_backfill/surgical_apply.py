#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical write: insert *_en keys into prototypes_db/*.json via text-level
insertion (no re-serialization, no reformatting). Every non-added byte of the
file is preserved so git diff shows only the new lines.

Insertion points (kept adjacent to their Chinese source key for readability):
  organism.scientific                    -> + ,"scientific_en": "..."
  mechanisms[i].name                     -> + ,"name_en": "..."
  mechanisms[i].description              -> + ,"description_en": "..."
  mechanisms[i].causal_chain.transferable_principle
                                         -> + ,"transferable_principle_en": "..."

Usage:
  python -X utf8 surgical_apply.py --preview --canon <repo_root> [--pid X]
  python -X utf8 surgical_apply.py --write  --canon <repo_root> [--pid X]
"""
import argparse, json, os, re, sys

TRANS = '/tmp/bmdl_en_backfill/translations'


class TextEditor:
    """Pre-scan a JSON text: record every container range and string token,
    then answer 'which innermost dict directly contains a given key'."""

    def __init__(self, text):
        self.text = text
        self.n = len(text)
        self.containers = []   # (start, end, is_dict)  document order
        self._prescan()

    def _prescan(self):
        t = self.text
        n = self.n
        stack = []             # (start, open_char)
        i = 0
        while i < n:
            c = t[i]
            if c == '"':
                i = self._str_end(i) + 1
            elif c in '{[':
                stack.append((i, c))
                i += 1
            elif c in '}]':
                if stack:
                    s, oc = stack.pop()
                    if (oc == '{' and c == '}') or (oc == '[' and c == ']'):
                        self.containers.append((s, i, oc == '{'))
                    else:
                        # malformed pairing: still close as dict/array by oc
                        self.containers.append((s, i, oc == '{'))
                i += 1
            else:
                i += 1
        self.containers.sort()

    def _str_end(self, i):
        """i at opening quote -> index of closing quote (or n-1)."""
        j = i + 1
        while j < self.n:
            c = self.text[j]
            if c == '\\':
                j += 2
                continue
            if c == '"':
                return j
            j += 1
        return self.n - 1

    def innermost_dict_owner(self, pos):
        """Return (start, is_dict) of the innermost container enclosing pos,
        or None if pos is not inside any container."""
        cand = None
        for s, e, is_dict in self.containers:
            if s >= pos:
                break  # containers sorted by start
            if pos < e:
                cand = (s, is_dict)
        return cand

    def direct_key_dicts(self, key):
        """All innermost dict starts containing `key` as a direct member."""
        t = self.text
        n = self.n
        idstarts = []
        i = 0
        while i < n:
            c = t[i]
            if c == '"':
                end = self._str_end(i)
                if t[i + 1:end] == key:
                    k = end + 1
                    while k < n and t[k] in ' \t\r\n':
                        k += 1
                    if k < n and t[k] == ':':
                        owner = self.innermost_dict_owner(i)
                        if owner is not None and owner[1]:
                            idstarts.append(owner[0])
                i = end + 1
            elif c == '"' and False:
                i += 1
            else:
                i += 1
        # de-dup (same dict via repeated key)
        seen = set()
        out = []
        for s in idstarts:
            if s not in seen:
                seen.add(s)
                out.append(s)
        return out

    def value_end(self, dict_start, key):
        """Offset just after the value of `key` inside dict_start (assumes key
        is a direct member). None if absent."""
        t = self.text
        dstart = dict_start + 1
        # find closing brace of dict_start
        close = None
        for s, e, is_dict in self.containers:
            if s == dict_start:
                close = e
                break
        if close is None:
            return None
        i = dstart
        while i < close:
            c = t[i]
            if c == '"':
                end = self._str_end(i)
                if t[i + 1:end] == key:
                    k = end + 1
                    while k < close and t[k] in ' \t\r\n':
                        k += 1
                    if k < close and t[k] == ':':
                        v = k + 1
                        while v < close and t[v] in ' \t\r\n':
                            v += 1
                        if v < close:
                            vc = t[v]
                            if vc == '"':
                                vend = self._str_end(v)
                                return vend + 1
                            if vc in '{[':
                                owner = None
                                for s2, e2, _ in self.containers:
                                    if s2 == v:
                                        return e2 + 1
                                return None
                            v2 = v
                            while v2 < close and t[v2] not in ',}\n':
                                v2 += 1
                            return v2
                # skip past this string value pair quickly
                k2 = end + 1
                while k2 < close and t[k2] in ' \t\r\n':
                    k2 += 1
                if k2 < close and t[k2] == ':':
                    vv = k2 + 1
                    while vv < close and t[vv] in ' \t\r\n':
                        vv += 1
                    vc = t[vv] if vv < close else ''
                    if vc == '"':
                        i = self._str_end(vv) + 1
                        continue
                    if vc in '{[':
                        for s2, e2, _ in self.containers:
                            if s2 == vv:
                                i = e2 + 1
                                break
                        else:
                            i = vv + 1
                        continue
                    v3 = vv
                    while v3 < close and t[v3] not in ',}\n':
                        v3 += 1
                    i = v3
                    continue
                i = end + 1
            else:
                i += 1
        return None

    def find_key(self, dict_start, key):
        """Return the char offset of the `key` string token (its opening quote)
        inside dict_start, if it is a direct member. None if absent."""
        t = self.text
        close = None
        for s, e, is_dict in self.containers:
            if s == dict_start:
                close = e
                break
        if close is None:
            return None
        i = dict_start + 1
        while i < close:
            c = t[i]
            if c == '"':
                end = self._str_end(i)
                if t[i + 1:end] == key:
                    k = end + 1
                    while k < close and t[k] in ' \t\r\n':
                        k += 1
                    if k < close and t[k] == ':':
                        return i
                i = end + 1
            else:
                i += 1
        return None

    def line_indent(self, offset):
        ls = self.text.rfind('\n', 0, offset)
        line = self.text[ls + 1:] if ls >= 0 else self.text[:offset]
        return re.match(r'[ \t]*', line).group(0)


def build_plan(text, translation):
    ed = TextEditor(text)
    plan = []
    mech_ordered = sorted(translation.get('mechanisms', []), key=lambda m: m['idx'])

    # 1) organism.scientific_en
    for start in ed.direct_key_dicts('scientific'):
        ve = ed.value_end(start, 'scientific')
        ks = ed.find_key(start, 'scientific')
        if ve is None or ks is None:
            continue
        indent = ed.line_indent(ks)
        val = translation.get('organism_scientific_en')
        if val:
            plan.append((ve, indent, 'scientific_en', val))

    # 2) mechanism dicts: those that directly contain name + description + causal_chain
    mech_starts = []
    for start in ed.direct_key_dicts('name'):
        has_desc = ed.value_end(start, 'description') is not None
        has_cc = ed.value_end(start, 'causal_chain') is not None
        if has_desc and has_cc:
            mech_starts.append(start)
    mech_starts.sort(key=lambda s: s)
    if len(mech_starts) != len(mech_ordered):
        raise RuntimeError(
            f'mechanism count mismatch: text={len(mech_starts)} translation={len(mech_ordered)}')
    for start, tm in zip(mech_starts, mech_ordered):
        ve_name = ed.value_end(start, 'name')
        ve_desc = ed.value_end(start, 'description')
        ks_name = ed.find_key(start, 'name')
        ks_desc = ed.find_key(start, 'description')
        if ve_name is not None and tm.get('name_en'):
            plan.append((ve_name, ed.line_indent(ks_name), 'name_en', tm['name_en']))
        if ve_desc is not None and tm.get('description_en'):
            plan.append((ve_desc, ed.line_indent(ks_desc), 'description_en', tm['description_en']))

    # 3) causal_chain.transferable_principle_en (order matches mechanisms order)
    cc_starts = [s for s in ed.direct_key_dicts('transferable_principle')]
    cc_starts.sort()
    if len(cc_starts) != len(mech_ordered):
        raise RuntimeError(
            f'causal_chain count mismatch: text={len(cc_starts)} mechanisms={len(mech_ordered)}')
    for start, tm in zip(cc_starts, mech_ordered):
        ve = ed.value_end(start, 'transferable_principle')
        ks = ed.find_key(start, 'transferable_principle')
        if ve is None or ks is None:
            continue
        if tm.get('transferable_principle_en'):
            plan.append((ve, ed.line_indent(ks), 'transferable_principle_en', tm['transferable_principle_en']))

    return plan


def apply_plan(text, plan):
    edits = [(offset, ',\n' + indent + f'"{key}": {json.dumps(value, ensure_ascii=False)}')
             for offset, indent, key, value in plan]
    for offset, new_line in sorted(edits, key=lambda e: e[0], reverse=True):
        text = text[:offset] + new_line + text[offset:]
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preview', action='store_true')
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--canon', default='.')
    ap.add_argument('--pid', default='')
    args = ap.parse_args()
    if not (args.preview or args.write):
        ap.error('need --preview or --write')

    canon_dir = args.canon
    db = canon_dir if os.path.basename(canon_dir) == 'prototypes_db' else os.path.join(canon_dir, 'prototypes_db')
    pids = [args.pid] if args.pid else sorted(
        os.path.basename(p)[:-5] for p in os.listdir(db) if p.endswith('.json'))

    total = 0
    n_ok = 0
    for pid in pids:
        tpath = os.path.join(TRANS, pid + '.json')
        if not os.path.exists(tpath):
            print(f'[{pid}] MISSING translation file')
            continue
        translation = json.load(open(tpath, encoding='utf-8'))
        canon_path = os.path.join(db, pid + '.json')
        text = open(canon_path, encoding='utf-8').read()
        try:
            plan = build_plan(text, translation)
        except RuntimeError as e:
            print(f'[{pid}] SKIP: {e}')
            continue
        if args.preview:
            for _, indent, key, value in plan:
                print(f'[{pid}] {indent}"{key}": {json.dumps(value, ensure_ascii=False)}')
            total += len(plan)
            n_ok += 1
            continue
        new_text = apply_plan(text, plan)
        try:
            parsed = json.loads(new_text)
            if len(parsed['mechanisms']) != len(json.loads(text)['mechanisms']):
                raise RuntimeError('mechanism count changed')
        except Exception as e:
            print(f'[{pid}] REFUSE write (broken output): {e}')
            continue
        with open(canon_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'[{pid}] written {len(plan)} insertions')
        total += len(plan)
        n_ok += 1
    print(f'\n== {"PREVIEW" if args.preview else "WRITE"} total insertions: {total}, files: {n_ok}/{len(pids)} ==')


if __name__ == '__main__':
    main()