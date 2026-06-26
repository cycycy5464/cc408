---
title: ""
date: 2026-06-25
type: landing

design:
  spacing: "6rem"

sections:
  - block: hero-landing
    content:
      title: |
        CC408
        <span class="gradient-text">408考研 · 知识整理平台</span>
      text: |
        系统化知识整理 · 历年真题练习 · 可视化知识图谱
      buttons:
        - text: 📖 知识点
          url: /docs/
          design:
            style: outline
        - text: ✏️ 刷题中心
          url: /exam/
          design:
            style: solid
        - text: 🗺️ 知识图谱
          url: /graph/
          design:
            style: outline
    design:
      background:
        color: "#0d1117"
      css_class: hero-section
  - block: collection
    content:
      title: 最近更新
      text: 最新整理的知识点和题目
      filters:
        folders:
          - docs
        orderby: date
        order: desc
      page_type: docs
      count: 6
    design:
      view: article-grid
      columns: 3
  - block: collection
    content:
      title: 热门资源
      text: 精选学习资料免费下载
      filters:
        folders:
          - resources
        tag: "推荐"
    design:
      view: card
      columns: 3
---
