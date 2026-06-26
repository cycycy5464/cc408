---
title: "二叉树"
date: 2026-06-25
weight: 2
tags: [树, 二叉树, 遍历]
difficulty: 2
prerequisites:
  - "线性表"
  - "栈"
subject: data-structure
chapter: 4
chapter_title: "树与二叉树"
exam_points:
  - "树的存储结构"
  - "二叉树遍历"
  - "树与森林的遍历"
---

## 概述

二叉树是 n(n≥0) 个结点的有限集合，该集合或者为空根（称为空二叉树），或者由一个根结点和两棵互不相交的、分别称为根结点的左子树和右子树的二叉树组成。

## 二叉树的性质

1. 第 i 层最多有 $2^{i-1}$ 个结点（i≥1）
2. 深度为 k 的二叉树最多有 $2^k - 1$ 个结点
3. 对任何二叉树，若叶子结点数为 $n_0$，度为2的结点数为 $n_2$，则 $n_0 = n_2 + 1$

## 二叉树的遍历

### 先序遍历（DLR）

```c
void PreOrder(BiTree T) {
    if (T != NULL) {
        visit(T);           // 访问根结点
        PreOrder(T->lchild); // 先序遍历左子树
        PreOrder(T->rchild); // 先序遍历右子树
    }
}
```

### 中序遍历（LDR）

```c
void InOrder(BiTree T) {
    if (T != NULL) {
        InOrder(T->lchild);  // 中序遍历左子树
        visit(T);            // 访问根结点
        InOrder(T->rchild);  // 中序遍历右子树
    }
}
```

### 后序遍历（LRD）

```c
void PostOrder(BiTree T) {
    if (T != NULL) {
        PostOrder(T->lchild);  // 后序遍历左子树
        PostOrder(T->rchild);  // 后序遍历右子树
        visit(T);              // 访问根结点
    }
}
```

### 层序遍历

```c
void LevelOrder(BiTree T) {
    InitQueue(Q);
    EnQueue(Q, T);
    while (!QueueEmpty(Q)) {
        DeQueue(Q, p);
        visit(p);
        if (p->lchild != NULL) EnQueue(Q, p->lchild);
        if (p->rchild != NULL) EnQueue(Q, p->rchild);
    }
}
```

## 线索二叉树

利用二叉树中的空指针域，存放指向结点在某种遍历次序下的前驱和后继结点的指针。

## 树与森林

- 树的存储：双亲表示法、孩子表示法、孩子兄弟表示法
- 树/森林与二叉树的转换
