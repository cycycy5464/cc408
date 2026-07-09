---
title: "模拟卷3 计算机组成原理 第19题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "choice"
difficulty: 3
number: 19
---

假定某计算机系统的 CPU 内部采用总线结构，其指令的取指周期由以下微操作序列实现，即： a. MAR ← (PC); b. MDR ← Memory, Read; c. PC ← (PC)+1; d. IR ← (MDR). 一种较好的设计是为其安排（ ）个节拍周期。

A\. 1

B\. 2

C\. 3

D\. 4

[tag_link]

正确答案：C
> **【解析】**在取指周期的微操作序列中： 微操作 a（ MAR←(PC) ）与微操作 c（ PC←(PC)+1 ）可以并行执行。
> 因为 a 读取 PC 的当前值用于地址传输，c 更新 PC 为新值。
> 在硬件设计上，可以在同一节拍内先读取 PC 的旧值，再更新为新值，两者无冲突。
> 微操作 b（ MDR←Memory, Read ）依赖于 a 提供的地址，必须在 a 之后单独节拍执行。
> 微操作 d（ IR←(MDR) ）依赖于 b 读取的数据，必须在 b 之后单独节拍执行。
> 因此，最少需要 3 个节拍周期 ： 第一节拍并行执行 a 和 c；
> 第二节拍执行 b；
> 第三节拍执行 d。
> 这种设计优化了节拍数，提高了取指效率。
>

