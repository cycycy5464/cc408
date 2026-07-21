---
title: "模拟卷2 操作系统 第29题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "操作系统"
knowledge_points:
  - "缺页异常"
  - "操作系统概念"
question_type: "choice"
difficulty: 3
number: 29

---

下列叙述中错误的是（　）。

A\. I、III 和 IV
B\. II、III 和 IV
C\. III 和 IV
D\. I、II、III 和 IV

[缺页异常](/study_methods/tags/408quiz//#%e7%bc%ba%e9%a1%b5%e5%bc%82%e5%b8%b8)
[操作系统概念](/study_methods/tags/408quiz//#%e6%93%8d%e4%bd%9c%e7%b3%bb%e7%bb%9f%e6%a6%82%e5%bf%b5)

[tag_link]

正确答案：A
> I 错误：在请求分页存储管理中，缺页中断次数受程序访问局部性、工作集大小等多因素影响，增加页面大小可能减少缺页次数，但并非精确减半，叙述过于绝对。
> II 正确：分页存储管理通过将进程地址空间划分为页面，并利用外存交换，使得进程可以使用比物理内存更大的逻辑地址空间，从而在逻辑上扩充了主存容量。
> III 错误：减少页面大小虽可降低内部碎片，但会导致页表增大、管理开销上升，并可能增加缺页中断次数，因此页面并非越小越好。
> IV 错误：虚拟存储器的地址空间大小由地址位数（如 CPU 寻址能力）决定，是逻辑概念，不等于主存与辅存容量之和；
> 实际物理资源（主存和辅存）用于支持虚拟地址空间的映射和交换。
> 综上，错误叙述为 I、III 和 IV，对应选项 A。
>
