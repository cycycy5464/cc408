---
title: "进程与线程 第4题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "死锁"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 202
tags: ['课后题']
---

考虑某个系统在下表时刻的状态。
进 程 名
Allocation
Max
Available
A
B
C
D
A
B
C
D
A
B
C
D
Po
0
0
1
2
0
0
1
2
1
5
2
0
P₁
1
0
0
0
1
7
5
0
P₂
1
3
5
4
2
3
5
6
P₃
0
0
1
4
0
6
5
6
165第 2 章   进 程 与 线 程
165
使用银行家算法回答下面的问题：
1) Need 矩阵是怎样的?
2)系统是否处于安全状态?如安全，请给出一个安全序列。
3)若从进程P₁ 发来一个请求(0,4,2,0),这个请求能否立刻被满足?如安全，请给出一 个安全序列。

[tag_link]

【解答】