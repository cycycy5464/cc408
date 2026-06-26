---
title: "快速排序"
date: 2026-06-25
weight: 1
tags: [排序, 分治, 重点]
difficulty: 3
prerequisites:
  - "递归"
  - "二叉树遍历"
subject: data-structure
chapter: 6
chapter_title: "排序"
exam_points:
  - "排序算法比较"
  - "时间复杂度分析"
---

## 概述

快速排序是一种高效的排序算法，采用分治法策略。

## 算法思想

1. 从数组中选择一个元素作为**基准**（pivot）
2. 将所有比基准小的元素放在基准前面，比基准大的放在后面
3. 对基准前后两个子数组递归执行上述过程

## 代码实现

```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

## 复杂度分析

- 时间复杂度：$O(n \log n)$（平均），$O(n^2)$（最坏）
- 空间复杂度：$O(\log n)$（递归栈）
- 稳定性：不稳定排序

## 相关题目

- [2024年408真题 - 选择题第5题](/exam/choice/2024-q5/)
- [2023年408真题 - 应用题第2题](/exam/application/2023-q2/)
