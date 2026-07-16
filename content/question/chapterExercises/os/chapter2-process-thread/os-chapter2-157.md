---
title: "进程与线程 第8题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "操作系统"
knowledge_points:
  - "同步与互斥"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 157
tags: ['课后题']
---

假设有两个线程(编号为0和1)需要去访问同一个共享资源，为避免竞争状态的问题， 我们必须实现一种互斥机制，使得在任何时候只能有一个线程访问这个资源。假设有如
下一段代码：bool                flag[2];                           //flag      数组，初始化为 FALSEEnter_Critical_Section(int                        my_thread_id,int                        other_thread_id){while(flag[other_thread_id]==TRUE);                                  //空循环语句flag[my_thread_id]=TRUE;Exit_Critical_Section(int                my_thread_id,int                 other_thread_id){ flag[my_thread_id]=FALSE;
下一段代码：
bool                flag[2];                           //flag      数组，初始化为 FALSE
Enter_Critical_Section(int                        my_thread_id,int                        other_thread_id){
while(flag[other_thread_id]==TRUE);                                  //空循环语句
flag[my_thread_id]=TRUE;
Exit_Critical_Section(int                my_thread_id,int                 other_thread_id){ flag[my_thread_id]=FALSE;
当一个线程想要访问临界资源时，就调用上述的这两个函数。例如，线程0的代码可能 是这样的：
Enter_Critical_Section(0,1); 使用这个资源；Exit_Critical_Section(0,1); 做其他的事情；
Enter_Critical_Section(0,1); 使用这个资源；
Exit_Critical_Section(0,1); 做其他的事情；
试问：
1)以上的这种机制能够实现资源互斥访问吗?为什么?
2)若把Enter_Critical_Section()函数中的两条语句互换位置，可能发生死锁吗?

[tag_link]

【解答】