// CC408 Resource Filter - with debounce
(function() {
  'use strict';
  var searchInput = document.getElementById('filter-search');
  var subjectSelect = document.getElementById('filter-subject');
  var difficultySelect = document.getElementById('filter-difficulty');
  if (!searchInput || !subjectSelect || !difficultySelect) return;

  function debounce(fn, ms) {
    var t;
    return function() { clearTimeout(t); t = setTimeout(fn, ms); };
  }

  function filterCards() {
    var searchTerm = searchInput.value.toLowerCase();
    var subject = subjectSelect.value;
    var difficulty = difficultySelect.value;
    var cards = document.querySelectorAll('.card-glass[data-subject]');
    cards.forEach(function(card) {
      var matchSubject = !subject || card.getAttribute('data-subject') === subject;
      var matchDifficulty = !difficulty || card.getAttribute('data-difficulty') === difficulty;
      var matchSearch = !searchTerm || card.textContent.toLowerCase().indexOf(searchTerm) !== -1;
      card.style.display = (matchSubject && matchDifficulty && matchSearch) ? '' : 'none';
    });
  }

  searchInput.addEventListener('input', debounce(filterCards, 200));
  subjectSelect.addEventListener('change', filterCards);
  difficultySelect.addEventListener('change', filterCards);
})();
