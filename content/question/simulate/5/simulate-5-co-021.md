---
title: "模拟卷5 组成原理 第21题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "组成原理"
knowledge_points:
  - "异常和中断"
question_type: "choice"
difficulty: 3
number: 21

---

DMA 方式的接口电路中有程序中断部件，其作用包括（ ）。
I. 实现数据传送
II. 向 CPU 提出总线使用权
III. 向 CPU 提出传输结束
IV. 检查数据是否出错

A\. 仅 III
B\. III 和 IV
C\. I、III 和 IV
D\. I 和 II

[异常和中断](/study_methods/tags/408quiz//#%e5%bc%82%e5%b8%b8%e5%92%8c%e4%b8%ad%e6%96%ad)

[tag_link]

正确答案：A
> <p> 考查 DMA 方式中的中断与中断传输方式的区别。
> 前者是向 CPU 报告数据传输结束，后者是传送数据，另外 DMA 方式中的中断不包括检查是否出错，而是报告错误。
> <p>注意：DMA 方式与程序中断方式的比较如下。
> <p>① DMA 传送数据的方式是靠硬件传送，而程序传送方式是由程序来传送。
> <p>② 程序中断方式需要中断 CPU 的现行程序，需要保护现场，而 DMA 方式不需要中断现行程序。
> <p>③ 程序中断方式需要在一条指令执行结束才能得到响应，而 DMA 方式则可以在指令周期内的任意存储周期结束时响应。
> <p>④ DMA 方式的优先级高于程序中断方式的优先级。
>
