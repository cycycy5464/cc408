---
title: "模拟卷5 组成原理 第43题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "组成原理"
knowledge_points:
  - "寄存器类型"
  - "补码"
question_type: "comprehensive"
difficulty: 4
number: 43

---

（11 分）已知两个实数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>8.25</span></span></span></span>
，它们在 C 语言中定义为 float 型变量，分别存放在寄存器 A 和 B 中。另外，还有两个寄存器 C 和 D。A、B、C、D 都是 32 位的寄存器。请问下列问题（要求用十六进制表示二进制序列）：
（1）寄存器 A 和 B 中的内容分别是什么？
（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相加后的结果存放在 C 寄存器中，寄存器 C 中的内容是什么？
（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相减后的结果存放在 D 寄存器中，寄存器 D 中的内容是什么？

[寄存器类型](/study_methods/tags/408quiz//#%e5%af%84%e5%ad%98%e5%99%a8%e7%b1%bb%e5%9e%8b)
[补码](/study_methods/tags/408quiz//#%e8%a1%a5%e7%a0%81)

[tag_link]

<p>**【答案】**
（1）寄存器 A 中的内容为 0xC2880000，寄存器 B 中的内容为 0xC1040000。
（2）寄存器 C 中的内容为 0xC2988000。
（3）寄存器 D 中的内容为 0xC26F0000。
<p>**【解析】**
对于浮点数采用 IEEE 754 单精度格式（32 位），其中包含 1 位符号位、8 位指数位（偏移量 127）和 23 位尾数位。
<p>**（1）对于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>68</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1000100</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.000100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>133</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000101</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为隐藏最高位 1 后的小数部分
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>000100</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00010000000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000010100010000000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>2880000</span></span></span></span>
。</li></ul><p>**对于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>8.25</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>8.25</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1000.01</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.00001</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>130</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000010</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00001</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00001000000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000001000001000000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>1040000</span></span></span></span>
。</li></ul><p>**（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>68</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>8.25</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>76.25</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>76.25</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1001100.01</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.00110001</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>133</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000101</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00110001</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00110001000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000010100110001000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>2988000</span></span></span></span>
。</li></ul><p>**（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>68</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>8.25</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>59.75</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>59.75</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>111011.11</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.1101111</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">5</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>5</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>132</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000100</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1101111</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11011110000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000010011011110000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>26</span><span class="mord mathnormal" style=margin-right:.13889em>F</span><span class=mord>0000</span></span></span></span>
。</li></ul></div><h5 id=44>44</h5><p>（12 分）现有 4 级流水线，分别完成取指、指令译码并取数、运算、回写四步操作。假设完成各部操作的时间依次为 100ns、100ns、80ns、50ns。请问：
（1）流水线的操作周期应设计为多少？
（2）若相邻两条指令如下，发生数据相关，而且在硬件上不采取措施，那么第 2 条指令要推迟多少时间进行？
<pre tabindex=0><code class=language-assembly data-lang=assembly>ADD R1, R2, R3     # R2 + R3 -> R1
SUB R4, R1, R5     # R1 - R5 -> R4
`</pre><p>（3）如果在硬件设计上加以改进，至少需要推迟多少时间？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
