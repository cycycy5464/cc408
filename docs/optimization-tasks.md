# CC408 优化任务清单

> 按照代码审查报告优先级排序

## 🔴 P0 — 必须修复

- [x] **P0-1: 题目交互 JS 抽取为共享模块**
  - 创建 `assets/js/question-interaction.js` ✅
  - `exam/408quiz-detail.html` 已迁移 ✅
  - 待迁移：`exam/year-detail.html`、`exam/single.html`、`_default/taxonomy.html`、`question/chapter-exercises.html`、`question/list.html`

- [x] **P0-2: 收藏 ID 统一**
  - 共享模块中统一使用 `{source}-{year}-{number}` 格式 ✅
  - taxonomy.html 已添加 `data-source` 属性 ✅
  - 待迁移模板继承统一逻辑

## 🔴 P1 — 功能缺失

- [ ] **P1-1: 搜索可搜到题目**
  - 将 `question` section 加入 `search-index.html`
  - 使用题目标题 + 知识点标签 + 题干摘要作为搜索内容

## 🟡 P2 — 代码质量/性能

- [ ] **P2-1: CSS 分区**
  - 将图谱样式（`.graph-*`）移到 graph 模板
  - 将标签管理样式（`.tm-*`）移到 terms 模板
  - 将返回按钮样式移到独立文件或 partial

- [ ] **P2-2: 题库 JSON 按需加载**（评估后决定是否执行）
  - 改为翻页时 fetch 单页数据而非一次加载全部 3889 题

- [ ] **P2-3: 导航高亮改用 `.Section` 检测**

## 🟢 P3 — 体验增强

- [ ] **P3-1: 知识点侧边栏搜索**
- [ ] **P3-2: 收藏页批量操作**
- [ ] **P3-3: Hugo Output Formats 输出 JSON API**
