---
title: "模拟卷2 操作系统 第31题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "操作系统"
knowledge_points:
  - "文件概念"
  - "文件系统"
question_type: "choice"
difficulty: 3
number: 31

---

某文件系统物理结构采用三级索引分配方法，如果每个磁盘块的大小为 1024B，每个盘块索引号占用 4 字节，请问在该文件系统中，最大的文件长度约为（　）。

A\. 16GB
B\. 32GB
C\. 8GB
D\. 以上均不对

[文件概念](/study_methods/tags/408quiz//#%e6%96%87%e4%bb%b6%e6%a6%82%e5%bf%b5)
[文件系统](/study_methods/tags/408quiz//#%e6%96%87%e4%bb%b6%e7%b3%bb%e7%bb%9f)

[tag_link]

正确答案：A
> <p>
每个磁盘块大小为 1024 字节，每个盘块索引号占用 4 字节，因此一个索引块可以存储的索引号数量为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1024</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>256</span></span></span></span></span></div><p>个。
> <p>在三级索引分配方法中，文件通过三级间接索引访问数据块：
<ul><li>顶级索引块（三级间接块）存储 256 个指针，每个指向一个二级索引块；
> </li><li>每个二级索引块存储 256 个指针，每个指向一个一级索引块；
> </li><li>每个一级索引块存储 256 个指针，每个指向一个数据块。
> </li></ul><p>因此，总数据块数为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>256</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord>25</span><span class=mord><span class=mord>6</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">24</span></span></span></span></span></span></span></span></span></span></span></span></span></div><p>块。
> <p>每个数据块大小为 1024 字节（即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span></span></span></span></span></span></span></span>
字节），所以最大文件长度为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9474em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">24</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">34</span></span></span></span></span></span></span></span></span></span></span></span></span></div><p>字节。
> <p>由于

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>1</span><span class=mspace> </span><span class="mord text"><span class=mord>GB</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">30</span></span></span></span></span></span></span></span></span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">字节</span></span></span></span></span></span></div><p>因此文件长度为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9474em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">34</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">30</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">4</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>16</span><span class=mspace> </span><span class="mord text"><span class=mord>GB</span></span></span></span></span></span></div><p>故最大文件长度约为 16 GB，选项 A 正确。
>
