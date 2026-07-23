# 题目标签管理 · 部署后远端持久化可行性分析

> 背景：知识图谱的「管理标签」能力已迁移到导航栏「标签」页（`/tags/`），由 `assets/js/kag-store.js` 提供增删改查（CRUD）。
> 本期实现为**纯静态、零后端**：浏览器 `localStorage` 持久化 + 导入/导出 `question-kp-mapping.json`。
> 本文分析部署到 GitHub Pages 后，如何让标签 CRUD 对所有访客**共享且持久**。

## 当前方案（已实现，零成本）

- 数据真源：`static/mapping/question-kp-mapping.json`（`questionIndex[file].knowledge_points`）。
- 用户编辑只写入本地 `localStorage`（键 `cc408-kp-edits`），并叠加在内存中的 mapping 之上。
- 「导出映射」下载完整 JSON，可线下交给维护者合并回仓库；「导入映射」从本地文件恢复。

优点：无需服务器、无隐私/令牌暴露风险、即开即用。
缺点：编辑**仅本人本机可见**，无法跨设备/跨访客共享。

## 需求拆解

部署后要让「任何人执行的标签增删改」持久化并被所有访客读到，本质需要：
1. 一个**可写的数据后端**（或写回仓库）；
2. 客户端能在**不暴露写令牌**的前提下调用它；
3. 与仓库内 `question-kp-mapping.json` 真源保持**一致/可合并**。

## 候选方案对比

### 方案 A：服务端代理写回仓库（GitHub Contents API）

- 架构：`静态页 → Serverless 函数（持有 GitHub PAT / GitHub App 令牌）→ 更新仓库文件`。
- 客户端只调用自己的 Serverless（同域或配置 CORS），令牌留在服务端。
- 数据真源仍是 `static/mapping/question-kp-mapping.json`，天然版本化、可 review、可回滚。
- 实现要点：
  - 函数用 `PUT /repos/{owner}/{repo}/contents/static/mapping/question-kp-mapping.json`，需先 `GET` 取 `sha` 再提交。
  - 并发：用仓库 `main` 最新 `sha` 提交，冲突时返回 409 让前端重试/合并。
  - 写频率低（标签编辑非高频），GitHub API 速率限制（未认证 60/h，认证 5000/h）足够。
- 缺点：需要托管一个 Serverless（见下）；写仓库会触发一次重新构建/部署（GitHub Pages 需 Actions 或手动 `hugo` 生成）。

### 方案 B：独立 KV / 数据库（Supabase / Upstash / Cloudflare KV）

- 架构：`静态页 → KV/DB SDK 或自建 API`，按 `file` 存 `knowledge_points` 增量。
- 加载时：先取仓库基础 mapping，再 `merge` KV 中的增量覆盖。
- 优点：实时、不触发站点重构建、可支持多用户并发与审计。
- 缺点：引入第二数据源，需维护「基础 mapping + 远端增量」的合并逻辑；DB 需鉴权（匿名写要做好防滥用，如限流/校验）。

### 方案 C：Issue / PR 表单（纯 GitHub，无令牌暴露）

- 架构：页面「提交修改」按钮打开预填好的 Issue 或 PR 模板，由维护者合并。
- 优点：零基础设施、零令牌、完全在 GitHub 内审计。
- 缺点：非实时，依赖人工合并，体验偏重。

### 方案 D：客户端直连 GitHub API（不推荐）

- 把 PAT 放在前端会**直接泄露令牌**，任何人可借此改写仓库。仅适合个人私有场景，公开站点**禁止**。

## 推荐路径（按投入从小到大）

1. **短期（已交付）**：保持 localStorage + 导入/导出，满足单用户离线编辑与线下交接。
2. **中期推荐**：**方案 A（Cloudflare Workers / Vercel Functions 代理写回仓库）**。
   - 站点已托管在 GitHub Pages，配一个 Cloudflare Worker（免费额度足够）持有 `GITHUB_TOKEN`，
     暴露 `POST /api/tags` 接收 `{file, knowledge_points}`，服务端 `GET`+`PUT` 回写 JSON 并触发 Pages 重建。
   - 前端 `kag-store.js` 的 `saveEdits()` 在写 localStorage 成功后，异步 `POST` 到该端点；
     `load()` 仍先取仓库 JSON（已含他人提交结果）。
3. **若想要实时、不重建**：采用**方案 B（Cloudflare KV）**，`kag-store.js` 在 `load()` 后 `merge` KV 增量。

## 接入点（代码侧预留）

`assets/js/kag-store.js` 已封装 `load / getKps / setKps / saveEdits / exportMapping / importMapping`，
后续接入远端只需在 `saveEdits()` 内追加一次网络写、`importMapping()` 之外增加「拉取远端最新」入口，
UI 与存储结构无需变动。建议新增环境变量式开关（如 `window.KAG_REMOTE_ENDPOINT`）控制是否启用远端写。

## 结论

- 本期交付的纯静态方案已可用，且数据可经导入/导出回流到仓库真源。
- 要让「部署后标签 CRUD 对全员持久」，首选 **Serverless 代理写回仓库（方案 A）**，兼顾零额外数据源与安全性；
  对实时性要求高时再升级到 KV（方案 B）。**切勿**在前端直连 GitHub API。

## 实现状态

✅ **方案 A 已实现**：`serverless/worker.js`（Cloudflare Worker 代理）+ `assets/js/kag-store.js` 的
`pushEdits()/isRemoteEnabled()` + `layouts/_default/terms.html` 的「☁ 同步到仓库」入口 +
`config/_default/hugo.yaml` 的 `params.tagProxyEndpoint`。详见
[06-serverless-proxy-implementation.md](./06-serverless-proxy-implementation.md) 与 `serverless/README.md`。
