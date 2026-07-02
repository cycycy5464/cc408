# CC408 — 408 考研知识整理平台

## 项目简介
Hugo 静态站点，部署在 GitHub Pages（`cycycy5464.github.io/cc408/`）。
使用 Hugo 0.135，无 Hugo 模块依赖（独立项目）。

## 目录结构
```
cc408/
├── content/
│   ├── docs/               # 知识点（4科: data-structure/computer-org/os/network）
│   ├── exam/               # 刷题（408quiz/simulate/exercise）
│   ├── code/               # 算法实现
│   ├── study-methods/      # 备考方法
│   ├── qa/                 # 常见问题
│   └── graph/              # 知识图谱页面
├── layouts/                # 页面模板
│   ├── _default/
│   ├── docs/               # 知识点布局（带侧边栏）
│   └── partials/           # 组件
├── assets/
│   ├── css/custom.scss     # 设计系统（暗色主题、蓝绿渐变）
│   └── js/                 # watermask, knowledge-graph, resource-filter
├── static/                 # 静态文件
│   ├── images/docs/        # 知识图谱配图
│   └── data/knowledge-graph.json
└── tasks/                  # 任务与教训
```

## Build & Run
```bash
cd cc408
git push                              # GitHub Actions 自动构建部署
# 或本地构建
GOROOT=/c/Users/cheny/miniconda3/go \
PATH="...:$PATH" \
hugo --minify                         # 需要 Go 0.21+
```

## 关键教训（详见 tasks/lessons.md）
1. `relURL` 不要前导 `/`：`"docs/" | relURL` 而非 `"/docs/" | relURL`
2. Hugo 菜单 `.URL` 自动含 baseURL 前缀（`/cc408/`）
3. 导航高亮用 `$section` 互斥匹配，不用 `hasPrefix`
4. 列表页用 `.CurrentSection` 做范围过滤
5. 中文文件处理统一 `utf-8` 编码
