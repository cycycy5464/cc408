(function () {
  "use strict";

  var pageSize = 12;
  var dataElement = document.getElementById("question-data");
  var grid = document.getElementById("question-grid");
  if (!dataElement || !grid) return;

  var questions;
  try {
    questions = JSON.parse(dataElement.textContent || "[]");
  } catch (error) {
    return;
  }

  var controls = {
    source: document.getElementById("filter-source"),
    year: document.getElementById("filter-exam-year"),
    set: document.getElementById("filter-set"),
    subject: document.getElementById("filter-subject"),
    chapter: document.getElementById("filter-chapter"),
    type: document.getElementById("filter-type"),
    search: document.getElementById("filter-search"),
    status: document.getElementById("question-list-status"),
    pagination: document.getElementById("question-pagination")
  };
  var currentPage = 1;

  function escapeHtml(value) {
    return String(value || "").replace(/[&<>"']/g, function (character) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character];
    });
  }

  function sourceReference(question) {
    var number = question.number ? "第" + question.number + "题" : "";
    if (question.source === "408真题") {
      var year = question.years && question.years[0];
      return [year ? year + "年真题" : "408真题", number].filter(Boolean).join(" · ");
    }
    if (question.source === "模拟题") {
      return [question.set ? "模拟题第" + question.set + "套" : "模拟题", number].filter(Boolean).join(" · ");
    }
    return [question.chapter || "章节习题", number].filter(Boolean).join(" · ");
  }

  function renderCard(question) {
    var type = question.type === "comprehensive" ? "解答题" : "选择题";
    var typeStyle = question.type === "comprehensive"
      ? 'style="background:rgba(245,158,11,.12);color:#f59e0b"'
      : 'style="background:rgba(57,186,230,.12);color:var(--accent)"';
    var year = question.years && question.years[0] || "";
    return '<div class="question-block" data-subject="' + escapeHtml(question.subject) + '" data-year="' + year + '" data-number="' + question.number + '">' +
      '<div class="q-number">' +
      escapeHtml(sourceReference(question)) +
      ' <span class="q-subject-tag">' + escapeHtml(question.subject) + '</span>' +
      ' <span class="q-subject-tag" ' + typeStyle + '>' + type + '</span>' +
      '</div>' +
      '<div class="q-body">' + (question.content_html || question.stem || question.title) + '</div>' +
      '<div class="question-actions">' +
      '<button class="reveal-btn" onclick="toggleAnswer(this)">查看答案与解析</button>' +
      '<button class="favorite-btn" data-qid="ql-' + escapeHtml(question.url) + '" data-title="' + escapeHtml(question.title) + '" data-year="' + year + '" data-number="' + question.number + '" data-subject="' + escapeHtml(question.subject) + '">⭐ 收藏</button>' +
      '</div></div>';
  }

  function processQuestionBlock(block) {
    // Hide [tag_link]
    block.querySelectorAll('p').forEach(function(p) {
      if (p.textContent.trim() === '[tag_link]') p.style.display = 'none';
    });

    // Find answer panel
    var findAnswer = function(el) {
      for (let child = el.firstChild; child; child = child.nextSibling) {
        if (child.nodeType === Node.TEXT_NODE) {
          const m = child.textContent.match(/正确答案[：:]\s*([ABCDabcd])/);
          if (m) {
            var av = m[1].toUpperCase();
            var before = child.textContent.substring(0, m.index);
            var after = child.textContent.substring(m.index + m[0].length);
            var panel = document.createElement('div');
            panel.className = 'answer-panel';
            panel.style.display = 'none';
            var title = document.createElement('div');
            title.className = 'answer-title';
            title.innerHTML = '正确答案：<strong>' + av + '</strong>';
            panel.appendChild(title);
            panel.setAttribute('data-answer', av);
            if (before.trim()) child.textContent = before;
            else el.removeChild(child);
            if (after.trim()) el.insertBefore(document.createTextNode(after), child.nextSibling);
            el.insertBefore(panel, child.nextSibling);
            var pp = panel.parentNode;
            if (pp && pp.tagName === 'P') {
              var sib = pp.nextSibling;
              while (sib) { var nxt = sib.nextSibling; panel.appendChild(sib); sib = nxt; }
              pp.parentNode.insertBefore(panel, pp);
              pp.parentNode.removeChild(pp);
            }
            return true;
          }
        } else if (child.nodeType === Node.ELEMENT_NODE) {
          if (findAnswer(child)) return true;
        }
      }
      return false;
    };
    var found = findAnswer(block);

    // Comprehensive fallback
    if (!found) {
      var anchor = null;
      var qBody = block.querySelector('.q-body');
      if (qBody) {
        var allP2 = qBody.querySelectorAll('p');
        for (var pi = 0; pi < allP2.length; pi++) {
          var p2 = allP2[pi];
          var txt = p2.textContent.trim();
          if (txt === '[tag_link]') { anchor = p2; continue; }
          var pureTag = true;
          for (var ci = 0; ci < p2.childNodes.length; ci++) {
            var cn = p2.childNodes[ci];
            if (cn.nodeType === Node.TEXT_NODE) {
              if (cn.textContent.trim()) { pureTag = false; break; }
            } else if (cn.nodeType === Node.ELEMENT_NODE && cn.tagName !== 'A') {
              pureTag = false; break;
            }
          }
          if (pureTag) anchor = p2;
        }
        if (anchor) {
          var panel = document.createElement('div');
          panel.className = 'answer-panel';
          panel.style.display = 'none';
          panel.setAttribute('data-answer', '');
          var t = document.createElement('div');
          t.className = 'answer-title';
          t.textContent = '答案与解析：';
          panel.appendChild(t);
          var cur = anchor.nextSibling;
          while (cur) { var nxt = cur.nextSibling; panel.appendChild(cur); cur = nxt; }
          qBody.appendChild(panel);
        }
      }
    }

    // Convert options
    var qb = block.querySelector('.q-body');
    if (!qb) return;
    var allP = [];
    for (var i = 0; i < qb.children.length; i++) {
      if (qb.children[i].tagName === 'P') allP.push(qb.children[i]);
    }
    for (var pi = 0; pi < allP.length; pi++) {
      var p = allP[pi];
      var txt = p.textContent.trim();
      var opts = txt.match(/([A-D])\s*\.\s*(.*?)(?=\s*[A-D]\s*\.|$)/g);
      if (opts && opts.length > 0) {
        var frag = document.createDocumentFragment();
        var idx = txt.search(/[A-D]\s*\./);
        var pre = idx > 0 ? txt.slice(0, idx).trim() : '';
        if (pre) {
          var sp = document.createElement('p');
          sp.className = 'exam-stem-text';
          sp.textContent = pre;
          frag.appendChild(sp);
        }
        var created = false;
        for (var oi = 0; oi < opts.length; oi++) {
          var m = opts[oi].match(/^([A-D])\s*\.\s*(.*)/);
          if (m) {
            created = true;
            var opt = document.createElement('div');
            opt.className = 'exam-option';
            opt.setAttribute('data-opt', m[1]);
            opt.innerHTML = '<span class="opt-label">' + m[1] + '.</span> <span class="opt-text">' + m[2] + '</span>';
            opt.addEventListener('click', function() {
              var parent = this.parentElement;
              if (parent) {
                parent.querySelectorAll('.exam-option').forEach(function(o) { o.classList.remove('selected'); });
              }
              this.classList.add('selected');
            });
            frag.appendChild(opt);
          }
        }
        if (created) p.parentNode.replaceChild(frag, p);
      }
    }

    // Replace 【解析】
    var rp = function(el) {
      for (let c = el.firstChild; c; c = c.nextSibling) {
        if (c.nodeType === Node.TEXT_NODE && c.textContent.includes('【解析】')) {
          const h = c.textContent.replace(/【解析】/g, '<div class="analysis-title">解析：</div>');
          const t = document.createElement('div'); t.innerHTML = h;
          el.replaceChild(t.firstChild, c);
        } else if (c.nodeType === Node.ELEMENT_NODE) rp(c);
      }
    };
    rp(block);

    // Setup favorite button
    setupFavoriteBtn(block);
  }

  function setupFavoriteBtn(block) {
    var btn = block.querySelector('.favorite-btn');
    if (!btn) return;
    var STORAGE_KEY = 'quiz_collections';
    function loadAll() { try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []; } catch(e) { return []; } }
    function saveAll(items) { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(items)); } catch(e) {} }
    var qid = btn.getAttribute('data-qid');
    var year = btn.getAttribute('data-year');
    var qnum = btn.getAttribute('data-number');
    var subject = btn.getAttribute('data-subject');
    var title = btn.getAttribute('data-title');
    var id = qid || (year + '-' + qnum);
    var allItems = loadAll();
    var collectedMap = {};
    allItems.forEach(function(item) { collectedMap[item.id] = item; });
    if (collectedMap[id]) { btn.classList.add('collected'); btn.textContent = '已收藏'; }
    btn.onclick = function(e) {
      var all = loadAll();
      var cm = {};
      all.forEach(function(item) { cm[item.id] = item; });
      if (cm[id]) {
        var kept = all.filter(function(item) { return item.id !== id; });
        delete cm[id];
        btn.classList.remove('collected');
        btn.textContent = '⭐ 收藏';
        saveAll(kept);
      } else {
        var stored = extractQuizData(block, id, qnum, year, subject, title);
        all.push(stored);
        cm[id] = stored;
        btn.classList.add('collected');
        btn.textContent = '已收藏';
        saveAll(all);
      }
    };
  }

  function extractQuizData(block, id, qnum, year, subject, title) {
    var body = block ? block.querySelector('.q-body') : null;
    var isChoice = body && body.querySelector('.exam-option') !== null;
    var question = '', options = [], answer = '', explanation = '';
    if (body) {
      var nodes = body.children;
      var passed = false;
      for (var ni = 0; ni < nodes.length; ni++) {
        var child = nodes[ni];
        if (child.tagName === 'P') {
          var txt = child.textContent.trim();
          if (txt === '[tag_link]') { passed = true; continue; }
          if (!passed) { if (/^[A-D]\s*[.、．]/.test(txt)) break; question += txt + '\n'; }
        }
        if (child.classList && child.classList.contains('exam-option')) {
          var ot = child.querySelector('.opt-text');
          if (ot) options.push(ot.textContent.trim());
        }
      }
      var ap = block.querySelector('.answer-panel');
      if (ap) {
        answer = ap.getAttribute('data-answer') || '';
        for (var ni2 = 1; ni2 < ap.children.length; ni2++) {
          explanation += ap.children[ni2].textContent || '';
        }
      }
    }
    return {
      id: id, type: isChoice ? 'choice' : 'answer', multiple: false,
      subject: subject, source: year ? '408真题' : '习题', years: year ? [year] : [], quizNumber: parseInt(qnum) || 0,
      question: question.trim(), options: isChoice ? options : undefined,
      answer: answer, explanation: explanation.trim(), tags: [],
      pageUrl: window.location.pathname, pageTitle: document.title, collectedAt: new Date().toISOString()
    };
  }

  function selectedQuestions() {
    var source = controls.source.value;
    var year = controls.year.value;
    var set = controls.set.value;
    var subject = controls.subject.value;
    var chapter = controls.chapter.value;
    var type = controls.type.value;
    var search = controls.search.value.trim().toLowerCase();
    return questions.filter(function (q) {
      var matchesSource = !source || q.source === source;
      var matchesYear = !year || (q.years || []).map(String).indexOf(year) !== -1;
      var matchesSet = !set || String(q.set || "") === set;
      var matchesSubject = !subject || q.subject === subject;
      var matchesChapter = !chapter || q.chapter === chapter;
      var matchesType = !type || q.type === type;
      var searchText = [q.title, q.stem, q.subject, q.chapter, q.source].filter(Boolean).join(" ").toLowerCase();
      return matchesSource && matchesYear && matchesSet && matchesSubject && matchesChapter && matchesType && (!search || searchText.indexOf(search) !== -1);
    });
  }

  function populateSelect(select, items, selected, label) {
    var values = [];
    items.forEach(function (item) {
      if (item && values.indexOf(item) === -1) values.push(item);
    });
    select.innerHTML = '<option value="">' + label + '</option>' + values.map(function (value) {
      return '<option value="' + escapeHtml(value) + '">' + escapeHtml(value) + '</option>';
    }).join("");
    if (values.indexOf(selected) !== -1) select.value = selected;
  }

  function updateDependentFilters() {
    var source = controls.source.value;
    document.querySelectorAll(".source-dependent").forEach(function (element) {
      var kind = source === "408真题" ? "exam" : source === "模拟题" ? "simulate" : source === "课后题" ? "exercise" : "none";
      element.classList.toggle("visible", element.classList.contains("source-" + kind));
    });
    if (source !== "408真题") controls.year.value = "";
    if (source !== "模拟题") controls.set.value = "";
    if (source !== "课后题") controls.chapter.value = "";

    var sourceQuestions = questions.filter(function (q) { return !source || q.source === source; });
    var currentSubject = controls.subject.value;
    populateSelect(controls.subject, sourceQuestions.map(function (q) { return q.subject; }), currentSubject, "全部科目");
    var subject = controls.subject.value;
    var chapterQuestions = sourceQuestions.filter(function (q) { return !subject || q.subject === subject; });
    populateSelect(controls.chapter, chapterQuestions.map(function (q) { return q.chapter; }), controls.chapter.value, "全部章节");
  }

  function renderPagination(totalPages) {
    if (totalPages <= 1) {
      controls.pagination.innerHTML = "";
      return;
    }
    var pages = [1, currentPage - 1, currentPage, currentPage + 1, totalPages]
      .filter(function (page) { return page >= 1 && page <= totalPages; })
      .filter(function (page, index, list) { return list.indexOf(page) === index; })
      .sort(function (left, right) { return left - right; });
    var buttons = '<button class="question-page-btn" data-page="' + (currentPage - 1) + '" ' + (currentPage === 1 ? "disabled" : "") + '>上一页</button>';
    var previousPage = 0;
    pages.forEach(function (page) {
      if (page - previousPage > 1) buttons += '<span class="question-page-gap" aria-hidden="true">...</span>';
      buttons += '<button class="question-page-btn' + (page === currentPage ? " active" : "") + '" data-page="' + page + '">' + page + "</button>";
      previousPage = page;
    });
    buttons += '<button class="question-page-btn" data-page="' + (currentPage + 1) + '" ' + (currentPage === totalPages ? "disabled" : "") + '>下一页</button>';
    controls.pagination.innerHTML = buttons;
    controls.pagination.querySelectorAll("[data-page]").forEach(function (button) {
      button.addEventListener("click", function () {
        currentPage = Number(button.dataset.page);
        render();
        grid.scrollIntoView({ block: "start", behavior: "smooth" });
      });
    });
  }

  function render() {
    var filtered = selectedQuestions();
    var totalPages = Math.max(1, Math.ceil(filtered.length / pageSize));
    if (currentPage > totalPages) currentPage = totalPages;
    var start = (currentPage - 1) * pageSize;
    var visible = filtered.slice(start, start + pageSize);
    grid.innerHTML = visible.map(renderCard).join("");
    controls.status.textContent = filtered.length ? "共 " + filtered.length + " 题，当前显示第 " + (start + 1) + " - " + (start + visible.length) + " 题" : "没有符合条件的题目";

    // Process each new question block for interactive features
    grid.querySelectorAll('.question-block').forEach(function(block) {
      processQuestionBlock(block);
    });

    renderPagination(totalPages);
  }

  controls.source.addEventListener("change", function () { currentPage = 1; updateDependentFilters(); render(); });
  controls.year.addEventListener("change", function () { currentPage = 1; render(); });
  controls.set.addEventListener("change", function () { currentPage = 1; render(); });
  controls.subject.addEventListener("change", function () { currentPage = 1; updateDependentFilters(); render(); });
  controls.chapter.addEventListener("change", function () { currentPage = 1; render(); });
  controls.type.addEventListener("change", function () { currentPage = 1; render(); });
  controls.search.addEventListener("input", function () { currentPage = 1; render(); });

  updateDependentFilters();
  render();
})();
