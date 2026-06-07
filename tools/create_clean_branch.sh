#!/bin/bash
# Create a clean delivery branch for ADRMATS
# Run this after extraction is complete and prototypes_db is rebuilt

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

echo "=== Creating Clean Delivery Branch ==="

# 1. Stash any uncommitted changes
echo "Stashing uncommitted changes..."
git stash push -m "WIP: before creating clean branch"

# 2. Create new branch from main
echo "Creating release/v1.0 from main..."
git checkout main
git pull origin main
git checkout -b release/v1.0

# 3. Merge feature branch content
echo "Merging library content from feature/extraction-results..."
git checkout feature/extraction-results -- prototypes_db/
git checkout feature/extraction-results -- prototypes/
git checkout feature/extraction-results -- feature-mapping.json
git checkout feature/extraction-results -- taxonomy/
git checkout feature/extraction-results -- templates/
git checkout feature/extraction-results -- docs/design.md

# 4. Copy clean README
if [ -f README-clean.md ]; then
    cp README-clean.md README.md
    rm README-clean.md
fi

# 5. Remove unwanted files (if they exist)
echo "Removing unwanted files..."
rm -rf tools/ extraction/ 2>/dev/null || true
rm -f SESSION-CONTEXT.md REVIEW-GUIDE.md .gitmodules 2>/dev/null || true
rm -f quality-audit-*.md 架构审查*.md 下一步执行计划*.md 最新提取质量问题汇总.md 2>/dev/null || true
rm -f 文献检索指令*.md 2>/dev/null || true
rm -f docs/quality-audit-*.md docs/路径映射修复指令.md 2>/dev/null || true

# 6. Update .gitignore for clean branch
cat > .gitignore << 'EOF'
# Environment
.env
*.env

# Literature PDFs
仿生文献库/

# macOS
.DS_Store

# IDE
.vscode/
.idea/

# Python
__pycache__/
*.pyc
.venv/

# Node
node_modules/

# Temporary
*.tmp
*.bak
EOF

# 7. Commit
echo "Committing clean branch..."
git add -A
git commit -m "chore: 创建干净的仿生设计库交付分支 v1.0

包含内容:
- prototypes_db/ (33个正典JSON)
- prototypes/ (36个渲染的prototype.md)
- feature-mapping.json (四层映射+权重)
- taxonomy/ (分类体系)
- templates/ (原型模板)
- docs/design.md (设计文档)
- README.md (项目说明)

排除内容:
- tools/ (构建/验证脚本)
- extraction/ (提参管道)
- 进度跟踪文档
- 文献检索指令
- 仿生文献库PDF"

# 8. Push
echo "Pushing to origin..."
git push origin release/v1.0

echo "=== Done! ==="
echo "Clean branch 'release/v1.0' created and pushed."
echo "Switch back to working branch: git checkout feature/extraction-results"
echo "Restore stashed changes: git stash pop"
