# 题目标签远端持久化 · 方案 A 实现记录

> 对应可行性分析：[05-tag-management-remote-feasibility.md](./05-tag-management-remote-feasibility.md) 中推荐的「Serverless 代理写回仓库（方案 A）」。
> 部署与令牌配置细节见仓库 `serverless/README.md`。

## 目标
让「标签」页（`/tags/`）里任意访客对题目标签（knowledge_points）的增删改，
经一个**持有 GitHub 令牌的服务端代理**写回仓库真源 `static/mapping/question-kp-mapping.json`，
对所有访客持久可见；令牌不出现在前端。

## 已交付内容

### 1. Serverless 代理（Cloudflare Worker）
- `serverless/worker.js`：接收 `POST { edits: { "<file.md>": ["kp", ...] } }`，
  通过 GitHub Contents API 先 `GET` 取最新 `sha`、合并增量、再 `PUT` 回写；
  并发冲突（HTTP 409）自动取最新 sha 重试（最多 3 次）。
- `serverless/wrangler.toml`：非敏感配置（`GITHUB_REPO` / `GITHUB_BRANCH` / `MAPPING_PATH`），
  令牌 `GITHUB_TOKEN` 作为 **secret** 经 `wrangler secret put` 注入。
- CORS 已放开（预检 + 实际响应），可被 `cycycy5464.github.io` 跨域调用。
- 仅接受「更新已存在题目的 knowledge_points」，不增删题目结构，降低误写风险。

### 2. 前端（assets/js/kag-store.js）
- 新增 `REMOTE_ENDPOINT`：优先 `window.KAG_REMOTE_ENDPOINT`，其次 Hugo 注入的 `params.tagProxyEndpoint`。
- 新增 `isRemoteEnabled()` 与 `pushEdits()`：把本地编辑增量 `_edits` POST 到代理。
- `setKps` 仍只写本地（每次增删不触发远端），**仅显式「保存 / 同步」才推送**，避免高频写仓库。

### 3. UI（layouts/_default/terms.html）
- 动作区新增「☁ 同步到仓库」按钮，**默认隐藏**，配置端点后自动出现。
- 「💾 保存」在写 localStorage 成功后，若已启用远端则自动 `pushEdits()` 并提示同步题数；
  失败仅提示同步失败、本地仍保留。

### 4. 配置（config/_default/hugo.yaml）
- 新增 `params.tagProxyEndpoint: ''`（默认空 = 仅本地）。
- 填入 Worker 地址并重建后，远端同步即生效。

## 闭环验证（数据流）
```
浏览器(/tags/) --POST edits--> Worker(GITHUB_TOKEN)
        --> GET  question-kp-mapping.json (取 sha)
        --> PUT  question-kp-mapping.json (合并 edits, 带 sha)
        --> git push master
        --> .github/workflows/publish-cc408.yaml 重新构建并部署 Pages
下次任意访客刷新 /tags/ 即读到最新标签
```
现有 `publish-cc408.yaml` 在 `push: branches: ["master"]` 时自动重建并发布，提交 JSON 即触发 redeploy，闭环成立。

## 安全提示
- 前端**绝不**直连 GitHub API（会泄露 PAT）。
- 当前 Worker 端点对全网开放 POST；个人/低频站点可用，生产建议加 `X-API-Key` 校验、
  Cloudflare Turnstile / WAF、单 IP 限流（详见 `serverless/README.md`）。

## 不在本期范围
- 实时增量（方案 B / Cloudflare KV）：需引入第二数据源与合并逻辑，本期未做。
- 远端「拉取他人最新」：因写入即触发重建，下次刷新即为最新，无需额外拉取入口。
