---
title: "栈"
aliases: ["栈"]
date: 2026-06-25
weight: 7
tags: [栈, 队列]
difficulty: 2
prerequisites: ["线性表定义与基本操作", "线性表概述", "链表", "顺序表"]
subject: data-structure
chapter: 1
chapter_title: "栈"
---

⭐ 中优先级

关于栈直接考查其定义和概念比较少，**更多的是考查应用** ，但是这一节还是 **作为基础** ，需要熟悉下。

### 定义

**栈** 是一个元素的集合，加入元素的操作叫做 **“压栈”（push）** ，而移除元素的操作叫做 **“出栈”（pop）** 。它遵循 **后进先出（LIFO, Last In First Out）** 的原则。 _这意味着最后被压入栈的元素是第一个被弹出的元素_ 。


![](/cc408/images/docs/data-structure/87bc389ec2.svg)

### 基本操作

  * `push(element)`: 将元素添加到 **栈** 的顶部。
  * `pop()`: 移除并返回 **栈顶** 的元素。如果 **栈** 为空，这个操作可能会抛出一个错误或返回特定的值（例如 null 或 undefined），具体取决于实现。
  * `peek()` 或 `top()`: 返回 **栈顶** 的元素但不移除它。这只是一个查看操作，**栈** 的内容不会改变。如果 **栈** 为空，这个操作可能会抛出一个错误或返回特定的值。
  * `isEmpty()`: 判断 **栈** 是否为空。如果 **栈** 为空，返回 **true** ；否则返回 **false** 。
  * `size()` 或 `length()`: 返回 **栈** 中元素的数量。

### 实现

**栈** 的实现方式有两种，**顺序栈** 和 **链式栈** 。  
**顺序栈** 是在 **顺序表** 的基础上实现 **栈结构** ，  
**链式栈** 是在 **链表** 的基础上实现 **栈结构** 。

#### 顺序栈

**顺序栈** 是使用 **数组** 来实现的 **栈** ，利用数组的索引来模拟 **栈** 的操作。  
与普通的线性表不同，**栈** 的操作被限制在表的一端进行，这一端被称为 **栈顶 \(Top\)** ，另一端被称为 **栈底 \(Bottom\)** 。


![](/cc408/images/docs/data-structure/a9c67520fe.svg)

**顺序栈** 的关键在于 **栈顶指针** ，**栈顶指针** 是一个整数变量，用于指示 **栈顶** 元素在 **数组** 中的位置。其值的变化直接反映了栈中元素的变化。

当 **栈空** 时，一般将 **栈顶指针** 设置为 **1** ，当 **栈满** 时，**栈顶指针** 指向 **数组** 中的最后一个元素。

当元素 **入栈** 时，将栈顶指针 **向后** 移动一个位置、然后放置新元素即可。当元素 **出栈** 时，需要将栈顶指针 **向前** 移动一个位置。

当然，入栈需要保证栈不满，出栈需要保证栈不空。

  * 栈的定义

```c
#define MAX_SIZE 100 // 定义栈的最大容量

// 定义顺序栈的结构
typedef struct {
```c
int data[MAX_SIZE]; // 使用数组存储数据
int top;            // 栈顶指针
```

} SeqStack;
```

  * 初始化

```c
// 初始化栈
SeqStack* initStack() {
```c
SeqStack* stack = (SeqStack*)malloc(sizeof(SeqStack));
if(!stack) {
    printf("Failed to allocate memory for stack\n");
    exit(1);
}
// 栈顶指针初始化为 -1，表示栈为空
stack->top = -1; 
return stack;
```

}
```

  * 入栈

```c
// 入栈操作
bool push(SeqStack* stack, int value) {
```c
if (isFull(stack)) {
    printf("Stack is full!\n");
    return false;
}
// 先移动栈顶指针，再存放元素
stack->data[++stack->top] = value;
return true;
```

}
```

  * 出栈

```c
// 出栈操作
bool pop(SeqStack* stack, int* value) {
```c
if (isEmpty(stack)) {
    printf("Stack is empty!\n");
    return false;
}
// 先取出元素，再移动栈顶指针
*value = stack->data[stack->top--];
return true;
```

}
```

  * 获取栈顶元素

```c
// 获取栈顶元素
bool peek(SeqStack* stack, int* value) {
```c
if (isEmpty(stack)) {
    printf("Stack is empty!\n");
    return false;
}
*value = stack->data[stack->top];
return true;
```

}
```

  * 判断栈空

```c
// 判断栈是否为空
// 当栈中没有元素时，栈顶指针通常指向一个特殊的位置，例如 -1。
bool isEmpty(SeqStack* stack) {
```c
return stack->top == -1;
```

}

// 判断栈是否已满
// 当栈顶指针指向数组中的最后一个元素时，说明栈已经满了
bool isFull(SeqStack* stack) {
```c
return stack->top == MAX_SIZE - 1;
```

}
```

#### 链式栈

栈的 **链式存储结构** 利用 **[单链表](/docs/data-structure/ch01-linear-list/linked-list/#%e5%8d%95%e9%93%be%e8%a1%a8%e5%ae%9a%e4%b9%89)** 来实现栈的功能。

![](/cc408/images/docs/data-structure/159403def3.svg)

在 **链式栈** 实现中，一般 **头结点不存放数据** ，仅作为链表的固定起点。栈顶元素始终为 `head->next`。这样依然可以保证 入栈 和 出栈 的时间复杂度为 O\(1\) 。

链式栈具备以下 **重要特性** ：

  * `head` 始终存在，不存储实际数据，只作为哨兵节点。
  * **栈顶元素** 始终位于 `head->next`。
  * **空栈** 时，`head->next == NULL`。
  * 入栈时在 `head->next` 前插入新节点；出栈时删除 `head->next`。
  * 栈的定义

```c
// 定义链式栈的节点结构
typedef struct Node {
int data;
struct Node* next;
} Node;

// 定义链式栈（带头结点）
typedef struct {
Node* head;  // 指向头结点
} LinkedStack;
```

  * 初始化

```c
// 初始化栈（带头结点）
LinkedStack* initStack() {
```c
LinkedStack* stack = (LinkedStack*)malloc(sizeof(LinkedStack));
if (!stack) {
    printf("Failed to allocate memory for stack\n");
    exit(1);
}
stack->head = (Node*)malloc(sizeof(Node)); // 创建头结点
if (!stack->head) {
    printf("Failed to allocate memory for head node\n");
    exit(1);
}
stack->head->next = NULL; // 初始为空栈
return stack;
```

}
```

  * 入栈

```c
// 入栈操作（头插法）
void push(LinkedStack* stack, int value) {
```c
Node* newNode = (Node*)malloc(sizeof(Node));
if (!newNode) {
    printf("Failed to allocate memory for new node\n");
    exit(1);
}
newNode->data = value;
newNode->next = stack->head->next;
stack->head->next = newNode;
```

}
```

  * 出栈

```c
// 出栈操作
bool pop(LinkedStack* stack, int* value) {
```c
if (isEmpty(stack)) {
    printf("Stack is empty!\n");
    return false;
}
Node* topNode = stack->head->next;
*value = topNode->data;
stack->head->next = topNode->next;
free(topNode);
return true;
```

}
```

  * 获取栈顶元素

```c
// 获取栈顶元素
bool peek(LinkedStack* stack, int* value) {
```c
if (isEmpty(stack)) {
    printf("Stack is empty!\n");
    return false;
}
*value = stack->head->next->data;
return true;
```

}
```

  * 判断栈空

```c
// 判断栈是否为空
bool isEmpty(LinkedStack* stack) {
```c
return stack->head->next == NULL;
```

}
```


## 相关笔记

- 线性表定义与基本操作
- 线性表概述
- 链表
- 顺序表
