#!/usr/bin/env python3
"""
仓库治理检查脚本

用法：
    python tools/check_repo_hygiene.py

检查项目：
1. docs/ 根目录 allowlist 检查
2. 根目录不允许的文件检查
3. brief JSON 位置检查
4. 重复状态文档检查
"""

import os
import sys
import subprocess

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


def get_git_tracked_files():
    """获取 git 追踪的文件列表"""
    try:
        result = subprocess.run(
            ['git', 'ls-files'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return set(result.stdout.strip().split('\n')) if result.stdout.strip() else set()
    except Exception:
        return set()


def get_git_ignored_files():
    """获取被 .gitignore 忽略的文件列表"""
    try:
        result = subprocess.run(
            ['git', 'ls-files', '--ignored', '--exclude-standard'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return set(result.stdout.strip().split('\n')) if result.stdout.strip() else set()
    except Exception:
        return set()


def check_docs_allowlist():
    """检查 docs/ 根目录 allowlist"""
    issues = []

    # docs/ 允许的 md 文件
    allowed_docs = {
        'design.md',
        'ADRMATS_DELIVERY_PLAN.md',
        'ADRMATS_CALL_GUIDE.md',
        'ADRMATS_INTEGRATION.md',
        'SUPPORT_SCOPE_AND_RISKS.md',
        'REPOSITORY_HYGIENE.md'
    }

    # 不允许的文件模式
    disallowed_patterns = [
        'Github management-INSTRUCTIONS.md',
        'quality-audit',
        '路径映射修复指令',
        'AI_AGENT_PROGRESS',
        'AI_COORDINATION_PROTOCOL',
        'AI_SUPERVISOR_DIRECTIVE',
        'HANDOFF',
        'REVIEW-GUIDE',
        'SESSION-CONTEXT',
        '_evaluation',
        '任务布置_',
        '分层核查标准_',
        '金标准闭环_',
        '优化方案_',
        '文献检索指令',
        '下一步执行计划_',
        '最新提取质量问题汇总',
        '架构审查与优化建议_'
    ]

    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        for item in os.listdir(docs_dir):
            item_path = os.path.join(docs_dir, item)

            # 跳过目录（如 archive/、context/）
            if os.path.isdir(item_path):
                continue

            # 检查是否在 allowlist 中
            if item not in allowed_docs:
                # 检查是否匹配不允许的模式
                for pattern in disallowed_patterns:
                    if pattern in item:
                        issues.append(f"docs/ 下不允许的文件: {item}")
                        break

    return issues


def check_root_directory():
    """检查根目录是否有不允许的文件"""
    issues = []

    # 允许的根目录文件
    allowed_files = {
        'README.md',
        'CLAUDE.md',
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


def check_brief_json_outside_examples():
    """检查 examples/adrmats_briefs/ 外是否存在 brief JSON"""
    issues = []

    # 允许 brief JSON 的目录
    allowed_dirs = ['examples/adrmats_briefs']

    # 获取 git 追踪的文件
    tracked_files = get_git_tracked_files()

    for tracked_file in tracked_files:
        if tracked_file.endswith('.json') and '_brief_' in tracked_file.lower():
            # 检查是否在允许的目录中
            in_allowed = False
            for allowed_dir in allowed_dirs:
                if tracked_file.startswith(allowed_dir):
                    in_allowed = True
                    break

            if not in_allowed:
                issues.append(f"brief JSON 在不允许的位置: {tracked_file}")

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

    # 获取 git 追踪的文件
    tracked_files = get_git_tracked_files()

    for tracked_file in tracked_files:
        # git ls-files 对含特殊字符的路径会加引号，需剥离
        clean_path = tracked_file.strip('"')
        for pattern in duplicate_docs:
            if pattern.replace('*', '') in clean_path:
                # 检查是否在 archive、context 或 optimization-v1 目录中（这些是合法位置）
                if not (clean_path.startswith('docs/archive/') or clean_path.startswith('docs/context/') or clean_path.startswith('docs/optimization-v1/')):
                    issues.append(f"重复状态文档: {clean_path}")

    return issues


def main():
    """主函数"""
    print_section("仓库治理检查")

    all_issues = []

    # 1. 检查 docs/ allowlist
    safe_print("[检查 1] docs/ 根目录 allowlist...")
    docs_issues = check_docs_allowlist()
    all_issues.extend(docs_issues)
    if docs_issues:
        for issue in docs_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] docs/ 目录合规")

    # 2. 检查根目录
    safe_print("\n[检查 2] 根目录文件...")
    root_issues = check_root_directory()
    all_issues.extend(root_issues)
    if root_issues:
        for issue in root_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] 根目录文件合规")

    # 3. 检查 brief JSON 位置
    safe_print("\n[检查 3] brief JSON 位置...")
    brief_issues = check_brief_json_outside_examples()
    all_issues.extend(brief_issues)
    if brief_issues:
        for issue in brief_issues:
            safe_print(f"  [ISSUE] {issue}")
    else:
        safe_print("  [PASS] brief JSON 位置合规")

    # 4. 检查重复状态文档
    safe_print("\n[检查 4] 重复状态文档...")
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
