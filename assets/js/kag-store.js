// CC408 Knowledge-point Store — shared CRUD module for question tags (knowledge_points)
// Loaded via Hugo Pipes (resources.ExecuteAsTemplate) so {{ .Site.BaseURL }} is injected.
(function () {
  'use strict';

  var BASE_URL = '{{ .Site.BaseURL }}';
  // 远端同步端点（方案 A）。优先用 window.KAG_REMOTE_ENDPOINT，其次 Hugo 注入的 params.tagProxyEndpoint。
  // 为空表示仅本地（localStorage），不启用远端写。
  var REMOTE_ENDPOINT = (window.KAG_REMOTE_ENDPOINT ||
    '{{ .Site.Params.tagProxyEndpoint | default "" }}').replace(/\/+$/, '');
  var STORAGE_KEY = 'cc408-kp-edits';
  var _mapping = null;
  var _edits = {};

  function loadEdits() {
    try {
      _edits = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}') || {};
    } catch (e) {
      _edits = {};
    }
    return _edits;
  }

  function saveEdits() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(_edits));
      return true;
    } catch (e) {
      return false;
    }
  }

  function applyEdits() {
    if (!_mapping || !_mapping.questionIndex) return;
    for (var file in _edits) {
      if (_mapping.questionIndex[file]) {
        _mapping.questionIndex[file].knowledge_points = _edits[file];
      }
    }
  }

  function load() {
    return new Promise(function (resolve, reject) {
      if (_mapping) { resolve(_mapping); return; }
      fetch(BASE_URL + 'mapping/question-kp-mapping.json')
        .then(function (r) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          return r.json();
        })
        .then(function (data) {
          _mapping = data;
          loadEdits();
          applyEdits();
          resolve(_mapping);
        })
        .catch(reject);
    });
  }

  function getQuestions() {
    if (!_mapping) return [];
    var idx = _mapping.questionIndex || {};
    return Object.keys(idx).map(function (file) {
      var q = idx[file];
      return {
        file: file,
        title: q.title || file.replace(/\.md$/, ''),
        subject: q.subject || '',
        year: q.year || '',
        set: q.set,
        source: q.source || '',
        kps: (q.knowledge_points || []).slice()
      };
    });
  }

  function getKps(file) {
    if (!_mapping || !_mapping.questionIndex[file]) return [];
    return (_mapping.questionIndex[file].knowledge_points || []).slice();
  }

  function setKps(file, arr) {
    if (!_mapping || !_mapping.questionIndex[file]) return;
    var next = (arr || []).slice();
    _mapping.questionIndex[file].knowledge_points = next;
    _edits[file] = next;
    saveEdits();
  }

  function addKp(file, kp) {
    var cur = getKps(file);
    if (kp && cur.indexOf(kp) < 0) {
      cur.push(kp);
      setKps(file, cur);
    }
    return cur;
  }

  function removeKp(file, kp) {
    var cur = getKps(file).filter(function (k) { return k !== kp; });
    setKps(file, cur);
    return cur;
  }

  function exportMapping() {
    if (!_mapping) return;
    var blob = new Blob([JSON.stringify(_mapping, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'question-kp-mapping.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function importMapping(fileObj, onDone) {
    var reader = new FileReader();
    reader.onload = function () {
      try {
        var data = JSON.parse(reader.result);
        if (!data || !data.questionIndex) throw new Error('文件缺少 questionIndex 字段');
        _mapping = data;
        _edits = {};
        var idx = data.questionIndex || {};
        for (var f in idx) {
          if (idx[f] && idx[f].knowledge_points) _edits[f] = idx[f].knowledge_points.slice();
        }
        saveEdits();
        if (onDone) onDone(null);
      } catch (e) {
        if (onDone) onDone(e);
      }
    };
    reader.readAsText(fileObj);
  }

  // 是否启用远端同步（方案 A）
  function isRemoteEnabled() {
    return !!REMOTE_ENDPOINT;
  }

  // 把本地编辑增量（_edits: { file: [kps] }）POST 到 Serverless 代理写回仓库。
  // 返回 Promise：resolve({ ok, changed })，reject(Error)。
  function pushEdits() {
    if (!REMOTE_ENDPOINT) return Promise.reject(new Error('远端未启用'));
    var payload = { edits: _edits };
    return fetch(REMOTE_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }).then(function (r) {
      return r.json().then(function (j) {
        if (!r.ok) throw new Error(j.error || ('HTTP ' + r.status));
        return j;
      });
    });
  }

  // Render knowledge-point pill tags into a container; onRemove(kp) called when ✕ clicked
  function renderTags(container, kps, onRemove) {
    if (!container) return;
    var html = '';
    (kps || []).forEach(function (kp) {
      html += '<span class="kp-tag">' + kp +
        '<span class="kp-del" data-kp="' + kp.replace(/"/g, '&quot;') + '">✕</span></span>';
    });
    if (!(kps && kps.length)) html = '<span class="kp-empty">无标签</span>';
    container.innerHTML = html;
    container.querySelectorAll('.kp-del').forEach(function (el) {
      el.addEventListener('click', function () {
        if (onRemove) onRemove(el.getAttribute('data-kp'));
      });
    });
  }

  window.KagStore = {
    BASE_URL: BASE_URL,
    load: load,
    getQuestions: getQuestions,
    getKps: getKps,
    setKps: setKps,
    addKp: addKp,
    removeKp: removeKp,
    saveEdits: saveEdits,
    exportMapping: exportMapping,
    importMapping: importMapping,
    renderTags: renderTags,
    isRemoteEnabled: isRemoteEnabled,
    pushEdits: pushEdits
  };
})();
