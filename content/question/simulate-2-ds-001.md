---
title: "模拟卷2 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
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

正确答案：D
> 程序片段中，变量 y 从 0 开始，每次循环迭代 y 增加 1。
> 循环条件为 n ≥ ( y + 1 ) 2 ，即 ( y + 1 ) 2 ≤ n 时循环继续。
> 因此，循环执行的次数取决于满足该条件的最大整数 y。
> 设循环迭代了 k 次，则 k 满足 k 2 ≤ n 且 ( k + 1 ) 2 > n ，这意味着 k 是 ⌊ n ​ ⌋ 。
> 循环迭代次数与 n ​ 成正比，故时间复杂度为 O ( n ​ ) 。
> 其他选项中， O ( lo g n ) 、 O ( n ) 和 O ( n lo g n ) 均与迭代次数不符。
>

