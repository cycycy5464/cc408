---
title: "进程与线程 第33题"
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
number: 136
tags: ['课后题']
---

有两个并发进程P₁ 和 P₂, 其程序代码如下：
P1  ( ) {
P2  (){
x=1;
//A1
x=-3;
//B1
y=2;
C=x*x;
Z=x+y;
print
c;
//B2
print
z;
可能打印出的z 值有(),可能打印出的c 值 有 ( ) ( 其 中x 为 P₁,P₂  的共享变量)。A.z=1,-3;c=-1,9                                             B.z=-1,3;c=1,9C.z=-1,3,1;c=9                                               D.z=3;c=1,934.   并发进程之间的关系是()。A.  无关的                            B. 相关的C.   可能相关的                         D.   可能是无关的，也可能是有交往的35.  若系统中有4个进程共享3台打印机，采用信号量机制控制打印机的共享使用，则信号 量的取值范围是()。A.[-1,4]                          B . [-2,2]          C.[-1,3]                              D.[-3,2]36. 两个进程P₀ 、P₁ 互斥的 Peterson 算法描述如下：进程P0flag[0       ]=1;(1)  ;while(flag[1]&&turn==1); 临界区；flag[0]=0;其余代码；进程P1flag    [ 1]=1; (2);while(flag[0]&&turn==0); 临界区；flag[1]=0;其余代码；
可能打印出的z 值有(),可能打印出的c 值 有 ( ) ( 其 中x 为 P₁,P₂  的共享变量)。

A. z=1,-3;c=-1,9                                             B.z=-1,3;c=1,9
C. z=-1,3,1;c=9                                               D.z=3;c=1,9

[tag_link]

正确答案：B