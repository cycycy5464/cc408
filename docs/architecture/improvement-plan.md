# CC408 前端改进方案

## 参考设计方向

基于 csgraduates.com 的暗色科技风，重构整体视觉体系。

## 配色体系（新）
```scss
$bg-primary:    #0a0e14;     // 更深的主背景
$bg-secondary:  #131820;     // 侧边栏/面板
$bg-card:       #1a1f2b;     // 卡片
$bg-hover:      #1e2532;     // hover 态
$accent:        #39bae6;     // 主强调色（蓝，从 teal 改为更科技感的蓝）
$accent2:       #95e6cb;     // 辅助强调（青绿，用于梯度）
$accent3:       #ff8f40;     // 暖色点缀（橙，用于标签/提示）
$text-primary:  #e6edf3;
$text-secondary:#8b949e;
$border-color:  #252b36;
```

## 排版体系
- 标题：Inter（粗体 700-900），H1 3rem / H2 1.8rem / H3 1.4rem
- 正文：Noto Sans SC（400 阅读 / 600 强调），16px/1.8 行高
- 代码：JetBrains Mono 14px/1.6 行高
- 数字/数据：JetBrains Mono（tablular-nums）

## 组件设计

### 导航栏
- 毛玻璃效果（backdrop-filter: blur(12px)）
- 当前页面高亮指示器（底部彩色条）
- 移动端汉堡菜单

### 首页 Hero
- 渐变网格背景动画（CSS Grid + radial-gradient 叠加）
- 大标题 + 副标题 + 三个功能入口卡片
- 卡片：半透明背景 + 玻璃态 + hover 发光边框
- 滚动提示箭头（CSS 动画）

### 知识点页面
- 左侧常驻侧边栏，按科目分组
- 树形目录可折叠，当前章节高亮
- 右侧内容区：良好的阅读排版（行高、段落间距、标题层级）
- 代码块：暗色背景 + 圆角 + 语言标签 + 复制按钮
- 难度星标和标签

### 题目页面
- 筛选栏：下拉 + 搜索 + 标签 pills
- 题目卡片：左侧彩色科目条 + 来源 + 难度
- 答案/解析折叠面板（details/summary 自定义样式）

### 知识图谱
- 全屏深色背景
- D3.js 力导向图，节点带光晕
- 搜索框在左上角，信息面板在右侧

### 资源区
- 卡片网格带缩略图占位
- 下载/预览按钮区分

## 技术改进清单

### P0 - 阻塞问题
1. **修复 CSS 不编译**：baseof.html 使用 Hugo pipes 编译 SCSS
2. **修复知识图谱不渲染**：重命名 graph/single.html → graph/list.html，或创建 list.html
3. **修复侧边栏为空**：使用 `File.Dir` 前缀匹配而非 `Section` 严格匹配

### P1 - 视觉
4. 重写整个 SCSS，建立统一的 token 系统
5. 首页 Hero 重新设计（网格背景 + 卡片入口）
6. 导航栏毛玻璃 + 活跃态指示
7. 统一卡片组件样式（整理内联 style 到 SCSS）
8. 响应式完善（navbar 移动端汉堡、文档页面栈叠）

### P2 - 功能
9. 添加 favicon
10. 添加 SEO meta 标签
11. 代码块复制按钮
12. 添加打印样式
13. 主题切换（暗色默认 + 可选亮色）

### P3 - 清理
14. 删除 assets/js/ 下的重复 JS 文件
15. 清理内联 `<style>` 块
16. 修复 Space Grotesk 字体引用
17. 添加 .gitignore hugo_stats.json
