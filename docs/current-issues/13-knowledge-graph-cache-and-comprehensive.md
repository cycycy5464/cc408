# 问题 13：知识图谱综合题知识球无法跳转 + 脚本强缓存旧版

**等级**：🟠 中危
**关联问题**：`04-knowledge-graph-url-bug.md`（节点跳转链接 404，链接还原修复已先落地）
**日期**：2026-07-16

---

## 任务背景

在 `04` 号问题修复（节点 id 还原为原始链接、双击跳转使用 `window.location.href = d.id`）之后，用户仍反馈：

> 双击综合题知识球无法跳转 KG：`filtered 1 invalid links`
> `t @ knowledge-graph.min.js:1` → `B @ ...` → `(匿名) @ ...` → `d3.v7.min.js:2`

错误栈与修复前**完全一致**，且浏览器一直加载缓存的旧脚本。

---

## 根因分析

### 根因 1：脚本未加指纹，浏览器强缓存旧版（关键）

`layouts/graph/list.html` 中脚本构建只做了 `Minify`，**没有 `Fingerprint`**：

```go
{{ $kg := resources.Get "js/knowledge-graph.js" | resources.ExecuteAsTemplate "knowledge-graph.js" . | resources.Minify }}
<script src="{{ $kg.RelPermalink }}"></script>
```

产物文件名恒为 `knowledge-graph.min.js`。即便新版脚本（含链接还原逻辑，已核实 `t`=renderGraph、`B`=handleNodeClick）早已编译进 `public/`，浏览器仍加载缓存的旧版，导致错误栈原样复现。

### 根因 2：综合题知识球下钻为空

`getKpLevel` 在构造知识球节点时，对知识球的题目计数**未按题型（qtype）过滤**：综合题科目下会列出只含选择题的知识球。双击下钻到 `getQuestionLevel` 时按 `comprehensive` 过滤，结果为空 → 表现为“无法跳转 / filtered invalid links”。

---

## 修复方案

### 修复 1：脚本加指纹，破除强缓存

`layouts/graph/list.html`：

```go
{{ $kg := resources.Get "js/knowledge-graph.js" | resources.ExecuteAsTemplate "knowledge-graph.js" . | resources.Minify | resources.Fingerprint }}
<script src="{{ $kg.RelPermalink }}" integrity="{{ $kg.Data.Integrity }}"></script>
```

文件名随内容生成哈希（如 `knowledge-graph.min.239151….js`），并带 `integrity` 校验。旧的静态名 `knowledge-graph.min.js` 已删除，不再被引用。用户下次访问即拿到修复版。

### 修复 2：`getKpLevel` 按题型过滤知识球

`assets/js/knowledge-graph.js` 的 `getKpLevel`：

```javascript
Object.keys(kps).forEach(function (kp) {
  if (searchQ && kp.toLowerCase().indexOf(searchQ) < 0) return;
  // 只统计当前题型(qtype)的题目：避免显示只含其它题型的“死”知识球，
  // 否则双击下钻到题目层会因题型不匹配而为空，表现为“无法跳转”。
  var count = 0;
  kps[kp].forEach(function (f) {
    var q = nav.questions[f];
    if (!q) return;
    var qt = (q.number <= 40 || q.number === undefined) ? 'selection' : 'comprehensive';
    if (qt === qtype) count++;
  });
  if (count === 0) return;
  nodes.push({
    id: 'kp-' + kp + '-' + year + '-' + subject + '-' + qtype,
    label: kp,
    type: 'kp',
    subject: subject,
    meta: kp,
    _parentYear: year,
    _parentSubject: subject,
    _parentQtype: qtype,
    count: count
  });
});
```

题型下无题的知识球直接不显示，杜绝双击下钻空白的“死球”。

---

## 验证

- `hugo --gc` 构建成功，无报错、无 lint 错误。
- `public/graph/index.html` 已引用带指纹的新脚本并带 `integrity` 属性。
- 已删除不再引用的旧 `public/knowledge-graph.min.js`。

### 用户侧复测步骤

1. **强制刷新**（Ctrl+F5）或清除浏览器缓存一次，确保加载到新哈希脚本。
2. 进入“综合题 → 科目”：此时只会显示确实含综合题的知识球。
3. 双击知识球 → 正常下钻到题目球；再双击题目球 → 在新标签打开题页。
4. 控制台不再出现 `missing` / `filtered invalid links` 报错。

---

## 待办（可选增强）

- 若希望**双击综合题知识球在仅含一道题时直接打开题页**（跳过题目层），可再加一层“单题直达”逻辑。

*状态：✅ 已修复*
