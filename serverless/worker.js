/**
 * CC408 题目标签同步代理 · Cloudflare Worker（方案 A）
 *
 * 接收前端 POST 的本地编辑增量 { edits: { "<file.md>": ["知识点1","知识点2"] } }，
 * 经 GitHub Contents API 写回仓库 static/mapping/question-kp-mapping.json，
 * 提交到 master 后由 .github/workflows/publish-cc408.yaml 自动重新构建并部署到 Pages。
 *
 * 设计要点：
 *  - 令牌 GITHUB_TOKEN 只存放在服务端（Worker 环境变量 / secret），前端永不接触。
 *  - 写文件前先 GET 取最新 sha，提交时带 sha；并发冲突返回 409 并重试。
 *  - 仅接受更新已存在题目的 knowledge_points，不增删题目结构，降低误写风险。
 */

// ---- UTF-8 安全的 base64（Worker 全局无 Buffer 保证，用标准 API） ----
function bytesToBase64(bytes) {
  let bin = '';
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) {
    bin += String.fromCharCode.apply(null, bytes.subarray(i, i + chunk));
  }
  return btoa(bin);
}

function base64ToBytes(b64) {
  const bin = atob(b64.replace(/\s/g, ''));
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return bytes;
}

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}

async function getFile(token, repo, branch, path) {
  const url =
    'https://api.github.com/repos/' +
    encodeURIComponent(repo) +
    '/contents/' +
    encodeURIComponent(path) +
    '?ref=' +
    encodeURIComponent(branch);
  const res = await fetch(url, {
    headers: {
      Authorization: 'Bearer ' + token,
      Accept: 'application/vnd.github+json',
      'User-Agent': 'cc408-tag-proxy',
    },
  });
  if (!res.ok) {
    const t = await res.text();
    throw new Error('GET 文件失败 HTTP ' + res.status + ' ' + t.slice(0, 200));
  }
  return res.json(); // { content(base64), sha, ... }
}

async function putFile(token, repo, branch, path, contentBase64, sha, message) {
  const url =
    'https://api.github.com/repos/' +
    encodeURIComponent(repo) +
    '/contents/' +
    encodeURIComponent(path);
  const res = await fetch(url, {
    method: 'PUT',
    headers: {
      Authorization: 'Bearer ' + token,
      Accept: 'application/vnd.github+json',
      'Content-Type': 'application/json',
      'User-Agent': 'cc408-tag-proxy',
    },
    body: JSON.stringify({
      message: message,
      content: contentBase64,
      sha: sha,
      branch: branch,
    }),
  });
  if (res.status === 409) throw new Error('CONFLICT');
  if (!res.ok) {
    const t = await res.text();
    throw new Error('PUT 文件失败 HTTP ' + res.status + ' ' + t.slice(0, 200));
  }
  return res.json();
}

// 把 edits 合并进仓库最新 mapping，并返回变更题数；冲突时最多重试 3 次
async function applyEdits(token, repo, branch, path, edits) {
  let lastErr;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      const meta = await getFile(token, repo, branch, path);
      const text = new TextDecoder().decode(base64ToBytes(meta.content));
      const data = JSON.parse(text);
      if (!data.questionIndex) throw new Error('JSON 缺少 questionIndex');

      let changed = 0;
      for (const file in edits) {
        if (!Object.prototype.hasOwnProperty.call(edits, file)) continue;
        if (!data.questionIndex[file]) continue; // 只更新已存在题目
        const kps = edits[file];
        data.questionIndex[file].knowledge_points = Array.isArray(kps)
          ? kps.filter(function (k) {
              return typeof k === 'string';
            })
          : [];
        changed++;
      }

      const newContent = bytesToBase64(
        new TextEncoder().encode(JSON.stringify(data, null, 2))
      );
      await putFile(
        token,
        repo,
        branch,
        path,
        newContent,
        meta.sha,
        'chore(tags): sync knowledge_points via proxy (' + changed + ' files)'
      );
      return changed;
    } catch (e) {
      if (e.message === 'CONFLICT') {
        lastErr = e;
        continue; // 取最新 sha 重试
      }
      throw e;
    }
  }
  throw lastErr || new Error('重试次数超限');
}

export default {
  async fetch(request, env) {
    // CORS 预检
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders() });
    }

    const token = env.GITHUB_TOKEN;
    const repo = env.GITHUB_REPO || 'cycycy5464/cc408';
    const branch = env.GITHUB_BRANCH || 'master';
    const path =
      env.MAPPING_PATH || 'static/mapping/question-kp-mapping.json';

    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', {
        status: 405,
        headers: corsHeaders(),
      });
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return new Response('Invalid JSON', {
        status: 400,
        headers: corsHeaders(),
      });
    }

    const edits = body && body.edits;
    if (!edits || typeof edits !== 'object') {
      return new Response('Missing "edits" object', {
        status: 400,
        headers: corsHeaders(),
      });
    }
    if (!token) {
      return new Response(
        JSON.stringify({ ok: false, error: 'GITHUB_TOKEN 未配置' }),
        {
          status: 500,
          headers: { 'Content-Type': 'application/json', ...corsHeaders() },
        }
      );
    }

    try {
      const changed = await applyEdits(token, repo, branch, path, edits);
      return new Response(JSON.stringify({ ok: true, changed: changed }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders() },
      });
    } catch (e) {
      const status = e.message === 'CONFLICT' ? 409 : 500;
      return new Response(
        JSON.stringify({ ok: false, error: e.message }),
        {
          status: status,
          headers: { 'Content-Type': 'application/json', ...corsHeaders() },
        }
      );
    }
  },
};
