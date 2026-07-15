---
title: "模拟卷4 数据结构 第41题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "数据结构"
knowledge_points:
  - "最小生成树"
question_type: "comprehensive"
difficulty: 4
number: 41

---

请回答下列问题：

(1) 试证明若图中各条边的权值各不相同，则它的最小生成树唯一。
(2) Prim 算法和 Kruskal 算法生成的最小生成树一定相同吗？
(3) 画出下列带权图 G 的所有最小生成树。

[最小生成树](/study_methods/tags/408quiz//#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a0%91)

[tag_link]

<p>**【解析】**
(1) 采用反证法证明：假设图中有两个不同的最小生成树
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
。设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中但不在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中的权值最小的边。将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
添加到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中，会形成一个环，该环中至少存在一条边
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
不在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中。由于图中各边权值各不相同，比较
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
的权值。若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.10764em>f</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal">e</span><span class=mclose>)</span></span></span></span>
，则在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
替换
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
会得到一棵权值更小的生成树，与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
是最小生成树矛盾；若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.10764em>f</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal">e</span><span class=mclose>)</span></span></span></span>
，则在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
替换
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
会得到一棵权值更小的生成树，与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
是最小生成树矛盾。因此假设不成立，最小生成树唯一。
<p>(2) Prim 算法和 Kruskal 算法都是贪心算法，用于求解最小生成树。当图中边权值各不相同时，最小生成树唯一，因此两种算法必然得到相同的最小生成树。但当图中存在权值相同的边时，最小生成树可能不唯一，两种算法在选择边时可能做出不同选择，从而生成不同的最小生成树。因此，它们生成的最小生成树不一定相同。
<p>(3) 根据 Kruskal 算法，先把
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">d</span></span></span></span>
的边（权值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>20</span></span></span></span>
）加入集合，而接下来选择下一条边时，因为有两条权值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>40</span></span></span></span>
的边可以选择，那么因为不同的选择就会生成出不同的最小生成树。若选择
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7778em;vertical-align:-.0833em></span><span class="mord mathnormal">b</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">d</span></span></span></span>
，然后同样出现
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">d</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">a</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">c</span></span></span></span>
的选择，而不管先选择哪条边，另一条边也会成为下一个选择的对象，所以这里不影响树的结构，最后答案为左边这棵树；而当之前第二次选择边的时候，选择
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">b</span></span></span></span>
则会是右边的最小生成树。
<div class=img-container style=height:auto;width:60% oncontextmenu=return!1> [图片]
