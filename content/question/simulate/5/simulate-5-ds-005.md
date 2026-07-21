---
title: "模拟卷5 数据结构 第5题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "二叉排序树"
question_type: "choice"
difficulty: 3
number: 5

---

利用逐个插入建立序列 (50,72,43,85,75,20,35,45,65,30) 对应的二叉排序树后，要查找元素 30 要进行的元素间比较次数是（ ）。

A\. 4
B\. 5
C\. 6
D\. 7

[二叉排序树](/study_methods/tags/408quiz//#%e4%ba%8c%e5%8f%89%e6%8e%92%e5%ba%8f%e6%a0%91)

[tag_link]

正确答案：B
> <p> 考查二叉排序树的构造和查找。
> 按题中数据的输入次序，建立的二叉排序树如右图所示。
> 查找元素 30 需要依次比较的元素为 50,43,20,35,30，比较次数为 5 次。
> <pre tabindex=0>`      50
     /  \
   43    72
  /  \  /  \
 20  45 65  85
  \        /
  35      75
 /
30
`</pre>
>
