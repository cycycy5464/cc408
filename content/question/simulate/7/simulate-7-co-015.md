---
title: "模拟卷7 组成原理 第15题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "组成原理"
knowledge_points:
  - "访存过程"
question_type: "choice"
difficulty: 3
number: 15

---

某存储系统中，主存容量是 Cache 容量的 4096 倍，Cache 被分为 64 块，当主存地址和 Cache 地址采用直接映射方式时，地址映射表的大小应为（ ）。（假设不考虑一致维护位）

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4097</span></span></span></span>
bit
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>64</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>12</span></span></span></span>
bit
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4096</span></span></span></span>
bit
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>64</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>13</span></span></span></span>
bit

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)

[tag_link]

正确答案：B
> <p> 本题考查 Cache 与主存的映射原理。
> 由于 Cache 被分为 64 块，那么 Cache 有 64 行，采用直接映射，一行相当于一组。
> 故而该标记阵列每行存储 1 个标记项，其中主存标记项为 12bit（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">12</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4096</span></span></span></span>
，是 Cache 容量的 4096 倍，那就是地址长度比 Cache 长 12 位），加上 1 位有效位，故而为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>64</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>13</span></span></span></span>
bit。
> <p>注意：主存—Cache 地址映射表（标记阵列）中内容：映射的 Cache 地址（直接映射不需要因为 Cache 地址唯一，组相联只需要组号）、主存标记（命中判断）、有效位。
> 如下图所示。
> <div class=img-container style=height:auto;width:60% oncontextmenu=return!1><img src=/images/408simulate/7_15_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>
