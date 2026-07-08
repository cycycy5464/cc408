# CC408 — Lessons Learned

## Hugo 0.135 特有行为

### 1. `relURL` 前导斜杠问题
- `"/docs/" | relURL` → `/docs/` ❌（不添加 baseURL 路径）
- `"docs/" | relURL` → `/cc408/docs/` ✅
- **规则**: 传给 `relURL` 时不要前导 `/`

### 2. Hugo 菜单 `.URL` 自动解析 baseURL
- 在 `menus.yaml` 中定义 `url: /docs/`
- 在模板中 `.URL` 返回的是 `/cc408/docs/`（已经包含 baseURL 路径）
- **不要**用 `eq .URL "/docs/"` 判断，而应该用 `eq .URL "/cc408/docs/"`
- **原因**: Hugo 在加载菜单配置时已经把 URL 用 baseURL 解析过了

### 3. 列表页范围过滤
- `{{ range where .Site.RegularPages "Section" "docs" }}` 会扫描整个 section
- 子页面（如 `/docs/data-structure/`）也会显示全部 docs 内容
- **修复**: 用 `.CurrentSection` 做范围判断：
  - 主入口页: `eq .CurrentSection .FirstSection`
  - 子页: 用 `.RegularPages` 获取当前 section 下的页面

### 4. 用 `else if` 链做互斥 section 匹配
- `hasPrefix` 做导航高亮时，`/exam/` 会匹配 `/exam/408quiz/`
- **修复**: 先检测 URL 前缀确定 `$section` 变量，再和每个菜单项做 `eq` 比较
- `else if` 保证各 section 互斥，不会出现多高亮

## 内容管理

### 5. 中文文件编码
- 中文命名的 `.md` 源文件用 PowerShell 复制时需用 `Copy-Item` 命令
- Python 处理时统一用 `encoding='utf-8'` 读写
- 避免使用 GBK 编码的字符串（如 `'✅'`）在 Python 中 print

### 6. 内容批量转换流程
1. PowerShell 复制源文件 → `_tmp/{subject}_source/`
2. Python 脚本批量添加 frontmatter + 修复图片路径 + 代码块转换
3. 单独复制 `.assets/` 图片到 `static/images/docs/{subject}/`
4. 清理旧冲突文件 → `git commit`

### 7. 导航栏双下划线根因
- 首页下划线始终存在: `hasPrefix` 会让 `/cc408/`（首页）匹配 `/cc408/docs/` 等高亮
- 真题+刷题同时高亮: `hasPrefix /cc408/exam/` 匹配 `/cc408/exam/408quiz/`
- **根因**: prefix 匹配无法区分父子路径
- **修复**: 用 `$section` 变量互斥匹配

## 项目结构

### 8. 独立项目 vs 子目录
- cc408 是独立 Hugo 项目（有自己的 `.git`），不是父项目的子目录
- commit 时要确认在正确的 git 仓库中操作
- 推送时区分父项目仓库（`cycycy5464.github.io`）和 cc408 仓库（`cc408`）

### 9. GitHub Actions 部署
- 工作流文件在 `.github/workflows/publish-cc408.yaml`
- 触发分支: `master`
- Hugo 0.135 需要 Go 环境（Ubuntu runner 自带）
- **注意**: `baseURL` 必须设为子路径 `/cc408/` 形式

### 10. 代码块转换陷阱（4-space indent）
- 源文件中的 4-space 缩进可能是列表项续行，不是代码块
- **区分标准**：行首 `* `、`- `、`1. ` 开头的不是代码；含 `{` `;` `#include` 的才是代码
- **转换**：先判断内容类型（代码 vs 散文 vs 列表），再决定是否包 ` ```c `
- 批量转换后需执行 `fix-codeblocks.py` 清理误包

### 11. 答案折叠设计
- 真题答案批量用 `<details><summary>查看答案</summary>` 包裹
- **正则策略**：用 `正确答案：` 行作为锚点，其后内容为折叠体
- 个体题目（choice/application/comprehensive）用 `## 答案`、`## 解析` 做锚点
- 避免在 regex replace 中使用 Python 的 `\U` emoji 转义

### 12. Python 文件处理注意事项
- 中文路径先用 PowerShell `Copy-Item` 复制到无中文名的临时目录
- 所有文件用 `encoding='utf-8'` 打开（默认 gbk 会 crash）
- `print()` 中文时避免用 emoji（gbk 编码限制）
- PowerShell 变量 `$_` 在 bash heredoc 中需用 `'` 包裹防转义

### 13. 知识图谱 O(n³) → O(n*k) 优化
- 三层嵌套循环 `range pages → range prerequisites → range pages` 
- **优化**: 先构建 `title → URL` 索引 (`merge dict`)，再用 `index $titleIdx .` O(1) 查找
- Hugo 模板中 `dict` + `merge` 可以实现哈希表效果

### 14. 代码审查优先级策略
- SSH 公钥等敏感文件即使 `.pub` 也要立即从 git 历史清除
- `goldmark.renderer.unsafe: true` 会增加 XSS 风险，推荐改为 false
- 用 JS 在模板层做折叠（前端行为）优于在 markdown 内容写 `<details>`（内容污染）
- 性能问题优先修 O(n²+) 嵌套循环，修完可带来量级提速

### 15. 用户内容保护规则
- **绝不覆盖用户手动修改的内容文件**。用户替换过 quiz 文件后，任何脚本都不应再次写入
- 如果用户说"不要再还原了"，立即停止对该目录的所有修改性操作
- 模板改动（`layouts/`）和内容改动（`content/`）要分开 commit，方便 revert 时隔离
- `git revert` 会撤销 commit 中所有文件的改动，包括非预期的。如果只想还原部分文件，用 `git checkout` 或 `git restore`

### 16. 考试内容目录结构
- csgraduates 使用 `2024/content.md` 目录结构
- Hugo 的 section 页面需要 `_index.md`，不能是 `content.md`
- 扁平文件 `2024.md` 和目录 `2024/content.md` 不能共存，Hugo 会创建两个页面
- 从 csgraduates 迁移后记得重命名 `content.md` 为 `_index.md`

### 17. Hugo section 页文件名必须是 _index.md
- `content/exam/408quiz/content.md` → Hugo 不识别为 section 页
- `content/exam/408quiz/_index.md` → 正确，会生成 `/exam/408quiz/` 页面
- 其他特殊 Hugo 文件名：`_index.md`（section）、`index.md`（单页 bundle）

### 18. 内容操作铁律
- **只删指定行**：用精确正则匹配目标行，不要全局替换
- **操作前确认文件路径**：目录结构变了（flat .md → dir/content.md）后，旧路径的操作会失效
- **git add 前检查 diff**：`git diff --cached` 确认只有预期改动
- _index.md 等关键文件修改后要立即检查内容完整性
- 用户明确说了"其他不准动"，那就只改用户指定的内容行，用 `re.sub` 精确匹配行首模式

### 19. Hugo type 决定模板选择
- `type: exam_collection` → Hugo 查找 `layouts/exam_collection/single.html`
- `type: exam` → Hugo 查找 `layouts/exam/single.html`
- 用户自定义 type 需要对应创建模板文件，否则回退到 `_default/`
- `layout` 参数在 frontmatter 中指定的是**模板文件名**，不是路径。`layout: exam` 会找 `layouts/xxx/exam.html`

### 20. Hugo 页面路径与 section 传播
- `content/exam/408quiz/2009/content.md` → section 是 `408quiz`（因为 `_index.md` 在 408quiz 目录）
- section 不会向父级传播，`exam/single.html` 不会默认影响 408quiz 下的页面
- 解决方法：设 `type: exam` 让 Hugo 使用 exam 类型的模板

### 21. 模板文件必须单独处理
- 内容文件（`content/`）和模板文件（`layouts/`）应该分开 git add/commit
- `git add -A` 会同时添加内容和模板的改动，revert 时无法隔离
- 用户手动修改过的内容，永远不应该被工具自动覆盖

### 22. `[tag_link]` 标记处理
- `[tag_link]` 是源内容中的答案折叠标记，Hugo 渲染为 `<p>[tag_link]</p>` 文本
- **不在模板层面处理这个标记会导致用户看到原始文本**
- **修复方式**：在 JS 中检测 `[tag_link]` 并隐藏（`display: none`），同时作为大题答案折叠的锚点
- 其他年份（2010-2026）没有此标记，只有 2009 年存在

### 23. `<button>` 元素默认颜色问题
- `<button>` 元素不继承父元素的 `color`，而是使用浏览器默认的 `ButtonText`（通常为黑色）
- 在深色主题下必须显式设置 `color` 属性
- **规则**：所有自定义 `<button>` 都必须设置 `color: var(--text-primary)`

### 24. Hugo `<script type="application/json">` 的转义陷阱
- `{{ $data | jsonify | safeJS }}` 在 `<script>` 标签中会被双重转义
  - `jsonify` 返回 JSON 字符串 → `safeJS` 标记为安全 JS → Hugo 在 script 上下文中包裹引号
  - 输出: `>`**"**`{...}`（多了一层引号包裹，JSON.parse 会解析成字符串而非对象）
- **修复**: 改用 `<div style="display:none">{{ $data | jsonify }}</div>`
  - HTML 上下文中 `&#34;`（引号的 HTML 实体）被 `textContent` 自动解码回 `"`
  - `JSON.parse(div.textContent)` 得到正确的对象

### 25. Hugo 模板作用域与 Scratch（Hugo 0.135）
- Hugo v0.135 下 `newScratch` 和 `$s.Get/Set` 可能触发解析错误：
  ```
  parse failed: undefined variable "$nodes"
  ```
  即使 `$s` 已定义且 `$nodes` 在代码后面才赋值，仍可能报错。
- **修复**: 改用直接变量赋值，避开 Scratch API：
  ```go
  {{ $nodes := slice }}
  {{ range ... }}
    {{ $nodes = $nodes | append ... }}
  {{ end }}
  ```
  这种写法在 Hugo 0.135 下可用。
- **注意**: `range` 内修改外层变量用 `=`（赋值）而非 `:=`（声明+赋值）
- 如果直接赋值仍然报错，尝试在 `range` 外层先声明一个空 `slice` 再赋值

## 内容管理

### 26. Junction 连接 Obsidian Vault 和 Hugo 项目
- `mklink /J vault/cc408-content/ hugo-project/content/`
- 实现实时双向同步，零拷贝
- 需要排除 `_index.md`（Hugo 专属节页面）→ `userIgnoreFilters: ["_index.md"]`
- 旧备份移出 vault 避免 Obsidian 索引（`D:\_archived_...\`）

### 27. Obsidian 书签配置文件
- 路径: `.obsidian/bookmarks.json`
- 格式:
  ```json
  {
    "items": [
      { "type": "folder", "title": "📖 408考研", "path": "cc408-content" }
    ]
  }
  ```

## 内容操作

### 28. 批量修改 frontmatter 的注意事项
- **sed 分隔符冲突**: 标题含 `/`（如 `总线和I/O系统`）→ 用 `s|pat|rep|` 替代 `s/pat/rep/`
- **PowerShell `-join` 优先级**: `"a" + (array) -join ","` 中 `+` 先执行，数组被转成空格字符串
  - 正确: `'"prefix ["' + ($titles -join '", "') + '"]'`
- **PowerShell IFS 陷阱**: `IFS='||'` 等价于 `IFS='|'`（IFS 是单字符集合）
  - `A||B` 按 `|` 拆分得 `A, '', B`，中间出现空元素
  - **修复**: 用单字符 `|` 作为分隔符

### 29. 知识图谱 prerequisites 填充策略
- 按章节顺序自动推断: chN 依赖 ch(N-1)
- ch00 无前置知识，跳过
- 每篇笔记的 frontmatter 自动更新 `prerequisites: ["前一章title1", "前一章title2"]`
- 112 节点 + 451 连线，完全自动生成

### 30. SCSS `@import` 含 `.css` 后缀不会内联
- `@import "exam.css"` 在 Sass 中生成原生 CSS `@import url(exam.css)`，不会内联
- 浏览器单独请求该文件，导致 404（文件不在 standalone 路径）
- **修复**: 重命名为 `_exam.scss`，导入改为 `@import "exam"`（无后缀）
- Sass 自动解析 `_exam.scss` 为 SCSS 部分文件并内联

### 31. 文件截断导致 SCSS 编译错误
- `assets/css/exam.css` 文件末尾被截断，`border: 1px solid v` 后缺失内容
- 之前因为 `@import "exam.css"` 生成原生 CSS `@import`，SCSS 处理器未解析，所以未报错
- 改为内联后，SCSS 处理器尝试解析截断的 CSS → 编译报错
- **修复**: 补全截断的 CSS 规则
### 32. `static/` vs `assets/` JS 冲突导致模板引用旧版本
- Hugo 中 `static/` 下的文件直接复制到 `public/`，`assets/` 下的文件需经 Hugo 管线处理
- `{{ "js/xxx.js" | relURL }}` 解析的是 **`static/js/xxx.js`**，不是 `assets/js/xxx.js`
- 当两边各有一个同名 JS 文件时，`assets/` 的更新不会被模板感知
- **根因**: 知识图谱 JS 从 `<script>` 标签改为 `<div>` 读取数据，但更新在 `assets/` 中，而模板引用的是 `static/` 旧版本
- **修复**: 确认模板引用的具体路径，确保更新正确的文件

### 33. 题目拆分脚本的关键边界处理
- 源 content.md 中存在两种题目编号格式：`##### N`（标准 markdown header）和 `N. (N分)`（内联格式，含转义反斜杠）
- 综合题（41-47）的科目按题号范围强制覆盖：41-42=DS, 43-44=CO, 45-46=OS, 47=CN
- 源文件中 `#### 科目` 标题可能缺失或内联在文本中（如 "组成原理 43"），需用题号范围兜底
- **修复**: 同时支持两种编号格式 + 大题科目按范围覆盖

### 34. 标签数据的科目名称不一致
- `tags_data.json` 和 `tags_pro_data.json` 中科目 key 使用简称「组成原理」而非全称「计算机组成原理」
- 前端 JS 中使用的是全称做索引，导致该科目卡片和标签数据为空
- **修复**: 统一使用源数据的 key 名称，用 `SUBJECT_FULL_NAMES` 映射表做显示转换

### 35. Chart.js 大规模数据渲染
- 247 个水平条形图需要足够的高度（64px/项 × 247 ≈ 15,800px）和 scroll 容器
- 条形图中 `barThickness` 必须设为固定值，否则 Chart.js 自动压缩
- 显示数据表格（表格在前）作为图表的文字替代，支持滚动和点击跳转
- **交互**: 点击图表柱或表格行 → 跳转到 `/knowledge_points/<标签名>/`

### 32. `static/` vs `assets/` JS 冲突导致模板引用旧版本
- Hugo 中 `static/` 下的文件直接复制到 `public/`，`assets/` 下的文件需经 Hugo 管线处理
- `{{ "js/xxx.js" | relURL }}` 解析的是 **`static/js/xxx.js`**，不是 `assets/js/xxx.js`
- 当两边各有一个同名 JS 文件时，`assets/` 的更新不会被模板感知
- **根因**: 知识图谱 JS 从 `<script>` 标签改为 `<div>` 读取数据，但更新在 `assets/` 中，而模板引用的是 `static/` 旧版本
- **修复方案**: 
  - 方案A: 更新 `static/` 中的对应文件（简单直接）
  - 方案B: 模板改用 Hugo 资产管线：`{{ $js := resources.Get "js/xxx.js" }} → {{ $js.RelPermalink }}`
- **规则**: 模板引用的 JS/CSS 文件，先确认它来自 `static/` 还是 `assets/`

### 36. GitHub Actions Node.js 版本迁移
- 当 Actions runner 警告 `target Node.js 20 but running on Node.js 24`，需升级 Action 的 major version
- `actions/checkout@v4` → `@v5`（2025 年 9 月起 Node.js 20 废弃）
- `actions/configure-pages@v5` → `@v6`
- `actions/upload-pages-artifact@v3` → `@v4`
- `actions/deploy-pages@v4` → `@v5`
- **规则**: `git push` 后检查 Actions 运行日志，看到 deprecation warning 就升级对应 action
- **无需改业务代码**，只改 workflow 文件的 `uses:` 行版本号

### 37. IndexedDB → localStorage 迁移原因
- `IDBObjectStore.createIndex()` 返回 `IDBIndex`，**没有** `createIndex` 方法（`IDBIndex` 不可再创索引）
- `tagIdx.createIndex("subject", "subject")` 在第 2 次数据库打开时（`onupgradeneeded` 不触发）不会报错，但首次创建时抛 `TypeError`，导致数据库创建失败
- **修复**: 改用 `localStorage`（同步 API，零版本冲突，两脚本共用同一 key `quiz_collections`）
- **教训**: IndexedDB 的 `onupgradeneeded` 中任何 JS 错误都会导致数据库创建中止且不易调试
- 如果必须用 IndexedDB，schema 变更需递增版本号，且 `createIndex` 必须在 store 上调用，不能在已返回的 index 上调用
