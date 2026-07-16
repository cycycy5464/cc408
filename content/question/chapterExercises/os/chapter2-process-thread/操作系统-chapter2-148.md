---
title: "进程与线程 第45题"
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
number: 148
tags: ['课后题']
---

哲学家就餐问题的解决方案如下：
semaphore                 *chopstick[5];semaphore            *seat;哲学家i:P (seat);P(chopStick[i]);P(chopStick[(i+1)85]); 吃饭V(chopstick[i]);V(chopStick[(i+1)85]);V(seat)
semaphore                 *chopstick[5];
semaphore            *seat;
哲学家i:
P (seat);
P(chopStick[i]);
P(chopStick[(i+1)85]); 吃饭
V(chopstick[i]);
V(chopStick[(i+1)85]);
V(seat)
其中，信号量seat 的初值最大为()。

A. 0                                  B.1                                  C.4                                   D.5

[tag_link]

正确答案：C