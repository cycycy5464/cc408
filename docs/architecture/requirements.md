# CC408 需求文档（历史对话汇总）

## 项目概述
CC408 是 408 考研（数据结构、计算机组成原理、操作系统、计算机网络）知识整理平台，独立 Hugo 站点，部署于 `https://cycycy5464.github.io/cc408/`。

## 三套体系 + 一套资源

### 体系1：知识点笔记（docs/）
- 按四门科目分目录：data-structure、computer-org、os、network
- 侧边栏文档布局（左侧 280px 固定 + 右侧 800px 内容区）
- 支持 KaTeX 数学公式、C/C++ 代码高亮
- 结构化 frontmatter：title、weight、tags、difficulty、prerequisites、subject、chapter、chapter_title、exam_points
- 每篇知识点底部关联题目链接
- 标签系统用于交叉筛选

### 体系2：题目/真题库（exam/）
- 按题型分类：choice（选择题）、application（应用题）、comprehensive（综合题）
- 顶部筛选栏：科目、难度、关键词搜索
- 题目卡片列表，点击展开解析
- 每题关联知识点链接
- frontmatter：type、subject、source、year、difficulty、tags、related_knowledge

### 体系3：知识图谱（graph/）
- 全屏 D3.js 力导向图页面
- 节点颜色按科目区分：数据结构(蓝绿)、计组(琥珀)、OS(紫)、网络(蓝)
- 交互：拖拽、缩放、点击弹出信息面板、双击跳转详情
- 搜索框定位节点
- 数据源：手动 JSON 或 Hugo 自动生成

### 一套资源（resources/）
- 卡片网格布局
- 公开资源（free）：带水印直接下载
- 高质量资源（premium）：在线预览，引导获取功能预留暂不实现

## 视觉设计约束
- 暗色底 (#0d1117) + 蓝绿渐变 (#58d6c0 → #3b82f6)
- 侧边栏背景 (#161b22)，卡片背景 (#1c2128)
- 字体：正文 Noto Sans SC/Inter，代码 JetBrains Mono，标题 Inter/Space Grotesk
- 首页：Hero 全屏 + 网格线/粒子动画背景 + 三个入口卡片（glassmorphism）
- 参考网站：csgraduates.com 的排版风格

## 水印系统
- 页面浏览水印：Canvas 半透明斜向重复文字，MutationObserver 防篡改
- 文档下载水印：PyMuPDF 处理 PDF 每页嵌入水印

## 已知问题（用户反馈）
- "前端写的非常糟糕 没有一点审美"
- "图标重叠"
- "首页空空"
- 需要全面重新设计前端

## 参考网站
- https://www.csgraduates.com/（暗色科技风、侧边栏文档布局、内容排版风格）
