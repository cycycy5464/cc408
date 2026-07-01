---
title: "生产者消费者问题"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, producer_consumer]
difficulty: 2
---

C 代码实现

```c
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <stdio.h>

#define N 5

pthread_mutex_t mutex;
sem_t empty;
sem_t full;

void *producer() {
  while (1) {
    sem_wait(&empty);
    pthread_mutex_lock(&mutex);
    printf("producer put item into buffer ...\n");
    pthread_mutex_unlock(&mutex);
    sem_post(&full);
  }
}

void *consumer() {
  while (1) {
    sem_wait(&full);
    pthread_mutex_lock(&mutex);
    printf("consumer get item from buffer ...\n");
    pthread_mutex_unlock(&mutex);
    sem_post(&empty);
  }
}

int main() {
  pthread_t p, c;

  pthread_mutex_init(&mutex, NULL);
  sem_init(&empty, 0, N);
  sem_init(&full, 0, 0);

  pthread_create(&p, NULL, producer, NULL);
  pthread_create(&c, NULL, consumer, NULL);

  pthread_join(p, NULL);
  pthread_join(c, NULL);

  return 0;
}
```

执行结果

```
producer put item into buffer ...
consumer get item from buffer ...
consumer get item from buffer ...
producer put item into buffer ...
producer put item into buffer ...
consumer get item from buffer ...
consumer get item from buffer ...
producer put item into buffer ...
producer put item into buffer ...
consumer get item from buffer ...
....
```
