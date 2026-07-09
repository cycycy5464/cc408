---
title: "模拟卷4 数据结构 第1题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 1
---

若循环队列以数组 Q[0..m-1] 为其存储结构，变量 rear 表示循环队列中的队尾元素的实际位置，其移动按 rear=(rear+1) MOD m 进行，变量 length 表示当前循环队列中的元素个数，则循环队列的队首元素的实际位置是（ ）。

A\. rear-length

B\. (rear-length+m) MOD m

C\. (1+rear-m-length) MOD m

D\. (rear-length-1) MOD m

[tag_link]

正确答案：C
> 循环队列中，队尾元素的位置由 rear 给出，队列当前元素个数为 length 。
> 设队���元素的位置为 front ，由于队列元素从 front 连续存储到 rear （考虑循环），因此 rear 与 front 满足关系： rear = ( front + length − 1 ) mod m 解出 front ，得： front = ( rear − length + 1 ) mod m 选项 C 的表达式为 (1 + rear - m - length) MOD m ，可化简为： ( rear − length + 1 − m ) mod m 在模 m 运算下，减去 m 不改变余数，因此该表达式等价于： ( rear − length + 1 ) mod m 与推导结果一致。
> 通过实例验证：设 m = 10 ， rear = 3 ， length = 5 ，则队首应为位置 9。
> 计算选项 C： ( 1 + 3 − 10 − 5 ) mod 10 = ( − 11 ) mod 10 = 9 结果正确；
> 而其他选项均不满足。
> 因此，循环队列的队首元素实际位置为选项 C。
>

