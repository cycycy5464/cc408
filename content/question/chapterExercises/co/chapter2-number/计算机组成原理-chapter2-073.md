---
title: "数据的表示和运算 第21题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "浮点数的表示和运算"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 73
tags: ['课后题']
---

在按字节编址的计算机中，采用小端方式存储数据，某静态二维数组b的声明如下：static         short         b[2][4]=      2,9,-1,5},{3,1,-6,2}};                            若b 的首地址为0x8049820,  采用按行优先存储，地址0x804982c中 的 内 容 是 ( ) 。A.FAH                     B.FFH                         C.00H                           D.05H22. 在按字节编址的计算机中，数据在存储器中以小端方式存放。假定 int 型变量 i 的地址为08000000H,i   的机器数为01234567H,  地址08000000H单元的内容是()。A . 01H                     B.23H                          C.45H                          D.67H23.在按字节编址的32位计算机中，按边界对齐方式为以下结构型变量x 分配存储空间：struct           cont_info{char      id;unsigned        post;char      phone;}x;若x 的首地址为0x8049820,   则成员变量 phone 的起始地址为()。A.0x8049828           B.Ox8049826           C.0x8049825             D.Ox804982224. 假定变量i 、f 的数据类型分别是int 、float 。已知i=12345,f=1.2345×2³,         则在一个32 位机器中执行下列表达式时，结果为“假”的是()。A.i==(int)(double)i                                  B.f==(float)(double)fC.i==(int)(float)i                                         D.f==(float)(int)f25. 有以下C 语言代码段：int      m= 13;float                  a=12.6,x;x=m/2  +a/  2;printf("8f\n",x);

[tag_link]

正确答案：A