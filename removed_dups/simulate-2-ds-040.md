---
title: "模拟卷2 数据结构 第40题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 40
---

A 和 B 建立 TCP 连接，MSS 为 1KB。某时，慢开始门限值为 2KB，A 的拥塞窗口为 4KB，在接下来的一个 RTT 内，A 向 B 发送了 4KB 的数据（TCP 的数据部分），并且得到了 B 的确认，确认报文中的窗口字段的值为 2KB，那么，请问在下一个 RTT 中，A 最多能向 B 发送的数据（　）。

A\. 2KB
B\. 5KB
C\. 5KB
D\. 4KB

[通信指标](/study_methods/tags/408quiz//#%e9%80%9a%e4%bf%a1%e6%8c%87%e6%a0%87)
[窗口大小限制](/study_methods/tags/408quiz//#%e7%aa%97%e5%8f%a3%e5%a4%a7%e5%b0%8f%e9%99%90%e5%88%b6)

[tag_link]

正确答案：A
> <p>
首先，TCP 发送方的实际发送窗口大小由拥塞窗口（cwnd）和接收方通告窗口（rwnd）共同决定，取两者最小值。
> 初始时，cwnd = 4 KB，ssthresh = 2 KB，由于 cwnd > ssthresh，因此 A 处于拥塞避免阶段。
> 在拥塞避免阶段，当发送的数据在一个 RTT 内被全部确认后，cwnd 会线性增加一个 MSS（1 KB），因此更新后的 cwnd = 4 KB + 1 KB = 5 KB。
> <p>然而，确认报文中携带的窗口字段值为 2 KB，即接收方通告窗口 rwnd = 2 KB。
> 因此，下一个 RTT 中 A 的发送窗口大小为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>min</span><span class=mopen>(</span><span class="mord text"><span class=mord>cwnd</span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>rwnd</span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>min</span><span class=mopen>(</span><span class=mord>5</span><span class="mord text"><span class=mord> KB</span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class="mord text"><span class=mord> KB</span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>2</span><span class="mord text"><span class=mord> KB</span></span></span></span></span></span></div><p>所以，A 最多能向 B 发送 2 KB 数据。
>
