---
title: "模拟卷8 数据结构 第7题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 8
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 7
---

已知有向图 G=(V, A)，其中 V={a,b,c,d,e}，A={<a,b>, <a,c>, <d,c>, <d,e>, <b,e>, <c,e>}，对该图进行拓扑排序，下面序列中不是拓扑排序的是（ ）。

A\. a,d,c,b,e
B\. d,a,b,c,e
C\. a,b,d,c,e
D\. a,h,c,d,e

[tag_link]

正确答案：D
> <p> 拓扑排序要求对于有向图中的每一条边<u,v>，在排序序列中顶点 u 必须出现在顶点 v 之前。
> 给定图 G 的顶点集 V={a,b,c,d,e}，边集 A={<a,b>, <a,c>, <d,c>, <d,e>, <b,e>, <c,e>}，因此约束条件为：a 在 b 和 c 之前，d 在 c 和 e 之前，b 在 e 之前，c 在 e 之前。
> <p>逐一检查选项：
<ul><li>选项 A（a,d,c,b,e）：a 在 b 和 c 之前，d 在 c 和 e 之前，b 和 c 在 e 之前，所有边约束均满足，是拓扑排序。
> </li><li>选项 B（d,a,b,c,e）：d 在 c 和 e 之前，a 在 b 和 c 之前，b 和 c 在 e 之前，所有边约束均满足，是拓扑排序。
> </li><li>选项 C（a,b,d,c,e）：a 在 b 和 c 之前，d 在 c 和 e 之前，b 和 c 在 e 之前，所有边约束均满足，是拓扑排序。
> </li><li>选项 D（a,h,c,d,e）：序列中包含顶点 h，而 h 不在图 G 的顶点集 V 中，因此不是有效序列。
> 即使假设 h 是 b 的笔误，序列变为 a,b,c,d,e，此时边<d,c>要求 d 在 c 之前，但序列中 d 在 c 之后，违反约束。
> 故选项 D 不是拓扑排序。
> </li></ul><p>因此，不是拓扑排序的序列是选项 D。
>
