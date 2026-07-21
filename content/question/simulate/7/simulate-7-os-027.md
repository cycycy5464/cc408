---
title: "模拟卷7 操作系统 第27题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统概念"
  - "外存空间管理"
question_type: "choice"
difficulty: 3
number: 27

---

某操作系统采用可变分区分配存储管理方法，操作系统占用低地址部分的 126KB。用户区大小为 386KB，且用户区始址为 126KB，用空闲分区表管理空闲分区。若分配时采用分配空闲区高地址部分的方案，且初始时用户区的 386KB 空间空闲，对申请序列：作业 1 申请 80KB，作业 2 申请 56KB，作业 3 申请 120KB，作业 1 释放 80KB，作业 3 释放 120KB，作业 4 申请 156KB，作业 5 申请 81KB。如果采用首次适应算法处理上述序列，则最小空闲块的大小为（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>12</span><span class="mord mathnormal" style=margin-right:.07153em>K</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>13</span><span class="mord mathnormal" style=margin-right:.07153em>K</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>89</span><span class="mord mathnormal" style=margin-right:.07153em>K</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>56</span><span class="mord mathnormal" style=margin-right:.07153em>K</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>

[操作系统概念](/study_methods/tags/408quiz//#%e6%93%8d%e4%bd%9c%e7%b3%bb%e7%bb%9f%e6%a6%82%e5%bf%b5)
[外存空间管理](/study_methods/tags/408quiz//#%e5%a4%96%e5%ad%98%e7%a9%ba%e9%97%b4%e7%ae%a1%e7%90%86)

[tag_link]

正确答案：B
> <p> 我们按照序列逐步模拟存储分配与释放过程。
> 操作系统占用低地址 126KB，用户区始址 126KB，大小 386KB，即用户区范围为 126KB～512KB。
> 初始时，整个用户区空闲，空闲分区表仅有一个分区：起始地址 126KB，大小 386KB。
> 分配时采用首次适应算法，且从找到的空闲分区的高地址部分切割。
> <ol><li><p>**作业 1 申请 80KB**：查找第一个大小≥80KB 的空闲分区（126KB, 386KB），从高地址部分切割 80KB，分配后空闲分区变为（126KB, 306KB）。
> 作业 1 占据 432KB～512KB。
> </li><li><p>**作业 2 申请 56KB**：查找第一个大小≥56KB 的空闲分区（126KB, 306KB），从高地址部分切割 56KB，分配后空闲分区变为（126KB, 250KB）。
> 作业 2 占据 376KB～432KB。
> </li><li><p>**作业 3 申请 120KB**：查找第一个大小≥120KB 的空闲分区（126KB, 250KB），从高地址部分切割 120KB，分配后空闲分区变为（126KB, 130KB）。
> 作业 3 占据 256KB～376KB。
> </li><li><p>**作业 1 释放 80KB**：释放区域为 432KB～512KB，与现有空闲分区（126KB, 130KB）不相邻，空闲分区表变为两个：（126KB, 130KB）和（432KB, 80KB）。
> </li><li><p>**作业 3 释放 120KB**：释放区域为 256KB～376KB，与第一个空闲分区（126KB, 130KB）相邻（结束于 256KB），合并为（126KB, 250KB）。
> 第二个空闲分区（432KB, 80KB）不变。
> 空闲分区表为（126KB, 250KB）和（432KB, 80KB）。
> </li><li><p>**作业 4 申请 156KB**：查找第一个大小≥156KB 的空闲分区（126KB, 250KB），从高地址部分切割 156KB，分配后该分区变为（126KB, 94KB）。
> 作业 4 占据 220KB～376KB。
> 空闲分区表为（126KB, 94KB）和（432KB, 80KB）。
> </li><li><p>**作业 5 申请 81KB**：查找第一个大小≥81KB 的空闲分区（126KB, 94KB），从高地址部分切割 81KB，分配后该分区变为（126KB, 13KB）。
> 作业 5 占据 139KB～220KB。
> 空闲分区表最终为（126KB, 13KB）和（432KB, 80KB）。
> </li></ol><p>最终有两个空闲块，大小分别为 13KB 和 80KB，最小空闲块大小为 13KB，对应选项 B。
>
