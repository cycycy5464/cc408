---
title: "进程与线程 第6题"
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
number: 155
tags: ['课后题']
---

如下图所示，三个合作进程P₁,P₂,P₃,     它们都需要通过同一设备输入各自的数据a,b,c,    该 输入设备必须互斥地使用，而且其第一个数据必须由P₁ 进程读取，第二个数据必须由P₂ 进 程读取，第三个数据必须由P₃ 进程读取。然后，三个进程分别对输入数据进行下列计算：
打印机                P₁非抢占式输入设备P₂P₃
打印机                P₁
非抢占式输入设备
P₂
P₃
P₁:x=a+b;
P₂:y=a*b;
P₃:z=y+c-a;
最后，P₁ 进程通过所连接的打印机将计算结果x,y,z   的值打印出 来。请用信号量实现它们的同步。

[tag_link]

【解答】