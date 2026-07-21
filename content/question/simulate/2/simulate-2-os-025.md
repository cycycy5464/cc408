---
title: "模拟卷2 操作系统 第25题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "操作系统"
knowledge_points:
  - "临界资源"
question_type: "choice"
difficulty: 3
number: 25

---

��某个十字路口，每个车道只允许一辆汽车通过，且允许直行、左拐和右拐，如图 1 所示。如果把各个方向的车看成进程，则需要对这些进程进行同步，那么这里临界资源个数至少应该有（　）个。

A\. 1
B\. 2
C\. 4
D\. 不确定

[临界资源](/study_methods/tags/408quiz//#%e4%b8%b4%e7%95%8c%e8%b5%84%e6%ba%90)

[tag_link]

正确答案：C
> <p>
<div class=img-container style=height:auto;width:50% oncontextmenu=return!1><img src=/images/408simulate/2_25_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1></div><p>不妨如上图所示，把十字路口车道的公共区域分为 4 块，分别为图上的 1、2、3、4，直行的车辆需要获得该方向上的两个邻近的临界资源，如北方开来的车辆需要获得 1、2 两个临界资源。
> 南方开来的车需要获得 3、4 两个临界资源。
> 而往右转的车辆则只需要获得一个临界资源，比如北方来车右转的情况需要获得 1 这个临界资源。
> 左转的情况需要获得 3 个临界资源，比如北方来车左转组需要 1、2、3 号临界资源。
> 综上所述，4 个临界资源便可以很好地保证车子不相撞（即互斥的效果）。
> 当然只用 4 个信号量还是很容易造成死锁的，不过这并不是本题要考虑的问题，题目中问到的是至少用几个信号量。
> <p>也可以用排除法来做该题，该路口可以有南北方向车同时直行，所以临界资源个数大于或等于 2，排除 A。
> 该路口可以 4 个方向车都左转，所以临界资源个数大于或等于 4，排除 B。
> D 选项通常不会选，所以选 C。
>
