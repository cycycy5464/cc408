---
title: "内存管理 第2题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "虚拟内存管理"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 95
tags: ['课后题']
---

【解答】
分区号
大 小
始 址
1
12KB
120K
2
10KB
150K
3
5KB
200K
4
18KB
420K
采用最佳适应算法时，作业序列分别进入5,1,4号空闲分区，可以满足其请求。分配处理之 后的空闲分区表见下表：
此时再无空闲分区可以满足200KB大小的作业，所以该作业序列请求无法满足。
分区号
大 小
始 址
1
12KB
120K
2
10KB
150K
3
5KB
200K
4
122KB
316K
5
96KB
530K
采用首次适应算法时，96KB 大小的作业进入4号空闲分区，20KB大小的作业进入1号空闲 分区，这时空闲分区如下表所示。

[tag_link]

正确答案：【解答】