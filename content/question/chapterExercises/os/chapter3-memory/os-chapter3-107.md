---
title: "内存管理 第62题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "虚拟内存管理"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 107
tags: ['课后题']
---

B
图中，灰色部分为分配出去的空间，白色部分为空闲区。这样，容易发现，此时主存中最大 空闲分区的大小为9MB。
初始分配15MB分配 6MB
初始
分配
15MB
2MB
8MB2MB分配 8MB10MB分配 30MB10MB释放  15MB8MB
8MB
2MB
分配 8MB
10MB
分配 30MB
10MB
释放  15MB
40MB
55MB30MB30MB30MB30MB
55MB
30MB
30MB
30MB
9MB
15MB15MB15MB15MB
15MB
15MB
15MB
6MB
最佳适配算法是指每次为作业分配内存空间时，总是找到能满足空间大小需要的最小空闲分 区给作业，可以产生最小的内存空闲分区。下图显示了这个过程的主存空间变化。

[tag_link]

