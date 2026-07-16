---
title: "存储系统 第6题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "虚拟存储器"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 15
tags: ['课后题']
---

局部性通常有两种不同的形式：时间局部性和空间局部性。程序员是否能编写出高速缓
存友好的代码，就取决于这两方面的问题。对于下面这个函数，说法正确的是()。int            sumvec(int            v[N]){int        i, sum=0;for(i=0;i<N;i++)sum+=v[i];return            sum;
存友好的代码，就取决于这两方面的问题。对于下面这个函数，说法正确的是()。
int            sumvec(int            v[N]){
int        i, sum=0;
for(i=0;i<N;i++)
sum+=v[i];
return            sum;

A. 对于变量i 和 sum,   循环体具有良好的空间局部性
B. 对于变量i 、sum 和v[N],   循环体具有良好的空间局部性
C. 对于变量i 和 sum,   循环体具有良好的时间局部性
D. 对于变量i 、sum 和 v[N],  循环体具有良好的时间局部性

[tag_link]

正确答案：【解答】