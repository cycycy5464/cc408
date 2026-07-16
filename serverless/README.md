# CC408 题目标签同步代理（方案 A · Serverless 写回仓库）

把「标签」页（`/tags/`）里用户对题目标签（knowledge_points）的增删改，
经 Cloudflare Worker 代理写回 GitHub 仓库的 `static/mapping/question-kp-mapping.json`，
由现有 `.github/workflows/publish-cc408.yaml` 在 push 到 `master` 时自动重新构建并部署到 Pages。

> 前端令牌永不离开服务端。请勿在前端直连 GitHub API（会泄露 PAT）。

## 目录
- `worker.js` —— Cloudflare Worker 主程序（接收增量、调用 Contents API）。
- `wrangler.toml` —— 部署配置（非敏感项；令牌用 secret）。

## 部署步骤

### 1. 准备 GitHub 令牌
在 https://github.com/settings/tokens 创建 PAT：
- **Fine-grained token**：仅授权仓库 `cycycy5464/cc408` 的 **Contents: Read and write**。
- 或 **Classic token**：勾选 `repo` 范围。
复制令牌备用（仅显示一次）。

### 2. 安装并登录 Wrangler
```bash
npm install -g wrangler
wrangler login
```

### 3. 写入敏感令牌（secret，不入仓库）
```bash
cd serverless
wrangler secret put GITHUB_TOKEN
# 粘贴第 1 步的令牌
```
非敏感配置（仓库名/分支/映射路径）已在 `wrangler.toml` 的 `[vars]` 中，通常无需改动。

### 4. 部署
```bash
wrangler deploy
```
部署后获得一个 Worker 地址，形如：
`https://cc408-tag-proxy.<你的子域>.workers.dev`

### 5. 在前端启用远端同步
把上一步的 Worker 地址填入站点配置 `config/_default/hugo.yaml`：
```yaml
params:
  tagProxyEndpoint: "https://cc408-tag-proxy.<子域>.workers.dev"
```
然后重新构建（`hugo --gc`）。「标签」页会出现「☁ 同步到仓库」按钮，
「💾 保存」时也会自动把本地编辑推送到仓库。

## 安全与限流（生产建议）
- 当前端点对全网开放 POST。个人/低频站点可用；若担心滥用，建议：
  - 在 `worker.js` 增加 `X-API-Key` 校验（与可信维护者共享，密钥不要进前端构建产物）；
  - 接入 Cloudflare Turnstile 或 WAF 规则；
  - 用 Cloudflare 的 Rate Limiting 限制单 IP 频率。
- Worker 仅接受「更新已存在题目的 knowledge_points」，不增删题目结构。
- 并发提交冲突（HTTP 409）已在 Worker 内自动取最新 sha 重试（最多 3 次）。

## 数据流
```
浏览器(/tags/) --POST {edits}--> Worker(GITHUB_TOKEN)
        --> GET  question-kp-mapping.json (取 sha)
        --> PUT  question-kp-mapping.json (带 sha, 合并 edits)
        --> git push master
        --> GitHub Actions 重新构建并部署 Pages
下次任意访客刷新即读到最新标签
```
