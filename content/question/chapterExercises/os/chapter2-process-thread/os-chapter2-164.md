---
title: "进程与线程 第15题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "同步与互斥"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 164
tags: ['课后题']
---

有3个进程P 、P₁ 、P₂合作处理数据，P 从输入设备读数据到缓冲区，缓冲区可存1000个 字。P₁ 和 P₂ 的功能一样，都是从缓冲区取出数据并计算，再打印结果。请用信号量的 P,V 操作实现。其中，语句read() 从输入设备读入20个字到缓冲区； get() 从缓冲区取出 20个字； comp()计算40个字输出并得到结果的1个字； print()打印结果的2个字。

[tag_link]

【解答】