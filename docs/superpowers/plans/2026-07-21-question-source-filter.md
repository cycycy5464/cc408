# 题目库页源码筛选 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 在 `/question/` 页面添加三级联动的题源筛选器（全部/真题/模拟题/课后题），替代当前仅支持年份+科目的扁平筛选

**Architecture:** 修改 `question-card.html` 部分添加 `data-source`/`data-set` 属性，重写 `list.html` 模板的筛选器 UI 和 JS 逻辑

**Tech Stack:** Hugo templating + vanilla JavaScript (no external deps)

---

### Task 1: 修改 question-card.html 添加 data-source 和 data-set

**Files:**
- Modify: `layouts/partials/question-card.html:18`

**变更：** 在 card 的 data-* 属性中新增 `data-source` 和 `data-set`，供 JS 筛选用

- [ ] **Step 1: 编辑 question-card.html**

在 `data-type` 行后添加 `data-source` 和 `data-set`：

```html
    data-type="{{ $page.Params.question_type }}"
    data-source="{{ $page.Params.source }}"
    data-set="{{ with $page.Params.set }}{{ . }}{{ end }}">
```

注意保持 `data-chapter` 的现有逻辑（对于课后题，从 title 前缀提取章节名；对于真题/模拟题，它的值无实际用途但不影响筛选）。

- [ ] **Step 2: 验证 Hugo 编译不报错**

Run: `hugo` (should build without errors)

---

### Task 2: 重写 list.html — 模板部分（无 JS）

**Files:**
- Modify: `layouts/question/list.html`

**变更：**
1. 移除 `where "Params.source" "!=" "课后题"` 过滤器，包含全部题目
2. 添加题源 `<select>` 作为主筛选器（全部 / 408真题 / 模拟题 / 课后题）
3. 动态辅助筛选器：年份（真题时）、卷号（模拟题时）、章节（课后题时）
4. 保留科目、题型、搜索筛选器（全部可见）
5. 筛选器控件使用 class `filter-bar`（已在 custom.scss:273 中定义）

- [ ] **Step 1: 编辑 list.html**

替换完整内容：

```html
{{ define "main" }}
{{ partial "back-button.html" . }}
{{ $qpages := where .Site.RegularPages "Section" "question" }}
<div class="content-area content-area-wide">
  <h1>{{ .Title }}</h1>
  {{ .Content }}

  <div class="filter-bar question-toolbar">
    <select id="filter-source" data-filter="source">
      <option value="">全部题源</option>
      <option value="408真题">408真题</option>
      <option value="模拟题">模拟题</option>
      <option value="课后题">章节习题</option>
    </select>
    <select id="filter-exam-year" data-filter="exam-year" class="source-dependent source-exam">
      <option value="">全部年份</option>
      {{ range seq 2009 2026 }}<option value="{{ . }}">{{ . }}</option>{{ end }}
    </select>
    <select id="filter-set" data-filter="set" class="source-dependent source-simulate">
      <option value="">全部卷</option>
      {{ range seq 1 8 }}<option value="{{ . }}">第{{ . }}套</option>{{ end }}
    </select>
    <select id="filter-subject" data-filter="subject">
      <option value="">全部科目</option>
    </select>
    <select id="filter-chapter" data-filter="chapter" class="source-dependent source-exercise">
      <option value="">全部章节</option>
    </select>
    <select id="filter-type" data-filter="type">
      <option value="">全部题型</option>
      <option value="choice">选择题</option>
      <option value="comprehensive">解答题</option>
    </select>
    <input type="text" id="filter-search" data-filter="search" placeholder="搜索题目…">
  </div>

  <div class="question-grid" id="question-grid">
    {{ range $qpages.ByParam "number" }}{{ partial "question-card.html" . }}{{ end }}
  </div>

  <div class="border-top-section">
    <a href="{{ "exam/" | relURL }}" class="btn btn-ghost">← 返回刷题中心</a>
  </div>
</div>

<style>
.question-toolbar { display: flex; gap: .75rem; flex-wrap: wrap; align-items: center; padding: 1rem; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); margin-bottom: 1.5rem; }
.question-toolbar select, .question-toolbar input { padding: .45rem .75rem; background: var(--bg-card); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: var(--fs-sm); font-family: var(--font-body); }
.question-toolbar input { flex: 1; min-width: 180px; }
.question-toolbar select:focus, .question-toolbar input:focus { outline: none; border-color: var(--accent); }
.source-dependent { display: none; }
.source-dependent.visible { display: inline-block; }
</style>

<script>
(function() {
  // ... (JS in Task 3)
})();
</script>
{{ end }}
```

- [ ] **Step 2: 验证 Hugo 编译不报错**

Run: `hugo` (build)

---

### Task 3: 重写 list.html — JS 筛选逻辑

**Files:**
- Modify: `layouts/question/list.html` (JS 部分)

**变更：** 实现完整的级联筛选逻辑：
- `switchSource()`: 切换题源时显示/隐藏对应的辅助筛选器（year/set/chapter）
- `populateSubject()`: 根据当前题源加载可见题目的科目列表
- `populateChapter()`: 课后题模式下，根据选定科目加载章节列表
- `filter()`: 综合筛选（source + year/set/chapter + subject + type + search）

- [ ] **Step 1: 替换 list.html 中 `<script>` 块**

```javascript
(function() {
  const grid = document.getElementById('question-grid');
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll('.question-card'));
  const sourceSel = document.getElementById('filter-source');
  const examYearSel = document.getElementById('filter-exam-year');
  const setSel = document.getElementById('filter-set');
  const subjSel = document.getElementById('filter-subject');
  const chapSel = document.getElementById('filter-chapter');
  const typeSel = document.getElementById('filter-type');
  const search = document.getElementById('filter-search');

  // ---- UI visibility ----
  function switchSource() {
    const v = sourceSel.value;
    document.querySelectorAll('.source-dependent').forEach(function(el) {
      el.classList.toggle('visible', el.classList.contains('source-' +
        (v === '408真题' ? 'exam' : v === '模拟题' ? 'simulate' : v === '课后题' ? 'exercise' : 'none')));
    });
    if (v !== '课后题') chapSel.value = '';
    if (v !== '408真题') examYearSel.value = '';
    if (v !== '模拟题') setSel.value = '';
    populateSubject();
    filter();
  }

  // ---- Populate subjects dynamically ----
  function populateSubject() {
    const sk = sourceSel.value;
    const cur = subjSel.value;
    subjSel.innerHTML = '<option value="">全部科目</option>';
    const seen = {};
    cards.forEach(function(c) {
      if (sk && c.dataset.source !== sk) return;
      const v = c.dataset.subject;
      if (v && !seen[v]) { seen[v] = true;
        const o = document.createElement('option');
        o.value = v; o.textContent = c.dataset.subjectName || v;
        subjSel.appendChild(o);
      }
    });
    subjSel.value = cur;
    if (!subjSel.value) subjSel.value = '';
  }

  // ---- Populate chapters (for 课后题) ----
  function populateChapter() {
    const sk = sourceSel.value;
    if (sk !== '课后题') return;
    const cur = chapSel.value;
    chapSel.innerHTML = '<option value="">全部章节</option>';
    const seen = {};
    cards.forEach(function(c) {
      if (c.dataset.source !== '课后题') return;
      if (subjSel.value && c.dataset.subject !== subjSel.value) return;
      const v = c.dataset.chapter;
      if (v && !seen[v]) { seen[v] = true;
        const o = document.createElement('option');
        o.value = v; o.textContent = c.dataset.chapterName || v;
        chapSel.appendChild(o);
      }
    });
    chapSel.value = cur;
    if (!chapSel.value) chapSel.value = '';
  }

  // ---- Main filter ----
  function filter() {
    const sk = sourceSel.value, ey = examYearSel.value, st = setSel.value,
          sj = subjSel.value, ch = chapSel.value,
          t = typeSel.value, q = search.value.toLowerCase();
    cards.forEach(function(c) {
      const matchSource = !sk || c.dataset.source === sk;
      // For exam questions, years is a comma-separated list like "2009"
      const matchYear = !ey || (c.dataset.year || '').split(',').indexOf(ey) >= 0;
      const matchSet = !st || c.dataset.set === st;
      const matchSubj = !sj || c.dataset.subject === sj;
      const matchChap = !ch || c.dataset.chapter === ch;
      const matchType = !t || c.dataset.type === t;
      const matchSearch = !q || c.textContent.toLowerCase().includes(q);
      c.style.display = (matchSource && matchYear && matchSet && matchSubj && matchChap && matchType && matchSearch) ? 'block' : 'none';
    });
  }

  // ---- Event wiring ----
  sourceSel.addEventListener('change', switchSource);
  examYearSel.addEventListener('change', filter);
  setSel.addEventListener('change', filter);
  subjSel.addEventListener('change', function() { populateChapter(); filter(); });
  chapSel.addEventListener('change', filter);
  typeSel.addEventListener('change', filter);
  search.addEventListener('input', filter);

  // ---- Init ----
  switchSource();
})();
```

- [ ] **Step 2: 验证 Hugo 编译不报错**

Run: `hugo`

---

### Task 4: 验证构建与功能

**Files:**
- Verify: `layouts/question/list.html`, `layouts/partials/question-card.html`

- [ ] **Step 1: 完整构建**

Run: `hugo`

Expected: Build succeeds in < 120s, no errors or warnings.

- [ ] **Step 2: 启动开发服务器并手动验证**

Run: `hugo server` then open `http://localhost:1313/cc408/question/`

验证清单：
1. 默认显示全部题源，包含真题 + 模拟题 + 课后题的所有卡片
2. 选择"408真题" → 年份下拉出现，科目列表只显示真题科目，筛选正常
3. 选择"模拟题" → 卷号下拉出现，科目只显示模拟题科目
4. 选择"章节习题" → 章节下拉出现，科目只显示课后题科目
5. 切换题源时，旧的辅助筛选值被清空
6. 搜索框正常过滤

- [ ] **Step 3: 如果发现问题，回退并修复**
