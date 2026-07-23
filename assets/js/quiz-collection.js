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
        selectAll: document.getElementById("qc-select-all"),
        deleteSelected: document.getElementById("qc-delete-selected"),
        batchBar: document.getElementById("qc-batch-bar"),
        selectCount: document.getElementById("qc-select-count"),
      };
      this.selectedIds = {};
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

      if (this.el.selectAll) {
        this.el.selectAll.addEventListener("click", () => this.toggleSelectAll());
      }
      if (this.el.deleteSelected) {
        this.el.deleteSelected.addEventListener("click", () => this.batchDelete());
      }
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
      var isDisplay = this.mode === "display";
      var date = new Date(quiz.collectedAt).toLocaleDateString("zh-CN");

      var optionsHtml = "";
      if (isChoice && quiz.options) {
        optionsHtml = quiz.options.map(function (opt, i) {
          var letter = String.fromCharCode(65 + i);
          return '<div class="exam-option" data-opt="' + letter + '"><span class="opt-label">' + letter + '.</span><span class="opt-text">' + opt + "</span></div>";
        }).join("");
      }

      var questionHtml = typeof quiz.question === "string" ? quiz.question : Array.isArray(quiz.question) ? quiz.question.join("<br>") : "";

      var tags = "";
      if (quiz.tags) {
        var tagStr = typeof quiz.tags === 'string' ? quiz.tags : Array.isArray(quiz.tags) ? quiz.tags.join(",") : String(quiz.tags);
        var tagList = [];
        try { tagList = JSON.parse(tagStr); if (!Array.isArray(tagList)) tagList = []; } catch(e) { tagList = []; }
        if (tagList.length === 0) {
          tagList = tagStr.split(",").map(function (t) { return t.replace(/^\[|"|\]$/g, '').trim(); }).filter(Boolean);
        }
        tags = '<div class="qc-card-tags">' + tagList.map(function (t) { return '<span class="tag">' + t + '</span>' }).join("") + '</div>';
      }

      var sourceLabel = this.formatSourceReference(quiz);
      var source = sourceLabel ? '<div class="qc-card-source"><a class="quiz-card-reference" href="' + (quiz.pageUrl || "#") + '" target="_blank" rel="noopener">' + sourceLabel + "</a><span>收藏于 " + date + "</span></div>" : "";

      return '<div class="question-block" data-quiz-id="' + quiz.id + '">' +
        '<label class="qc-select-checkbox"><input type="checkbox" class="qc-card-checkbox" data-id="' + quiz.id + '" onchange="this.closest('.question-block').classList.toggle('qc-selected',this.checked)"><span></span></label>' +
        source +
        tags +
        questionHtml.split("\n").filter(Boolean).map(function (p) { return "<p>" + p + "</p>"; }).join("") +
        (isChoice ? optionsHtml : "") +
        '<div class="answer-panel" style="display:' + (isDisplay ? "block" : "none") + '">' +
        (quiz.answer ? '<div class="answer-title">正确答案：<strong>' + quiz.answer + "</strong></div>" : "") +
        (quiz.explanation ? '<div class="analysis-title">解析：</div><div class="qc-explanation-text">' + quiz.explanation + "</div>" : "") +
        "</div>" +
        '<div class="question-actions">' +
        (isChoice || quiz.explanation ? '<button class="reveal-btn" data-action="reveal">' + (isDisplay ? "隐藏答案与解析" : "查看答案与解析") + '</button>' : "") +
        '<button class="favorite-btn active">★ 已收藏</button>' +
        '<button class="favorite-btn danger" data-action="delete" style="margin-left:auto">🗑 删除</button>' +
        "</div>" +
        "</div>";
    }

    formatSourceReference(quiz) {
      var years = Array.isArray(quiz.years) ? quiz.years : [];
      if (years.length === 0 && quiz.tags) {
        years = String(quiz.tags).match(/20\d{2}/g) || [];
      }
      var number = quiz.quizNumber ? "第" + quiz.quizNumber + "题" : "";
      var source = quiz.source || "";
      var label = "";
      if (source === "408真题" || (!source && years.length > 0)) {
        label = years.length > 0 ? years[0] + "年真题" : "408真题";
      } else if (source === "模拟题") {
        label = quiz.pageTitle || "模拟题";
      } else if (source === "课后题") {
        label = quiz.pageTitle || "章节习题";
      } else {
        label = quiz.pageTitle || "收藏题目";
      }
      return [label, number].filter(Boolean).join(" · ");
    }

    bindCardEvents(card, quiz) {
      var isChoice = quiz.type === "choice";
      var self = this;
      var answerPanel = card.querySelector(".answer-panel");

      card.querySelector('[data-action="delete"]').addEventListener("click", async function () {
        await self.store.remove(quiz.id);
        self.showNotification("已删除", "info");
        await self.loadQuizzes();
      });

      var revealBtn = card.querySelector('[data-action="reveal"]');
      if (revealBtn && answerPanel) {
        revealBtn.addEventListener("click", function () {
          var hidden = answerPanel.style.display === "none";
          answerPanel.style.display = hidden ? "block" : "none";
          revealBtn.textContent = hidden ? "隐藏答案与解析" : "查看答案与解析";

          if (hidden && isChoice) {
            var correct = quiz.answer;
            if (correct) {
              card.querySelectorAll(".exam-option").forEach(function (opt) {
                if (opt.dataset.opt === correct) opt.classList.add("correct");
                else if (opt.classList.contains("selected")) opt.classList.add("wrong");
              });
            }
          } else {
            card.querySelectorAll(".exam-option").forEach(function (o) { o.classList.remove("correct", "wrong"); });
          }
        });
      }

      if (isChoice) {
        var options = card.querySelectorAll(".exam-option");
        if (this.mode === "practice") {
          options.forEach(function (opt) {
            opt.addEventListener("click", function () { self.selectOption(card, quiz, opt); });
          });
        } else {
          this.showDisplayOptions(card, quiz);
        }
      }
    }

    selectOption(card, quiz, opt) {
      var letter = opt.dataset.opt;
      var allOptions = card.querySelectorAll(".exam-option");

      if (quiz.multiple) {
        opt.classList.toggle("selected");
      } else {
        allOptions.forEach(function (o) { o.classList.remove("selected"); });
        opt.classList.add("selected");
        this.checkAnswer(card, quiz, letter);
      }
    }

    checkAnswer(card, quiz, selectedLetter) {
      var correct = (quiz.answer || "").toUpperCase().trim();
      var answerPanel = card.querySelector(".answer-panel");

      card.querySelectorAll(".exam-option").forEach(function (o) {
        o.style.pointerEvents = "none";
        if (o.dataset.opt === correct) o.classList.add("correct");
        else if (o.classList.contains("selected")) o.classList.add("wrong");
      });

      if (answerPanel) {
        answerPanel.style.display = "block";
        var title = answerPanel.querySelector(".answer-title");
        var isCorrect = selectedLetter === correct;
        if (title) {
          title.innerHTML = "正确答案：<strong>" + correct + "</strong> " + (isCorrect ? "✅" : "❌");
        }
      }
    }

    showDisplayOptions(card, quiz) {
      var correctAnswers = (quiz.answer || "").split(/[,，\s]+/).map(function (a) { return a.trim().toUpperCase(); }).filter(Boolean);
      card.querySelectorAll(".exam-option").forEach(function (o) {
        o.classList.add("display-mode");
        if (correctAnswers.indexOf(o.dataset.opt) !== -1) {
          o.classList.add("correct-shown");
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

    toggleSelectAll() {
      var checkboxes = document.querySelectorAll(".qc-card-checkbox");
      var allChecked = Array.from(checkboxes).every(function(cb) { return cb.checked; });
      checkboxes.forEach(function(cb) {
        cb.checked = !allChecked;
        cb.closest(".question-block").classList.toggle("qc-selected", !allChecked);
      });
      this.el.selectAll.textContent = allChecked ? "全选" : "取消全选";
      this.updateBatchBar();
    }

    updateBatchBar() {
      var count = document.querySelectorAll(".qc-card-checkbox:checked").length;
      if (this.el.batchBar) {
        this.el.batchBar.style.display = count > 0 ? "flex" : "none";
      }
      if (this.el.selectCount) {
        this.el.selectCount.textContent = count + " 项选中";
      }
    }

    batchDelete() {
      var ids = [];
      document.querySelectorAll(".qc-card-checkbox:checked").forEach(function(cb) {
        ids.push(cb.getAttribute("data-id"));
      });
      if (!ids.length) return;
      if (!confirm("确定删除选中的 " + ids.length + " 项收藏？")) return;
      var self = this;
      ids.forEach(async function(id) {
        await self.store.remove(id);
      });
      this.selectedIds = {};
      this.loadQuizzes();
      this.showNotification("已删除 " + ids.length + " 项", "info");
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
