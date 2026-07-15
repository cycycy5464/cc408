---
title: "模拟卷3 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "数据结构"
knowledge_points:
  - "复杂度分析"
question_type: "choice"
difficulty: 3
number: 1

---

设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
是描述问题规模的正整数，下面程序片段的时间复杂度是（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0503em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8003em><span class=svg-align style=top:-3em><span class=pstrut style=height:3em></span><span class=mord style=padding-left:.833em><span class="mord mathnormal">n</span></span></span><span style=top:-2.7603em><span class=pstrut style=height:3em></span><span class=hide-tail style=min-width:.853em;height:1.08em><svg width="400em" height="1.08em" viewBox="0 0 4e5 1080" preserveAspectRatio="xMinYMin slice"><path d="M95 702c-2.7.0-7.17-2.7-13.5-8-5.8-5.3-9.5-10-9.5-14 0-2 .3-3.3 1-4 1.3-2.7 23.83-20.7 67.5-54 44.2-33.3 65.8-50.3 66.5-51 1.3-1.3 3-2 5-2 4.7.0 8.7 3.3 12 10s173 378 173 378c.7.0 35.3-71 104-213s137.5-285 206.5-429S812 97.3 814 94c5.3-9.3 12-14 20-14H4e5v40H845.2724s-225.272 467-225.272 467-235 486-235 486c-2.7 4.7-9 7-19 7-6 0-10-1-12-3s-194-422-194-422-65 47-65 47zM834 80h4e5v40H834z"/></svg></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2397em><span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>

[复杂度分析](/study_methods/tags/408quiz//#%e5%a4%8d%e6%9d%82%e5%ba%a6%e5%88%86%e6%9e%90)

[tag_link]

正确答案：A
> 程序片段中，变量 i 初始化为 2。
> 循环条件为 i < n/3，每次循环体执行 i = i * 3，使得 i 的值以指数速度增长。
> 设循环执行次数为 k。
> 在执行 k 次后，i 的值变为 2 × 3^k。
> 循环终止时满足 2 × 3^k ≥ n/3，由此可得 k ≥ log₃(n/6)。
> 由于对数函数的特性，k 与 log n 成正比。
> 每次循环体执行时间为常数，因此整体时间复杂度取决于循环次数，为 O(log n)。
> 选项 A 正确。
>
