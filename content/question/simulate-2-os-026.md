---
title: "模拟卷2 操作系统 第26题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "choice"
difficulty: 3
number: 26
---

对于两个并发进程，设互斥信号量为 mutex，若 mutex=0，则表示（ ）。

A\. 没有进程进入临界区

B\. 有一个进程进入临界区

C\. 有一个进程进入临界区，另一个进程等待进入

D\. 有一个进程在等待进入

[tag_link]

正确答案：B
> 互斥信号量 mutex 用于控制进程对临界区的访问，其初始值通常为 1，表示没有进程进入临界区。
> 当 mutex=0 时，表示有一个进程已经成功执行了 P(mutex) 操作（即 wait 操作），将 mutex 减 1 后变为 0，这意味着该进程进入了临界区，且当前没有其他进程在等待进入临界区（因为等待时 mutex 会变为负值）。
> 因此，选项 B 正确。
> 选项 A 错误，因为 mutex=0 表示有进程在临界区内；
> 选项 C 和 D 错误，因为 mutex=0 时没有进程等待，等待发生时 mutex 值会小于 0。
>

