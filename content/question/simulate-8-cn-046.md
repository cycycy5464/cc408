---
title: "模拟卷8 计算机网络 第46题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 8
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "comprehensive"
difficulty: 4
number: 46
---

（8 分）一个文件系统中有一个 20MB 大文件和一个 20KB 小文件，当分别采用连续分配、隐式链接分配方案时，每块大小为 4096B，每块地址用 4B 表示，问：

(1) 该文件系统所能管理的最大文件是多少？

(2) 每种方案对大、小两文件各需要多少专用块来记录文件的物理地址（说明各块的用途）？

(3) 如需要读大文件前面第 5.5KB 的信息和后面第 (16M+5.5KB) 的信息，则每个方案各需要多少次磁盘 I/O 操作？

[tag_link]

<p>**【解析】**
本题考查文件物理结构的分配方案：连续分配、链接分配和索引分配。
<p>（1）**连续分配**：文件大小理论上不受限制，可大到整个磁盘文件区。
**链接分配**：由于块地址占 4 字节（32 位），能表示的最大块数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">32</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>4</span><span class="mord text"><span class=mord>G</span></span></span></span></span>
，每个盘块存放文件内容的大小为 4092 字节，因此链接分配可管理的最大文件为：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>4</span><span class="mord text"><span class=mord>G</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>4092</span><span class="mord text"><span class=mord>B</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>16368</span><span class="mord text"><span class=mord>GB</span></span></span></span></span>
。
<p>注意：有同学认为最后一块可以不存放指针而使用全部 4096 字节，但一般文件系统的块结构是固定的，为了多出 4 字节的空间会增加很多额外开销，因此通常不会这样做。
<p>（2）**连续分配**：对大小文件都只需在文件控制块 FCB 中设置两项，一是首块物理块号，另一是文件总块数，不需要专用块记录文件的物理地址。
**链接分配**：对大小文件也只需在 FCB 中设置两项，一是首块物理块号，另一是文件最后一个物理块号；同时在每个物理块中设置存放下一个块号的指针。
<p>（3）**连续分配**：读取大文件前面或后面的信息时，需先计算信息在文件中的相对块号。
前面信息的相对逻辑块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>5.5</span><span class="mord text"><span class=mord>K</span></span><span class=mord>/4</span><span class="mord text"><span class=mord>K</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（从 0 开始编号），
后面信息的相对逻辑块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>16</span><span class="mord text"><span class=mord>M</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>5.5</span><span class="mord text"><span class=mord>K</span></span><span class=mclose>)</span><span class=mord>/4</span><span class="mord text"><span class=mord>K</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4097</span></span></span></span>
。
物理块号 = 文件首块号 + 相对逻辑块号，每块只需一次磁盘 I/O 操作即可读出。
<p>**链接分配**：读取大文件前面 5.5KB 的信息时，先读一次文件头块得到信息所在块的块号，再读一次第 1 号逻辑块得到所需信息，共需 2 次读盘。
读取大文件
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>16</span><span class="mord text"><span class=mord>MB</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>5.5</span><span class="mord text"><span class=mord>KB</span></span></span></span></span>
处的信息时，逻辑块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>16</span><span class="mord text"><span class=mord>M</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>5.5</span><span class="mord text"><span class=mord>K</span></span><span class=mclose>)</span><span class=mord>/4092</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4101</span></span></span></span>
，需要先顺序读出该块之前的所有块，共花费 4101 次磁盘 I/O 操作得到目标块的块号，最后再花一次 I/O 操作读出该块信息。因此总共需要 4102 次 I/O 操作。
</div><h5 id=47>47</h5><p>（9 分）设 A、B 两站相距 4km，使用 CSMA/CD 协议，信号在网络上的传播速度为 200000km/s，两站发送速率为 100Mbps，A 站先发送数据，如果发生碰撞，则：
<p>(1) 最先发送数据的 A 站最晚经过多长时间才检测到发生了碰撞？最快又是多少？
<p>(2) 检测到碰撞后，A 站已发送数据长度的范围是多少（设 A 要发送的帧足够长）？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-940de506bfc79619fca63900cf0f0338-7 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/8/ data-page-title="模拟卷 8"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-940de506bfc79619fca63900cf0f0338-7")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-940de506bfc79619fca63900cf0f0338-7",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
