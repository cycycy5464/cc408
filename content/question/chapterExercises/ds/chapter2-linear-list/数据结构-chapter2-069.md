---
title: "线性表 第13题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "数据结构"
knowledge_points:
  - "线性表的链式表示"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 69
tags: ['课后题']
---

设有一个带头结点的非循环双链表L,   其每个结点中除有 pre 、data       和 next    域外， 还有一个访问频度域 freq,    其值均初始化为零。每当在链表中进行一次 Locate(L,x)
运算时，令值为 x 的结点中 freq   域的值增1,并使此链表中的结点保持按访问频度递 减的顺序排列，且最近访问的结点排在频度相同的结点之前，以便使频繁访问的结点总 是靠近表头。试编写符合上述要求的Locate(L,x)        函数，返回找到结点的地址，类型 为指针型。

[tag_link]

【解答】