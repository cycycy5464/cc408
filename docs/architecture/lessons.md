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

## 模板与选项解析规则

### 10. `layouts/exam/year-detail.html` JS 解析依赖

**选项解析** (正则 `[A-D]\s*\.\s*`):
- 选项字母必须紧跟 `.`（句点）作为分隔符；**不能**用 `、`（顿号）或 `．`（全角句点）
- 选项文本内的 `、`（如 `USB、EISA`）或题干内的 `MB、` 会触发 `[A-D]\s*[.、．]` 误匹配，生成虚假选项按钮
- 修复：正则限定只匹配 `\.`，排除 `、` 和 `．`（2026-07-11 修复）
- 纯空格（如 `A   B   C   D`）不匹配，缺失分隔符时选项按钮不生成（如 Q3）
- 所有选项建议在同一段落（选项间无空行），便于正则一次解析全部 4 项
- 选项间有空行时 Goldmark 每项独立成 `<p>`，正则逐段只匹配单项，虽能工作但布局异常
- 选项必须与 `[tag_link]` 分析段落分离（中间至少空一行），否则 `findAnswer` 移除 `[tag_link]` 所在 `<p>` 时选项也被删除

**`findAnswer` 机制**:
- 搜索 `.q-body` 中含 `[tag_link]` 文本的节点，将其及后续兄弟节点移入答案面板
- `[tag_link]` 所在 `<p>` 中的全部内容（含选项文字）会被移除，因此选项必须与 `[tag_link]` 分离到不同 `<p>`
- 综合题（`question_type: "comprehensive"`）也依赖 `[tag_link]` 分离题干与解析，否则全部内容在 `.q-body` 中始终可见

### 11. Goldmark Markdown 表格与周围文本

- 表格后紧跟文本（无空行）时，Goldmark 将文本吸收为表格行
- 修复：表格与前后文本之间必须保留空行
- 若两个表格之间混有分析段落，每个表格/段落后都需空行

## SVG 文件编辑规范

### 9. SVG text 元素禁止重复属性
- `2010_Q4_2.svg` 中每个 `<text>` 有重复的 `font-size="16" fill="#000"`：`<text ... font-size="16" font-family="Helvetica,sans-serif" fill="#000" font-size="16" fill="#000">24</text>`
- 这是 **malformed XML**，不同解析器处理方式不同（取第一个或最后一个）
- **修复**: 只保留一组属性，删除重复
- **根因**: 可能经过多次 draw.io 导出或手动编辑，导致属性叠加

### 10. CSS 值不能被破坏
- `2010_Q3_1.svg` 和 `2010_Qx_3.svg` 中 `word-wrap: normal;` 被破坏为 `word-wrap: normal; mal; mal;`
- 浏览器虽忽略无效声明，但破坏的文件表明被有 bug 的工具处理过
- **修复**: 全局替换为正确的 `word-wrap: normal;`
- **根因**: 文件在某种有 bug 的导出/保存过程中被截断或重复了 `normal` 的前半部分

### 11. SVG 批量检查清单
修复 SVG 问题应检查:
1. 重复的 XML 属性（特别是 `font-size`、`fill`）
2. CSS 值是否完整、无垃圾字符
3. `<foreignObject>` 与 `<text>` 渲染方式是否一致
4. 保存后用 SVG 验证器或浏览器渲染检查

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

### 38. Hugo list.html 渲染 `years` 字段缺失崩溃
- `question/list.html` 调用 `delimit .Params.years ","`，当 `years` 不存在时 Hugo 报 `can't iterate over <nil>`
- 真题文件有 `years: ["2009"]`，但模拟题新生成的文件缺少 `years` 字段
- **修复**: 模拟题 frontmatter 加 `years: ["模拟卷"]` 使模板正常遍历
- **教训**: Hugo 模板中遍历 `.Params.xxx` 前要确保所有同 section 页面都有该字段

### 39. `---` 水平分割线与 frontmatter 冲突
- 源 content.md 中 `---` 可作为 frontmatter 分隔符或 markdown 水平分割线（between 选择题和综合题）
- JS 脚本按 `---` 计数（前2个为 frontmatter，之后为水平分割线）是脆弱做法
- **修复**: 用 boolean flag `inFrontmatter` 只在前两个 `---` 间过滤，之后的 `---` 正常处理
- **教训**: 解析含多个 `---` 的 md 文件时，用显式的状态机（begin/end frontmatter）而非全局计数

### 40. 图片操作导致 UTF-8 文件损坏
- 使用外部图片编辑器修改 `.md` 文件后，中文 UTF-8 多字节字符被替换为 `?`（0x3F）
- Hugo 报错 `yaml: invalid trailing UTF-8 octet`，实际是文件编码受损
- **恢复策略**:
  - git 跟踪的文件 → `git checkout --` 恢复
  - 从备份 `content.md` 再生 → 解析 `#### 科目` / `##### 题号` 结构提取
  - 无法再生的 → 重建 frontmatter + 保留 ASCII 内容残片

### 42. 绝不用 PowerShell 写 UTF-8 文件
- PowerShell `Set-Content` 默认使用系统 ANSI 编码（中文 Windows 下为 GBK）
- 管道重定向 `>` 或 `| Set-Content` 写 UTF-8 文件时破坏中文多字节字符 → 文件损坏
  - 损坏特征：`yaml: invalid trailing UTF-8 octet`（Hugo 构建报错）
  - 写空文件：当源文件也是 GBK 写入的 UTF-8 文件时，`Set-Content -NoNewline` 产生 0 字节文件
- **修复方案**：
  - 用 Python `open(path, 'w', encoding='utf-8')` 替代 PowerShell 的 `Set-Content`
  - 从损坏文件中恢复：用 `raw.decode('utf-8', errors='replace')` 提取 ASCII 内容残片，重建 frontmatter
- **规则**：凡是对 `.md` 或任何含中文的文本文件的**写操作**，必须用 Python 或 Node.js，不得用 PowerShell

### 43. 收藏页 tags 解析容错

### 44. `type` + `layout` 同时存在时的模板查找顺序
- `_index.md` 中 `type: exam` + `layout: year-detail` → Hugo 查找 `layouts/exam/year-detail.html`
- 不会回退到 `layouts/year/list.html`（即使 `type` 暗示 `year` 目录）
- **规则**: `layout` 覆盖默认的 `type` 推断。明确写了 `layout:` 时，Hugo 精确查找 `layouts/{type}/{layout}.html`
- **教训**: 修改模板前先确认 `_index.md` 中的 `type` 和 `layout`，找到真正生效的模板文件

### 45. 同行选项的 JS 拆分
- 部分源文件将所有选项写在同一行：`A. 2006H B.2007H C.2008H D.2009H`
- Hugo 渲染为单个 `<p>`，JS 正则 `^([A-D])[.、．]\s*(.+)` 误认为一个选项
- **修复**: 用全局匹配 `/([A-D])[.、．]\s*(.*?)(?=\s*[A-D][.、．]|$)/g` 拆分同一 `<p>` 内的多个选项
- 拆分为独立 `<div class="exam-option">` 后各占一行

### 46. 年份真题按全局题号排序而非科目分组
- 题目文件含有 `subjects` 元数据，但真题本身按题号 1-47 混排（选择+综合）
- **模板策略**: 全局 `sort "Params.number"` + 移除按 subject 的 range 循环
- 每题的科目信息用 `<span class="q-subject-tag">` 内联在题号旁，不分组
- **教训**: 用户期望的是"更像真题试卷"的布局，不是按知识点划分的习题集布局
- localStorage 中 `tags` 字段可能存为纯逗号分隔字符串、JSON 数组字符串 `["A","B"]`、或 JS 数组
- `createQuizCard` 中 `tags.split(",")` 对数组类型抛 TypeError，对 JSON 数组字符串产生带方括号/引号的碎片标签
- **修复**: 先用正则 `\["[^\]]*"\]` 匹配 JSON 数组，解析失败再回退逗号拆分 + `replace(/^\[|"|\]$/g, '')` 清理
- **教训**: 用户 localStorage 中的数据格式不受代码版本控制，展示时必须做多格式兼容

## SVG 还原

### 47. HTML 包裹的 SVG 提取
- csgraduates 的 SVG 以 HTML 片段形式出现：`<div class=svg-wrapper>` 包裹 `<svg>`
- 提取时用 `lastIndexOf("</svg>")` 而非 `indexOf("</svg>")`，因为内部可能有嵌套 SVG
- 非贪婪正则 `<svg[\s\S]*?</svg>` 匹配到嵌套 SVG 的第一个 `</svg>`，返回不完整 SVG
- **修复**: 用 `lastIndexOf("</svg>")` 找主 SVG 的闭合标签

### 48. HTML 无引号属性 → XML/SVG 错误
- csgraduates 的 HTML 属性无引号（如 `x=2 y=30.5`），这在 HTML5 中合法
- SVG 以 `image/svg+xml` MIME 提供时必须是合法 XML，所有属性值必须用引号包裹
- 批量修复正则 `/\s([a-zA-Z][\w-]*)=([^\s>"']+)/g` 可能产生双重引号（`=""0""`）
- **修复**: 加引号后必须执行 `replace(/""/g, '"')` 清理双重引号

### 49. SVG 路径缺少 stroke 属性
- 从 HTML 提取后，部分路径的 `stroke` 属性可能丢失
- 连接线 `M x y L x y` 格式的路径需要显式 `stroke="#000000" stroke-width="2"`
- 带 `fill="none"` 无 `stroke` 的路径完全不可见
- **检测**: 渲染后看不到连线或边框 → 检查 `<path>` 的 stroke 属性

### 50. 在线获取 vs 本地备份的 SVG 完整性
- csgraduates 的内联 SVG 可能被 HTML 分割（部分图形元素在 SVG 外作为独立 HTML）
- 从 svg-wrapper HTML 备份中提取的 SVG 比在线页面直接提取的更完整
- **策略**: 优先使用本地备份版本，而非在线页面提取的 SVG

### 51. ⚠️ `<foreignObject>` SVG 不能在 `<img>` 中渲染 — 换 `<object>`
- **根因**: draw.io 生成的 SVG 使用 `<foreignObject>` 嵌入 HTML 文字（`<div>`），Chrome 在 `<img>` 标签中**安全策略禁止渲染 `<foreignObject>`**。即使转成 data URI 也不行——问题在内容本身，不在加载方式。
- **表现**: 浏览器显示断裂图片占位图标，但 DevTools 中 `<img>` 的 src 已是正确 data URI。直接打开 `.svg` 在新标签页则正常。
- **教训**: **`<img src="...svg">` 遇到含有 `<foreignObject>` 的 SVG 永远失败**，不存在绕过方式。
- **正确方案**: 用 `<object type="image/svg+xml" data="...svg">` 替代 `<img>`，`<object>` 在独立文档上下文中完整支持 `<foreignObject>`。
- **检查方法**: 打开 SVG 源码，搜索 `<foreignObject>` 或 `<switch>` 包裹的 HTML 内容（`<div>`、`<span>`）。有这两个标签，就必须用 `<object>`。
- **修复时机**: 遇到断裂 SVG 图片时，先检查 SVG 源码有无 `<foreignObject>`，有则立即改 `<object>`，不要试 data URI 等<img>方案。

### 52. ⚠️ 题目文件 UTF-8 损坏修复后必须检查 subject 与内容匹配
- **根因**: PowerShell `Set-Content` 默认 GBK 编码写入 `.md` 文件，破坏 UTF-8 多字节字符（中文标点变为 `�`）；同时内容迁移脚本可能把**多题答案拼接**到同一文件，或把隔壁科目内容混入
- **表现**: 前端渲染出现乱码、同一题内出现另一个科目内容、subject 标签与实际题目内容不匹配
- **检查方法**: 对 `content/question/*.md` 做两遍扫描：
  1. UTF-8 完整性：`python -c "open(f).read().encode('utf-8')"` 或 grep `\ufffd`（`�`）
  2. subject 与内容关键词匹配：DS 题含"组成原理/OS/网络"关键词 → 标记为可疑
- **修复流程**:
  1. 用 `Write` 工具（UTF-8 安全）重写整个文件，不要用 PowerShell `Set-Content`
  2. 文件名 prefix（`ds/co/os/cn`）与 frontmatter `subjects` 必须一致
  3. 修复后检查 year-detail 页面渲染结果
- **教训**: 内容文件一旦用 PowerShell 写入，UTF-8 损坏不可逆。只能从备份或原始源重新生成

### 53. ⚠️ 选项解析 JS 扫描所有 `<p>` 导致解析中 B/C 被错识别为选项
- **根因**: `year-detail.html` 和 `single.html` 中选项转换用 `qBody.querySelectorAll('p')` 扫描 qBody 内**所有** `<p>` 元素，包括已被移入 `.answer-panel`（答案/解析区域）的 `<p>`。解析中包含 `B、C`（如"选项B、C"）时，被 regex `([A-D])[.、．]` 匹配为选项。
- **表现**: 解析内容中出现的 `B.` `C.` `B、` `C、` 被渲染为可点击的选项框，样式错乱
- **修复**: 用 `container.children` 遍历**直接子节点**，只处理 tagName === 'P' 的元素：
  ```javascript
  var allP3 = [];
  for (var i = 0; i < qBody.children.length; i++) {
    if (qBody.children[i].tagName === 'P') allP3.push(qBody.children[i]);
  }
  ```
- **检查范围**: `layouts/exam/year-detail.html` + `layouts/question/single.html` 两处 JS 均需修复
- **教训**: `querySelectorAll('p')` 搜索所有后代 `<p>`，包括 blockquote、answer-panel 嵌套的。当解析含选项字母 + 标点的文本时必出 bug。**只处理直接 `<p>` 子节点。**

### 54. ⚠️ 解析区混入隔壁题目内容（内容污染检测法）
- **根因**: 早期迁移脚本或手动编辑时，题目文件的分析区（`>` blockquote）被混入了**下一道题的内容**。
- **典型模式**: 题 N 的分析区末尾出现 "题 N+1 题干 + 选项 + 正确答案" 的完整内容（如 `2009-co-022 分析区末尾混入 OS 第23题`、`2009-os-032 分析区末尾混入 计算机网络第33题`）
- **检测方法**: 扫描所有 question 文件，统计 `正确答案` 出现次数。每个单题文件应**恰好 1 次**：
  ```python
  re.findall('正确答案', text)  # 超过1次 → 内容污染
  ```
- **修复**: 从 `正确答案` 的第 2 次出现处截断，删除其后所有行（包括尾部 `---` 装饰线）
- **补充检查**: 分析区末尾的 `---`（markdown 水平线）也应删除——通常是之前污染清理不彻底残留

### 55. ⚠️ 选项格式 `X 、`(字母+空格+顿号) 导致选项解析失败
- **根因**: 选项解析 JS 正则 `([A-D])[.、．]` 要求**字母紧跟分隔符**（`.` / `、` / `．`），但个别文件用了 `A 、2`（字母+空格+顿号 `、` U+3001），空格阻断匹配 → 该行不被转为可点击选项，多个选项挤在一行时只显示合并的一行（"只显示两个选项"）。
- **典型样本**: `2009-os-025.md` 原内容 `B 、3 C 、4 D 、5` 全在一行，A 独占一行 `A 、2`，渲染只剩 2 块文本。
- **修复（数据层，根因）**: 把选项归一化为标准 `A\. 文字` 格式（markdown 转义句点），每个选项独立一行：
  ```
  A\. 2
  B\. 3
  C\. 4
  D\. 5
  ```
- **修复（模板层，安全网）**: 在 4 个模板的选项正则中都允许字母与分隔符间有可选空格：
  - `layouts/question/single.html` L154/L160
  - `layouts/exam/year-detail.html` L190/L196
  - `layouts/exam/single.html` L315
  - `layouts/exam/408quiz/year-detail.html` L109
  - 改为 `([A-D])\s*[.、．]\s*`（含 lookahead 内 `\s*`）
- **检测方法**: 扫描所有 question 文件，找 `^[A-D]\s+[、．]`（字母+空格+顿号）或一行含 ≥2 个选项标记（排除 `>` 解析区误报）

### 56. ⚠️ 题干与选项挤在同一行 → 题干被 JS 整体替换而"丢失"
- **根因**: 选项解析 JS 用全局正则 `txt.match(/([A-D])\s*[.、．].../g)` 命中段落内**任意** `A.` 选项标记，命中后把**整段 `<p>`** 替换为选项 div，导致选项标记**之前**的题干文字被一起删掉 → 渲染只剩选项、题干"丢失"。
- **典型样本**: `2009-os-027.md` 原内容 `一个分段存储...最大段长是()。 A.28 字节 B. 21⁶ 字节 C.2 ²⁴ 字节 D. 2³² 字节` 全在一行，题干被吞。
- **修复（数据层，根因）**: 题干与每个选项各占独立段落，选项用标准 `A\. 文字` 格式：
  ```
  一个分段存储管理系统中，地址长度为32位，其中段号占8位，则最大段长是\(\)。

  A\. 2⁸   字节

  B\.  2¹⁶  字节

  C\. 2  ²⁴ 字节

  D\.  2³² 字节
  ```
- **修复（模板层，安全网）**: 在 `layouts/question/single.html` 与 `layouts/exam/year-detail.html` 的选项转换逻辑中，先算首个选项标记位置 `txt.search(/[A-D]\s*[.、．]/)`，若其前有非空题干前缀，则先插入一个 `<p class="exam-stem-text">` 保留题干，再放选项 div。这样即使数据未拆分也不会丢题干。
- **检测法**: 扫描 `[tag_link]` 之前的题干区，找"含 `A.`/`B.` 且首选项标记前还有中文题干"的单行：
  ```python
  pre = body.split('[tag_link]')[0]
  for l in pre.split('\n'):
      st = l.strip().replace('\\','')          # 去掉 markdown 转义反斜杠
      opts = re.findall(r'[A-D]\s*[.、．]', st)
      if 'A' in {o[0] for o in opts} and 'B' in {o[0] for o in opts}:
          if re.search(r'[\u4e00-\u9fff]', st[:st.find('A.')]):  # 前缀含中文=题干
              # 命中（注意 A、B、C 作为表名/操作标签的情况属误报，需人工复核）
  ```
- **注意**: 部分命中是**误报**（题干里用 `A、B、C、D` 表示表名/进程名/`A.B.C.D` 表示操作步骤），这些不是选项，需人工区分；JS 安全网能保证这类也不会丢题干。

### 57. ⚠️ 单题爬取（csgraduates 指定题号锚点）
- **经验来源**: `tasks/408-crawler/`（`crawler.js` + `filler.js` + `crawled_data/{year}.json`）。核心套路：Node `https.get` 抓整页 HTML → 解析**隐藏 div**（答案/解析默认 `display:none`）。
- **单题锚点结构**（以 `408quiz/2009/#43` 为例）：
  - 题号标题用 `<h5 id=43>`（**无引号**，`id=43` 不是 `id="43"`）
  - 选择题解析：`id=explanation-choice-<UUID>-<N>`（N=题号）
  - 综合题（Q41-47）解析：`id=solution-answer-<UUID>-<N>`（**N=题号-40**，即 Q43→N=3），内容在 `<div class="solution-detail" style=display:none>` 内，多个 `<p>` 分段
  - 题干在 `answer-container` 之前的若干 `<p>` 中
- **提取脚本**: `scripts/scrape_q43.js`（可改年份/题号复用），输出 markdown 表格到 `_tmp_q43.md`
- **坑**:
  - Python `urllib` 在本机**不支持 https**（`unknown url type`），用 Node 爬
  - 页面 HTML 经 `decode('utf-8','replace')` 或 PowerShell 控制台会显示 `?` 乱码，但**写文件（Node `fs.writeFileSync(...,'utf8')` / Python `[System.IO.File]::WriteAllText`）才是真 UTF-8**，读文件用 Read 工具验证
  - solution-detail 是 `answer-container` 的**兄弟节点**（非嵌套），正则用 `<div class="solution-detail[^>]*>([\s\S]*?)<\/div>` 单 `</div>` 即可，不要写 `</div></div>`
- **已验证**: 2009-#43 爬取成功，题目+解析与 `content/question/2009-co-043.md` 一致

### 22. Hugo 内容文件中的图片路径

- `content/question/` 下的 `.md` 不是 leaf bundle（不是 `index.md`），不能使用相对路径引用同目录图片
- `../../static/images/questions/...` ❌ — Hugo 不解析，开发服务器 404
- `![图](/cc408/images/questions/file.svg)` ✅ — 绝对路径，对应 `static/images/questions/`
- `{{ "images/questions/file.svg" | relURL }}` ✅ — 也可在模板中用 relURL 辅助

### 23. 解答题子问题段落格式

- 解答题干的 `(1)`、`(2)`、`(3)` 子问题如果每个独占一行且中间有空行，Goldmark 会渲染为独立 `<p>` 块
- 这使它们看起来像选择题选项（A./B./C. 格式），容易误导
- **修复**: 去掉子问题之间的空行，让 Goldmark 合并到同一个 `<p>` 段落：
  ```markdown
  要求：
  \(1\)描述算法的基本设计思想；
  \(2\)描述算法的详细实现步骤；
  \(3\)根据设计思想和实现步骤...
  ```

### 24. docx→md 转换中表格丢失问题

- 源的 docx 文件中的 HTML `<table>` 在 mammoth 转换时可能丢失表格结构，数据堆叠为纯文本
- **表现**: 题干中明明写了"下表给出了..."但表格完全不存在（如 2009-044 的 C1-C4 表）；或在解析/参考答案区域数据存在但无管道符格式
- **根因**: mammoth 将 `<table>` 转换为纯文本时只保留了单元格文字，丢失了行列分隔符
- **修复方案**: 从 csgraduates.com 重新爬取原始 HTML 页面，提取其中的 `<table>` 元素，转换为 markdown 表格
- **爬取最佳实践**:
  ```javascript
  const html = await fetch('https://www.csgraduates.com/study_methods/408quiz/2009/');
  // 提取题号 N 的 HTML 片段: <h5 id=N> ... </h5> 到下一个 <h5>
  const regex = new RegExp('<h5\\s+id=' + N + '(\\s|>)', 'i');
  // 表格在 <table class="table td-initial"> 或 <table> 中
  ```
- **验证策略**: 对比爬取数据与现有文件，确认表格行数、列数、表头一致后再替换
- **涉及文件**: 2009-co-044.md（3个表）、2009-cn-047.md（4个表）

### 27. 解析区超长段落和内容污染问题

- docx→md 转换后，解析区（尤其是综合题）经常出现**超长单一段落**，所有小问的答案连在一起无分段
- 表格末行可能被后续**文本污染**（表格行末尾直接跟着文字，破坏 Goldmark 表格渲染）
- **修复规范**:
  1. 解析中 `(1)`、`(2)`、`(3)` 子答案之间用**空行**隔开
  2. 每个 markdown **表格行必须独占一行**，末尾不能有任何文字
  3. 表前后用说明文字+空行分隔
- **常见内容错误**:
  - 指数格式：`2 6 − 2` → `$2^6-2$`（丢失脱字符 `^`）
  - 接口编号：`E1→E2` 混淆（需对照拓扑图验证）
- **断裂 markdown 链接**: 题干中 `[IP地址,标签](URL格式)` 会被解析为 markdown 链接，实际应为纯文本
- **修复**: 手动删除方括号和圆括号，保留文本内容
- **涉及文件**: 2009-cn-047.md

### 28. 全量扫描与批量修复策略

- 对 `content/question/` 下所有文件做全量扫描时，优先**逐个审计**而非通用正则扫描
- **正确流程**: 先写审计脚本（`scan_pollution.py`）白名单扫描 → 分类问题 → 针对性地写修复脚本
- 通用正则替换容易**误伤**正常文件（如错误的 `(1)(2)(3)` 分割可能破坏选择题选项）
- **修复优先级**: 内容污染最高（解析混入下题题干）→ 数据完整性问题 → 格式问题
- **自动化边界**: 表格缺失和JS污染需手动/半自动处理，不要过度自动化

### 29. 解析区 JS 污染问题

- 一些 docx→md 转换后，csgraduates 页面的交互式 JavaScript 代码（"查看答案与解析"功能）完整地混入了解析区
- **污染特征**: `[tag_link]` 后出现 `function toggleSolutionDetail`、`showNotification`、`collectAnswer`、`indexedDB` 等 JS 代码
- **涉及范围**: 所有 `ds-041.md` 文件（7个），包括 2014 真题和 simulate-1/2/5/6/7/8
- **恢复方案**:
  1. 优先从 csgraduates 重新爬取（如网站可访问）
  2. 备用方案：从 JS 中提取嵌入的文本碎片（`clean_js_pollution.py` 已实现）
  3. 最差方案：清理JS后留空位标注待补充
- **已创建恢复脚本**: `scripts/clean_js_pollution.py`

### 30. csgraduates.cn 访问限制

- 在公司内网环境下 csgraduates.cn 可能 **DNS 解析失败**（`getaddrinfo failed`）
- **失败表现**: Python requests 报 ProxyError/ConnectionError，curl 报 Could not resolve host，Playwright 无法连接
- **替代方案**:
  - 使用浏览器会话（需用户确认有浏览器可正常访问该域名）
  - 使用项目已有的 `tasks/408-crawler/crawled_data/` 下的 JSON 存档
  - **注意**: JSON 存档只包含选择题（1-40题），**不包含综合题（41-47题）**的解析
- **限制**: 爬虫脚本和浏览器自动化在本机受限（无uv/pip安装权限、Playwright无浏览器二进制文件）

### 31. 内容污染：下一题题干混入当前文件

- **现象**: 2022-co-043.md 中包含 Q44 的完整题干（"44. (8分)假设某磁盘驱动器..."），在 `[tag_link]` 之前
- **结构分析**: Q43题干 → Q44题干（污染）→ `[tag_link]` → Q43的解析
- **自动修复方法**: 找到 "44 . (8分)" 字符串位置，截断到下一个 `[tag_link]`
- **检测方法**: 检查 `[tag_link]` 之前的区域是否包含 "数字. (数字分)" 模式且数字 > 3
- **预防**: docx 转换时注意分页符，每个新题号应另起文件

### 32. 手动清理7个JS污染文件的经验

- **覆盖文件**: 2014-ds-041, simulate-1/2/5/6/7/8-ds-041（共7个）
- **清除内容**: `window.quizDB`、`IndexedDB`、`showNotification`、`collectAnswer` 等整套收藏/查看答案交互JS
- **附带清理**: 2014-ds-041 末尾还含下一题题干（"42 某网络中的路由器运行OSPF"），随JS一并移除
- **教训**: `ds-041.md`（数据结构解答题第1题）在转换过程中最容易混入JS代码，因为 csgraduates 页面在该题有收藏按钮和查看答案切换功能
- **手动操作要点**: 在 `[tag_link]` 后找到 JS 代码块起始位置，删除整段至文件末尾，保留题干和 `[tag_link]` 标记

### 33. 表格手动恢复要点

- **2009-ds-002.md**: 栈出入过程表格（4列：序号/说明/栈内/栈外，14行），表格在 blockquote `>` 内
- **simulate-2-co-015.md**: SRAM/DRAM 对比表（2列：RAM类型/特点），也在 blockquote 内
- **注意**: 恢复表格时注意表头分隔行（`|---|---|`）列数与表头一致，Hugo Goldmark 严格要求

### 34. 模拟题格式重构：单题拼成整卷展示

- 模拟题已和真题一样做了单题拆分（`content/question/simulate-1-*.md`），这是正确的格式
- **重构方案**：模仿真题 `408quiz/2009/` 结构，用 `year-detail.html` 模板将单题拼成整卷
  - `408quiz/simulate-*/`（空壳目录）→ 移到 `simulate/set-*/`
  - `simulate/set-N/_index.md` 加入 `layout: year-detail`, `set: N`, `source: "模拟题"`
  - `year-detail.html` 模板已天然支持 `set` 参数：`if $.Params.set` 分支按 `source=模拟题 + set=N` 过滤
- **旧整卷备份**：`simulate/set-*.md`（78KB/套）→ `simulate/backup/`
- **回退链接**：`year-detail.html` 新增条件判断，模拟卷返回 `simulate/`，真题返回 `408quiz/`
- **效果**：`/exam/simulate/set-1/` 正确渲染 59 题，和真题完全一致的交互体验

### 35. 收藏功能 localStorage key 统一 + 页面状态恢复

- **根因**：`layouts/exam/year-detail.html` 中 `toggleCollect` 函数使用 `cc408_collections` key 存储简单 `{num,subject,time}` 对象，而 `quiz-collection.js`（收藏页）和 `collect-quiz.js`（单题页）统一使用 `quiz_collections` key 存储完整题目数据 → 收藏页看不到任何真题收藏
- **状态丢失根因**：`toggleCollect` 只在点击时读写 localStorage，页面加载时**不检查**已有收藏 → 刷新后所有按钮都退回初始态
- **点击表现异常根因**：button 的 `textContent` 在 toggle 时设为 `'收藏'`（无星），但初始 HTML 包含 `⭐` → 第二次点击后显示 `收藏` 而非 `⭐ 收藏`，让用户感觉操作不连贯
- **修复方案**（全部在 `layouts/exam/year-detail.html`）：
  1. 移除 inline `onclick="toggleCollect(...)"`，改用 `data-qnum` 属性 + JS event-driven 方式
  2. 页面加载时立即检查 `quiz_collections`，已收藏的按钮自动显示 `已收藏` + `collected` class
  3. 保存时提取 DOM 中的完整题目数据（question、options、answer、explanation、tags），与 `collect-quiz.js` 格式一致
  4. 统一使用 `quiz_collections` key
- **规则**：所有收藏功能必须使用 `quiz_collections` 作为 localStorage key，确保真题页、单题页、收藏页三端数据互通

### 36. content.md 整卷残留导致真题页面显示异常

- **现象**: `content/exam/408quiz/2010/`~`2025/` 的年份文件夹下存在 `content.md`（40~67KB/个），是 docx→md 转换时留下的整卷文件
- **影响**: Hugo 将 `content.md` 渲染为独立页面，与 `_index.md` 的 year-detail 单题聚合**叠加显示**，页面混入整卷内容，出现多余"content"文字和链接
- **检测**: `find content/exam/408quiz -name "content.md"`（14个年份文件夹中招，仅 2009/2014/2022/2026 干净）
- **修复**: 移到 `content/exam/408quiz/backup-整卷/` 统一备份
- **预防**: docx→md 迁移后检查每个年份文件夹下只有 `_index.md`，无其他 `.md` 文件

### 58. 408quiz-detail.html 选项 JS 缺少多选项段落拆分

- `layouts/exam/408quiz-detail.html` 原 JS 用 `^([A-D])\s*[.、．]\s*(.+)` 逐 `<p>` 匹配选项
- Goldmark 将无空行的 4 个选项渲染为单个 `<p>`，简单正则只匹配首项 A，丢失 B/C/D
- **修复**: 改用 `txt.match(/([A-D])\s*\.\s*(.*?)(?=\s*[A-D]\s*\.|$)/g)` 拆分同一段内的多选项（与 `year-detail.html` 一致）
- **教训**: 所有模板中的选项转换代码应统一使用多选项拆分逻辑，不要用简单逐段匹配

### 37. ⚠️ 批量脚本执行前必须小范围测试 + 人工验证

- **事故**: commit `c3c8178` 的批量修复脚本对 `content/question/` 执行全局正则替换，导致部分选择题的 A/B/C/D 选项被误删
  - 示例：`2011-ds-001.md` 原版有 `A\. O(log₂n) B\. O(n) ...`，批处理后仅剩 `正确答案：A`
  - 部分文件完整丢失，部分文件部分丢失（如 4 个选项剩 3 个）
- **根因**:
  1. 脚本用全局正则匹配并替换了整段内容，选项行 `A\. 内容` 被正则误匹配为"多余行"而删除
  2. 未做小范围试跑就直接应用到全部 1152 个文件
  3. 未在 git add 前检查 diff 确认选项没有被改动
- **铁律**⚠️（已记录到 agent-rules）：
  1. **任何批量修改脚本必须先在 2~3 个文件上试跑**
  2. **人工验证试跑结果** — 打开文件检查选项、关键内容是否完整
  3. **验证通过后再应用到全量文件**
  4. **git add 前必须检查 diff**：`git diff --stat` 看改动了多少文件，`git diff` 抽查具体行级变更
- **恢复方案**: 从提交 `4cf9d6c`（选项丢失前最后一个干净版本）逐文件恢复选项行，注入到当前文件（保留格式化修复）
- **恢复结果**: 通过 `scripts/restore_options.py` 恢复 198 个文件（第一轮 135 + 第二轮同行格式 63），恢复率 80.1%（923/1152）
- **遗留问题**：208 个文件旧版也无标准选项行（爬虫历史数据），21 个文件旧版仅 1-3 项（数据不完整）
- **恢复教训**:
  1. 旧版选项格式是 `A\.内容`（反斜杠+点，无空格），`extract_options` 正则 `r'^[A-D]\\.\s'` 因要求尾随空格而无法匹配，需用 `r'^[A-D]\\.'`
  2. 部分文件选项在同一行（`A\.xxx B\.xxx C\.xxx D\.xxx`），需用 `re.split(r'(?=[A-D]\\.)', line)` 拆分为单项
  3. 恢复脚本应先 dry-run 统计范围，再执行实际恢复
  4. `find_insert_position` 以 `[tag_link]` 为锚点是可靠的（所有选择题文件都有该标记）

## 六、Q11-Q12 选项缺失与重复文件修复（2026-07-11）

### 问题

1. **ds-011 文件选项缺失**：2019、2024 年 ds-011 文件有完整题干和答案，但缺少 A/B/C/D 选项行
2. **ds-012 文件重复**：2013-2025 年的 ds-012 文件是 co-012 的重复（同 2010 年处理过的问题），subject 为"组成原理"（错误）而非"计算机组成原理"，且均缺少选项行

### 修复

1. 从爬虫数据（`tasks/408-crawler/crawled_data/`）补充选项到 2019-ds-011 和 2024-ds-011
2. 删除 11 个 ds-012 重复文件（与 lessons 第 5 节 2010 年处理方式一致）

### 教训

1. **ds-012 文件与 co-012 内容重复**的规律：当某年的 co-012 已存在且有完整选项时，同年的 ds-012 文件必为重复文件（subject 为"组成原理"而非"计算机组成原理"），应直接删除
2. **2011、2012 的 ds-012 例外**：这两年的 ds-012 是唯一版本（无 co-012 对应项），且有完整选项，需保留
3. 检测选项数时，正则需兼顾多种格式：`A\.内容`（无空格）、`A\. 内容`（有空格）、`A\.内容 B\.内容`（一行多项）
# CC408 优化 Lessons

> 本次优化 sprint 途中记录的经验教训

---

## Lesson 1: 共享 JS 要早做

JS 交互逻辑（选项转换、答案折叠、收藏）在同一项目中以 200+ 行的规模重复了 5 次。
早该在第一次写 `exam/408quiz-detail.html` 时就把逻辑抽取到 `assets/js/` 中。

**教训**: 项目中第二个出现类似交互的页面就是"抽取共享模块"的信号，不需要等到第五个。

---

## Lesson 2: 收藏 ID 必须统一

同一道题在不同页面使用不同的 ID 生成逻辑，导致收藏重复。
最佳实践：ID 应基于题目本身的属性（年份+题号+题源），而非页面路径或 DOM 属性。

**教训**: 涉及跨页面共享的数据（收藏 ID），必须在数据设计阶段统一约定。

---

## Lesson 3: Hugo 构建时间 vs 运行时性能

3889 个 .md 文件导致 `hugo` 构建 40-60s。
将全部题目的完整 HTML 注入 JSON 虽然让 JS 渲染简单，但构建时间 + 页面体积双双增加。
折中方案：按需加载 — 初次只加载前 N 题数据，翻页时 AJAX 获取。

**教训**: 静态站点追求"全量预生成"并不总是最优，需要根据运行时访问模式做取舍。

---

## Lesson 4: 内网环境的 git 推送

内网 SSH 端口 22 不通，需切换到 HTTPS remote + GCM 认证。
`git remote set-url origin https://github.com/cycycy5464/cc408.git`

**教训**: 在初始化项目时就配置 HTTPS remote，避免后续切换。

---

## Lesson 5: 模板中的 Go Template 语法错误

`{{ $type := if eq .A "x" }}y{{ else }}z{{ end }}` 是无效语法。
Go template 不支持在 `:=` 中嵌入 `if`，需先初始化再赋值。

**教训**: 每次修改模板后必须 `hugo --quiet` 验证构建，不能靠肉眼审查。

---

## Lesson 6: 模板批量替换用 Python 要谨慎

Python `re.sub` 替换 Hugo 模板文件时，`re.DOTALL` 模式可能匹配过度或不足。
两次事故：
- `taxonomy.html`：替换后残留旧 JS 碎片在函数体内，模板结构错乱
- `chapter-exercises.html`：误删 `{{ end }}` 闭合标签 + 残留已删除的函数调用

**教训**: 对 Hugo 模板做结构性修改，优先用 `Write` 全量重写而非 `re.sub`。必须用正则时，逐个确认替换边界并 `hugo` 验证。

---

## Lesson 7: CSS 提取后检查孤立闭括号

CSS 分区 (`custom.scss` → 各模板) 移除 `.tm-*` 样式块后，遗留了一个 `}`，
导致 SCSS 编译报 `expected selector or at-rule`。

**教训**: CSS 提取后运行 `grep -n '^}$'` 检查无匹配的闭括号。`hugo` 构建必须通过才能提交。

---

## Lesson 8: `<details>` 元素适合大数据层级展示

2650 道课后题用 `<details>` 手风琴展示（科目→章节→小节），零 JS，原生 HTML。
初始 DOM 只渲染外壳，展开时浏览器才渲染内部内容，性能无压力。

**教训**: 对于「需要折叠大量同类数据」的场景，优先用 `<details>` 而非 JS 手风琴。兼容性好、性能好、零依赖。

---

## Lesson 9: 课后题展示需要三重分组（科目→章节→小节）

课后题 2650 道、4 科、每科多章、每章多节。仅按题号排序会导致大量同号题目混淆。
需要 `data-section` 属性 + 三级联动筛选。

**教训**: 数据量大且有层级关系的内容，模板层面就要设计好分组层级，不要依赖 JS 动态解析。


---

## Lesson 10: 收藏 ID 格式需全局一致

`collect-quiz.js` 之前使用 `choice-/cc408/question/...` 作为收藏 ID，
而共享模块使用 `{year}-{number}`。同一题在不同页面收藏生成不同 ID。

**教训**: 所有涉及收藏的 JS 文件必须使用同一个 ID 生成函数或格式。
收集项目全部收藏入口，逐处核对。


---

## Lesson 11: Hugo :filename 已废弃

Hugo 0.144.0+ 将 `:filename` 重命名为 `:contentbasename`。
`permalinks` 中必须用 `:contentbasename` 否则构建报 deprecated 警告。

**教训**: Hugo 版本迭代快，配置语法要跟着 Hugo Release Notes 更新。
