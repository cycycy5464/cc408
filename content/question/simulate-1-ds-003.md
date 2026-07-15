---
title: "模拟卷1 数据结构 第3题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "数据结构"
knowledge_points:
  - "完全二叉树"
question_type: "choice"
difficulty: 3
number: 3

---

已知 A[1..N] 是一棵顺序存储的完全二叉树，9 号结点和 11 号结点共同的祖先是（ ）。

A\. 4
B\. 6
C\. 2
D\. 8

[完全二叉树](/study_methods/tags/408quiz//#%e5%ae%8c%e5%85%a8%e4%ba%8c%e5%8f%89%e6%a0%91)

[tag_link]

正确答案：C
> 在顺序存储的完全二叉树中，节点编号对应数组索引，且任意节点 i 的父节点索引为 floor(i/2)。
> 对于节点 9，其祖先链依次为：9 → 4 → 2 → 1；
> 对于节点 11，其祖先链依次为：11 → 5 → 2 → 1。
> 比较两条祖先链，第一个共同的节点是 2，因此 9 号结点和 11 号结点共同的祖先是 2。
> 选项 A、B、D 均不在两者的共同祖先链中，故正确答案为 C。
>
