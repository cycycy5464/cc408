# 问题 5：JSON.parse 无异常处理

**等级**：🟠 中危
**文件位置**：`assets/js/knowledge-graph.js` 第 22 行

---

## 问题描述

```javascript
var data = JSON.parse(script.textContent); // 无 try/catch
if (!data.nodes || !data.nodes.length) return;
```

- 如果 Hugo 生成的 JSON 因模板 bug 或特殊字符格式不合法，JSON.parse 会直接抛出异常。
- 整个知识图谱页面的 JS 全部崩溃，且无任何用户提示。

## 修复方案

```javascript
try {
  var data = JSON.parse(script.textContent);
} catch(e) {
  console.error('知识图谱数据解析失败:', e);
  container.innerHTML = '<p style="color:red">图谱数据加载失败，请刷新重试</p>';
  return;
}
```

---

*状态：⬜ 待修复*
