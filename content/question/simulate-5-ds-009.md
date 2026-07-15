---
title: "模拟卷5 数据结构 第9题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "数组查找"
question_type: "choice"
difficulty: 3
number: 9

---

折半查找有序表 (2,10,25,35,40,65,70,75,81,82,88,100)，若查找元素 75，需依次与表中元素（ ）进行比较。

A\. 65,82,75
B\. 70,82,75
C\. 65,81,75
D\. 65,81,70,75

[数组查找](/study_methods/tags/408quiz//#%e6%95%b0%e7%bb%84%e6%9f%a5%e6%89%be)

[tag_link]

正确答案：D
> <p> 考查折半查找的查找过程。
> 有序表长度为 12，依据折半查找的思想：
<ul><li>第一次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>12</span><span class=mclose>)</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>6</span></span></span></span>
个元素，即 65；
> </li><li>第二次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊((</span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>12</span><span class=mclose>)</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span></span></span></span>
个元素，即 81；
> </li><li>第三次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊(</span><span class=mord>7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>9</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>))</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>7</span></span></span></span>
个元素，即 70；
> </li><li>第四次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊(</span><span class=mord>7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>8</span><span class=mclose>⌋</span><span class=mord>/2</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
个元素，即 75。
> </li></ul><p>比较的元素依次为 65、81、70、75。
> 对应的折半查找判定树如下图所示。
> <pre tabindex=0>`        65
      /    \
    25      81
   /  \     /  \
  2    35  70   88
 /     \    \   /  \
10      40   75 82  100
`</pre>
>
