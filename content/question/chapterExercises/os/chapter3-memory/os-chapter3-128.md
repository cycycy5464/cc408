---
title: "内存管理 第41题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "虚拟内存管理"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 128
tags: ['课后题']
---

B
段式存储管理按程序逻辑结构划分段，段名与段长由用户定义，便于编程；各段作为独立逻  辑单位，支持共享、按段保护、动态增长(如数据段扩展)和动态链接(运行时按需加载)。而  提高内存利用率并非段式管理的目标：因其段长不固定，易产生外部碎片，内存利用率通常较低。 高效利用内存恰好是分页式管理的优势，通过固定页框离散分配，可有效消除外部碎片。

[tag_link]

B