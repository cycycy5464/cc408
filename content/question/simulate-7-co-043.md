---
title: "模拟卷7 计算机组成原理 第43题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "comprehensive"
difficulty: 4
number: 43
---

（10 分）设某计算机有变址寻址、间接寻址和相对寻址方式，一个指令长等于一个存储字。设当前指令的地址码部分为 `001AH`，正在执行的指令所在地址为 `1F05H`，变址寄存器中的内容为 `23A0H`。已知存储器的部分地址及相应内容如下表所示：

（1）当执行取数指令时，如为变址寻址方式，取出的数为多少？
（2）如为间接寻址，取出的数为多少？
（3）设计算机每取一个存储字 PC 自动加 1，转移指令采用相对寻址，当执行转移指令时，转移地址为多少？若希望转移到 `23A0H`，则指令的地址码部分应设为多少？

[tag_link]

<p>**【解析】**
本题考查指令的寻址方式。前两小题涉及数据寻址，其最终目的是寻址操作数，第 3 小题涉及指令寻址，其目的是寻址下一条将要执行的指令地址。下表列出了基本的寻址方式，其中偏移寻址包括变址寻址、基址寻址和相对寻址三种方式。
<table><thead><tr><th>寻址方式</th><th>规则</th><th>主要优点</th><th>主要缺点</th></tr></thead><tbody><tr><td>立即寻址</td><td>操作数=A</td><td>无需访问存储器</td><td>操作数范围受限</td></tr><tr><td>寄存器寻址</td><td>EA=R</td><td>无需访问存储器</td><td>寻址空间受限</td></tr><tr><td>直接寻址</td><td>EA=A</td><td>简单</td><td>寻址空间受限</td></tr><tr><td>间接寻址</td><td>EA=(A)</td><td>寻址空间大</td><td>多次访问主存</td></tr><tr><td>寄存器间接寻址</td><td>EA=(R)</td><td>寻址空间大</td><td>多访问一次主存</td></tr><tr><td>偏移寻址</td><td>EA=(R)+A</td><td>灵活</td><td>复杂</td></tr></tbody></table><p>特别注意相对寻址方式中的 PC 值更新的问题：根据历年统考真题，通常在取出当前指令后立即将 PC 的内容加 1（或加增量），使之变成下条指令的地址。
<p>(1) 变址寻址时，操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>((</span><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class="mord mathnormal">x</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">A</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>23</span><span class="mord mathnormal">A</span><span class=mord>0</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>001</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>23</span><span class="mord mathnormal" style=margin-right:.05017em>B</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>1748</span><span class="mord mathnormal" style=margin-right:.08125em>H</span></span></span></span>
。
<p>(2) 间接寻址时，操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>((</span><span class="mord mathnormal">A</span><span class=mclose>))</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>((</span><span class=mord>001</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>))</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>23</span><span class="mord mathnormal">A</span><span class=mord>0</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>2600</span><span class="mord mathnormal" style=margin-right:.08125em>H</span></span></span></span>
。
<p>(3) 转移指令使用相对寻址，因为指令字长等于存储字长，PC 每取出一条指令后自动加 1，因此转移地址 = (PC) + 1 + A = 1F05H + 1 + 001AH = 1F20H。若希望转移到 23A0H，则指令的地址码部分应为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>23</span><span class="mord mathnormal">A</span><span class=mord>0</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.07153em>PC</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>23</span><span class="mord mathnormal">A</span><span class=mord>0</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>1</span><span class="mord mathnormal" style=margin-right:.13889em>F</span><span class=mord>05</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>049</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.08125em>H</span></span></span></span>
。
</div><h5 id=44>44</h5><p>（11 分）设有一个 CPU 的指令执行部件如下图所示，由 Cache 每隔 100ns 提供 1 条指令。（注：B1、B2 和 B3 是三个相同的并行部件）
<div class=img-container style=height:auto;width:60% oncontextmenu=return!1> [图片] </div><p>（1）画出该指令流水线功能段的时空图。
（2）试计算流水线执行这 4 条指令的实际吞吐率和效率。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-b21e56584c27aaf174732231badd601f-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/7/ data-page-title="模拟卷 7"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-b21e56584c27aaf174732231badd601f-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-b21e56584c27aaf174732231badd601f-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
