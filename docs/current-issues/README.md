# CC408 当前待解决问题清单

基于 2026-07-02 代码审查报告，以下问题尚未解决。

---

## 已解决问题

| # | 问题 | 状态 |
|---|------|------|
| 1 | SSH公钥文件提交进仓库 | ✅ 已清理，.gitignore 已添加 |
| 5.1 | 仓库垃圾文件（test_build/、_tmp/等） | ✅ 已清理，.gitignore 已添加 |

---

## 待解决问题

### 🔴 高危（立即处理）

| # | 问题 | 文件位置 | 状态 |
|---|------|----------|------|
| 2 | markup.goldmark.renderer.unsafe: true — XSS风险 | config/_default/hugo.yaml:54-55 | ⬜ 待修复 |

### 🟠 中危（尽快处理）

| # | 问题 | 文件位置 | 状态 |
|---|------|----------|------|
| 3 | 知识图谱构建 O(n³) 三层嵌套循环 | layouts/partials/knowledge-graph-data.html:18-29 | ⬜ 待修复 |
| 4 | knowledge-graph.js 节点跳转链接全部404 | assets/js/knowledge-graph.js:62-69 | ⬜ 待修复 |
| 5 | JSON.parse 无异常处理 | assets/js/knowledge-graph.js:22 | ⬜ 待修复 |
| 6 | 水印保护极易绕过 | assets/js/watermark.js:23,51 | ⬜ 待修复 |
| 7 | convert-all-content.py 硬编码本地路径 | scripts/convert-all-content.py:126 | ⬜ 待修复 |
| 8 | process_code_blocks 误判代码块 | scripts/convert-all-content.py:145-163 | ⬜ 待修复 |

### 🟡 低危（近期处理）

| # | 问题 | 文件位置 | 状态 |
|---|------|----------|------|
| 9 | 全站 meta description 静态 | layouts/_default/baseof.html:7 | ⬜ 待修复 |
| 10 | favicon.ico 路径不跟随 baseURL | layouts/_default/baseof.html:8 | ⬜ 待修复 |
| 11 | navbar.html 导航高亮硬编码 /cc408/ | layouts/partials/navbar.html:7-11 | ⬜ 待修复 |
| 12 | resource-filter.js 搜索框无防抖 | assets/js/resource-filter.js:30 | ⬜ 待修复 |

### 🔵 工程建议

| # | 问题 | 说明 | 状态 |
|---|------|------|------|
| 5.2 | 知识图谱数据双维护 | static/data/knowledge-graph.json 与 partial 不同步 | ⬜ 待统一 |

---

## 统计

- 总问题数：12
- 已解决：2
- 待解决：10
- 完成率：16.7%

---

*更新于 2026-07-14*
