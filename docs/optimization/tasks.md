# CC408 优化任务清单

> 按照代码审查报告优先级排序

## 🔴 P0 — 必须修复

- [x] **P0-1: 题目交互 JS 抽取为共享模块**
  - `assets/js/question-interaction.js` ✅
  - `exam/408quiz-detail.html` ✅ 内联 JS ~400→~60 行
  - `exam/year-detail.html` ✅ 内联 JS ~500→~70 行
  - `_default/taxonomy.html` ✅ 已迁移
  - `question/chapter-exercises.html` ✅ 已迁移
  - 待迁移：`exam/single.html`（结构特殊，需要独立重构）、`question/list.html`（JS 渲染方式）

- [x] **P0-2: 收藏 ID 统一**
  - 共享模块 `buildFavoriteId()` ✅ `{source}-{year}-{number}` 格式
  - 所有模板 question-block 已添加 `data-source`/`data-set`/`data-year`/`data-number` ✅

## 🔴 P1 — 功能缺失

- [x] **P1-1: 搜索可搜到题目**
  - `search-index.html` 新增 `408真题` 题目索引 ✅
  - 搜索结果显示年份/科目/题号/题干摘要 ✅
  - 题库结果卡片蓝色左边框区分 ✅

## 🟡 P2 — 代码质量/性能

- [x] **P2-1: CSS 分区** — 将非通用样式（`.graph-*`、`.tm-*`、`.back-button-*`）移出 `custom.scss`
- [ ] **P2-2: 题库 JSON 按需加载**（评估后决定是否执行）
- [ ] **P2-3: 导航高亮改用 `.Section` 检测**

## 🟢 P3 — 体验增强

- [ ] **P3-1: 知识点侧边栏搜索**
- [ ] **P3-2: 收藏页批量操作**
- [ ] **P3-3: Hugo Output Formats 输出 JSON API**
