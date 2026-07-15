---
title: "模拟卷7 数据结构 第32题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "choice"
difficulty: 3
number: 32
---

下列关于中断 I/O 方式的描述中，正确的是（ ）

A\. CPU 在 I/O 设备进行数据准备时一直处于等待状态，直到 I/O 操作完成
B\. 中断 I/O 方式下，每传输一个数据块都需要 CPU 进行多次干预
C\. 中断处理过程中，CPU 在响应中断请求后立即保存当前进程的 PCB 信息
D\. 采用中断驱动 I/O 方式时，CPU 与 I/O 设备之间无法实现并行工作

[寄存器类型](/study_methods/tags/408quiz//#%e5%af%84%e5%ad%98%e5%99%a8%e7%b1%bb%e5%9e%8b)
[进程控制块](/study_methods/tags/408quiz//#%e8%bf%9b%e7%a8%8b%e6%8e%a7%e5%88%b6%e5%9d%97)

[tag_link]

正确答案：B
> <p>
<ul><li>A ❌ 描述的是 **程序直接控制（轮询）方式** 的特点，中断 I/O 方式中 CPU 在设备准备数据时可执行其他任务，无需忙等。
> </li><li>B ✅ 中断 I/O 方式下，每完成一个 **字（或字节）** 的传输，设备便向 CPU 发出中断请求，CPU 需介入进行数据存取与状态处理，因此传输一个数据块需多次中断及 CPU 干预。
> </li><li>C ❌ 响应中断后，CPU 首先保存的是 **当前程序的现场（如 PC、寄存器等）**，而非整个 PCB；
> PCB 的保存通常在进程切换时发生，并非中断响应的立即操作。
> </li><li>D ❌ 中断 I/O 方式正是为了实现 CPU 与 I/O 设备的并行工作，设备准备数据时 CPU 可执行其他任务，通过中断机制进行协调。
> </li></ul>
>
