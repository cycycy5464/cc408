---
title: "模拟卷4 操作系统 第28题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "choice"
difficulty: 3
number: 28
---

在一个请求分页系统中，采用 LRU 页面置换算法时，假如一个作业的页面走向为 1,3,2,1,1,3,5,1,3,2,1,5。当分配给该作业的物理块数分别为 3 和 4 时，则在访问过程中所发生的缺页率分别为（ ）。

A\. 50%、33%
B\. 25%、100%
C\. 25%、33%
D\. 50%、75%

[tag_link]

正确答案：A
> <p>
首先计算物理块数为 3 时的缺页率。
> 采用 **LRU 算法**，模拟访问过程：初始物理块为空，页面走向为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>5</span></span></span></span></span></div><p>
当物理块数为 3 时，访问过程中缺页发生情况如下：
<ul><li>访问 1、3、2 时均缺页（加载页面）；
> </li><li>访问第 4 个页面 1 时命中；
> </li><li>第 5 个页面 1 命中；
> </li><li>第 6 个页面 3 命中；
> </li><li>第 7 个页面 5 缺页（置换最近最少使用的页面 2）；
> </li><li>第 8 个页面 1 命中；
> </li><li>第 9 个页面 3 命中；
> </li><li>第 10 个页面 2 缺页（置换页面 5）；
> </li><li>第 11 个页面 1 命中；
> </li><li>第 12 个页面 5 缺页（置换页面 3）。
> </li></ul><p>总计缺页次数为 6 次，总访问次数为 12 次，缺页率为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>12</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>6</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>50%</span></span></span></span></span></div><p>再计算物理块数为 4 时的缺页率。
> 物理块数为 4 时，模拟过程如下：
<ul><li>访问 1、3、2 时均缺页（加载页面）；
> </li><li>访问第 4 个页面 1 命中；
> </li><li>第 5 个页面 1 命中；
> </li><li>第 6 个页面 3 命中；
> </li><li>第 7 个页面 5 缺页（此时物理块未满，加载页面 5）；
> </li><li>之后第 8 至 12 个页面
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>5</span></span></span></span>
均在物理块中命中。
> </li></ul><p>总计缺页次数为 4 次，总访问次数为 12 次，缺页率约为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>12</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>33%</span></span></span></span></span></div><p>因此，物理块数 3 和 4 对应的缺页率分别为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>50%</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>33%</span></span></span></span>
，对应选项 A。
>
