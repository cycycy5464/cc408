(function () {
  "use strict";

  var STORAGE_KEY = "quiz_collections";

  function loadAll() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    } catch (e) {
      return [];
    }
  }

  function saveAll(items) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    } catch (e) {}
  }

  function getQuiz(id) {
    var items = loadAll();
    for (var i = 0; i < items.length; i++) {
      if (items[i].id === id) return items[i];
    }
    return null;
  }

  function saveQuiz(quiz) {
    var items = loadAll();
    var found = false;
    for (var i = 0; i < items.length; i++) {
      if (items[i].id === quiz.id) {
        items[i] = quiz;
        found = true;
        break;
      }
    }
    if (!found) items.push(quiz);
    saveAll(items);
  }

  function removeQuiz(id) {
    var items = loadAll();
    var kept = [];
    for (var i = 0; i < items.length; i++) {
      if (items[i].id !== id) kept.push(items[i]);
    }
    saveAll(kept);
  }

  function extractQuizData() {
    var container = document.getElementById("exam-container");
    if (!container) return null;

    var pageUrl = window.location.pathname;
    var pageTitle = document.title;
    var meta = window.quizMeta || {};
    var isChoice = meta.questionType === "choice";

    var options = [];
    container.querySelectorAll(".exam-option").forEach(function (el) {
      var textEl = el.querySelector(".opt-text");
      if (textEl) options.push(textEl.textContent.trim());
    });

    var answerPanel = container.querySelector(".answer-panel");
    var answer = answerPanel ? answerPanel.getAttribute("data-answer") || "" : "";

    var explanation = "";
    var answerContents = container.querySelector(".answer-panel");
    if (answerContents) {
      var children = answerContents.children;
      for (var i = 1; i < children.length; i++) {
        explanation += children[i].textContent || "";
      }
    }

    var tags = [];
    function ensureArray(v) { return Array.isArray(v) ? v : typeof v === 'string' ? [v] : []; }
    ensureArray(meta.knowledgePoints).forEach(function(t) { tags.push(t); });
    ensureArray(meta.years).forEach(function(t) { tags.push(t); });
    if (meta.questionType) tags.push(isChoice ? "选择题" : "解答题");

    var question = "";
    var ps = container.querySelectorAll("p");
    for (var i = 0; i < ps.length; i++) {
      var p = ps[i];
      if (p.closest(".answer-panel")) continue;
      if (p.style.display === "none") continue;
      var txt = p.textContent.trim();
      if (txt === "[tag_link]") continue;
      if (/^[A-D][.、．]/.test(txt)) break;
      question += txt + "\n";
    }
    question = question.replace(/【解析】.*/s, "").replace(/正确答案[：:].*/s, "").trim();

    var subject = meta.subjects && meta.subjects.length > 0 ? meta.subjects[0] : "";
    var year = meta.years && meta.years.length > 0 ? String(meta.years[0]) : "";
    var number = meta.quizNumber || 0;
    var id = year ? year + "-" + number : pageUrl.replace(/\//g, "-");

    return {
      id: id,
      type: isChoice ? "choice" : "answer",
      multiple: false,
      subject: subject,
      source: meta.source || "",
      years: ensureArray(meta.years),
      quizNumber: meta.quizNumber || 0,
      question: question,
      options: isChoice ? options : undefined,
      answer: answer,
      explanation: explanation,
      tags: tags.join(","),
      pageUrl: pageUrl,
      pageTitle: pageTitle,
      collectedAt: new Date().toISOString(),
    };
  }

  function initFavoriteButton() {
    var btn = document.getElementById("fav-btn");
    if (!btn) return;

    var quizData = extractQuizData();
    if (!quizData) return;

    var existing = getQuiz(quizData.id);
    if (existing) {
      btn.classList.add("active");
      btn.innerHTML = "★ 已收藏";
    }

    btn.onclick = function () {
      var isActive = btn.classList.contains("active");
      if (isActive) {
        removeQuiz(quizData.id);
        btn.classList.remove("active");
        btn.innerHTML = "⭐ 收藏";
        showToast("已取消收藏", "info");
      } else {
        saveQuiz(quizData);
        btn.classList.add("active");
        btn.innerHTML = "★ 已收藏";
        showToast("已收藏", "success");
      }
    };
  }

  function showToast(msg, type) {
    var existing = document.querySelector(".collect-toast");
    if (existing) existing.remove();
    var el = document.createElement("div");
    el.className = "collect-toast";
    el.textContent = msg;
    el.style.cssText = "position:fixed;bottom:2rem;right:2rem;z-index:9999;padding:.6rem 1.2rem;border-radius:8px;font-size:.875rem;color:#0a0e14;font-weight:500;box-shadow:0 2px 12px rgba(0,0,0,.3);transition:opacity .3s;background:" + (type === "success" ? "#2ecc71" : "#39bae6");
    document.body.appendChild(el);
    setTimeout(function () {
      el.style.opacity = "0";
      setTimeout(function () { el.remove(); }, 300);
    }, 2000);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initFavoriteButton);
  } else {
    initFavoriteButton();
  }
})();
