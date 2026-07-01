---
title: "哲学家就餐问题"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, philosopher]
difficulty: 2
---

C 代码实现

```c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NUM_PHILOSOPHERS 5
sem_t forks[NUM_PHILOSOPHERS];

// P(forks[i]) ---> sem_wait(forks[i])
// V(forks[i]) ---> sem_post(forks[i])

void *philosopher(void *num) {
  int id = *(int *)num;

  int first, second;
  if (id < NUM_PHILOSOPHERS - 1) {
    // 对于前面的哲学家，先左后右
    first = id;
    second = (id + 1) % NUM_PHILOSOPHERS;
  } else {
    // 对于最后一个哲学家，先右后左
    first = (id + 1) % NUM_PHILOSOPHERS;
    second = id;
  }
  
  while (1) {
    // 思考
    printf("Philosopher %d is thinking\n", id);
    usleep(100);

    // 获取叉子
    sem_wait(&forks[first]);
    sem_wait(&forks[second]);

    // 吃饭
    printf("Philosopher %d is eating\n", id);
    usleep(100);

    // 释放叉子
    sem_post(&forks[first]);
    sem_post(&forks[second]);
  }
}

int main() {
  pthread_t philosophers[NUM_PHILOSOPHERS];
  int philosophers_numbers[NUM_PHILOSOPHERS];

  for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
    sem_init(&forks[i], 0, 1);
  }

  for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
    philosophers_numbers[i] = i;
    pthread_create(&philosophers[i], NULL, philosopher, &philosophers_numbers[i]);
  }

  for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
    pthread_join(philosophers[i], NULL);
  }

  return 0;
}
```

程序输出

```
Philosopher 3 is thinking
Philosopher 2 is eating
Philosopher 0 is thinking
Philosopher 4 is eating
Philosopher 2 is thinking
Philosopher 1 is eating
Philosopher 4 is thinking
Philosopher 3 is eating
Philosopher 1 is thinking
Philosopher 0 is eating
.....
```
