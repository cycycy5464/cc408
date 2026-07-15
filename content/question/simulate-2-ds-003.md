---
title: "模拟卷2 数据结构 第3题"
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
number: 3
---

将 5 个字母 “ooops” 按此顺序进栈，则有（　）种不同的出栈顺序可以仍然得到 “ooops”。

A\. 1
B\. 3
C\. 5
D\. 6

[tag_link]

正确答案：C
> <p> 将5个字母“ooops”按顺序进栈，即进栈序列为o、o、o、p、s。
> 要求出栈序列仍然为“ooops”，即出栈顺序为o、o、o、p、s。
> 由于三个o相同，不同的出栈顺序指的是三个o的个体出栈顺序不同，但最终输出的字符串相同。
> <p>设三个o分别为A、B、C（按进栈顺序），p为D，s为E。
> 出栈序列必须满足前三个为A、B、C的某种排列，第四个为D，第五个为E。
> 三个o的排列共有6种：ABC、ACB、BAC、BCA、CAB、CBA。
> 需要检查每种排列是否满足栈的合法性（即能否通过合理的进栈和出栈操作实现）。
> <ol><li>ABCDE：合法，可每进栈一个元素后立即出栈。
> </li><li>ACBDE：合法，A进栈后出栈，B进栈后不出，C进栈后出栈C，再出栈B。
> </li><li>BACDE：合法，A进栈后不出，B进栈后出栈B，再出栈A，然后C、D、E依次进栈出栈。
> </li><li>BCADE：合法，A进栈后不出，B进栈后出栈B，C进栈后出栈C，再出栈A。
> </li><li>CABDE：不合法，因为C首先出栈后，栈中剩余A和B（B为栈顶），下一个需要出栈A，但A不在栈顶，无法直接出栈。
> </li><li>CBADE：合法，A进栈后不出，B进栈后不出，C进栈后出栈C，再出栈B，最后出栈A。
> </li></ol><p>因此，只有5种合法的出栈顺序，对应选项C。
>
