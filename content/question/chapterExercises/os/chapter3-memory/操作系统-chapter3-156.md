---
title: "内存管理 第10题"
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
number: 156
tags: ['课后题']
---

B
静态装入是指在编程阶段就把物理地址计算好。可重定位是指在装入时把逻辑地址转换成物 理地址，但装入后不能改变。动态重定位是指在执行时再决定装入的地址并装入，装入后有可能 换出，所以同一个模块在内存中的物理地址是可能改变的，在作业运行过程中，当执行到一条访 存指令时，再把逻辑地址转换为主存的物理地址，实际上是通过地址变换机构实现的。

[tag_link]

C