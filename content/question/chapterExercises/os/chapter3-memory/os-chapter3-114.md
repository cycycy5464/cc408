---
title: "内存管理 第55题"
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
number: 114
tags: ['课后题']
---

D
地址结构长18位，所以主存的最大容量为2⁸=256KB; 页内偏移量占11位，所以页面大小 为2¹=2048B;  页号占7位，所以主存页数为2⁷=128个。该指令的相对地址为1500,小于一个 页面的大小，所以该指令存放在2号物理块中，物理地址为2×2048+1500=5596,指令数据的存 放地址为2500,大于一个页面的大小，所以指令数据存放在3号物理块中。

[tag_link]

C