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
