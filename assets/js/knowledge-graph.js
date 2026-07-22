// CC408 Knowledge Graph v2 — Multi-tab, drill-down, admin mode
(function () {
  'use strict';

  // Base URL from Hugo template (injected at build time)
  var BASE_URL = '{{ .Site.BaseURL }}';

  var container = document.getElementById('knowledge-graph');
  if (!container) { console.error('KG: #knowledge-graph not found'); document.body.insertAdjacentHTML('beforeend','<div style="color:red;padding:1rem">KG init error: container not found</div>'); return; }
  console.log('KG init OK');

  // ----- Constants -----
  var subjectColors = {
    'data-structure': '#58d6c0',
    'computer-org': '#f59e0b',
    'os': '#8b5cf6',
    'network': '#3b82f6',
    'exam': '#f0c040'
  };
  var subjectNames = {
    'data-structure': '数据结构',
    'computer-org': '组成原理',
    'os': '操作系统',
    'network': '计算机网络',
    'exam': '试题'
  };
  var subjectCodeMap = {
    '数据结构': 'data-structure',
    '组成原理': 'computer-org',
    '操作系统': 'os',
    '计算机网络': 'network'
  };
  // reverse of subjectNames
  var subjectNameFromCode = {
    'data-structure': '数据结构',
    'computer-org': '组成原理',
    'os': '操作系统',
    'network': '计算机网络'
  };

  var qtypeNames = {
    'selection': '选择题',
    'comprehensive': '综合题'
  };
  var qtypeCodes = {
    '选择题': 'selection',
    '综合题': 'comprehensive'
  };

  var nodeRadius = {
    'year': 20,
    'qtype': 18,
    'subject': 18,
    'kp': 14,
    'question': 10
  };

  // ----- State -----
  var state = {
    tab: 'docs',
    view: 'year',          // 'year' | 'subject' (exam/simulate only)
    focus: {
      year: null,
      qtype: null,
      subject: null,
      kp: null
    },
    breadcrumb: [],
    mapping: null,         // full mapping data
    config: null,          // current tab config
    source: '',            // '408真题' | '模拟题'
    currentNodes: [],
    currentLinks: [],
    searchQuery: '',
    adminMode: false,
    editTarget: null       // question file being edited
  };

  // ----- DOM refs -----
  var searchInput = document.getElementById('graph-search');
  var infoPanel = document.getElementById('node-info');
  var infoTitle = document.getElementById('info-title');
  var infoMeta = document.getElementById('info-meta');
  var infoTags = document.getElementById('info-tags');
  var infoLink = document.getElementById('info-link');
  var infoClose = document.getElementById('info-close');
  var breadcrumbEl = document.getElementById('graph-breadcrumb');
  var viewToggle = document.getElementById('graph-view-toggle');
  var yearNav = document.getElementById('graph-year-nav');
  var infoEdit = document.getElementById('info-edit');
  var kpEditor = document.getElementById('info-kp-editor');
  var kpAddInput = document.getElementById('kp-add-input');
  var kpAddBtn = document.getElementById('kp-add-btn');
  var kpSaveBtn = document.getElementById('kp-save-btn');
  var kpExportBtn = document.getElementById('kp-export-btn');

  // ----- Utility -----
  function subjectCode(name) {
    return subjectCodeMap[name] || name;
  }

  function subjectName(code) {
    return subjectNameFromCode[code] || code;
  }

  // 模拟题顶层维度取「整卷」：优先用 set 字段，否则从文件名/年份解析
  function parseSet(q) {
    var s = q.set;
    if (s !== undefined && s !== null && s !== '') return String(s);
    var lf = q.local_file || '';
    var m = lf.match(/simulate-(\d+)/);
    if (m) return m[1];
    var ym = (q.year || '').match(/(\d+)/);
    if (ym) return ym[1];
    return '0';
  }

  // 顶层节点文案：模拟题为「卷N」，真题为「N年」
  function topLabel(nav, y) {
    return (nav && nav.topIsSet) ? ('卷' + y) : (y + '年');
  }

  function getDataId(tab) {
    if (tab === 'docs') return 'graph-data-docs';
    if (tab === 'exam') return 'graph-data-exam';
    if (tab === 'simulate') return 'graph-data-simulate';
    return null;
  }

  // ----- Data loading -----
  function loadTabConfig(tab) {
    var dataId = getDataId(tab);
    if (!dataId) return null;
    var el = document.getElementById(dataId);
    if (!el) return null;
    try {
      return JSON.parse(el.textContent);
    } catch (e) {
      console.error('Parse error for', dataId, e);
      return null;
    }
  }

  function loadMapping(callback) {
    if (state.mapping) { callback(); return; }
    console.log('KG: loading mapping JSON from', BASE_URL + 'mapping/question-kp-mapping.json');
    var dataFile = BASE_URL + 'mapping/question-kp-mapping.json';
    fetch(dataFile)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        console.log('KG: mapping loaded, qIndex keys:', Object.keys(data.questionIndex||{}).length);
        state.mapping = data;
        callback();
      })
      .catch(function (err) {
        console.error('KG: Failed to load mapping:', err);
        container.innerHTML = '<p style="color:#8b949e;padding:2rem;text-align:center">⚠ 无法加载数据文件</p>';
      });
  }

  // ----- Navigation data builders -----
  function getQuestionsBySource(source) {
    if (!state.mapping) return {};
    var result = {};
    var idx = state.mapping.questionIndex || {};
    for (var file in idx) {
      if (idx[file].source === source) {
        result[file] = idx[file];
      }
    }
    return result;
  }

  function buildNavigation(source) {
    var questions = getQuestionsBySource(source);
    var yearsMap = {};
    var subjectsMap = {};
    var kpMap = {};

    for (var file in questions) {
      var q = questions[file];
      var year = (source === '模拟题') ? parseSet(q) : q.year;
      var subject = q.subject;
      var kps = q.knowledge_points || [];

      // Year index
      if (!yearsMap[year]) yearsMap[year] = {};
      if (!yearsMap[year][subject]) yearsMap[year][subject] = { kps: {}, count: 0 };
      yearsMap[year][subject].count += 1;

      // Subject index
      if (!subjectsMap[subject]) subjectsMap[subject] = {};
      if (!subjectsMap[subject][year]) subjectsMap[subject][year] = { kps: {}, count: 0 };
      subjectsMap[subject][year].count += 1;

      // KP index
      for (var kpi = 0; kpi < kps.length; kpi++) {
        var kp = kps[kpi];
        if (!kp) continue;

        // year -> subject -> kp
        if (!yearsMap[year][subject].kps[kp]) yearsMap[year][subject].kps[kp] = [];
        yearsMap[year][subject].kps[kp].push(file);

        // subject -> year -> kp
        if (!subjectsMap[subject][year].kps[kp]) subjectsMap[subject][year].kps[kp] = [];
        subjectsMap[subject][year].kps[kp].push(file);

        // KP global
        if (!kpMap[kp]) kpMap[kp] = { subjects: {}, years: [], questions: [] };
        if (!kpMap[kp].subjects[subject]) kpMap[kp].subjects[subject] = {};
        if (!kpMap[kp].subjects[subject][year]) kpMap[kp].subjects[subject][year] = [];
        kpMap[kp].subjects[subject][year].push(file);
        if (kpMap[kp].years.indexOf(year) < 0) kpMap[kp].years.push(year);
        kpMap[kp].questions.push(file);
      }
    }

    return {
      questions: questions,
      topIsSet: (source === '模拟题'),
      years: Object.keys(yearsMap).sort(),
      subjects: Object.keys(subjectsMap),
      yearsMap: yearsMap,
      subjectsMap: subjectsMap,
      kpMap: kpMap
    };
  }

  // ----- Get nodes & links for current state -----
  function getCurrentViewData() {
    if (state.tab === 'docs') return getDocsViewData();
    return getExamViewData();
  }

  function getDocsViewData() {
    var config = state.config;
    if (!config || !config.nodes) return { nodes: [], links: [] };
    var nodes = config.nodes;
    var links = config.links;
    if (state.searchQuery) {
      var q = state.searchQuery.toLowerCase();
      var matchedIds = {};
      nodes.forEach(function (n) {
        if (n.label && n.label.toLowerCase().indexOf(q) >= 0) {
          matchedIds[n.id] = true;
        }
      });
      nodes = nodes.filter(function (n) { return matchedIds[n.id]; });
      links = links.filter(function (l) {
        return matchedIds[l.source] && matchedIds[l.target];
      });
    }
    return { nodes: nodes, links: links };
  }

  function getExamViewData() {
    var nav = state._nav;
    if (!nav) return { nodes: [], links: [] };
    var searchQ = state.searchQuery.toLowerCase();
    var f = state.focus;

    // Determine level
    // Level 0: initial
    if (f.year === null && f.qtype === null && f.subject === null && f.kp === null) {
      if (state.view === 'year') return getYearLevel(nav, searchQ);
      else return getSubjectLevel(nav, searchQ);
    }
    // Level 1a: year selected -> show question types (year view)
    if (f.year !== null && f.qtype === null && f.subject === null && f.kp === null) {
      if (state.view === 'year') return getYearQtypeLevel(nav, f.year, searchQ);
    }
    // Level 1b: subject selected -> show years (subject view)
    if (f.subject !== null && f.year === null && f.qtype === null && f.kp === null) {
      if (state.view === 'subject') return getSubjectYearsLevel(nav, f.subject, searchQ);
    }
    // Level 1c: subject + year selected (subject view) -> show qtypes
    // 修复：subject 视图下点“卷/年份”后，若不清空科目则焦点变为 {subject, year}，
    // 此前没有任何分支匹配该组合，导致返回空（显示“暂无数据”）。
    if (f.subject !== null && f.year !== null && f.qtype === null && f.kp === null) {
      if (state.view === 'subject') return getSubjectYearQtypeLevel(nav, f.subject, f.year, searchQ);
    }
    // Level 2a: year + qtype selected -> show subjects
    if (f.year !== null && f.qtype !== null && f.subject === null && f.kp === null) {
      return getYearQtypeSubjectsLevel(nav, f.year, f.qtype, searchQ);
    }
    // Level 2b: subject selected in subject view -> show years (already handled above)
    // Level 3: year + qtype + subject selected -> show KPs
    if (f.year !== null && f.qtype !== null && f.subject !== null && f.kp === null) {
      return getKpLevel(nav, f.year, f.qtype, f.subject, searchQ);
    }
    // Level 4: year + qtype + subject + kp selected -> show questions
    if (f.year !== null && f.qtype !== null && f.subject !== null && f.kp !== null) {
      return getQuestionLevel(nav, f.year, f.qtype, f.subject, f.kp, searchQ);
    }
    return { nodes: [], links: [] };
  }

  // ----- View level builders -----
  function getYearLevel(nav, searchQ) {
    var nodes = [];
    var links = [];
    nav.years.forEach(function (y) {
      if (searchQ && y.indexOf(searchQ) < 0) return;
      nodes.push({
        id: 'year-' + y,
        label: topLabel(nav, y),
        type: 'year',
        subject: 'exam',
        meta: y
      });
    });
    return { nodes: nodes, links: links };
  }

  function getSubjectLevel(nav, searchQ) {
    var nodes = [];
    var links = [];
    nav.subjects.forEach(function (s) {
      var name = subjectName(s);
      if (searchQ && name.indexOf(searchQ) < 0) return;
      nodes.push({
        id: 'subj-' + s,
        label: name,
        type: 'subject',
        subject: s,
        meta: s
      });
    });
    return { nodes: nodes, links: links };
  }

  function getYearSubjectsLevel(nav, year, searchQ) {
    var nodes = [];
    var links = [];
    var subjects = nav.yearsMap[year];
    if (!subjects) return { nodes: [], links: [] };
    Object.keys(subjects).forEach(function (s) {
      var name = subjectName(s);
      if (searchQ && name.indexOf(searchQ) < 0) return;
      nodes.push({
        id: 'subj-' + s + '-' + year,
        label: name,
        type: 'subject',
        subject: s,
        meta: s,
        _parentYear: year,
        count: subjects[s].count
      });
      links.push({
        source: 'year-' + year,
        target: 'subj-' + s + '-' + year
      });
    });
    // Include year node
    nodes.push({
      id: 'year-' + year,
      label: topLabel(nav, year),
      type: 'year',
      subject: 'exam',
      meta: year
    });
    return { nodes: nodes, links: links };
  }

  function getSubjectYearsLevel(nav, subject, searchQ) {
    var nodes = [];
    var links = [];
    var years = nav.subjectsMap[subject];
    if (!years) return { nodes: [], links: [] };
    Object.keys(years).forEach(function (y) {
      if (searchQ && y.indexOf(searchQ) < 0) return;
      nodes.push({
        id: 'year-' + y + '-' + subject,
        label: topLabel(nav, y),
        type: 'year',
        subject: 'exam',
        meta: y,
        count: years[y].count
      });
      links.push({
        source: 'subj-' + subject,
        target: 'year-' + y + '-' + subject
      });
    });
    nodes.push({
      id: 'subj-' + subject,
      label: subjectName(subject),
      type: 'subject',
      subject: subject,
      meta: subject
    });
    return { nodes: nodes, links: links };
  }

  function getYearQtypeLevel(nav, year, searchQ) {
    var nodes = [];
    var links = [];
    var yData = nav.yearsMap[year];
    if (!yData) return { nodes: [], links: [] };
    var hasSel = false, hasCom = false;
    Object.keys(yData).forEach(function (s) {
      var kps = yData[s].kps || {};
      Object.keys(kps).forEach(function (kp) {
        kps[kp].forEach(function (f) {
          var q = nav.questions[f];
          if (!q) return;
          if (q.number <= 40 || q.number === undefined) { hasSel = true; }
          else { hasCom = true; }
        });
      });
    });
    nodes.push({
      id: 'year-' + year,
      label: topLabel(nav, year),
      type: 'year',
      subject: 'exam',
      meta: year
    });
    if (hasSel) {
      nodes.push({
        id: 'qtype-selection-' + year,
        label: '选择题',
        type: 'qtype',
        subject: 'exam',
        meta: 'selection',
        _parentYear: year
      });
      links.push({
        source: 'year-' + year,
        target: 'qtype-selection-' + year
      });
    }
    if (hasCom) {
      nodes.push({
        id: 'qtype-comprehensive-' + year,
        label: '综合题',
        type: 'qtype',
        subject: 'exam',
        meta: 'comprehensive',
        _parentYear: year
      });
      links.push({
        source: 'year-' + year,
        target: 'qtype-comprehensive-' + year
      });
    }
    return { nodes: nodes, links: links };
  }

  function getYearQtypeSubjectsLevel(nav, year, qtype, searchQ) {
    var nodes = [];
    var links = [];
    var yData = nav.yearsMap[year];
    if (!yData) return { nodes: [], links: [] };
    Object.keys(yData).forEach(function (s) {
      var name = subjectName(s);
      if (searchQ && name.indexOf(searchQ) < 0) return;
      var kps = yData[s].kps || {};
      var hasType = false;
      Object.keys(kps).forEach(function (kp) {
        kps[kp].forEach(function (f) {
          var q = nav.questions[f];
          if (!q) return;
          var qt = (q.number <= 40 || q.number === undefined) ? 'selection' : 'comprehensive';
          if (qt === qtype) { hasType = true; }
        });
      });
      if (hasType) {
        nodes.push({
          id: 'subj-' + s + '-' + year + '-' + qtype,
          label: name,
          type: 'subject',
          subject: s,
          meta: s,
          _parentYear: year,
          _parentQtype: qtype
        });
        links.push({
          source: 'qtype-' + qtype + '-' + year,
          target: 'subj-' + s + '-' + year + '-' + qtype
        });
      }
    });
    nodes.push({
      id: 'year-' + year,
      label: topLabel(nav, year),
      type: 'year',
      subject: 'exam',
      meta: year
    });
    nodes.push({
      id: 'qtype-' + qtype + '-' + year,
      label: qtypeNames[qtype] || qtype,
      type: 'qtype',
      subject: 'exam',
      meta: qtype,
      _parentYear: year
    });
    links.push({
      source: 'year-' + year,
      target: 'qtype-' + qtype + '-' + year
    });
    return { nodes: nodes, links: links };
  }

  // subject 视图下「科目 + 卷」层：仅统计该科目+卷内存在的题型
  function getSubjectYearQtypeLevel(nav, subject, year, searchQ) {
    var nodes = [];
    var links = [];
    var sData = nav.yearsMap[year] && nav.yearsMap[year][subject];
    if (!sData) return { nodes: [], links: [] };

    var hasSel = false, hasCom = false;
    var kps = sData.kps || {};
    Object.keys(kps).forEach(function (kp) {
      kps[kp].forEach(function (f) {
        var q = nav.questions[f];
        if (!q) return;
        if (q.number <= 40 || q.number === undefined) hasSel = true;
        else hasCom = true;
      });
    });

    nodes.push({
      id: 'year-' + year,
      label: topLabel(nav, year),
      type: 'year',
      subject: 'exam',
      meta: year
    });
    nodes.push({
      id: 'subj-' + subject,
      label: subjectName(subject),
      type: 'subject',
      subject: subject,
      meta: subject
    });
    if (hasSel) {
      nodes.push({
        id: 'qtype-selection-' + year,
        label: '选择题',
        type: 'qtype',
        subject: 'exam',
        meta: 'selection',
        _parentYear: year
      });
      links.push({ source: 'year-' + year, target: 'qtype-selection-' + year });
    }
    if (hasCom) {
      nodes.push({
        id: 'qtype-comprehensive-' + year,
        label: '综合题',
        type: 'qtype',
        subject: 'exam',
        meta: 'comprehensive',
        _parentYear: year
      });
      links.push({ source: 'year-' + year, target: 'qtype-comprehensive-' + year });
    }
    return { nodes: nodes, links: links };
  }

  function getKpLevel(nav, year, qtype, subject, searchQ) {
    var nodes = [];
    var links = [];
    var yData = nav.yearsMap[year];
    if (!yData || !yData[subject]) return { nodes: [], links: [] };
    var kps = yData[subject].kps || {};

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
      links.push({
        source: 'subj-' + subject + '-' + year + '-' + qtype,
        target: 'kp-' + kp + '-' + year + '-' + subject + '-' + qtype
      });
    });

    // Include parent nodes
    nodes.push({
      id: 'year-' + year,
      label: topLabel(nav, year),
      type: 'year',
      subject: 'exam',
      meta: year
    });
    nodes.push({
      id: 'qtype-' + qtype + '-' + year,
      label: qtypeNames[qtype] || qtype,
      type: 'qtype',
      subject: 'exam',
      meta: qtype,
      _parentYear: year
    });
    nodes.push({
      id: 'subj-' + subject + '-' + year + '-' + qtype,
      label: subjectName(subject),
      type: 'subject',
      subject: subject,
      meta: subject,
      _parentYear: year,
      _parentQtype: qtype
    });
    links.push({
      source: 'qtype-' + qtype + '-' + year,
      target: 'subj-' + subject + '-' + year + '-' + qtype
    });

    return { nodes: nodes, links: links };
  }

  function getQuestionLevel(nav, year, qtype, subject, kp, searchQ) {
    var nodes = [];
    var links = [];
    var kpData = nav.kpMap[kp];
    if (!kpData) return { nodes: [], links: [] };

    var files = [];
    var yData = nav.yearsMap[year];
    if (yData && yData[subject] && yData[subject].kps && yData[subject].kps[kp]) {
      yData[subject].kps[kp].forEach(function (f) {
        var q = nav.questions[f];
        if (!q) return;
        var qt = (q.number <= 40 || q.number === undefined) ? 'selection' : 'comprehensive';
        if (qt === qtype) files.push(f);
      });
    }

    files.forEach(function (file) {
      var q = nav.questions[file];
      if (!q) return;
      var label = q.title || file;
      if (searchQ && label.toLowerCase().indexOf(searchQ) < 0) return;
      nodes.push({
        id: 'q-' + file.replace('.md', ''),
        label: label.length > 20 ? label.substr(0, 18) + '…' : label,
        type: 'question',
        subject: subject,
        meta: file,
        url: BASE_URL + 'question/' + file.replace('.md', '/'),
        _parentKp: kp
      });
      links.push({
        source: 'kp-' + kp + '-' + year + '-' + subject + '-' + qtype,
        target: 'q-' + file.replace('.md', '')
      });
    });

    // Parent nodes
    nodes.push({
      id: 'year-' + year,
      label: topLabel(nav, year),
      type: 'year',
      subject: 'exam',
      meta: year
    });
    nodes.push({
      id: 'subj-' + subject + '-' + year + '-' + qtype,
      label: subjectName(subject),
      type: 'subject',
      subject: subject,
      meta: subject,
      _parentYear: year,
      _parentQtype: qtype
    });
    nodes.push({
      id: 'kp-' + kp + '-' + year + '-' + subject + '-' + qtype,
      label: kp,
      type: 'kp',
      subject: subject,
      meta: kp,
      _parentYear: year,
      _parentSubject: subject,
      _parentQtype: qtype
    });
    // 题目层需要补上 qtype 节点，否则其连线会成为悬空链接（filtered invalid links）
    nodes.push({
      id: 'qtype-' + qtype + '-' + year,
      label: qtypeNames[qtype] || qtype,
      type: 'qtype',
      subject: 'exam',
      meta: qtype,
      _parentYear: year
    });
    links.push({ source: 'year-' + year, target: 'qtype-' + qtype + '-' + year });
    links.push({ source: 'qtype-' + qtype + '-' + year, target: 'subj-' + subject + '-' + year + '-' + qtype });
    links.push({ source: 'subj-' + subject + '-' + year + '-' + qtype, target: 'kp-' + kp + '-' + year + '-' + subject + '-' + qtype });

    return { nodes: nodes, links: links };
  }

  // ----- Breadcrumb -----
  function updateBreadcrumb() {
    var f = state.focus;
    var parts = [];

    if (state.tab === 'docs') {
      breadcrumbEl.style.display = 'none';
      return;
    }

    breadcrumbEl.style.display = 'flex';

    if (state.view === 'year') {
      parts.push({ label: '🗓 按年份', action: 'home' });
    } else {
      parts.push({ label: '📚 按科目', action: 'home' });
    }

    if (f.year) {
      parts.push({ label: topLabel(state._nav, f.year), action: 'year' });
    }
    if (f.subject) {
      parts.push({ label: subjectName(f.subject), action: 'subject' });
    }
    if (f.kp) {
      parts.push({ label: f.kp, action: 'kp' });
    }

    var html = '';
    for (var i = 0; i < parts.length; i++) {
      if (i > 0) html += '<span class="sep">›</span>';
      if (i === parts.length - 1) {
        html += '<span>' + parts[i].label + '</span>';
      } else {
        html += '<span data-action="' + parts[i].action + '">' + parts[i].label + '</span>';
      }
    }
    breadcrumbEl.innerHTML = html;

    // Click handlers for breadcrumb
    breadcrumbEl.querySelectorAll('[data-action]').forEach(function (el) {
      el.addEventListener('click', function () {
        var action = this.getAttribute('data-action');
        if (action === 'home') {
          state.focus = { year: null, qtype: null, subject: null, kp: null };
        } else if (action === 'year') {
          state.focus.qtype = null;
          state.focus.kp = null;
          if (state.view === 'subject') {
            // subject 视图：回到“科目→卷”层，保留科目
            state.focus.year = null;
          } else {
            state.focus.subject = null;
          }
        } else if (action === 'qtype') {
          state.focus.subject = null;
          state.focus.kp = null;
        } else if (action === 'subject') {
          state.focus.kp = null;
        }
        renderGraph();
      });
    });
  }

  // ----- D3 Render -----
  var _simulation = null;
  var _svg = null;
  var _g = null;

  function selectExamYear(year) {
    state.focus = { year: year, qtype: null, subject: null, kp: null };
    renderGraph();
  }

  function yearQuestionCount(year) {
    var subjects = state._nav && state._nav.yearsMap ? state._nav.yearsMap[year] : null;
    var count = 0;
    if (!subjects) return count;
    Object.keys(subjects).forEach(function (subject) { count += subjects[subject].count || 0; });
    return count;
  }

  function updateYearNavigator() {
    var showNavigator = yearNav && state.tab === 'exam' && state.view === 'year' && state._nav;
    if (!yearNav) return;
    if (!showNavigator) {
      yearNav.style.display = 'none';
      yearNav.innerHTML = '';
      return;
    }

    yearNav.style.display = 'flex';
    yearNav.innerHTML = '';
    state._nav.years.forEach(function (year) {
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'graph-year-nav-btn' + (state.focus.year === year ? ' active' : '');
      button.textContent = year;
      button.title = year + '年真题';
      if (state.focus.year === year) button.setAttribute('aria-current', 'page');
      button.addEventListener('click', function () { selectExamYear(year); });
      yearNav.appendChild(button);
    });
  }

  function renderYearIndex(nodes) {
    container.innerHTML = '';
    var index = document.createElement('div');
    index.className = 'graph-year-index';
    nodes.forEach(function (node) {
      var year = node.meta;
      var card = document.createElement('button');
      card.type = 'button';
      card.className = 'graph-year-card';
      card.setAttribute('aria-label', '查看' + year + '年真题');
      var yearLabel = document.createElement('span');
      yearLabel.className = 'graph-year-card-label';
      yearLabel.textContent = year;
      var count = document.createElement('span');
      count.className = 'graph-year-card-count';
      count.textContent = yearQuestionCount(year) + '题';
      card.appendChild(yearLabel);
      card.appendChild(count);
      card.addEventListener('click', function () { selectExamYear(year); });
      index.appendChild(card);
    });
    container.appendChild(index);
  }

  function docsSubjectAnchor(subject, width, height) {
    var anchors = {
      'data-structure': [0.36, 0.36],
      'computer-org': [0.64, 0.36],
      'os': [0.36, 0.64],
      'network': [0.64, 0.64]
    };
    var anchor = anchors[subject] || [0.5, 0.5];
    return { x: width * anchor[0], y: height * anchor[1] };
  }

  function graphFitTransform(nodes, width, height) {
    var padding = 44;
    var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    nodes.forEach(function (node) {
      var radius = (nodeRadius[node.type] || 12) + 8;
      minX = Math.min(minX, node.x - radius);
      maxX = Math.max(maxX, node.x + radius);
      minY = Math.min(minY, node.y - radius);
      maxY = Math.max(maxY, node.y + radius);
    });
    var graphWidth = Math.max(maxX - minX, 1);
    var graphHeight = Math.max(maxY - minY, 1);
    var scale = Math.min((width - padding * 2) / graphWidth, (height - padding * 2) / graphHeight, 1.15);
    scale = Math.max(0.35, scale);
    var offsetX = (width - graphWidth * scale) / 2 - minX * scale;
    var offsetY = (height - graphHeight * scale) / 2 - minY * scale;
    return d3.zoomIdentity.translate(offsetX, offsetY).scale(scale);
  }

  function renderGraph() {
    console.log('KG: renderGraph, tab:', state.tab, 'nodes:', state.currentNodes.length);
    container.innerHTML = '';
    infoPanel.style.display = 'none';
    clearEdit();

    var data = getCurrentViewData();
    state.currentNodes = data.nodes;
    state.currentLinks = data.links;
    updateYearNavigator();

    var isExamYearIndex = state.tab === 'exam' && state.view === 'year' &&
      state.focus.year === null && state.focus.qtype === null &&
      state.focus.subject === null && state.focus.kp === null;
    if (isExamYearIndex) {
      updateBreadcrumb();
      renderYearIndex(data.nodes);
      return;
    }

    if (!data.nodes || !data.nodes.length) {
      container.innerHTML = '<p style="color:#8b949e;padding:2rem;text-align:center">暂无数据' +
        (state.searchQuery ? '（未匹配搜索条件）' : '') + '</p>';
      updateBreadcrumb();
      return;
    }

    updateBreadcrumb();

    var width = container.clientWidth || 800;
    var height = container.clientHeight || 500;

    _svg = d3.select(container).append('svg')
      .attr('width', width).attr('height', height);

    var zoom = d3.zoom()
      .scaleExtent([0.35, 5])
      .on('zoom', function (e) { if (_g) _g.attr('transform', e.transform); });
    _svg.call(zoom);

    _g = _svg.append('g');

    // Add shadow filter for node glow
    var defs = _svg.append('defs');
    data.nodes.forEach(function (d) {
      if (!d._filterId) {
        d._filterId = 'glow-' + Math.random().toString(36).substr(2, 6);
        var filter = defs.append('filter').attr('id', d._filterId)
          .append('feDropShadow')
          .attr('dx', 0).attr('dy', 0).attr('stdDeviation', 2)
          .attr('flood-color', subjectColors[d.subject] || '#888')
          .attr('flood-opacity', 0.4);
      }
    });

    var isHierarchical = state.tab !== 'docs';

    var link = _g.selectAll('.link')
      .data(data.links).enter().append('line')
      .attr('class', 'link')
      .attr('stroke-width', 1.2)
      .attr('opacity', 0.5);

    var node = _g.selectAll('.node')
      .data(data.nodes).enter().append('g')
      .attr('class', 'node')
      .call(d3.drag()
        .on('start', function (e, d) {
          if (!e.active) _simulation && _simulation.alphaTarget(0.3).restart();
          d.fx = d.x;
          d.fy = d.y;
        })
        .on('drag', function (e, d) { d.fx = e.x; d.fy = e.y; })
        .on('end', function (e, d) {
          if (!e.active) _simulation && _simulation.alphaTarget(0);
          d.fx = null;
          d.fy = null;
        })
      );

    node.append('circle')
      .attr('r', function (d) { return nodeRadius[d.type] || 12; })
      .attr('fill', function (d) { return subjectColors[d.subject] || '#888'; })
      .attr('opacity', 0.85)
      .attr('stroke', function (d) {
        if (state.adminMode && d.type === 'question') return '#f0c040';
        if (d.type === 'year' || d.type === 'subject') return null; // 描边改由 CSS .graph-ring 控制，随主题自适应
        return 'none';
      })
      .attr('class', function (d) {
        return (d.type === 'year' || d.type === 'subject') ? 'graph-ring' : '';
      })
      .attr('stroke-width', function (d) {
        return (state.adminMode && d.type === 'question') ? 2 : 1;
      })
      .attr('stroke-dasharray', function (d) {
        return (state.adminMode && d.type === 'question') ? '4 2' : 'none';
      })
      .style('cursor', 'pointer');

    // Text
    node.append('text')
      .attr('dy', '0.35em')
      .attr('text-anchor', 'middle')
      .attr('class', 'graph-node-label')
      .attr('font-size', function (d) {
        if (d.type === 'question') return '7px';
        if (d.type === 'kp') return '9px';
        return '10px';
      })
      .style('pointer-events', 'none')
      .text(function (d) {
        if (d.type === 'question') return 'Q';
        var label = d.label || '';
        if (label.length > 6) return label.substr(0, 5) + '…';
        return label;
      });

    // Count badge for intermediate nodes
    node.filter(function (d) { return d.count && (d.type === 'subject' || d.type === 'kp'); })
      .append('title')
      .text(function (d) { return d.label + ' (' + d.count + '题)'; });

    // Click handler
    node.on('click', function (e, d) {
      e.stopPropagation();
      if (state.adminMode && d.type === 'question') {
        openEditor(d);
        return;
      }
      handleNodeClick(d);
    });

    // Double-click to navigate
    node.on('dblclick', function (e, d) {
      e.stopPropagation();
      if (d.url) {
        window.open(d.url, '_blank');
      } else if (state.tab === 'docs' && d.id) {
        // 文档视图的知识球：跳转到对应文档页
        window.open(d.id, '_blank');
      } else if (d.type === 'question' && d.meta) {
        var url = BASE_URL + 'question/' + d.meta.replace('.md', '/');
        window.open(url, '_blank');
      } else if (!state.adminMode) {
        // Drill down on double-click too
        handleNodeClick(d);
      }
    });

    // Force simulation
    var chargeStrength = isHierarchical ? -400 : -105;
    var linkDist = isHierarchical ? 140 : 72;

    // Sanitize links.
    // d3.forceLink MUTATES each link's source/target from an id string into the
    // actual node object. When the same link objects are reused on a later render
    // (e.g. docs view returns state.config.links directly), forceLink would then do
    // nodeById.get(object) and throw "missing: [object Object]". Restore them to id
    // strings first so they always resolve, then drop any that reference missing nodes.
    data.links.forEach(function (l) {
      if (l.source && typeof l.source === 'object') l.source = l.source.id;
      if (l.target && typeof l.target === 'object') l.target = l.target.id;
    });
    var nodeIdSet = {};
    data.nodes.forEach(function (n) { nodeIdSet[n.id] = true; });
    var invalidLinks = 0;
    data.links = data.links.filter(function (l) {
      var sid = l.source, tid = l.target;
      if (!sid || !tid || !nodeIdSet[sid] || !nodeIdSet[tid]) {
        invalidLinks++;
        return false;
      }
      return true;
    });
    if (invalidLinks) console.warn('KG: filtered', invalidLinks, 'invalid links');

    if (_simulation) _simulation.stop();
    var simulation = d3.forceSimulation(data.nodes)
      .force('link', d3.forceLink(data.links).id(function (d) { return d.id; }).distance(linkDist))
      .force('charge', d3.forceManyBody().strength(chargeStrength))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collision', d3.forceCollide().radius(function (d) {
        return (nodeRadius[d.type] || 12) + 7;
      }));

    if (state.tab === 'docs') {
      simulation
        .force('subject-x', d3.forceX(function (d) { return docsSubjectAnchor(d.subject, width, height).x; }).strength(0.14))
        .force('subject-y', d3.forceY(function (d) { return docsSubjectAnchor(d.subject, width, height).y; }).strength(0.14));
    }

    function drawGraph() {
      link
        .attr('x1', function (d) { return d.source.x; })
        .attr('y1', function (d) { return d.source.y; })
        .attr('x2', function (d) { return d.target.x; })
        .attr('y2', function (d) { return d.target.y; });
      node.attr('transform', function (d) { return 'translate(' + d.x + ',' + d.y + ')'; });
    }

    // Pre-stabilize before the first paint, then fit the whole graph into its viewport.
    simulation.stop();
    for (var warmupTick = 0; warmupTick < 180; warmupTick++) simulation.tick();
    drawGraph();
    _svg.call(zoom.transform, graphFitTransform(data.nodes, width, height));
    _simulation = simulation.alpha(0.16).on('tick', drawGraph).restart();

    // Background click to clear info
    _svg.on('click', function () {
      infoPanel.style.display = 'none';
      clearEdit();
    });
  }

  // ----- Node click handling (drill down) -----
  function handleNodeClick(d) {
    if (state.tab === 'docs') {
      // Show info panel (original behavior)
      showInfoPanel(d);
      return;
    }

    // Exam/Simulate mode
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
    } else if (d.type === 'subject') {
      if (state.focus.year === null && state.view === 'subject') {
        // Subject view: select subject
        state.focus.subject = d.meta || d.subject;
        state.focus.year = null;
        state.focus.qtype = null;
        state.focus.kp = null;
        renderGraph();
      } else if (state.focus.year !== null) {
        // Year view: drill to KP level
        state.focus.subject = d.meta || d.subject;
        state.focus.kp = null;
        renderGraph();
      } else {
        showInfoPanel(d);
      }
    } else if (d.type === 'kp') {
      state.focus.kp = d.meta;
      renderGraph();
    } else if (d.type === 'question') {
      // Navigate to question page
      if (d.url && state.tab !== 'docs') {
        showInfoPanel(d);
        window.open(d.url, '_blank');
      } else {
        showInfoPanel(d);
      }
    }
  }

  // ----- Info panel -----
  function showInfoPanel(d) {
    infoTitle.textContent = d.label || '';
    infoTitle.style.color = subjectColors[d.subject] || '#888';

    var metaHtml = '';
    if (state.tab === 'docs') {
      metaHtml = '科目: ' + (subjectNames[d.subject] || d.subject) +
        '<br>难度: ' + '★'.repeat(d.difficulty || 1);
    } else if (d.type === 'year') {
      metaHtml = '年份: ' + d.label;
    } else if (d.type === 'qtype') {
      metaHtml = '题型: ' + (qtypeNames[d.meta] || d.label);
    } else if (d.type === 'subject') {
      metaHtml = '科目: ' + d.label + (d.count ? ' (' + d.count + '题)' : '');
    } else if (d.type === 'kp') {
      metaHtml = '知识点: ' + d.label + (d.count ? ' (' + d.count + '题)' : '');
    } else if (d.type === 'question') {
      metaHtml = '题目: ' + d.label + '<br>科目: ' + (subjectNames[d.subject] || d.subject);
    }

    infoMeta.innerHTML = metaHtml;

    if (d.type === 'question' && state.mapping) {
      var file = d.meta;
      var qData = state.mapping.questionIndex ? state.mapping.questionIndex[file] : null;
      if (qData && qData.knowledge_points && qData.knowledge_points.length) {
        infoTags.innerHTML = '<div style="font-size:0.8rem;color:#8b949e;margin-top:.3rem">知识点: ' +
          qData.knowledge_points.join(', ') + '</div>';
      } else {
        infoTags.innerHTML = '<div style="font-size:0.8rem;color:#8b949e;margin-top:.3rem">暂无知识点标签</div>';
      }
    } else if (d.prerequisites && d.prerequisites.length) {
      infoTags.innerHTML = '<div style="font-size:0.8rem;color:#8b949e;">前置: ' + d.prerequisites.join(', ') + '</div>';
    } else {
      infoTags.innerHTML = '';
    }

    if (d.url) {
      infoLink.href = d.url;
      infoLink.style.display = 'inline-block';
    } else if (d.type === 'question' && d.meta) {
      infoLink.href = BASE_URL + 'question/' + d.meta.replace('.md', '/');
      infoLink.style.display = 'inline-block';
    } else if (state.tab === 'docs' && d.id) {
      // 文档视图知识球：信息面板提供跳转到对应文档页的链接
      infoLink.href = d.id;
      infoLink.style.display = 'inline-block';
    } else {
      infoLink.style.display = 'none';
    }

    // Admin edit section
    if (state.adminMode && d.type === 'question') {
      openEditor(d);
    } else {
      infoEdit.style.display = 'none';
    }

    infoPanel.style.display = 'block';
  }

  // ----- Tag Editor -----
  function openEditor(d) {
    state.editTarget = d;
    infoEdit.style.display = 'block';
    var file = d.meta;
    var qData = state.mapping.questionIndex ? state.mapping.questionIndex[file] : null;
    var kps = (qData && qData.knowledge_points) || [];
    renderKpTags(kps);
  }

  function clearEdit() {
    state.editTarget = null;
    infoEdit.style.display = 'none';
    kpEditor.innerHTML = '';
    if (kpAddInput) kpAddInput.value = '';
  }

  function renderKpTags(kps) {
    if (!kpEditor) return;
    var html = '';
    kps.forEach(function (kp) {
      html += '<span class="kp-tag">' + kp +
        '<span class="kp-del" data-kp="' + kp.replace(/"/g, '&quot;') + '">✕</span></span>';
    });
    if (!kps.length) html = '<span style="font-size:.8rem;color:#8b949e">无标签</span>';
    kpEditor.innerHTML = html;

    // Delete handlers
    kpEditor.querySelectorAll('.kp-del').forEach(function (el) {
      el.addEventListener('click', function () {
        var kp = this.getAttribute('data-kp');
        removeKpFromCurrent(kp);
      });
    });
  }

  function removeKpFromCurrent(kp) {
    if (!state.editTarget || !state.mapping) return;
    var file = state.editTarget.meta;
    var qData = state.mapping.questionIndex[file];
    if (!qData) return;
    qData.knowledge_points = (qData.knowledge_points || []).filter(function (k) { return k !== kp; });
    renderKpTags(qData.knowledge_points);
    saveToLocalStorage();
  }

  function addKpToCurrent(kp) {
    if (!state.editTarget || !state.mapping || !kp) return;
    var file = state.editTarget.meta;
    var qData = state.mapping.questionIndex[file];
    if (!qData) {
      state.mapping.questionIndex[file] = { knowledge_points: [] };
      qData = state.mapping.questionIndex[file];
    }
    if (!qData.knowledge_points) qData.knowledge_points = [];
    if (qData.knowledge_points.indexOf(kp) < 0) {
      qData.knowledge_points.push(kp);
    }
    renderKpTags(qData.knowledge_points);
    saveToLocalStorage();
  }

  // ----- LocalStorage persistence -----
  function saveToLocalStorage() {
    try {
      var edits = JSON.parse(localStorage.getItem('cc408-kp-edits') || '{}');
      if (state.editTarget) {
        var file = state.editTarget.meta;
        var qData = state.mapping.questionIndex[file];
        edits[file] = (qData && qData.knowledge_points) || [];
      }
      localStorage.setItem('cc408-kp-edits', JSON.stringify(edits));
    } catch (e) { /* ignore */ }
  }

  function loadEditsFromStorage() {
    try {
      var edits = JSON.parse(localStorage.getItem('cc408-kp-edits') || '{}');
      if (!state.mapping) return;
      for (var file in edits) {
        if (state.mapping.questionIndex[file]) {
          state.mapping.questionIndex[file].knowledge_points = edits[file];
        }
      }
    } catch (e) { /* ignore */ }
  }

  function exportMapping() {
    if (!state.mapping) return;
    var dataStr = JSON.stringify(state.mapping, null, 2);
    var blob = new Blob([dataStr], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'question-kp-mapping.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  // ----- Search -----
  function handleSearch() {
    state.searchQuery = searchInput.value.trim();
    if (state.tab === 'docs') {
      renderGraph();
    } else {
      renderGraph();
    }
  }

  // ----- Tab switching -----
  function switchTab(tab) {
    console.log('KG: switchTab', tab);
    state.tab = tab;
    state.focus = { year: null, qtype: null, subject: null, kp: null };
    state.searchQuery = '';
    if (tab !== 'admin') state.adminMode = false;

    if (searchInput) {
      searchInput.placeholder = tab === 'docs' ? '搜索知识点...' : '搜索年份/科目/知识点...';
      searchInput.value = '';
    }

    // Show/hide view toggle
    if (viewToggle) {
      viewToggle.style.display = (tab === 'exam' || tab === 'simulate') ? 'flex' : 'none';
      var yearBtn = viewToggle.querySelector('[data-view="year"]');
      var subjBtn = viewToggle.querySelector('[data-view="subject"]');
      if (tab === 'simulate') {
        // 模拟题顶层为「卷N」（无年份语义），仅保留「按科目」
        if (yearBtn) { yearBtn.style.display = 'none'; yearBtn.classList.remove('active'); }
        if (subjBtn) { subjBtn.style.display = ''; subjBtn.classList.add('active'); }
        state.view = 'subject';
      } else {
        if (yearBtn) { yearBtn.style.display = ''; yearBtn.classList.add('active'); }
        if (subjBtn) { subjBtn.style.display = ''; subjBtn.classList.remove('active'); }
        state.view = 'year';
      }
    }

    // Highlight tab
    document.querySelectorAll('.graph-tab').forEach(function (t) {
      t.classList.toggle('active', t.getAttribute('data-graph') === tab);
    });

    if (tab === 'docs') {
      state.config = loadTabConfig('docs');
      renderGraph();
    } else if (tab === 'exam' || tab === 'simulate') {
      state.config = loadTabConfig(tab);
      state.source = tab === 'exam' ? '408真题' : '模拟题';
      console.log('KG: loading for', state.source, 'config:', state.config ? 'OK' : 'MISSING');
      loadMapping(function () {
        loadEditsFromStorage();
        state._nav = buildNavigation(state.source);
        renderGraph();
      });
    } else if (tab === 'admin') {
      // Toggle admin mode on exam tab
      state.adminMode = !state.adminMode;
      if (state.tab !== 'exam') {
        state.tab = 'exam';
        state.config = loadTabConfig('exam');
        state.source = '408真题';
      }
      document.querySelectorAll('.graph-tab').forEach(function (t) {
        t.classList.toggle('active', t.getAttribute('data-graph') === 'exam');
        t.classList.toggle('admin-active', t.getAttribute('data-graph') === 'admin' && state.adminMode);
      });
      if (state.adminMode) {
        loadMapping(function () {
          loadEditsFromStorage();
          state._nav = buildNavigation(state.source);
          state.focus = { year: null, qtype: null, subject: null, kp: null };
          renderGraph();
          container.classList.add('admin-mode');
        });
      } else {
        container.classList.remove('admin-mode');
        renderGraph();
      }
    }
  }

  // ----- Init -----
  function init() {
    // Tab click events
    document.querySelectorAll('.graph-tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        var g = this.getAttribute('data-graph');
        if (g !== 'admin' && g === state.tab) return;
        container.classList.remove('admin-mode');
        switchTab(g);
      });
    });

    // View toggle events
    document.querySelectorAll('.view-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var v = this.getAttribute('data-view');
        if (v === state.view) return;
        state.view = v;
        state.focus = { year: null, qtype: null, subject: null, kp: null };
        document.querySelectorAll('.view-btn').forEach(function (b) {
          b.classList.toggle('active', b.getAttribute('data-view') === v);
        });
        renderGraph();
      });
    });

    // Search
    if (searchInput) {
      searchInput.addEventListener('input', function () {
        clearTimeout(searchInput._timer);
        searchInput._timer = setTimeout(handleSearch, 300);
      });
    }

    // Info panel close
    if (infoClose) {
      infoClose.addEventListener('click', function () {
        infoPanel.style.display = 'none';
        clearEdit();
      });
    }

    // KP add
    if (kpAddBtn && kpAddInput) {
      kpAddBtn.addEventListener('click', function () {
        var kp = kpAddInput.value.trim();
        if (kp) {
          addKpToCurrent(kp);
          kpAddInput.value = '';
        }
      });
      kpAddInput.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
          var kp = kpAddInput.value.trim();
          if (kp) {
            addKpToCurrent(kp);
            kpAddInput.value = '';
          }
        }
      });
    }

    // Save & Export
    if (kpSaveBtn) {
      kpSaveBtn.addEventListener('click', saveToLocalStorage);
    }
    if (kpExportBtn) {
      kpExportBtn.addEventListener('click', exportMapping);
    }

    // Initial load
    state.config = loadTabConfig('docs');
    renderGraph();

    // Window resize
    var resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(renderGraph, 300);
    });
  }

  // Start
  init();
})();
