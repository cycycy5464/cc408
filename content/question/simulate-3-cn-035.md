---
title: "模拟卷3 计算机网络 第35题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "计算机网络"
knowledge_points:
  - "窗口大小限制"
question_type: "choice"
difficulty: 3
number: 35

---

下列关于滑动窗口的说法中，错误的是（ ）。
Ⅰ. 对于窗口大小为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的滑动窗口，最多可以有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
帧已发送但没有确认
Ⅱ. 假设帧序号有 3 位，采用连续 ARQ 协议，发送窗口的最大值为 4
Ⅲ. 在 GBN 协议中，如果发送窗口的大小为 16，则至少需要 4 位序列号才能保证协议不出错

A\. Ⅰ和Ⅱ
B\. 仅Ⅲ
C\. Ⅰ和Ⅲ
D\. Ⅰ、Ⅱ和Ⅲ

[窗口大小限制](/study_methods/tags/408quiz//#%e7%aa%97%e5%8f%a3%e5%a4%a7%e5%b0%8f%e9%99%90%e5%88%b6)

[tag_link]

正确答案：D
> 本题考查了有关滑动窗口的相关知识。
> 对于窗口大小为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的滑动窗口（发送窗口+接收窗口），发送窗口表示在还没有接收到对方确认信息的情况下，发送方最多还能发送多少个数据帧；
> 而接收窗口应该
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，所以发送窗口就应该
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，则最多只能有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
帧已发送但未收到确认。
> 所以 I 错误。
> 连续 ARQ 协议包括两种，后退
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>N</span></span></span></span>
帧（GBN），以及选择性重传(SR)，当采用后退
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>N</span></span></span></span>
帧协议时，发送窗口大小必须满足
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord mathnormal" style=margin-right:.13889em>W</span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7477em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.6644em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，而选择重传则是应该满足
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord mathnormal" style=margin-right:.13889em>W</span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">n</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span></span></span></span>
，而发送窗口最大值应该为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class="mord text"><span class=mord>MAX</span></span><span class=mopen>{</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class=mclose>}</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord text"><span class=mord>MAX</span></span><span class=mopen>{</span><span class=mord>7</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>4</span><span class=mclose>}</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>7</span></span></span></span>
，所以 II 错误。
> 同时，由
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7477em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.6644em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7804em;vertical-align:-.136em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16</span></span></span></span>
，可以得出
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
。
> 所以 III 错误。
>
