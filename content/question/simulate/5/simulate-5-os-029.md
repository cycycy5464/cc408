---
title: "模拟卷5 操作系统 第29题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "操作系统"
knowledge_points:
  - "缺页异常"
question_type: "choice"
difficulty: 3
number: 29

---

在某请求分页系统中，内存的存取时间为 1μs。若有一个可用的空页被置换的页表被修改，则它处理一个缺页中断需要 8μs；若被置换的页已被修改，则处理一个缺页中断因增加写回外存时间而需要 20μs。假设所有访问页表都在 TLB 中，且 TLB 中存储有页面是否在主存中的信息。假定 70% 被置换的页被修改过，为保证有效存取时间不超过 2μs，可接受的最大缺页中断率约为（ ）。

A\. 5.7%
B\. 11%
C\. 6.5%
D\. 50%

[缺页异常](/study_methods/tags/408quiz//#%e7%bc%ba%e9%a1%b5%e5%bc%82%e5%b8%b8)

[tag_link]

正确答案：C
> <p>
有效存取时间由无缺页和有缺页两种情况组成：
<ul><li>无缺页时，存取时间为内存存取时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
；
> </li><li>有缺页时，存取时间为缺页中断处理时间，该时间已包含后续内存访问。
> </li></ul><p>根据题意，缺页中断处理时间取决于被置换页是否被修改：
<ul><li><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>70%</span></span></span></span>
的概率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>20</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
（已修改）；
> </li><li><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>30%</span></span></span></span>
的概率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>8</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
（未修改）。
> </li></ul><p>平均处理时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>0.7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>20</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>0.3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>16.4</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span><span class=mord>.</span></span></span></span></span></div><p>设缺页中断率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span></span></span></span>
，则有效存取时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>EAT</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">p</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7778em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16.4</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>15.4</span><span class="mord mathnormal">p</span><span class=mord>.</span></span></span></span></span></div><p>要求
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord text"><span class=mord>EAT</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
，即

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>15.4</span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span></span></span></span></span></div><p>解得

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8304em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>15.4</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>0.0649</span><span class=mpunct>,</span></span></span></span></span></div><p>即约
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>6.5%</span></span></span></span>
。
> <p>因此，可接受的最大缺页中断率约为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>6.5%</span></span></span></span>
。
>
