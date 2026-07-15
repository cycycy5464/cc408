---
title: "模拟卷7 计算机网络 第35题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "choice"
difficulty: 3
number: 35
---

CSMA 协议可以利用多种监听算法来减小发送冲突的概率，下面关于各种监听算法的描述中，错误的是（ ）。

A\. Ⅰ、Ⅱ和Ⅲ
B\. Ⅱ和Ⅲ
C\. Ⅰ、Ⅱ和Ⅳ
D\. Ⅱ和Ⅳ

[tag_link]

正确答案：A
> <p> 首先，分析各监听算法的特性：非坚持型监听算法在信道忙时等待随机时间再监听，这减少了冲突，但可能导致信道空闲时无站点立即发送，从而增加网络空闲时间，因此陈述Ⅰ“有利于减少网络空闲时间”是错误的。
> <p>其次，1-坚持型监听算法在信道空闲时立即发送，虽然减少了空闲时间，但多个站点可能同时发送，导致冲突概率增加，因此陈述Ⅱ“有利于减少冲突的概率”是错误的。
> <p>再者，P 坚持型监听算法通过概率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.13889em>P</span></span></span></span>
发送来平衡冲突和空闲时间，相比非坚持型能减少空闲时间，因此陈述Ⅲ“无法减少网络的空闲时间”是错误的。
> <p>最后，1-坚持型算法因持续监听并在信道空闲时立即发送，能及时抢占信道，陈述Ⅳ是正确的。
> <p>综上，错误的陈述是Ⅰ、Ⅱ和Ⅲ，对应选项 A。
>
