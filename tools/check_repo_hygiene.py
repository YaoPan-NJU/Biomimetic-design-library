#!/usr/bin/env python3
"""
仓库治理检查脚本

用法：
    python tools/check_repo_hygiene.py

检查项目：
1. 根目录是否有不允许的 .md 过程文档、evaluation 文件、brief JSON、README 变体
2. docs/ 下是否有 AI_AGENT_PROGRESS.md、AI_SUPERVISOR_DIRECTIVE.md、AI_COORDINATION_PROTOCOL.md
3. 是否存在 __pycache__、.pyc、.env、*.local 等应忽略文件
4. examples/adrmats_briefs/ 外是否存在 brief JSON
5. 是否存在 HANDOFF.md、REVIEW-GUIDE.md、SESSION-CONTEXT.md 等重复状态文档
"""

import os
import sys
import glob

# 设置环境变量确保 UTF-8 编码
os.environ['PYTHONUTF8'] = '1'


def safe_print(text):
    """安全打印，处理编码问题"""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('utf-8', errors='replace').decode('utf-8'))


def print_section(title):
    """打印带分隔线的标题"""
    safe_print(f"\n{'='*60}")
    safe_print(f"  {title}")
    safe_print(f"{'='*60}\n")


def check_root_directory():
    """检查根目录是否有不允许的文件"""
    issues = []

    # 允许的根目录文件
    allowed_files = {
        'README.md',
        '.gitignore',
        '.gitmodules',
        'feature-mapping.json',
        'feature_matching_rules.json',
        'pollutant_aliases.json',
        'pollutant_profiles.json'
    }

    # 检查根目录文件
    for item in os.listdir('.'):
        if os.path.isfile(item):
            if item not in allowed_files:
                # 检查是否是不允许的文件类型
                if item.endswith('.md') and item != 'README.md':
                    issues.append(f"根目录不允许的 .md 文件: {item}")
                elif '_evaluation' in item or '_brief_' in item:
                    issues.append(f"根目录不允许的评估/brief 文件: {item}")
                elif item.startswith('README') and item != 'README.md':
                    issues.append(f"README 变体文件: {item}")

    return issues


def check_docs_directory():
    """检查 docs/ 目录是否有过程文件"""
    issues = []

    # 不应在 docs/ 根目录的过程文件
    process_files = [
        'AI_AGENT_PROGRESS.md',
        'AI_SUPERVISOR_DIRECTIVE.md',
        'AI_COORDINATION_PROTOCOL.md',
        'HANDOFF.md',
        'REVIEW-GUIDE.md',
        'SESSION-CONTEXT.md'
    ]

    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        for item in os.listdir(docs_dir):
            if os.path.isfile(os.path.join(docs_dir, item)):
                if item in process_files:
                    issues.append(f"docs/ 下的过程文件: {item}")

    return issues


def check_ignored_files():
    """检查是否存在应忽略的文件"""
    issues = []

    # 检查 __pycache__
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            issues.append(f"存在 __pycache__ 目录: {os.path.join(root, '__pycache__')}")

        for file in files:
            if file.endswith('.pyc'):
                issues.append(f"存在 .pyc 文件: {os.path.join(root, file)}")
            elif file == '.env':
                issues.append(f"存在 .env 文件: {os.path.join(root, file)}")
            elif file.endswith('.local'):
                issues.append(f"存在 .local 文件: {os.path.join(root, file)}")

    return issues


def check_brief_json_outside_examples():
    """检查 examples/adrmats_briefs/ 外是否存在 brief JSON"""
    issues = []

    # 允许 brief JSON 的目录
    allowed_dirs = ['examples/adrmats_briefs']

    for root, dirs, files in os.walk('.'):
        # 跳过 .git 目录
        if '.git' in root:
            continue

        for file in files:
            if file.endswith('.json') and '_brief_' in file.lower():
                # 检查是否在允许的目录中
                rel_path = os.path.relpath(os.path.join(root, file), '.')
                in_allowed = False
                for allowed_dir in allowed_dirs:
                    if rel_path.startswith(allowed_dir):
                        in_allowed = True
                        break

                if not in_allowed:
                    issues.append(f"brief JSON 在不允许的位置: {rel_path}")

    return issues


def check_duplicate_state_docs():
    """检查是否存在重复状态文档"""
    issues = []

    # 重复状态文档列表
    duplicate_docs = [
        'HANDOFF.md',
        'REVIEW-GUIDE.md',
        'SESSION-CONTEXT.md',
        '质量审计报告*.md',
        '优化方案*.md',
        '下一步执行计划*.md'
    ]

    for pattern in duplicate_docs:
        matches = glob.glob(pattern)
        if matches:
            for match in matches:
                issues.append(f"重复状态文档: {match}")

    return issues


def main():
    """主函数"""
    print_section("仓库治理检查")

    all_issues = []

    # 1. 检查根目录
    safe_print("[检查 1] 根目录文件...")
    root_issues = check_root_directory()
    all_issues.extend(root_issues)
    if root_issues:
        for issue in root_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] 根目录文件合规")

    # 2. 检查 docs/ 目录
    safe_print("\n[检查 2] docs/ 目录...")
    docs_issues = check_docs_directory()
    all_issues.extend(docs_issues)
    if docs_issues:
        for issue in docs_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] docs/ 目录合规")

    # 3. 检查应忽略文件
    safe_print("\n[检查 3] 应忽略文件...")
    ignored_issues = check_ignored_files()
    all_issues.extend(ignored_issues)
    if ignored_issues:
        for issue in ignored_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] 无应忽略文件")

    # 4. 检查 brief JSON 位置
    safe_print("\n[检查 4] brief JSON 位置...")
    brief_issues = check_brief_json_outside_examples()
    all_issues.extend(brief_issues)
    if brief_issues:
        for issue in brief_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] brief JSON 位置合规")

    # 5. 检查重复状态文档
    safe_print("\n[检查 5] 重复状态文档...")
    duplicate_issues = check_duplicate_state_docs()
    all_issues.extend(duplicate_issues)
    if duplicate_issues:
        for issue in duplicate_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] 无重复状态文档")

    # 汇总结果
    print_section("检查结果汇总")

    if all_issues:
        safe_print(f"[FAIL] 发现 {len(all_issues)} 个问题：")
        for i, issue in enumerate(all_issues, 1):
            safe_print(f"  {i}. {issue}")
        return 1
    else:
        safe_print("[PASS] 仓库治理检查通过，无问题")
        return 0


if __name__ == "__main__":
    sys.exit(main())
