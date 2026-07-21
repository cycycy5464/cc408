---
title: "模拟卷5 数据结构 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "数据结构"
knowledge_points:
  - "复杂度分析"
  - "链表"
question_type: "comprehensive"
difficulty: 4
number: 42

---

（12 分）假设二叉树采用二叉链表存储结构，设计一个算法求其指定的某一层 k （ k > 1 ）的叶子结点个数，要求：

（1）给出算法的基本设计思想。

（2）写出二叉树采用的存储结构代码。

（3）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

[复杂度分析](/study_methods/tags/408quiz//#%e5%a4%8d%e6%9d%82%e5%ba%a6%e5%88%86%e6%9e%90)
[链表](/study_methods/tags/408quiz//#%e9%93%be%e8%a1%a8)

[tag_link]

【答案】

（1）算法的基本设计思想：采用递归先序遍历二叉树，遍历时记录当前节点所在层数。若当前层数等于指定层数 k ，则判断该节点是否为叶子结点（左右孩子均为空），若是则计数器加 1；若当前层数小于 k ，则递归遍历其左右子树；若当前层数大于 k ，则停止向下递归。最终累计得到第 k 层的叶子结点个数。

（2）二叉树采用的二叉链表存储结构代码： typedef struct BiTNode { char data ; // 结点数据，假设为字符型 struct BiTNode * lchild , * rchild ; // 左右孩子指针 } BiTNode , * BiTree ;

（3）算法描述（C 语言）： // 函数功能：计算二叉树 T 中第 k 层的叶子结点个数 // 参数：T 为二叉树根结点指针，currentLevel 为当前结点所在层数（根结点为第 1 层），k 为指定层数 // 返回值：第 k 层的叶子结点个数 int countLeafAtLevel ( BiTree T , int currentLevel , int k ) { if ( T == NULL ) { // 空树，返回 0 return 0 ; } if ( currentLevel == k ) { // 到达第 k 层 // 判断是否为叶子结点 if ( T -&gt; lchild == NULL && T -&gt; rchild == NULL ) { return 1 ; } else { return 0 ; } } else if ( currentLevel &lt; k ) { // 当前层小于 k，继续向下递归 return countLeafAtLevel ( T -&gt; lchild , currentLevel + 1 , k ) + countLeafAtLevel ( T -&gt; rchild , currentLevel + 1 , k ); } else { // 当前层大于 k，不再递归 return 0 ; } } // 调用示例：int leafCount = countLeafAtLevel(root, 1, k); 【解析】 算法设计思想解析：由于需要统计二叉树中指定层 k 的叶子结点个数，采用深度优先搜索（DFS）策略，通过递归遍历二叉树并在过程中跟踪当前层数。当层数等于 k 时，判断当前结点是否为叶子结点并进行计数；若层数小于 k ，则继续递归遍历左右子树；若层数大于 k ，则提前返回，避免无效访问。这种方法只需遍历一次二叉树，且在层数超过 k 时停止递归，提高了效率。 存储结构采用标准的二叉链表，每个结点包含数据域和指向左右子树的指针，便于递归操作。 算法实现时，递归终止条件包括：结点为空时返回 0；当前层数等于 k 时，根据叶子结点定义返回 1 或 0；当前层数小于 k 时，递归计算左右子树的叶子结点数之和；当前层数大于 k 时直接返回 0。该算法的时间复杂度为 O ( n ) ，最坏情况下需访问所有结点（当 k 大于等于树高时）；空间复杂度为 O ( h ) ， h 为树的高度，即递归栈的深度。注意题目中 k > 1 ，但算法对 k = 1 同样适用，调用时传入 currentLevel=1 即可。
