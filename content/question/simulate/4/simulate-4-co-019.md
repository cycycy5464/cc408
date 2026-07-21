---
title: "模拟卷4 组成原理 第19题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "组成原理"
knowledge_points:
  - "计算机性能指标"
question_type: "choice"
difficulty: 3
number: 19

---

流水 CPU 是由一系列叫做“段”的处理部件组成的。当流水稳定后，相比具备
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个并行部件的 CPU 相比，一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
段流水 CPU（ ）。

A\. 具备同等水平的吞吐能力
B\. 不具备同等能力的吞吐能力
C\. 吞吐能力小于前者的吞吐能力
D\. 吞吐能力大于后者的吞吐能力

[计算机性能指标](/study_methods/tags/408quiz//#%e8%ae%a1%e7%ae%97%e6%9c%ba%e6%80%a7%e8%83%bd%e6%8c%87%e6%a0%87)

[tag_link]

正确答案：C
> 对于一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
段流水 CPU，在流水稳定后，理想情况下每个时钟周期可以完成一条指令，因此吞吐能力为每时钟周期一条指令。
> 而对于具备
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个并行部件的 CPU，每个部件可以独立执行指令，每个时钟周期可以同时完成
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
条指令，因此吞吐能力为每时钟周期
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
条指令。
> 假设时钟周期相同，前者的吞吐能力明显小于后者。
> 因此，一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
段流水 CPU 的吞吐能力小于具备
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个并行部件的 CPU 的吞吐能力，对应选项 C。
>
