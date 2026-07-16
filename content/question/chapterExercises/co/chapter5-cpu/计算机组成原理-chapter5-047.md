---
title: "中央处理器 第3题"
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
number: 47
tags: ['课后题']
---

设有如下图所示的单总线结构，分析指令ADD(RO),R1 [ 即实现( RO)+(R1)→(RO)]的 指令流程和控制信号。
指令译码/控制器总线IRinAdIRoutPCin PCoutMARinMDRinMemW→MDRoutROinR₀ROoutRn-1in  Rn-1outYinALUinALUZoutMDRoutEMDRinEMARMDR控制信号-控制信号MARoutMemR→PC+1—主  存PCIRYZRn-1
指令译码/控制器
总线
IRin
AdIRout
PCin PCout
MARin
MDRin
MemW→
MDRout
ROin
R₀
ROout
Rn-1in  Rn-1out
Yin
ALUin
ALU
Zout
MDRoutE
MDRinE
MAR
MDR
控制信号-
控制信号
MARout
MemR→
PC+1—
主  存
PC
IR
Y
Z
Rn-1
主存储器(M)ACCALU04. 右图是一个简化的CPU 与主存连接结构示意 图(图中省略了所有的多路选择器)。其中有 一个累加寄存器( ACC) 、 一个状态寄存器 和 其 他 4 个寄存器：存储器地址寄存器 (MAR) 、 存储器数据寄存器( MDR) 、 程 序计数器( PC)  和指令寄存器( IR),    各 部 件及其之间的连线表示数据通路，箭头表示信 息传递方向。
主存储器(M)
ACC
ALU
要求：                                                       微操作信号
1)请写出图中a、b、c、d 四个寄存器的名称。             状态寄存器         发生器
2)简述图中取指令的数据通路。
3)简述数据在运算器和主存之间进行存/取访问的数据通路(假设地址已在MAR 中 ) 。
4)简述完成指令LDAX  的数据通路( X 为主存地址，LDA 的功能为(X)→ACC)。
5)简述完成指令 ADD   Y 的数据通路 ( Y  为主存地址， ADD  的功能为(ACC)+
(Y)→ACC)。
6)简述完成指令STAZ  的数据通路( Z 为主存地址，STA 的功能为(ACC)→Z)。

[tag_link]

【解答】