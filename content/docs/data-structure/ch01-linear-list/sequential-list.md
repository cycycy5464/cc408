---
title: "顺序表"
date: 2026-06-25
weight: 5
tags: [线性表]
difficulty: 2
prerequisites: []
subject: data-structure
chapter: 1
chapter_title: "顺序表"
---

🔥 高优先级

关于顺序表，一般不会直接考察本节中介绍的这些操作，因为太简单了。更多的是考察基于顺序表（数组）的 **算法设计** ，但是这些操作是更高级算法设计的基础。

### 顺序表定义

**顺序表（Sequential List）** 是一种常见的数据结构，用于存储一组元素，并按照它们在内存中的物理顺序来排列和访问这些元素。顺序表通常由一个 **数组** 或 **列表** 构成，其中每个元素都占据一个连续的内存位置，并且可以通过索引值来访问。

假设线性表 A 存储的其实位置为 `LOC(A)`，每个元素占用的存储空间的大小为 `sizeof(Elem)`，则 A 所对应的顺序存储结构为：

![](/images/docs/data-structure/69a2847b52.svg)

  * 顺序表 **优点** ：
* **随机访问性强** ：顺序表支持通过索引直接访问元素，访问速度快，时间复杂度为 **_O\(1\)_** 。
* **空间使用连续** ：顺序表中的元素存储在连续的内存块中，这有助于提高缓存的局部性，从而提高访问速度。
* **操作简单** ：无需处理复杂的指针操作。



  * 顺序表 **缺点** ：
* **固定大小或调整大小的开销** ：对于静态数组，大小是固定的，如果预分配的空间不足或过大，会导致内存浪费或数组溢出。动态数组可以重新分配大小，但这会增加时间和空间开销。
* **插入和删除的时间开销** ：如果要在顺序表的中间插入或删除元素，可能需要移动大量的元素，时间复杂度为 **_O\(n\)_** 。




### 操作

#### 数据结构定义


![](/images/docs/data-structure/0b383715a7.svg)

以下代码定义了一个顺序表 `SeqList`，它使用 **固定大小的数组** `data` 来存储元素，`length` 记录当前表的长度。`InitList` 函数初始化顺序表，设置 _长度为 0_ ，表示空表。    
```c
#define MAXSIZE 100
typedef struct {
    ElementType data[MAXSIZE];
    int length;
} SeqList;

void InitList(SeqList *L) {
    L->length = 0;
}
```



​    



#### 插入

![](/images/docs/data-structure/image-20260611231618428.png)

在第 `pos` 个位置 **插入新元素** `e`。首先检查 **插入位置合法性** 和 **空间是否已满** ，然后从尾部向后移动元素，为插入留出位置，最后将元素插入并更新长度。
    
```c
bool Insert(SeqList *L, int pos, ElementType e) {
    if (L->length == MAXSIZE || pos < 1 || pos > L->length + 1) {
        return false;
    }
    for (int i = L->length; i >= pos; i--) {
        L->data[i] = L->data[i - 1];
    }
    L->data[pos - 1] = e;
    L->length++;
    return true;
}
```


#### 删除

![](/images/docs/data-structure/image-20260611231641535.png)

**删除第`pos` 个元素**，并通过指针返回删除的元素值。删除后将该位置后的所有元素 **前移** ，最后更新长度。

```c
bool Delete(SeqList *L, int pos, ElementType *e) {
    if (pos < 1 || pos > L->length) {
        return false;
    }
    *e = L->data[pos - 1];
    for (int i = pos; i < L->length; i++) {
        L->data[i - 1] = L->data[i];
    }
    L->length--;
    return true;
}bool Delete(SeqList *L, int pos, ElementType *e) {

    ![](/images/docs/data-structure/06a5ee8d55.svg)

    *e = L->data[pos - 1];
```



#### 查找操作

在线性表中 **顺序查找** 第一个值等于 `e` 的元素，返回其**逻辑位置** （从 1 开始）；若未找到，返回 0。
```c
int LocateElem(SeqList L, ElementType e) {
    for (int i = 0; i < L.length; i++) {
        if (L.data[i] == e) {
            return i + 1;
        }
    }
    return 0;
}
```


#### 获取元素

**获取顺序表中第`pos` 个元素**，返回值通过指针 `*e` 输出。若位置非法则返回 _false_ 。
    
    
```c
bool GetElem(SeqList L, int pos, ElementType *e) {
    if (pos < 1 || pos > L.length) {
        return false;
    }
    *e = L.data[pos - 1];
    return true;
}
```



#### 判空

**判断顺序表是否为空** ，直接判断 `length` 是否为 _0_ 。
    
    
```c
bool IsEmpty(SeqList L) {
    return L.length == 0;
}
```



#### 清空

**清空顺序表** ，只需将 `length` _置 0_ ，无需实际删除元素，等价于逻辑上的清空。
    
    
```c
void ClearList(SeqList *L) {
    L->length = 0;
}
```



#### 长度

**返回当前顺序表的长度** ，即有效元素个数。
    
    
```c
int Length(SeqList L) {
    return L.length;
}
```
