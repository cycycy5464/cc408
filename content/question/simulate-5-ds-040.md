---
title: "模拟卷5 数据结构 第40题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 40
---

第一次传输时，设 TCP 的拥塞窗口的慢启动门限初始值为 8（单位为报文段），当拥塞窗口上升到 12 时，网络发生超时，TCP 开始慢启动和拥塞避免，那么第 12 次传输时拥塞窗口大小为（ ）。

A\. 5
B\. 6
C\. 7
D\. 8

[tag_link]

正确答案：B
> <p> 首先，根据 TCP 拥塞控制机制，初始慢启动门限 ssthresh=8，拥塞窗口 cwnd 从 1 开始。
> 在慢启动阶段，cwnd 每轮次翻倍：第 1 次传输 cwnd=1，第 2 次传输 cwnd=2，第 3 次传输 cwnd=4，第 4 次传输 cwnd=8（达到 ssthresh，进入拥塞避免）。
> 拥塞避免阶段每轮次 cwnd 加 1：第 5 次传输 cwnd=9，第 6 次传输 cwnd=10，第 7 次传输 cwnd=11，第 8 次传输 cwnd=12。
> 此时网络发生超时，超时后将 ssthresh 设置为当前 cwnd 的一半，即 12/2=6，cwnd 重置为 1。
> <p>超点后重新开始慢启动：第 9 次传输 cwnd=1，第 10 次传输 cwnd=2，第 11 次传输 cwnd=4。
> 由于此时 cwnd=4 小于 ssthresh=6，仍处于慢启动，但慢启动的目标是使 cwnd 达到 ssthresh，因此从第 11 次传输到第 12 次传输，cwnd 应从 4 增长至 ssthresh 值 6，而不是翻倍到 8。
> 故第 12 次传输时 cwnd=6。
>
