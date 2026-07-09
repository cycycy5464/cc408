---
title: "模拟卷5 数据结构 第4题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 4
---

一般说来，若深度为 k 的 n 个结点的二叉树具有最小路径长度时，第 k 层（根为第 1 层）上的结点数为（ ）。

A\.

B\.

C\.

D\.

[tag_link]

正确答案：B
> 对于深度为 k 且具有最小路径长度的二叉树，为了使所有结点到根的路径长度之和最小，树应尽可能平衡，即前 k-1 层完全填满。
> 前 k-1 层的结点总数为 2 k − 1 − 1 ，剩余结点全部位于第 k 层。
> 因此，第 k 层的结点数为 n − ( 2 k − 1 − 1 ) = n − 2 k − 1 + 1 ，对应选项 A 和 B（两者表达式相同）。
> 选项 C 和 D 与推导结果不符，故正确答案为 A。
>

