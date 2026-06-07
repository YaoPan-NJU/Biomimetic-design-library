#!/usr/bin/env python3
"""
Clean up extraction JSON filenames: remove macOS " 2"/" 3" suffixes.

After multi_worker_extract.sh runs on PDFs with " 2" suffix, the output JSONs
also have " 2" in their names. This script renames them to match the canonical
naming convention (without suffix).

Logic:
- For each JSON with " 2" or " 3" suffix:
  - If a JSON without the suffix already exists → the new one (v2 prompt) takes precedence, overwrite
  - If no JSON without the suffix exists → rename to remove suffix
"""

import os
import sys
import json
import shutil

def main():
    json_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'extractions', '论文', 'json')
    json_dir = os.path.abspath(json_dir)

    if not os.path.isdir(json_dir):
        print(f"ERROR: Directory not found: {json_dir}")
        sys.exit(1)

    renamed = 0
    overwritten = 0
    skipped = 0

    # Collect all JSON files
    files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    for fn in sorted(files):
        stem = fn[:-5]  # remove .json

        # Check if this has a " 2" or " 3" suffix
        if not (stem.endswith(' 2') or stem.endswith(' 3')):
            continue

        # Get the canonical stem (without suffix)
        canonical_stem = stem[:-2]
        canonical_fn = canonical_stem + '.json'

        src = os.path.join(json_dir, fn)
        dst = os.path.join(json_dir, canonical_fn)

        # Validate the source JSON
        try:
            with open(src, 'r') as f:
                data = json.load(f)
            if 'schema_version' not in data and 'knowledge_items' not in data:
                print(f"  SKIP (invalid): {fn}")
                skipped += 1
                continue
        except (json.JSONDecodeError, Exception) as e:
            print(f"  SKIP (parse error): {fn} - {e}")
            skipped += 1
            continue

        if os.path.exists(dst):
            # Check if existing file is valid
            try:
                with open(dst, 'r') as f:
                    existing = json.load(f)
                existing_valid = 'schema_version' in existing or 'knowledge_items' in existing
            except:
                existing_valid = False

            if existing_valid:
                # New v2 extraction overwrites old v1
                print(f"  OVERWRITE: {canonical_fn} ← {fn}")
                shutil.copy2(src, dst)
                os.remove(src)
                overwritten += 1
            else:
                # Existing is invalid, replace
                print(f"  REPLACE (invalid existing): {canonical_fn} ← {fn}")
                shutil.copy2(src, dst)
                os.remove(src)
                renamed += 1
        else:
            # Simple rename
            print(f"  RENAME: {fn} → {canonical_fn}")
            os.rename(src, dst)
            renamed += 1

    print(f"\nDone: {renamed} renamed, {overwritten} overwritten, {skipped} skipped")

    # Final count
    final_count = len([f for f in os.listdir(json_dir) if f.endswith('.json')])
    print(f"Total JSONs in 论文/json/: {final_count}")

if __name__ == '__main__':
    main()
