---
title: "模拟卷6 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "数据结构"
knowledge_points:
  - "栈"
question_type: "choice"
difficulty: 3
number: 1

---

设有一个递归算法如下：

A\. 2
B\. 3
C\. 4
D\. 5

[栈](/study_methods/tags/408quiz//#%e6%a0%88)

[tag_link]

正确答案：B
> <p>【解析】
计算 X(5) 时，首先调用 X(5) 一次。
> 由于参数 n=5 大于 3，执行 else 分支，需要递归调用 X(n-2) 即 X(3) 和 X(n-4) 即 X(1)。
> <p>调用 X(3) 时，因为 3≤3，直接返回 1，不再递归，此次调用计一次。
> 调用 X(1) 时，同样因为 1≤3，直接返回 1，也不再递归，此次调用也计一次。
> <p>因此，总共调用了三次 X 函数：分别是 X(5)、X(3) 和 X(1)。
> 对应选项为 B.3。
>
