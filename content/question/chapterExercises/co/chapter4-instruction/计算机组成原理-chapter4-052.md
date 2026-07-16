---
title: "指令系统 第12题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机组成原理"
knowledge_points:
  - "CISC和RISC"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 52
tags: ['课后题']
---

假设P 为调用过程，Q 为被调用过程，程序在32位x86 处理器上执行，以下是 C 语言 程序中过程调用所涉及的操作：
① 过 程Q 保存P 的现场，并为非静态局部变量分配空间
② 过 程P 将实参存放到Q 能访问到的地方
③ 过 程P 将返回地址存放到特定处，并转移到Q 执行
④ 过 程Q 取出返回地址，并转移回到过程P 执行
⑤ 过 程Q 恢 复P 的现场，并释放局部变量所占空间
⑥执行过程Q 的函数体
过程调用的正确执行步骤是()。

A. ②→③→④→(                                       B.②-     ③→ (①→ (
C. ②→③→             ⑥→                   D.②→(  ③-     ⑤-

[tag_link]

正确答案：C