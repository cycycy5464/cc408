(function () {
  "use strict";

  const STORAGE_KEY = "quiz_collections";

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
    } catch (e) {
      console.error("Failed to save to localStorage:", e);
    }
  }

  class QuizStore {
    async getAll() { return loadAll(); }

    async get(id) {
      const items = loadAll();
      return items.find(function (q) { return q.id === id; }) || null;
    }

    async add(quiz) {
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

    async remove(id) {
      var items = loadAll();
      var kept = [];
      for (var i = 0; i < items.length; i++) {
        if (items[i].id !== id) kept.push(items[i]);
      }
      saveAll(kept);
    }

    async clearAll() {
      saveAll([]);
    }
  }

  class QuizCollectionApp {
    constructor() {
      this.store = new QuizStore();
      this.quizzes = [];
      this.filtered = [];
      this.mode = "practice";
      this.layout = 2;
      this.subjectFilter = null;
      this.tagFilter = null;
      this.searchQuery = "";
      this.selections = {};
      this.init();
    }

    async init() {
      this.cacheElements();
      this.bindEvents();
      await this.loadQuizzes();
    }

    cacheElements() {
      this.el = {
        stats: document.getElementById("qc-stats"),
        toolbar: document.getElementById("qc-toolbar"),
        search: document.getElementById("qc-search"),
        filters: document.getElementById("qc-filters"),
        subjectFilters: document.getElementById("qc-subject-filters"),
        tagFilters: document.getElementById("qc-tag-filters"),
        grid: document.getElementById("qc-grid"),
        empty: document.getElementById("qc-empty"),
        exportBtn: document.getElementById("qc-export"),
        importBtn: document.getElementById("qc-import"),
        clearBtn: document.getElementById("qc-clear"),
      };
    }

    bindEvents() {
      this.el.search.addEventListener("input", () => {
        this.searchQuery = this.el.search.value.toLowerCase();
        this.applyFilters();
      });

      this.el.toolbar.querySelectorAll(".qc-mode-btn").forEach((btn) => {
        btn.addEventListener("click", () => this.changeMode(btn.dataset.mode));
      });

      this.el.toolbar.querySelectorAll(".qc-layout-btn").forEach((btn) => {
        btn.addEventListener("click", () => this.changeLayout(parseInt(btn.dataset.cols)));
      });

      this.el.exportBtn.addEventListener("click", () => this.exportCollections());
      this.el.importBtn.addEventListener("click", () => {
        const input = document.createElement("input");
        input.type = "file";
        input.accept = ".json";
        input.classList.add("qc-hidden-input");
        input.addEventListener("change", (e) => this.importCollections(e));
        input.click();
      });
      this.el.clearBtn.addEventListener("click", () => this.clearAll());
    }

    async loadQuizzes() {
      this.quizzes = await this.store.getAll();
      this.quizzes.sort(function (a, b) {
        return new Date(b.collectedAt) - new Date(a.collectedAt);
      });
      this.applyFilters();
    }

    updateStats(quizzes) {
      var total = quizzes.length;
      var choices = 0, answers = 0;
      for (var i = 0; i < quizzes.length; i++) {
        if (quizzes[i].type === "choice") choices++;
        else answers++;
      }
      var subjects = {};
      var allTags = {};
      for (var i = 0; i < quizzes.length; i++) {
        var q = quizzes[i];
        if (q.subject) subjects[q.subject] = true;
        if (q.tags) {
          q.tags.split(",").forEach(function (t) {
            var tag = t.trim();
            if (tag) allTags[tag] = true;
          });
        }
      }
      var subjCount = 0; for (var k in subjects) subjCount++;
      var tagCount = 0; for (var k in allTags) tagCount++;

      this.el.stats.innerHTML = [
        { value: total, label: "总题目数" },
        { value: choices, label: "选择题" },
        { value: answers, label: "解答题" },
        { value: subjCount, label: "科目分类" },
        { value: tagCount, label: "标签分类" },
      ]
        .map(function (s) { return '<div class="qc-stat-item"><div class="qc-stat-value">' + s.value + '</div><div class="qc-stat-label">' + s.label + '</div></div>'; })
        .join("");
    }

    createSubjectFilters(quizzes) {
      var subjects = {};
      for (var i = 0; i < quizzes.length; i++) {
        var s = quizzes[i].subject;
        if (s) subjects[s] = true;
      }
      var keys = Object.keys(subjects);
      if (keys.length < 2) {
        this.el.filters.style.display = "none";
        return;
      }
      this.el.filters.style.display = "block";
      var html = ['<span class="qc-filter-label">科目:</span>'];
      var self = this;
      keys.forEach(function (s) {
        html.push('<button class="qc-filter-btn' + (self.subjectFilter === s ? " active" : "") + '" data-subject="' + s + '">' + s + "</button>");
      });
      this.el.subjectFilters.innerHTML = html.join("");

      this.el.subjectFilters.querySelectorAll(".qc-filter-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var subj = btn.dataset.subject;
          self.subjectFilter = self.subjectFilter === subj ? null : subj;
          self.applyFilters();
        });
      });
    }

    createTagFilters(quizzes) {
      var tagSet = {};
      for (var i = 0; i < quizzes.length; i++) {
        var q = quizzes[i];
        if (q.tags) {
          q.tags.split(",").forEach(function (t) {
            var tag = t.trim();
            if (tag) tagSet[tag] = true;
          });
        }
      }
      var tags = Object.keys(tagSet);
      if (tags.length < 2) return;
      var html = ['<span class="qc-filter-label">标签:</span>'];
      var self = this;
      tags.forEach(function (t) {
        html.push('<button class="qc-filter-btn' + (self.tagFilter === t ? " active" : "") + '" data-tag="' + t + '">' + t + "</button>");
      });
      this.el.tagFilters.innerHTML = html.join("");

      this.el.tagFilters.querySelectorAll(".qc-filter-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var tag = btn.dataset.tag;
          self.tagFilter = self.tagFilter === tag ? null : tag;
          self.applyFilters();
        });
      });
    }

    applyFilters() {
      var result = [];
      for (var i = 0; i < this.quizzes.length; i++) {
        result.push(this.quizzes[i]);
      }
      if (this.subjectFilter) {
        result = result.filter(function (q) { return q.subject === this; }.bind(this.subjectFilter));
      }
      if (this.tagFilter) {
        result = result.filter(function (q) { return q.tags && q.tags.split(",").map(function (t) { return t.trim(); }).indexOf(this) !== -1; }.bind(this.tagFilter));
      }
      if (this.searchQuery) {
        var q = this.searchQuery;
        result = result.filter(function (quiz) {
          var text = [quiz.question, quiz.answer, quiz.explanation, quiz.subject, quiz.tags, quiz.pageTitle].filter(Boolean).join(" ").toLowerCase();
          return text.indexOf(q) !== -1;
        });
      }
      this.filtered = result;
      this.updateStats(this.quizzes);
      this.createSubjectFilters(this.quizzes);
      this.createTagFilters(this.quizzes);
      this.displayQuizzes();
    }

    displayQuizzes() {
      this.selections = {};
      if (this.filtered.length === 0) {
        this.el.grid.style.display = "none";
        this.el.empty.style.display = "block";
        return;
      }
      this.el.grid.style.display = "grid";
      this.el.empty.style.display = "none";
      this.el.grid.className = "qc-grid cols-" + this.layout;
      var self = this;
      this.el.grid.innerHTML = this.filtered.map(function (quiz) { return self.createQuizCard(quiz); }).join("");
      this.filtered.forEach(function (quiz) {
        var card = document.querySelector('[data-quiz-id="' + quiz.id + '"]');
        if (card) self.bindCardEvents(card, quiz);
      });
    }

    createQuizCard(quiz) {
      var isChoice = quiz.type === "choice";
      var badgeClass = isChoice ? "choice-type" : "answer-type";
      var badgeText = isChoice ? "选择题" : "解答题";
      var date = new Date(quiz.collectedAt).toLocaleDateString("zh-CN");

      var tags = "";
      if (quiz.tags) {
        tags = quiz.tags.split(",").map(function (t) { return t.trim(); }).filter(Boolean).map(function (t) { return '<span class="qc-card-tag">' + t + "</span>"; }).join("");
      }

      var optionsHtml = "";
      if (isChoice && quiz.options) {
        var isMulti = quiz.multiple;
        optionsHtml = '<div class="qc-options">' +
          quiz.options.map(function (opt, i) {
            var letter = String.fromCharCode(65 + i);
            var markerClass = isMulti ? "multi" : "";
            return '<button class="qc-option ' + markerClass + '" data-opt-index="' + i + '" data-opt-letter="' + letter + '"><span class="qc-option-marker"></span><span>' + opt + "</span></button>";
          }).join("") +
          "</div>" +
          (isMulti ? '<div class="qc-multiple-hint">可多选</div>' : "");
      }

      var questionHtml = typeof quiz.question === "string" ? quiz.question : Array.isArray(quiz.question) ? quiz.question.join("<br>") : "";

      return '<div class="qc-card" data-quiz-id="' + quiz.id + '">' +
        '<div class="qc-card-header">' +
        '<span class="qc-type-badge ' + badgeClass + '">' + badgeText + '</span>' +
        '<span class="qc-subject-tag">' + (quiz.subject || "") + '</span>' +
        "</div>" +
        '<div class="qc-card-meta">' +
        (quiz.pageTitle ? '<a href="' + (quiz.pageUrl || "#") + '" target="_blank" rel="noopener">' + quiz.pageTitle + "</a>" : "") +
        "<span>" + date + "</span>" +
        "</div>" +
        (tags ? '<div class="qc-card-tags">' + tags + "</div>" : "") +
        '<div class="qc-question-text">' + questionHtml + "</div>" +
        (isChoice ? optionsHtml : "") +
        '<div class="qc-answer">' +
        (this.mode === "display" ? '<div class="qc-answer-text">正确答案：' + quiz.answer + "</div>" : "") +
        (this.mode === "display" ? '<div class="qc-explanation">' + (quiz.explanation || "") + "</div>" : "") +
        (this.mode === "practice" && !isChoice ? '<button class="qc-check-answer-btn">👁 查看答案</button>' : "") +
        (this.mode === "practice" && !isChoice ? '<div class="qc-explanation hidden">' + (quiz.explanation || "") + "</div>" : "") +
        '<div class="qc-result-message" style="display:none"></div>' +
        "</div>" +
        '<div class="qc-card-actions">' +
        '<button class="qc-card-btn danger" data-action="delete">🗑 删除</button>' +
        "</div>" +
        "</div>";
    }

    bindCardEvents(card, quiz) {
      var isChoice = quiz.type === "choice";
      var self = this;

      card.querySelector('[data-action="delete"]').addEventListener("click", async function () {
        await self.store.remove(quiz.id);
        self.showNotification("已删除", "info");
        await self.loadQuizzes();
      });

      if (isChoice) {
        var options = card.querySelectorAll(".qc-option");
        if (this.mode === "practice") {
          options.forEach(function (opt) {
            opt.addEventListener("click", function () { self.selectOption(card, quiz, opt); });
          });
        } else {
          this.showDisplayOptions(card, quiz);
        }
      }

      if (!isChoice && this.mode === "practice") {
        var checkBtn = card.querySelector(".qc-check-answer-btn");
        var explanation = card.querySelector(".qc-explanation");
        if (checkBtn && explanation) {
          checkBtn.addEventListener("click", function () {
            var hidden = explanation.classList.toggle("hidden");
            checkBtn.textContent = hidden ? "👁 查看答案" : "🙈 隐藏答案";
          });
        }
      }
    }

    selectOption(card, quiz, opt) {
      var isMulti = quiz.multiple;
      var idx = opt.dataset.optIndex;
      var allOptions = card.querySelectorAll(".qc-option");
      var resultMsg = card.querySelector(".qc-result-message");

      if (!this.selections[quiz.id]) this.selections[quiz.id] = [];
      var selected = this.selections[quiz.id];

      if (isMulti) {
        var pos = selected.indexOf(idx);
        if (pos > -1) selected.splice(pos, 1);
        else selected.push(idx);
        allOptions.forEach(function (o) {
          o.classList.toggle("selected", selected.indexOf(o.dataset.optIndex) !== -1);
        });
      } else {
        selected = [idx];
        this.selections[quiz.id] = selected;
        allOptions.forEach(function (o) {
          o.classList.toggle("selected", o.dataset.optIndex === idx);
        });
        this.checkAnswer(card, quiz, selected, resultMsg);
      }
    }

    checkAnswer(card, quiz, selected, resultMsg) {
      var correctAnswers = quiz.answer.split(/[,，\s]+/).map(function (a) { return a.trim().toUpperCase(); }).filter(Boolean);
      var selectedLetters = selected.map(function (i) { return String.fromCharCode(65 + parseInt(i)); });
      var allOptions = card.querySelectorAll(".qc-option");

      var isCorrect = correctAnswers.length === selectedLetters.length && correctAnswers.every(function (a) { return selectedLetters.indexOf(a) !== -1; });

      allOptions.forEach(function (o) {
        o.style.pointerEvents = "none";
        var letter = o.dataset.optLetter;
        if (correctAnswers.indexOf(letter) !== -1) o.classList.add("correct");
        else if (selected.indexOf(o.dataset.optIndex) !== -1 && correctAnswers.indexOf(letter) === -1) o.classList.add("wrong");
      });

      resultMsg.style.display = "block";
      resultMsg.className = "qc-result-message " + (isCorrect ? "correct" : "wrong");
      resultMsg.textContent = isCorrect ? "✅ 正确！" : "❌ 错误，正确答案是：" + quiz.answer;
    }

    showDisplayOptions(card, quiz) {
      var correctAnswers = quiz.answer.split(/[,，\s]+/).map(function (a) { return a.trim().toUpperCase(); }).filter(Boolean);
      card.querySelectorAll(".qc-option").forEach(function (o) {
        o.classList.add("display-mode");
        var letter = o.dataset.optLetter;
        if (correctAnswers.indexOf(letter) !== -1) {
          o.classList.add("correct-shown");
          var marker = o.querySelector(".qc-option-marker");
          if (marker) marker.textContent = "✓";
        } else {
          o.classList.add("wrong-shown");
        }
        o.style.pointerEvents = "none";
      });
    }

    changeMode(mode) {
      this.mode = mode;
      this.el.toolbar.querySelectorAll(".qc-mode-btn").forEach(function (btn) {
        btn.classList.toggle("active", btn.dataset.mode === mode);
      });
      this.displayQuizzes();
    }

    changeLayout(cols) {
      this.layout = cols;
      this.el.toolbar.querySelectorAll(".qc-layout-btn").forEach(function (btn) {
        btn.classList.toggle("active", parseInt(btn.dataset.cols) === cols);
      });
      if (this.filtered.length > 0) {
        this.el.grid.className = "qc-grid cols-" + cols;
      }
    }

    async exportCollections() {
      var all = await this.store.getAll();
      if (all.length === 0) {
        this.showNotification("没有可导出的收藏", "info");
        return;
      }
      var blob = new Blob([JSON.stringify(all, null, 2)], { type: "application/json" });
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      var now = new Date().toISOString().slice(0, 10);
      a.download = "quiz-collections-" + now + ".json";
      a.click();
      URL.revokeObjectURL(url);
      this.showNotification("导出成功", "success");
    }

    async importCollections(e) {
      var file = e.target.files[0];
      if (!file) return;
      try {
        var text = await file.text();
        var data = JSON.parse(text);
        if (!Array.isArray(data)) throw new Error("格式错误：需要数组");
        var count = 0;
        for (var i = 0; i < data.length; i++) {
          if (data[i].id) {
            await this.store.add(data[i]);
            count++;
          }
        }
        this.showNotification("成功导入 " + count + " 条收藏", "success");
        await this.loadQuizzes();
      } catch (err) {
        this.showNotification("导入失败：" + err.message, "error");
      }
    }

    async clearAll() {
      if (this.quizzes.length === 0) {
        this.showNotification("没有可清空的收藏", "info");
        return;
      }
      if (!confirm("确定要清空所有收藏吗？此操作不可恢复。")) return;
      await this.store.clearAll();
      this.showNotification("已清空所有收藏", "info");
      await this.loadQuizzes();
    }

    showNotification(msg, type) {
      var existing = document.querySelector(".qc-notification");
      if (existing) existing.remove();
      var el = document.createElement("div");
      el.className = "qc-notification " + (type || "info");
      el.textContent = msg;
      document.body.appendChild(el);
      setTimeout(function () {
        el.style.opacity = "0";
        el.style.transition = "opacity 0.3s";
        setTimeout(function () { el.remove(); }, 300);
      }, 2500);
    }
  }

  if (document.getElementById("quiz-collection-app")) {
    new QuizCollectionApp();
  }
})();
