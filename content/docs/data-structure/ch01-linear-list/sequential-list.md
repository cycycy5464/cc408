---
title: "线性表"
date: 2026-06-25
weight: 1
tags: [线性表, 顺序表, 链表]
difficulty: 1
prerequisites: []
subject: data-structure
chapter: 1
chapter_title: "线性表"
exam_points:
  - "顺序表操作"
  - "链表操作"
---

## 概述

线性表是最基本、最简单、也是最常用的一种数据结构。线性表中数据元素之间的关系是一对一的关系，即除了第一个和最后一个数据元素之外，其它数据元素都是首尾相接的。

## 顺序表

顺序表是用一段物理地址连续的存储单元依次存储数据元素的线性结构，一般情况下采用数组存储。

### 基本操作

```c
#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int length;
} SqList;

// 初始化
void InitList(SqList *L) {
    L->length = 0;
}

// 插入元素 (在第i个位置插入e)
int ListInsert(SqList *L, int i, ElemType e) {
    if (i < 1 || i > L->length + 1) return 0;
    if (L->length >= MAXSIZE) return 0;
    for (int j = L->length; j >= i; j--) {
        L->data[j] = L->data[j-1];
    }
    L->data[i-1] = e;
    L->length++;
    return 1;
}

// 查找元素
int LocateElem(SqList L, ElemType e) {
    for (int i = 0; i < L.length; i++) {
        if (L.data[i] == e) return i + 1;
    }
    return 0;
}
```

### 复杂度分析

- 插入/删除：平均 $O(n)$，最坏 $O(n)$
- 查找：$O(n)$

## 链表

链表用一组任意的存储单元存储线性表的数据元素。

### 单链表

```c
typedef struct LNode {
    ElemType data;
    struct LNode *next;
} LNode, *LinkList;

// 头插法建表
LinkList CreateHead(LinkList *L) {
    *L = (LinkList)malloc(sizeof(LNode));
    (*L)->next = NULL;
    ElemType e;
    scanf("%d", &e);
    while (e != 9999) {
        LNode *p = (LNode*)malloc(sizeof(LNode));
        p->data = e;
        p->next = (*L)->next;
        (*L)->next = p;
        scanf("%d", &e);
    }
    return *L;
}

// 按值查找
LNode* LocateNode(LinkList L, ElemType e) {
    LNode *p = L->next;
    while (p && p->data != e) {
        p = p->next;
    }
    return p;
}
```

### 双向链表

```c
typedef struct DuLNode {
    ElemType data;
    struct DuLNode *prior, *next;
} DuLNode, *DuLinkList;
```

## 栈与队列

### 栈（Stack）

先进后出（LIFO）

```c
#define STACK_MAX 100
typedef struct {
    ElemType data[STACK_MAX];
    int top;
} SqStack;
```

### 队列（Queue）

先进先出（FIFO）

```c
#define QUEUE_MAX 100
typedef struct {
    ElemType data[QUEUE_MAX];
    int front, rear;
} SqQueue;
```

## 相关题目

- [2023年408真题 - 应用题第1题](/exam/application/2023-q1/)
