---
title: "模拟卷8 数据结构 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 8
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 42
---

单链表有环，是指单链表的最后一个结点的指针指向了链表中的某个结点（通常单链表的最后一个结点的指针域是为空的）。试编写算法判断单链表是否存在环。 （1）给出算法的基本设计思想。 （2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。 （3）说明你所设计算法的时间复杂度和空间复杂度。

[tag_link]

【答案】 （1）基本设计思想：采用快慢指针法（Floyd 判圈算法）。设置两个指针，慢指针每次移动一步，快指针每次移动两步。如果链表中存在环，快指针最终会追上慢指针并相遇；如果不存在环，快指针会首先到达链表尾部（即指向 NULL）。 （2）算法描述（C++）： struct ListNode { int val ; ListNode * next ; ListNode ( int x ) : val ( x ), next ( NULL ) {} }; bool hasCycle ( ListNode * head ) { if ( head == NULL || head -&gt; next == NULL ) { return false ; // 空链表或只有一个节点且无环 } ListNode * slow = head ; ListNode * fast = head ; while ( fast != NULL && fast -&gt; next != NULL ) { slow = slow -&gt; next ; // 慢指针移动一步 fast = fast -&gt; next -&gt; next ; // 快指针移动两步 if ( slow == fast ) { return true ; // 相遇，说明有环 } } return false ; // 快指针到达尾部，说明无环 } （3）时间复杂度：O(n)，其中 n 为链表节点数。在最坏情况下，需要遍历整个链表一次或两次。空间复杂度：O(1)，仅使用了两个额外指针。 【解析】 该算法的核心是快慢指针的追逐原理。如果链表有环，快指针每次比慢指针多移动一步，两者在环内的相对距离每次减少一步，因此必然会在有限步内相遇；如果链表无环，快指针将先到达链表尾部（即遇到 NULL）。时间复杂度为 O(n)，因为每个节点最多被访问两次（快指针可能遍历两次）；空间复杂度为 O(1)，因为只使用了常数级别的额外空间。这种方法是判断链表是否存在环的最优解之一，既高效又节省内存。 43 （10 分）设某机中，CPU 的地址总线 A₁₅～A₀，数据总线 D₇～D₀（A₀、D₀为最低位），存储器地址空间为 3000H～67FFH。其中 3000H～4FFFH 为 ROM 区，选用 4K×2 的 ROM 芯片；5000H～67FFH 为 RAM 区，选用 2K×4 的 SRAM 芯片。请问： （1）组成该存储器需要多少片 ROM 芯片和 SRAM 芯片？ （2）ROM 芯片、SRAM 芯片各需连接 CPU 的哪几根地址线和数据线？ （3）应如何设置片选信号，分别写出各片选信号的逻辑表达式。 查看答案与解析 收藏

---

