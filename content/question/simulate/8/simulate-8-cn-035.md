---
title: "模拟卷8 计算机网络 第35题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 8
subjects:
  - "计算机网络"
knowledge_points:
  - "协议数据单元"
  - "介质访问控制"
question_type: "choice"
difficulty: 3
number: 35

---

考虑建立一个 CSMA/CD 网，电缆长度为 1km，不使用中继器，传输速率为 1Gbps，电缆中信号的传播速率是 200000km/s，则该网络中最小帧长是（ ）。

A\. 10000bit
B\. 1000bit
C\. 5000bit
D\. 20000bit

[协议数据单元](/study_methods/tags/408quiz//#%e5%8d%8f%e8%ae%ae%e6%95%b0%e6%8d%ae%e5%8d%95%e5%85%83)
[介质访问控制](/study_methods/tags/408quiz//#%e4%bb%8b%e8%b4%a8%e8%ae%bf%e9%97%ae%e6%8e%a7%e5%88%b6)

[tag_link]

正确答案：A
> <p>
首先，计算信号在电缆中的传播时延。
> 电缆长度为 1 km，信号传播速率为 200000 km/s，因此传播时延为长度除以传播速率：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class="mord text"><span class=mord> km</span></span><span class=mord>/200000</span><span class="mord text"><span class=mord> km/s</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>5</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">6</span></span></span></span></span></span></span></span></span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">秒</span></span></span></span></span></span></div><p>即 5 微秒。
> <p>在 CSMA/CD 网络中，最小帧长需确保在帧传输过程中能检测到冲突，这要求帧的发送时间不小于信号往返传播的时间（即冲突窗口）。
> 冲突窗口时间为 2 倍传播时延：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>5</span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">微秒</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>10</span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">微秒</span></span></span></span></span></span></div><p>传输速率为 1 Gbps，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span></span></span></span></span></span></span></span></span>
比特/秒。
> 最小帧长等于冲突窗口时间乘以传输速率：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>10</span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">微秒</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1141em;vertical-align:-.25em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span></span></span></span></span></span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">比特</span><span class=mord>/</span><span class="mord cjk_fallback">秒</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9474em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">6</span></span></span></span></span></span></span></span></span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">秒</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1141em;vertical-align:-.25em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span></span></span></span></span></span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">比特</span><span class=mord>/</span><span class="mord cjk_fallback">秒</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>10000</span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">比特</span></span></span></span></span></span></div><p>因此，最小帧长为 10000 比特，对应选项 A。
>
