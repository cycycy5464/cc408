---
title: "模拟卷6 计算机组成原理 第11题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "choice"
difficulty: 3
number: 11
---

一组经过第一趟 2-路归并排序后的记录的关键字为 (25,50,15,35,80,85,20,40,36,70)，其中包含 5 个长度为 2 的有序序，用 2-路归并排序方法对该序列进行第二趟归并后的结果为（ ）。

A\. 15,25,35,50,80,20,85,40,70,36
B\. 15,25,35,50,20,40,80,85,36,70
C\. 15,25,50,35,80,85,20,36,40,70
D\. 15,25,35,50,80,20,36,40,70,85

[归并排序](/study_methods/tags/408quiz//#%e5%bd%92%e5%b9%b6%e6%8e%92%e5%ba%8f)

[tag_link]

正确答案：B
> <p>
首先，第一趟归并后得到序列

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span></span></span></span></span></div><p>其中包含 5 个长度为 2 的有序子序列，分别为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span></span></span></span></span></div><p>在第二趟 2-路归并中，需要将相邻的有序子序列两两合并。
> 具体来说：
<ul><li>合并第一个和第二个子序列：将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mclose>)</span></span></span></span>
合并，得到有序序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span></span></span></span></li><li>合并第三个和第四个子序列：将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mclose>)</span></span></span></span>
合并，得到有序序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span></span></span></span></li><li>第五个子序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span></span></span></span>
没有相邻配对，保持原样。
> </li></ul><p>因此，第二趟归并后的序列由三个有序子序列依次组成：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span><span class=mpunct>,</span></span></span></span></span></div><p>整体为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span></span></span></span></span></div><p>对比选项，B 与此一致。
>
