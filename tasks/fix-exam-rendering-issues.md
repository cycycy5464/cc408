# 修复题目渲染问题 + 爬虫验证

## 已修复（本会话累计）

### A. 渲染/数据问题
- [x] SVG `<foreignObject>` 换 `<object>` 标签（`year-detail.html`）
- [x] SVG 白底 `background:#fff` 设置（262 个文件）
- [x] 2009-ds-010 内容污染（混入组成原理题）
- [x] 2009-ds-011 subject 错配 → 2009-co-011
- [x] 2009-co-013 选项 `__` 未闭合 + 格式清理
- [x] 2019-co-043 subject 错配(CO→OS, 哲学家就餐)
- [x] 12 个文件 `__` 选项标记修复
- [x] 选项解析 JS：只处理直接 `<p>` 子节点（防解析中 `B\C` 误识别为选项）— `year-detail.html` + `single.html`
- [x] 44 个 UTF-8 损坏文件经 csgraduates 源重新 split（14 年：2010-2013, 2015-2021, 2023-2025）
- [x] 658 个重新 split 文件补回 `[tag_link]`（脚本 `scripts/add_tag_link.py`）
- [x] 2009-co-022 内容污染（OS 题混入）清理
- [x] 2009-os-032 内容污染（网络题混入）+ 尾部 `---` 清理（曾误删后用 csgraduates 源重建）
- [x] 88 个文件尾部 `---` 横线批量清理
- [x] 2009-os-025 选项格式 `X 、`→`X\.` 独立行（只显示两选项的 bug）
- [x] 2009-os-027 题干与选项同行 → 题干被 JS 整体替换丢失；拆行 + 加 JS 安全网保留题干前缀

### B. 模板层加固（防复发）
- [x] 4 个模板选项正则允许字母与分隔符间空格：`([A-D])\s*[.、．]\s*`
  - `layouts/question/single.html`、`layouts/exam/year-detail.html`、`layouts/exam/single.html`、`layouts/exam/408quiz/year-detail.html`
- [x] `single.html` + `year-detail.html` 选项转换时保留题干前缀（`<p class="exam-stem-text">`），防整段替换丢题干

### C. 爬虫验证
- [x] 学习 `tasks/408-crawler/` 经验（Node `https.get` → 解析隐藏 div）
- [x] 爬取 `408quiz/2009/#43` 成功，输出 markdown 表格（`scripts/_tmp_q43.md`）
- [x] 复用脚本 `scripts/scrape_q43.js`（可改年份/题号爬任意单题）

## 待处理（已知限制）
- [ ] 解析区 `>` blockquote 格式在 csgraduates 源中丢失（次要，不影响功能）
- [ ] simulate 文件 UTF-8 损坏，无 csgraduates 源，需手动/备份修复
- [ ] csgraduates 源综合题 SVG 配图被替换为 `[图片]`（已知限制）
- [ ] 题干含 `A、B、C、D`（表名/操作步骤）的单行属选项解析误报，已用 JS 安全网保证不丢题干，但会渲染多余可点击项，需人工复核

## Review

**本次会话目标**：修复真题站点渲染异常 + 验证爬虫链路。

**根因归纳**：
1. 早期迁移/PowerShell `Set-Content` 写入导致 UTF-8 损坏、内容污染、subject 错配。
2. 选项解析 JS 用全局正则把整段 `<p>` 替换为选项，题干与选项同行时吞掉题干；且正则不允许字母与分隔符间空格。
3. 个别文件选项用 `X 、`（带空格顿号）格式，正则不匹配 → 选项不渲染。

**处理方式**：数据层先修根因（拆行/归一化格式/补标记），模板层加安全网（只扫直接 `<p>`、允许空格、保留题干前缀）防复发。

**验证**：
- 全库扫描确认仅 1 个文件有 `X 、` 格式、2 个 true contamination、88 个尾部 `---`，均已处理。
- 爬取 #43 成功，结果与 `content/question/2009-co-043.md` 一致，证明爬虫链路可靠。

**教训沉淀**：Lesson #51~#57 已记录（SVG foreignObject、UTF-8 污染、选项解析、内容污染、选项格式、题干丢失、单题爬取）。

**下一步建议**：simulate 文件损坏需另寻源；如要做整年答案速对 markdown 表，可基于 `crawled_data/{year}.json` 的 `answers` 生成。
