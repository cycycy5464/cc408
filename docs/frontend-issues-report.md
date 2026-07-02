# CC408 前端问题报告

> 报告生成时间：2026-07-02
> 最后检查版本：当前项目状态

---

## 📋 问题概览

| 优先级 | 数量 | 问题类型 |
|--------|------|----------|
| 🔴 高 | 3 | 功能缺失、代码错误 |
| 🟡 中 | 7 | 体验优化、代码质量 |
| 🟢 低 | 10 | 视觉优化、性能优化 |

---

## 🔴 高优先级问题

### 问题 1：导航栏路径硬编码导致本地开发高亮失效

**描述**：导航栏路径检查硬编码了 `/cc408/` 前缀，在本地开发环境（没有子路径）时，导航高亮不工作。

**相关文件**：
- [layouts/partials/navbar.html](file:///e:\programcc408\cc408\layouts\partials\navbar.html#L7-L28)

**问题代码**：
```html
{{ if hasPrefix $current "/cc408/docs/" }}{{ $section = "docs" }}
{{ else if hasPrefix $current "/cc408/exam/408quiz/" }}{{ $section = "quiz" }}
{{ else if hasPrefix $current "/cc408/exam/" }}{{ $section = "exam" }}
{{ else if hasPrefix $current "/cc408/graph/" }}{{ $section = "graph" }}
{{ else if hasPrefix $current "/cc408/resources/" }}{{ $section = "resources" }}
```

**修复建议**：
使用 Hugo 的 `relURL` 或动态获取 baseURL，或者使用更灵活的路径匹配方式。

---

### 问题 2：水印文件缺失

**描述**：`watermark.html` 引用了 `js/watermark.js`，但该文件不存在。

**相关文件**：
- [layouts/partials/watermark.html](file:///e:\programcc408\cc408\layouts\partials\watermark.html#L3)
- [layouts/_default/baseof.html](file:///e:\programcc408\cc408\layouts\_default\baseof.html#L22)

**问题代码**：
```html
{{ if ne .Section "graph" }}
<script src="{{ "js/watermark.js" | relURL }}"></script>
{{ end }}
```

**修复建议**：
1. 创建缺失的 `static/js/watermark.js` 文件，或
2. 暂时注释掉这个引用，或
3. 移除水印功能

---

### 问题 3：资源过滤功能不完整

**描述**：`resource-filter.js` 依赖 `card-glass` 类的卡片，但在布局文件中没有看到这个类被使用。

**相关文件**：
- [assets/js/resource-filter.js](file:///e:\programcc408\cc408\assets\js\resource-filter.js#L18)
- [layouts/resources/list.html](file:///e:\programcc408\cc408\layouts\resources\list.html)（假设存在）

**问题代码**：
```javascript
var cards = document.querySelectorAll('.card-glass[data-subject]');
```

**修复建议**：
1. 检查资源列表页面是否正确实现了过滤器
2. 更新 JS 选择器以匹配实际的卡片类名
3. 或移除未使用的过滤器功能

---

## 🟡 中优先级问题

### 问题 4：移动端菜单点击后不自动关闭

**描述**：移动端点击菜单按钮打开导航后，点击菜单项不会自动关闭菜单。

**相关文件**：
- [layouts/partials/navbar.html](file:///e:\programcc408\cc408\layouts\partials\navbar.html#L3)
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss#L179-L182)

**修复建议**：
给移动端菜单项添加点击事件，点击后移除 `open` 类。

---

### 问题 5：缺少搜索功能

**描述**：配置中开启了搜索，但实际没有搜索实现。

**相关文件**：
- [config/_default/params.yaml](file:///e:\programcc408\cc408\config\_default\params.yaml#L33)
- [layouts/partials/navbar.html](file:///e:\programcc408\cc408\layouts\partials\navbar.html)

**修复建议**：
1. 集成 Hugo 的搜索功能，或
2. 集成第三方搜索服务（如 Algolia），或
3. 在配置中关闭 `show_search`

---

### 问题 6：知识图谱容器高度固定

**描述**：知识图谱高度固定，响应式体验不好。

**相关文件**：
- [assets/js/knowledge-graph.js](file:///e:\programcc408\cc408\assets\js\knowledge-graph.js#L8)
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss#L176)

**修复建议**：
使用相对单位（vh、%）或响应式布局，让图表根据屏幕尺寸自动调整。

---

### 问题 7：代码重复 - 科目映射硬编码

**描述**：多个文件中重复硬编码科目名称和图标。

**相关文件**：
- [layouts/_default/index.html](file:///e:\programcc408\cc408\layouts\_default\index.html#L18-L23)
- [layouts/docs/single.html](file:///e:\programcc408\cc408\layouts\docs\single.html#L9-L14)
- [assets/js/knowledge-graph.js](file:///e:\programcc408\cc408\assets\js\knowledge-graph.js#L10-L17)

**修复建议**：
创建 `data/subjects.yaml` 数据文件，在多个地方复用。

---

### 问题 8：模板中使用内联样式

**描述**：多个模板文件使用内联 `style` 属性，不利于维护。

**相关文件**：
- [layouts/_default/baseof.html](file:///e:\programcc408\cc408\layouts\_default\baseof.html#L24-L27)
- [layouts/exam/list.html](file:///e:\programcc408\cc408\layouts\exam\list.html#L7)
- [layouts/docs/single.html](file:///e:\programcc408\cc408\layouts\docs\single.html#L50-L52)

**修复建议**：
将内联样式移到 SCSS 文件中，使用 CSS 类。

---

### 问题 9：SCSS 格式不规范

**描述**：多个属性写在同一行，不利于阅读和维护。

**相关文件**：
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss#L24-L28)

**问题代码**：
```scss
--fs-h2: 1.6rem; --fs-h3: 1.25rem;
--fs-body: 1rem; --fs-sm: 0.875rem; --fs-xs: 0.75rem;
```

**修复建议**：
每个属性单独一行。

---

### 问题 10：缺少友好的错误处理

**描述**：知识图谱加载失败时的提示不够友好。

**相关文件**：
- [assets/js/knowledge-graph.js](file:///e:\programcc408\cc408\assets\js\knowledge-graph.js#L25-L29)

**修复建议**：
增加更详细的错误信息和恢复建议。

---

## 🟢 低优先级问题

### 问题 11：颜色对比度可以优化

**描述**：`--text-muted` 在深色背景上的对比度略低。

**相关文件**：
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss#L16)

**当前值**：
```scss
--text-muted: #5d6b7a;
```

**建议值**：
```scss
--text-muted: #7a8896;
```

---

### 问题 12：水印可能影响阅读体验

**描述**：水印虽然不透明度低，但长时间阅读可能造成干扰。

**相关文件**：
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss#L172)

**修复建议**：
1. 降低不透明度（如 `0.02`），或
2. 增加用户可关闭水印的选项

---

### 问题 13：缺少焦点状态样式

**描述**：按钮和链接的焦点状态不够明显，不利于键盘导航。

**相关文件**：
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss)

**修复建议**：
增加 `:focus-visible` 样式。

---

### 问题 14：知识图谱移动端体验差

**描述**：触摸操作没有优化，双击跳转在移动端可能不友好。

**相关文件**：
- [assets/js/knowledge-graph.js](file:///e:\programcc408\cc408\assets\js\knowledge-graph.js#L73-L75)

**修复建议**：
在移动端改为单击跳转，长按显示详情。

---

### 问题 15：没有图片优化

**描述**：项目中有很多图片，但没有压缩或响应式图片配置。

**相关文件**：
- [config/_default/hugo.yaml](file:///e:\programcc408\cc408\config\_default\hugo.yaml#L40-L43)
- [static/images/](file:///e:\programcc408\cc408\static\images)

**修复建议**：
1. 压缩图片
2. 使用 Hugo 的图片处理功能生成响应式图片

---

### 问题 16：缺少懒加载

**描述**：图片没有使用懒加载技术。

**修复建议**：
给图片添加 `loading="lazy"` 属性。

---

### 问题 17：缺少预加载策略

**描述**：KaTeX 等外部资源没有预加载。

**相关文件**：
- [layouts/_default/baseof.html](file:///e:\programcc408\cc408\layouts\_default\baseof.html#L9-L19)

**修复建议**：
给关键资源添加 `rel="preload"`。

---

### 问题 18：缺少分页功能

**描述**：内容列表没有分页，内容增多时会影响性能。

**相关文件**：
- [layouts/_default/index.html](file:///e:\programcc408\cc408\layouts\_default\index.html#L40-L67)
- [config/_default/hugo.yaml](file:///e:\programcc408\cc408\config\_default\hugo.yaml#L28-L29)

**修复建议**：
实现 Hugo 的分页功能。

---

### 问题 19：标签页面可能缺失

**描述**：导航栏有标签链接，但可能没有对应的实现。

**相关文件**：
- [config/_default/menus.yaml](file:///e:\programcc408\cc408\config\_default\menus.yaml#L18-L20)
- [layouts/_default/taxonomy.html](file:///e:\programcc408\cc408\layouts\_default\taxonomy.html)
- [layouts/_default/terms.html](file:///e:\programcc408\cc408\layouts\_default\terms.html)

**修复建议**：
检查并完善标签页面模板。

---

### 问题 20：卡片间距在小屏幕可以优化

**描述**：移动端卡片间距可以进一步调整。

**相关文件**：
- [assets/css/custom.scss](file:///e:\programcc408\cc408\assets\css\custom.scss#L177-L188)

---

## 📝 修复建议路线图

### 第一阶段（立即修复）
1. [ ] 问题 1：修复导航栏路径硬编码
2. [ ] 问题 2：处理水印文件缺失
3. [ ] 问题 3：完善或移除资源过滤功能

### 第二阶段（本周内）
4. [ ] 问题 4：移动端菜单自动关闭
5. [ ] 问题 7：提取科目数据到单独文件
6. [ ] 问题 8：移除内联样式
7. [ ] 问题 9：格式化 SCSS

### 第三阶段（本月内）
8. [ ] 问题 5：添加搜索功能
9. [ ] 问题 6：优化知识图谱响应式
10. [ ] 问题 10-20：其他优化

---

## 🔍 检查清单

修复完成后，请检查：
- [ ] 本地开发环境导航高亮正常
- [ ] 所有 JS 引用的文件都存在
- [ ] 所有功能正常工作
- [ ] 移动端体验良好
- [ ] 代码符合项目规范
- [ ] 页面加载速度正常

---

*报告结束*
