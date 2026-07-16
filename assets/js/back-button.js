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
  const CURRENT_PAGE_KEY = 'cc408-current-page';
  
  // 获取baseURL（从页面中的链接推断）
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
  
  // 页面类型映射
  const PAGE_TYPES = {
    '/': 'home',
    '/docs/': 'docs-list',
    '/exam/': 'exam-list',
    '/exam/quiz-collection/': 'quiz-collection',
    '/graph/': 'graph',
    '/tags/': 'tags-list',
    '/resources/': 'resources-list',
    '/question/': 'question-list',
    '/search/': 'search'
  };
  
  // 默认返回目标映射（相对于baseURL）
  const DEFAULT_BACK_TARGETS = {
    '/docs/': '/',
    '/exam/': '/',
    '/exam/quiz-collection/': '/exam/',
    '/graph/': '/',
    '/tags/': '/',
    '/resources/': '/',
    '/question/': '/exam/',
    '/search/': '/'
  };
  
  /**
   * 获取页面类型
   */
  function getPageType(path) {
    const baseURL = getBaseURL();
    // 移除baseURL前缀
    let relativePath = path;
    if (path.startsWith(baseURL)) {
      relativePath = path.substring(baseURL.length - 1);
    }
    
    // 精确匹配
    if (PAGE_TYPES[relativePath]) {
      return PAGE_TYPES[relativePath];
    }
    
    // 前缀匹配
    for (const [prefix, type] of Object.entries(PAGE_TYPES)) {
      if (prefix !== '/' && relativePath.startsWith(prefix)) {
        return type;
      }
    }
    
    return 'unknown';
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
      
      // 从后往前找，跳过当前页面
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
    const currentType = getPageType(currentPath);
    
    // 根据页面类型确定返回目标
    if (currentType.includes('detail') || currentType.includes('single')) {
      // 详情页返回到对应的列表页
      if (currentPath.includes('/docs/')) {
        return baseURL + 'docs/';
      } else if (currentPath.includes('/exam/')) {
        return baseURL + 'exam/';
      } else if (currentPath.includes('/question/')) {
        return baseURL + 'question/';
      } else if (currentPath.includes('/resources/')) {
        return baseURL + 'resources/';
      }
    }
    
    // 4. 使用默认映射
    for (const [prefix, target] of Object.entries(DEFAULT_BACK_TARGETS)) {
      const fullPrefix = baseURL + prefix.replace(/^\//, '');
      if (currentPath.startsWith(fullPrefix) && currentPath !== fullPrefix) {
        if (target === '/') {
          return baseURL;
        }
        return baseURL + target.replace(/^\//, '');
      }
    }
    
    // 5. 最终返回首页
    return baseURL;
  }
  
  /**
   * 保存页面状态
   */
  function savePageState(path) {
    try {
      const state = {
        scrollY: window.scrollY,
        scrollX: window.scrollX,
        timestamp: Date.now(),
        // 保存筛选条件
        filters: {},
        // 保存展开的章节
        expandedSections: [],
        // 保存其他交互状态
        expanded: [],
        // 保存URL参数
        searchParams: window.location.search
      };
      
      // 保存筛选条件
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
      
      // 保存展开的章节
      const detailsElements = document.querySelectorAll('details[open]');
      detailsElements.forEach(el => {
        if (el.id) {
          state.expandedSections.push(el.id);
        }
      });
      
      // 保存其他展开状态
      const expandedElements = document.querySelectorAll('.expanded, [aria-expanded="true"]');
      expandedElements.forEach(el => {
        if (el.id) {
          state.expanded.push(el.id);
        }
      });
      
      const stateKey = STATE_KEY_PREFIX + encodeURIComponent(path);
      localStorage.setItem(stateKey, JSON.stringify(state));
      
      // 清理过期状态（超过24小时）
      cleanupOldStates();
      
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
      
      // 检查状态是否过期（超过24小时）
      if (Date.now() - state.timestamp > 24 * 60 * 60 * 1000) {
        localStorage.removeItem(stateKey);
        return false;
      }
      
      // 恢复滚动位置
      if (state.scrollY !== undefined) {
        // 延迟执行，确保页面已加载
        setTimeout(() => {
          window.scrollTo({
            top: state.scrollY,
            left: state.scrollX || 0,
            behavior: 'smooth'
          });
        }, 300);
      }
      
      // 恢复筛选条件
      if (state.filters) {
        Object.entries(state.filters).forEach(([filterName, value]) => {
          const element = document.querySelector(`[data-filter="${filterName}"]`);
          if (element) {
            if (element.tagName === 'SELECT') {
              element.value = value;
              // 触发change事件
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
      
      // 恢复展开的章节
      if (state.expandedSections) {
        state.expandedSections.forEach(id => {
          const element = document.getElementById(id);
          if (element && element.tagName === 'DETAILS') {
            element.open = true;
          }
        });
      }
      
      // 恢复其他展开状态
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
      
      // 清除已恢复的状态
      localStorage.removeItem(stateKey);
      
      return true;
      
    } catch (e) {
      console.warn('恢复页面状态失败:', e);
      return false;
    }
  }
  
  /**
   * 清理过期状态
   */
  function cleanupOldStates() {
    try {
      const keys = Object.keys(localStorage);
      const now = Date.now();
      
      keys.forEach(key => {
        if (key.startsWith(STATE_KEY_PREFIX)) {
          try {
            const stateStr = localStorage.getItem(key);
            if (stateStr) {
              const state = JSON.parse(stateStr);
              if (now - state.timestamp > 24 * 60 * 60 * 1000) {
                localStorage.removeItem(key);
              }
            }
          } catch (e) {
            // 解析失败，删除该key
            localStorage.removeItem(key);
          }
        }
      });
    } catch (e) {
      console.warn('清理过期状态失败:', e);
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
    
    // 为所有导航栏链接添加点击事件
    const navLinks = document.querySelectorAll('.navbar a[href]');
    navLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        // 保存当前页面状态
        savePageState(currentPath);
        
        // 保存导航历史
        const targetPath = this.getAttribute('href');
        if (targetPath && !targetPath.startsWith('http') && !targetPath.startsWith('#')) {
          saveNavigationHistory(currentPath, targetPath);
        }
      });
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
    
    // 初始化导航栏链接
    initNavbarLinks();
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
  
  // 页面卸载前保存状态
  window.addEventListener('beforeunload', onPageUnload);
  
  // 页面可见性变化时保存状态
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