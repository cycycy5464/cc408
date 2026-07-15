# Tasks 目录

任务相关文件，按功能分类。

---

## 目录结构

```
tasks/
├── docs/              # 任务文档
├── scripts/           # 任务脚本
├── 408-crawler/       # 408 爬虫项目
└── 真题修复/          # 真题修复项目
```

---

## docs — 任务文档

| 文件 | 内容 |
|------|------|
| `2009-2025完整打印版转换.md` | 打印版转换方案 |
| `408答案解析爬虫.md` | 答案解析爬虫文档 |
| `题目颗粒化重构方案.md` | 题目颗粒化重构方案 |
| `页面渲染规则.md` | 页面渲染规则 |
| `fix-exam-rendering-issues.md` | 修复考试渲染问题 |
| `hugo-knowledge-graph.md` | Hugo 知识图谱文档 |
| `current.md` | 当前任务进度 |
| `lessons.md` | 经验教训 |
| `verify_summary.md` | 验证总结 |

---

## scripts — 任务脚本

| 脚本 | 功能 |
|------|------|
| `check_2009_questions.py` | 检查2009年题目 |
| `check_headings.py` | 检查标题格式 |
| `check_years.py` | 检查年份目录 |
| `find_questions.py` | 查找题目 |
| `fix_2010_taglink.py` | 修复2010年taglink |
| `fix_frontmatter.py` | 修复frontmatter |
| `fix_years.py` | 修复年份目录 |
| `investigate.py` | 调查脚本 |
| `resolve_duplicates.py` | 解决重复题目 |
| `restore_missing.py` | 恢复缺失内容 |
| `split_questions.awk` | 拆分题目脚本 |
| `split_simulate.ps1` | 拆分模拟题 |
| `validate_content.py` | 验证内容格式 |

---

## 408-crawler — 408 爬虫项目

爬取 408 考研真题的爬虫工具，包含：
- `crawler.js` - 主爬虫
- `filler.js` - 数据填充
- `crawled_data_backup/` - 爬取数据备份

---

## 真题修复 — 真题修复项目

真题修复相关脚本和文档，详见 `真题修复/README.md`

---

*更新于 2026-07-15*
