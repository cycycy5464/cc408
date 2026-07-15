---
title: "模拟卷3 计算机组成原理 第18题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "choice"
difficulty: 3
number: 18
---

一条双字长直接寻址的子程序调用 CALL 指令，其第一个字节是操作码和寻址特征，第二个字节是地址码 5000H。假设 PC 当前值为 1000H，SP 的内容为 0100H，栈顶内容为 1234H，存储器按字编址，而且进栈操作是先 (SP) ← (SP)，后存入数据。则 CALL 指令执行后，SP 及栈顶的内容分别为（ ）。

A\. 00FFH, 1000H
B\. 0101H, 1000H
C\. 00FEH, 1002H
D\. 00FFH, 1002H

[tag_link]

正确答案：D
> <p> 首先，`CALL` 指令为双字长直接寻址，且存储器按字编址，因此指令占用两个字：第一个字包含操作码和寻址特征，第二个字为地址码 `5000H`。
> 程序计数器当前值为 `1000H`，即指令起始地址，故指令占地址 `1000H` 和 `1001H`，下一条指令地址为 `1002H`，此即返回地址。
> <p>其次，执行 `CALL` 指令时需将返回地址压栈。
> 初始栈指针 `SP=0100H`，栈顶内容（地址 `0100H` 处）为 `1234H`。
> 进栈操作描述“先 `(SP) ← (SP)`，后存入数据”应理解为栈向下增长，压栈前 `SP` 先减 `1`（因按字编址，压入一个字占用一个地址单位），即

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.13889em>SP</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>←</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal" style=margin-right:.13889em>SP</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8778em;vertical-align:-.1944em></span><span class=mord>00</span><span class="mord mathnormal" style=margin-right:.13889em>FF</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mpunct>,</span></span></span></span></span></div><p>然后将返回地址 `1002H` 存入新 `SP` 指向的地址 `00FFH`。
> <p>因此，执行后 `SP=00FFH`，栈顶内容（地址 `00FFH` 处）`=1002H`。
> 选项 D 符合。
>
