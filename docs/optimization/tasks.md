# CC408 优化任务清单

> 按照代码审查报告优先级排序

## 🔴 P0 — 必须修复

- [x] **P0-1: 题目交互 JS 抽取为共享模块**
  - `assets/js/question-interaction.js` 创建 ✅
  - 迁移：`exam/408quiz-detail.html`、`exam/year-detail.html`、`exam/single.html`、`taxonomy.html`、`chapter-exercises.html` ✅
  - 内联 JS 总计减少 **~1120 行**

- [x] **P0-2: 收藏 ID 统一**
  - 共享模块 `buildFavoriteId()` 统一 `{source}-{year}-{number}` 格式
  - 所有模板 question-block 添加 `data-source`/`data-set`/`data-year`/`data-number`

## 🔴 P1 — 功能缺失

- [x] **P1-1: 搜索可搜到题目**
  - `search-index.html` 新增 408 真题索引
  - 搜索结果显示年份/科目/题号/题干摘要

## 🟡 P2 — 代码质量/性能

- [x] **P2-1: CSS 分区** — `.graph-*` → `graph/list.html`、`.tm-*` → `terms.html`、`.back-button-*` → `back-button.html`。`custom.scss` 505→343 行
- [x] **P2-2: 题库 JSON 按需加载** — 移除 `content_html` 字段，JSON 从 ~300KB 降至 ~50KB
- [x] **P2-3: 导航高亮改用 `.Section` 方法** — 替代硬编码 `hasPrefix` 链

## 🟢 P3 — 体验增强

- [x] **P3-1: 知识点侧边栏搜索** — 输入即过滤章节和文章
- [x] **P3-2: 收藏页批量操作** — 全选/勾选框/批量删除/选择计数

## 🐛 修复的 Bug

- [x] taxonomy.html 模板结构损坏（Python re.sub 残留旧代码）
- [x] taxonomy.html 普通标签页显示 TOC/全部解析（判定 `$isKp` 分支）
- [x] taxonomy.html 课后题标签按科目→章节→小节手风琴结构
- [x] chapter-exercises.html 缺少 `{{ end }}` 闭合标签
- [x] chapter-exercises.html 残留已删除函数调用
- [x] chapter-exercises.html 未选科目/章节时卡片不应展示
- [x] chapter-exercises.html 新增小节筛选层级
- [x] custom.scss 孤立 `}` 导致 SCSS 编译失败
- [x] docs/list.html 学科页双返回按钮
- [x] docs/single.html 返回按钮样式丢失（侧边栏改用内联样式）
- [x] back-button.js 返回目标路径过浅（按深度分级）
- [x] 课后题卡片标题改为小节名+题号
- [x] question-card.html 添加 `data-section` 属性


## 🔧 轻量重构/清理
- [x] 图片原生 lazy loading（render-image.html hook）
- [x] 移除 JS 冗余懒加载（baseof.html 精简）
- [x] 删除未使用 CSS：knowledge-card, filter-bar（custom.scss -8 行）
- [x] collect-quiz.js ID 统一为 {year}-{number} 格式（与共享模块一致）
- [x] **P3-3: JSON API** — generate-questions-json.py 生成 static/data/questions-all.json（3442 题）
- [x] 构建流程集成 — deploy workflow 中自动运行 generator


## 📋 数据修正
- [x] chapter7-search/005.md 拆分 Q5/Q6（Q5 单独保留，Q6 提取至 .bak）
- [ ] chapter7-search/006-050.md 编号链整体偏移（Q7→006 等，需后续处理）
