---
title: "模拟卷7 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 1
---

设 n 是描述问题规模的正整数，下列程序片段的时间复杂度是（ ）。

A\.

B\.

C\.

D\.

[tag_link]

正确答案：A
> 程序首先将变量 i 初始化为 n 的平方，即 i = n 2 。
> 然后进入 while 循环，循环条件为 i  = 1 ，每次迭代将 i 除以 2 。
> 循环的迭代次数取决于 i 从 n 2 减少到 1 所需除以 2 的次数。
> 设迭代次数为 k ，经过 k 次迭代后， i 的值变为 n 2 / 2 k 。
> 当循环终止时， i = 1 ，因此有 n 2 / 2 k = 1 ，即 n 2 = 2 k 。
> 取对数可得 k = lo g 2 ​ ( n 2 ) = 2 lo g 2 ​ n 。
> 在时间复杂度分析中，常数因子可以忽略，因此迭代次数 k 的数量级为 O ( lo g n ) 。
> 所以，该程序片段的时间复杂度是 O ( lo g n ) 。
> 对比选项，A 正确。
>

