---
title: "模拟卷4 数据结构 第9题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "数据结构"
knowledge_points:
  - "堆的概念"
question_type: "choice"
difficulty: 3
number: 9

---

一组数据 (30,20,10,15,35,1,10,5)，用堆排序（小顶堆）的筛选方法建立的初始堆为（ ）。

A\. 1,5,15,20,35,10,30,10
B\. 1,10,30,10,5,15,35,20
C\. 1,5,10,15,35,30,10,20
D\. A、B 和 C 均不正确

[堆的概念](/study_methods/tags/408quiz//#%e5%a0%86%e7%9a%84%e6%a6%82%e5%bf%b5)

[tag_link]

正确答案：C
> <p> 考查初始堆的建立。
> 首先对以第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌋</span></span></span></span>
个结点为根的子树（也即最后一个结点的父结点为根的子树）筛选，使该子树成为堆，之后向前依次对各结点为根的子树进行筛选，直到筛选到根结点。
> 从
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>∼</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
依次筛选堆的过程如下图所示：
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1><img src=/images/408simulate/4_9_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>
