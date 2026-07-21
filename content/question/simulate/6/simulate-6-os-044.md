---
title: "模拟卷6 操作系统 第44题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "操作系统"
knowledge_points:
  - "缓冲区"
question_type: "comprehensive"
difficulty: 4
number: 44

---

（7 分）有三个进程 PA、PB 和 PC 合作解决文件打印问题：PA 将文件记录从磁盘读入主存的缓冲区 1，每执行一次读一个记录；PB 将缓冲区 1 的内容复制到缓冲区 2，每执行一次复制一个记录；PC 将缓冲区 2 的内容打印出来，每执行一次打印一个记录。缓冲区的大小等于一个记录的大小。请用 P、V 操作来保证文件的正确打印。

[缓冲区](/study_methods/tags/408quiz//#%e7%bc%93%e5%86%b2%e5%8c%ba)

[tag_link]

<p>**【解析】**
本题考查用 PV 操作解决进程的同步互斥问题。
<p>进程 PA、PB、PC 之间的关系为：PA 与 PB 共用一个单缓冲区，PB 又与 PC 共用一个单缓冲区，其合作方式如下图所示。当缓冲区 1 为空时，进程 PA 可将一个记录读入其中；若缓冲区 1 中有数据且缓冲区 2 为空，则进程 PB 可将记录从缓冲区 1 复制到缓冲区 2 中；若缓冲区 2 中有数据，则进程 PC 可以打印记录。在其他条件下，相应进程必须等待。事实上，这是一个生产者-消费者问题。
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1> [图片] </div><p>为遵循这一同步规则，应设置 4 个信号量 empty1、empty2、full1、full2，信号量 empty1 及 empty2 分别表示缓冲区 1 及缓冲区 2 是否为空，其初值为 1；信号量 full1 及 full2 分别表示缓冲区 1 及缓冲区 2 是否有记录可供处理，其初值为 0。相应的进程描述如下：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>empty1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>   <span style=color:#8f5902;font-style:italic>// 缓冲区 1 是否为空
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000>semaphore</span> <span style=color:#000>full1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>    <span style=color:#8f5902;font-style:italic>// 缓冲区 1 是否有记录可供处理
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000>semaphore</span> <span style=color:#000>empty2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>   <span style=color:#8f5902;font-style:italic>// 缓冲区 2 是否为空
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000>semaphore</span> <span style=color:#000>full2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>    <span style=color:#8f5902;font-style:italic>// 缓冲区 2 是否有记录可供处理
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>
</span></span><span style=display:flex><span><span style=color:#000>cobegin</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>PA</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>while</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>从磁盘读入一条记录</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>将记录存入缓冲区</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>PB</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>while</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>从缓冲区</span> <span style=color:#0000cf;font-weight:700>1</span> <span style=color:#a40000>中取出一条记录</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>将取出的记录存入缓冲区</span> <span style=color:#0000cf;font-weight:700>2</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>PC</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>while</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>从缓冲区</span> <span style=color:#0000cf;font-weight:700>2</span> <span style=color:#a40000>中取出一条记录</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>将取出的记录打印出来</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span> <span style=color:#000>coend</span>
</span></span>`</pre>
