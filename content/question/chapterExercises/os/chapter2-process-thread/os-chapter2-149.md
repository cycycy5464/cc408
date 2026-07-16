---
title: "进程与线程 第46题"
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
number: 149
tags: ['课后题']
---

有两个优先级相同的并发程序P₁ 和 P₂,  它们的执行过程如下所示。假设当前信号量s1=
0, s2=0 。 当 前 的z=2,   进程运行结束后，x,y   和Z 的值分别是()。进程P₁                                                                 进程P₂y :=1 ;  y:=y+2; z:=y+1;X:  =1  X:=x+1;P (s1)   ;V( s1)   ;X:=x+y;P (s2);Z:=x+Z;
0, s2=0 。 当 前 的z=2,   进程运行结束后，x,y   和Z 的值分别是()。
进程P₁                                                                 进程P₂
y :=1 ;  y:=y+2; z:=y+1;
X:  =1  X:=x+1;
P (s1)   ;
V( s1)   ;
X:=x+y;
P (s2);
Z:=x+Z;
y:=z+y;                                                                                  V ( s2)  ;
y:=z+y;                                                                                  V ( s2)  ;

A. 5,9,9                           B.5,9,4                            C.5,12,9                          D.5,12,4

[tag_link]

正确答案：C