---
title: "模拟卷7 组成原理 第20题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "组成原理"
knowledge_points:
  - "计算机性能指标"
question_type: "choice"
difficulty: 3
number: 20

---

在 32 位总线系统中，若时钟频率为 500MHz，传送一个 32 位字需要 5 个时钟周期，则该总线系统的数据传输速率是（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>200</span><span class="mord mathnormal" style=margin-right:.05017em>MB</span><span class=mord>/</span><span class="mord mathnormal">s</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>400</span><span class="mord mathnormal" style=margin-right:.05017em>MB</span><span class=mord>/</span><span class="mord mathnormal">s</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>600</span><span class="mord mathnormal" style=margin-right:.05017em>MB</span><span class=mord>/</span><span class="mord mathnormal">s</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>800</span><span class="mord mathnormal" style=margin-right:.05017em>MB</span><span class=mord>/</span><span class="mord mathnormal">s</span></span></span></span>

[计算机性能指标](/study_methods/tags/408quiz//#%e8%ae%a1%e7%ae%97%e6%9c%ba%e6%80%a7%e8%83%bd%e6%8c%87%e6%a0%87)

[tag_link]

正确答案：B
> <p> 首先，理解关键参数：总线宽度为 32 位，时钟频率为 500 MHz，传送一个 32 位字需要 5 个时钟周期。
> 数据传输速率指单位时间内传输的数据量，通常以字节每秒（B/s）为单位。
> <p>计算每秒传输的字数：时钟频率为 500 MHz，即每秒有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>500</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span>
个时钟周期。
> 由于每 5 个时钟周期传输一个字，因此每秒传输的字数为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>500</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9474em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1141em;vertical-align:-.25em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">字</span><span class=mord>/</span><span class="mord cjk_fallback">秒</span></span></span></span></span></span></div><p>每个字的数据量：32 位等于 4 字节（因为 8 位为 1 字节）。
> 因此，每秒传输的数据量为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1141em;vertical-align:-.25em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">字</span><span class=mord>/</span><span class="mord cjk_fallback">秒</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>4</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">字节</span><span class=mord>/</span><span class="mord cjk_fallback">字</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>400</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1141em;vertical-align:-.25em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">字节</span><span class=mord>/</span><span class="mord cjk_fallback">秒</span></span></span></span></span></span></div><p>在数据传输速率中，常以 MB/s 表示兆字节每秒，其中 1 MB =
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span>
字节。
> 因此，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>400</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span>
字节/秒等于 400 MB/s，对应选项 B。
>
