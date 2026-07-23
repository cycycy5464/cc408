# CC408 全维度分析报告

> 生成于：2026-07-22 | 分析范围：交互体验、代码架构、性能优化、Hugo 架构

---

## 一、用户视角体验问题

### 1.1 首页体验

| 问题 | 严重度 | 说明 |
|------|--------|------|
| **首页 Hero 区无实际操作入口** | 🟡 中 | 大面积的渐变标题 + 动画背景，但用户无法在这里做任何操作。3个 CTA 按钮(知识点/刷题/图谱)淹没在 Hero 底部，首屏看不到 |
| **首页加载偏慢** | 🟡 中 | Hero 的 `radial-gradient` 和网格背景 `60px 60px` 的 CSS 渲染在低端设备上有明显卡顿 |
| **最近更新只显示 8 条** | 🟢 低 | 21 章的内容只显示最近 8 条，用户不知道完整内容在哪里 |

### 1.2 刷题体验

| 问题 | 严重度 | 说明 |
|------|--------|------|
| **知识点文章底部「相关题目」点击后跳到试卷页而非单题** | 🟡 中 | 用户想看某知识点相关的一道题，却被带到整张试卷，需要自己找对应题目— 上周已修复 |
| **题库页 `/question/` 分页数据加载** | 🟢 低 | 857+ 题分页 12 题/页，用户翻 72 页才能看完，但每翻一页要重新渲染所有卡片 |
| **搜索无法搜到题目** | 🔴 高 | 搜索索引只索引 `docs` 和 `exam` 区块，不包含 `question` 目录，输入题号/题干关键字搜不到任何题目 |
| **收藏页没有「批量管理」** | 🟢 低 | 用户只能一个个删除收藏，无法批量操作 |
| **模拟题无年份标记** | 🟢 低 | 模拟题在卡片上只显示 "第 N 套"，没有年份上下文 |

### 1.3 导航体验

| 问题 | 严重度 | 说明 |
|------|--------|------|
| **导航栏刷题高亮异常** | 🟡 中 | `/question/` 下的页面在导航栏中被匹配到 `exam` 高亮，但菜单中"刷题"对应的是 `/exam/`。期望：单独高亮 |
| **知识点侧边栏无法快速跳转** | 🟢 低 | 手风琴菜单需要用户一个章节一个章节地点开，无搜索/过滤 |
| **标签页 `/tags/` 跳转到分类页而非直接展示** | 🟡 中 | 用户点了一个标签，跳转到 `/tags/{tag}/` 分类页（之前是标题列表，刚改成卡片），但分类页标题还是"标签：xxx"，和刷题页的上下文割裂 |

### 1.4 移动端体验

| 问题 | 严重度 | 说明 |
|------|--------|------|
| **主页在手机上排版紧凑** | 🟡 中 | Hero 在移动端高度自适应后内容仍然拥挤，CTA 按钮堆叠 |
| **试卷 TOC 在手机上完全隐藏** | 🟢 低 | 需要翻到底部才能点到下一题 |
| **知识点侧边栏在手机上折叠** | 🟢 低 | 折叠后没有明确的入口提示 |

---

## 二、代码审查

### 2.1 架构概览评级

```
架构风格:   静态站点生成器 (Hugo) + 客户端交互 (Vanilla JS)
模板引擎:   Hugo Go Templates
前端框架:   Vanilla JS, D3.js v7, Chart.js
CSS架构:   全局 CSS 自定义属性 + SCSS 分区
数据持久化: localStorage (收藏), 静态 JSON (标签/图谱映射)
```

**总体评价**: ⭐⭐⭐ (6/10) — 功能完备，但存在大量技术债务，JS 代码重复严重，架构边界不清。

---

### 2.2 严重代码问题

#### 🔴 P0: 同一份 JS 交互逻辑在 5 个模板中重复

以下文件各包含一套几乎完全相同的 JS（约 200-250 行），用于：
1. 隐藏 `[tag_link]`
2. 查找 `正确答案：X` 并创建 `.answer-panel`
3. 将 `A\. text` 转换为可点击 `.exam-option`
4. 替换 `【解析】`
5. 收藏按钮逻辑

| 文件 | 行数 |
|------|------|
| `layouts/exam/408quiz-detail.html` | ~200 行内联 JS |
| `layouts/exam/year-detail.html` | ~250 行内联 JS |
| `layouts/exam/single.html` | ~300 行内联 JS |
| `layouts/question/single.html` | 独立 `collect-quiz.js`，但逻辑不同 |
| `layouts/_default/taxonomy.html` | ~200 行内联 JS |
| `layouts/question/chapter-exercises.html` | ~200 行内联 JS |

**影响**：修复一个 bug 需要改 5 个文件。已确认至少有 2 次修复不同步（2026-07 的 lessons.md 中提到）。

**建议**：将题目交互 JS 提取为 `assets/js/question-interaction.js` 共享模块。

#### 🔴 P1: 收藏系统 ID 不统一

| 页面 | 收藏 ID 生成方式 |
|------|-----------------|
| `exam/single.html` | `'fav-' + location.pathname.replace(/\//g, '-') + '-' + qNumber` |
| `exam/408quiz-detail.html` | `year + '-' + qnum` |
| `taxonomy.html` | `qid` (data 属性) 或 `year + '-' + qnum` |
| `chapter-exercises.html` | `$page.File.UniqueID` |

**影响**：同一题在不同页面收藏会生成不同 ID，导致重复收藏或收藏后找不到。

#### 🔴 P2: 搜索索引不包含题目

`layouts/partials/search-index.html` 的搜索索引只索引 `docs` 和 `exam` section 的页面，不包含 `question`。用户输入「队列」搜不到题目，只能搜到知识点文章。

```html
{{ $pages := where .Site.RegularPages "Section" "docs" | append (where .Site.RegularPages "Section" "exam") }}
```

**建议**：将题目内容加入搜索索引（或至少加入标题和知识点标签）。

#### 🟡 P3: `question/list.html` JSON 数据膨胀

当前修改将 `$page.Content`（完整 HTML）写入 JSON：
```hugo
{{ dict ... "content_html" ($page.Content | string) | jsonify | safeJS }}
```

3889 道题的 JSON + 完整 HTML ≈ 300KB+。虽然分页只渲染 12 题，但所有数据一次加载到页面中。

**影响**：
- 首屏 JS 解析时间增加
- 移动端低端设备内存压力
- `jsonify` 对超大数据集的 Hugo 构建时间影响

---

### 2.3 中等问题

#### 🟡 CSS 架构问题

**570 行 `custom.scss` 中混入了多种角色的样式**：
- 全局设计 token（:root 变量）✅
- 布局系统（navbar, hero, content-area, docs-layout, exam-layout）✅
- 组件（card, button, tag, pagination）✅
- **知识图谱专属样式**（`.graph-*` 类，约 50 行）❌ 应该在 graph 模板中
- **标签管理面板样式**（`.tm-*` 类，约 50 行）❌ 应该在 terms 模板中
- **返回按钮样式**（`.back-button-*`，约 80 行）❌ 应该是独立文件

**建议**：按角色拆分：
- `_tokens.scss` — 设计变量 + 主题
- `_layout.scss` — 布局系统
- `_components.scss` — 通用组件
- 各模板内联或独立的 `_exam.scss`、`_graph.scss` 等

#### 🟡 导航栏高亮逻辑脆弱

```hugo
{{ else if hasPrefix $current (print $baseRel "question/") }}{{ $section = "exam" }}
```

`/question/` 的页面被强匹配到 `exam` section。如果新增一个 `/question-bank/` 路由，高亮会断裂。

**建议**：使用 Hugo 的 `.Section` 方法或更精确的路由匹配。

#### 🟡 水印系统可绕过

`watermark.js` 通过 Canvas 绘制水印覆盖层，但用户可以通过 DevTools 删除 `.watermark-layer` DOM 元素或设置 `display:none`。仅防君子不防小人。

---

### 2.4 可复用组件分析

| 组件 | 复用情况 | 建议 |
|------|---------|------|
| **题目交互 JS**（选项/答案/收藏） | ❌ 在 5 个文件中重复 | 提取为 `assets/js/question-interaction.js` |
| **question-block 样式** | ❌ 在 5 个模板中重复定义 | 移到 `_exam.scss` |
| **过滤工具栏**（select/input 组合） | ✅ `question/list.html` 和 `chapter-exercises.html` 各一套 | 可提取为 partial |
| **分页组件** | ✅ 仅 `question-list.js` 有 | 可改为通用组件 |
| **返回按钮** | ✅ 已封装为 `back-button.html` partial | 架构良好 |
| **导航栏** | ✅ 已封装 | 良好 |
| **知识点侧边栏** | ✅ 已封装为 `docs-sidebar.html` | 良好 |
| **exam-year-nav** | ✅ 已封装 | 良好 |

---

## 三、性能瓶颈

### 3.1 构建性能

| 问题 | 影响 |
|------|------|
| **3889 个 .md 文件** | Hugo 构建时遍历所有文件解析 frontmatter，每次 `hugo` 耗时约 40-60s |
| **无 `writeStats: false` 额外配置** | 当前已关闭，但如果开启 purgeCSS 会增加构建时间 |
| **`jsonify` 超大 JSON** | `static/data/tags-data.json` 加 `question/list.html` 的内联 JSON，构建时 JSON 序列化开销大 |
| **图片处理** | `content/question/` 中有大量 SVG 图片，Hugo 默认不处理 SVG，但遍历检查仍耗时 |

### 3.2 运行时性能

| 问题 | 影响 |
|------|------|
| **3889 题 JSON 一次加载** | 题库页面的 JSON 数据包含全部题目信息（含完整 HTML），页面 JS 需解析 300KB+ JSON |
| **D3.js 图谱全量渲染** | 知识图谱页面加载所有节点数据（≈ 1000+ 节点），D3 力导向图在低端设备可能掉帧 |
| **无图片懒加载** | baseof.html 中已排除 SVG 的惰性加载，但普通图片仍可能阻塞渲染 |
| **Chart.js 全量渲染** | tag-analysis 页面中 447 个 KPs 柱状图使用 Chart.js 渲染 447 个 bar，图表高度 800px+ |

### 3.3 建议优化

**高优先级**：
1. 题库页按需加载：初次只加载前 12 题的数据，翻页时异步补充
2. 搜索索引增加题目：将 `question` section 加入 `search-index.html`
3. D3.js 图谱虚拟化：只渲染可见区域的节点，缩放时动态加载

**低优先级**：
4. 图片 WebP 转换：将 PNG/SVG 图片转为 WebP
5. 预加载关键 CSS：将首屏 CSS 内联到 `<head>`，非关键 CSS 异步加载

---

## 四、Hugo 架构优化建议

### 4.1 Hugo 能力未被充分利用

| Hugo 特性 | 当前使用 | 建议 |
|-----------|---------|------|
| **Hugo Pipes (asset pipeline)** | 仅用于 `custom.scss` 编译 + `question-list.js` 的 minify | 可以用于：JS 打包、图片处理、PostCSS 处理 |
| **Hugo Modules** | 未使用 | 可以引入主题作为模块，而不是 copy-paste |
| **Cascade (前置元数据层叠)** | 未使用 | 可以统一设置 `question`目录下所有文件的默认参数 |
| **Content View Templates** | 未使用 | 可以为 `question` 创建 `_default/question.json.json` 输出 JSON |
| **Hugo Output Formats** | 仅 HTML | 可以输出 `search.json` 或 `questions.json` API |
| **Hugo Data Templates** | `data/subjects.yaml` 已使用 | 可以生成更多结构化数据 |
| **Site.RegularPages 过滤** | 多处使用 `where .Site.RegularPages "Section" "question"` | 可以创建 `.Pages` 的缓存集合 |
| **Hugo Menus** | 菜单已定义但导航硬编码 | 可以用 menus 系统管理全部导航 |

### 4.2 架构可改进方向

#### 4.2.1 将题库数据输出为独立 JSON API

当前 `question/list.html` 将完整 JSON 内联在页面中。更好的做法：

```yaml
# config/_default/hugo.yaml
outputs:
  section: [HTML]
  page: [HTML]
  # 新增 
  question: [HTML, JSON]
```

创建 `layouts/question/single.json.json` 输出单题的 JSON 数据，供前端 AJAX 按需加载。

#### 4.2.2 使用 Hugo Cache 减少重复查询

```hugo
{{ $qpages := where .Site.RegularPages "Section" "question" }}
```

这个查询在 `exam/408quiz-detail.html`、`exam/single.html`、`question/list.html`、`chapter-exercises.html`、`docs/single.html` 等多个模板中重复。可以使用 Hugo 的 `partialCached` 或缓存 Partial：

```hugo
{{ partialCached "question-pages" . "question-pages" }}
```

#### 4.2.3 利用 Hugo Collection 预计算

对于 tag-analysis 页面的标签统计，可以通过 Hugo 的 `resources` 在构建时预计算并输出为 JSON，而不是在客户端 Chart.js 渲染时再计算。

---

## 五、总结优先级

| 优先级 | 问题 | 类型 | 估算工时 |
|--------|------|------|---------|
| 🔴 P0 | **题目交互 JS 在 5 个模板中重复** | 代码质量 | 4h |
| 🔴 P0 | **收藏 ID 不统一** | Bug | 2h |
| 🔴 P1 | **搜索搜不到题目** | 功能缺失 | 3h |
| 🟡 P2 | **CSS 架构混乱** | 代码质量 | 4h |
| 🟡 P2 | **题库 JSON 膨胀** | 性能 | 3h |
| 🟡 P2 | **导航高亮硬编码** | 代码质量 | 1h |
| 🟢 P3 | **知识点侧边栏无搜索** | UX 改进 | 2h |
| 🟢 P3 | **收藏页批量管理** | 功能增强 | 2h |
| 🟢 P3 | **Hugo Output Formats 输出 JSON** | 架构优化 | 3h |

---

*本报告基于 2026-07-22 的代码状态编写*
