# CC408 — 待办任务

> 项目状态: 基础功能已完成，内容已全面迁移

## [高] 部署与验证

- [x] 推送 cc408 repo 到 GitHub（`git push`）
- [x] 验证 GitHub Actions 构建通过
- [x] 确认 `https://cycycy5464.github.io/cc408/` 可访问
- [x] 验证所有页面链接正确（首页、知识点、刷题、图谱、资源）

## [高] 导航功能完善

- [x] 导航栏 active 状态修复（仅高亮当前 section）
- [x] 列表页范围过滤（exam/list, docs/list）
- [x] 知识点↔题目双向链接

## [中] 内容补充

- [x] 为已有知识点补充 `prerequisites` 前置知识字段（知识图谱数据源）
- [x] 为题目补充 `related_knowledge` 关联知识点（现有 3 题有关联，其余缺失）
- [x] 编写质量校验脚本（已创建 verify-content.py，放入 CI 流程）

## [中] 内容修复

- [x] 移除所有真题页面的 B站视频链接
- [x] 真题答案改为折叠展示（<details> 下拉查看）
- [x] 个体题目答案/解析均折叠
- [x] 修复 94 个文件中的误包代码块（列表项被包在 ```c 中）
- [ ] 检查 csgraduates 与 cc408 的内容质量差异，补充缺失内容

## [中] 知识图谱增强

- [x] 从 docs frontmatter 自动生成 `static/data/knowledge-graph.json`
- [x] 完善 Hugo partial `knowledge-graph-data.html`
- [x] D3.js 图谱增加学科聚类、科目图例、搜索功能

## [低] 交互优化

- [ ] 知识点详情页侧边栏默认折叠非当前科目
- [ ] 卡片组件化 SCSS 整理（subject-card, exam-card, knowledge-card）
- [ ] 刷题页面答题/解析模式切换
- [ ] 首页数据动态统计（科目篇数、最近更新等）

## [低] 搜索与索引

- [ ] 集成 Pagefind 全文搜索
- [ ] 标签聚合页面（/tags/）
- [ ] 全站 sitemap 优化

## 已验证修复

- ✅ 导航栏首页下划线不会串到其他页面（2026-07-02）
- ✅ 真题页只有真题高亮，刷题页只有刷题高亮
- ✅ 知识点详情页知识点导航正确高亮
