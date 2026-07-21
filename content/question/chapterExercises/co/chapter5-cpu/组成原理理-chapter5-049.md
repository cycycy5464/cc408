---
title: "中央处理器 第6题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "组成原理"
knowledge_points:
  - "数据通路的功能和基本结构"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 49
tags: ['课后题']
---

已知单总线计算机结构如下图所示，其中M 为主存，XR 为变址寄存器，EAR 为有效地 址寄存器，LATCH 为暂存器。假设指令地址已存在于PC中，请给出ADDX,D   指令周 期信息流程和相应的控制信号。说明：
1) ADD   X,D指令字中，X 为变址寄存器 XR,D    为形式地址，指令的功能是将变址寻 址得到的操作数和ACC 中的操作数相加，结果送回ACC。
2)寄存器的输入/输出均采用控制信号控制，如 PCi 表示 PC  的输入控制信号，MDR。 表示MDR 的输出控制信号。
3)凡需要经过总线的传送，都需要注明，如(PC)→MAR, 相应的控制信号为PC₀和 MAR
ACC           MOALU加 法 器LATCHXR     MARMDR地 址WREARPCIRXM
ACC           MO
ALU
加 法 器
LATCH
XR     MAR
MDR
地 址
WR
EAR
PC
IR
X
M

[tag_link]

B