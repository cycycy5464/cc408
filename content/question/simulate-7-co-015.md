---
title: "模拟卷7 计算机组成原理 第15题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "choice"
difficulty: 3
number: 15
---

某存储系统中，主存容量是 Cache 容量的 4096 倍，Cache 被分为 64 块，当主存地址和 Cache 地址采用直接映射方式时，地址映射表的大小应为（ ）。（假设不考虑一致维护位）

A\.

B\.

C\.

D\.

[tag_link]

正确答案：B
> 本题考查 Cache 与主存的映射原理。
> 由于 Cache 被分为 64 块，那么 Cache 有 64 行，采用直接映射，一行相当于一组。
> 故而该标记阵列每行存储 1 个标记项，其中主存标记项为 12bit（ 2 12 = 4096 ，是 Cache 容量的 4096 倍，那就是地址长度比 Cache 长 12 位），加上 1 位有效位，故而为 64 × 13 bit。
> 注意：主存—Cache 地址映射表（标记阵列）中内容：映射的 Cache 地址（直接映射不需要因为 Cache 地址唯一，组相联只需要组号）、主存标记（命中判断）、有效位。
> 如下图所示。
>

