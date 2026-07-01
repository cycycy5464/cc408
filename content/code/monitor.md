---
title: "管程实现生产者消费者"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, monitor]
difficulty: 2
---

考虑一个经典的并发问题：生产者 - 消费者问题。你有一个共享缓冲区和两组线程，生产者在缓冲区中放入数据，而消费者从缓冲区中取出数据。

```
Monitor ProducerConsumerMonitor {
    BufferType buffer; // 假设这是一个有限的队列或数组
    Condition full;
    Condition empty;
    
    procedure produce(item) {
        if (buffer.isFull()) {
            wait(full);
        }
        buffer.add(item);
        signal(empty);
    }
    
    procedure consume() {
        if (buffer.isEmpty()) {
            wait(empty);
        }
        Item item = buffer.remove();
        signal(full);
        return item;
    }
}
```

管程在这里就是将生产者消费者需要的逻辑封装成了`produce`和`consume`这两个函数，其内部依然使用了更低级的同步原语（这里是条件变量，也可以使用信号量实现这个逻辑），并且定义了缓冲区`buffer`。
