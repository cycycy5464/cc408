# 问题 4：knowledge-graph.js 节点跳转链接全部404

**等级**：🟠 中危
**文件位置**：`assets/js/knowledge-graph.js` 第 62-69 行

---

## 问题描述

```javascript
// 生产环境 d.id = "/cc408/docs/data-structure/xxx/"
var parts = d.id.replace('/cc408/', '').split('/').filter(Boolean);
document.getElementById('info-link').href = '/' + parts.join('/') + '/';
// 结果: "/docs/data-structure/xxx/" ← 丢失了 /cc408 前缀！

// 双击跳转同样的 bug
window.location.href = '/' + parts.join('/') + '/'; // ❌
```

- 所有知识图谱节点的跳转链接在生产环境（baseURL = /cc408/）下都会跳到 404。
- 本地开发（无 baseURL 前缀）则正常，形成开发/生产行为不一致的隐性 Bug。

## 修复方案

```javascript
// 在 Hugo 模板中注入 baseURL
var BASE_URL = "{{ .Site.BaseURL }}";
// JS 中直接使用节点原始 id
window.location.href = d.id;
```

---

*状态：⬜ 待修复*
