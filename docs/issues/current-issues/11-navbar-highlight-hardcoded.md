# 问题 11：navbar.html 导航高亮硬编码 /cc408/

**等级**：🟡 低危
**文件位置**：`layouts/partials/navbar.html` 第 7-11 行

---

## 问题描述

```html
{{ if hasPrefix $current "/cc408/docs/" }}{{ $section = "docs" }}
{{ else if hasPrefix $current "/cc408/exam/" }}{{ $section = "exam" }}
```

- baseURL 一旦变更（例如移到根域名），导航高亮逻辑全部失效
- 硬编码的 `/cc408/` 前缀导致代码不可移植

## 修复方案

基于 `.Site.BaseURL` 动态拼接判断前缀，不要写死 `/cc408/`：

```html
{{ $base := urls.Parse .Site.BaseURL | trimRight "/" }}
{{ if hasPrefix $current $base }}{{ $current = $current | strings.TrimPrefix $base }}{{ end }}
{{ if hasPrefix $current "/docs/" }}{{ $section = "docs" }}
{{ else if hasPrefix $current "/exam/" }}{{ $section = "exam" }}
```

---

*状态：⬜ 待修复*
