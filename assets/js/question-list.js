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
    section: document.getElementById("filter-section"),
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

  function stars(difficulty) {
    var result = "";
    for (var index = 1; index <= 4; index++) result += index <= difficulty ? "★" : "☆";
    return result;
  }

  function renderCard(question) {
    var type = question.type === "comprehensive" ? "解答题" : "选择题";
    var summary = question.stem || question.title;
    var year = question.years && question.years[0] || "";
    // Show section+number for chapter exercises
    var title = question.source === "课后题" && question.section
      ? question.section + " 第" + question.number + "题"
      : question.title;
    return '<a class="question-card quiz-summary-card" href="' + escapeHtml(question.url) + '">' +
      '<div class="quiz-card-reference">' + escapeHtml(sourceReference(question)) + '</div>' +
      '<div class="stem">' + escapeHtml(title) + '</div>' +
      '<div class="meta">' +
      '<span class="tag">' + escapeHtml(question.subject) + '</span>' +
      '<span class="tag tag-warm">' + type + '</span>' +
      '<span class="quiz-card-difficulty" aria-label="难度 ' + question.difficulty + '">' + stars(question.difficulty) + '</span>' +
      '</div></a>';
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
      var matchesSection = !section || q.section === section;
      var matchesType = !type || q.type === type;
      var searchText = [q.title, q.stem, q.subject, q.chapter, q.section, q.source].filter(Boolean).join(" ").toLowerCase();
      return matchesSource && matchesYear && matchesSet && matchesSubject && matchesChapter && matchesSection && matchesType && (!search || searchText.indexOf(search) !== -1);
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
    if (source !== "课后题") controls.section.value = "";
    controls.section.style.display = (source === "课后题" && controls.chapter.value) ? "inline-block" : "none";

    var sourceQuestions = questions.filter(function (q) { return !source || q.source === source; });
    var currentSubject = controls.subject.value;
    populateSelect(controls.subject, sourceQuestions.map(function (q) { return q.subject; }), currentSubject, "全部科目");
    var subject = controls.subject.value;
    var chapterQuestions = sourceQuestions.filter(function (q) { return !subject || q.subject === subject; });
    populateSelect(controls.chapter, chapterQuestions.map(function (q) { return q.chapter; }), controls.chapter.value, "选择章节");

    // Populate sections
    var ch = controls.chapter.value;
    controls.section.innerHTML = "<option value=\"\">全部小节</option>";
    if (ch) {
      var secSet = {};
      chapterQuestions.filter(function (q) { return q.chapter === ch && q.section; }).forEach(function (q) { secSet[q.section] = true; });
      Object.keys(secSet).sort().forEach(function (s) {
        var o = document.createElement("option");
        o.value = s; o.textContent = s;
        controls.section.appendChild(o);
      });
    }
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


    renderPagination(totalPages);
  }

  controls.source.addEventListener("change", function () { currentPage = 1; updateDependentFilters(); render(); });
  controls.year.addEventListener("change", function () { currentPage = 1; render(); });
  controls.set.addEventListener("change", function () { currentPage = 1; render(); });
  controls.subject.addEventListener("change", function () { currentPage = 1; updateDependentFilters(); render(); });
  controls.chapter.addEventListener("change", function () { currentPage = 1; updateDependentFilters(); render(); });
  controls.section.addEventListener("change", function () { currentPage = 1; render(); });
  controls.type.addEventListener("change", function () { currentPage = 1; render(); });
  controls.search.addEventListener("input", function () { currentPage = 1; render(); });

  updateDependentFilters();
  render();
})();
