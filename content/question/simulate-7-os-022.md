---
title: "模拟卷7 操作系统 第22题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "choice"
difficulty: 3
number: 22
---

对于单 CPU 单通道工作过程，下列可以完全并行工作的是（ ）。

A\. 程序和程序之间
B\. 程序和通道之间
C\. 程序和设备之间
D\. 设备和设备之间

[tag_link]

正确答案：C
> <p> 本题考查通道的工作原理。
> 做题的时候要注意完全并行的“完全”这两个字，对于单 CPU 系统来讲，程序和程序之间是并发的关系，而不是真正意义上的并行，要理解好并发和并行的区别。
> 通道方式是 DMA 方式的进一步发展，通道实际上也是实现 I/O 设备和主存之间直接交换数据的控制器。
> 通道的基本工作过程如下图所示。
> <div class=img-container style=height:auto;width:80% oncontextmenu=return!1><img src=/images/408simulate/7_22_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1></div><p>CPU 通过执行 I/O 指令负责启停通道，以及处理来自通道的中断实现对通道的管理，因此通道和程序（即 CPU）并没有完全并行，因为通道仍然需要 CPU 来对它实行管理，B 错误。
> 而在设备工作时，它只与通道交互，此时程序与其并行工作，C 正确。
> 而 A、D 显然错误。
>
