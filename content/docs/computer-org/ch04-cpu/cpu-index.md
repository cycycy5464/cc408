---
title: "中央处理器"
aliases: ["中央处理器"]
date: 2026-06-25
weight: 20
tags: [CPU]
difficulty: 2
prerequisites: ["数据对齐", "指令格式与寻址方式", "高级语言与机器码", "指令系统", "指令操作码", "指令集种类"]
subject: computer-org
chapter: 3
chapter_title: "中央处理器"
---

本章是重中之重，几乎每年都会在大题和选择题中考察。需要熟练掌握 CPU 的结构、寄存器类型以及指令执行的流程，关于 CPU 的考察也常常和指令系统混合在一起，需要能够从一个高维的角度，思考 CPU、指令、控制器以及外部设备的关系。
  ![](/cc408/images/docs/computer-org/image-20260612231133463.png)
## CPU的功能和基本结构

## 指令执行过程

## 数据通路的功能和基本结构

## 控制器的功能和工作原理

## 异常和中断机制

- 基本概念
- 分类
- 检测和响应

## 指令流水线

- 基本概念
- 基本实现
- 结构冒险、数据冒险和控制冒险
- 超标量和动态流水线的基本概念

## 多处理器基本概念

- SISD、SIMD、MIMD、向量处理器的基本概念
- 硬件多线程的概念
- 多核处理器的基本概念
- 共享内存多处理器的概念

## 总线和输入/输出系统

### 总线

- 基本概念
- 组成及性能指标
- 事务和定时

### I/O接口

- 功能和基本结构
- 端口及其编址

### I/O方式

- 程序查询方式
- 程序中断方式
- DMA方式





* * *

##### [功能和结构](</constitution_principle/cpu/structure/>)

##### [控制器](</constitution_principle/cpu/controller/>)

##### [异常与中断](</constitution_principle/cpu/interrupt/>)

##### [指令流水线](</constitution_principle/cpu/pipeline/>)

##### [多处理器](</constitution_principle/cpu/multicore/>)


## 相关笔记

- [[data-alignment|数据对齐]]
- [[format-addressing|指令格式与寻址方式]]
- [[hll-machine|高级语言与机器码]]
- [[instruction-index|指令系统]]
- [[opcode|指令操作码]]
- [[types|指令集种类]]
