---
title: "模拟卷4 计算机组成原理 第15题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "choice"
difficulty: 3
number: 15
---

设某按字节编址的计算机已配有 00000H～07FFFH 的 ROM 区，MAR 为 20 位，现再用 16K×8 位的 RAM 芯片构成剩下的 RAM 区 08000H～FFFFFH，则需要这样的 RAM 芯片（ ）片。

A\. 61

B\. 62

C\. 63

D\. 64

[tag_link]

正确答案：B
> 首先，MAR 为 20 位，总地址空间为 2^20=1MB，地址范围从 00000H 到 FFFFFH。
> ROM 区已配置为 00000H～07FFFH，计算其大小：结束地址 07FFFH 减去起始地址 00000H 再加 1，得到 08000H，即 32KB（因为 08000H=32768 字节=32KB）。
> 因此，RAM 区的地址范围为 08000H～FFFFFH。
> 总地址空间为 100000H（即 1MB），RAM 区大小等于总空间减去 ROM 区大小，即 100000H - 08000H = F8000H，转换为十进制为 992KB（因为 F8000H=1,015,808 字节=992KB）。
> 题目中 RAM 芯片规格为 16K×8 位，即每个芯片容量为 16KB（16K×8 位=16,384 字节）。
> 所需芯片数等于 RAM 区总容量除以单个芯片容量：992KB / 16KB = 62。
> 因此，需要 62 片这样的 RAM 芯片。
>

