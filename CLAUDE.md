# CC408 — 408 考研知识整理平台

本项目的验证均由用户完成！ 完成任务提醒用户验证！

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

## Notes

- 当你完成任务的时候回顾一下用户本轮的对话，确保任务都完成了再让用户验证
- 不允许从git恢复数据，从爬虫数据恢复，爬虫数据没有的就修改爬虫脚本重新爬
- md表格和文本之间需要换行  题目可能存在非解析内容混入，注意不要毁坏原有解析内容 题目可能存在md表格未正确生成 数据散落的情况 需要修复 注意不要毁坏原有内容 选择题D选项可能会和tag粘连丢失  有的代码完全没有包裹需要```c 有的代码只有```缺了c 如果存在需要latex格式的 请修复为hugo可以正确展示的latex格式 MD 表格每行竖线数量必须统一，分隔行、数据行列数一致，无多余空竖列。将遇到的问题问题的解决方法都纳入记忆
- 选择题保证是4选项 不允许多也不允许少 请确保选择题都是4个选项（如果不是则从爬虫数据覆盖）覆盖完毕需要检查选项个数
- 大题 不同小问的解析需要换行 有序号的也需要换行展示
- 真题修复任务需要参考task/真题修复文件夹的readme
- 组成原理 和 计算机组成原理的区别 导致 选择题重复 从爬虫数据获取记得处理
