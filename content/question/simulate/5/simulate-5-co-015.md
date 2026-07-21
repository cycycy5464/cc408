---
title: "模拟卷5 组成原理 第15题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "组成原理"
knowledge_points:
  - "访存过程"
question_type: "choice"
difficulty: 3
number: 15

---

设有一主存-Cache 层次的存储器，其主存容量 1MB，Cache 容量 16KB，每字块有 8 个字，每字 32 位，采用直接地址映像方式，若主存地址为 35301H，且 CPU 访问 Cache 命中，则该主存块在 Cache 的第（ ）字块中（Cache 起始字块为第 0 字块）。

A\. 152
B\. 153
C\. 154
D\. 151

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)

[tag_link]

正确答案：A
> <p>
主存容量为 1MB，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">20</span></span></span></span></span></span></span></span></span></span></span></span>
字节，因此主存地址为 20 位。
> Cache 容量为 16KB，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">14</span></span></span></span></span></span></span></span></span></span></span></span>
字节。
> 每个字为 32 位（即 4 字节），每个字块包含 8 个字，因此块大小为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>32</span></span></span></span>
字节，块内偏移需要
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9386em;vertical-align:-.2441em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mord>32</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
位。
> Cache 共有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">14</span></span></span></span></span></span></span></span></span><span class=mord>/32</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>512</span></span></span></span>
块，索引需要
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9386em;vertical-align:-.2441em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mord>512</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span></span></span></span>
位。
> 在直接映射方式下，主存地址划分为：标签（高 6 位）、索引（中间 9 位）、偏移（低 5 位）。
> <p>给定主存地址 35301H，转换为二进制为 0011 0101 0011 0000 0001（共 20 位）。
> 偏移量为低 5 位（00001），索引为位 5 至位 13（010011000），转换为十进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>128</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>16</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>152</span></span></span></span>
。
> 也可通过计算主存块号得到：地址 35301H 对应十进制 217857 字节，块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>217857</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>32</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>6808</span></span></span></span>
（余数为 1），Cache 块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>6808</span><span class="mspace allowbreak"></span><span class=mspace style=margin-right:.6667em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mspace style=margin-right:.1667em></span><span class=mord>512</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>152</span></span></span></span>
。
> 因此，该主存块位于 Cache 的第 152 字块中。
>
