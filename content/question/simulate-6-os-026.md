---
title: "模拟卷6 操作系统 第26题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "choice"
difficulty: 3
number: 26
---

设有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个进程共用一个相同的程序段，假设每次最多允许
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个进程（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
）同时进入临界区，则信号量
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
的初值为（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span><span class="mord mathnormal">m</span></span></span></span>

[tag_link]

正确答案：A
> 在操作系统中，信号量用于管理对共享资源的访问，其初值通常表示系统中可用资源的数量。
> 本题中，临界区允许最多
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个进程同时进入，因此初始时可用资源数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
。
> 信号量
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
的初值应设置为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
，这样当进程执行 P 操作（wait）时，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
减 1，若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
仍为非负则进程可进入临界区；
> 当进程执行 V 操作（signal）时，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
加 1，释放资源。
> 若初值设为其他选项，如
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
（进程总数）会导致超过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个进程同时进入，不符合限制；
> <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
或
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span><span class="mord mathnormal">m</span></span></span></span>
为负数，不符合资源数量的初始状态。
> 因此，正确初值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
。
>
