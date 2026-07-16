# 问题 14：知识图谱「按科目」视图下点「卷」显示为空

**等级**：🟠 中危
**关联问题**：`13-knowledge-graph-cache-and-comprehensive.md`（缓存 + 综合题下钻）
**日期**：2026-07-16

---

## 用户现象

> 模拟题在知识图谱中点击科目 → 点击模拟卷，显示为空。

初步怀疑“模拟题没有科目标签”，经数据核查**不成立**。

---

## 数据核查：模拟题有科目标签

`static/mapping/question-kp-mapping.json` 中 `source === '模拟题'` 共 **376** 道，科目分布正常：

```
network:        72
computer-org:  104
data-structure:104
os:             96
```

每条都带 `subject` 字段（示例 `"subject":"network"`、`"set":1`、`"year":"模拟卷1"`）。故根因**不在标签缺失**。

---

## 真正根因：subject 视图下导航状态被清空

复现路径（「按科目」视图，`state.view === 'subject'`）：

1. `getSubjectLevel` → 点击科目 → `f = {subject, …}` → `getSubjectYearsLevel` 展示「卷1/卷2…」节点（`id: 'year-'+y+'-'+subject`）。
2. 点击「卷」节点时，`handleNodeClick` 的 `year` 分支**无条件清空 `state.focus.subject = null`**（`knowledge-graph.js` 原 914-919 行）。
3. 此时 `f = {year, qtype:null, subject:null}`，回到 `getExamViewData` 层级分发：
   - `f.year !== null && f.qtype === null && f.subject === null` 这一分支要求 `state.view === 'year'` 才返回 `getYearQtypeLevel`，而当前是 `subject` 视图；
   - 其后没有「`subject + year` 且无 `qtype`」的匹配分支 → 直接 `return {nodes:[], links:[]}` → 显示“暂无数据”。

即：subject 视图下点「卷」把科目抹掉，而层级分发器对“已选科目+已选卷”组合无处理分支 → 空。

> 该缺陷在**真题的 subject 视图**下同样存在，并非模拟题专属。

---

## 修复方案

### 1. `handleNodeClick` 的 `year` / `qtype` 分支：subject 视图下保留已选科目

```javascript
if (d.type === 'year') {
  state.focus.year = d.meta || d.label.replace('年', '');
  state.focus.qtype = null;
  state.focus.kp = null;
  // subject 视图下点击“卷/年份”时保留已选科目，继续在该科目下下钻；
  // year 视图下则清空科目（year→qtype→科目 的常规流程）。
  if (!(state.view === 'subject' && state.focus.subject)) {
    state.focus.subject = null;
  }
  renderGraph();
} else if (d.type === 'qtype') {
  state.focus.qtype = d.meta;
  state.focus.kp = null;
  // subject 视图下保留已选科目，否则下钻到 KP 层会因 subject 为空而空白
  if (!(state.view === 'subject' && state.focus.subject)) {
    state.focus.subject = null;
  }
  renderGraph();
}
```

### 2. `getExamViewData` 新增 `Level 1c` 分支

```javascript
// Level 1c: subject + year selected (subject view) -> show qtypes
if (f.subject !== null && f.year !== null && f.qtype === null && f.kp === null) {
  if (state.view === 'subject') return getSubjectYearQtypeLevel(nav, f.subject, f.year, searchQ);
}
```

### 3. 新增 `getSubjectYearQtypeLevel`：仅统计该「科目+卷」下存在的题型

与 `getYearQtypeLevel` 类似，但 `hasSel/hasCom` 只在该科目+卷的 KP 内统计，避免展示空题型节点；题型节点 id 沿用 `qtype-`+qtype+`-`+year，以衔接后续 `getKpLevel`（其 `qtype` 父节点约定同一 id）。

### 4. 面包屑「年份」动作按视图区分

subject 视图下点击年份面包屑回到“科目→卷”层（保留科目）；year 视图下清空科目。

---

## 修复后路径（subject 视图）

```
科目 → 卷(N) → 题型(选择题/综合题) → 知识点 → 题目
```

所有层级均有对应分支，不再返回空。

---

## 验证

- `hugo --gc` 构建成功（构建耗时较长，约 280s，因站点内容量较大）。
- `public/graph/index.html` 已引用新指纹脚本 `knowledge-graph.min.74599c5c….js` 并带 `integrity`。
- `assets/js/knowledge-graph.js` 无 lint 错误。

### 用户侧复测

强制刷新（Ctrl+F5）后：进入「按科目」视图 → 点某科目（如 数据结构）→ 点某模拟卷 → 应显示选择题/综合题 → 点题型显示知识点 → 点知识点显示题目。

*状态：✅ 已修复*
