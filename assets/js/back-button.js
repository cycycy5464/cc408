/**
 * 智能返回按钮逻辑
 * 功能：
 * 1. 智能判断返回目标
 * 2. 保存和恢复页面状态
 * 3. 处理浏览器历史记录
 */

(function() {
  'use strict';
  
  // 页面状态存储Key前缀
  const STATE_KEY_PREFIX = 'cc408-page-state-';
  const HISTORY_KEY = 'cc408-navigation-history';
  
  // 防重复保存：同 path 500ms 内跳过
  var lastSavedPath = '';
  var lastSavedTime = 0;
  var globalLinksInitialized = false;
  
  // 获取baseURL
  function getBaseURL() {
    // 尝试从导航栏链接获取baseURL
    const navLinks = document.querySelectorAll('.navbar a[href]');
    for (const link of navLinks) {
      const href = link.getAttribute('href');
      if (href && href.startsWith('/') && !href.startsWith('//')) {
        // 提取baseURL部分
        const parts = href.split('/');
        if (parts.length > 1) {
          return '/' + parts[1] + '/';
        }
      }
    }
    // 默认返回/cc408/
    return '/cc408/';
  }
  
  /**
   * 保存导航历史
   */
  function saveNavigationHistory(fromPath, toPath) {
    try {
      let history = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
      
      // 添加新记录
      history.push({
        from: fromPath,
        to: toPath,
        timestamp: Date.now()
      });
      
      // 只保留最近20条记录
      if (history.length > 20) {
        history = history.slice(-20);
      }
      
      localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
    } catch (e) {
      console.warn('保存导航历史失败:', e);
    }
  }
  
  /**
   * 获取上一个页面
   */
  function getPreviousPage(currentPath) {
    try {
      const history = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
      
      // 优先：找到"导航到当前页"的记录，返回其 from（真正的上一页）
      for (let i = history.length - 1; i >= 0; i--) {
        if (history[i].to === currentPath) {
          return history[i].from;
        }
      }
      
      // 备选：返回最近的、不是当前页面的目标页
      for (let i = history.length - 1; i >= 0; i--) {
        if (history[i].to !== currentPath) {
          return history[i].to;
        }
      }
    } catch (e) {
      console.warn('获取导航历史失败:', e);
    }
    
    return null;
  }
  
  /**
   * 智能判断返回目标
   */
  function getSmartBackTarget(currentPath) {
    const baseURL = getBaseURL();
    
    // 1. 首先检查是否有自定义返回URL
    const backButton = document.querySelector('.back-button[data-back-url]');
    if (backButton) {
      const customUrl = backButton.getAttribute('data-back-url');
      // 如果是相对路径，添加baseURL
      if (customUrl && !customUrl.startsWith('http')) {
        return baseURL + customUrl.replace(/^\//, '');
      }
      return customUrl;
    }
    
    // 2. 检查导航历史
    const previousPage = getPreviousPage(currentPath);
    if (previousPage) {
      // 确保上一个页面不是当前页面
      if (previousPage !== currentPath) {
        return previousPage;
      }
    }
    
    // 3. 使用默认返回目标
    // 根据页面类型确定返回目标
    if (currentPath.includes('/docs/')) {
      return baseURL + 'docs/';
    } else if (currentPath.includes('/exam/')) {
      return baseURL + 'exam/';
    } else if (currentPath.includes('/question/')) {
      return baseURL + 'question/';
    } else if (currentPath.includes('/resources/')) {
      return baseURL + 'resources/';
    } else if (currentPath.includes('/graph/')) {
      return baseURL;
    } else if (currentPath.includes('/tags/')) {
      return baseURL;
    } else if (currentPath.includes('/search/')) {
      return baseURL;
    }
    
    // 4. 最终返回首页
    return baseURL;
  }
  
  /**
   * 保存页面状态
   */
  function savePageState(path) {
    var now = Date.now();
    if (path === lastSavedPath && (now - lastSavedTime) < 500) {
      return;
    }
    lastSavedPath = path;
    lastSavedTime = now;
    
    try {
      const state = {
        scrollY: window.scrollY,
        scrollX: window.scrollX,
        timestamp: Date.now(),
        filters: {},
        expandedSections: [],
        expanded: [],
        searchParams: window.location.search
      };
      
      const filterElements = document.querySelectorAll('select[data-filter], input[data-filter]');
      filterElements.forEach(el => {
        const filterName = el.getAttribute('data-filter');
        if (filterName) {
          if (el.tagName === 'SELECT') {
            state.filters[filterName] = el.value;
          } else if (el.type === 'checkbox') {
            state.filters[filterName] = el.checked;
          } else {
            state.filters[filterName] = el.value;
          }
        }
      });
      
      const detailsElements = document.querySelectorAll('details[open]');
      detailsElements.forEach(el => {
        if (el.id) {
          state.expandedSections.push(el.id);
        }
      });
      
      const expandedElements = document.querySelectorAll('.expanded, [aria-expanded="true"]');
      expandedElements.forEach(el => {
        if (el.id) {
          state.expanded.push(el.id);
        }
      });
      
      const stateKey = STATE_KEY_PREFIX + encodeURIComponent(path);
      localStorage.setItem(stateKey, JSON.stringify(state));
      
    } catch (e) {
      console.warn('保存页面状态失败:', e);
    }
  }
  
  /**
   * 恢复页面状态
   */
  function restorePageState(path) {
    try {
      const stateKey = STATE_KEY_PREFIX + encodeURIComponent(path);
      const stateStr = localStorage.getItem(stateKey);
      
      if (!stateStr) {
        return false;
      }
      
      const state = JSON.parse(stateStr);
      
      if (Date.now() - state.timestamp > 24 * 60 * 60 * 1000) {
        localStorage.removeItem(stateKey);
        return false;
      }
      
      if (state.filters) {
        Object.entries(state.filters).forEach(([filterName, value]) => {
          const element = document.querySelector(`[data-filter="${filterName}"]`);
          if (element) {
            if (element.tagName === 'SELECT') {
              element.value = value;
              element.dispatchEvent(new Event('change', { bubbles: true }));
            } else if (element.type === 'checkbox') {
              element.checked = value;
              element.dispatchEvent(new Event('change', { bubbles: true }));
            } else {
              element.value = value;
              element.dispatchEvent(new Event('input', { bubbles: true }));
            }
          }
        });
      }
      
      if (state.expandedSections) {
        state.expandedSections.forEach(id => {
          const element = document.getElementById(id);
          if (element && element.tagName === 'DETAILS') {
            element.open = true;
          }
        });
      }
      
      if (state.expanded) {
        state.expanded.forEach(id => {
          const element = document.getElementById(id);
          if (element) {
            element.classList.add('expanded');
            if (element.hasAttribute('aria-expanded')) {
              element.setAttribute('aria-expanded', 'true');
            }
          }
        });
      }
      
      if (state.scrollY !== undefined) {
        requestAnimationFrame(function() {
          window.scrollTo(state.scrollX || 0, state.scrollY);
        });
      }
      
      return true;
      
    } catch (e) {
      console.warn('恢复页面状态失败:', e);
      return false;
    }
  }
  
  /**
   * 初始化返回按钮
   */
  function initBackButton() {
    const backButton = document.querySelector('.back-button[data-smart-back="true"]');
    if (!backButton) {
      return;
    }
    
    const currentPath = window.location.pathname;
    const backTarget = getSmartBackTarget(currentPath);
    
    // 设置返回目标
    backButton.setAttribute('href', backTarget);
    
    // 添加点击事件
    backButton.addEventListener('click', function(e) {
      e.preventDefault();
      
      // 保存当前页面状态
      savePageState(currentPath);
      
      // 保存导航历史
      saveNavigationHistory(currentPath, backTarget);
      
      // 跳转
      window.location.href = backTarget;
    });
  }
  
  /**
   * 初始化导航栏链接点击事件
   */
  function initNavbarLinks() {
    const currentPath = window.location.pathname;
    
    const navLinks = document.querySelectorAll('.navbar a[href]:not([data-nav-initialized])');
    navLinks.forEach(link => {
      link.setAttribute('data-nav-initialized', 'true');
      link.addEventListener('click', function(e) {
        savePageState(currentPath);
        
        const targetPath = this.getAttribute('href');
        if (targetPath && !targetPath.startsWith('http') && !targetPath.startsWith('#')) {
          saveNavigationHistory(currentPath, targetPath);
        }
      });
    });
  }
  
  /**
   * 全局链接点击委托 — 记录所有内部链接的导航历史
   */
  function initGlobalLinks() {
    if (globalLinksInitialized) return;
    globalLinksInitialized = true;
    
    const currentPath = window.location.pathname;
    
    document.addEventListener('click', function(e) {
      var link = e.target.closest('a[href]');
      if (!link) return;
      
      var href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('javascript:')) return;
      
      savePageState(currentPath);
      saveNavigationHistory(currentPath, href);
    });
  }
  
  /**
   * 页面加载时恢复状态
   */
  function onPageLoad() {
    const currentPath = window.location.pathname;
    
    // 尝试恢复页面状态
    restorePageState(currentPath);
    
    // 保存导航历史
    if (document.referrer) {
      try {
        const referrerUrl = new URL(document.referrer);
        const referrerPath = referrerUrl.pathname;
        
        // 只保存站内导航历史
        const baseURL = getBaseURL();
        if (referrerPath.startsWith(baseURL) && referrerPath !== currentPath) {
          saveNavigationHistory(referrerPath, currentPath);
        }
      } catch (e) {
        // URL解析失败，忽略
      }
    }
    
    initNavbarLinks();
    initGlobalLinks();
  }
  
  /**
   * 页面卸载前保存状态
   */
  function onPageUnload() {
    const currentPath = window.location.pathname;
    savePageState(currentPath);
  }
  
  // 初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initBackButton();
      onPageLoad();
    });
  } else {
    initBackButton();
    onPageLoad();
  }
  
  // 页面卸载时保存状态（比 beforeunload 更可靠）
  window.addEventListener('pagehide', onPageUnload);
  
  // 从 bfcache 恢复时重新初始化
  window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
      onPageLoad();
    }
  });
  
  // 页面可见性变化时保存状态（兼顾移动端切后台）
  document.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'hidden') {
      onPageUnload();
    }
  });
  
  // 暴露全局方法供其他脚本使用
  window.CC408BackButton = {
    savePageState: savePageState,
    restorePageState: restorePageState,
    getSmartBackTarget: getSmartBackTarget,
    saveNavigationHistory: saveNavigationHistory
  };
  
})();