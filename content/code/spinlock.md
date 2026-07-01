---
title: "TAS 实现自旋锁"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, spinlock]
difficulty: 2
---

通过 TAS 实现自旋锁的 C 代码

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

int lock = 0; // 初始值表示锁是自由的

// 使用 Test and Set 实现的简单自旋锁
void acquire_lock() {
    while (__sync_lock_test_and_set(&lock, 1) == 1) {
        // 锁被占用，继续自旋等待
    }
}

// 释放自旋锁
void release_lock() {
    __sync_lock_release(&lock);
}

// 线程函数
void *thread_function(void *thread_id) {
    int id = *(int *)thread_id;

    acquire_lock();
    printf("Thread %d acquired the lock.\n", id);

    // 在这里执行临界区代码
    sleep(1);

    release_lock();
    printf("Thread %d released the lock.\n", id);

    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;
    int id1 = 1, id2 = 2;

    // 创建两个线程
    if (pthread_create(&thread1, NULL, thread_function, (void *)&id1) != 0 ||
        pthread_create(&thread2, NULL, thread_function, (void *)&id2) != 0) {
        fprintf(stderr, "Error creating threads.\n");
        return 1;
    }

    // 等待线程结束
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

运行结果

```
Thread 1 acquired the lock.
Thread 2 acquired the lock.
Thread 1 released the lock.
Thread 2 released the lock.
```
