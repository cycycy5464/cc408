---
title: "指令系统 第6题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "组成原理"
knowledge_points:
  - "CISC和RISC"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 46
tags: ['课后题']
---

程序 P中有两个变量i 和j,  被分别分配在寄存器 eax 和 edx 中 ，P 中语句“if(i<j){.….}” 对应的指令序列如下(左边为指令地址，中间为机器代码，右边为汇编指令),其中jle  指令的偏移量为Od:
804846a
39
c2
cmp
dword     ptr
edx,eax
804846c
7e
Od
jle
xxxxxxxX
若执行到804846aH 处的 cmp 指令时，i=105,j=100,          则jle 指令执行后将转到() 处的指令执行。

A. 8048461H              B.804846eH                C.8048479H             D.804847bH

[tag_link]

正确答案：D