---
title: "模拟卷7 数据结构 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 42
---

（13 分）已知一棵二叉树采用二叉链表存储，结点结构为：

root 指向根结点。请编写算法判断该二叉树是否是平衡二叉树，即二叉树中任意结点的左右子树的深度相差不超过 1。例如下图所示的二叉树就是一棵平衡二叉树。

要求： （1）给出算法的基本设计思想。 （2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

[tag_link]

【答案】 （1）基本设计思想：采用递归后序遍历二叉树，在计算每个结点高度的同时判断其左右子树是否平衡。递归函数返回当前子树的高度，若子树不平衡则返回 -1 作为标志。对于每个结点，先递归检查其左右子树，若任一子树返回 -1，则当前子树不平衡；否则计算左右子树高度差，若超过 1 则返回 -1，否则返回当前子树高度（即左右子树最大高度加 1）。最终，若根结点对应的递归返回值不为 -1，则二叉树是平衡的。 （2）算法描述（C 语言）： #include &lt;stdlib.h&gt; // 用于 abs 函数 #include &lt;stdbool.h&gt; // 用于 bool 类型 struct Node { struct Node * lchild ; int data ; struct Node * rchild ; }; // 辅助函数：检查以 root 为根的子树是否平衡，返回高度；若不平衡返回 -1 int checkBalance ( struct Node * root ) { if ( root == NULL ) { return 0 ; // 空树高度为 0，平衡 } // 递归检查左子树 int leftHeight = checkBalance ( root -&gt; lchild ); if ( leftHeight == - 1 ) { return - 1 ; // 左子树不平衡，向上传递 } // 递归检查右子树 int rightHeight = checkBalance ( root -&gt; rchild ); if ( rightHeight == - 1 ) { return - 1 ; // 右子树不平衡，向上传递 } // 检查当前结点左右子树高度差 if ( abs ( leftHeight - rightHeight ) &gt; 1 ) { return - 1 ; // 当前结点不平衡 } // 返回当前子树高度 return ( leftHeight &gt; rightHeight ? leftHeight : rightHeight ) + 1 ; } // 主函数：判断二叉树是否平衡 bool isBalanced ( struct Node * root ) { return checkBalance ( root ) != - 1 ; } 【解析】 该算法基于递归实现，核心思想是在计算结点高度时同步判断平衡性，避免重复遍历。checkBalance 函数采用后序遍历顺序：先递归处理左右子树，再处理当前结点。若子树不平衡（返回 -1），则立即向上返回，无需进一步计算；否则比较左右子树高度差，若超过 1 则返回 -1 表示不平衡，否则返回当前子树高度。isBalanced 函数通过调用 checkBalance 检查返回值是否为 -1 来判断整棵树的平衡性。算法中每个结点仅访问一次，时间复杂度为 O(n)，n 为结点数；递归栈空间复杂度为 O(h)，h 为树高。这种设计既高效又简洁，符合题目要求。 43 （10 分）设某计算机有变址寻址、间接寻址和相对寻址方式，一个指令长等于一个存储字。设当前指令的地址码部分为 001AH ，正在执行的指令所在地址为 1F05H ，变址寄存器中的内容为 23A0H 。已知存储器的部分地址及相应内容如下表所示： 地址 001 A H 1 F 05 H 1 F 1 F H ​ 内容 23 A 0 H 2400 H 2500 H ​ 地址 23 A 0 H 23 B A H ​ 内容 2600 H 1748 H ​ ​ （1）当执行取数指令时，如为变址寻址方式，取出的数为多少？ （2）如为间接寻址，取出的数为多少？ （3）设计算机每取一个存储字 PC 自动加 1，转移指令采用相对寻址，当执行转移指令时，转移地址为多少？若希望转移到 23A0H ，则指令的地址码部分应设为多少？ 查看答案与解析 收藏

---

