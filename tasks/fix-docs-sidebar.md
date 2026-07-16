# 修复 docs 侧边混入 exam 页面 + 排序控制方案

## 问题分析

### 问题1：exam 页面混入 docs 侧边栏

**根因**：3 个模板使用 `where $.Site.RegularPages "Params.subject" $subject` 全局查询，没有按 Section 过滤。exam 页面（`subject: data-structure`）也被匹配。

**受影响文件**：

| 文件 | 行号 | 用途 |
|------|------|------|
| `layouts/docs/single.html` | 17 | 侧边栏导航链接 |
| `layouts/docs/list.html` | 15 | 知识点数量统计 |
| `layouts/_default/index.html` | 21 | 首页卡片数量统计 |

**受影响的 exam 页面**（`subject: data-structure`）：
- `content/exam/application/2023-q1.md`
- `content/exam/choice/2024-q5.md`
- `content/exam/exercise/data_structure/*.md`（11个文件）

**修复方案**：在 `where` 查询中增加 `Section "docs"` 过滤。

### 问题2：排序控制

**现状**：所有 docs 文件已有 `weight` 字段（0-28），Hugo 默认按 weight 升序排列。

---

## 修改计划

### 修改1：`layouts/docs/single.html` (line 17)

```diff
- {{ range where $.Site.RegularPages "Params.subject" $subject }}
+ {{ range sort (where (where $.Site.RegularPages "Section" "docs") "Params.subject" $subject) "Params.weight" }}
```

### 修改2：`layouts/docs/list.html` (line 15)

```diff
- {{ $count := len (where $.Site.RegularPages "Params.subject" .key) }}
+ {{ $count := len (where (where $.Site.RegularPages "Section" "docs") "Params.subject" .key) }}
```

### 修改3：`layouts/_default/index.html` (line 21)

```diff
- {{ $count := len (where $.Site.RegularPages "Params.subject" .key) }}
+ {{ $count := len (where (where $.Site.RegularPages "Section" "docs") "Params.subject" .key) }}
```

---

## 排序控制方案

### 方案A：使用现有 weight 字段（推荐，无需额外开发）

**操作方式**：修改 md 文件 frontmatter 中的 `weight` 值

```yaml
---
title: "链表"
weight: 6    # 数字越小越靠前
---
```

**优点**：
- 所有 docs 文件已有 weight 字段
- Hugo 原生支持，无需额外代码
- 版本控制友好（git 可追踪变更）

**缺点**：
- 需要手动编辑 md 文件
- 没有可视化界面

### 方案B：创建排序管理页面（可选增强）

创建一个 admin 页面，通过拖拽调整顺序，自动更新 md 文件的 weight。

**实现方式**：
1. 新增 `content/admin/sort-docs.md` + `layouts/admin/sort-docs.html`
2. 页面加载所有 docs 的 title/weight/path
3. 拖拽排序后，通过 JS 生成新的 weight 值
4. 保存时输出修改后的 frontmatter（需配合 Hugo Module 或构建脚本）

**优点**：可视化操作，直观
**缺点**：增加复杂度，需要额外维护

---

## 建议

**先实施方案A**（修改模板 + 使用现有 weight），验证效果后再决定是否需要方案B。

## 验证步骤

1. 运行 `hugo server -D`
2. 访问 `http://localhost:1313/cc408/docs/data-structure/ch00-intro/basic-concepts/`
3. 确认侧边栏不再显示 exam 页面
4. 确认知识点按 weight 升序排列
5. 检查首页卡片的"共 X 篇知识点"计数正确
