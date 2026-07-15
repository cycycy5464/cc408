# CC408 脚本工具集

按功能分类的脚本工具，用于内容迁移、题目修复、图片处理等任务。

---

## 目录结构

```
scripts/
├── content-migration/    # 内容转换/迁移
├── question-fix/         # 题目/选项修复
├── image-processing/     # 图片处理
├── content-validation/   # 内容检查/验证
├── knowledge-graph/      # 知识图谱/标签
├── utility/              # 其他工具
└── archive/              # 已归档脚本
```

---

## content-migration — 内容转换/迁移

| 脚本 | 功能 | 用法 |
|------|------|------|
| `extract_39_47.py` | 从外部 content.md 提取第39-47题 | `python extract_39_47.py` |
| `migrate-quiz.py` | 迁移 408quiz 真题到项目格式 | `python migrate-quiz.py --src <path>` |
| `scrape_q43.js` | 爬取 2009 年第43题内容 | `node scrape_q43.js` |
| `split_questions.py` | 将整卷 Markdown 拆分为单题文件 | `python split_questions.py` |

---

## question-fix — 题目/选项修复

| 脚本 | 功能 | 用法 |
|------|------|------|
| `restore_2010_options_from_crawled.py` | 从爬虫数据恢复2010年选项 | `python restore_2010_options_from_crawled.py [--dry-run]` |
| `restore_options.py` | 从 git 旧 commit 恢复选项 | `python restore_options.py [--dry-run] [--limit N]` |
| `find_option_loss.py` | 对比两个 commit 找出选项丢失 | `python find_option_loss.py` |

---

## image-processing — 图片处理

| 脚本 | 功能 | 用法 |
|------|------|------|
| `batch-fix-svgs.js` | 批量修复 SVG 中的 foreignObject | `node batch-fix-svgs.js` |
| `fix-image-paths.js` | 修复题目中的图片引用路径 | `node fix-image-paths.js` |
| `fix-q47-svg.js` | 修复特定 SVG 文件属性 | `node fix-q47-svg.js` |
| `reorganize-images.js` | 按年份/题号重组图片目录 | `node reorganize-images.js` |
| `reorganize-images-v2.js` | v2版图片重组 | `node reorganize-images-v2.js` |
| `restore-Q47.js` | 还原 2009-cn-047 题格式 | `node restore-Q47.js` |

---

## content-validation — 内容检查/验证

| 脚本 | 功能 | 用法 |
|------|------|------|
| `audit_all.py` | 综合审计扫描题目问题 | `python audit_all.py` |
| `check_files.py` | 检查 Summary 渲染问题 | `python check_files.py` |
| `validate-content.py` | 验证 frontmatter 合法性 | `python validate-content.py` |

---

## knowledge-graph — 知识图谱/标签

| 脚本 | 功能 | 用法 |
|------|------|------|
| `add_aliases.sh` | 为 Obsidian 添加中文 aliases | `bash add_aliases.sh` |
| `add_tag_link.py` | 在答案行前插入 tag_link 标记 | `python add_tag_link.py` |
| `add_wikilinks.sh` | 自动添加 Obsidian wiki-links | `bash add_wikilinks.sh` |
| `analyze_graph.py` | 分析先修关系映射图 | `python analyze_graph.py` |
| `populate_prereq.sh` | 自动填充 prerequisites | `bash populate_prereq.sh` |
| `update_knowledge_points.py` | 批量更新 knowledge_points | `python update_knowledge_points.py` |

---

## utility — 其他工具

| 脚本 | 功能 | 用法 |
|------|------|------|
| `gen-backup.js` | 生成整卷备份 | `node gen-backup.js` |
| `save-server.js` | 启动 SVG 编辑保存服务 | `node save-server.js` |
| `watermark-pdf.py` | 给 PDF 添加水印 | `python watermark-pdf.py` |
| `debug_regex.ps1` | 调试正则表达式 | `.\debug_regex.ps1` |
| `test_regex.ps1` | 测试正则替换效果 | `.\test_regex.ps1` |
| `test_script.py` | 测试 batch_fix 函数 | `python test_script.py` |

---

## 注意事项

- 部分脚本包含硬编码路径，使用前请检查并修改
- `archive/` 目录下的脚本已归档，仅供参考
- PowerShell 脚本 (.ps1) 仅在 Windows 环境可用

---

*更新于 2026-07-15*
