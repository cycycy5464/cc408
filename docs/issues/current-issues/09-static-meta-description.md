# 问题 9：全站 meta description 静态

**等级**：🟡 低危
**文件位置**：`layouts/_default/baseof.html` 第 7 行

---

## 问题描述

```html
<meta name="description" content="CC408 408考研知识整理平台 — 系统化知识整理 · 历年真题练习 · 可视化知识图谱">
```

- 所有页面（快速排序、TCP三次握手、死锁预防……）共用同一段描述
- 搜索引擎会因 duplicate meta 给这些页面降权
- SEO 完全失效

## 修复方案

```html
<meta name="description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Summary | plainify | truncate 150 }}{{ end }}">
```

---

*状态：⬜ 待修复*
