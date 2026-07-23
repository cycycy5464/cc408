# 问题 10：favicon.ico 路径不跟随 baseURL

**等级**：🟡 低危
**文件位置**：`layouts/_default/baseof.html` 第 8 行

---

## 问题描述

```html
<link rel="icon" href="/favicon.ico" type="image/x-icon">
```

- 站点部署在 `/cc408/` 子路径，`/favicon.ico` 会指向根域名，不是站点的 favicon
- 浏览器会请求 `https://cycycy5464.github.io/favicon.ico` 而非 `https://cycycy5464.github.io/cc408/favicon.ico`

## 修复方案

```html
<link rel="icon" href="{{ "favicon.ico" | relURL }}" type="image/x-icon">
```

---

*状态：⬜ 待修复*
