# CC408 项目完整索引

> **408 考研知识平台** — 基于 Hugo 的静态网站，涵盖数据结构、计算机组成原理、操作系统、计算机网络四门课程的知识点笔记与真题练习。

**仓库**: `github.com/cycycy5464/cc408`  
**线上地址**: `https://cycycy5464.github.io/cc408/`  
**技术栈**: Hugo 0.164.0 + Go Modules + D3.js + KaTeX + Chart.js

---

## 快速导航

| 想做什么 | 去哪里 |
|---------|--------|
| 了解项目架构 | [项目结构](#项目结构) |
| 编写知识点笔记 | [content/docs/](#contentdocs--知识点笔记) |
| 添加真题题目 | [content/question/](#contentquestion--真题题目) |
| 修改页面模板 | [layouts/](#layouts--页面模板) |
| 修改样式 | [assets/css/](#assetscss--样式文件) |
| 修改交互逻辑 | [assets/js/](#assetsjs--交互脚本) |
| 运行脚本工具 | [scripts/](#scripts--脚本工具) |
| 了解部署流程 | [GitHub Actions](#github-actions--部署) |
| 查看经验教训 | [docs/lessons.md](#经验教训) |

---

## 项目结构

```
cc408/
├── .github/workflows/      # CI/CD 部署配置
├── assets/                 # Hugo 资源管道 (构建时处理)
│   ├── css/                #   样式文件 (SCSS)
│   └── js/                 #   交互脚本 (JS)
├── config/                 # Hugo 配置文件
│   └── _default/           #   默认配置
├── content/                # 所有 Markdown 内容
│   ├── code/               #   算法实现
│   ├── docs/               #   知识点笔记 (4门课)
│   ├── exam/               #   考试页面
│   ├── graph/              #   知识图谱
│   ├── question/           #   真题题目 (1300+题, exam/模拟题/simulate/章节练习)
│   ├── resources/          #   学习资源
│   ├── search/             #   搜索页面
│   └── study-methods/      #   学习方法
├── data/                   # Hugo 数据文件
├── docs/                   # 项目文档 (非 Hugo 内容)
├── layouts/                # Hugo 模板 (渲染逻辑)
├── scripts/                # 工具脚本
├── static/                 # 静态文件 (原样复制)
├── removed_dups/          # 已移除的重复模拟题
└── test_build/             # 测试构建产物
```

---

## 配置文件详解

### Hugo 核心配置 (`config/_default/`)

| 文件 | 作用 | 关键配置 |
|------|------|---------|
| `hugo.yaml` | 站点基础配置 | `baseURL`, `title: CC408`, `theme: hugo-theme-stack`, 语言 `zh`, 分类系统 (tags/subjects/years/knowledge_points) |
| `params.yaml` | 外观与功能开关 | 暗色主题默认, KaTeX 数学公式, 搜索启用, 页脚版权 |
| `menus.yaml` | 导航菜单 | 首页/知识点/练习/合集/图谱/真题分析/标签/资源 (8项) |
| `languages.yaml` | 语言配置 | 中文简体 `zh-CN` |
| `module.yaml` | Hugo 模块挂载 | 标准路径映射 |

### 其他配置

| 文件 | 作用 |
|------|------|
| `go.mod` | Go 模块定义 (Hugo 使用 Go Modules 管理主题) |
| `package.json` | Node.js 依赖 (`xmldom` 用于脚本) |
| `hugo_stats.json` | 构建统计 (PurgeCSS 使用) |

---

## content/ — 内容目录

### content/docs/ — 知识点笔记

**结构**: 4门课程 → 28章 → ~112篇文章

```
docs/
├── data-structure/         # 数据结构 (10章)
│   ├── ch00-intro/         #   绪论
│   ├── ch01-linear-list/   #   线性表
│   ├── ch02-stack-queue/   #   栈和队列
│   ├── ch03-string/        #   串
│   ├── ch04-tree/          #   树
│   ├── ch05-graph/         #   图
│   ├── ch06-search/        #   查找
│   ├── ch07-sort/          #   排序
│   ├── ch07-search/        #   查找 (续)
│   └── ch08-sort/          #   排序 (续)
├── computer-org/           # 计算机组成原理 (7章)
│   ├── ch00-overview/      #   计算机系统概述
│   ├── ch01-data-rep/      #   数据的表示和运算
│   ├── ch02-memory/        #   存储器层次结构
│   ├── ch03-instruction/   #   指令系统
│   ├── ch04-cpu/           #   中央处理器
│   ├── ch05-bus/           #   总线
│   └── ch06-io/            #   输入输出系统
├── os/                     # 操作系统 (5章)
│   ├── ch00-overview/      #   操作系统概述
│   ├── ch01-process/       #   进程管理
│   ├── ch02-memory/        #   内存管理
│   ├── ch03-file/          #   文件管理
│   └── ch04-io/            #   设备管理
└── network/                # 计算机网络 (6章)
    ├── ch00-overview/      #   计算机网络概述
    ├── ch01-physical/      #   物理层
    ├── ch02-datalink/      #   数据链路层
    ├── ch03-network/       #   网络层
    ├── ch04-transport/     #   传输层
    └── ch05-application/   #   应用层
```

**单篇文章格式** (`content/docs/data-structure/ch01-linear-list/linear-list.md`):
```yaml
---
title: "线性表"
difficulty: 2              # 难度 1-3
tags: ["数据结构", "线性表"]
prerequisites: ["绪论"]    # 先修知识点
knowledge_points: ["线性表的定义", "顺序存储"]  # 关联知识点
---
```

**关联**: 文章通过 `tags` 和 `knowledge_points` 与真题关联，通过 `prerequisites` 构建知识图谱。

---

### content/question/ — 真题题目

**数量**: 857 道真题 + 376 道模拟题 (2009-2026年 + 8套模拟题)

**文件命名**: `{year}-{subject}-{number}.md`, 模拟题在 `simulate/{set}/` 子目录
- `year`: `2009`-`2026`, 模拟题在子目录 `simulate/1/` 到 `simulate/8/`
- `subject`: `ds` (数据结构), `co` (组成原理), `os` (操作系统), `cn` (计算机网络)
- `number`: `001`-`047` (001-040 选择题, 041-047 综合应用题)

**Frontmatter 格式**:
```yaml
---
title: "2009 年第 1 题"
years: [2009]
subjects: ["data-structure"]
knowledge_points: ["线性表"]
question_type: "choice"    # choice (选择题) / comprehensive (综合题)
difficulty: 2
source: "408真题"
number: 1
---
```

**题目内容格式**:
```markdown
以下关于线性表的叙述中，正确的是

A\. 线性表的存储结构只能采用顺序存储

B\. 线性表的存储结构只能采用链式存储

C\. 线性表的存储结构可以采用顺序存储，也可以采用链式存储

D\. 以上都不对

[tag_link]

正确答案：C

【解析】线性表的存储结构...
```

**数据流**:
```
content/question/*.md
    ↓ Hugo 构建
Static HTML (包含 .q-body + .q-number + 按钮)
    ↓ 浏览器 JS (5步 DOM 转换)
交互页面 (点击选项、查看答案、收藏)
```

---

### content/exam/ — 考试页面

```
exam/
├── _index.md               # 考试中心首页 (4个入口卡片)
├── 408quiz/                # 真题试卷
│   ├── _index.md           #   年份列表
│   ├── 2009/_index.md      #   2009年真题 (type: exam, layout: year-detail)
│   ├── ...                 #   2010-2025
│   └── 2026/_index.md      #   2026年真题
├── simulate/               # 模拟题
│   ├── _index.md           #   模拟题列表
│   ├── set-1/_index.md     #   第1套模拟题
│   └── ...                 #   set-2 到 set-8
├── quiz-collection/        # 收藏题目 (localStorage)
└── ...
```

**试卷组装逻辑**:
```
content/exam/408quiz/{year}/_index.md  →  设置 year 参数
        ↓
layouts/exam/year-detail.html          →  查询 content/question/*.md
                                          (筛选 years 包含该年份的题目)
        ↓
完整试卷页面                           →  47道题，按题号排序
```

---

### content/graph/ — 知识图谱

单个 `_index.md`，使用 `layouts/graph/list.html` 渲染全页 D3.js 力导向图可视化。

**数据来源**:
- 知识点节点: `layouts/partials/knowledge-graph-data.html` 从 `content/docs/` 提取
- 题目关联: `static/mapping/question-kp-mapping.json`

---

### content/code/ — 算法实现

经典算法的 C 语言实现:
- `banker.md` - 银行家算法
- `clock.md` - Clock 页面置换算法
- `lru.md` - LRU 缓存
- `monitor.md` - 管程
- `philosopher.md` - 哲学家就餐问题
- `producer_consumer.md` - 生产者消费者问题
- `reader_writer.md` - 读者写者问题
- `spinlock.md` - 自旋锁实现

---

### content/resources/ — 学习资源

可下载的学习资料，如思维导图等。

---

### content/study-methods/ — 学习方法

| 文件 | 内容 |
|------|------|
| `fast_study.md` | 快速学习技巧 |
| `methodology.md` | 学习方法论 |
| `tag-analysis.md` | 考试标签/知识点分析 (Chart.js) |
| `use_anki.md` | Anki 记忆卡片使用指南 |

---

### content/search/ — 搜索

启用全文搜索功能，生成搜索索引。

---

## layouts/ — 页面模板

### 核心模板

| 文件 | 作用 |
|------|------|
| `_default/baseof.html` | **主布局** — 定义 `<head>` (KaTeX/Google Fonts/SCSS)、`<body>` (导航栏/主内容/页脚)，所有页面继承此模板 |
| `_default/index.html` | **首页** — Hero 区域 (渐变标题+3个按钮)、4门课程卡片、最近更新 (8项)、学习工具网格 (5个) |
| `_default/single.html` | **通用单页** — 课程标签、难度星级、标签、文章内容、关联真题 |
| `_default/list.html` | **通用列表** — 标题 + 内容区域 |

### 题目模板 (`layouts/question/`)

| 文件 | 作用 |
|------|------|
| `single.html` | **单题页面** — 题号、元信息行 (年份/课程/难度/知识点/题型)、内容区、答案折叠面板、前后导航、收藏按钮。 |
| `list.html` | **题库列表** — 过滤工具栏 (题源/年份/套数/科目/章节/题型下拉+搜索)、摘要卡片网格、客户端分页。数据 JSON 约 50KB。 |
| `chapter-exercises.html` | **章节习题** — 交互卡片（选项/答案/收藏），选科目+章节后显示 |

### 考试模板 (`layouts/exam/`)

| 文件 | 作用 |
|------|------|
| `408quiz-detail.html` | **真题整卷** — 按年份组装所有题目、右侧 TOC 导航、交互卡片、逐题收藏、全局显示所有解析 |
| `year-detail.html` | **模拟卷整卷** — 同上，支持 simulate set 和 408quiz 两类 |
| `single.html` | **单套题页** — 解析 `<h5>` 标题结构分题，选项/答案/收藏 |
| `quiz-collection.html` | **收藏页面** — 从 localStorage 读取，支持练习/显示双模式 |
| `list.html` | **考试中心** — 根目录显示4个入口卡片，子目录显示筛选后的试卷列表 |

### 知识点模板 (`layouts/docs/`)

| 文件 | 作用 |
|------|------|
| `single.html` | **知识点详情** — 双栏布局：左侧边栏 (260px, 固定) 显示课程分组和文章链接，右侧内容区显示文章 |
| `list.html` | **知识点列表** — 按课程分组显示 |

### 图谱模板 (`layouts/graph/`)

| 文件 | 作用 |
|------|------|
| `list.html` | **知识图谱页面** — 全页 D3.js 力导向图，选项卡 (知识点/真题/模拟/管理)、搜索、信息面板 |

### 可复用组件 (`layouts/partials/`)

| 文件 | 作用 |
|------|------|
| `navbar.html` | **顶部导航栏** — 品牌 Logo、7个菜单项 (Hugo `.Section` 自动高亮)、主题切换按钮 |
| `footer.html` | **页脚** — 版权年份插值 |
| `back-button.html` | **返回按钮** — 页面左上角智能返回按钮，支持历史记录和状态保存（含内联样式） |
| `docs-sidebar.html` | **知识点侧边栏** — 手风琴章节导航 + 搜索过滤 |
| `knowledge-graph-data.html` | **知识图谱数据** — Hugo 模板生成 JSON (节点+链接)，O(n*k) 优化 |
| `search-index.html` | **搜索索引** — 生成搜索 JSON（含 docs/exam/question 三大区块） |
| `watermark.html` | **水印** — Canvas 水印覆盖层 (防截图) |

---

## assets/ — 资源管道 (构建时处理)

### assets/css/ — 样式

| 文件 | 作用 |
|------|------|
| `custom.scss` | **主样式表** (315行) — CSS 自定义属性 (暗色/亮色主题)、字体 (Inter/Noto Sans SC/JetBrains Mono)、导航栏 (毛玻璃)、Hero (网格动画背景)、卡片、侧边栏、响应式断点、打印样式 |
| `_exam.scss` | 考试相关样式 |
| `_quiz-collection.scss` | 收藏页面样式 |

### assets/js/ — 交互脚本

| 文件 | 行数 | 作用 |
|------|------|------|
| `knowledge-graph.js` | 1220 | **D3.js 知识图谱引擎** — 多选项卡、下钻导航、力导向布局、搜索、管理标签编辑器 |
| `question-interaction.js` | 175 | **题目交互共享模块** — 选项转换、答案折叠、收藏逻辑，供 5 个模板共用 |
| `theme-toggle.js` | - | 主题切换 — 读写 `localStorage('cc408-theme')`，触发 `cc408:themechange` 事件 |
| `back-button.js` | - | **智能返回按钮** — 支持历史记录导航、页面状态保存与恢复、智能返回目标判断 |
| `collect-quiz.js` | - | 单题收藏 — 从 DOM 提取题目数据，保存到 `localStorage('quiz_collections')` |
| `quiz-collection.js` | - | 收藏页面渲染 — 从 localStorage 读取，创建可过滤卡片网格 |
| `resource-filter.js` | - | 资源页面过滤 |
| `watermark.js` | - | Canvas 水印生成 (防截图) |

---

## static/ — 静态文件 (原样复制)

| 目录 | 内容 |
|------|------|
| `images/questions/` | 题目图片 (SVG/PNG)，按年份-题号组织 |
| `images/docs/` | 知识点图片 |
| `data/` | JSON 数据文件 (题目-知识点映射、标签统计) |
| `data/questions-all.json` | **全量题目 API**（3442 题，CI 自动生成） |
| `js/` | JS 静态副本 |
| `css/` | CSS 编译产物 |
| `mapping/` | 知识点映射数据 |

---

## scripts/ — 脚本工具

详见 [scripts/README.md](scripts/README.md)

### 按功能分类

| 分类 | 脚本数 | 主要用途 |
|------|--------|---------|
| `content-migration/` | 4 | 内容转换、迁移、爬取 |
| `question-fix/` | 3 | 选项恢复、重复检测 |
| `image-processing/` | 6 | SVG 修复、图片重组 |
| `content-validation/` | 3 | 内容审计、格式验证 |
| `knowledge-graph/` | 9 | 标签管理、先修关系、标签数据生成 |
| `utility/` | 6 | 备份、水印、调试 |

---

## data/ — 数据文件

### data/subjects.yaml

定义四门课程，全站引用:

```yaml
- key: data-structure    # cls: ds, icon: 📊
- key: computer-org      # cls: co, icon: ⚙️
- key: os                # cls: os, icon: 🖥️
- key: network           # cls: cn, icon: 🌐
```

---

## .github/workflows/ — CI/CD

### publish-cc408.yaml

**触发**: push 到 `master` 分支 或 手动触发

**构建流程**:
1. Checkout (完整历史)
2. 安装 Hugo 0.164.0 extended
3. 构建: `hugo --minify`
4. 上传 `./public` 为 artifact
5. 部署到 GitHub Pages

---

## docs/ — 项目文档

```
docs/
├── PROJECT_INDEX.md          # 本索引（唯一入口）
├── architecture/             # 系统架构与需求
│   ├── requirements.md       #   完整需求文档
│   ├── question-system.md    #   题目渲染系统
│   ├── improvement-plan.md   #   前端改进计划
│   ├── hugo-knowledge-graph.md
│   ├── content-migration-guide.md
│   ├── question-data-sources.md
│   └── lessons.md            #   经验教训（汇总）
├── reviews/                  # 代码审查与审计
│   ├── code-review-2026-07-22.md
│   ├── CC408代码审查报告.docx
│   └── frontend-audit.md
├── optimization/             # 优化 sprint
│   └── tasks.md              #   P0-P3 任务进度
├── issues/                   # 当前问题追踪
│   └── current-issues/       #   14 个问题文档
├── guides/                   # 开发指南
│   ├── svg编辑.md
│   ├── HUGO_PERFORMANCE.md
│   ├── 题目颗粒化重构方案.md
│   ├── fix-docs-sidebar.md
│   └── 按钮修改.md
└── archive/                  # 已归档（历史备份）
    ├── backup-整卷/          #   17份真题整卷
    ├── simulate-backup/      #   8套模拟卷
    ├── verification-checklist.md
    ├── session-progress.md
    └── superpowers/          #   过期计划
```

---

## tasks/ — 任务跟踪

| 目录/文件 | 内容 |
|-----------|------|
| `docs/current.md` | 当前任务进度 |
| `docs/lessons.md` | **经验教训** (57+ 条) — 修改前必读! |
| `408-crawler/` | 408 爬虫项目 (crawler.js + 数据备份) |
| `真题修复/` | 真题修复项目 (脚本+文档+备份) |
| `scripts/` | 任务专用脚本 (13个) |

---

## 关键架构模式

### 页面渲染规则

**URL → 模板路由全表**:

| URL 路径 | 模板文件 | 内容来源 |
|:---------|:---------|:---------|
| `/` | `_default/index.html` | `content/_index.md` |
| `/docs/` | `docs/list.html` | `content/docs/_index.md` |
| `/docs/{subject}/` | `docs/list.html` | `content/docs/{subject}/_index.md` |
| `/docs/{subject}/{article}/` | `docs/single.html` | 相应 .md 文章 |
| `/exam/` | `exam/list.html` | `content/exam/_index.md` |
| `/exam/408quiz/` | `exam/408quiz/list.html` | `content/exam/408quiz/_index.md` |
| `/exam/408quiz/{year}/` | `exam/single.html` | `content/exam/408quiz/{year}/_index.md` |
| `/exam/simulate/` | `exam/list.html` | `content/exam/simulate/_index.md` |
| `/exam/simulate/set-{n}/` | `exam/year-detail.html` | `content/exam/simulate/set-{n}/_index.md` |
| `/question/` | `question/list.html` | `content/question/_index.md` |
| `/question/{id}/` | `question/single.html` | 相应 .md 单题 |
| `/code/` | `code/list.html` | `content/code/_index.md` |
| `/graph/` | `graph/list.html` | — (D3.js) |
| `/search/` | `search/list.html` | — (全文搜索) |
| `/resources/` | `resources/list.html` | `content/resources/_index.md` |
| `/study-methods/tag-analysis/` | `_default/tag-analysis.html` | `static/data/tags-data.json` |
| `/knowledge_points/{tag}/` | `_default/taxonomy.html` | 标签分类页 |
| `/exam/quiz-collection/` | `exam/quiz-collection.html` | localStorage |
| `/tags/` | `_default/terms.html` | Hugo 分类系统 |

**模板查找顺序**: `layouts/{section}/{subsection}/list.html` → `layouts/{section}/list.html` → `layouts/_default/list.html`

**题目内容格式 (选择题)**:
```markdown
题干文本，可以包含 $LaTeX$ 和 Markdown 链接。

A\. 选项一
B\. 选项二
C\. 选项三
D\. 选项四

[tag_link]

正确答案：A

分析文本...
```
- 选项使用 `\.` 转义句点，选项间**无空行**
- `[tag_link]` 独占一行，前后空行分隔
- `正确答案：X` 独占一行，后空一行与分析文本分离

**综合题格式**: `question_type: "comprehensive"`。用 `[tag_link]` 切分题干与解析，无 `正确答案` 行。

**筛选举例**:
| 场景 | Hugo/JS 规则 |
|:----|:-------------|
| 真题年份列表排除模拟题 | `hasPrefix .Name "simulate"` 过滤 |
| 真题整卷过滤 | `in .Params.years $year` |
| 模拟卷整卷过滤 | `eq .Params.source "模拟题"` AND `eq .Params.set $.Params.set` |
| 题目库筛选 | 客户端 JS `data-*` 属性匹配 |

### 题目渲染流程

```
作者编写 Markdown + Frontmatter
        ↓
Hugo 构建 → 解析 frontmatter，渲染 Markdown，选择模板
        ↓
静态 HTML → 包含原始 .q-body + .q-number + 按钮
        ↓
浏览器 JS (5步 DOM 转换)
  1. 隐藏 [tag_link]
  2. 折叠答案
  3. 转换选项为可点击 div
  4. 替换 【解析】
  5. 添加显示按钮
        ↓
交互页面 → 点击选项、查看答案、收藏
```

### 知识图谱数据流

```
content/docs/*.md frontmatter (prerequisites, subject, difficulty)
        ↓
layouts/partials/knowledge-graph-data.html → 生成 JSON (节点+链接)
        ↓
assets/js/knowledge-graph.js → D3.js 力导向可视化
        ↓
static/mapping/question-kp-mapping.json → 题目-知识点映射 (真题选项卡)
```

### 收藏系统

```
exam/408quiz-detail.html / year-detail.html / taxonomy.html / question/single.html / chapter-exercises.html
    ↓ question-interaction.js / collect-quiz.js 保存到 localStorage (共享模块)
exam/quiz-collection/    → quiz-collection.js 读取同一 key，渲染卡片
```

统一使用 `quiz_collections` localStorage key。收藏 ID 格式：`{year}-{number}`（真题）或 `sim-{set}-{number}`（模拟题）。

---

## 经验教训

修改项目前**必须阅读** `docs/architecture/lessons.md`，关键要点:

1. **Hugo relURL**: 不要前缀 `/` — `"docs/" | relURL` 才正确
2. **菜单 URL**: Hugo 自动在 menu 配置中解析 baseURL
3. **导航高亮**: 使用 Hugo `.Section` 方法，不要手动 `hasPrefix`
4. **列表作用域**: 使用 `.CurrentSection` 过滤，不要用全局 `where`
5. **文件编码**: 始终 UTF-8；不要用 PowerShell `Set-Content` 处理 `.md` 文件
6. **SVG foreignObject**: 不能在 `<img>` 标签中渲染；必须用 `<object>` 标签
7. **答案折叠**: `[tag_link]` 标记分隔题干和答案
8. **图片路径**: 从 `content/question/` 使用绝对路径 `/cc408/images/questions/...`
9. **批量脚本**: 先测试 2-3 个文件，验证后再应用全部
10. **题目选项**: 必须使用 `A\. text` 格式 (转义点号)，每行一个选项
11. **共享 JS 早做**: 交互逻辑出现第 2 次时就该抽取模块，不要等到第 5 次
12. **收藏 ID 统一**: 跨页面共享数据（收藏 ID）必须在设计阶段统一格式
13. **内网 git**: 用 HTTPS remote + GCM，SSH 端口 22 可能不通

---

## 快速开始

### 本地开发

```bash
# 安装 Hugo
brew install hugo  # macOS
# 或下载: https://github.com/gohugoio/hugo/releases

# 启动开发服务器
hugo server -D

# 访问 http://localhost:1313/cc408/
```

### 构建

```bash
hugo --minify
# 输出到 public/ 目录
```

### 部署

推送到 `master` 分支，GitHub Actions 自动构建部署到 GitHub Pages。

---

*索引生成于 2026-07-22*
