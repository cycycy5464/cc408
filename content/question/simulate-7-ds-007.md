---
title: "模拟卷7 数据结构 第7题"
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
number: 7
---

一个含有 n 个顶点和 e 条边的简单无向图，其邻接矩阵存储中零元素的个数是（ ）。

A\.

B\.

C\.

D\.

[tag_link]

正确答案：D
> 邻接矩阵是一个 n × n 的矩阵，总共有 n 2 个元素。
> 在简单无向图中，没有自环，因此对角线上的 n 个元素均为零。
> 图的每条边对应两个对称的非对角线元素（例如，边 ( i , j ) 对应 A [ i ] [ j ] 和 A [ j ] [ i ] ），所以非零元素的个数为 2 e 。
> 零元素的个数等于总元素数减去非零元素数，即 n 2 − 2 e 。
>

