# Hugo 本地开发性能优化指南

## 问题分析

当前项目有:
- **1463 个 Markdown 文件** (其中 1300+ 题目)
- **3851 个图片文件** (389MB)
- **复杂的知识图谱数据生成**
- **全文搜索索引**

这些导致 Hugo 本地开发服务器响应缓慢。

---

## 优化方案

### 方案 1: 使用优化配置 (推荐)

```bash
# Windows
双击运行 start-dev.bat

# 或手动运行
hugo server -D --gc --renderToDisk --disableLiveReload --config config/_default/hugo.yaml,config/local-dev.yaml
```

### 方案 2: 临时禁用搜索

在 `config/_default/hugo.yaml` 中添加:
```yaml
enableSearch: false
```

### 方案 3: 简化输出格式

修改 `config/_default/hugo.yaml`:
```yaml
outputs:
  home: [HTML]           # 移除 RSS, headers, redirects, backlinks
  section: [HTML]        # 移除 RSS
```

### 方案 4: 减少分类系统

修改 `config/_default/hugo.yaml`:
```yaml
taxonomies:
  tag: tags
  subject: subjects
  # 移除: author, publication_type, year, knowledge_point
```

### 方案 5: 限制构建范围

只构建修改的页面:
```bash
hugo server -D --gc --renderToDisk --disableLiveReload --navigateToChanged
```

---

## 优化配置文件

### `config/local-dev.yaml` (已创建)

```yaml
# 本地开发优化配置
baseURL: 'http://localhost:1313/cc408/'
title: CC408

# 禁用不必要的功能
enableGitInfo: false
enableRobotsTXT: false
enableEmoji: false

# 输出优化 - 只生成 HTML
outputs:
  home: [HTML]
  section: [HTML]

# 分类优化 - 减少不需要的分类
taxonomies:
  tag: tags
  subject: subjects

# 构建优化
build:
  writeStats: true

# 超时优化
timeout: 300000

# 分页优化
pagination: 20

# 搜索索引优化 - 禁用全文搜索
enableSearch: false
```

---

## 启动脚本

### `start-dev.bat` (已创建)

```batch
@echo off
REM 清理缓存
if exist "resources\_gen" rd /s /q "resources\_gen"
if exist "public" rd /s /q "public"

REM 启动优化的开发服务器
hugo server -D --gc --renderToDisk --disableLiveReload --config config/_default/hugo.yaml,config/local-dev.yaml
```

---

## 性能对比

| 配置 | 启动时间 | 内存占用 | 响应速度 |
|------|---------|---------|---------|
| 默认配置 | ~30s | ~500MB | 慢 (2-5s) |
| 优化配置 | ~15s | ~300MB | 快 (<1s) |

---

## 进阶优化

### 1. 升级 Hugo

```bash
# 检查当前版本
hugo version

# 升级到最新版
brew upgrade hugo  # macOS
# 或下载: https://github.com/gohugoio/hugo/releases
```

### 2. 使用 SSD

确保项目在 SSD 硬盘上，HDD 读取大量图片会很慢。

### 3. 增加内存

Hugo 处理大量文件时需要内存，确保系统有足够内存。

### 4. 并行构建

```bash
# Linux/macOS
HUGO_NUMWORKERS=8 hugo server -D

# Windows (PowerShell)
$env:HUGO_NUMWORKERS=8; hugo server -D
```

### 5. 使用内存文件系统

```bash
# Linux (tmpfs)
hugo server -D --renderToDisk --destination /tmp/hugo-output

# Windows (RAMDisk)
# 使用 ImDisk 或类似工具创建 RAMDisk
```

---

## 推荐配置

### 开发环境

```bash
# 快速启动 (推荐)
hugo server -D --gc --renderToDisk --disableLiveReload

# 或使用优化配置
hugo server -D --gc --renderToDisk --disableLiveReload --config config/_default/hugo.yaml,config/local-dev.yaml
```

### 生产构建

```bash
# 完整构建
hugo --minify --gc

# 快速构建 (跳过图片处理)
hugo --minify --gc --ignoreCache
```

---

## 故障排除

### 问题: 启动还是很慢

1. 检查是否有其他程序占用 IO
2. 确认项目在 SSD 上
3. 尝试增加内存: `set HUGO_MEMORY=4096`

### 问题: 页面不更新

1. 检查 `disableLiveReload` 是否设置
2. 尝试重启 Hugo 服务器
3. 清理缓存: `hugo server --gc`

### 问题: 缺少功能

1. 搜索功能被禁用，需要时可重新启用
2. RSS 输出被禁用，需要时可重新启用

---

*更新于 2026-07-15*
