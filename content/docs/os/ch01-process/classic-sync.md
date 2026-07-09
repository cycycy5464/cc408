---
title: "经典同步问题"
aliases: ["经典同步问题"]
date: 2026-06-25
weight: 8
tags: [进程管理]
difficulty: 1
prerequisites: ["计算机系统概述", "操作系统概念", "操作系统结构", "程序运行环境"]
subject: os
chapter: 1
chapter_title: "经典同步问题"
---

🔥 高优先级

**同步问题设计** 是操作系统解答题必考题，本节的几个经典问题虽然不会直接考察，但是其中的设计思想还是需要深入掌握。

### 生产者消费者问题

**Producer**


![](/images/docs/os/aa1263419a.svg)





**Consumer**


生产者消费者问题是并发编程中的经典问题，涉及到两种线程 —— **生产者** 和 **消费者** ，它们共享一个固定大小的缓冲区或存储区。

  * 生产者的任务是生成数据并将其 **放入缓冲区** 。
  * 消费者的任务是 **从缓冲区中取出** 并消费这些数据。

关键的挑战在于确保生产者不会在缓冲区满时添加数据，同时确保消费者不会在缓冲区空时尝试消费数据。
    
    
semaphore mutex = 1;          // 临界区互斥信号量
semaphore empty = n;          // 空闲缓冲区数量
semaphore full  = 0;          // 忙缓冲区数量

        P(empty)              // 等待一个空位置
        P(mutex)              // 进入临界区前先获取mutex
        ....                  // 将数据项添加到缓冲区
        V(mutex)              // 离开临界区，释放mutex
        V(full)               // 增加一个数据项的计数

        P(full)               // 等待一个数据项
        P(mutex)              // 进入临界区前先获取mutex
        ...                  // 从缓冲区取出数据项并消费
        V(mutex)              // 离开临界区，释放mutex
        V(empty)              // 增加一个空位置的计数





生产者消费者过程可以参考以下流程图理解：

![](/images/docs/os/3b8c075a6a.svg)

### 读者 - 写者问题


![](/images/docs/os/image-20260611221433589.png)





**可以多个读者一起读，**

**但是此时写者不能写**

**系统一个时刻最多允许一个写者在写，**

**并且此时其他读者和写者都不允许操作**

**读者写者问题** 是另一个经典的并发编程问题，涉及到对 **共享数据** 或 **资源** 的访问，这些 **资源** 可以被 **多个读者** 同时读取，但只能被 **一个写者** 写入，而且当 **写者** 正在写入数据时，没有其他 **读者** 或 **写者** 可以访问该 **资源** 。

这个问题的挑战在于两点：

* 允许多个读者同时读取资源。
* 确保当有一个写者访问资源时，没有其他读者或写者可以同时访问。
* 读者优先

```c
int read_count = 0;
semaphore wrt  = 1;
semphore mutex = 1;

reader() {
```c
while (1) {
    P(mutex)                     // 获取互斥访问权，以修改 read_count
    read_count += 1
    if (read_count == 1) {       // 如果这是第一个读者，需要锁定资源，防止写者写入
        P(wrt)
    }
    V(mutex)                     // 释放互斥访问权
    ...                          // 读取资源
    P(mutex)                     // 获取互斥访问权，以修改 read_count
    read_count -= 1
    if (read_count == 0) {       // 如果没有读者在读取，释放资源，允许写者写入
        V(wrt)
    }
    V(mutex)                     // 释放互斥访问权
}
```

}

writer() {
```c
while (1) {
    P(wrt)                       // 获取资源的互斥访问权
    ...                          // 写入资源
    V(wrt)                       // 释放资源的互斥访问权
}
```

}
```

* 写者优先

```c
int read_count = 0;
int write_count = 0;
semaphore wrt = 1;
semaphore mutex = 1;
semaphore write_mutex = 1;

reader() {
```c
while (1) {
    P(write_mutex)                  // 在读取之前，确保没有写者正在等待或写入
    P(mutex)                        // 获取互斥访问权，以修改 read_count
    read_count += 1
    if (read_count == 1) {
        P(wrt)
    }
    V(mutex)
    V(write_mutex)
```


```c
    ...                             // 读取资源
```


```c
    P(mutex)                        // 获取互斥访问权，以修改read_count
    read_count -= 1
    if (read_count == 0) {
        V(wrt)
    }
    V(mutex)
}
```

}

writer() {
```c
while (1) {
    P(write_mutex)                  // 获取互斥访问权，以修改 write_count
    write_count += 1
    if (write_count == 1) {         // 如果这是第一个写者，锁定资源，防止新的读者读取
        P(wrt)
    }
    V(write_mutex)
```


```c
    ...                             // 写入资源
```


```c
    P(write_mutex)                  // 获取互斥访问权，以修改write_count
    write_count -= 1
    if (write_count == 0) {         // 如果没有其他写者在等待或写入，释放资源
        V(wrt)
    }
    V(write_mutex)
}
```

}
```

* 公平算法

```c
 ```c
 int read_count = 0;
 int write_count = 0;
 semaphore wrt = 1;
 semaphore mutex = 1;
 semaphore queue = 1; // 新增队列信号量，以确保公平性
 
 reader() {
     while (1) {
         P(queue);                 // 进入队列
         P(mutex);                 // 获取互斥访问权，以修改 read_count
         read_count += 1;
         if (read_count == 1) {
             P(wrt);               // 如果是第一个读者，锁定资源
         }
         V(mutex);
         V(queue);                 // 离开队列
         ...                       // 读取资源
         P(mutex);                 // 获取互斥访问权，以修改 read_count
         read_count -= 1;
         if (read_count == 0) {
             V(wrt);               // 如果是最后一个读者，释放资源
         }
         V(mutex);
     }
 }
 
 writer() {
     while (1) {
         P(queue);                 // 进入队列
         P(wrt);                   // 锁定资源
         ...                       // 写入资源
         V(wrt);                   // 释放资源
         V(queue);                 // 离开队列
     }
 }
 ```
```


试题中如果考察读者写者问题的话，一般考察的还是读者优先，读者优先的同步实现方案可以通过以下流程图进行理解：

![](/images/docs/os/a025a153ee.svg)

### 哲学家就餐问题

![](/images/docs/os/image-20260611221716758.png)

假设有五位 **哲学家** 坐在一个 **圆桌** 周围，每两位哲学家之间有一把 **叉子** 。哲学家的生活由 **思考和吃饭** 两种活动组成。为了吃饭，一个哲学家需要两把叉子——左边和右边的一把。问题在于，如何设计一个算法使得哲学家们可以正常就餐，而不会因为竞争叉子而导致死锁或饥饿。

哲学家就餐问题有多种解法，这里只提供一种 **最直观的解法** ，对于包含 **N** 位哲学家的问题：- **前 N-1** 个哲学家先拿起 **左边的叉子** ，再拿起 **右边的叉子** \- **最后一个** 哲学家先拿起 **右边的叉子** ，再拿起 **左边的叉子**
    
    
```c
semaphore fork[5] = {1, 1, 1, 1, 1};      // 五个叉子，初始都是可用的

void philosopher(int i) {
    if (i < 5) {
        // 对于前面的哲学家，先左后右
        first = i;
        second = (i + 1) % 5;
    } else {
        // 对于最后一个哲学家，先右后左
        first = (i + 1) % 5;
        second = i;
    }
    while (1) {
        think();
        P(fork[first]);
        P(fork[second]);
        eat();
        V(fork[first]);
        V(fork[second]);
    }
}
```



哲学家就餐过程可以参考以下流程图理解：

![](/images/docs/os/image-20260611221818129.png)

![](/images/docs/os/image-20260611221830941.png)


## 相关笔记

- [[computer-overview|计算机系统概述]]
- [[os-concept|操作系统概念]]
- [[os-structure|操作系统结构]]
- [[program-env|程序运行环境]]
