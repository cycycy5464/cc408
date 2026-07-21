---
title: "模拟卷5 计算机网络 第37题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "计算机网络"
knowledge_points:
  - "路由器"
question_type: "choice"
difficulty: 3
number: 37

---

路由器中发现 TTL 值为 0 的分组，将进行（ ）处理，并向源主机返回（ ）的 ICMP 报文。

A\. 返回发送方，源点抑制
B\. 继续转发，改变路由
C\. 丢弃，时间超过
D\. 本地提交，终点不可达

[路由器](/study_methods/tags/408quiz//#%e8%b7%af%e7%94%b1%e5%99%a8)

[tag_link]

正确答案：C
> <p>
在 IP 网络中，TTL（生存时间）字段用于限制数据包在网络中的存活跳数。
> 路由器每转发一次分组，TTL 值减 1；
> 当 TTL 值减为 0 时，路由器必须丢弃该分组，以防止其无限循环消耗网络资源。
> <p>丢弃后，路由器会向源主机发送一个 ICMP 时间超过报文（ICMP Type 11），通知源主机该分组因 TTL 超时而被丢弃。
> 这有助于源主机诊断网络路径问题，例如在 traceroute 工具中就是利用这一机制。
> <p>其他选项中：A 的“源点抑制”是 ICMP 用于流量控制的报文；
> B 的“改变路由”是 ICMP 重定向报文，用于提示更优路由；
> D 的“终点不可达”是 ICMP 用于指示目的地无法到达的报文。
> 这些均与 TTL 值为 0 的处理场景无关。
>
