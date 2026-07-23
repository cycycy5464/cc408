# 问题 12：resource-filter.js 搜索框无防抖

**等级**：🟡 低危
**文件位置**：`assets/js/resource-filter.js` 第 30 行

---

## 问题描述

```javascript
searchInput.addEventListener('input', filterCards); // 每次按键立即执行全量扫描
```

- 每次击键都执行 `querySelectorAll` + `textContent` 全文扫描，内容量大时有明显卡顿
- 中文输入法 composition 阶段会触发大量无效查询

## 修复方案

```javascript
function debounce(fn, delay) {
  var t;
  return function() { clearTimeout(t); t = setTimeout(fn, delay); };
}
searchInput.addEventListener('input', debounce(filterCards, 200));
```

---

*状态：⬜ 待修复*
