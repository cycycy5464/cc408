---
title: "模拟卷7 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
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
是描述问题规模的正整数，下列程序片段的时间复杂度是（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0503em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8003em><span class=svg-align style=top:-3em><span class=pstrut style=height:3em></span><span class=mord style=padding-left:.833em><span class="mord mathnormal">n</span></span></span><span style=top:-2.7603em><span class=pstrut style=height:3em></span><span class=hide-tail style=min-width:.853em;height:1.08em><svg width="400em" height="1.08em" viewBox="0 0 4e5 1080" preserveAspectRatio="xMinYMin slice"><path d="M95 702c-2.7.0-7.17-2.7-13.5-8-5.8-5.3-9.5-10-9.5-14 0-2 .3-3.3 1-4 1.3-2.7 23.83-20.7 67.5-54 44.2-33.3 65.8-50.3 66.5-51 1.3-1.3 3-2 5-2 4.7.0 8.7 3.3 12 10s173 378 173 378c.7.0 35.3-71 104-213s137.5-285 206.5-429S812 97.3 814 94c5.3-9.3 12-14 20-14H4e5v40H845.2724s-225.272 467-225.272 467-235 486-235 486c-2.7 4.7-9 7-19 7-6 0-10-1-12-3s-194-422-194-422-65 47-65 47zM834 80h4e5v40H834z"/></svg></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2397em><span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>

[复杂度分析](/study_methods/tags/408quiz//#%e5%a4%8d%e6%9d%82%e5%ba%a6%e5%88%86%e6%9e%90)

[tag_link]

正确答案：A
> <p>
程序首先将变量
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span></span></span></span>
初始化为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的平方，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
。
> 然后进入 while 循环，循环条件为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><span class=mrel><span class="mord vbox"><span class=thinbox><span class=rlap><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=inner><span class=mord><span class=mrel></span></span></span><span class=fix></span></span></span></span></span><span class=mrel>=</span></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，每次迭代将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span></span></span></span>
除以
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
。
> 循环的迭代次数取决于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span></span></span></span>
从
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
减少到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
所需除以
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
的次数。
> <p>设迭代次数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
，经过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
次迭代后，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span></span></span></span>
的值变为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0991em;vertical-align:-.25em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mord>/</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span></span></span></span></span></span></span></span></span></span></span>
。
> 当循环终止时，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，因此有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0991em;vertical-align:-.25em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mord>/</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8491em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span></span></span></span></span></span></span></span></span></span></span>
。
> 取对数可得
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.9386em;vertical-align:-.2441em></span><span class=mord>2</span><span class=mspace style=margin-right:.1667em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span></span></span></span>
。
> <p>在时间复杂度分析中，常数因子可以忽略，因此迭代次数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
的数量级为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
。
> 所以，该程序片段的时间复杂度是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
。
> 对比选项，A 正确。
>
