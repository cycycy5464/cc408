---
title: "模拟卷7 数据结构 第40题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 40
---

UDP 协议和 TCP 协议报文首部的非共同字段有（ ）。

A\. 源端口
B\. 目的端口
C\. 序列号
D\. 校验和

[协议数据单元](/study_methods/tags/408quiz//#%e5%8d%8f%e8%ae%ae%e6%95%b0%e6%8d%ae%e5%8d%95%e5%85%83)

[tag_link]

正确答案：C
> UDP 和 TCP 协议报文首部中，源端口和目的端口是两者都具备的字段，用于标识通信的端点。
> 校验和字段在 UDP 和 TCP 中也都存在，尽管 UDP 的校验和是可选的，但通常被视为首部的一部分。
> 序列号是 TCP 特有的字段，用于保证数据的有序传输和可靠性；
> UDP 作为无连接协议，没有序列号字段，因此序列号是两者的非共同字段。
>
