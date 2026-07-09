---
title: "模拟卷7 数据结构 第4题"
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
number: 4
---

含有 4 个元素值均不相同的结点的二叉排序树有（ ）种。

A\. 4

B\. 6

C\. 10

D\. 14

[tag_link]

正确答案：D
> 二叉排序树（BST）的结构数量由卡特兰数决定。
> 对于 n 个值均不相同的节点，不同形态的二叉排序树数量等于第 n 个卡特兰数 C n ​ ，计算公式为 C n ​ = n + 1 1 ​ ( n 2 n ​ ) , 其中 ( n 2 n ​ ) 表示组合数。
> 当 n = 4 时，计算 C 4 ​ ： C 4 ​ = 5 1 ​ ( 4 8 ​ ) = 5 1 ​ × 70 = 14. 因此，含有 4 个元素值均不相同的结点的二叉排序树共有 14 种。
>

