---
title: "内存管理 第64题"
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
number: 105
tags: ['课后题']
---

D
例 如 ，file1.o 的逻辑地址为0～1023,main.o  的逻辑地址为0～1023,假设链接时将 file1.o 链接在main.o 之后，则链接之后file1.o 对应的逻辑地址应为1024～2047。
编译后的程序需要经过链接才能装载，而链接后形成的目标程序中的地址也就是逻辑地址。 以 C 语言为例：C 程序经过预处理→编译→汇编→链接产生了可执行文件，其中链接的前一步是  产生可重定位的二进制目标文件。C 语言采用源文件独立编译的方法，如程序main.c,filel.c,file2.c,      file1.h,file2.h  在链接的前一步生成了main.o,filel.o,file2.0,    这些目标模块的逻辑地址都从0开始， 但只是相对于该模块的逻辑地址。链接器将这三个文件、libc 和其库文件链接成一个可执行文件， 从而形成整个程序的完整逻辑地址空间。

[tag_link]

