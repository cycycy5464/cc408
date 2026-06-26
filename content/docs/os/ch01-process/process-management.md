---
title: "进程管理"
date: 2026-06-25
weight: 1
tags: [进程, 线程, 同步]
difficulty: 3
prerequisites: []
subject: os
chapter: 1
chapter_title: "操作系统概述"
exam_points:
  - "进程与线程"
  - "进程同步与通信"
  - "死锁"
---

## 进程的概念

进程是程序的一次执行过程，是操作系统进行资源分配的基本单位。

### 进程的状态

```
┌─────────┐    创建     ┌─────────┐
│  空白态  │ ──────────→ │  就绪态  │
│         │ ←────────── │         │
└─────────┘    终止     └─────────┘
                    ↑    ↓
              ┌─────────┐  中断   ┌─────────┐
              │  阻塞态  │ ←────── │  运行态  │
              └─────────┘         └─────────┘
```

### PCB（进程控制块）

```c
typedef struct {
    int pid;              // 进程ID
    int state;            // 进程状态
    int priority;         // 优先级
    void *stack_ptr;      // 栈指针
    struct pcb *next;     // 下一PCB指针
} PCB;
```

## 进程调度算法

### FCFS（先来先服务）

非抢占式，按到达顺序调度。对短作业不公平。

### SJF（短作业优先）

按运行时间排序，短作业优先。最优平均等待时间，但难以预测运行时间。

### 时间片轮转（RR）

```c
void RoundRobin(ProcessQueue *ready, int quantum) {
    while (!isEmpty(ready)) {
        Process *p = dequeue(ready);
        p->state = RUNNING;
        p->remaining_time -= quantum;
        
        if (p->remaining_time <= 0) {
            p->state = TERMINATED;
        } else {
            p->state = READY;
            enqueue(ready, p);
        }
    }
}
```

## 进程同步

### 信号量机制

```c
// P操作（wait）
void wait(int *s) {
    (*s)--;
    if (*s < 0) block();
}

// V操作（signal）
void signal(int *s) {
    (*s)++;
    if (*s <= 0) wakeup();
}
```

### 生产者-消费者问题

```c
semaphore empty = n;    // 空缓冲区数量
semaphore full = 0;     // 满缓冲区数量
semaphore mutex = 1;    // 互斥信号量

// 生产者
void producer() {
    while (1) {
        produce();
        wait(&empty);
        wait(&mutex);
        add_to_buffer();
        signal(&mutex);
        signal(&full);
    }
}

// 消费者
void consumer() {
    while (1) {
        wait(&full);
        wait(&mutex);
        remove_from_buffer();
        signal(&mutex);
        signal(&empty);
        consume();
    }
}
```

## 死锁

### 产生条件

1. 互斥条件
2. 请求与保持条件
3. 不剥夺条件
4. 循环等待条件

### 死锁预防

破坏四个必要条件之一即可。
