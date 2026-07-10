---
title: "模拟卷3 数据结构 第11题"
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
number: 11
---

如果一台计算机具有多个可以并行运行的 CPU，就可以同时执行相互独立的任务，则下列排序算法中，适合并行处理的是（ ）。

A\. II、VI 和 V

B\. II、III 和 V

C\. II、III、IV 和 V

D\. I、II、III、IV 和 V

[tag_link]

正确答案：A
> 考查各种排序算法的性质。
> 本题即分析排序算法的执行过程中，能否划分成多个子序列进行并行独立的排序。
> 快速排序在一趟排序划分成两个子序列后，各子序列又可并行排序；
> 归并排序的各个归并段可以并行排序。
> 而希尔排序分出来的几组子表也可以进行相对独立的排序。
> 因此 II、VI 和 V 满足并行性。
> 而其他选项不能划分成子序列来并行执行排序，故选 A。
>

