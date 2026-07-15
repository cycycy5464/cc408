---
title: "模拟卷6 计算机网络 第39题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "choice"
difficulty: 3
number: 39
---

假设在没有发生拥塞的情况下，在一条往返时间 RTT 为 10ms 的线路上采用慢开始控制策略。如果接收窗口的大小为 24KB，最大报文段 MSS 为 2KB。那么发送方能发送出一个完全窗口（也就是发送窗口达到 24KB）需要的时间是（ ）。

A\. 30ms
B\. 60ms
C\. 50ms
D\. 40ms

[tag_link]

正确答案：D
> <p>
在慢开始控制策略中，拥塞窗口（cwnd）初始值为 1 个 MSS（2KB），每经过一个 RTT，cwnd 翻倍。
> 接收窗口大小为 24KB。
> 发送窗口取 cwnd 和接收窗口的最小值。
> 当 cwnd 增长到等于或超过 24KB 时，发送窗口达到 24KB。
> <p>计算 cwnd 增长过程：经过第一个 RTT 后，cwnd=4KB；
> 第二个 RTT 后，cwnd=8KB；
> 第三个 RTT 后，cwnd=16KB，仍小于 24KB；
> 第四个 RTT 后，cwnd=32KB，超过 24KB，此时发送窗口被接收窗口限制为 24KB，即完全窗口。
> <p>每个 RTT 为 10ms，因此达到完全窗口需要经过 4 个 RTT，总时间为 4 × 10ms = 40ms。
>
