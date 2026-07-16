---
title: "指令系统 第4题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "CISC和RISC"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 44
tags: ['课后题']
---

某C 语言程序中对数组变量b 的声明为“int    b[10][5];”, 有一条for 语句如下：
for(i=0;i<10;i++)for(j=0;j<5;j++)     sum+=b[i][j];
for(i=0;i<10;i++)
for(j=0;j<5;j++)     sum+=b[i][j];
假设执行到“sum+=b[i][j];” 时 ，sum 的值在 eax中 ，b[i][0]所在的地址在 edx 中，j  在 esi中，则“sum+=b[i][i];” 所对应的指令( Intel 格式)可以是()。

A. add   dword   ptr    eax,[edx+esi*4]           B.add   dword    ptr    eax,[esi+edx*4]
C. add  dword  ptr  eax,[edx+esi*2]          D.add   dword   ptr   eax,[esi+edx*2]

[tag_link]

正确答案：【解答】