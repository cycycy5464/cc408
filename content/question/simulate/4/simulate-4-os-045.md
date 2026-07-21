---
title: "模拟卷4 操作系统 第45题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "操作系统"
knowledge_points:
  - "信号量"
question_type: "comprehensive"
difficulty: 4
number: 45

---

（8 分）在一间酒吧里有 3 个音乐爱好者队列，第 1 队的音乐爱好者只有随身听，第 2 队只有音乐磁带，第 3 队只有电池。而要听音乐就必须随身听、音乐磁带和电池这 3 种物品俱全。酒吧老板一次出售这 3 种物品中的任意两种。当一名音乐爱好者得到这 3 种物品并听完一首乐曲后，酒吧老板才能再一次出售这 3 种物品中的任意两种。于是第 2 名音乐爱好者得到这 3 种物品，并开始听乐曲。全部买卖就这样进行下去。试用 P、V 操作正确解决这一买卖。

[信号量](/study_methods/tags/408quiz//#%e4%bf%a1%e5%8f%b7%e9%87%8f)

[tag_link]

<p>本题考查用 PV 操作解决进程的同步互斥问题。
<p>第 1 队音乐爱好者要竞争“待出售的音乐磁带和电池”，而且在初始状态下，系统并无“待出售的音乐磁带和电池”，故可为该种资源设置一初值为 0 的信号量 `buy1`；同样，需设置初值为 0 的 `buy2`、`buy3` 分别对应“待出售的随身听和电池”、“待出售的随身听和音乐磁带”。另外，为了同步买者的付费动作和卖者的给货动作，还需设置信号量 `payment` 和 `goods`，以保证买者在付费后才能得到所需商品。信号量 `music_over` 用来同步音乐爱好者听乐曲和酒吧老师的下一次出售行为。具体的算法描述如下：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>buy1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>buy2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>buy3</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>payment</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>goods</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>music_over</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#000>cobegin</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>boss</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 酒吧老板
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>拿出任意两种物品出售；</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#a40000>出售的是音乐磁带和电池</span><span style=color:#000;font-weight:700>)</span>   <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#a40000>出售的是随身听和电池</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#a40000>出售的是随身听和音乐磁带</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy3</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                  <span style=color:#8f5902;font-style:italic>// 等待付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 给货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>               <span style=color:#8f5902;font-style:italic>// 等待乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>fan1</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 第1队音乐爱好者
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>                  <span style=color:#8f5902;font-style:italic>// 因为一个进程代表一队，而不是一个爱好者，
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>                                        <span style=color:#8f5902;font-style:italic>// 所以这里是 while(true)，下同
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy1</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 等有音乐磁带和电池出售
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                 <span style=color:#8f5902;font-style:italic>// 付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                   <span style=color:#8f5902;font-style:italic>// 取货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#a40000>欣赏一曲乐曲；</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>              <span style=color:#8f5902;font-style:italic>// 通知老板乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>fan2</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 第2队音乐爱好者
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy2</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 等有随身听和电池出售
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                 <span style=color:#8f5902;font-style:italic>// 付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                   <span style=color:#8f5902;font-style:italic>// 取货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#a40000>欣赏一曲乐曲；</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>              <span style=color:#8f5902;font-style:italic>// 通知老板乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>fan3</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 第3队音乐爱好者
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy3</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 等有随身听和音乐磁带出售
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                 <span style=color:#8f5902;font-style:italic>// 付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                   <span style=color:#8f5902;font-style:italic>// 取货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#a40000>欣赏一曲乐曲；</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>              <span style=color:#8f5902;font-style:italic>// 通知老板乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000>coend</span>
</span></span>`</pre>
