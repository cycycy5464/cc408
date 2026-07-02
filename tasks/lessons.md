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
