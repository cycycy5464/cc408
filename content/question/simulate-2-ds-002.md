---
title: "模拟卷2 数据结构 第2题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 2
---

循环队列用数组 `A[0...m-1]` 存放其元素值，头尾指针分别为 `front` 和 `rear`，`front` 指向队头元素，`rear` 指向队尾元素的下一个元素，其移动按数组下标增大的方向进行（`rear != m-1` 时），则当前队列中的元素个数是（　）。

A\. `(rear - front + m) % m`
B\. `(rear - front + 1) % m`
C\. `rear - front - 1`
D\. `rear - front`

[tag_link]

正确答案：A
> <p>【解析】在循环队列中，`front` 指针指向队头元素，`rear` 指针指向队尾元素的下一个位置。
> 队列中的元素从 `front` 开始，到 `rear` 的前一个位置结束。
> 由于数组是循环的：
<ul><li>当 `rear ≥ front` 时，元素个数为 `rear − front`；
> </li><li>当 `rear < front` 时，表示 `rear` 已从数组末尾绕回到开头，此时元素个数为 `(rear + m) − front`，即 `rear − front + m`。
> </li></ul><p>综合这两种情况，元素个数可统一表示为
`(rear − front + m) % m`，
该公式通过取模运算确保结果始终为非负整数且正确反映队列长度。
> <p>其他选项中：
<ul><li>B 项 `(rear − front + 1) % m` 在队列为空（`front == rear`）时会得到 1，而非 0；
> </li><li>C 项 `rear − front − 1` 在空队列时得到 −1，且不适用于循环情况；
> </li><li>D 项 `rear − front` 在 `rear < front` 时会产生负数，未考虑循环特性。
> </li></ul><p>因此，只有 A 项适用于所有情况。
>
