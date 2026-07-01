---
title: "读者写着问题"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, reader_writer]
difficulty: 2
---

C 代码实现

```c
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <stdio.h>

int reader_count = 0;
pthread_mutex_t ownership;
pthread_mutex_t mutex;

void *reader_routine(void *num) {
  int id = *(int *)num;
  while (1) {
    pthread_mutex_lock(&mutex);
    if (reader_count == 0) {
      pthread_mutex_lock(&ownership);
    }
    reader_count++;
    pthread_mutex_unlock(&mutex);

    printf("Reader %d is reading ...\n", id);
    usleep(300);

    pthread_mutex_lock(&mutex);
    reader_count--;
    if (reader_count == 0) {
      pthread_mutex_unlock(&ownership);
    }
    pthread_mutex_unlock(&mutex);

    usleep(100);
  }
}

void *writer_routine() {
  while (1) {
    pthread_mutex_lock(&ownership);
    printf("Writer is writing ...\n");
    usleep(500);
    pthread_mutex_unlock(&ownership);

    usleep(100);
  }
}

int main() {
  pthread_t readers[3];
  int reader_ids[3] = {0, 1, 2};
  pthread_t writer;

  pthread_mutex_init(&ownership, NULL);

  pthread_create(&writer, NULL, writer_routine, NULL);
  for (int i = 0; i < 3; i++) {
    pthread_create(&readers[i], NULL, reader_routine, (void *)&reader_ids[i]);
  }

  pthread_join(writer, NULL);
  for (int i = 0; i < 3; i++) {
    pthread_join(readers[i], NULL);
  }

  return 0;
}
```

运行结果

```
Reader 0 is reading ...
Reader 2 is reading ...
Reader 1 is reading ...
Writer is writing ...
Reader 0 is reading ...
Reader 2 is reading ...
Reader 1 is reading ...
Writer is writing ...
....
```
