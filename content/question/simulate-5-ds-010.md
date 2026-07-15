---
title: "模拟卷5 数据结构 第10题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "堆的概念"
question_type: "choice"
difficulty: 3
number: 10

---

堆排序分为两个阶段，其中第一阶段将给定的序列建成一个堆，第二阶段逐次输出堆顶元素。设给定序列{48,62,35,77,55,14,35,98}，若在堆排序的第一阶段将该序列建成一个堆（大根堆），那么交换元素的次数为（ ）。

A\. 5
B\. 6
C\. 7
D\. 8

[堆的概念](/study_methods/tags/408quiz//#%e5%a0%86%e7%9a%84%e6%a6%82%e5%bf%b5)

[tag_link]

正确答案：B
> <p> 考查初始堆的构造过程。
> 首先对以第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌋</span></span></span></span>
个结点为根的子树筛选，使该子树成为堆，之后向前依次对各结点为根的子树进行筛选，直到筛选到根结点。
> 序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class=mord>48</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>62</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>77</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>55</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>14</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>98</span><span class=mclose>}</span></span></span></span>
建立初始堆的过程如下所示：
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1><img src=/images/408simulate/5_10_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>
