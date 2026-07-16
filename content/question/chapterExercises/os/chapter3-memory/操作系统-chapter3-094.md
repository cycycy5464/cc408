---
title: "内存管理 第3题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "虚拟内存管理"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 94
tags: ['课后题']
---

【解答】
空闲区分配。这说明最先适配算法尽可能地使用了低地址部分的空闲区域，留下了高地 址部分的大的空闲区，更有可能满足进程的申请。
3)若随后又要申请80KB,  则最先适配算法可以分配成功，而最佳适配算法则没有足够大的
第一块：始址240K,  大小60KB; 第二块：超始地址450K,  大小62KB。
2)最佳适配的内存分配情况如上图中的(b)所示。内存中的空块为：
第一块：始址290K,  大小10KB;  第二块：始址400K,  大小112KB。
内存中的空块为：
(b)
reg150KB
reg90KB
reg100KB
reg50KB
512KB
450KB
400KB
300KB
240KB
150KB
0KB
(a)
reg150KBreg50KBreg90KBreg100KB
reg150KB
reg50KB
reg90KB
reg100KB
512KB
400KB
290KB 300KB
200KB
150KB
0KB
1)最先适配的内存分配情况如下图中的(a)所示。

[tag_link]

正确答案：B