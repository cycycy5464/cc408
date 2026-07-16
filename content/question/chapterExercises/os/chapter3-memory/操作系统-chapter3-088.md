---
title: "内存管理 第1题"
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
number: 88
tags: ['课后题']
---

5×2=3μs
1) 因为页表在主存，所以CPU 必须访问主存两次，即实现一次页面访问的存取时间是
页表在主存时，实现一次存取需要访问主存两次：第一次是访问页表，获得所需访问数据所 在页面的物理地址；第二次才是根据这个物理地址存取数据。

[tag_link]

正确答案：D