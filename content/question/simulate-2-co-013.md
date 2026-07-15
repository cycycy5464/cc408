---
title: "模拟卷2 组成原理 第13题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "组成原理"
knowledge_points:
  - "补码"
question_type: "choice"
difficulty: 3
number: 13

---

一个 8 位的二进制整数，若采用补码表示，且由 3 个“1”和 5 个“0”组成，则最小值为（　）。

A\. -127
B\. -32
C\. -125
D\. -3

[补码](/study_methods/tags/408quiz//#%e8%a1%a5%e7%a0%81)

[tag_link]

正确答案：C
> <p>
在 8 位补码表示中，最高位是符号位：0 表示正数，1 表示负数。
> 由于要求最小值，该数必为负数，因此符号位必须为 1。
> 已知该数由 3 个“1”和 5 个“0”组成，因此符号位占用一个“1”，剩余 7 位由 2 个“1”和 5 个“0”组成。
> <p>补码表示中，负数的值计算公式为：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>128</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord text"><span class=mord>(</span><span class="mord cjk_fallback">剩余</span><span class=mord> 7 </span><span class="mord cjk_fallback">位的无符号值</span><span class=mord>)</span></span></span></span></span></span></div><p>要使得数值最小，需要剩余 7 位的无符号值尽可能小。
> <p>剩余 7 位中，无符号值最小的情况是将两个“1”放在最低位（即第 0 位和第 1 位），此时剩余 7 位二进制为 `0000011`，对应的无符号值为 3。
> 因此整个 8 位二进制数为 `10000011`。
> <p>计算数值：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>128</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>125</span></span></span></span></span></div><p>即选项 C。
> <p>验证其他选项：
<ul><li>`-127` 的补码为 `10000001`，只有 2 个“1”，不符合条件；
> </li><li>`-32` 的补码为 `11100000`，虽符合 3 个“1”和 5 个“0”，但值为 `-32`，大于 `-125`；
> </li><li>`-3` 的补码为 `11111101`，有 7 个“1”，不符合条件。
> </li></ul><p>因此，最小值为 `-125`。
>
