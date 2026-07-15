---
title: "模拟卷1 组成原理 第12题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "组成原理"
knowledge_points:
  - "计算机性能指标"
question_type: "choice"
difficulty: 3
number: 12

---

某工作站采用时钟频率 f 为 15MHz、处理速率为 10MIPS 的处理机来执行一个已知混合程序。假定该混合型程序平均每条指令需要 1 次访存，且每次存取存储器存取为 1 周期延迟，试问此计算机的有效 CPI 是（ ）。

A\. 2.5
B\. 2
C\. 1.5
D\. 1

[计算机性能指标](/study_methods/tags/408quiz//#%e8%ae%a1%e7%ae%97%e6%9c%ba%e6%80%a7%e8%83%bd%e6%8c%87%e6%a0%87)

[tag_link]

正确答案：C
> <p> 有效 CPI（每条指令的时钟周期数）可以根据处理速率（MIPS）和时钟频率（f）的关系计算。
> 公式为：MIPS = f（MHz）/ CPI。
> 给定 f = 15 MHz，处理速率为 10 MIPS，代入公式得 CPI = 15 / 10 = 1.5。
> <p>问题中提到的访存信息（平均每条指令 1 次访存，每次访存 1 周期延迟）是背景条件，但处理速率 10 MIPS 是实际测量值，已经包含了所有延迟效果，因此直接使用公式计算出的 CPI 即为有效 CPI，无需额外调整。
> 计算结果显示 CPI 为 1.5，对应选项 C。
>
