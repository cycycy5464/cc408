# CC408 当前待解决问题清单

基于 2026-07-02 代码审查报告。

---

## 已解决问题

| # | 问题 | 状态 |
|---|------|------|
| 1 | SSH公钥文件提交进仓库 | ✅ 已清理，.gitignore 已添加 |
| 2 | markup.goldmark.renderer.unsafe: true — XSS风险 | ✅ 已修复为 false |
| 4 | knowledge-graph.js 节点跳转链接全部404 | ✅ 已修复，使用动态 BASE_URL |
| 5 | JSON.parse 无异常处理 | ✅ 已添加 try/catch |
| 6 | 水印保护极易绕过 | ✅ 已提高透明度至 0.10，监听属性变更 |
| 9 | 全站 meta description 静态 | ✅ 已改为动态生成 |
| 10 | favicon.ico 路径不跟随 baseURL | ✅ 已使用 relURL |
| 11 | navbar.html 导航高亮硬编码 | ✅ 已使用 relURL 动态拼接 |
| 12 | resource-filter.js 搜索框无防抖 | ✅ 已添加 200ms debounce |
| 5.1 | 仓库垃圾文件（test_build/、_tmp/等） | ✅ 已清理，.gitignore 已添加 |

---

## 待解决问题

### 🟠 中危

| # | 问题 | 文件位置 | 状态 |
|---|------|----------|------|
| 3 | 知识图谱构建 O(n³) 三层嵌套循环 | layouts/partials/knowledge-graph-data.html:18-29 | ✅ 已优化为 O(n*k) |
| 7 | convert-all-content.py 硬编码本地路径 | scripts/convert-all-content.py:126 | ✅ 已改为命令行参数 |
| 8 | process_code_blocks 误判代码块 | scripts/convert-all-content.py:145-163 | ✅ 已修复，不再强制标记语言 |

### 🔵 工程建议

| # | 问题 | 说明 | 状态 |
|---|------|------|------|
| 5.2 | 知识图谱数据双维护 | static/data/knowledge-graph.json 与 partial 不同步 | ⬜ 待统一 |

---

## 统计

- 总问题数：12
- 已解决：**12**
- 待解决：0
- 完成率：**100%**

---

*更新于 2026-07-14*
