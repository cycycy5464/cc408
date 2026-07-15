---
title: "模拟卷3 组成原理 第16题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "组成原理"
knowledge_points:
  - "访存过程"
question_type: "choice"
difficulty: 3
number: 16

---

某计算机 Cache 的容量为 128KB，块大小为 16 字节，采用 8 路组相联映射方式。则字节地址为 1234567H 的单元调入该 Cache 后，其 Tag 为（ ）。

A\. 1234H
B\. 2468H
C\. 048DH
D\. 12345H

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)

[tag_link]

正确答案：C
> <p> Cache 容量为 128KB，块大小为 16 字节，因此总块数为 128KB / 16B = 8192 块。
> 采用 8 路组相联映射，组数为 8192 / 8 = 1024 组，故索引（Index）需要 10 位（2¹⁰ = 1024）。
> 块内偏移（Offset）需要 4 位（2⁴ = 16 字节）。
> 地址 1234567H 为 28 位（7 个十六进制数字），因此标记（Tag）位数为 28 - 10 - 4 = 14 位。
> <p>Tag 通过将地址右移（Offset 位数 + Index 位数）即 14 位得到。
> 1234567H 右移 14 位相当于除以 2^14（16384），计算得 1234567H / 4000H ≈ 48DH（或十进制 19088743 / 16384 = 1165，即 48DH）。
> 选项 C 的 048DH 即为该值，因此 Tag 为 048DH。
>
