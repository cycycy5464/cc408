---
title: "模拟卷5 操作系统 第44题"
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
number: 44
---

（12 分）现有 4 级流水线，分别完成取指、指令译码并取数、运算、回写四步操作。假设完成各部操作的时间依次为 100ns、100ns、80ns、50ns。请问：
（1）流水线的操作周期应设计为多少？
（2）若相邻两条指令如下，发生数据相关，而且在硬件上不采取措施，那么第 2 条指令要推迟多少时间进行？

（3）如果在硬件设计上加以改进，至少需要推迟多少时间？

[汇编代码](/study_methods/tags/408quiz//#%e6%b1%87%e7%bc%96%e4%bb%a3%e7%a0%81)

[tag_link]

<p>**【解析】**
(1) 流水线操作的时钟周期
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span></span></span></span>
应按四步操作中的最长时间来考虑，所以
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
。
<p>(2) 两条指令在流水线中执行情况如下表所示：
<table><thead><tr><th>指令</th><th>时钟 1</th><th>时钟 2</th><th>时钟 3</th><th>时钟 4</th><th>时钟 5</th><th>时钟 6</th><th>时钟 7</th></tr></thead><tbody><tr><td>ADD</td><td>取指</td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td><td></td><td></td></tr><tr><td>SUB</td><td></td><td>取指</td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td><td></td></tr></tbody></table><p>ADD 指令在时钟 4 时将结果写入寄存器堆 (R1)，但 SUB 指令在时钟 3 时读寄存器堆 (R1)。本来 ADD 指令应先写入 R1，SUB 指令后读 R1，结果变成 SUB 指令先读 R1，ADD 指令后写 R1，因而发生两条指令间数据相关。如果硬件上不采取措施，第 2 条指令 SUB 至少应推迟 2 个操作时钟周期（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
），即将 SUB 指令中的指令译码并取数阶段推迟到 ADD 指令的写回阶段之后才能保证不会出错。如下表所示：
<table><thead><tr><th>指令</th><th>时钟 1</th><th>时钟 2</th><th>时钟 3</th><th>时钟 4</th><th>时钟 5</th><th>时钟 6</th><th>时钟 7</th></tr></thead><tbody><tr><td>ADD</td><td>取指</td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td><td></td><td></td></tr><tr><td>SUB</td><td></td><td>取指</td><td></td><td></td><td>指令译码并取数</td><td>运算</td><td>写回</td></tr></tbody></table><p>(3) 如果硬件上加以改进，可只延迟 1 个操作时钟周期（100ns）。因为在 ADD 指令中，运算阶段就已经得到结果了，因此可以通过数据旁路技术在运算结果一得到的时候将结果快速送入寄存器 R1，而不需要等到写回阶段完成。流水线中执行情况如下图所示：
<table><thead><tr><th>时钟</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr></thead><tbody><tr><td>ADD</td><td>取指</td><td>指令译码并取数</td><td>运算（并采用数据旁路技术写入寄存器 R1）</td><td>写回</td><td></td><td></td><td>取指</td></tr><tr><td>SUB</td><td></td><td>取指</td><td></td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td></tr></tbody></table></div><h5 id=45>45</h5><p>（7 分）一个主修动物行为学、辅修计算机科学的学生参加了一个课题。调查花果山的猴子是否能被教会理解死锁。他找到一处峡谷，横跨峡谷拉了一根绳索（假设为南北方向），这样猴子就可以攀着绳索越过峡谷。只要它们朝着相同的方向，同
<p>一时刻可以有多只猴子通过。但是如果是相反的方向上同时有猴子通过则会发生死锁（这些猴子将被卡在绳索中间，假设这些猴子无法在绳索上从另一只猴子身上翻过去）。如果一只猴子想越过峡谷，它必须看当前是否有别的猴子在逆向通过。请用 P、V 操作来解决该问题。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-5 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-5")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-5",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
