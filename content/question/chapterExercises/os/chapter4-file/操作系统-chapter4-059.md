---
title: "文件管理 第6题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "目录"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 59
tags: ['课后题']
---

在某个文件系统中，外存为硬盘。物理块大小为512B,  有文件A 包含598条记录，每条 记录占255B,  每个物理块放2条记录。文件A 所在的目录如下图所示。文件目录采用多  级树形目录结构，由根目录节点、作为目录文件的中间节点和作为信息文件的树叶组成， 每个目录项占127B,  每个物理块放4个目录项，根目录的第一块常驻内存。试问：
1) 若文件的物理结构采用链式存储方式，链指针地址占2B,   则要将文件 A 读入内存， 至少需要存取几次硬盘?
2)若文件为连续文件，则要读文件A 的第487条记录至少要存取几次硬盘?
roottmpyoufilel        dirl        dir2like    margde v      etemikboot
root
tmp
you
filel        dirl        dir2
like    marg
de v      ete
mik
boot

[tag_link]

B