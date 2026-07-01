---
title: "银行家算法"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, banker]
difficulty: 2
---

C 代码

```c
#include <stdio.h>

#define MAX_PROCESSES 5
#define MAX_RESOURCES 3

int total[MAX_RESOURCES] = {17, 7, 12};
int available[MAX_RESOURCES] = {10, 5, 7};

int maximum[MAX_PROCESSES][MAX_RESOURCES] = {
  {7, 5, 3},
  {3, 2, 2},
  {9, 0, 2},
  {2, 2, 2},
  {4, 3, 3}
};

int allocation[MAX_PROCESSES][MAX_RESOURCES] = {
  {0, 1, 0},
  {2, 0, 0},
  {3, 0, 2},
  {2, 1, 1},
  {0, 0, 2}
};

int need[MAX_PROCESSES][MAX_RESOURCES] = {
  {7, 4, 3},
  {1, 2, 2},
  {6, 0, 0},
  {0, 1, 1},
  {4, 3, 1}
};

// 检查是否可以分配资源
int isSafe(int process, int request[]);
// 检查系统是否处于安全状态
int isSafeState();

int isSafe(int process, int request[]) {
  // 检查请求是否超过最大需求
  for (int i = 0; i < MAX_RESOURCES; i++) {
    if (request[i] > need[process][i]) {
      printf("Error: Request exceeds maximum demand.\n");
      return 0;
    }
  }

  // 检查请求是否超过可用资源
  for (int i = 0; i < MAX_RESOURCES; i++) {
    if (request[i] > available[i]) {
      printf("Process %d must wait, not enough resources.\n", process);
      return 0;
    }
  }

  // 尝试分配资源
  for (int i = 0; i < MAX_RESOURCES; i++) {
    available[i] -= request[i];
    allocation[process][i] += request[i];
    need[process][i] -= request[i];
  }

  // 检查分配后系统是否安全
  if (isSafeState()) {
    printf("Request granted. System is still in safe state.\n");
    return 1;
  } else {
    // 回滚分配
    for (int i = 0; i < MAX_RESOURCES; i++) {
      available[i] += request[i];
      allocation[process][i] -= request[i];
      need[process][i] += request[i];
    }

    printf("Request denied. Granting the request would result in an unsafe state.\n");
    return 0;
  }
}

// 检查系统是否处于安全状态
int isSafeState() {
  int work[MAX_RESOURCES];
  int finish[MAX_PROCESSES] = {0};

  // 初始化工作向量
  for (int i = 0; i < MAX_RESOURCES; i++) {
    work[i] = available[i];
  }

  // 找到一个可分配的进程
  int count = 0;
  while (count < MAX_PROCESSES) {
    int found = 0;
    for (int i = 0; i < MAX_PROCESSES; i++) {
      if (!finish[i]) {
        int j;
        for (j = 0; j < MAX_RESOURCES; j++) {
          if (need[i][j] > work[j]) {
            break;
          }
        }
        if (j == MAX_RESOURCES) {
          // 进程 i 可以完成
          for (int k = 0; k < MAX_RESOURCES; k++) {
            work[k] += allocation[i][k];
          }
          finish[i] = 1;
          found = 1;
          count++;
        }
      }
    }
    if (!found) {
      // 没有找到可分配的进程，系统处于不安全状态
      return 0;
    }
  }

  // 所有进程都能完成，系统处于安全状态
  return 1;
}

int main() {
  // 尝试分配资源
  int process = 1;
  int request[] = {1, 0, 2};
  isSafe(process, request);

  return 0;
}
```
