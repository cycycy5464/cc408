---
title: "模拟卷7 操作系统 第45题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "comprehensive"
difficulty: 4
number: 45
---

（7 分）兄弟俩共同使用一个账号，每次限存或取 10 元，存钱与取钱的进程分别如下所示：

由于兄弟俩可能同时存钱和取钱，因此这两个进程是并发的。若哥哥先存了两次钱，但在第三次存钱时，弟弟在取钱。请问：

（1）最后账号 `amount` 上面可能出现的值？
（2）如何用 P、V 操作实现两并发进程的互斥执行？

[tag_link]

<p>**【答案】**
（1）最后账号 `amount` 可能出现的值为 10、20 或 30。
（2）使用 P、V 操作实现互斥：定义一个信号量 `mutex` 并初始化为 1。在存钱进程 `SAVE()` 和取钱进程 `TAKE()` 中，在访问共享变量 `amount` 的代码段前后分别执行 `P(mutex)` 和 `V(mutex)`，确保同一时刻只有一个进程进入临界区。
<p>**【解析】**
假设存钱进程 `SAVE()` 和取钱进程 `TAKE()` 的正确逻辑为：
<ul><li>`SAVE()`：读取 `amount` 到局部变量，加 10，再写回 `amount`。</li><li>`TAKE()`：读取 `amount` 到局部变量，减 10，再写回 `amount`。
哥哥先存了两次钱，`amount` 从 0 增加到 20。第三次存钱时，弟弟同时取钱，两个进程并发执行，由于没有互斥保护，它们的操作可能交错执行，导致竞态条件。</li></ul><p>考虑第三次存钱和取钱的交错情况：
<ul><li>若存钱先完整执行，再取钱执行：存钱后 `amount=30`，取钱后 `amount=20`，最终为 20。</li><li>若取钱先完整执行，再存钱执行：取钱后 `amount=10`，存钱后 `amount=20`，最终为 20。</li><li>若操作交错：例如存钱读取 20 后，取钱也读取 20，然后存钱写入 30，取钱写入 10，最终为 10；或类似交错导致存钱写入覆盖取钱结果，最终为 30。
因此，`amount` 可能为 10、20 或 30。</li></ul><p>为实现互斥，引入信号量 `mutex` 并初始化为 1。在 `SAVE()` 和 `TAKE()` 中，将访问 `amount` 的代码段作为临界区，在进入前执行 `P(mutex)`（申请资源），退出后执行 `V(mutex)`（释放资源）。这样，任何时刻只有一个进程能执行临界区代码，避免数据不一致。修改后的代码示例如下：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>mutex</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#000>SAVE</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>mutex</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>m1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>amount</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>m1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>m1</span> <span style=color:#ce5c00;font-weight:700>+</span> <span style=color:#0000cf;font-weight:700>10</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>amount</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>m1</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>mutex</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#000>TAKE</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>mutex</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>m2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>amount</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>m2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>m2</span> <span style=color:#ce5c00;font-weight:700>-</span> <span style=color:#0000cf;font-weight:700>10</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>amount</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>m2</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>mutex</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>通过 P、V 操作确保进程互斥执行，保证 `amount` 操作的原子性。
</div><h5 id=46>46</h5><p>（7 分）设一个没有设置快表的虚拟页式存储系统，页面大小为 100 字节。一个仅有 460 个字节的程序有下述内存访问序列（下标从 0 开始）：
10、11、104、170、73、309、185、245、246、434、458、364。
为该程序分配有 2 个可用页帧（Page frame）。试问：
<p>（1）试叙述缺页中断与一般中断的主要区别？
（2）若分别采用 FIFO 和 LRU 算法，试计算访问过程中发生多少次缺页中断？
（3）若一次访存的时间是 10ms，平均缺页中断处理时间为 25ms，为使该虚拟存储系统的平均有效访问时间不大于 22ms，则可接受的最大缺页中断率是多少？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-b21e56584c27aaf174732231badd601f-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/7/ data-page-title="模拟卷 7"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-b21e56584c27aaf174732231badd601f-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-b21e56584c27aaf174732231badd601f-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
