---
title: "模拟卷1 数据结构 第5题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "数据结构"
knowledge_points:
  - "二叉排序树"
question_type: "choice"
difficulty: 3
number: 5

---

分别以下列序列构造二叉排序树，与用其他三个序列所构造的结果不同的是（ ）。

A\. （100,80,90,60,120,110,130）
B\. （100,120,110,130,80,60,90）
C\. （100,60,80,90,120,110,130）
D\. （100,80,60,90,120,130,110）

[二叉排序树](/study_methods/tags/408quiz//#%e4%ba%8c%e5%8f%89%e6%8e%92%e5%ba%8f%e6%a0%91)

[tag_link]

正确答案：C
> <p>
在构造二叉排序树时，序列A、B、D生成的树结构相同，而序列C生成的左子树结构不同，具体如下：
<ul><li>A、B、D的树结构为：</li></ul><pre tabindex=0>`        100
       /   \
      80    120
     / \    / \
    60  90 110 130
`</pre><ul><li>C的树结构为：</li></ul><pre tabindex=0>`        100
       /   \
      60    120
        \    / \
         80 110 130
          \
           90
`</pre><p>因此，与其他三个序列所构造的结果不同的是C。
>
