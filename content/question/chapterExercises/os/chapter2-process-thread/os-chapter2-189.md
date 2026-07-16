---
title: "进程与线程 第23题"
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
number: 189
tags: ['课后题']
---

下面是并发进程的程序代码，正确的是()。
Semaphore          x1=x2=y=1;
int         c1=c2=0;
P1()
{
while(1){
P(x 1);
if(++c1==1)P(y); V(x1) ;
computer(A);
P(x 1);
if(--c1==0)V(y); V(x1) ;
}
}
P2()
{
while(1){
P(x 2);
if(++c2==1)P(y);
V(x2) ;
computer(B);
P(x 2);
if(--c2==0)V(y);
V(x2) ;
}
}

A. 进程不会死锁，也不会“饥饿”        B.   进程不会死锁，但是会“饥饿”C.  进程会死锁，但是不会“饥饿”        D.  进程会死锁，也会“饥饿”24.有两个并发进程，对于如下这段程序的运行，正确的说法是()。int                   x,y,z,t,u; P1  ( )while(1){ x=0;t=  0 ;if       x<=1 u=t;while(1){x= 1 ;y=0;if      x>=1       then z = y ;then       t=t+2;P2 ()y=y+1;
A. 进程不会死锁，也不会“饥饿”        B.   进程不会死锁，但是会“饥饿”
C. 进程会死锁，但是不会“饥饿”        D.  进程会死锁，也会“饥饿”

[tag_link]

正确答案：B