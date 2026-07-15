---
title: "数组查找"
aliases: ["数组查找"]
date: 2026-06-25
weight: 23
tags: [查找, 哈希]
difficulty: 3
prerequisites: ["图的算法和应用", "图的定义", "图概述"]
subject: data-structure
chapter: 3
chapter_title: "数组查找"
---

⭐ 中优先级

在选择题中偶会考查，内容也不算难，关键在于掌握算法思想，也许会在算法设计题中间接考察到。

### 顺序查找

顺序查找的 **核心思想** 是从数组（线性表）的第一个元素开始，逐个检查每个元素是否等于目标值，直到找到目标或检查完整个数组。

其代码实现如下，非常简单，遍历一次数组即可：

```c
int SequentialSearch(int A[], int n, int value) {
    for (int i = 0; i < n; i++) {
        if (A[i] == value) {
            return i;  // 找到，返回索引
        }
    }
    return -1;  // 未找到
}
```



顺序查找的 **时间复杂度** 如下：

  * **最好情况** ： O\(1\)
  * **最坏情况** ： O\(n\)
  * **平均情况** ： O\(n\)

### 折半查找

折半查找 **要求数组是有序的** 。

其 **核心思想** 在于每次将查找范围折半，只保留目标可能存在的一半，直到范围为空或找到目标为止。

例如，在有序数组中查找一个元素时，可以先比较中间元素：

  * 如果目标值小于中间值，查左半部分；
  * 如果目标值大于中间值，查右半部分；
  * 如果相等，则查找成功。

下图给出了一个实例，从数组中折半查找元素 23：


![](/cc408/images/docs/data-structure/image-20260612141452857.png)

折半查找可以基于 **迭代实现** ，也可以作为一个 **递归函数实现** ：

  * 迭代版

```c
int BinarySearch(int A[], int n, int value) {
```c
int low = 0;
int high = n - 1;
```


```c
while (low <= high) {
    int mid = low + (high - low) / 2;  // 防止溢出
```


```c
    if (A[mid] == value) {
        return mid;  // 找到
    } else if (A[mid] < value) {
        low = mid + 1;
    } else {
        high = mid - 1;
    }
}
```


```c
return -1;  // 未找到
```

}
```

  * 递归版

```c
```c
int BinarySearchRecursive(int A[], int low, int high, int value) {
    if (low > high) {
        return -1;  // 区间无效，查找失败
    }

    int mid = low + (high - low) / 2;

    if (A[mid] == value) {
        return mid;  // 找到目标
    } else if (A[mid] < value) {
        return BinarySearchRecursive(A, mid + 1, high, value);  // 查右半部分
    } else {
        return BinarySearchRecursive(A, low, mid - 1, value);   // 查左半部分
    }
}
```
```


折半查找的 **时间复杂度** 如下：

  * **最好情况** ： O\(1\)
  * **最坏情况** ： O\(log2​n\)
  * **平均情况** ： O\(log2​n\)

#### 折半查找判定树

折半查找判定树（Binary Search Decision Tree）是折半查找（Binary Search）过程的树形表示，用于清晰地 **描述在查找过程中所做的每一次比较决策** 。

所以简单地来说，如何根据一个有序序列得到一个折半查找判定树呢，就是将折半查找的过程走一遍，举两个实际的例子来说明一下：

假设数组为 `[10, 20, 30, 40, 50, 60]`，元素个数为 6。

🌳 **折半查找判定树构造原则**

折半查找需要选一个“中点”作为根节点。偶数长度数组有两个中点，一般可以：

  * 选靠左的那个（常见做法）：`mid = (low + high) // 2`
  * 或者选靠右的那个

假设按 **常规左中点** 来构造，则 **构造过程如下** ：

  1. `[10, 20, 30, 40, 50, 60]`，`mid = 2` → 30 为根；

  2. 左边 `[10, 20]`，`mid = 0` → 10 为左子树；

* 右边是 `[20]` → 作为 10 的右子节点；



  3. 右边 `[40, 50, 60]`，`mid = 4` → 50 为右子树；

* 左边 `[40]` → 左子节点；
 * 右边 `[60]` → 右子节点。




最后可以得到如下折半查找判定树：

![](/cc408/images/docs/data-structure/image-20260612141532987.png)

### 分块查找

线性表的 **分块查找** 通常应用于一种特定的情境：线性表（例如数组）被分为多个大小相等（或者最后一个块可能较小）的块，并且块内的元素是无序的，但是块与块之间是有序的。也就是说，每个块内的最大（或最小）元素小于下一个块的任意元素。

常用的 **分块查找策略** 如下：

  1. 先对块索引进行顺序或二分查找以确定所需元素可能所在的块。
  2. 然后在确定的块中进行顺序查找。

**Index Table**


![](/cc408/images/docs/data-structure/image-20260612141548244.png)


## 相关笔记

- [[algorithms|图的算法和应用]]
- [[definition|图的定义]]
- [[graph-index|图概述]]
