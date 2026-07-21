---
title: "输入输出系统 第26题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "组成原理"
knowledge_points:
  - "I/O方式"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 42
tags: ['课后题']
---

磁盘和主存进行数据交换时，大致可分为四个过程：①寻道；②旋转；③连续读/写
磁盘块；④结束、校验。则下列关于磁盘读/写过程的叙述中，错误的是()。

A. 在①②④三个阶段都用到了中断处理
B. 在第③阶段，DMA 控制器向CPU 请求的是总线使用权
C. 在第③阶段，DMA 控制器使用总线的优先级比 CPU 低
D. 在第③阶段，磁盘的读/写和CPU 执行其他任务是可以并行执行的

[tag_link]

正确答案：C