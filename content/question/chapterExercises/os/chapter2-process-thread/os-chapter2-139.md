---
title: "进程与线程 第36题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "同步与互斥"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 139
tags: ['课后题']
---

两个进程P₀ 、P₁ 互斥的 Peterson 算法描述如下：
进程P0
flag[0       ]=1;
(1)  ;
while(flag[1]&&turn==1); 临界区；
flag[0]=0;
其余代码；
进程P1
flag    [ 1]=1; (2);
while(flag[0]&&turn==0); 临界区；
flag[1]=0;
其余代码；
其中，(1)和(2)处的代码分别为()。
118                 2 0 2 7 年 操 作 系 统 考 研 复 习 指 导

A. turn=0,turn=0         B.turn=0,turn=1             C.    turn=1,turn=0           D.turn=1,turn=1

[tag_link]

正确答案：C