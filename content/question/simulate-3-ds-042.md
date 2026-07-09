---
title: "模拟卷3 数据结构 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 42
---

（13 分）假设二叉树采用二叉链表存储结构存储，设计一个算法，求先序遍历序列中第 k（1≤k≤二叉树中结点个数）个结点的值，要求： （1）给出算法的基本设计思想。 （2）写出二叉树采用的存储结构代码。 （3）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

[tag_link]

【答案】 （1）算法的基本设计思想： 采用递归先序遍历二叉树，设置一个计数器记录已访问的结点数。遍历时，每访问一个结点，计数器加 1。当计数器等于 k 时，当前结点即为所求，记录其值并终止遍历；若计数器小于 k，则继续递归遍历左子树和右子树。通过递归和计数器控制，可在找到第 k 个结点后提前结束遍历，提高效率。 （2）二叉树采用的存储结构代码： // 二叉链表存储结构 typedef struct BiTNode { int data ; // 结点数据域，假设为整型 struct BiTNode * lchild ; // 左孩子指针 struct BiTNode * rchild ; // 右孩子指针 } BiTNode , * BiTree ; （3）算法描述（C++ 语言）： // 辅助递归函数：在先序遍历中查找第 k 个结点 // 参数：node-当前结点指针，k-目标序号，count-计数器（引用传递），result-存储结果（引用传递），found-是否找到标志（引用传递） void PreOrderKthHelper ( BiTree node , int k , int & count , int & result , bool & found ) { if ( node == nullptr || found ) { return ; // 结点为空或已找到目标，直接返回 } count ++ ; // 访问当前结点，计数器加 1 if ( count == k ) { result = node -&gt; data ; // 找到第 k 个结点，记录其值 found = true ; // 设置找到标志，提前终止遍历 return ; } PreOrderKthHelper ( node -&gt; lchild , k , count , result , found ); // 递归遍历左子树 PreOrderKthHelper ( node -&gt; rchild , k , count , result , found ); // 递归遍历右子树 } // 主函数：求先序遍历中第 k 个结点的值 // 参数：root-二叉树根节点指针，k-要查找的序号（1≤k≤结点总数） // 返回值：第 k 个结点的值，如果 k 无效或未找到，返回 -1（假设结点值非负） int PreOrderKth ( BiTree root , int k ) { int count = 0 ; // 计数器，初始化为 0 int result = - 1 ; // 存储结果，初始化为 -1 表示未找到 bool found = false ; // 标志位，初始为 false PreOrderKthHelper ( root , k , count , result , found ); return result ; // 返回结果 } 【解析】 算法基于递归先序遍历实现，先序遍历顺序为根结点、左子树、右子树。通过计数器 count 记录访问结点的次序，当 count 等于 k 时，当前结点即为所求。使用引用参数传递 count、result 和 found，使得递归过程中能共享和修改这些变量，并通过 found 标志提前终止遍历，避免不必要的递归调用。 二叉链表存储结构是二叉树常用的链式存储方式，每个结点包含数据域和指向左右子树的指针，便于动态管理二叉树。 算法的时间复杂度为 O(n)，其中 n 为二叉树结点数，最坏情况下需遍历所有结点（当 k 大于结点总数或为最后一个结点时），但平均情况下若 k 较小可提前结束。空间复杂度为 O(h)，h 为二叉树高度，主要由递归栈空间占用。算法简洁高效，符合先序遍历特性。 43 （12 分）已知 32 位寄存器中存放的变量 x 的机器码为 C000004H，请问： （1）当 x 是无符号整数时： x 的真值是多少？ x/2 的真值是多少？ x/2 存放在 R1 中的机器码是什么？ 2x 的真值是多少？ 2x 存放在 R1 中的机器码是什么？ （2）当 x 是带符号整数（补码）时： x 的真值是多少？ x/2 的真值是多少？ x/2 存放在 R1 中的机器码是什么？ 2x 的真值是多少？ 2x 存放在 R1 中的机器码是什么？ （3）当 x 是 float 型浮点数时： x 的真值是多少？ x/2 的真值是多少？ x/2 存放在 R1 中的机器码是什么？ 2x 的真值是多少？ 2x 存放在 R1 中的机器码是什么？ 查看答案与解析 收藏

---

