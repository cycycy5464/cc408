# 408真题答案解析爬虫 (题干+选项增强版)

## 任务清单

- [x] 分析 csgraduates.com 页面结构（meta description 答案速对 + 折叠解析区域）
- [x] 编写 Node.js 爬虫程序 `crawler.js`
- [x] 爬取所有年份（2009-2026）的答案、解析、题干和选项数据
- [x] 编写填充脚本 `filler.js`，将数据填充到各年份 md 文件
- [x] 保存页面结构、爬虫程序到任务文件夹

## JSON 数据结构

每个年份的 JSON 文件包含以下字段：

```json
{
  "year": 2009,
  "url": "https://...",
  "answers": { "1": "B", "2": "C", ... },
  "questions": {
    "1": {
      "stem": "题干文本...",
      "options": { "A": "选项A", "B": "选项B", "C": "选项C", "D": "选项D" }
    },
    "41": {
      "stem": "综合题题干...",
      "options": {}
    }
  },
  "explanations": {
    "1": { "answer": "B", "analysis": "解析文本..." }
  },
  "solutions": {
    "1": "综合题解答文本...",
    ...
  }
}
```

| 字段 | 说明 |
|------|------|
| `answers` | 选择题答案速对，key=题号，value=选项字母 |
| `questions.*.stem` | 题干文本 |
| `questions.*.options` | 选择题选项（A-D），综合题为空对象 |
| `explanations.*.analysis` | 选择题解析 |
| `solutions.*` | 综合题解答/答案 |

## 爬虫工作原理

### 页面结构分析

csgraduates.com 的 408 真题页面结构：

1. **选择题（Q1-40）**
   - 答案速对表 → 在 `<meta name=description>` 中直接嵌入
   - 题干 → `<h5 id=N>` 之后的第一个 `<p>`
   - 选项 → `<span class=choice-label>A.</span> <span class=choice-text>文本</span>`
   - 正确答案 → 在 `<span class=correct-answer-text>` 中
   - 解析内容 → 在 `<div id="explanation-choice-XXXXX-N">` 中（默认隐藏）

2. **综合应用题（Q41-47）**
   - 题干 → `<h5 id=N>` 之后的多个 `<p>`，直到 `.answer-container`
   - 解析内容 → 在 `<div class="solution-detail" id="solution-answer-XXXXX-N">` 中（默认隐藏，含 SVG 配图）

### 爬虫流程

```
crawler.js:
  fetch(url) → 解析HTML
    ├─ meta[name=description] → 选择题答案速对(40题)
    ├─ h5 + p + choice-container → 题干 + 选项(47题)
    ├─ explanation-choice divs → 选择题解析(含答案)
    └─ solution-answer divs → 综合题解析(7题)
  ↓ 保存到 JSON
crawled_data/{year}.json
```

## 爬取结果

| 项目 | 数量 |
|------|------|
| 成功爬取 | 18/18 年（2009-2026） |
| 选择题答案 | 40 题/年（2026 年无答案速对，但解析已提取） |
| 题干 | 47 题/年 ✅ |
| 选择题选项 | 平均 39.8 题/年 |
| 选择题解析 | 平均 39.5 题/年（部分年份 Q40 无解析） |
| 综合题解析 | 7 题/年 ✅ |

### 已知限制
- 源站 2010、2012-2018、2021 年的 Q40 未提供解析，无法填充
- 综合题中的 SVG 图片被替换为 `[图片]` 标记，需手动补充
- 极少数选择题的选项容器格式略有差异，可能导致该题选项缺失

## 程序文件

| 文件 | 说明 |
|------|------|
| `crawler.js` | 爬虫主程序（提取答案、解析、题干、选项） |
| `filler.js` | 数据填充脚本 |
| `page_structure.html` | 2009 年页面 HTML 结构参考 |
| `crawled_data/` | 各年份结构化数据 JSON |

### 命令行用法

```bash
# 爬取指定年份
node crawler.js              # 所有年份
node crawler.js 2024         # 单年
node crawler.js 2010 2020    # 范围

# 填充到 Markdown
node filler.js               # 所有年份
node filler.js 2024          # 单年
node filler.js 2010 2020     # 范围
```
