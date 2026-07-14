# CC408 前端 UI/UX 审计报告

> 审查方法：[ui-ux-pro-max] 四维框架（设计系统 / UX 流程 / UI 概念与布局 / 实现与无障碍）
> 审查对象：CC408 Hugo 静态站点前端（`assets/css/*`、`assets/js/*`、`layouts/*`、`config/_default/params.yaml`）
> 审查日期：2026-07-14
> 配套旧报告：`docs/frontend-issues-report.md`（本报告在其基础上用四维框架重新组织，并去除已修复项）

---

## 0. 本次会话已交付的改动

| 改动 | 文件 | 说明 |
|------|------|------|
| ✅ 主题切换按钮 | `layouts/partials/navbar.html`、`layouts/_default/baseof.html`、`assets/js/theme-toggle.js`、`assets/css/custom.scss` | 导航栏新增 🌙/☀ 切换按钮；`<html data-theme>` 驱动深色/浅色双 token 体系；`localStorage` 持久化 + `prefers-color-scheme` 自动初始；`<head>` 内联脚本防闪烁（FOUC）。已 `hugo --minify` 构建通过。 |
| ✅ 真题页浅色孤岛修复 | `assets/css/custom.scss` | 在 `:root` 中集中定义 `exam.css` 缺失的 11 个变量（`--primary/--border/--code-bg/--table-header-bg/...`），并补 `:root[data-theme="light"]` 浅色取值，真题页在两种主题下均正确渲染。 |

---

## 1. 四维问题清单

### 维度一：设计系统（Design System）

#### D1-P0｜真题页「浅色孤岛」—— 变量未接入设计系统
- **严重度**：P0（视觉断裂，影响所有真题页可读性）
- **影响**：在整体深色站点（`--bg-primary:#0a0e14`）中，真题内容区出现成片浅色块（代码块 `#f6f8fa`、表头 `#f0f4fa`、奇数列 `#fafbfd`、知识点标签 `#eef3fb`），风格割裂、对比刺眼。
- **证据**：
  - `assets/css/exam.css` 使用 `var(--primary,#1a72c4)`、`var(--border,#e0e6ef)`、`var(--code-bg,#f6f8fa)`、`var(--table-header-bg,#f0f4fa)`、`var(--table-row-alt,#fafbfd)`、`var(--tag-bg,#eef3fb)`、`var(--tag-border,#c8d8f0)`、`var(--code-inline-bg,#f0f3f8)`、`var(--answer-color,#d7322a)`、`var(--text-primary,#1f2a38)` 等——这些变量**均未在深色设计系统中定义**，一律回退到浅色 hardcode 值。
  - `assets/css/custom.scss:5-38` 的 `:root` 缺少上述变量（仅 `--text-primary/--text-muted/--border-color` 等部分存在）。
- **状态**：✅ 已在本会话修复（见 §0）。

#### D1-P1｜科目配色双来源——JS 与 SCSS token 漂移
- **严重度**：P1（同一科目全站颜色不一致）
- **影响**：知识图谱节点/辉光/信息面板标题用一组颜色，首页 hero 卡片图标用另一组，同一科目在不同位置显示不同色。
- **证据**：
  - `assets/js/knowledge-graph.js:10-16` 硬编码 `data-structure:#58d6c0 / computer-org:#f59e0b / os:#8b5cf6 / network:#3b82f6 / exam:#f0c040`。
  - `assets/css/custom.scss:13-16` 定义 `--color-ds:#39bae6 / --color-co:#ff8f40 / --color-os:#a277ff / --color-cn:#95e6cb`。
  - 四科**全部不一致**，且键名体系不同（`data-structure` vs `ds`）。

### 维度二：UX 流程（UX Flow）

#### D2-P0｜资源筛选器完全失效——选择器与模板不匹配
- **严重度**：P0（核心功能不可用）
- **影响**：资源下载页的「搜索 / 科目 / 难度」筛选无任何效果，用户无法过滤资源。
- **证据**：
  - `assets/js/resource-filter.js:4-6,18,27-29` 依赖 `#filter-search`、`#filter-subject`、`#filter-difficulty` 与 `.card-glass[data-subject]`。
  - `layouts/resources/list.html:6-12` 实际只渲染 `<div class="card">`，**无 `card-glass`、无 `data-subject`/`data-difficulty`、无上述三个 id**。
  - 全仓搜索 `card-glass` = **0 匹配**；`if (!searchInput||!subjectSelect||!difficultySelect) return;`（第 7 行）因元素缺失直接 return，事件绑定永不执行。
  - 注：真正带 `data-subject` 的卡片在 `layouts/question/list.html:35`，但那是题库页，与 `resource-filter.js` 无关。

#### D2-P1｜两套 Toast 实现风格不统一
- **严重度**：P1（维护与体验不一致）
- **影响**：收藏提示与题集提示的样式来源、配色、动画各不相同；`collect-quiz.js` 缺 error 态红色。
- **证据**：
  - `assets/js/collect-quiz.js:146-158` 用 `el.style.cssText` **内联**硬编码样式（success `#2ecc71`、info `#39bae6`），仅 opacity 淡出，无 error 态。
  - `assets/js/quiz-collection.js:466-478` 用 CSS 类 `.qc-notification`，样式在 `assets/css/_quiz-collection.scss:447-472`，含 `@keyframes qc-notify-in` 滑入与 `.error{background:#e74c3c}`。

### 维度三：UI 概念与布局（UI Concept / Layout）

#### D3-P1｜缺少明暗主题选项（已由本次会话补齐）
- **严重度**：P1（降低了不同环境/偏好的可用性）→ ✅ 已通过主题切换按钮解决
- **证据**：`config/_default/params.yaml:5-7` `appearance.mode: dark`、`show_theme_chooser: false`；assets 全目录搜索 `prefers-color-scheme|prefers-reduced-motion|data-theme|theme-toggle` = 0 匹配（修复前）。

#### D3-P2｜图谱信息面板固定定位可能遮挡内容
- **严重度**：P2（窄屏/小窗体验）
- **影响**：`assets/css/custom.scss:204` `.info-panel{position:fixed;right:1.5rem;top:90px;width:280px}` 在中小屏可能遮挡图谱；移动端虽有 `left:1rem;right:1rem` 覆盖（第 248 行），但桌面中等宽度（769–1100px）仍易遮挡。
- **改进**：面板支持拖拽/折叠，或仅在选中节点时显示并提供关闭后「不自动再弹」的记忆开关。

### 维度四：实现与无障碍（Implementation & Accessibility）

#### D4-P1｜自定义控件缺 ARIA 角色与键盘可达性
- **严重度**：P1（键盘/读屏用户受阻）
- **影响**：刷题选项、图谱分页 Tab 纯靠鼠标，键盘与辅助技术不可达或无状态语义。
- **证据**：
  - `exam-option`（选择题选项）：`quiz-collection.js:271` 创建、`342-346` 仅绑定 `click`——无 `role`/`aria-checked`/`tabindex`/键盘事件，是 `div`。
  - `graph-tab`（图谱分页）：`knowledge-graph.js:1136-1143` 绑定 `click`；`assets/css/custom.scss:214` 为普通 `div`——无 `role="tab"`/`aria-selected`/键盘。
  - `reveal-btn`：`quiz-collection.js:302,320-325` 切换文字；`custom.scss:151`——`<button>` 可聚焦但缺 `aria-expanded`。
  - `qc-mode-btn`/`filter`/`view-btn`：`quiz-collection.js:100-102,180-186,209-214`、`knowledge-graph.js:1146-1157`——`<button>` 可聚焦但缺 `aria-pressed`。
  - （正面）navbar/footer 已用语义 role（`role=navigation/menubar/menuitem/contentinfo`）。

#### D4-P1｜动效无 `prefers-reduced-motion` 守卫
- **严重度**：P1（前庭功能障碍/敏感用户不适）
- **影响**：卡片 hover 位移、`.qc-notify-in` 滑入、`.hero-card-icon` 缩放等动画对所有用户强制播放。
- **证据**：assets 全目录搜索 `prefers-reduced-motion` = 0 匹配；涉及 `custom.scss:79`(`.card:hover{transform:translateY(-2px)}`)、`assets/css/_quiz-collection.scss:474`(`@keyframes qc-notify-in`)。

#### D4-P2｜JS 无障碍属性系统性缺失
- **严重度**：P2
- **影响**：`assets/js` 中除 `kpAddInput` 的回车添加（第 1184 行）外，无任何 `role/aria-label/tabindex/键盘事件` 管理，建议建立统一的「自定义控件无障碍规范」。

---

## 2. 分级改进方案（P0 / P1 / P2）

### P0（必须修，阻断体验/功能）
| 编号 | 方案 | 具体做法 | 验收标准 |
|------|------|----------|----------|
| D1-P0 | 真题页接入设计系统 | ✅ 已完成：`custom.scss` 集中定义 11 个 exam 变量 + 浅色取值 | 真题页在深/浅主题下代码块、表格、标签均为深色协调色，无刺眼浅块 |
| D2-P0 | 修复资源筛选器 | 二选一：① 改 `resource-filter.js` 选择器为 `.card[data-subject]` 并在 `layouts/resources/list.html` 卡片上补 `data-subject`/`data-difficulty` 与 `#filter-*` 控件；② 若资源页本不需要筛选，移除该 JS 引用避免死代码 | 在资源页用搜索框/科目下拉能实际过滤卡片；或确认不再加载该脚本且无控制台报错 |

### P1（重要，应尽早修）
| 编号 | 方案 | 具体做法 | 验收标准 |
|------|------|----------|----------|
| D1-P1 | 统一种目配色 | 在 `custom.scss` 增 `:root[data-theme="light"]` 下的 `--color-*`；`knowledge-graph.js` 改为读取 CSS 变量（`getComputedStyle(document.documentElement).getPropertyValue('--color-ds')`）或共享一份映射，弃用硬编码 hex | 同一科目在 hero 卡片与图谱节点颜色一致；改色只改一处 |
| D2-P1 | 统一 Toast | 删除 `collect-quiz.js` 内联样式，改用 `.qc-notification` 体系并补 `.error` 态 | 全站提示风格、配色、动画一致；含成功/信息/错误三态 |
| D3-P1 | 主题切换 | ✅ 已完成（navbar 按钮 + token + 持久化 + 系统偏好） | 点击按钮即时切换并刷新图标；刷新后保持；首次访问跟随系统 |
| D4-P1 | 控件无障碍 | `exam-option` 改 `role="radio"`+`aria-checked`+方向键导航，外层 `role="radiogroup"`；`graph-tab` 改 `role="tab"`+`aria-selected`+左右键；`reveal-btn` 加 `aria-expanded`；各 `aria-pressed` 状态按钮补 `aria-pressed` | 仅用键盘可完成刷题选项选择、图谱分页切换；读屏能播报当前选中态 |
| D4-P1 | reduced-motion 守卫 | `custom.scss` 增加 `@media (prefers-reduced-motion: reduce){ *{animation:none!important;transition:none!important} }`（保留必要 opacity 淡变） | 系统开启「减少动效」后，hover 位移/滑入动画停止，功能不受影响 |

### P2（优化，可排期）
| 编号 | 方案 | 具体做法 | 验收标准 |
|------|------|----------|----------|
| D3-P2 | 信息面板可收起/防遮挡 | 面板支持折叠记忆；桌面中宽屏避免遮挡图谱 | 关闭后不再自动弹出；中等宽度下不遮挡主图 |
| D4-P2 | 建立无障碍规范 | 在 `docs/` 记录自定义控件无障碍 checklist，PR 时校验 | 新增交互组件默认带 ARIA/键盘支持 |

---

## 3. 验收总表（Definition of Done）

- [x] **主题切换按钮**：导航栏可见、可点、图标随状态变化、刷新保持、首访跟随系统（已完成并构建通过）。
- [x] **真题页浅色孤岛**：11 个变量接入设计系统，深浅主题均协调（已完成）。
- [ ] **资源筛选器**：恢复实际过滤或移除死脚本。
- [ ] **科目配色**：JS 与 SCSS 单一来源，全站一致。
- [ ] **Toast 统一**：单一样式体系 + error 态。
- [ ] **控件无障碍**：选项/分页可键盘操作、状态可朗读。
- [ ] **reduced-motion**：系统偏好生效。

---

## 4. 优先级建议（给审核人）

1. **立即跟进项**：D2-P0 资源筛选器（功能失效，用户直接受影响）——建议确认是「修」还是「删」。
2. **本迭代收尾**：D1-P1（配色统一）、D4-P1（无障碍 + reduced-motion）——成本低、收益高。
3. **排期优化**：D3-P2、D4-P2。

> 注：D3-P1 主题切换与 D1-P0 真题页孤岛已在本会话实现，可直接进入审核/合并流程。
