// CC408 Resource Filter - Pure frontend filtering
(function() {
  'use strict';

  var searchInput = document.getElementById('filter-search');
  var subjectSelect = document.getElementById('filter-subject');
  var difficultySelect = document.getElementById('filter-difficulty');

  if (!searchInput || !subjectSelect || !difficultySelect) return;

  function filterCards() {
    var searchTerm = searchInput.value.toLowerCase();
    var subject = subjectSelect.value;
    var difficulty = difficultySelect.value;

    var cards = document.querySelectorAll('.card-glass[data-subject]');
    cards.forEach(function(card) {
      var cardSubject = card.getAttribute('data-subject');
      var cardDifficulty = card.getAttribute('data-difficulty');
      var cardText = card.textContent.toLowerCase();

      var matchSubject = !subject || cardSubject === subject;
      var matchDifficulty = !difficulty || cardDifficulty === difficulty;
      var matchSearch = !searchTerm || cardText.indexOf(searchTerm) !== -1;

      card.style.display = (matchSubject && matchDifficulty && matchSearch) ? '' : 'none';
    });
  }

  searchInput.addEventListener('input', filterCards);
  subjectSelect.addEventListener('change', filterCards);
  difficultySelect.addEventListener('change', filterCards);
})();
