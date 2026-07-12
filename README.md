# CC408 — 408 考研知识整理平台

> Hugo 静态站点，部署于 GitHub Pages。覆盖数据结构、组成原理、操作系统、计算机网络四科。

## 快速开始

```bash
# 本地开发
cd cc408
hugo server

# 构建发布
hugo --minify
```

## 项目结构

```
cc408/
├── content/
│   ├── docs/               # 知识点（4科）
│   ├── exam/               # 刷题页面
│   ├── question/           # 题目文件（按年份-科目-编号命名）
│   ├── code/               # 算法实现
│   ├── study-methods/      # 备考方法
│   ├── qa/                 # 常见问题
│   └── graph/              # 知识图谱
├── layouts/                # Hugo 模板
│   ├── _default/
│   ├── question/           # 题目详情模板
│   ├── exam/               # 刷题列表模板
│   ├── docs/               # 知识点模板
│   └── partials/           # 公共组件
├── assets/
│   ├── css/custom.scss     # 暗色主题 + 蓝绿渐变
│   └── js/                 # 收藏、知识图谱、筛选等脚本
├── config/_default/        # Hugo 配置
├── static/                 # 静态资源（图片、数据等）
│   └── images/questions/   # 题目配图（SVG/PNG）
├── scripts/                # 工具脚本
├── tasks/                  # 任务跟踪 & 经验教训
│   ├── current.md          # 当前任务
│   ├── lessons.md          # 关键教训（重要）
│   └── fix-exam-rendering-issues.md
└── .github/workflows/      # CI/CD
```

## 关键教训

详细经验见 [`tasks/lessons.md`](tasks/lessons.md)，核心要点：

| # | 教训 |
|---|------|
| 1 | `relURL` 不要前导 `/`：`"docs/" | relURL` ✅ |
| 2 | Hugo 菜单 `.URL` 自动含 baseURL 前缀 |
| 3 | 导航高亮用 `$section` 互斥匹配，不用 `hasPrefix` |
| 4 | 列表页用 `.CurrentSection` 做范围过滤 |
| 5 | 所有文件统一 UTF-8 编码 |
| 6 | SVG 文件必须在 void 元素加 `/` 自闭合才能被 Hugo 解析 |
| 7 | 题目 `<p>` 中 `(1)(2)(3)` 会被拆分为独立段落，解答题应合并为连续文本 |
| 8 | `content/question/` 不是 leaf bundle，图片用 `/cc408/images/questions/...` 引用 |

## 部署

**当前部署**：GitHub Actions → GitHub Pages

- 触发分支：`master`
- 构建命令：`hugo --minify`
- 部署地址：`https://cycycy5464.github.io/cc408/`
- 工作流文件：`.github/workflows/publish-cc408.yaml`
