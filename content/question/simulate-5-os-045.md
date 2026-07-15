---
title: "模拟卷5 操作系统 第45题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "comprehensive"
difficulty: 4
number: 45
---

（7 分）一个主修动物行为学、辅修计算机科学的学生参加了一个课题。调查花果山的猴子是否能被教会理解死锁。他找到一处峡谷，横跨峡谷拉了一根绳索（假设为南北方向），这样猴子就可以攀着绳索越过峡谷。只要它们朝着相同的方向，同

一时刻可以有多只猴子通过。但是如果是相反的方向上同时有猴子通过则会发生死锁（这些猴子将被卡在绳索中间，假设这些猴子无法在绳索上从另一只猴子身上翻过去）。如果一只猴子想越过峡谷，它必须看当前是否有别的猴子在逆向通过。请用 P、V 操作来解决该问题。

[tag_link]

<p>**【答案】**
信号量定义：
<ul><li>mutex：初值为 1，用于保护共享变量。</li><li>rope：初值为 1，用于控制绳索的访问。</li></ul><p>共享变量：
<ul><li>SN_count：从南向北的猴子数量，初值为 0。</li><li>NS_count：从北向南的猴子数量，初值为 0。</li></ul><pre tabindex=0>`semaphore mutex = 1;
semaphore rope = 1;
semaphore SN_count = 0;
semaphore NS_count = 0;
`</pre><p>从南向北的猴子执行以下操作：
<pre tabindex=0>`south_monkey() {
    P(mutex)
    SN_count++
    if (SN_count == 1) P(rope)
    V(mutex)

    // 通过绳索

    P(mutex)
    SN_count--
    if (SN_count == 0) V(rope)
    V(mutex)
}
`</pre><p>从北向南的猴子执行以下操作：
<pre tabindex=0>`north_monkey() {
    P(mutex)
    NS_count++
    if (NS_count == 1) P(rope)
    V(mutex)

    // 通过绳索

    P(mutex)
    NS_count--
    if (NS_count == 0) V(rope)
    V(mutex)
}
`</pre><p>**【解析】**
该问题本质上是单车道桥梁同步问题的变体，需要防止两个方向的猴子同时使用绳索导致死锁，同时允许同一方向的多只猴子共享绳索。使用 P、V 操作（信号量）来实现同步。
<p>首先，定义信号量 mutex 用于互斥访问共享变量 SN_count 和 NS_count，确保计数操作原子性。信号量 rope 用于控制绳索的访问权限，初值为 1 表示绳索空闲。
<p>对于从南向北的猴子：当第一只猴子到达时，在 mutex 保护下增加 SN_count，由于 SN_count 从 0 变为 1，它执行 P(rope) 获取绳索访问权，阻止北向南的猴子进入。之后释放 mutex，允许其他南向北猴子进入，它们增加 SN_count 但不会再次 P(rope)，因此同一方向多只猴子可以同时通过绳索。当猴子通过后，在 mutex 保护下减少 SN_count，如果 SN_count 变为 0，表示该方向没有猴子了，则执行 V(rope) 释放绳索访问权，允许另一方向猴子使用。
<p>对于从北向南的猴子，操作对称：第一只猴子获取 rope，后续猴子共享访问，最后一只猴子释放 rope。
<p>这种设计确保：只要有一个方向的猴子在使用绳索，rope 信号量就被持有，另一方向的猴子会在执行 P(rope) 时阻塞，直到当前方向所有猴子离开并释放 rope。因此，相反方向的猴子不会同时通过，避免了死锁。同一方向的猴子可以共享绳索，符合问题要求。整个过程通过 P、V 操作实现了同步，且不会产生饥饿，除非一个方向持续有猴子到达，但问题未要求公平性，故解法可行。
</div><h5 id=46>46</h5><p>（8 分）在某段式存储管理系统中，逻辑地址为 32 位，其中高 16 位为段号，低 16 位为段内偏移量，以下是段表（其中的地址均为 16 进制）：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:10.84em;vertical-align:-5.15em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.69em><span style=top:-7.65em><span class=pstrut style=height:7.65em></span><span class=mtable><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">段</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>3</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5</span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>6</span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>7</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">基地址</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>10000</span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11900</span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11</span><span class="mord mathnormal" style=margin-right:.02778em>D</span><span class=mord>00</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11</span><span class="mord mathnormal" style=margin-right:.13889em>F</span><span class=mord>00</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>13000</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">长度</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>18</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>0</span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>3</span><span class="mord mathnormal" style=margin-right:.13889em>FF</span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span><span class="mord mathnormal" style=margin-right:.13889em>FF</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1000</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>FFF</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">保护</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">只读</span></span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">只读</span></span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">读</span><span class=mord>/</span><span class="mord cjk_fallback">写</span></span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">禁止访问</span></span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">读</span><span class=mord>/</span><span class="mord cjk_fallback">写</span></span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">禁止访问</span></span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">禁止访问</span></span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">读</span><span class=mord>/</span><span class="mord cjk_fallback">写</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:7.65em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-12.1em><span class=pstrut style=height:7.65em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-13.3em><span class=pstrut style=height:7.65em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span></span></span></span></span></div><p>以下是代码段的内容（代码前的数字表示存放代码的十六进制逻辑地址）：
<pre tabindex=0>`main
240  push x[10108H]
244  call sin
248  ...

sin
360  mov r2,4+(sp)
364  ...
368  ret
`</pre><p>试问：
<p>（1）x 的逻辑地址为 10108H，它的物理地址是多少？要求给出具体的计算过程。
（2）若栈指针 SP 的当前值为 70FF0H，push x 指令的执行过程：先将 SP 减 4，然后存储 x 的值。试问存储 x 的物理地址是多少？
（3）call sin 指令的执行过程：先将当前 PC 值入栈，然后在 PC 内装入目标 PC 值。请问：哪个值被压入栈了？新的 SP 指针的值是多少？新的 PC 值是多少？
（4）“mov r2,4+(SP)”的功能是什么？（假设指令集与 x86 系列 CPU 相同）
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
