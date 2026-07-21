---
title: "模拟卷3 操作系统 第25题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "操作系统"
knowledge_points:
  - "进程和线程"
  - "进程概念"
question_type: "choice"
difficulty: 3
number: 25

---

系统拥有一个 CPU、IO1 和 IO2 为两个不同步的输入/输出装置，它们能够同时工作。当使用 CPU 之后控制转向 IO1、IO2 时，或者使用 IO1、IO2 之后控制转向 CPU 时，由控制程序执行中断处理，但这段处理时间忽略不计。有 A、B 两个进程同时被创建，进程 B 的调度优先权比进程 A 高，但是，当进程 A 正在占用 CPU 时，即使进程 B 需要占用 CPU，也不能打断进程 A 的执行。若在同一系统中分别单独执行，则需要占用 CPU、IO1、IO2 的时间如下图所示：

A\. 进程 A
B\. 进程 B
C\. 进程 A 和进程 B 同时
D\. 不一定

[进程和线程](/study_methods/tags/408quiz//#%e8%bf%9b%e7%a8%8b%e5%92%8c%e7%ba%bf%e7%a8%8b)
[进程概念](/study_methods/tags/408quiz//#%e8%bf%9b%e7%a8%8b%e6%a6%82%e5%bf%b5)

[tag_link]

正确答案：A
> <p>
由于进程 B 的调度优先级高于进程 A，且 CPU 非抢占（进程 A 占用 CPU 时不可被打断），初始时两进程同时就绪，CPU 优先分配给进程 B。
> 通过模拟并发执行的时间线：
<ul><li>进程 B 首先运行 CPU 20ms（0–20ms），随后进程 A 运行 CPU 25ms（20–45ms）。
> </li><li>进程 A 请求 IO1 时需等待至 50ms（因 IO1 被 B 占用），之后 A 使用 IO1 30ms（50–80ms），同时 B 运行 CPU 20ms（50–70ms）后使用 IO2 20ms（70–90ms）。
> </li><li>A 在 80ms 就绪后运行 CPU 20ms（80–100ms），期间 B 在 90ms 就绪但因 A 占用 CPU 而等待。
> </li><li>A 随后使用 IO2 20ms（100–120ms），B 运行 CPU 10ms（100–110ms）后等待 IO2 至 120ms。
> </li><li>B 使用 IO2 20ms（120–140ms），A 运行 CPU 20ms（120–140ms）。
> </li><li>最后 A 使用 IO1 30ms（140–170ms）结束，B 运行 CPU 45ms（140–185ms）结束。
> </li></ul><p>因此进程 A 在 170ms 结束，进程 B 在 185ms 结束，进程 A 先结束。
>
