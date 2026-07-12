# 408 真题渲染系统

## 内容存储

每题一个独立 Markdown 文件，位于 `content/question/`。

### 命名规则

```
{year}-{subject}-{number}.md
```

| 部分 | 示例 | 说明 |
|------|------|------|
| `{year}` | `2009`, `2024`, `simulate-1` | 真题年份或模拟卷标识 |
| `{subject}` | `ds`, `co`, `os`, `cn` | 科目缩写 |
| `{number}` | `001`–`047` | 题号（001–040 选择，041–047 综合） |

### 前置元数据

```yaml
---
title: "2024 计算机网络 第33题"
date: 2026-07-07
type: question
years:
  - "2024"
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "choice"          # choice | comprehensive
difficulty: 3                    # 1–4
source: "408真题"
number: 33
---
```

### 正文格式

```
选择题：
题面文字...

A. 选项
B. 选项
C. 选项
D. 选项

[tag_link]                       ← 分隔标记（答案折叠关键）

正确答案：B                       ← 选择题格式
> 解析文本...

综合题：
题面文字...
（可含图片）

[tag_link]
[tag_link]                       ← 双重标记

答案与解析文本...
```

## 年份页面组装

### 触发器

`content/exam/408quiz/{year}/_index.md`：

```yaml
type: exam
layout: year-detail
year: 2009
```

### 模板：`layouts/exam/year-detail.html`

组装逻辑（Hugo 端）：

```
1. 取 _index.md 的 year → $year
2. 扫描所有 content/question/ 下的页面
3. 筛选 .Params.years 包含 $year 的页面
4. 按 .Params.number 升序排序
5. 按科目分组（数据结构→组成原理→操作系统→计算机网络）
6. 每组输出：
   <h2 class="exam-section-title">科目名（共 N 题）</h2>
   <div class="question-block">
     <div class="q-number">第 N 题</div>
     <div class="q-body">{{ .Content }}</div>
     <div class="question-actions">
       <button class="reveal-btn">查看答案与解析</button>
       <button class="favorite-btn">⭐ 收藏</button>
     </div>
   </div>
```

### 浏览器端 JS 处理

页面加载后，内联脚本执行 4 步 DOM 转换：

| 步骤 | 查找 | 替换为 |
|------|------|--------|
| 1. 隐藏标记 | `<p>[tag_link]</p>` | `display: none` |
| 2. 折叠答案 | `正确答案：[A-D]` | `.answer-panel`（初始隐藏），将后续兄弟节点（blockquote 解析）移入 |
| 3. 转换选项 | `<p>A. 文本</p>` | `<div class="exam-option">`（可点击选中） |
| 4. 解析标题 | `【解析】` 文本 | `<div class="analysis-title">解析：</div>` |

综合题无 `正确答案` 模式时，以最后一个 `[tag_link]` 为界，其后内容整体移入 `.answer-panel`。

### 按钮行为

- **每题"查看答案与解析"**：切换该题 `.answer-panel`，显示时标注正确（绿色）和选错（红色）选项
- **⭐ 收藏**：写入 `localStorage`，键 `quiz_collections`（与收藏页共用同一 key）
- **全局"查看全部答案与解析"**：批量切换所有面板

## 单题页面

`layouts/question/single.html`，用于独立 URL 访问每题。

与年份页面的区别：

| 特性 | 年份页面 | 单题页面 |
|------|----------|----------|
| 题号显示 | `第 N 题`（科目标题下） | `第 N 题` + 标签栏（年份/难度/科目/知识点/题型） |
| 导航 | 页面内滚动 | 上一题/下一题链接 |
| 收藏 | 内联 `toggleCollect()` | `collect-quiz.js` 模块（IndexedDB） |
| 元数据 | `data-*` 属性 | `window.quizMeta` 全局变量 |

## 端到端数据流

```
content/question/*.md          ← 作者编写（Markdown + 前置元数据）
        ↓
Hugo 构建                      ← 解析前置元数据、渲染 Markdown、选择模板
        ↓
静态 HTML                      ← 含 .q-body（原始 HTML）+ .q-number + 按钮
        ↓
浏览器 JS                     ← 4 步 DOM 转换（折叠、选项、解析、交互）
        ↓
可交互页面                     ← 点击选项、查看答案、收藏
```

## 相关文件

| 文件 | 作用 |
|------|------|
| `content/question/` | 1164+ 个单题 Markdown |
| `content/exam/408quiz/{year}/_index.md` | 年份页面激活器 |
| `layouts/exam/year-detail.html` | 年份页面模板（组题+渲染） |
| `layouts/question/single.html` | 单题页面模板 |
| `layouts/question/list.html` | 题库列表页 |
| `assets/js/collect-quit.js` | 单题收藏逻辑 |
