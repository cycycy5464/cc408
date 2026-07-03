# 修复 2009 真题页面渲染问题

## 任务清单

- [x] Fix `[tag_link]` displayed as raw text in 2009 exam page
- [x] Fix favorite button text color invisible on dark theme

## 变更总结

### 文件：`layouts/exam/single.html`

#### Fix 1: `[tag_link]` 显示为原始文本 + 大题答案折叠

**问题根因**：`content/exam/408quiz/2009/content.md` 中有 54 处 `[tag_link]` 标记，该标记是原始来源用于分隔题目与答案的标记。Hugo 将其渲染为 `<p>[tag_link]</p>`，但前端的 JS 没有处理该文本节点，导致用户可以看到 `[tag_link]` 文字。同时，大题（41-47题）的答案折叠因找不到分界标记而失效（"解析没隐藏"）。

**修改方式**（两处改动，均在 DOM 操作之前处理）：

1. **第一遍重组时隐藏**（`else` 分支开头）：在将内容分组到各 question-block 时，遇到 `<p>[tag_link]</p>` 立即 `style.display = 'none'`。这比原先的"后处理清理"更安全，避免了与 `querySelectorAll` 在 DOM 重构后的冲突。

2. **大题折叠检测**（`if (!answerEl)` 循环内）：在大题答案折叠逻辑中，增加对隐藏的 `<p>[tag_link]</p>` 检测。检测到后作为答案内容的折叠起点。

**关键区别**：第一次实现用了后处理 `container.querySelectorAll('p')` 遍历，与 `<div>` 在 `<p>` 内引起的 DOM 重构冲突，导致选择题选项消失。这次改为**在重组阶段就隐藏标记**，不影响后续选项转换逻辑。

#### Fix 2: 收藏按钮字体颜色

**问题根因**：`.favorite-btn` 没有设置 `color` 属性，导致使用浏览器默认的 `ButtonText`（通常是黑色）。在深色主题背景下，黑色文字不可见。

**修改方式**（第 68-77 行）：
- 添加 `color: var(--text-primary)` 确保默认状态下文字可见（浅灰色）
- 添加 `:hover` 状态：文字颜色变为主色调 `var(--accent)`
- 添加 `.active` 状态：收藏后的文字为金色 `#f0c040`

## Lesson Learned

- **后处理遍历 DOM 有风险**：`querySelectorAll('p')` 在 DOM 被 JS 修改后（如 `<div>` in `<p>` 重构）可能产生不可预期结果
- **正确的做法**：在第一次重组阶段（DOM 尚未被修改）就隐藏标记元素
- 隐藏标记后保留在 DOM 中，仍可作为其他逻辑的索引锚点

## Review

- ✅ Hugo build 通过（332 pages, no errors）
- `[tag_link]` 只在 2009/content.md 中存在，不影响其他年份
- 收藏按钮现在有明确的颜色设置，不会受浏览器默认值影响
- 下一次回退 `[tag_link]` 改动时，记得连带回退 lessons.md 中的 lesson 22
