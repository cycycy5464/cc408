---
title: "指令系统 第21题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "组成原理"
knowledge_points:
  - "指令的寻址方式"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 35
tags: ['课后题']
---

某计算机字长为16位，标志寄存器中存在ZF 、SF 、OF和 CF 标志位，采用双字节字长 指令字。假定 bgt ( 大于零转移)指令的第一个字节指明操作码和寻址方式，第二个字 节为立即数Imm8, 用补码表示。指令功能是：若转移条件成立，则 PC=PC+2+Imm8×2;
否则，PC=PC+2 。   则下列叙述中错误的是()。

A. 该计算机按字节编址
B. 若 bgt 指令是无符号整数的比较，则转移条件可以是 ZF+CF=0
C. 若 bgt 指令是有符号整数的比较，则转移条件可以是 SF 田OF=0
D. 转移目标地址的范围是相对于bgt 指令的前127条指令到后128条指令之间

[tag_link]

正确答案：C