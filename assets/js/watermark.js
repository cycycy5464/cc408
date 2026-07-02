// CC408 Page Watermark - Canvas-based anti-screenshot
(function() {
  'use strict';

  var WATERMARK_TEXT = 'CC408 · cycycy5464.github.io';
  var WATERMARK_INTERVAL;
  var observer;

  function createWatermark() {
    // Remove existing watermark
    var existing = document.getElementById('cc408-watermark');
    if (existing) existing.remove();

    var canvas = document.createElement('canvas');
    canvas.width = 300;
    canvas.height = 300;
    var ctx = canvas.getContext('2d');

    ctx.save();
    ctx.translate(150, 150);
    ctx.rotate(-Math.PI / 4);
    ctx.font = '14px Inter, sans-serif';
    ctx.fillStyle = 'rgba(255, 255, 255, 0.10)';
    ctx.textAlign = 'center';
    ctx.fillText(WATERMARK_TEXT, 0, 0);
    ctx.restore();

    var dataUrl = canvas.toDataURL();

    var div = document.createElement('div');
    div.id = 'cc408-watermark';
    div.className = 'watermark-layer';
    div.style.backgroundImage = 'url(' + dataUrl + ')';
    document.body.appendChild(div);
  }

  function startWatermark() {
    createWatermark();

    // Protect against removal
    observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        mutation.removedNodes.forEach(function(node) {
          if (node.id === 'cc408-watermark') {
            createWatermark();
          }
        });
      });
    });

    observer.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['style', 'class'] });
  }

  // Start on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startWatermark);
  } else {
    startWatermark();
  }
})();
