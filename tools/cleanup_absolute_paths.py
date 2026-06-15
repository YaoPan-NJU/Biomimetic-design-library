#!/usr/bin/env python3
"""
Convert absolute source_file paths to relative paths in prototypes_db/*.json.

Before: "source_file": "/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/outputs/extractions/论文/json/xxx.json"
After:  "source_file": "tools/litextract/outputs/extractions/论文/json/xxx.json"
"""

import os
import sys
import json
import glob

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    db_dir = os.path.join(repo_root, 'prototypes_db')

    if not os.path.isdir(db_dir):
        print(f"ERROR: prototypes_db not found at {db_dir}")
        sys.exit(1)

    # Pattern to match absolute paths
    prefix = repo_root + '/'

    total_files = 0
    total_replacements = 0

    for json_path in sorted(glob.glob(os.path.join(db_dir, '*.json'))):
        with open(json_path, 'r') as f:
            content = f.read()

        # Replace absolute paths with relative paths
        new_content = content.replace(prefix, '')
        replacements = content.count(prefix)

        if replacements > 0:
            with open(json_path, 'w') as f:
                f.write(new_content)

            fname = os.path.basename(json_path)
            print(f"  {fname}: {replacements} replacements")
            total_files += 1
            total_replacements += replacements

    print(f"\nDone: {total_files} files, {total_replacements} total replacements")

if __name__ == '__main__':
    main()
