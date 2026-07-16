---
title: "指令系统 第2题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "指令的寻址方式"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 40
tags: ['课后题']
---

某计算机字长16位，标志寄存器FLAGS 中的ZF 、SF 和 OF 分别是零标志、符号标志 和溢出标志，采用双字节字长指令字。假定 bgt ( 大于零转移)指令的第一个字节指明 操作码和寻址方式，第二个字节为偏移地址Imm8,   用补码表示。指令功能是：
若 ( ZF+(SF   田 OF)=0),       则 PC=PC+2+Imm8×2;          否则，PC=PC+2。
请回答下列问题：
1)该计算机的编址单位是多少?
2) bgt 指令执行的是有符号整数比较，还是无符号整数比较?
3)偏移地址 Imm8 的含义是什么?转移目标地址的范围是什么?

[tag_link]

A