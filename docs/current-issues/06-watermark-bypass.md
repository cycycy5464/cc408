# 问题 6：水印保护极易绕过

**等级**：🟠 中危
**文件位置**：`assets/js/watermark.js` 第 23 行 & 第 51 行

---

## 问题描述

```javascript
ctx.fillStyle = 'rgba(255, 255, 255, 0.04)'; // 透明度仅 4%，截图后几乎不可见

// Observer 只监听 childList（节点增删）
observer.observe(document.body, { childList: true, subtree: true });
// 直接改 style.display='none' 完全绕过，不触发 Observer
```

- **视觉上**：opacity: 0.04 几乎透明，截图后水印肉眼难以识别。
- **绕过上**：Observer 只监听子节点增删，在 DevTools 中修改 #cc408-watermark 的 style 属性可完全绕过，Observer 不会触发。

## 改善方案（无法根本杜绝，但可提高门槛）

```javascript
// 同时监听属性变更
observer.observe(document.body, {
  childList: true, subtree: true,
  attributes: true,
  attributeFilter: ['style', 'class']
});
// 透明度提高到至少 0.08~0.12
ctx.fillStyle = 'rgba(255, 255, 255, 0.10)';
```

---

*状态：⬜ 待修复*
