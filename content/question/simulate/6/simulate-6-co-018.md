---
title: "模拟卷6 组成原理 第18题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "组成原理"
knowledge_points:
  - "寄存器类型"
question_type: "choice"
difficulty: 3
number: 18

---

在计算机体系结构中，CPU 内部包括程序计数器 PC、存储器数据寄存器 MDR、指令寄存器 IR 和存储器地址寄存器 MAR 等。若 CPU 要执行的指令为：MOV RO, #100（即将数值 100 传送到寄存器 RO），则 CPU 首先完成的操作是（ ）。

A\. 100→RO
B\. 100→MDR
C\. PC→MAR
D\. PC→IR

[寄存器类型](/study_methods/tags/408quiz//#%e5%af%84%e5%ad%98%e5%99%a8%e7%b1%bb%e5%9e%8b)

[tag_link]

正确答案：C
> CPU 执行指令的第一步是取指阶段。
> 在这个阶段，CPU 需要从内存中读取当前要执行的指令。
> 程序计数器 PC 存储了下一条指令的内存地址。
> 为了访问内存，CPU 首先将 PC 的内容送到存储器地址寄存器 MAR，以便内存控制器根据该地址定位指令所在的位置。
> 随后，内存将指令数据通过数据总线传送到存储器数据寄存器 MDR，再送入指令寄存器 IR 进行译码。
> 对于指令“MOV RO, #100”，虽然最终目的是将立即数 100 传送到寄存器 RO，但 CPU 必须首先取指，因此最初的操作是 PC→MAR。
> 选项 A 和 B 涉及指令执行阶段的操作，发生在取指之后；
> 选项 D 不符合标准取指流程，因为 PC 不直接送入 IR。
>
