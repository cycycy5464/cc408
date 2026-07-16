---
title: "中央处理器 第1题"
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
number: 46
tags: ['课后题']
---

某计算机的数据通路结构如下图所示，写出实现 ADD  R1,(R2)的微操作序列(取指令及 指令执行的过程，包括 PC 自增的过程)。
MDRIR                                  移位器
MDR
ALU
A                B
M
LA                         LB
MAR
RO
R1
R2
R3
PC
02 .设CPU内部结构如下图所示，此外还设有B、C、D、E、H、L 六个寄存器(图中未画出), 它们各自的输入端和输出端都与内部总线相通，并分别受控制信号控制(如Bin 受寄存器B  的输入控制；Bout 受寄存器B的输出控制),假设ALU 的结果直接送入寄存器Z。要求从 取指令开始，写出完成下列指令的微操作序列及所需的控制信号。
ADD         B,C                             (B)+(C)→BSUB  ACC,H                          (ACC)-(H)→ACC
ADD         B,C                             (B)+(C)→B
SUB  ACC,H                          (ACC)-(H)→ACC
控制信号CUCPUIRinIRPCin+1— 地址线MARMDRin数据线MDRACCin   ACCout_Yin控制信号Zout内 部 总 线时钟ALUACCPCoutPCY
控制信号
CU
CPU
IRin
IR
PCin
+1— 地址线
MAR
MDRin
数据线
MDR
ACCin   ACCout_
Yin
控制信号
Zout
内 部 总 线
时钟
ALU
ACC
PCout
PC
Y

[tag_link]

C