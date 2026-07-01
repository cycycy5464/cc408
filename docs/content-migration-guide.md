# 考研杂货铺 → cc408 内容搬运方法

## 文件夹结构
- `D:\内容整理\考研杂货铺\` — 原始资源
  - `数据结构\` — 详细笔记（含 .assets/ 配图目录）
  - `组成原理\`
  - `操作系统\`
  - `计算机网络\`
  - `知识点\按章节\` — 精简版知识点
  - `知识点\按主题\`
  - `题目\` — 各科习题
  - `images\` — 全局共用配图（SVG+PNG）

## 搬运流程

### 1. 复制源文件到项目临时目录
```bash
powershell -Command 'Copy-Item "D:\内容整理\考研杂货铺\{科目}\*.md" "E:\programcc408\cc408\_tmp\{科目}_source\" -Force'
```

### 2. 运行转换脚本
使用 `scripts/convert-{subject}-content.py` 批量处理：
- **添加 frontmatter**（title, weight, tags, difficulty, subject, chapter）
- **移除原始 H1 标题**（`# 标题`），用 frontmatter 的 title 替代
- **移除优先级标记**（如 `🔥 高优先级`）
- **4-space 缩进代码块 → ```c fenced 代码块**
- **图片路径修正**：
  - `![](../images/xxx.svg)` → `![](/images/docs/{subject}/xxx.svg)`
  - `![alt](filename.assets/image.png)` → `![](/images/docs/{subject}/image.png)`

### 3. 复制图片素材
```bash
python -c "
遍历 {科目} 下 .assets/ 目录和 images/ 目录
所有图片 → static/images/docs/{subject}/
"
```

### 4. 清理冲突文件
移除旧版已有知识点（避免重复路径）。

### 5. 提交
```bash
git add cc408/content/docs/{subject}/
git add cc408/static/images/docs/{subject}/
git commit -m "feat: migrate {subject} chapters"
```

## 科目对照表
| 本地目录 | cc408 subject | 章节数 |
|----------|--------------|--------|
| 数据结构 | data-structure | 8 |
| 组成原理 | computer-org | 7 |
| 操作系统 | os | 6 |
| 计算机网络 | network | 6 |
