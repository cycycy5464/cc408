---
title: "模拟卷6 数据结构 第5题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 5
---

如图所示为一棵平衡二叉树（字母不是关键字），在结点 D 的右子树上插入结点 F 后，会导致该平衡二叉树失去平衡，则调整后的平衡二叉树中平衡因子的绝对值为 1 的分支结点数为（ ）。

A\. 0
B\. 1
C\. 2
D\. 3

[tag_link]

正确答案：B
> <p> 考查平衡二叉树的旋转。
> 由于在结点 A 的右孩子（R）的右子树（R）上插入新结点 F，A 的平衡因子由 -1 减至 -2，导致以 A 为根的子树失去平衡，需要进行 RR 旋转（左单旋）。
> <div class=img-container style=height:auto;width:80% oncontextmenu=return!1><img src=/images/408simulate/6_5_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1></div><p>RR 旋转的过程如上图所示，将 A 的右孩子 C 向左上旋转代替 A 成为根结点，将 A 结点向左下旋转成为 C 的左子树的根结点，而 C 的原来的左子树 E 则作为 A 的右子树。
> 故，调整后的平衡二叉树中平衡因子的绝对值为 1 的分支结点数为 1。
> <p>注意：平衡旋转的操作都是在插入操作后，引起不平衡的最小不平衡子树上进行的，只要将这个最小不平衡子树调整平衡，则其上级结点也将恢复平衡。
>
