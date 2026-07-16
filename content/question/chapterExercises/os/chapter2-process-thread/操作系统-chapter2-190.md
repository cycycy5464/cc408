---
title: "进程与线程 第24题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "死锁"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 190
tags: ['课后题']
---

有两个并发进程，对于如下这段程序的运行，正确的说法是()。
int                   x,y,z,t,u; P1  ( )
while(1){ x=0;
t=  0 ;
if       x<=1 u=t;
while(1){
x= 1 ;
y=0;
if      x>=1       then z = y ;
then       t=t+2;
P2 ()
y=y+1;

A. 程序能正确运行，结果唯一           B.   程序不能正确运行，可能有两种结果
C. 程序不能正确运行，结果不确定        D.  程序不能正确运行，可能死锁

[tag_link]

正确答案：C