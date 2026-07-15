---
title: "模拟卷6 数据结构 第42题"
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
question_type: "comprehensive"
difficulty: 4
number: 42
---

图 1 为某操作系统中文件系统的目录结构。

请回答一下问题：

(1) 本题中的目录结构可抽象为数据结构中的哪种逻辑结构？

(2) 请设计合理的链式存储结构，以保存图 1 中的文件目录信息。要求给出链式存储结构的数据类型定义，并画出对应图 1 中根目录部分到目录 A、B 及其子目录和文件的链式存储结构示意图。

(3) 哈夫曼树是一种特殊的树形结构，请证明哈夫曼树的总结点数总为奇数。

[tag_link]

【解析】 本题考察树的相关内容。

(1) 树

(2) 采用孩子兄弟表示法，数据结构描述如下： typedef struct CSNode { char name [ MaxSize ]; //存储名称 int NodeType ; //值为 0 代表指向文件，为 1 代表指向目录 union p { //用于存储指向文件/目录的信息指针 filepointer p1 ; //文件信息 catalogpointer p2 ; //目录信息 }; struct CSNode * firstchild , * nextsibling ; //第一个孩子和右兄弟指针 } CSNode ; 图中目录结构的存储大致如下： [图片] 本小问只要符合题目要求的答案即可算正确，给出答案仅供参考。

（3）由哈夫曼树中没有度为 1 的结点可知任意哈夫曼树的 n 1 ​ = 0 ，又因哈夫曼树为二叉树，满足 n 0 ​ = 1 + n 2 ​ ，所以哈夫曼树的总结点数 n = n 0 ​ + n 1 ​ + n 2 ​ = n 0 ​ + 0 + n 0 ​ − 1 = 2 n 0 ​ − 1 ，可知无论初始有多少个叶子结点，哈夫曼树的总结点数一定为奇数。
