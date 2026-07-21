---
title: "模拟卷1 数据结构 第6题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "数据结构"
knowledge_points:
  - "最小生成树"
  - "图的概念"
question_type: "choice"
difficulty: 3
number: 6

---

设无向图 G=(V,E) 和 G&rsquo;=(V&rsquo;,E&rsquo;)，如果 G&rsquo; 是 G 的生成树，则下面说法错误的是（ ）。

A\. G&rsquo; 是 G 的子图
B\. G&rsquo; 是 G 的连通分量
C\. G&rsquo; 是 G 的极小连通子图且 V&rsquo;=V
D\. G&rsquo; 是 G 的一个无环子图

[最小生成树](/study_methods/tags/408quiz//#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a0%91)
[图的概念](/study_methods/tags/408quiz//#%e5%9b%be%e7%9a%84%e6%a6%82%e5%bf%b5)

[tag_link]

正确答案：B
> 生成树是无向连通图的一个子图，它包含原图的所有顶点，并且是树结构，因此是无环的连通图。
> 选项A正确，因为生成树的顶点集和边集都是原图的子集，所以它是原图的子图。
> 选项B错误，因为连通分量是极大连通子图，即不能再添加任何顶点或边而保持连通。
> 生成树是极小连通子图，不是极大连通子图。
> 对于连通图，其唯一的连通分量是图本身，而生成树是它的一个真子图（除非原图本身就是树），因此生成树不是连通分量。
> 选项C正确，生成树是极小连通子图，意味着去掉任意一条边都会破坏其连通性，并且顶点集与原图相同（V&rsquo;=V）。
> 选项D正确，生成树作为树结构，不包含任何环，因此是无环子图。
>
