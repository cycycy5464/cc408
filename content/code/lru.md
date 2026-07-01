---
title: "LRU 算法"
date: 2026-07-01
type: code
subject: os
tags: [算法, C语言, lru]
difficulty: 2
---

C++ 代码实现

```cpp
#include <vector>
#include <cstdio>
#include <unordered_map>

struct ListNode {
  ListNode *prev;
  ListNode *next;
  int val;

  ListNode() = default;
  ListNode(int v): val(v) {}
};

class LRUReplacer {
public:
  LRUReplacer(int capacity): capacity_(capacity), size_(0) {
    head_ = new ListNode();
    tail_ = new ListNode();
    tail_->next = head_;
    head_->prev = tail_;
  }

  ~LRUReplacer() {
    while (!IsEmpty()) {
      RemoveFromHead();
    }
    delete head_;
    delete tail_;
  }

  bool IsEmpty() {
    return size_ == 0 && tail_->next == head_ && head_->prev == tail_;
  }

  bool IsFull() {
    return size_ == capacity_;
  }

  void Add(int page) {
    printf("add %d, ", page);
    // hit
    if (ht_.count(page)) {
      printf("    hit, ");
      ListNode *n = ht_[page];
      RemoveNode(n);
      AddToTail(n);
      Print();
      return;
    }
    // not hit
    printf("not hit, ");
    ListNode *n = new ListNode(page);
    if (size_ < capacity_) {
      AddToTail(n);
      ht_[page] = n;
    } else {
      RemoveFromHead();
      AddToTail(n);
    }
    Print();
  }

private:
  int capacity_;
  int size_;
  ListNode *tail_;
  ListNode *head_;
  std::unordered_map<int, ListNode *> ht_;

  void AddToTail(ListNode *n) {
    ListNode *temp = tail_->next;
    n->next = temp;
    temp->prev = n;
    tail_->next = n;
    n->prev = tail_;
    size_++;
  }

  void RemoveFromHead() {
    ListNode *temp1 = head_->prev;
    ListNode *temp2 = temp1->prev;
    temp2->next = head_;
    head_->prev = temp2;
    ht_.erase(temp1->val);
    delete temp1;
    size_--;
  }

  void RemoveNode(ListNode *n) {
    ListNode *temp1 = n->prev;
    ListNode *temp2 = n->next;
    temp1->next = temp2;
    temp2->prev = temp1;
    size_--;
  }

  void Print() {
    printf("size: %d, pages: ", size_);
    for (ListNode *n = head_->prev; n != tail_; n = n->prev) {
      printf("%d ", n->val);
    }
    printf("\n");
  }
};

int main() {
  std::vector<int> pages{7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 2};
  LRUReplacer lru(3);
  for (int page : pages) {
    lru.Add(page);
  }
}
```

运行结果：

```
add 7, not hit, size: 1, pages: 7 
add 0, not hit, size: 2, pages: 7 0 
add 1, not hit, size: 3, pages: 7 0 1 
add 2, not hit, size: 3, pages: 0 1 2 
add 0,     hit, size: 3, pages: 1 2 0 
add 3, not hit, size: 3, pages: 2 0 3 
add 0,     hit, size: 3, pages: 2 3 0 
add 4, not hit, size: 3, pages: 3 0 4 
add 2, not hit, size: 3, pages: 0 4 2 
add 3, not hit, size: 3, pages: 4 2 3 
add 0, not hit, size: 3, pages: 2 3 0 
add 2, not hit, size: 3, pages: 3 0 2
```
