---
title: "输入输出系统 第6题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "I/O方式"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 54
tags: ['课后题']
---

假设磁盘传输数据以32位的字为单位，传输速率为1MB/s,CPU   的时钟频率为50MHz。 回答以下问题：
1)采取程序查询方式，假设查询操作需要100个时钟周期，求CPU 为 I/O 查询所花费 的时间比率(假设进行足够的查询以避免数据丢失)。
2)采用中断方式进行控制，每次传输的开销(包括中断处理)为80个时钟周期。求 CPU 为传输硬盘所花费的时间比率。
3)采用DMA 的方式，假定DMA 的启动需要1000个时钟周期， DMA 完成时后处理需 要500个时钟周期。若平均传输的数据长度为4KB ( 此处K=1000),        试问硬盘工 作时CPU 将用多少时间比率进行输入/输出操作?忽略DMA申请总线的影响。

[tag_link]

C