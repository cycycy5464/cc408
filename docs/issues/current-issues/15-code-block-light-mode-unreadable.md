# 问题 15：浅色模式下 ```c 等代码块看不清

**等级**：🟠 中危
**范围**：所有语言代码块（```c / ```cpp / ```python … 均受影响）
**日期**：2026-07-16

---

## 用户现象

> 浅色模式下 ```c 包裹的代码看不清楚。

深色模式正常，浅色模式代码块文字（尤其未着色的标识符、标点）几乎不可见。

---

## 根因

Hugo 的代码高亮（`markup.highlight`）此前使用默认 **monokai** 样式，且 `noClasses` 为 `true`。

注意 Hugo 的语义（易混淆）：

- `noClasses: true` → **使用行内样式**（每个 token 带 `style="color:#..."`，`<pre>` 带 `background-color:#272822`）。
- `noClasses: false` → 输出 `.chroma` / `.chroma .k` 等 **class**，配色由 CSS 控制。

旧配置 `noClasses: true` 导致生成的代码块带**行内硬色调**：

```html
<div class="highlight"><pre tabindex="0" style="color:#f8f8f2;background-color:#272822;...">
```

关键链条：

1. 行内 `background-color:#272822` 强制代码块背景为**深色**（深浅模式都暗，因行内样式优先级高于样式表）。
2. `assets/css/custom.scss` 中 `pre code { color: var(--text-primary) }`：浅色模式下 `--text-primary` 为深色（`#1f2a38`）。
3. 代码里**未被语法着色的部分**（C 的变量名、函数名、标点等）继承 `var(--text-primary)` → 浅色模式 = 深色文字，叠在强制深色背景 `#272822` 上 → **看不见**；而已有 monokai 浅色 token 在暗底上反而能看，造成“浅色模式看不清”的错觉。
4. 深色模式：`--text-primary` 为浅色 `#e2e8f0`，叠在暗底上正常 → 因此只有浅色模式出问题。

结论：根因是 Hugo 高亮输出**行内 monokai 硬色调**，与站点双主题机制冲突，而非某语言特有。

> 排查踩坑：首次把 `noClasses` 语义理解反了（以为 `true`=用 class），导致一度改错方向；经 `hugo config` 确认生效值 `noclasses = true`（行内）后纠正为 `false`。

---

## 修复方案

### 1. `config/_default/hugo.yaml` 与 `config/local.yaml`：`noClasses: false`

```yaml
markup:
  _merge: deep
  highlight:
    lineNos: false
    noClasses: false   # 输出 .chroma class（非行内样式），配色由 CSS 控制以适配双主题
```

改为 `false` 后，Hugo 输出 `<pre class="chroma">` 与 `<span class="k">` 等 class，不再注入行内色；且本主题未引入 Hugo 自动注入的 chroma 样式表，配色完全由下方 CSS 决定。

### 2. 新增 `assets/css/_chroma.scss`：双主题 `.chroma` 配色

- 容器 `.highlight pre` 背景用 `var(--code-bg)`（深浅主题各自的 `--code-bg` 已在 `:root` / `:root[data-theme="light"]` 定义），消除强制暗底。
- 深色（默认 `:root`）采用 monokai 调色；浅色（`:root[data-theme="light"]`）采用 github 调色。
- 各 token 类（`.k` 关键字、`.s` 字符串、`.m` 数字、`.c` 注释、`.nf` 函数名等）按主题分别上色，保证浅色模式下深色背景上全部清晰可读。
- 规则用 `:root` / `:root[data-theme="light"]` 前缀提升特异性，确保覆盖任何潜在的 Hugo 默认样式。

### 3. `assets/css/custom.scss`：引入新文件

```scss
@import "exam";
@import "quiz-collection";
@import "chroma";
```

---

## 验证

- `hugo --gc` 构建成功（站点较大，构建约 5 分钟；因改动 `markup.highlight` 配置，需清除 `resources/` 与 `public/` 缓存后重建，否则页面渲染缓存会复用旧的行内产物）。
- 生成页面代码块：`<pre class="chroma">`、token 为 `<span class="k">` 等 class，**不再含 `background-color:#272822` 行内色**；Hugo 也未注入竞争的 `.chroma` 样式表。
- 编译后 `public/css/custom.min.*.css` 含 103 处 `.chroma` 规则，含浅色块与 `.highlight pre` 覆盖。
- 浅色模式：代码块背景为浅色（`--code-bg`），文字与语法色均为深色系，可读。
- 深色模式：保持 monokai 风格，正常。

### 用户侧复测

强制刷新（Ctrl+F5）后，切换到浅色模式，打开任一含 ```c 的题目页（如 `2026-ds-041`），
确认代码块背景为浅色、关键字/字符串/注释/标识符均清晰可辨。

*状态：✅ 已修复*
