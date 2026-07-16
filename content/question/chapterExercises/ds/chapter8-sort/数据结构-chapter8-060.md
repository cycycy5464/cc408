---
title: "排序 第7题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "数据结构"
knowledge_points:
  - "选择排序"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 60
tags: ['课后题']
---

优先队列( Priority   Queue) 是一种数据结构，它类似于普通队列，但每个元素都有一个 优先级。元素在入队时会根据其优先级来排序，而不按照先入先出的顺序来排序。每次 从优先队列中出队时，出队的是优先级最高的元素，而不是最早进入队列的元素。
队列中的元素的数据结构的定义如下：
typedef             struct{int          value;                      //元素的值int             priority;                 //元素的优先级，priority        越大，优先级越高}PriorityQueueElement;
typedef             struct{
int          value;                      //元素的值
int             priority;                 //元素的优先级，priority        越大，优先级越高
}PriorityQueueElement;
请设计一个优先队列，要求满足：①初始时队列为空；②入队时，不允许增加队列的 占用空间；③出队后，出队元素所占用的空间可重复使用，即整个队列所占用的空间  不变；④入队操作和出队操作的时间复杂度始终保持为O(log₂n) 。请回答：
1) 该队列是应选择链式存储结构，还是选择顺序存储结构?
2)给出优先队列的数据结构的定义。
3)用伪代码给出入队操作和出队操作的基本过程(关键之处可用文字描述)。

[tag_link]

【解答】