---
title: "模拟卷5 数据结构 第7题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "最小生成树"
question_type: "choice"
difficulty: 3
number: 7

---

如果具有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个顶点的图是一个环，则它有（ ）棵生成树。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
D\. 1

[最小生成树](/study_methods/tags/408quiz//#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a0%91)

[tag_link]

正确答案：B
> 由于图是一个环，它包含 n 个顶点和 n 条边。
> 生成树是连接所有顶点且无环的子图，对于环图，只需移除任意一条边即可打破环并得到一棵生成树。
> 环中共有 n 条边，每条边的移除对应一棵不同的生成树，因此生成树的数量为 n。
>
