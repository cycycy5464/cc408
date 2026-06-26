---
title: "哈希表"
date: 2026-06-25
weight: 3
tags: [哈希, 查找, 散列]
difficulty: 2
prerequisites:
  - "线性表"
subject: data-structure
chapter: 7
chapter_title: "查找"
exam_points:
  - "哈希函数构造"
  - "冲突处理方法"
  - "哈希表性能分析"
---

## 概述

哈希表（Hash Table）是根据关键码值而直接进行访问的数据结构。它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。

## 哈希函数构造方法

### 直接定址法

$h(key) = key$ 或 $h(key) = a \times key + b$

### 除留余数法（最常用）

$h(key) = key \mod p$，其中 $p \leq m$，m 为表长

### 数字分析法

抽取关键字中取值比较均匀的数字作为哈希地址

### 平方取中法

关键字平方后取中间几位作为哈希地址

## 冲突处理方法

### 线性探测再散列

$h_i = (h(key) + i) \mod m$

### 二次探测再散列

$h_i = (h(key) + i^2) \mod m$ 或 $h_i = (h(key) - i^2) \mod m$

### 链地址法

所有同义词结点链接成一个单链表

```c
typedef struct HashNode {
    ElemType data;
    struct HashNode *next;
} HashNode;

typedef struct {
    HashNode *buckets[M];
    int count;
} HashTable;
```

## 哈希表性能分析

- 平均查找长度取决于：哈希函数、处理冲突的方法、装填因子 $\alpha = n/m$
- 装填因子越小，发生冲突的可能性越小
