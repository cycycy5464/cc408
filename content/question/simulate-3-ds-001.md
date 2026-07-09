---
title: "模拟卷3 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 1
---

设 n 是描述问题规模的正整数，下面程序片段的时间复杂度是（ ）。

A\.

B\.

C\.

D\.

[tag_link]

正确答案：A
> 程序片段中，变量 i 初始化为 2。
> 循环条件为 i &lt; n/3，每次循环体执行 i = i * 3，使得 i 的值以指数速度增长。
> 设循环执行次数为 k。
> 在执行 k 次后，i 的值变为 2 × 3^k。
> 循环终止时满足 2 × 3^k ≥ n/3，由此可得 k ≥ log₃(n/6)。
> 由于对数函数的特性，k 与 log n 成正比。
> 每次循环体执行时间为常数，因此整体时间复杂度取决于循环次数，为 O(log n)。
> 选项 A 正确。
>

