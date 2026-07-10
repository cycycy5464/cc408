# 修复题目渲染问题

## 已修复

- [x] SVG `<foreignObject>` 换 `<object>` 标签
- [x] SVG 白底(background:#fff)设置
- [x] 2009-ds-010 内容污染（混入组成原理题）
- [x] 2009-ds-011 subject 错配 → 2009-co-011
- [x] 2009-co-013 选项 `__` 未闭合 + 格式清理
- [x] 2019-co-043 subject 错配(CO→OS, 哲学家就餐)
- [x] 12 个文件 `__` 选项标记修复
- [x] 选项解析 JS: 只处理直接 `<p>` 子节点，防解析中 `B\C` 误识别为选项

## 待处理（已扫描确认的问题）

### P1 — 44 个文件 UTF-8 损坏 ⚠️
通过重新 split 从 csgraduates 源数据再生以下年份全部 question 文件：
- [x] 2010（从 csgraduates 重新 split）
- [x] 2011
- [x] 2012
- [x] 2013
- [x] 2015
- [x] 2016
- [x] 2017
- [x] 2018
- [x] 2019
- [x] 2020
- [x] 2021
- [x] 2023
- [x] 2024
- [x] 2025

过程中有以下问题：

### P2 — 从 csgraduates 重新 split 后需要额外处理
- [x] `[tag_link]` 标记丢失 — 658 个文件已补回
- [ ] 解析区的 `>` blockquote 格式丢失 — csgraduates 源不使用 `>` 前缀（次要，不影响功能）
- [x] 自动化修复脚本 `scripts/add_tag_link.py`

### P3 — 主题内容错配检查
- [x] 扫描所有 question 文件，精炼出 2 类问题：
  - 2 个文件有 true contamination（2009-co-022, 2009-os-032）— 已修复
  - 88 个文件尾部 `---` 横线 — 已批量清理
- [ ] 其余含 `正确答案` 的分析文本是自然解析内容（false positive），无需处理
