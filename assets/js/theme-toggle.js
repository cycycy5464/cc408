/**
 * CC408 主题切换
 * - 在 <html data-theme="dark|light"> 上切换
 * - 持久化到 localStorage('cc408-theme')
 * - 初始值由 baseof.html 的内联脚本根据系统偏好/本地存储设定（防止闪烁）
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'cc408-theme';

  function getCurrent() {
    return document.documentElement.getAttribute('data-theme') || 'dark';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) { /* 隐私模式可能禁用 localStorage，忽略即可 */ }
  }

  function updateButton(btn) {
    if (!btn) return;
    var isLight = getCurrent() === 'light';
    btn.setAttribute('aria-pressed', String(isLight));
    btn.setAttribute('aria-label', isLight ? '切换到深色模式' : '切换到浅色模式');
    btn.title = isLight ? '切换到深色模式' : '切换到浅色模式';
    var icon = btn.querySelector('.theme-toggle-icon');
    if (icon) icon.textContent = isLight ? '☀' : '🌙';
  }

  function toggle() {
    applyTheme(getCurrent() === 'dark' ? 'light' : 'dark');
    updateButton(document.querySelector('.theme-toggle-btn'));
  }

  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.querySelector('.theme-toggle-btn');
    if (btn) btn.addEventListener('click', toggle);
    updateButton(btn);
  });
})();
