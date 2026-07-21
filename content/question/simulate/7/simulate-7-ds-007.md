---
title: "模拟卷7 数据结构 第7题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "数据结构"
knowledge_points:
  - "邻接矩阵"
question_type: "choice"
difficulty: 3
number: 7

---

一个含有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个顶点和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
条边的简单无向图，其邻接矩阵存储中零元素的个数是（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class="mord mathnormal">e</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class="mord mathnormal">e</span></span></span></span>

[邻接矩阵](/study_methods/tags/408quiz//#%e9%82%bb%e6%8e%a5%e7%9f%a9%e9%98%b5)

[tag_link]

正确答案：D
> 邻接矩阵是一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的矩阵，总共有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
个元素。
> 在简单无向图中，没有自环，因此对角线上的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个元素均为零。
> 图的每条边对应两个对称的非对角线元素（例如，边
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal">i</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.05724em>j</span><span class=mclose>)</span></span></span></span>
对应
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">A</span><span class=mopen>[</span><span class="mord mathnormal">i</span><span class=mclose>]</span><span class=mopen>[</span><span class="mord mathnormal" style=margin-right:.05724em>j</span><span class=mclose>]</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">A</span><span class=mopen>[</span><span class="mord mathnormal" style=margin-right:.05724em>j</span><span class=mclose>]</span><span class=mopen>[</span><span class="mord mathnormal">i</span><span class=mclose>]</span></span></span></span>
），所以非零元素的个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class="mord mathnormal">e</span></span></span></span>
。
> 零元素的个数等于总元素数减去非零元素数，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class="mord mathnormal">e</span></span></span></span>
。
>
