---
title: "进程与线程 第1题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "同步与互斥"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 150
tags: ['课后题']
---

下面是两个并发执行的进程，它们能正确运行吗?若不能请举例说明并改正。
int x;
process_P1{ int y,z;
x=1;
y=0;
if(x>=1) y=y+1;
z=y;
process_P2{ int t,u;
x=0;
t=0;
if(x<=1) t=t+2;
u=t;
}
}

[tag_link]

【解答】