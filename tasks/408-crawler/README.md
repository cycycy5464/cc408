# 408真题答案解析爬虫

## 任务清单

- [x] 分析 csgraduates.com 页面结构（meta description 答案速对 + 折叠解析区域）
- [x] 编写 Node.js 爬虫程序 `crawler.js`
- [x] 爬取所有年份（2009-2026）的答案和解析数据
- [x] 编写填充脚本 `filler.js`，将数据填充到各年份 md 文件
- [x] 保存页面结构、爬虫程序到任务文件夹

## 爬虫工作原理

### 页面结构分析

csgraduates.com 的 408 真题页面结构：

1. **选择题（Q1-40）**
   - 答案速对表 → 在 `<meta name=description>` 中直接嵌入
   - 正确答案 → 在 `<span class=correct-answer-text>` 中
   - 解析内容 → 在 `<div id="explanation-choice-XXXXX-N">` 中（默认隐藏）

2. **综合应用题（Q41-47）**
   - 解析内容 → 在 `<div class="solution-detail" id="solution-answer-XXXXX-N">` 中（默认隐藏，含 SVG 配图）

### 爬虫流程

```
crawler.js:
  fetch(url) → 解析HTML
    ├─ meta[name=description] → 选择题答案速对(40题)
    ├─ explanation-choice divs → 选择题解析(含答案)
    └─ solution-answer divs → 综合题解析(7题)
  ↓ 保存到 JSON
crawled_data/{year}.json

filler.js:
  读取 {year}.json + {year}.md
  → 逐行扫描，按题号识别
  → 填充 正确答案：、解析内容、答案内容
  ↓
  更新 {year}.md
```

## 爬取结果

| 项目 | 数量 |
|------|------|
| 成功爬取 | 18/18 年（2009-2026） |
| 选择题答案 | 40 题/年（2026 年无答案速对，但解析已提取） |
| 选择题解析 | 平均 39.5 题/年（部分年份 Q40 无解析） |
| 综合题解析 | 7 题/年 ✅ |
| 已填充文件 | 16 个 md 文件（2009 已于测试时填充，2026 文件不存在） |

### 已知限制
- 源站 2010、2012-2018、2021 年的 Q40 未提供解析，无法填充
- 综合题中的 SVG 图片被替换为 `[图片]` 标记，需手动补充

## 程序文件

| 文件 | 说明 |
|------|------|
| `crawler.js` | 爬虫主程序 |
| `filler.js` | 数据填充脚本 |
| `page.html` | 2009 年页面 HTML 结构参考 |
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
