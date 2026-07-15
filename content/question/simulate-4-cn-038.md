---
title: "模拟卷4 计算机网络 第38题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "计算机网络"
knowledge_points:
  - "以太网"
  - "协议数据单元"
question_type: "choice"
difficulty: 3
number: 38

---

下图中，主机 A 发送一个 IP 数据报给主机 B。通信过程中以太网 1 上出现的以太网帧中承载一个 IP 数据报，该以太网帧中的目的地址和 IP 报头中的目的地址分别是（ ）。

A\. B 的 MAC 地址，B 的 IP 地址
B\. B 的 MAC 地址，R1 的 IP 地址
C\. R1 的 MAC 地址，B 的 IP 地址
D\. R1 的 MAC 地址，R1 的 IP 地址

[以太网](/study_methods/tags/408quiz//#%e4%bb%a5%e5%a4%aa%e7%bd%91)
[协议数据单元](/study_methods/tags/408quiz//#%e5%8d%8f%e8%ae%ae%e6%95%b0%e6%8d%ae%e5%8d%95%e5%85%83)

[tag_link]

正确答案：C
> 在主机 A 向主机 B 发送 IP 数据报的过程中，由于主机 B 位于不同的网络（通过 WAN 连接），主机 A 需要先将数据报发送到默认网关（即交换机 R1，在此场景中充当路由器或网关角色）。
> 因此，在以太网 1 上，主机 A 发出的以太网帧的目的 MAC 地址是下一跳设备 R1 的 MAC 地址，以便帧能正确传递到 R1。
> 而 IP 数据报头的目的 IP 地址始终是最终目标主机 B 的 IP 地址，不会在传输过程中改变。
> 所以，以太网帧中的目的地址是 R1 的 MAC 地址，IP 报头中的目的地址是 B 的 IP 地址，对应选项 C。
>
