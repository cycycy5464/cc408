---
title: "文件管理 第44题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "目录"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 48
tags: ['课后题']
---

设文件 F1 的当前引用计数值为1,先建立F1 的硬链接文件F2,  再建立F2 的符号链接
文件F3,   现有两个进程P₁ 和P₂ 分别打开了F1和 F2,   则下列说法中正确的是()。

A. 两次打开操作只涉及一次文件索引节点的磁盘读取操作
B. 进程 P₁ 和 P₂ 对F1 具有相同的访问权限
C. 若删除文件F3,   则 F2 的引用计数值减1
D. 进程P₁ 读取 F1 时需要提供F1 的绝对路径作为系统调用参数

[tag_link]

正确答案：A