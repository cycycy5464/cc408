---
title: "模拟卷8 计算机组成原理 第11题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 8
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "choice"
difficulty: 3
number: 11
---

若对 29 个记录只进行三趟多路平衡归并，则选取的归并路数至少是（ ）。

A\. 2
B\. 3
C\. 4
D\. 5

[外部排序](/study_methods/tags/408quiz//#%e5%a4%96%e9%83%a8%e6%8e%92%e5%ba%8f)

[tag_link]

正确答案：C
> <p> 在多路平衡归并中，归并趟数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span></span></span></span>
与归并路数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
、初始归并段数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
之间的关系为：经过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span></span></span></span>
趟归并，最多能处理
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7936em></span><span class=mord><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7936em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span></span></span></span></span></span></span></span>
个初始归并段，即需满足

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9795em;vertical-align:-.136em></span><span class=mord><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8436em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mord>.</span></span></span></span></span></div><p>本题中，对 29 个记录排序，初始归并段数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>29</span></span></span></span>
，要求只进行三趟归并（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
），因此需满足

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0001em;vertical-align:-.136em></span><span class=mord><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>29.</span></span></span></span></span></div><p>计算各选项的立方：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6835em;vertical-align:-.0391em></span><span class=mord>8</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1.0585em;vertical-align:-.1944em></span><span class=mord>29</span><span class=mpunct>,</span><span class=mspace style=margin-right:1em></span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class=mord>3</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6835em;vertical-align:-.0391em></span><span class=mord>27</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1.0585em;vertical-align:-.1944em></span><span class=mord>29</span><span class=mpunct>,</span><span class=mspace style=margin-right:1em></span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class=mord>4</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7804em;vertical-align:-.136em></span><span class=mord>64</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1.0585em;vertical-align:-.1944em></span><span class=mord>29</span><span class=mpunct>,</span><span class=mspace style=margin-right:1em></span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class=mord>5</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7804em;vertical-align:-.136em></span><span class=mord>125</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>29.</span></span></span></span></span></div><p>若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
，则
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6835em;vertical-align:-.0391em></span><span class=mord>27</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>29</span></span></span></span>
，需至少四趟归并，不符合“只进行三趟”的要求；
> <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span></span></span></span>
时，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7804em;vertical-align:-.136em></span><span class=mord>64</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>29</span></span></span></span>
，可在三趟内完成。
> 因此归并路数至少为 4。
>
