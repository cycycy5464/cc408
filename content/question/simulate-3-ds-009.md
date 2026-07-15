---
title: "模拟卷3 数据结构 第9题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 9
---

下列关于 m 阶 B-树的说法中，正确的有（ ）。
I. 每个结点至少有两棵非空子树
II. 非叶结点仅起索引作用，每次查找一定会查找到某个叶结点
III. 所有叶子在同一层上
IV. 插入一个数据项引起 B-树结点分裂后，树长高一层

A\. I、II
B\. II、III
C\. III、IV
D\. III

[tag_link]

正确答案：D
> <p>
本题考查 B-树的性质。
> m 阶 B-树根结点至少有两棵子树（这两棵子树可以是空树），其他非叶结点至少有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.2em;vertical-align:-.35em></span><span class=minner><span class="mopen delimcenter" style=top:0><span class="delimsizing size1">⌈</span></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.6954em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">m</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style=top:0><span class="delimsizing size1">⌉</span></span></span></span></span></span>
棵子树，因此 I 错误。
> II 是 B+ 树的性质。
> B-树又称多路平衡查找树，叶结点都在同一层次上，可视为查找失败结点，因此 III 正确。
> 结点的分裂不一定会使树高增加 1，如图 1 所示；
> 只有当分裂传递到根结点并使根结点也分裂时，树高才会增加 1，如图 2 所示，因此 IV 错误。
> <div class=img-container style=height:auto;width:auto oncontextmenu=return!1><img src=/images/408simulate/3_9_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>
