---
title: "模拟卷4 操作系统 第22题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "choice"
difficulty: 3
number: 22
---

在 DMA 方式下，数据从内存传送到外设经过的路径是（ ）。

A\. 内存 → 数据总线 → 外设
B\. 内存 → 数据总线 → DMA → 外设
C\. 内存 → CPU → 数据总线 → 外设
D\. 外设 → 内存

[异常和中断](/study_methods/tags/408quiz//#%e5%bc%82%e5%b8%b8%e5%92%8c%e4%b8%ad%e6%96%ad)
[总线类型](/study_methods/tags/408quiz//#%e6%80%bb%e7%ba%bf%e7%b1%bb%e5%9e%8b)

[tag_link]

正确答案：B
> 【解析】本题考查 DMA 的数据传送方式。
> 在 DMA 方式下，数据传送不需要经过 CPU，但需要经过 DMA 控制器中的数据缓冲寄存器。
> DMA 控制器中的数据缓冲寄存器用来暂存每次传送的数据。
> 输入时，数据由外设（如磁盘）先送往数据缓冲寄存器，再通过数据总线送到主存。
> 反之，输出时，数据由主存通过数据总线送到数据缓冲寄存器，然后再送到外设。
>
