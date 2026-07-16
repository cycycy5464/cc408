---
title: "内存管理 第18题"
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
number: 148
tags: ['课后题']
---

B
分页式和段页式存储管理均以固定大小的页框为单位分配内存，进程末页通常无法填满页 框，从而产生内部碎片；固定分区式因分区大小固定，当进程小于分区时，剩余空间同样形成内 部碎片。而分段式按逻辑段动态分配内存，为每个段分配恰好满足其长度的连续空间，不会因分 配粒度固定而导致空间浪费，因此不产生内部碎片(但可能因段间空隙产生外部碎片)。

[tag_link]

【解答】