---
title: "模拟卷3 数据结构 第2题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 2
---

当字符序列 `t3_` 作为栈的输入时，则输出长度为 3，且可用 C 语言标识符的序列有（ ）个。

A\. 4
B\. 5
C\. 3
D\. 6

[tag_link]

正确答案：C
> 【解析】考查栈的操作。
> 标识符只能以字母或下划线开头，即由 `t`、`3`、`_` 能够组成的合法标识符只有：`t3_`、`t_3`、`_3t`、`_t3`，而当用 `t3_` 作为栈的输入时，`_t3` 无法作为输出序列，所以输出的合法标识符有 `t3_`；
> `t_3`；
> `_3t`，因此选 `C`。
>
