---
title: "CLOCK 时钟替换算法"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, clock]
difficulty: 2
---

C++ 代码

```cpp
#include <vector>
#include <cstdio>

class ClockReplacer {
public:
  ClockReplacer(int capacity): capacity_(capacity), size_(0), ptr_(0) {
    pages_.resize(capacity, -1);
    refs_.resize(capacity, 0);
  }

  bool IsFull() {
    return size_ == capacity_;
  }

  void Put(int page) {
    // Hit
    // If this page exists in current pages
    for (int i = 0; i < size_; i++) {
      if (pages_[i] == page) {
        refs_[i] = 1;
        Print();
        return;
      }
    }
    // Not Hit
    if (!IsFull()) {
      pages_[ptr_] = page;
      refs_[ptr_] = 1;
      ptr_ = (ptr_ + 1) % capacity_;
      size_++;
    } else {
      while (true) {
        if (refs_[ptr_] == 0) {
          pages_[ptr_] = page;
          refs_[ptr_] = 1;
          ptr_ = (ptr_ + 1) % capacity_;
          break;
        } else {
          refs_[ptr_] = 0;
          ptr_ = (ptr_ + 1) % capacity_;
        }
      }
    }
    Print();
  }

private:
  int capacity_;
  int size_;

  std::vector<int> pages_;
  std::vector<int> refs_;
  int ptr_;

  void Print() {
    for (int i = 0; i < size_; i++) {
      if (i > 0) {
        printf(" ");
      }
      printf("%d:%d", pages_[i], refs_[i]);
    }
    printf("\n");
  }
};

int main() {
  std::vector<int> pages{7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 2};
  ClockReplacer clock(3);
  for (int page : pages) {
    clock.Put(page);
  }
  return 0;
}
```

运行结果：

```
      7:1
      7:1      0:1
 ---> 7:1      0:1      1:1
      2:1 ---> 0:0      1:0
      2:1 ---> 0:1      1:0
 ---> 2:1      0:0      3:1
 ---> 2:1      0:1      3:1
      4:1 ---> 0:0      3:0
      4:1      2:1 ---> 3:0
      4:1      2:1 ---> 3:1
 ---> 4:0      2:0      0:1
 ---> 4:0      2:1      0:1
```
