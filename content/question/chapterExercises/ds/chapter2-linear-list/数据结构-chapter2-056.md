---
title: "线性表 第31题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "数据结构"
knowledge_points:
  - "线性表的链式表示"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 56
tags: ['课后题']
---

下列关于静态链表的说法中，正确的是()。
I.  静态链表兼具顺序表和单链表的优点，因此存取表中第 i 个元素的时间与i 无关
II.  静态链表能容纳的最大元素个数在表定义时就确定了，以后不能增加
Ⅲ.静态链表与动态链表在元素的插入、删除上类似，不需要移动元素
IV.  相比动态链表，静态链表可能浪费较多的存储空间
prevdatanext32.【2016统考真题】已知一个带有表头结点的循环双链表L,结点结构为
prev
data
next
其中prev   和 next    分别是指向其直接前驱和直接后继结点的指针。现要删除指针 p 所 指的结点，正确的语句序列是()。

A. I 、Ⅱ 、Ⅲ                                                B.Ⅱ 、Ⅲ 、IV
C. I 、Ⅲ 、IV                                                 D.I 、Ⅱ 、IV
A. p->next->prev=p->               prev;p-          >prev->next=p->prev                  ;free           (p); B.p->next->prev=p->next                        ;p->prev->next=p->next;                           free(p);
C. p->next->prev=p->next                    ;p-      >prev->next=p->prev                 ;free(p);
D. p->next-     >prev=p-    >prev    ;p->     prev->next=p->next;               free(p);

[tag_link]

正确答案：B