---
title: "模拟卷4 数据结构 第5题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "数据结构"
knowledge_points:
  - "森林的概念"
  - "二叉树的遍历"
question_type: "choice"
difficulty: 3
number: 5

---

某二叉树结点的中序序列为 BDAECF，后序序列为 DBEFCA，则该二叉树对应的森林包括（ ）棵树。

A\. 1
B\. 2
C\. 3
D\. 4

[森林的概念](/study_methods/tags/408quiz//#%e6%a3%ae%e6%9e%97%e7%9a%84%e6%a6%82%e5%bf%b5)
[二叉树的遍历](/study_methods/tags/408quiz//#%e4%ba%8c%e5%8f%89%e6%a0%91%e7%9a%84%e9%81%8d%e5%8e%86)

[tag_link]

正确答案：C
> <p> 考查由遍历序列确定二叉树、森林与二叉树的转换。
> 根据后序序列，A 是二叉树的根结点。
> 根据中序遍历序列，则二叉树的形态一定如下图左所示。
> 对于 A 的左子树，由后序序列可知，因为 B 比 D 后被访问，因此，B 必为 D 的父结点，又由中序序列可知，D 是 B 的右儿子。
> 对于 A 的右子树，同理可确定结点 E、C、F 的关系。
> 此二叉树的形态如下图右所示。
> <div class=img-container style=height:auto;width:80% oncontextmenu=return!1><img src=/images/408simulate/4_5_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1></div><p>再根据二叉树与森林的对应关系。
> 森林中树的棵数即为其对应二叉树（向右上旋转 45° 后）中根结点 A 及其“右兄弟”数。
> 可知此森林中有 3 棵树，根结点分别为 A、C 和 F。
>
