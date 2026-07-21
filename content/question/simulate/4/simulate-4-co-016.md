---
title: "模拟卷4 组成原理 第16题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "组成原理"
knowledge_points:
  - "访存过程"
question_type: "choice"
difficulty: 3
number: 16

---

在 Cache 和主存构成的两级存储体系中，Cache 的存取时间是 100ns，主存的存取时间是 1000ns，如果希望有效（平均）存取时间不超过 Cache 存取时间 15%，则 Cache 的命中率至少应为（ ）。（设 Cache 和主存不能同时访问。）

A\. 90%
B\. 98%
C\. 95%
D\. 99%

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)

[tag_link]

正确答案：D
> <p>
在高速缓存与主存不能同时访问的两级存储体系中，有效存取时间取决于命中率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span></span></span></span>
。
> 命中时存取时间为高速缓存存取时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
，未命中时需先访问高速缓存（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
）再访问主存（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1000</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
），总时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1100</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
。
> 因此有效存取时间公式为：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3361em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">eff</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1000</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mord>.</span></span></span></span></span></div><p>题目要求有效存取时间不超过高速缓存存取时间的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>15%</span></span></span></span>
，即不超过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>100</span><span class="mord text"><span class=mord>ns</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1.15</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>115</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
。
> 代入不等式：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>115.</span></span></span></span></span></div><p>解得：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8778em;vertical-align:-.1944em></span><span class=mord>985</span><span class=mpunct>,</span><span class=mspace style=margin-right:1em></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>0.985</span><span class=mpunct>,</span></span></span></span></span></div><p>即命中率至少为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>98.5%</span></span></span></span>
。
> 选项中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>99%</span></span></span></span>
满足要求，因此高速缓存命中率至少应为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>99%</span></span></span></span>
。
>
