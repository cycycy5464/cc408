# CC408 使用指南

## 快速开始

### 1. 本地运行

确保已安装 Hugo Extended v0.135+：

```bash
# 进入项目目录
cd E:\programcc408\cc408

# 启动开发服务器
hugo server

# 访问 http://localhost:1313
```

### 2. 构建发布版本

```bash
# 构建静态文件到 public/ 目录
hugo --minify

# 查看生成的文件
ls public/
```

### 3. PDF 水印处理

```bash
# 需要先安装 PyMuPDF
pip install PyMuPDF

# 运行水印脚本（处理 static/resources/ 下的所有 PDF）
python scripts/watermark-pdf.py

# 带水印的 PDF 输出到 static/resources-wm/
```

## 站点结构

```
cc408/
├── config/_default/      # 配置文件
│   ├── hugo.yaml         # 站点配置（标题、URL、语言）
│   ├── params.yaml       # 主题参数（暗色模式、KaTeX、水印）
│   ├── menus.yaml        # 导航菜单
│   ├── module.yaml       # Hugo 模块
│   └── languages.yaml    # 中文语言配置
├── content/              # 所有内容（Markdown）
│   ├── _index.md         # 首页
│   ├── docs/             # 知识点（按科目分目录）
│   │   ├── data-structure/    # 数据结构
│   │   ├── computer-org/      # 计算机组成原理
│   │   ├── os/              # 操作系统
│   │   └── network/         # 计算机网络
│   ├── exam/             # 题目
│   │   ├── choice/          # 选择题
│   │   ├── application/     # 应用题
│   │   └── comprehensive/   # 综合题
│   ├── graph/            # 知识图谱页面
│   └── resources/        # 资源下载
│       ├── free/            # 公开资源
│       └── premium/         # 高质量资源
├── layouts/              # HTML 模板
│   ├── _default/          # 基础模板
│   ├── docs/              # 知识点页面
│   ├── exam/              # 题目页面
│   ├── graph/             # 知识图谱页面
│   ├── resources/         # 资源页面
│   └── partials/          # 可复用组件
├── assets/               # 前端资源
│   ├── css/custom.scss    # 暗色主题样式
│   └── js/                # JS 脚本
├── static/               # 静态文件（直接复制到 public/）
│   ├── js/                # JS 脚本（URL 映射到 /js/）
│   ├── data/              # 知识图谱 JSON 数据
│   └── resources/         # 原始 PDF 资源
└── scripts/              # 构建脚本
    └── watermark-pdf.py   # PDF 水印处理
```

## 添加内容

### 添加知识点笔记

在 `content/docs/{科目}/` 下创建 `.md` 文件：

```yaml
---
title: "快速排序"
date: 2026-06-25
weight: 1
tags: [排序, 分治, 重点]
difficulty: 3
prerequisites: ["递归", "二叉树遍历"]
subject: data-structure
chapter: 6
chapter_title: "排序"
exam_points: ["排序算法比较"]
---

## 算法思想

正文内容...

## 代码实现

```c
// C 代码会自动高亮
```

## 公式

时间复杂度 $O(n \log n)$
```

### 添加题目

在 `content/exam/{choice|application|comprehensive}/` 下创建 `.md` 文件：

```yaml
---
title: "2024年408真题 - 选择题第1题"
date: 2026-06-25
type: choice
subject: data-structure
source: "2024年408真题"
year: 2024
difficulty: 2
tags: [二叉树, 遍历]
related_knowledge:
  - "/docs/data-structure/ch04-tree/binary-tree-traversal/"
---

## 题目

题干内容...

## 选项

1. 选项 A
2. 选项 B
3. 选项 C
4. 选项 D

## 答案

选项 1

## 解析

详细解析...
```

### 添加资源

在 `content/resources/free/` 或 `content/resources/premium/` 下创建 `.md` 文件：

```yaml
---
title: "数据结构思维导图"
date: 2026-06-25
type: free
file_type: pdf
file_size: "2.3 MB"
tags: [数据结构, 思维导图, 推荐]
---

资源描述...
```

然后将实际文件放到 `static/resources/` 对应目录。

### 更新知识图谱数据

#### 方式一：手动编辑 JSON

编辑 `static/data/knowledge-graph.json`：

```json
{
  "nodes": [
    {
      "id": "/docs/data-structure/ch06-sorting/quick-sort/",
      "label": "快速排序",
      "subject": "data-structure",
      "difficulty": 3,
      "prerequisites": ["递归", "分治"],
      "slug": "quick-sort"
    }
  ],
  "links": [
    {
      "source": "/docs/data-structure/ch06-sorting/quick-sort/",
      "target": "/docs/data-structure/ch04-tree/binary-tree-traversal/"
    }
  ]
}
```

#### 方式二：启用 Hugo 自动生成

取消注释 `config/_default/module.yaml` 中的 blox-tailwind 模块，然后在 `graph/_index.md` 中添加：

```html
{{ partial "knowledge-graph-data.html" . }}
```

## 页面说明

### 首页 (`/`)
- Hero 区域：标题 + 三大入口按钮
- 最近更新：最近 6 条知识点
- 热门资源：标记为"推荐"的资源

### 知识点 (`/docs/`)
- 左侧侧边栏：按科目分组，自动列出所有知识点
- 右侧内容区：Markdown 渲染，支持 KaTeX 公式 + C/C++ 代码高亮
- 顶部元信息：标签、难度星级、前置知识
- 底部：相关题目链接

### 刷题 (`/exam/`)
- 顶部筛选栏：按科目/难度/关键词筛选
- 题目卡片：显示来源、年份、难度
- 点击展开：查看完整题目和解析

### 知识图谱 (`/graph/`)
- 全屏力导向图：节点颜色代表不同科目
- 拖拽调整布局，滚轮缩放
- 单击节点：右侧弹出信息面板
- 双击节点：跳转到对应知识点
- 搜索框：按名称定位节点

### 资源 (`/resources/`)
- 卡片网格：显示标题、大小、标签
- 公开资源：直接下载（PDF 自动加水印）
- 高质量资源：在线预览

## 视觉效果

- **配色**：深色底 (#0d1117) + 蓝绿渐变 (#58d6c0 → #3b82f6)
- **水印**：页面浏览时显示半透明斜向文字水印，防截图
- **科目色**：数据结构(蓝绿) / 组成原理(琥珀) / 操作系统(紫) / 网络(蓝)

## 部署

### 方案一：独立仓库（推荐）

把 `cc408/` 目录初始化为独立 Git 仓库，推送到 GitHub，GitHub Pages 自动构建部署。

```bash
# 在 cc408 目录下初始化独立仓库
cd E:\programcc408\cc408
git init
git add -A
git commit -m "init"

# 推送到 GitHub（新建仓库 cycycy5464/cc408）
git remote add origin https://github.com/cycycy5464/cc408.git
git push -u origin main
```

GitHub 会自动检测 `.github/workflows/publish-cc408.yaml`，每次推送到 main 分支就自动构建部署。

访问地址：`https://cycycy5464.github.io/cc408/`

### 方案二：同一仓库子目录部署

如果你不想单独开一个仓库，可以把 `cc408/` 的内容合并到个人主页仓库中。需要修改构建流程：

1. 保留 `cc408/` 目录在 `E:\programcc408` 下
2. 修改 `.github/workflows/publish.yaml`，在构建主站点后额外构建 cc408
3. 将 cc408 的 `public/` 内容复制到 `public/cc408/`

### 本地预览

```bash
cd E:\programcc408\cc408
hugo server
# 打开 http://localhost:1313
```

### Netlify / Vercel

1. 连接 GitHub 仓库
2. 构建命令：`hugo --minify`
3. 输出目录：`public`

## 注意事项

1. **本地开发需要 Hugo Extended**，普通版不支持 SCSS
2. **知识图谱数据**默认使用手写的 JSON，新增知识点后需同步更新
3. **PDF 水印**需要在构建前运行 `python scripts/watermark-pdf.py`
4. **模块依赖**：GitHub Pages 部署时有 Go 环境可正常编译模块；本地开发已临时注释模块导入以跳过 Go 依赖
