---
title: "模拟卷4 数据结构 第7题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "数据结构"
knowledge_points:
  - "图的概念"
question_type: "choice"
difficulty: 3
number: 7

---

以下关于图的表述中，正确的是（ ）。

A\. 强连通有向图的任何顶点到其他所有顶点都有弧
B\. 图与树的区别在于图的边数大于或等于顶点数
C\. 无向图的连通分量指无向图中的极大连通子图
D\. 假设有图
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">G</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⟨</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=mclose>}⟩</span></span></span></span>
，顶点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8879em;vertical-align:-.136em></span><span class=mord><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⊆</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8879em;vertical-align:-.136em></span><span class=mord><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⊆</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
，则
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7519em></span><span class=mord><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0019em;vertical-align:-.25em></span><span class=mopen>{</span><span class=mord><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class=mclose>}</span></span></span></span>
构成
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">G</span></span></span></span>
的子图。

[图的概念](/study_methods/tags/408quiz//#%e5%9b%be%e7%9a%84%e6%a6%82%e5%bf%b5)

[tag_link]

正确答案：C
> <p>
首先分析选项 A：强连通有向图要求任意两个顶点之间存在双向路径，但并不要求直接有弧（即直接的边）。
> 例如，一个包含三个顶点的有向环，顶点间通过路径相连而非都有直接弧，因此该表述错误。
> <p>接着看选项 B：图与树的区别在于树是无环连通图，且对于 n 个顶点的树，边数为 n-1。
> 图的边数可以小于、等于或大于顶点数，例如孤立顶点图边数少于顶点数，因此该表述不准确。
> <p>选项 C 正确，因为无向图的连通分量定义为极大连通子图，即不能再添加其他顶点和边而保持连通的子图，这是图论中的标准概念。
> <p>最后检查选项 D：子图需要顶点集 V&rsquo;⊆V 和边集 E&rsquo;⊆E，且 E&rsquo;中边的端点必须都在 V&rsquo;中。
> 选项仅说明 V&rsquo;和 E&rsquo;是子集，未强调边的端点限制，因此表述不完整，错误。
> <p>综上，正确选项为 C。
>
