---
title: "模拟卷4 计算机网络 第36题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "choice"
difficulty: 3
number: 36
---

TCP/IP 网络中，某主机的 IP 地址为 130.25.3.135，子网掩码为 255.255.255.192，那么该主机所在的子网的网络地址是（ ），该子网最大可分配地址个数是（ ）。

A\. 130.25.0.0, 30
B\. 130.25.3.0, 30
C\. 130.25.3.128, 62
D\. 130.25.3.255, 126

[tag_link]

正确答案：C
> <p>
首先，计算子网的网络地址。
> 将 IP 地址 `130.25.3.135` 和子网掩码 `255.255.255.192` 转换为二进制进行 AND 操作。
> <ul><li>IP 地址的二进制为 `10000010.00011001.00000011.10000111`</li><li>子网掩码的二进制为 `11111111.11111111.11111111.11000000`</li></ul><p>AND 操作后，前三个字节不变，最后一个字节为
`10000111 AND 11000000 = 10000000`
即十进制 `128`，因此网络地址为 `130.25.3.128`。
> <p>其次，计算子网最大可分配地址个数。
> 子网掩码 `255.255.255.192` 对应 `/26`，主机位有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>6</span></span></span></span>
位，总主机地址数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>64</span></span></span></span>
。
> 减去网络地址和广播地址后，可分配地址个数为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>64</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>62</span></span></span></span></span></div><p>因此，该子网网络地址为 `130.25.3.128`，最大可分配地址个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>62</span></span></span></span>
，对应选项 C。
>
