---
title: "中央处理器 第5题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "数据通路的功能和基本结构"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 48
tags: ['课后题']
---

某机主要功能部件如下图所示，其中 M 为主存，MDR 为存储器数据寄存器，MAR 为 存储器地址寄存器，IR 为指令寄存器， PC 为程序计数器(并假设当前指令地址在 PC
中 ) ,RO～R3为通用寄存器，C 、D 为暂存器。
移位器                                    RO
ALU                                   PC
R2
D                                           R3
MDR
MAR
1)请补充各部件之间的主要连接线(总线自己画),并注明数据流动方向。
2)画出“ADD(R1),(R2)+”    指令周期流程图，该指令的含义是进行求和运算，源操作 数地址在R1 中，目的操作数寻址方式为自增型寄存器间接寻址方式(先取地址后加
1),并将相加结果写回R2 寄存器。

[tag_link]

【解答】