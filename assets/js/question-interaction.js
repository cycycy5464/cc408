/**
 * question-interaction.js
 *
 * Shared module for question block interactive features.
 * Used by: exam single/detail, taxonomy, chapter-exercises, question-list pages.
 *
 * Exposes globals:
 *   toggleAnswer(btn)       — onclick handler for reveal buttons
 *   processQuestionBlocks() — converts all .question-block in #exam-container
 *   setupFavorites()        — binds favorite buttons in #exam-container
 */
(function () {
  'use strict';

  // ── toggleAnswer: global onclick handler ──
  window.toggleAnswer = function (btn) {
    var block = btn.closest('.question-block');
    if (!block) return;
    var panel = block.querySelector('.answer-panel');
    if (!panel) return;
    if (panel.style.display === 'none' || panel.style.display === '') {
      panel.style.display = 'block';
      btn.textContent = '隐藏答案';
      var correct = panel.getAttribute('data-answer');
      if (correct) {
        block.querySelectorAll('.exam-option').forEach(function (opt) {
          if (opt.getAttribute('data-opt') === correct) opt.classList.add('correct');
          else if (opt.classList.contains('selected')) opt.classList.add('wrong');
        });
      }
    } else {
      panel.style.display = 'none';
      btn.textContent = '查看答案与解析';
      block.querySelectorAll('.exam-option').forEach(function (o) { o.classList.remove('correct', 'wrong'); });
    }
  };

  // ── process a single question block ──
  function processBlock(block) {
    var qBody = block.querySelector('.q-body');
    if (!qBody) return;

    // 1. Hide [tag_link] paragraphs
    qBody.querySelectorAll('p').forEach(function (p) {
      if (p.textContent.trim() === '[tag_link]') p.style.display = 'none';
    });

    // 2. Find answer and create answer panel
    var foundAnswer = findAnswerInNode(block);

    // 3. Comprehensive-question fallback: use [tag_link] or tag-only paragraph as anchor
    if (!foundAnswer) {
      var anchor = null;
      var allP = qBody.querySelectorAll('p');
      for (var i = 0; i < allP.length; i++) {
        var p = allP[i];
        var txt = p.textContent.trim();
        if (txt === '[tag_link]') { anchor = p; continue; }
        if (isPureTagParagraph(p)) anchor = p;
      }
      if (anchor) {
        var panel = document.createElement('div');
        panel.className = 'answer-panel';
        panel.style.display = 'none';
        panel.setAttribute('data-answer', '');
        var title = document.createElement('div');
        title.className = 'answer-title';
        title.textContent = '答案与解析：';
        panel.appendChild(title);
        var cur = anchor.nextSibling;
        while (cur) { var nxt = cur.nextSibling; panel.appendChild(cur); cur = nxt; }
        qBody.appendChild(panel);
      }
    }

    // 4. Convert A. B. C. D. options to clickable divs
    convertOptions(qBody);

    // 5. Replace 【解析】 markers
    replaceAnalysisMarkers(block);
  }

  // ── find answer text node and create answer panel ──
  function findAnswerInNode(root) {
    for (var child = root.firstChild; child; child = child.nextSibling) {
      if (child.nodeType === Node.TEXT_NODE) {
        var m = child.textContent.match(/正确答案[：:]\s*([ABCDabcd])/);
        if (m) {
          var answerValue = m[1].toUpperCase();
          var before = child.textContent.substring(0, m.index);
          var after = child.textContent.substring(m.index + m[0].length);
          var panel = document.createElement('div');
          panel.className = 'answer-panel';
          panel.style.display = 'none';
          var title = document.createElement('div');
          title.className = 'answer-title';
          title.innerHTML = '正确答案：<strong>' + answerValue + '</strong>';
          panel.appendChild(title);
          panel.setAttribute('data-answer', answerValue);
          if (before.trim()) child.textContent = before;
          else root.removeChild(child);
          if (after.trim()) root.insertBefore(document.createTextNode(after), child.nextSibling);
          root.insertBefore(panel, child.nextSibling);
          var p = panel.parentNode;
          if (p && p.tagName === 'P') {
            var sib = p.nextSibling;
            while (sib) { var nxt = sib.nextSibling; panel.appendChild(sib); sib = nxt; }
            p.parentNode.insertBefore(panel, p);
            p.parentNode.removeChild(p);
          }
          return true;
        }
      } else if (child.nodeType === Node.ELEMENT_NODE) {
        if (findAnswerInNode(child)) return true;
      }
    }
    return false;
  }

  // ── check if a <p> contains only <a> children (pure tag paragraph) ──
  function isPureTagParagraph(p) {
    if (!p.childNodes.length) return false;
    for (var ci = 0; ci < p.childNodes.length; ci++) {
      var cn = p.childNodes[ci];
      if (cn.nodeType === Node.TEXT_NODE && cn.textContent.trim()) return false;
      if (cn.nodeType === Node.ELEMENT_NODE && cn.tagName !== 'A') return false;
    }
    return true;
  }

  // ── convert option lines in <p> to clickable .exam-option ──
  function convertOptions(qBody) {
    var allP = [];
    for (var i = 0; i < qBody.children.length; i++) {
      if (qBody.children[i].tagName === 'P') allP.push(qBody.children[i]);
    }
    for (var pi = 0; pi < allP.length; pi++) {
      var p = allP[pi];
      var txt = p.textContent.trim();
      var optParts = txt.match(/([A-D])\s*\.\s*(.*?)(?=\s*[A-D]\s*\.|$)/g);
      if (!optParts || optParts.length === 0) continue;

      var fragment = document.createDocumentFragment();
      var firstIdx = txt.search(/[A-D]\s*\./);
      var stemPrefix = firstIdx > 0 ? txt.slice(0, firstIdx).trim() : '';
      if (stemPrefix) {
        var stemP = document.createElement('p');
        stemP.className = 'exam-stem-text';
        stemP.textContent = stemPrefix;
        fragment.appendChild(stemP);
      }
      var created = false;
      for (var oi = 0; oi < optParts.length; oi++) {
        var part = optParts[oi].trim();
        var pm = part.match(/^([A-D])\s*\.\s*(.*)/);
        if (pm) {
          created = true;
          var opt = document.createElement('div');
          opt.className = 'exam-option';
          opt.setAttribute('data-opt', pm[1]);
          opt.innerHTML = '<span class="opt-label">' + pm[1] + '.</span> <span class="opt-text">' + pm[2] + '</span>';
          opt.addEventListener('click', function () {
            var parent = this.parentElement;
            if (parent) {
              parent.querySelectorAll('.exam-option').forEach(function (o) { o.classList.remove('selected'); });
            }
            this.classList.add('selected');
          });
          fragment.appendChild(opt);
        }
      }
      if (created) p.parentNode.replaceChild(fragment, p);
    }
  }

  // ── replace 【解析】 with styled marker ──
  function replaceAnalysisMarkers(root) {
    for (var child = root.firstChild; child; child = child.nextSibling) {
      if (child.nodeType === Node.TEXT_NODE && child.textContent.includes('【解析】')) {
        var h = child.textContent.replace(/【解析】/g, '<div class="analysis-title">解析：</div>');
        var t = document.createElement('div');
        t.innerHTML = h;
        root.replaceChild(t.firstChild, child);
      } else if (child.nodeType === Node.ELEMENT_NODE) {
        replaceAnalysisMarkers(child);
      }
    }
  }

  // ── build consistent favorite ID ──
  function buildFavoriteId(block) {
    var year = block.getAttribute('data-year') || '';
    var number = block.getAttribute('data-number') || '';
    var source = block.getAttribute('data-source') || '';
    if (source === '模拟题') {
      var set = block.getAttribute('data-set') || '';
      return 'sim-' + set + '-' + number;
    }
    if (source === '课后题') {
      var chapter = block.getAttribute('data-chapter') || '';
      return 'ex-' + chapter + '-' + number;
    }
    // default: real exam
    return year ? year + '-' + number : 'q-' + number;
  }

  // ── setup favorite buttons ──
  function setupFavorites(container) {
    var STORAGE_KEY = 'quiz_collections';

    function loadAll() {
      try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []; } catch (e) { return []; }
    }

    function saveAll(items) {
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(items)); } catch (e) {}
    }

    var pageUrl = window.location.pathname;
    var pageTitle = document.title;

    container.querySelectorAll('.favorite-btn').forEach(function (btn) {
      var block = btn.closest('.question-block');
      if (!block) return;

      var id = buildFavoriteId(block);
      var year = block.getAttribute('data-year') || '';
      var qnum = block.getAttribute('data-number') || '';
      var subject = block.getAttribute('data-subject') || '';

      // Check initial state
      var allItems = loadAll();
      var collected = {};
      allItems.forEach(function (item) { collected[item.id] = item; });
      if (collected[id]) { btn.classList.add('collected'); btn.textContent = '已收藏'; }

      btn.onclick = function () {
        var items = loadAll();
        var cm = {};
        items.forEach(function (item) { cm[item.id] = item; });
        if (cm[id]) {
          items = items.filter(function (item) { return item.id !== id; });
          btn.classList.remove('collected');
          btn.textContent = '⭐ 收藏';
          saveAll(items);
        } else {
          var quizData = extractQuizData(block, id, qnum, year, subject);
          items.push(quizData);
          btn.classList.add('collected');
          btn.textContent = '已收藏';
          saveAll(items);
        }
      };
    });
  }

  // ── extract quiz data from DOM for favorites ──
  function extractQuizData(block, id, qnum, year, subject) {
    var body = block ? block.querySelector('.q-body') : null;
    var isChoice = body && body.querySelector('.exam-option') !== null;
    var question = '';
    var options = [];
    var answer = '';
    var explanation = '';

    if (body) {
      var nodes = body.children;
      var passedTagLink = false;
      for (var ni = 0; ni < nodes.length; ni++) {
        var child = nodes[ni];
        if (child.tagName === 'P') {
          var txt = child.textContent.trim();
          if (txt === '[tag_link]') { passedTagLink = true; continue; }
          if (!passedTagLink) {
            if (/^[A-D]\s*[.、．]/.test(txt)) break;
            question += txt + '\n';
          }
        }
        if (child.classList && child.classList.contains('exam-option')) {
          var optText = child.querySelector('.opt-text');
          if (optText) options.push(optText.textContent.trim());
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
      id: id,
      type: isChoice ? 'choice' : 'answer',
      multiple: false,
      subject: subject,
      source: block.getAttribute('data-source') || '408真题',
      years: year ? [year] : [],
      quizNumber: parseInt(qnum) || 0,
      question: question.trim(),
      options: isChoice ? options : undefined,
      answer: answer,
      explanation: explanation.trim(),
      tags: [],
      pageUrl: pageUrl,
      pageTitle: pageTitle,
      collectedAt: new Date().toISOString()
    };
  }

  // ── public API ──
  window.processQuestionBlocks = function () {
    var container = document.getElementById('exam-container');
    if (!container) return;
    container.querySelectorAll('.question-block').forEach(function (block) {
      // Skip already-processed blocks
      if (block.getAttribute('data-processed') === 'true') return;
      processBlock(block);
      block.setAttribute('data-processed', 'true');
    });
  };

  window.setupFavorites = function () {
    var container = document.getElementById('exam-container');
    if (!container) return;
    setupFavorites(container);
  };

  // ── convenience: process + favorites in one call ──
  window.initQuestionBlocks = function () {
    window.processQuestionBlocks();
    window.setupFavorites();
  };

})();
