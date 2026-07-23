# 问题 2：markup.goldmark.renderer.unsafe: true — XSS风险

**等级**：🔴 高危
**文件位置**：`config/_default/hugo.yaml` 第 54-55 行

---

## 问题描述

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true # ← 允许 Markdown 中渲染任意原始 HTML
```

- 此开关允许 Markdown 内容中嵌入任意原始 HTML，包括 `<script>` 标签。
- 只要有一篇内容被污染（来自外部来源的笔记、脚本转换生成的内容），任意 JS 都能注入进页面。
- 静态站点的 XSS 往往被低估——攻击者可劫持用户 session、利用 GitHub Pages 同源特性做进一步攻击。

## 修复方案

```yaml
markup:
  goldmark:
    renderer:
      unsafe: false # 改为 false，用 Hugo shortcode 替代内联 HTML
```

## 注意事项

修改后需要检查现有内容中是否有依赖内联 HTML 的部分，可能需要用 Hugo shortcode 替代。

---

*状态：⬜ 待修复*
