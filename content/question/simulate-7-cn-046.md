---
title: "模拟卷7 计算机网络 第46题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "comprehensive"
difficulty: 4
number: 46
---

（7 分）设一个没有设置快表的虚拟页式存储系统，页面大小为 100 字节。一个仅有 460 个字节的程序有下述内存访问序列（下标从 0 开始）：
10、11、104、170、73、309、185、245、246、434、458、364。
为该程序分配有 2 个可用页帧（Page frame）。试问：

（1）试叙述缺页中断与一般中断的主要区别？
（2）若分别采用 FIFO 和 LRU 算法，试计算访问过程中发生多少次缺页中断？
（3）若一次访存的时间是 10ms，平均缺页中断处理时间为 25ms，为使该虚拟存储系统的平均有效访问时间不大于 22ms，则可接受的最大缺页中断率是多少？

[tag_link]

<p>**【解析】**
本题考查缺页中断和页面置换算法。
<p>（1）缺页中断是一种特殊的中断，它与一般中断的区别是：
① 在指令执行期间产生和处理中断信号。CPU 通常在一条指令执行完后检查是否有中断请求，而缺页中断是在指令执行时间，发现所要访问的指令或数据不在内存时产生和处理的；
② 一条指令在执行期间可能产生多次缺页中断。如一条读取数据的多字节指令，指令本身跨越两个页面，若指令后一部分所在页面和数据所在页面均不在内存，则该指令的执行至少产生两次缺页中断。
<p>（2）每个页面大小为 100 字节，则页面的访问顺序如下：
<table><thead><tr><th>10</th><th>11</th><th>104</th><th>170</th><th>73</th><th>309</th><th>185</th><th>245</th><th>246</th><th>434</th><th>458</th><th>364</th></tr></thead><tbody><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>3</td><td>1</td><td>2</td><td>2</td><td>4</td><td>4</td><td>3</td></tr></tbody></table><p>采用 FIFO 算法的页面置换情况如下表，共产生缺页中断 6 次。
<table><thead><tr><th>走向</th><th>0</th><th>0</th><th>1</th><th>1</th><th>0</th><th>3</th><th>1</th><th>2</th><th>2</th><th>4</th><th>4</th><th>3</th></tr></thead><tbody><tr><td>块号 1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>3</td><td>3</td><td>2</td><td>2</td><td>4</td><td>4</td><td>3</td></tr><tr><td>块号 2</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>3</td><td>3</td><td>2</td><td>2</td><td>4</td></tr><tr><td>淘汰</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td></td><td>1</td><td></td><td>3</td><td></td><td>2</td></tr><tr><td>缺页</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td><td></td><td>√</td><td></td><td>√</td></tr></tbody></table><p>采用 LRU 算法的页面置换情况如下表，共产生缺页中断 7 次。
<table><thead><tr><th>走向</th><th>0</th><th>0</th><th>1</th><th>1</th><th>0</th><th>3</th><th>1</th><th>2</th><th>2</th><th>4</th><th>4</th><th>3</th></tr></thead><tbody><tr><td>块号 1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>3</td><td>1</td><td>2</td><td>2</td><td>4</td><td>4</td><td>3</td></tr><tr><td>块号 2</td><td></td><td></td><td>0</td><td>0</td><td>1</td><td>0</td><td>3</td><td>1</td><td>1</td><td>2</td><td>2</td><td>4</td></tr><tr><td>淘汰</td><td></td><td></td><td></td><td></td><td>1</td><td>0</td><td>3</td><td>1</td><td></td><td>1</td><td></td><td>2</td></tr><tr><td>缺页</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td></tr></tbody></table><p>（3）设可接受的最大缺页中断率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span></span></span></span>
。若要访问页面在内存中，一次访问的时间是 10ms（访问内存页表）+ 10ms（访问内存）= 20ms。如果不在内存，所花时间为 10ms（访问内存页表）+ 25ms（中断处理）+ 10ms（访问内存页表）+ 10ms（访问内存）= 55ms。
<p>平均有效访问时间：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>20</span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">p</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>55</span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8304em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>22</span><span class="mord text"><span class=mord>ms</span></span></span></span></span></span></div><p>解得可接受的最大缺页中断率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span></span></span></span>
为 5.7%。
</div><h5 id=47>47</h5><p>（9 分）设有 4 台主机 A、B、C 和 D 都处在同一物理网络中，它们的 IP 地址分别为：
<ul><li>A: 192.155.28.112</li><li>B: 192.155.28.120</li><li>C: 192.155.28.135</li><li>D: 192.155.28.202</li></ul><p>子网掩码都是 255.255.255.224。请回答：
<p>（1）该网络的 4 台主机中哪些可以直接通信？哪些需要通过设置路由器才能通信？请画出网络连接示意图，并注明各个主机的子网地址和主机地址。
（2）如要加入第 5 台主机 E，使它能与主机 D 直接通信，其 IP 地址的范围是多少？
（3）若不改变主机 A 的物理位置，而将其 IP 改为 192.155.28.168，则它的直接广播地址和本地广播地址各是多少？若使用本地广播地址发送信息，请问哪些主机能够收到？
（4）若要使该网络中的 4 台主机都能够直接通信，可采取什么办法？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-b21e56584c27aaf174732231badd601f-7 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/7/ data-page-title="模拟卷 7"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-b21e56584c27aaf174732231badd601f-7")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-b21e56584c27aaf174732231badd601f-7",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
