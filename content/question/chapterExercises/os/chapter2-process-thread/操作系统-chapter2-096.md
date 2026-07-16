---
title: "进程与线程 第2题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "处理机调度"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 96
tags: ['课后题']
---

有三个作业A,B,C,     它们分别单独运行时的CPU 和 I/O占用时间如下图所示。
现在请考虑三个作业同时开始执行。系统中的资源有一个 CPU  和两台输入/输出设备 (I/O₁ 和 I/O₂)  同时运行。三个作业的优先级为A 最高、B 次之、C 最低，一旦低优先级
的进程开始占用CPU 或I/O 设备，高优先级进程也要等待到其结束后方可占用。
I/O₁CPU40 CPU20  20I/O₁I/O₂CPU 30I/O₁   40CPU作业A作业B作业CCPU30CPU70I/O₂20I/O₁ 30I/O₁4030I/O₂
I/O₁CPU
40 CPU
20  20
I/O₁
I/O₂CPU 30
I/O₁   40
CPU
作业A
作业B
作业C
CPU
30
CPU
70
I/O₂
20
I/O₁ 30
I/O₁
40
30
I/O₂
请回答下面的问题：
1)最早结束的作业是哪个?
2)最后结束的作业是哪个?
3)计算这段时间CPU 的利用率(三个作业全部结束为止)。

[tag_link]

C