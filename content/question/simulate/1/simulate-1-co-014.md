---
title: "模拟卷1 组成原理 第14题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "组成原理"
knowledge_points:
  - "寄存器类型"
question_type: "choice"
difficulty: 3
number: 14

---

在 C 语言中，short 型的长度为 16 位，若编译器将一个 short 型变量 x 分配到一个 32 位寄存器 R 中，且 X=0x8FA0，则 R 的内容为（ ）。

A\. 0x00008FA0
B\. 0xFFFF8FA0
C\. 0xFFFFFFA0
D\. 0x80008FA0

[寄存器类型](/study_methods/tags/408quiz//#%e5%af%84%e5%ad%98%e5%99%a8%e7%b1%bb%e5%9e%8b)

[tag_link]

正确答案：B
> 在 C 语言中，`short` 类型默认为有符号整数，长度为 16 位。
> 当将其值存入 32 位寄存器时，需要进行符号扩展以保持数值不变。
> 给定 `x = 0x8FA0`，其二进制表示为 `1000 1111 1010 0000`，最高位为 1，表示负数。
> 符号扩展时，高 16 位需用符号位（1）填充，因此扩展后的 32 位值为 `0xFFFF8FA0`。
>
