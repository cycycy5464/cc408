# 408 计算机学科专业基础综合模拟卷 5

#### 数据结构

##### 1

假设栈的容量为 3，入栈的序列为 1,2,3,4,5，则出栈的序列可能为（ ）。

A\. 3,2,1,5,4
B\. 1,5,4,3,2
C\. 5,4,3,2,1
D\. 4,3,2,1,5

[tag_link]

正确答案：A
> <p>
栈的容量为 3，入栈序列固定为 1,2,3,4,5。
> 出栈序列必须符合栈的后进先出规则，且受容量限制。
> <p>对于选项 A（3,2,1,5,4）：
<ul><li>先入栈 1,2,3（栈满），出栈 3,2,1，栈空。
> </li><li>再入栈 4，入栈 5，出栈 5,4。
> 操作过程中栈内元素数始终不超过 3，且符合出栈序列，因此可能。
> </li></ul><p>对于选项 B（1,5,4,3,2）：
<ul><li>出栈 1 后，需出栈 5，但 5 尚未入栈。
> 入栈 2,3,4 后栈满，无法直接入栈 5；
> 若先出栈元素则破坏序列顺序。
> </li><li>要使 5 先出栈，需在 5 入栈时栈中包含 4,3,2，但容量仅为 3，无法同时容纳 4 个元素，因此不可能。
> </li></ul><p>对于选项 C（5,4,3,2,1）：
<ul><li>需先出栈 5，但 5 最后入栈。
> 入栈 1,2,3 后栈满，入栈 4 需先出栈元素，而出栈会破坏序列以 5 开始，因此不可能。
> </li></ul><p>对于选项 D（4,3,2,1,5）：
<ul><li>需先出栈 4，但入栈 1,2,3 后栈满，入栈 4 需先出栈元素，而出栈会导致序列首元素不为 4，因此不可能。
> </li></ul><p>综上，只有选项 A 可能。
>

##### 2

若以 1234 作为双端队列的输入序列，则既不能由输入受限的双端队列得到，也不能由输出受限的双端队列得到的输出序列是（ ）。

A\. 1234
B\. 4132
C\. 4231
D\. 4213

[tag_link]

正确答案：C
> <p>
输入序列为 1234，需找出既不能由输入受限双端队列（插入仅在一端，删除可在两端）也不能由输出受限双端队列（删除仅在一端，插入可在两端）得到的输出序列。
> <ul><li>选项 A（1234）：两种受限队列均可通过顺序插入和删除得到。
> </li><li>选项 B（4132）：输入受限队列可通过插入 1,2,3,4 后依次删除后端 4、前端 1、后端 3、前端 2 得到；
> 输出受限队列无法得到，因为需要插入 4 前队列前端为 1 且后续顺序为 3,2，但无法通过插入 1,2,3 得到所需队列[1,3,2]。
> </li><li>选项 C（4231）：输入受限队列中，插入 1,2,3,4 后删除后端 4，队列变为[1,2,3]，2 不在端部，无法直接输出 2 而不先输出 1 或 3；
> 输出受限队列中，需要插入 4 前队列为[2,3,1]，但无法通过插入 1,2,3 得到该队列。
> 因此两种队列均无法得到 4231。
> </li><li>选项 D（4213）：输入受限队列无法得到（类似 4231 的原因），但输出受限队列可通过插入 1,2,3 得到队列[2,1,3]，再插入 4 前端后依次删除得到 4213。
> 综上，4231 既不能由输入受限也不能由输出受限双端队列得到。
> </li></ul>
>

##### 3

在下列遍历算法中，在遍历序列中叶结点之间的次序可能与其他算法不同的算法是（ ）。

A\. 先序遍历算法
B\. 中序遍历算法
C\. 后序遍历算法
D\. 层次遍历算法

[tag_link]

正确答案：D
> 先序、中序和后序遍历算法均属于深度优先遍历，其递归或迭代过程都遵循先处理左子树、后处理右子树的原则。
> 因此，对于任意二叉树，这三种遍历算法访问叶结点的次序始终相同：左子树中的所有叶结点都先于右子树中的所有叶结点被访问，且左、右子树内部叶结点的相对顺序也一致。
> 而层次遍历算法采用广度优先策略，按层次从上到下、从左到右访问节点。
> 由于叶结点可能分布在不同层次，其访问次序取决于层次和同一层次中的左右位置，可能与深度优先遍历的叶结点次序不同。
> 例如，对于根节点有左子节点（含两个叶结点）和右子节点（为叶结点）的二叉树，先序、中序和后序遍历的叶结点次序均为左子树中的两个叶结点先于右子叶结点，而层次遍历则先访问右子叶结点（位于第二层），再访问左子树中的叶结点（位于第三层）。
> 因此，层次遍历算法的叶结点次序可能与其他算法不同。
>

##### 4

一般说来，若深度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个结点的二叉树具有最小路径长度时，第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
层（根为第 1 层）上的结点数为（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9324em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span><span class="mbin mtight">−</span><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9324em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9324em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8491em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span></span></span></span>

[tag_link]

正确答案：B
> 对于深度为 k 且具有最小路径长度的二叉树，为了使所有结点到根的路径长度之和最小，树应尽可能平衡，即前 k-1 层完全填满。
> 前 k-1 层的结点总数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9324em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，剩余结点全部位于第 k 层。
> 因此，第 k 层的结点数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0991em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9324em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.03148em>k</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，对应选项 A 和 B（两者表达式相同）。
> 选项 C 和 D 与推导结果不符，故正确答案为 A。
>

##### 5

利用逐个插入建立序列 (50,72,43,85,75,20,35,45,65,30) 对应的二叉排序树后，要查找元素 30 要进行的元素间比较次数是（ ）。

A\. 4
B\. 5
C\. 6
D\. 7

[tag_link]

正确答案：B
> <p> 考查二叉排序树的构造和查找。
> 按题中数据的输入次序，建立的二叉排序树如右图所示。
> 查找元素 30 需要依次比较的元素为 50,43,20,35,30，比较次数为 5 次。
> <pre tabindex=0>`      50
     /  \
   43    72
  /  \  /  \
 20  45 65  85
  \        /
  35      75
 /
30
`</pre>
>

##### 6

由 4 棵树组成的森林中，第一、第二、第三和第四棵树中的结点数分别为 30、10、20、5，当把森林转换成二叉树后，对应二叉树中根结点的右子树的左子树的结点数为（ ）。

A\. 29
B\. 9
C\. 25
D\. 19

[tag_link]

正确答案：B
> <p>
将森林转换成二叉树时，采用“左孩子右兄弟”的表示法。
> 对于由多棵树组成的森林，转换规则为：取第一棵树的根作为二叉树的根，根的左子树由第一棵树中根的子树森林转换而成，根的右子树由剩余树组成的森林转换而成。
> <p>给定森林中四棵树的结点数分别为 30、10、20、5。
> 转换后二叉树的结构如下：
<ul><li>二叉树的根对应第一棵树的根。
> </li><li>根的左子树由第一棵树中除根外的 29 个结点转换而成，结点数为 29。
> </li><li>根的右子树由第二、三、四棵树（结点数共 10+20+5=35）转换而成。
> </li></ul><p>根的右子树本身也是一棵二叉树，其根对应第二棵树的根。
> 该右子树的左子树由第二棵树中除根外的子树森林转换而成，第二棵树有 10 个结点，除根外有 9 个结点，因此该左子树的结点数为 9。
> <p>故根结点的右子树的左子树的结点数为 9。
>

##### 7

如果具有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个顶点的图是一个环，则它有（ ）棵生成树。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
D\. 1

[tag_link]

正确答案：B
> 由于图是一个环，它包含 n 个顶点和 n 条边。
> 生成树是连接所有顶点且无环的子图，对于环图，只需移除任意一条边即可打破环并得到一棵生成树。
> 环中共有 n 条边，每条边的移除对应一棵不同的生成树，因此生成树的数量为 n。
>

##### 8

假设有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
条边的有向图用邻接表表示，则删除与某个顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.03588em>v</span></span></span></span>
相关的所有边的时间复杂度为（ ）。

A\. O(n)
B\. O(e)
C\. O(n+e)
D\. O(ne)

[tag_link]

正确答案：C
> 在有向图的邻接表表示中，每个顶点维护一个链表存储其出边。
> 删除与顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.03588em>v</span></span></span></span>
相关的所有边包括两部分：一是删除顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.03588em>v</span></span></span></span>
的所有出边，二是删除所有指向顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.03588em>v</span></span></span></span>
的入边。
> 删除出边只需清空顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.03588em>v</span></span></span></span>
的邻接链表，时间复杂度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord text"></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.03588em>v</span><span class=mclose>))</span></span></span></span>
，其中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord text"></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.03588em>v</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
。
> 删除入边则需要遍历所有顶点的邻接链表，检查每条边是否指向
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.03588em>v</span></span></span></span>
，并在找到时删除。
> 遍历所有链表需访问
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个顶点和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
条边，时间复杂度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">e</span><span class=mclose>)</span></span></span></span>
。
> 因此，总时间复杂度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord text"></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.03588em>v</span><span class=mclose>))</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">e</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">e</span><span class=mclose>)</span></span></span></span>
。
>

##### 9

折半查找有序表 (2,10,25,35,40,65,70,75,81,82,88,100)，若查找元素 75，需依次与表中元素（ ）进行比较。

A\. 65,82,75
B\. 70,82,75
C\. 65,81,75
D\. 65,81,70,75

[tag_link]

正确答案：D
> <p> 考查折半查找的查找过程。
> 有序表长度为 12，依据折半查找的思想：
<ul><li>第一次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>12</span><span class=mclose>)</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>6</span></span></span></span>
个元素，即 65；
> </li><li>第二次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊((</span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>12</span><span class=mclose>)</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span></span></span></span>
个元素，即 81；
> </li><li>第三次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊(</span><span class=mord>7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>9</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>))</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>7</span></span></span></span>
个元素，即 70；
> </li><li>第四次查找第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊(</span><span class=mord>7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>8</span><span class=mclose>⌋</span><span class=mord>/2</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
个元素，即 75。
> </li></ul><p>比较的元素依次为 65、81、70、75。
> 对应的折半查找判定树如下图所示。
> <pre tabindex=0>`        65
      /    \
    25      81
   /  \     /  \
  2    35  70   88
 /     \    \   /  \
10      40   75 82  100
`</pre>
>

##### 10

堆排序分为两个阶段，其中第一阶段将给定的序列建成一个堆，第二阶段逐次输出堆顶元素。设给定序列{48,62,35,77,55,14,35,98}，若在堆排序的第一阶段将该序列建成一个堆（大根堆），那么交换元素的次数为（ ）。

A\. 5
B\. 6
C\. 7
D\. 8

[tag_link]

正确答案：B
> <p> 考查初始堆的构造过程。
> 首先对以第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌋</span></span></span></span>
个结点为根的子树筛选，使该子树成为堆，之后向前依次对各结点为根的子树进行筛选，直到筛选到根结点。
> 序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class=mord>48</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>62</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>77</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>55</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>14</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>98</span><span class=mclose>}</span></span></span></span>
建立初始堆的过程如下所示：
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1><img src=/images/408simulate/5_10_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>

##### 11

对 {05,46,13,55,94,17,42} 进行基数排序，一趟排序的结果是（ ）。

A\. 05,46,13,55,94,17,42
B\. 05,13,17,42,46,55,94
C\. 42,13,94,05,55,46,17
D\. 05,13,46,55,17,42,94

[tag_link]

正确答案：C
> <p>
基数排序通常从最低有效位（LSD）开始，对数字的每一位进行稳定排序。
> 给定序列 {05,46,13,55,94,17,42} 均为两位数，第一趟排序根据个位数字进行。
> <p>首先，提取每个数字的个位：05（个位 5）、46（个位 6）、13（个位 3）、55（个位 5）、94（个位 4）、17（个位 7）、42（个位 2）。
> <p>按照个位数字分配桶（0-9），保持稳定性：
<ul><li>个位 2:42</li><li>个位 3:13</li><li>个位 4:94</li><li>个位 5:05、55（保持原序，05 在 55 前）</li><li>个位 6:46</li><li>个位 7:17</li></ul><p>按桶顺序收集数字，得到序列：42,13,94,05,55,46,17。
> 这与选项 C 一致。
> <p>选项 A 是原始序列；
> 选项 B 是完全排序后的结果；
> 选项 D 不符合个位排序顺序。
> 因此，一趟排序结果为 C。
>

---
#### 计算机组成原理

##### 12

计算机中，与 CPU 的 CPI 无关的因素是（ ）。

A\. 时钟频率
B\. 系统结构
C\. 指令集
D\. 计算机组织

[tag_link]

正确答案：A
> CPI（Cycles Per Instruction）表示每条指令的平均时钟周期数，它衡量 CPU 执行指令的效率。
> 时钟频率决定 CPU 的时钟速度，即每秒钟的时钟周期数，它影响时钟周期时间（时钟周期时间的倒数），但并不直接改变每条指令所需的周期数，因此与 CPI 无关。
> 系统结构（B）定义了计算机的整体设计，包括指令执行方式，直接影响 CPI；
> 指令集（C）决定了指令的复杂性和执行所需的周期数，与 CPI 密切相关；
> 计算机组织（D）涉及硬件实现如流水线、缓存等，通过优化指令执行来降低 CPI。
> 因此，只有时钟频率与 CPI 无关。
>

##### 13

若数据在存储器中以小端方式存放，则十六进制数 12345678H 按字节地址从小到大依次为（ ）。

A\. 78563412H
B\. 87654321H
C\. 12345678H
D\. 21436587H

[tag_link]

正确答案：A
> 小端方式（Little-endian）存储规则为：多字节数据中，最低有效字节存放在最低地址，最高有效字节存放在最高地址。
> 对于十六进制数 12345678H，这是一个 32 位数据，占 4 个字节，从高到低字节依次为 12H、34H、56H、78H。
> 按小端方式存放时，地址从小到大依次存储最低有效字节到最高有效字节，即 78H、56H、34H、12H，组合起来即为 78563412H。
> 因此选项 A 正确。
>

##### 14

按 IEEE754 标准规定的 32 位浮点数（单精度浮点数）41A4C000H 对应的十进制数是（ ）。

A\. 4.59375
B\. -20.59375
C\. -4.59375
D\. 20.59375

[tag_link]

正确答案：D
> <p> 首先，将十六进制数 `41A4C000H` 转换为二进制：
`0100 0001 1010 0100 1100 0000 0000 0000`。
> <p>按照 IEEE754 单精度浮点数格式：
<ul><li>第 1 位为符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
；
> </li><li>第 2–9 位为指数位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
（8 位）；
> </li><li>第 10–32 位为尾数位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span></span></span></span>
（23 位）。
> </li></ul><p>具体分析如下：
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0</span></span></span></span>
，表示正数。
> </li><li>指数位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.9996em;vertical-align:-.3552em></span><span class=mord>1000001</span><span class=mord><span class=mord>1</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3448em><span style=top:-2.5198em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mopen mtight">(</span><span class="mord mtight">2</span><span class="mclose mtight">)</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.3552em><span></span></span></span></span></span></span></span></span></span>
，转换为十进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>131</span></span></span></span>
。
> IEEE754 中指数采用偏置表示，偏置量为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span></span></span></span>
，因此实际指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>131</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4.</span></span></span></span></li><li>尾数位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.9996em;vertical-align:-.3552em></span><span class=mord>0100100110000000000000</span><span class=mord><span class=mord>0</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3448em><span style=top:-2.5198em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mopen mtight">(</span><span class="mord mtight">2</span><span class="mclose mtight">)</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.3552em><span></span></span></span></span></span></span></span></span></span>
，表示小数部分。
> 计算
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span></span></span></span>
的十进制值：对应二进制小数位中，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.25</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">5</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.03125</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">8</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.00390625</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">9</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.001953125</span></span></span></span>
为 1，其余为 0，求和得
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.287109375.</span></span></span></span>
IEEE754 中尾数包含隐含的 1，因此实际尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1.287109375.</span></span></span></span></li></ul><p>浮点数的值为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1413em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>1</span><span class=mclose><span class=mclose>)</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8913em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style=margin-right:.05764em>S</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7144em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7144em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">e</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.287109375</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8641em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8641em><span style=top:-3.113em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.287109375</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>20.59375.</span></span></span></span></span></div><p>因此，对应的十进制数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>20.59375</span></span></span></span>
，选项 D 正确。
>

##### 15

设有一主存-Cache 层次的存储器，其主存容量 1MB，Cache 容量 16KB，每字块有 8 个字，每字 32 位，采用直接地址映像方式，若主存地址为 35301H，且 CPU 访问 Cache 命中，则该主存块在 Cache 的第（ ）字块中（Cache 起始字块为第 0 字块）。

A\. 152
B\. 153
C\. 154
D\. 151

[tag_link]

正确答案：A
> <p>
主存容量为 1MB，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">20</span></span></span></span></span></span></span></span></span></span></span></span>
字节，因此主存地址为 20 位。
> Cache 容量为 16KB，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">14</span></span></span></span></span></span></span></span></span></span></span></span>
字节。
> 每个字为 32 位（即 4 字节），每个字块包含 8 个字，因此块大小为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>32</span></span></span></span>
字节，块内偏移需要
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9386em;vertical-align:-.2441em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mord>32</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
位。
> Cache 共有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">14</span></span></span></span></span></span></span></span></span><span class=mord>/32</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>512</span></span></span></span>
块，索引需要
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9386em;vertical-align:-.2441em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mord>512</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span></span></span></span>
位。
> 在直接映射方式下，主存地址划分为：标签（高 6 位）、索引（中间 9 位）、偏移（低 5 位）。
> <p>给定主存地址 35301H，转换为二进制为 0011 0101 0011 0000 0001（共 20 位）。
> 偏移量为低 5 位（00001），索引为位 5 至位 13（010011000），转换为十进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>128</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>16</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>152</span></span></span></span>
。
> 也可通过计算主存块号得到：地址 35301H 对应十进制 217857 字节，块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>217857</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>32</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>6808</span></span></span></span>
（余数为 1），Cache 块号为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>6808</span><span class="mspace allowbreak"></span><span class=mspace style=margin-right:.6667em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mspace style=margin-right:.1667em></span><span class=mord>512</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>152</span></span></span></span>
。
> 因此，该主存块位于 Cache 的第 152 字块中。
>

##### 16

在页面尺寸为 4KB 的页式存储管理中，页表中的内容如下图所示，则物理地址 32773 对应的逻辑地址为（ ）。

A\. 32773
B\. 42773
C\. 12293
D\. 62773

[tag_link]

正确答案：C
> 首先，页面尺寸为 4KB，即 4096 字节。
> 物理地址 32773 可以分解为页框号和页内偏移：页框号 = 32773 ÷ 4096 = 8（因为 4096 × 8 = 32768），页内偏移 = 32773 - 32768 = 5。
> 然后，根据页表内容，页框号 8 对应虚页号 3。
> 因此，逻辑地址由虚页号和页内偏移组成：逻辑地址 = 虚页号 × 页面尺寸 + 页内偏移 = 3 × 4096 + 5 = 12288 + 5 = 12293。
> 故正确答案为 C. 12293。
>

##### 17

在通用计算机指令系统的二地址指令中，操作数的物理位置可安排在（ ）。
I. 一个主存单元和缓冲存储器
II. 两个数据寄存器
III. 一个主存单元和一个数据寄存器
IV. 一个数据寄存器和一个控制存储器
V. 一个主存单元和一个外存单元

A\. II、III 和 IV
B\. II、III
C\. I、II 和 III
D\. I、II、III 和 V

[tag_link]

正确答案：B
> 在通用计算机指令系统的二地址指令中，操作数的物理位置是指指令能够直接寻址或指定的存储位置。
> 分析各选项：缓冲存储器（如缓存）通常对程序员透明，指令不能直接寻址缓存地址，因此 I 不正确；
> 两个数据寄存器（II）是常见的安排，如寄存器 - 寄存器指令；
> 一个主存单元和一个数据寄存器（III）也常见，如寄存器 - 内存指令；
> 控制存储器用于存储微程序，不是数据操作数的存储位置，因此 IV 不正确；
> 外存单元（如磁盘）需要通过 I/O 机制访问，指令不能直接寻址，因此 V 不正确。
> 综上，只有 II 和 III 是合理的安排，对应选项 B。
>

##### 18

某微机的指令格式如下所示：

A\. 22H
B\. 1144H
C\. 1256H
D\. 0059H

[tag_link]

正确答案：B
> 指令格式中，操作码占据位 15 至 10，寻址特征位 X 占据位 9 至 8，位移量 D 占据位 7 至 0。
> 指令 2222H 的二进制表示为 0010 0010 0010 0010。
> 分解后，位 9 至 8 为 10，对应 X=10；
> 位 7 至 0 为 00100010，即 D=22H。
> 根据寻址特征，X=10 表示使用变址寄存器 X2 进行变址寻址，有效地址计算公式为 (X2) + D。
> 已知 (X2)=1122H，D=22H 为 8 位正数，扩展为 16 位后仍为 0022H，因此有效地址为 1122H + 0022H = 1144H。
> 选项 B 符合计算结果。
>

##### 19

某机采用微程序控制方式，微指令字长 24 位，采用水平型编码控制的微指令格式，断定方式。共有微命令 30 个，构成 4 个互斥类，各包含 5 个、8 个、14 个和 3 个微命令，外部条件共 3 个。则控制存储器的容量应该为（ ）。

A\. 256×24bit
B\. 30×24bit
C\. 31×24bit
D\. 24×24bit

[tag_link]

正确答案：A
> <p> 微指令字长为 24 位，控制字段采用水平型编码。
> 微命令分为 4 个互斥类，每类所需的位数需包含“无操作”状态，计算如下：
<ul><li>第一类有 5 个微命令，需
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌈</span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>5</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)⌉</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
位；
> </li><li>第二类有 8 个微命令，需
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌈</span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)⌉</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span></span></span></span>
位；
> </li><li>第三类有 14 个微命令，需
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌈</span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>14</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)⌉</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span></span></span></span>
位；
> </li><li>第四类有 3 个微命令，需
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌈</span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)⌉</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
位。
> </li></ul><p>控制字段共需
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>4</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>4</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>13</span></span></span></span>
位。
> <p>顺序字段占
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>24</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>13</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>11</span></span></span></span>
位，用于断定方式下的地址生成。
> 外部条件共有 3 个，条件选择字段需 3 位（可编码 8 种转移条件，满足 3 个外部条件及其他功能），下地址字段占
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>11</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
位。
> 下地址字段 8 位可寻址
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">8</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>256</span></span></span></span>
个微指令单元，因此控制存储器容量为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>24</span></span></span></span>
位。
>

##### 20

数据总线的宽度由总线的（ ）定义。

A\. 物理特性
B\. 功能特性
C\. 电气特性
D\. 时间特性

[tag_link]

正确答案：B
> <p>
数据总线的宽度指的是总线一次能传输的数据位数，这由数据线的数量决定。
> 在总线的各类特性中，功能特性定义了各信号线的具体功能，如地址线、数据线、控制线等。
> 数据总线的宽度直接与数据线的功能相关，因此它由功能特性定义。
> <p>物理特性涉及总线的机械连接方式（如插头、插座），电气特性涉及电压、电流等参数，时间特性则关注信号时序关系。
> 这些特性均不直接决定数据总线的宽度，故其他选项不正确。
> 因此，本题选择 B。
>

##### 21

DMA 方式的接口电路中有程序中断部件，其作用包括（ ）。
I. 实现数据传送
II. 向 CPU 提出总线使用权
III. 向 CPU 提出传输结束
IV. 检查数据是否出错

A\. 仅 III
B\. III 和 IV
C\. I、III 和 IV
D\. I 和 II

[tag_link]

正确答案：A
> <p> 考查 DMA 方式中的中断与中断传输方式的区别。
> 前者是向 CPU 报告数据传输结束，后者是传送数据，另外 DMA 方式中的中断不包括检查是否出错，而是报告错误。
> <p>注意：DMA 方式与程序中断方式的比较如下。
> <p>① DMA 传送数据的方式是靠硬件传送，而程序传送方式是由程序来传送。
> <p>② 程序中断方式需要中断 CPU 的现行程序，需要保护现场，而 DMA 方式不需要中断现行程序。
> <p>③ 程序中断方式需要在一条指令执行结束才能得到响应，而 DMA 方式则可以在指令周期内的任意存储周期结束时响应。
> <p>④ DMA 方式的优先级高于程序中断方式的优先级。
>

##### 22

某机有四级中断，优先级从高到低为 1→2→3→4。若将优先级顺序修改，改后 1 级中断的屏蔽字为 1101，2 级中断的屏蔽字为 0100，3 级中断的屏蔽字为 1111，4 级中断的屏蔽字为 0101，则修改后的优先顺序从高到低为（ ）。

A\. 1→2→3→4
B\. 3→1→4→2
C\. 1→3→4→2
D\. 2→1→3→4

[tag_link]

正确答案：B
> <p> 首先，理解屏蔽字的含义：每个中断的屏蔽字表示当处理该中断时，哪些中断被屏蔽。
> 屏蔽字为 4 位二进制数，假设位顺序对应中断 1、2、3、4。
> 若某位为 1，则屏蔽对应中断；
> 若为 0，则不屏蔽。
> 根据中断优先级规则，高优先级中断可以屏蔽低优先级中断，而低优先级中断不能屏蔽高优先级中断。
> 因此，从屏蔽字可以推导优先级关系：若中断 i 的屏蔽字中对应中断 j 的位为 1，则中断 j 的优先级低于中断 i；
> 若为 0，则中断 j 的优先级高于中断 i。
> <p>给定屏蔽字：中断 1 为 1101，中断 2 为 0100，中断 3 为 1111，中断 4 为 0101。
> 分析每个屏蔽字：
<ul><li>中断 1 的屏蔽字 1101：位 3 为 0，说明中断 3 优先级高于中断 1；
> 位 2 和位 4 为 1，说明中断 2 和中断 4 优先级低于中断 1。
> </li><li>中断 2 的屏蔽字 0100：位 1、位 3、位 4 均为 0，说明中断 1、3、4 优先级均高于中断 2。
> </li><li>中断 3 的屏蔽字 1111：所有位为 1，说明中断 3 屏蔽所有中断，因此中断 3 优先级最高。
> </li><li>中断 4 的屏蔽字 0101：位 1 和位 3 为 0，说明中断 1 和中断 3 优先级高于中断 4；
> 位 2 为 1，说明中断 2 优先级低于中断 4。
> </li></ul><p>综合上述关系：中断 3 优先级最高；
> 中断 1 优先级高于中断 4 和中断 2；
> 中断 4 优先级高于中断 2。
> 因此，修改后的优先级从高到低为 3→1→4→2，对应选项 B。
> 验证屏蔽字与优先级顺序一致，确认正确。
>

---
#### 操作系统

##### 23

相对采用单一内核结构，采用微内核结构设计和实现操作系统有诸多好处，但是（ ）不是微内核的优势。

A\. 使系统更高效
B\. 想添加新任务时，不必修改内核
C\. 使系统更安全
D\. 使系统更可靠

[tag_link]

正确答案：A
> 微内核结构通过最小化内核功能，仅保留进程调度、内存管理等核心服务，而将文件系统、设备驱动等其他服务置于用户空间。
> 这种设计提升了系统的安全性和可靠性：用户空间服务的故障不易蔓延至内核，从而增强了隔离性（对应选项 C 和 D）。
> 同时，微内核支持模块化扩展，添加新任务时只需在用户空间实现，无需修改内核，提高了灵活性（对应选项 B）。
> 然而，微内核的劣势在于效率：由于服务分布在用户空间，需要频繁的进程间通信和上下文切换，这引入了额外开销，导致性能通常不如单一内核结构高效。
> 因此，选项 A“使系统更高效”并非微内核的优势，反而是其常见缺点。
>

##### 24

有一个计数信号量 S，若干个进程对 S 进行了 28 次 P 操作和 18 次 V 操作后，信号量 S 的值为 0。然后又对信号量 S 进行了 3 次 V 操作。此时有（ ）个进程等待在信号量 S 的队列中。

A\. 2
B\. 0
C\. 3
D\. 7

[tag_link]

正确答案：B
> <p> 首先，设信号量 S 的初始值为 X。
> 根据信号量的操作规则，P 操作会使 S 减 1，V 操作会使 S 加 1。
> 经过 28 次 P 操作和 18 次 V 操作后，S 的值为 X - 28 + 18 = X - 10。
> 已知此时 S 的值为 0，因此 X - 10 = 0，解得初始值 X = 10。
> <p>然后，在 S 值为 0 的情况下，又进行了 3 次 V 操作。
> 每次 V 操作使 S 加 1，所以 S 变为 0 + 3 = 3。
> <p>在计数信号量中，当 S 的值大于或等于 0 时，表示没有进程等待在信号量的队列中。
> 具体地，若 S > 0，表示有可用资源；
> 若 S = 0，表示资源刚好用完且无进程等待；
> 若 S < 0，其绝对值表示等待进程数。
> 在 28 次 P 和 18 次 V 操作后 S = 0，说明等待队列已空。
> 后续 3 次 V 操作使 S 变为 3，S 仍为正数，因此等待队列中依然没有进程。
> <p>故此时有 0 个进程等待在信号量 S 的队列中。
>

##### 25

进程从运行状态到等待状态可能是（ ）。

A\. 运行进程执行了 P 操作
B\. 进程调度程序的调度
C\. 运行进程的时间片用完
D\. 运行进程执行了 V 操作

[tag_link]

正确答案：A
> <p> 进程从运行状态进入等待状态通常是由于进程请求某个资源或等待某个事件，但该资源暂时不可用或事件尚未发生。
> P 操作（即 wait 操作）是同步机制中的一种，用于申请资源。
> 当运行进程执行 P 操作时，如果信号量值小于等于 0，表示资源不足，该进程会被阻塞并进入等待状态，因此选项 A 正确。
> <p>其他选项中，B 和 C 通常导致进程从运行状态转为就绪状态：进程调度程序的调度可能将运行进程切换为就绪状态以让其他进程运行；
> 时间片用完也会触发调度，使进程从运行转为就绪。
> D 选项的 V 操作（即 signal 操作）用于释放资源，可能唤醒等待中的进程，但执行 V 操作的进程本身不会进入等待状态。
> <p>因此，只有 A 选项描述了进程从运行状态到等待状态的可能情况。
>

##### 26

关于临界区问题（critical section problem）的一个算法（假设只有进程 P0 和 P1 可能会进入该临界区）如下（i 为 0 或 1），该算法（ ）。

A\. 不能保证进程互斥进入临界区，且会出现“饥饿”
B\. 不能保证进程互斥进入临界区，但不会出现“饥饿”
C\. 保证进程互斥进入临界区，但会出现“饥饿”
D\. 保证进程互斥进入临界区，不会出现“饥饿”

[tag_link]

正确答案：B
> <p>
<p>该算法不能保证进程互斥进入临界区。
> 分析两个进程 P0 和 P1 的执行流程：假设初始时共享变量 turn=0，P0 首先执行，检查 turn!=0 为假，跳过 turn=0 的设置，再检查 turn!=0 为假，不跳转，然后设置 turn=1 并进入临界区。
> 此时 P1 也开始执行，检查 turn!=1 为假，跳过 turn=1 的设置，再检查 turn!=1 为假，不跳转，设置 turn=0 并进入临界区。
> 这样，P0 和 P1 同时处于临界区，违反了互斥条件。
> <p>虽然互斥无法保证，但算法不会导致“饥饿”（即某个进程永远无法进入临界区）。
> 因为每个进程在尝试进入时，都会通过循环检查 turn 是否等于自己的标识 i。
> 无论 turn 初始值如何，进程在执行中总会将 turn 设置为对方或 0，使得另一个进程在后续尝试中能够通过检查并进入临界区。
> 例如，P0 退出临界区时设置 turn=0，之后 P1 尝试时可能先设置 turn=1 再检查通过，从而进入临界区。
> 两个进程在竞争中有机会交替进入，没有进程会被永久阻塞。
> <p>因此，该算法不能保证互斥，但不会出现饥饿。
>

##### 27

设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为同类资源数，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
为系统中并发进程数。当
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个进程共享
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个互斥资源时，每个进程的最大需求是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span></span></span></span>
，则下列情况会出现系统死锁的是（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>

[tag_link]

正确答案：D
> <p>
系统死锁的一个常见条件是当所有进程都持有部分资源并等待更多资源时，资源总数不足以满足任何进程的剩余需求。
> 具体来说，如果每个进程的最大需求为 w，那么在最坏情况下，每个进程都已获得 w-1 个资源并等待最后一个资源。
> 此时，已分配资源总数为 n(w-1)，如果资源总数 m 不超过 n(w-1)，即 m ≤ n(w-1)，则系统可能陷入死锁。
> <p>分析各个选项：
A. m=2, n=1, w=2：计算 n(w-1)=1×(2-1)=1，m=2>1，不会死锁。
> B. m=2, n=2, w=1：计算 n(w-1)=2×(1-1)=0，m=2>0，不会死锁。
> C. m=4, n=3, w=2：计算 n(w-1)=3×(2-1)=3，m=4>3，不会死锁。
> D. m=4, n=2, w=3：计算 n(w-1)=2×(3-1)=4，m=4 恰好等于 n(w-1)，此时两个进程各获得 2 个资源后，所有资源被占用，每个进程还需 1 个资源才能完成，但无可用资源，因此系统会出现死锁。
>

##### 28

总体上说，“按需调页”（Demand-paging）是一个很好的虚拟内存管理策略。但是，有些程序设计技术并不适合于这种环境。例如，（ ）。

A\. 堆栈
B\. 线性搜索
C\. 矢量运算
D\. 二分搜索

[tag_link]

正确答案：D
> <p> 按需调页（Demand-paging）是一种虚拟内存管理策略，它在页面被实际访问时才将其加载到内存中，依赖于程序的局部性原理来减少页面错误和提高性能。
> 适合该环境的程序通常具有良好时间或空间局部性，即访问模式集中或连续。
> <p>堆栈操作集中在栈顶，具有高度局部性；
> 线性搜索顺序访问元素，连续内存访问利于页面重用；
> 矢量运算通常涉及顺序或规律数据访问，也能有效利用页面。
> 这些技术都能较好适应按需调页。
> <p>然而，二分搜索需要在有序数组中反复跳跃访问中间元素，访问模式非连续且不可预测，导致频繁跨页面访问。
> 这种低局部性会引发大量页面错误，显著降低系统效率，因此不适合按需调页环境。
>

##### 29

在某请求分页系统中，内存的存取时间为 1μs。若有一个可用的空页被置换的页表被修改，则它处理一个缺页中断需要 8μs；若被置换的页已被修改，则处理一个缺页中断因增加写回外存时间而需要 20μs。假设所有访问页表都在 TLB 中，且 TLB 中存储有页面是否在主存中的信息。假定 70% 被置换的页被修改过，为保证有效存取时间不超过 2μs，可接受的最大缺页中断率约为（ ）。

A\. 5.7%
B\. 11%
C\. 6.5%
D\. 50%

[tag_link]

正确答案：C
> <p>
有效存取时间由无缺页和有缺页两种情况组成：
<ul><li>无缺页时，存取时间为内存存取时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
；
> </li><li>有缺页时，存取时间为缺页中断处理时间，该时间已包含后续内存访问。
> </li></ul><p>根据题意，缺页中断处理时间取决于被置换页是否被修改：
<ul><li><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>70%</span></span></span></span>
的概率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>20</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
（已修改）；
> </li><li><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>30%</span></span></span></span>
的概率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>8</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
（未修改）。
> </li></ul><p>平均处理时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>0.7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>20</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>0.3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>16.4</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span><span class=mord>.</span></span></span></span></span></div><p>设缺页中断率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span></span></span></span>
，则有效存取时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>EAT</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">p</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7778em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16.4</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>15.4</span><span class="mord mathnormal">p</span><span class=mord>.</span></span></span></span></span></div><p>要求
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord text"><span class=mord>EAT</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mspace> </span><span class="mord mathnormal">μ</span><span class="mord text"><span class=mord>s</span></span></span></span></span>
，即

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>15.4</span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span></span></span></span></span></div><p>解得

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8304em;vertical-align:-.1944em></span><span class="mord mathnormal">p</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>15.4</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>0.0649</span><span class=mpunct>,</span></span></span></span></span></div><p>即约
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>6.5%</span></span></span></span>
。
> <p>因此，可接受的最大缺页中断率约为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>6.5%</span></span></span></span>
。
>

##### 30

在某个计算机系统中，内存的分配采用按需调页方式，测得当前 CPU 的利用率为 8%，硬盘交换空间的利用率为 55%，硬盘的繁忙率为 97%，其他设备的利用率可以忽略不计，由此断定系统发生异常，则解决方法是（ ）。
I. 加大交换空间容量
II. 增加内存容量
III. 增加 CPU 数量
IV. 安装一个更快的硬盘
V. 减少多道程序的道数

A\. II、III 和 IV
B\. II 和 V
C\. I 和 II
D\. II、III 和 V

[tag_link]

正确答案：B
> <p> 在按需调页系统中，CPU 利用率仅为 8%，表明 CPU 经常空闲；
> 硬盘交换空间利用率为 55%，说明交换空间尚有剩余；
> 但硬盘繁忙率高达 97%，表明硬盘持续进行大量 I/O 操作，这通常是因为物理内存不足导致频繁的页面交换（抖动）。
> <p>CPU 利用率低是因为进程频繁等待硬盘 I/O，而非 CPU 本身不足，因此增加 CPU 数量（III）无效。
> 交换空间利用率未满，加大其容量（I）不能解决频繁交换问题。
> 安装更快硬盘（IV）可能缩短单次交换时间，但无法从根本上减少交换频率，不是最佳方案。
> <p>增加内存容量（II）可以直接减少缺页和交换操作，从而降低硬盘繁忙率并提高 CPU 利用率；
> 减少多道程序的道数（V）能减轻内存压力，减少进程竞争内存导致的抖动。
> 因此，II 和 V 是直接有效的解决方法。
>

##### 31

信息在外存空间的排列也会影响存取等待时间。考虑几个逻辑记录 A、B、C、…、J，它们被存放在磁盘上，每个磁道存放 10 个记录，安排如表 1 所示。

A\. 60ms
B\. 104ms
C\. 144ms
D\. 204ms

[tag_link]

正确答案：C
> <p> 题中磁盘旋转速度为 20 ms/r，每个磁道存放 10 个记录，因此读出一个记录的时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>20/10</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。
> <p>1）对于第一种记录分布的情况，读出并处理记录 A 需要 6 ms，则此时读写磁头已转到记录 D 的开始处，因此为了读出记录 B，必须再转一圈少两个记录（从记录 D 到记录 B）。
> 后续 8 个记录的读取及处理与此相同，但最后一个记录的读取与处理只需 6 ms。
> 于是，处理 10 个记录的总时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>9</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>4</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>16</span><span class=mclose>)</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>4</span><span class=mclose>)</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>204</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mord>.</span></span></span></span></span></div><p>2）对于第二种记录分布的情况，读出并处理记录 A 后，读写磁头刚好转到记录 B 的开始处，因此立即就可读出并处理，后续记录的读取与处理情况相同。
> 共选择 2.7 圈。
> 最后一个记录的读取与处理只需 6 ms。
> 于是处理 10 个记录的总时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>20</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2.7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>6</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>60</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mord>.</span></span></span></span></span></div><p>综上，信息分布优化后，处理的时间缩短了
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>204</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>60</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>144</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。
>

##### 32

下列有关虚拟设备的论述中，正确的是（ ）。

A\. 虚拟设备是指将独占设备转变成了共享设备
B\. 虚拟设备是指允许用户以标准化方式来使用物理设备
C\. 虚拟设备是把一个物理设备变换成多个对应的逻辑设备
D\. 虚拟设备是允许用户程序不必全部装入多个对应的逻辑设备

[tag_link]

正确答案：C
> 本题考查虚拟设备的概念。
> 虚拟设备是指采用虚拟技术将一台独占设备转换为若干台逻辑设备的情况。
> 这种设备并不是物理地变成共享设备，一般的独享设备也不能转变为共享设备，否则会导致很多不可预知的错误，而是用户在使用它们时“感觉”是共享设备，是逻辑的概念。
> 引入虚拟设备的目的是为了克服独占设备速度慢、利用率低的特点。
>

---
#### 计算机网络

##### 33

电路交换的优点有（ ）。

A\. I 和 II
B\. II 和 III
C\. I 和 III
D\. II 和 IV

[tag_link]

正确答案：A
> 电路交换、分组交换、报文交换的特点是重要的考查点。
> 主要有两种考查方式：一、直接考查某一种（或多种）交换方式的特点，辨别选项的正误；
> 二、给定应用背景，问适用哪一种交换方式，比较灵活，间接考查它们的特点。
> 其中，电路交换是面向连接的，一旦连接建立，数据便可直接通过连接好的物理通路到达接收端，因此传输时延小；
> 由于电路交换是面向连接的，可知传送的分组必定是按序到达的；
> 但在电路交换中，带宽始终被通信的双方独占，利用率就低了。
>

##### 34

以下滑动窗口协议中，一定按序接收到达的分组的有（ ）。
I. 停止—等待协议
II. 后退 N 帧协议
III. 选择重传协议

A\. I 和 II
B\. I 和 III
C\. II 和 III
D\. I、II 和 III

[tag_link]

正确答案：A
> <p> 停止—等待协议的发送窗口和接收窗口大小均为 1，发送方每发送一个分组后必须等待确认，才能发送下一个分组。
> 接收方一次只处理一个分组，因此分组到达的顺序与发送顺序完全一致，一定按序接收。
> <p>后退 N 帧协议中，接收方只按序接收分组。
> 如果某个分组丢失或出错，发送方会重传该分组及之后的所有分组，接收方对乱序到达的分组直接丢弃，确保只有顺序正确的分组被接受，因此也保证按序接收。
> <p>选择重传协议允许接收方缓存乱序到达的分组，即分组到达时可能不是按序的，但接收方会将这些分组暂时存储，等待缺失分组到达后再按序交付给上层。
> 因此，分组到达时不一定按序，不满足“一定按序接收到达的分组”的条件。
> <p>综上，只有停止—等待协议和后退 N 帧协议一定按序接收分组，对应选项 A。
>

##### 35

以下几种 CSMA 协议中，什么协议在监听到介质是空闲时一定发送（ ）。
I. 1-坚持 CSMA
II. p-坚持 CSMA
III. 非坚持 CSMA

A\. 只有 I
B\. I 和 III
C\. I 和 II
D\. I、II 和 III

[tag_link]

正确答案：B
> 本题考查 CSMA 协议的各种监听。
> 1-坚持 CSMA 和非坚持 CSMA 检测到信道空闲时，都立即发送数据帧，它们之间的区别是：如果检测到媒体忙时，是否持续监听媒体（1-坚持）还是等待一个随机的延迟时间后再监听（非坚持）。
> p-坚持 CSMA：当检测到媒体空闲时，该站点以概率 p 的可能性发送数据，而有 1-p 的概率会把发送数据帧的任务延迟到下一个时槽，Ⅱ错误。
>

##### 36

一台主机的 IP 地址为 11.1.1.100，子网掩码为 255.0.0.0。现在用户需要配置该主机的默认路由。经过观察发现，与该主机直接相连的路由器具有如下 4 个 IP 地址和子网掩码：
I. IP 地址：11.1.1.1，子网掩码：255.0.0.0
II. IP 地址：11.1.2.1，子网掩码：255.0.0.0
III. IP 地址：12.1.1.1，子网掩码：255.0.0.0
IV. IP 地址：13.1.2.1，子网掩码：255.0.0.0

A\. I 和 II
B\. I 和 III
C\. I、III 和 IV
D\. III 和 IV

[tag_link]

正确答案：A
> <p> 主机的 IP 地址为 11.1.1.100，子网掩码为 255.0.0.0，其网络地址通过按位与运算得到 11.0.0.0/8。
> 默认路由的网关必须与主机在同一子网内，即网关的网络地址也应为 11.0.0.0/8，这样主机才能直接通信。
> <p>逐一分析路由器选项：
<ul><li>I：IP 地址 11.1.1.1，子网掩码 255.0.0.0，网络地址为 11.0.0.0，与主机相同。
> </li><li>II：IP 地址 11.1.2.1，子网掩码 255.0.0.0，网络地址为 11.0.0.0，与主机相同。
> </li><li>III：IP 地址 12.1.1.1，子网掩码 255.0.0.0，网络地址为 12.0.0.0，与主机不同。
> </li><li>IV：IP 地址 13.1.2.1，子网掩码 255.0.0.0，网络地址为 13.0.0.0，与主机不同。
> </li></ul><p>只有 I 和 II 与主机在同一子网，可能作为默认路由的网关。
> III 和 IV 不在同一子网，主机无法直接可达，因此不能作为默认路由。
> 故正确选项为 A。
>

##### 37

路由器中发现 TTL 值为 0 的分组，将进行（ ）处理，并向源主机返回（ ）的 ICMP 报文。

A\. 返回发送方，源点抑制
B\. 继续转发，改变路由
C\. 丢弃，时间超过
D\. 本地提交，终点不可达

[tag_link]

正确答案：C
> <p>
在 IP 网络中，TTL（生存时间）字段用于限制数据包在网络中的存活跳数。
> 路由器每转发一次分组，TTL 值减 1；
> 当 TTL 值减为 0 时，路由器必须丢弃该分组，以防止其无限循环消耗网络资源。
> <p>丢弃后，路由器会向源主机发送一个 ICMP 时间超过报文（ICMP Type 11），通知源主机该分组因 TTL 超时而被丢弃。
> 这有助于源主机诊断网络路径问题，例如在 traceroute 工具中就是利用这一机制。
> <p>其他选项中：A 的“源点抑制”是 ICMP 用于流量控制的报文；
> B 的“改变路由”是 ICMP 重定向报文，用于提示更优路由；
> D 的“终点不可达”是 ICMP 用于指示目的地无法到达的报文。
> 这些均与 TTL 值为 0 的处理场景无关。
>

##### 38

位于不同子网中的主机之间互相通信，下面说法中正确的是（ ）。

A\. 路由器在转发 IP 数据报时，重新封装源 IP 地址和目的 IP 地址
B\. 路由器在转发 IP 数据报时，重新封装目的 IP 地址和目的硬件地址
C\. 路由器在转发 IP 数据报时，重新封装源硬件地址和目的硬件地址
D\. 源站可以直接进行 ARP 广播得到目的站的硬件地址

[tag_link]

正确答案：C
> <p>
当主机位于不同子网时，通信必须经过路由器转发。
> 路由器在转发 IP 数据报时，保持网络层的源 IP 地址和目的 IP 地址不变（除非进行 NAT），但数据链路层的封装需要更新。
> 具体来说，路由器会解封装接收到的帧，根据路由表确定下一跳，然后重新封装成新的帧，其中源硬件地址（如 MAC 地址）改为路由器出口的地址，目的硬件地址改为下一跳设备（如另一个路由器或目的主机）的地址。
> 因此，选项 C 正确。
> <p>选项 A 和 B 错误，因为标准 IP 路由中不重新封装 IP 地址；
> 选项 D 错误，因为 ARP 广播只能用于同一子网内获取硬件地址，跨子网时源主机通过 ARP 获取默认网关的地址，而非直接获取目的主机的硬件地址。
>

##### 39

下列关于路由器的说法中，正确的是（ ）。

A\. 路由器处理的信息量比交换机少，因而转发速度比交换机快
B\. 对于同一目标，路由器只提供延迟最小的最佳路由
C\. 通常的路由器可以支持多种网络层协议，并提供不同协议之间的分组转换
D\. 路由器不但能够根据 IP 地址进行转发，而且可以根据物理地址进行转发

[tag_link]

正确答案：C
> <p>
<p>关于路由器与交换机的比较，路由器工作在网络层（第三层），负责在不同网络之间基于 IP 地址进行路由选择和分组转发，处理过程涉及路由表查找和决策，因此处理的信息更复杂，转发速度通常比工作在数据链路层（第二层）、基于 MAC 地址快速转发的交换机慢，故选项 A 错误。
> <p>对于路由选择，路由器使用路由协议（如 RIP、OSPF）计算路径，最佳路由的度量标准可能包括延迟、带宽、跳数等多种因素，并非只追求延迟最小，且在实际中可能根据配置提供多条路径或负载均衡，因此选项 B 过于绝对，不正确。
> <p>路由器通常设计为支持多种网络层协议（如 IP、IPX 等），并能处理不同协议的分组，实现跨协议网络的互联，这体现了其多协议处理能力，尽管现代路由器主要专注于 IP 协议，但传统概念上这一说法成立，因此选项 C 正确。
> <p>路由器转发决策依赖于网络层地址（如 IP 地址），而物理地址（MAC 地址）是数据链路层用于局域网内寻址的，由交换机或网卡处理，路由器仅在发送数据到直接相连的网络时需要获取 MAC 地址，但不基于 MAC 地址进行路由转发，故选项 D 错误。
> <p>综上所述，正确选项为 C。
>

##### 40

第一次传输时，设 TCP 的拥塞窗口的慢启动门限初始值为 8（单位为报文段），当拥塞窗口上升到 12 时，网络发生超时，TCP 开始慢启动和拥塞避免，那么第 12 次传输时拥塞窗口大小为（ ）。

A\. 5
B\. 6
C\. 7
D\. 8

[tag_link]

正确答案：B
> <p> 首先，根据 TCP 拥塞控制机制，初始慢启动门限 ssthresh=8，拥塞窗口 cwnd 从 1 开始。
> 在慢启动阶段，cwnd 每轮次翻倍：第 1 次传输 cwnd=1，第 2 次传输 cwnd=2，第 3 次传输 cwnd=4，第 4 次传输 cwnd=8（达到 ssthresh，进入拥塞避免）。
> 拥塞避免阶段每轮次 cwnd 加 1：第 5 次传输 cwnd=9，第 6 次传输 cwnd=10，第 7 次传输 cwnd=11，第 8 次传输 cwnd=12。
> 此时网络发生超时，超时后将 ssthresh 设置为当前 cwnd 的一半，即 12/2=6，cwnd 重置为 1。
> <p>超点后重新开始慢启动：第 9 次传输 cwnd=1，第 10 次传输 cwnd=2，第 11 次传输 cwnd=4。
> 由于此时 cwnd=4 小于 ssthresh=6，仍处于慢启动，但慢启动的目标是使 cwnd 达到 ssthresh，因此从第 11 次传输到第 12 次传输，cwnd 应从 4 增长至 ssthresh 值 6，而不是翻倍到 8。
> 故第 12 次传输时 cwnd=6。
>

---

#### 数据结构

##### 41

（10 分）下图所示是一带权有向图的邻接表。其中出边表中的每个结点均含有三个字段，依次为边的另一个顶点在顶点表中的序号、边上的权值和指向下一个边结点的指针。试求：

（1）该带权有向图的图形。
（2）从顶点 V1 为起点的广度优先搜索的顶点序列及对应的生成树。
（3）以顶点 V1 为起点的深度优先搜索生成树。
（4）由顶点 V1 到顶点 V3 的最短路径。
（5）若将该图看成无向图，用 Prim 算法给出图 G 的一棵最小生成树的生成过程。

[tag_link]

<p>**【解析】**
(1) 该邻接表存储对应的带权有向图如下：
<div class=img-container style=height:auto;width:40% oncontextmenu=return!1> [图片] </div><p>(2) 以顶点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span></span></span></span>
为起点的广度优先搜索的顶点序列依次为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8778em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span></span></span></span>
，对应的生成树如下：
<div class=img-container style=height:auto;width:30% oncontextmenu=return!1> [图片] </div><p>(3) 生成树：顶点集合
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mopen>(</span><span class="mord mathnormal">G</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>}</span></span></span></span>
，边的集合
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=mopen>(</span><span class="mord mathnormal">G</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>)}</span></span></span></span>
。（图略）
<p>(4) V1 到 V3 最短路径为 67: (V1—V4—V3)。
<p>(5) 从 V1 点开始，第一趟寻找 V1 和点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>}</span></span></span></span>
之间的最小权值的边。(V5,V1)。
<p>第二趟寻找点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mclose>}</span></span></span></span>
和点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>}</span></span></span></span>
之间的最小权值的边。(V5,V6)。
<p>第三趟寻找点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>}</span></span></span></span>
和点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mclose>}</span></span></span></span>
之间的最小权值的边。(V1,V4)。
<p>第四趟寻找点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>}</span></span></span></span>
和点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mclose>}</span></span></span></span>
之间的最小权值的边。(V4,V2)。
<p>第五趟寻找点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>}</span></span></span></span>
和点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mclose>}</span></span></span></span>
之间的最小权值的边。(V2,V3)。
<p>所以最小生成树的边集合为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>{(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>6</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>4</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mord>3</span><span class=mclose>)}</span></span></span></span>
（图形略）。
</div><script src=/js/quiz.js defer></script><script>if(typeof window.quizDB=="undefined"){class e{constructor(){this.dbName="QuizCollectionsDB",this.storeName="quizzes",this.version=1,this.db=null}async init(){return new Promise((e,t)=>{const n=indexedDB.open(this.dbName,this.version);n.onerror=()=>t(n.error),n.onsuccess=()=>{this.db=n.result,e(this.db)},n.onupgradeneeded=e=>{const t=e.target.result;if(!t.objectStoreNames.contains(this.storeName)){const e=t.createObjectStore(this.storeName,{keyPath:"id"});e.createIndex("collectedAt","collectedAt",{unique:!1}),e.createIndex("tags","tags",{unique:!1,multiEntry:!0}),e.createIndex("type","type",{unique:!1})}}})}async add(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readwrite"),i=o.objectStore(this.storeName),s=i.add(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async remove(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readwrite"),i=o.objectStore(this.storeName),s=i.delete(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async get(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readonly"),i=o.objectStore(this.storeName),s=i.get(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async getAll(){return this.db||await this.init(),new Promise((e,t)=>{const s=this.db.transaction([this.storeName],"readonly"),o=s.objectStore(this.storeName),n=o.getAll();n.onsuccess=()=>e(n.result),n.onerror=()=>t(n.error)})}async getAllIds(){return this.db||await this.init(),new Promise((e,t)=>{const s=this.db.transaction([this.storeName],"readonly"),o=s.objectStore(this.storeName),n=o.getAllKeys();n.onsuccess=()=>e(n.result),n.onerror=()=>t(n.error)})}}window.quizDB=new e}function toggleSolutionDetail(e,t){const n=document.getElementById("solution-"+t);n&&(n.style.display==="none"||n.style.display===""?(n.style.display="block",e.textContent="隐藏答案与解析"):(n.style.display="none",e.textContent="查看答案与解析"))}async function collectAnswerQuiz(e,t){const s=document.getElementById("quiz-"+e);if(!s)return;let n=s.previousElementSibling;const a=[];let o="";for(;n&&n.tagName!=="H5";)a.unshift(n),n=n.previousElementSibling;n&&n.tagName==="H5"&&(o=n.innerText.trim());const i=a.map(e=>{const t=e.cloneNode(!0);return t.querySelectorAll("button, script, style").forEach(e=>e.remove()),t.outerHTML.trim()}).filter(e=>e.length>0),r=document.getElementById("solution-"+e);let c="";if(r){const e=r.cloneNode(!0);e.querySelectorAll("button, script, style").forEach(e=>e.remove()),c=e.innerHTML.trim()}const l=s.dataset.pageUrl,d=getSubjectFromUrl(l),u={id:e,type:"answer",quizNumber:o,question:i.length>0?i:["题目"],questionText:i.map(e=>{const t=document.createElement("div");return t.innerHTML=e,t.textContent.trim()}).join(`
`),answer:"",explanation:c,tags:s.dataset.tags,subject:d,pageUrl:s.dataset.pageUrl+`/#${o}`,pageTitle:s.dataset.pageTitle+` 第 ${o} 题`,collectedAt:(new Date).toISOString()};try{const n=await window.quizDB.get(e);n?(await window.quizDB.remove(e),t.classList.remove("collected"),t.innerHTML='<i class="fa-regular fa-bookmark"></i> 收藏',t.title="收藏此题",showNotification("已取消收藏")):(await window.quizDB.add(u),t.classList.add("collected"),t.innerHTML='<i class="fa-solid fa-bookmark"></i> 已收藏',t.title="取消收藏",showNotification("已添加到收藏"))}catch(e){console.error("Error managing answer quiz collection:",e),showNotification("操作失败，请重试")}}if(document.addEventListener("DOMContentLoaded",async function(){try{await window.quizDB.init();const e=await window.quizDB.getAllIds();document.querySelectorAll(".answer-container .collect-btn").forEach(t=>{const n=t.closest(".answer-container");n&&e.includes(n.id.replace("quiz-",""))&&(t.classList.add("collected"),t.innerHTML='<i class="fa-solid fa-bookmark"></i> 已收藏',t.title="取消收藏")})}catch(e){console.error("Error initializing answer quiz collections:",e)}}),!document.getElementById("quiz-animations")){const e=document.createElement("style");e.id="quiz-animations",e.textContent=`
    @keyframes slideIn {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
      from { transform: translateX(0); opacity: 1; }
      to { transform: translateX(100%); opacity: 0; }
    }
  `,document.head.appendChild(e)}</script><h5 id=42>42</h5><p>（12 分）假设二叉树采用二叉链表存储结构，设计一个算法求其指定的某一层
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7335em;vertical-align:-.0391em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
）的叶子结点个数，要求：
（1）给出算法的基本设计思想。
（2）写出二叉树采用的存储结构代码。
（3）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-2 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-2")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-2",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 42

（12 分）假设二叉树采用二叉链表存储结构，设计一个算法求其指定的某一层
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7335em;vertical-align:-.0391em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
）的叶子结点个数，要求：
（1）给出算法的基本设计思想。
（2）写出二叉树采用的存储结构代码。
（3）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

[tag_link]

<p>**【答案】**
<p>（1）算法的基本设计思想：采用递归先序遍历二叉树，遍历时记录当前节点所在层数。若当前层数等于指定层数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
，则判断该节点是否为叶子结点（左右孩子均为空），若是则计数器加 1；若当前层数小于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
，则递归遍历其左右子树；若当前层数大于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
，则停止向下递归。最终累计得到第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
层的叶子结点个数。
<p>（2）二叉树采用的二叉链表存储结构代码：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#204a87;font-weight:700>typedef</span> <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>char</span> <span style=color:#000>data</span><span style=color:#000;font-weight:700>;</span>                    <span style=color:#8f5902;font-style:italic>// 结点数据，假设为字符型
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>;</span> <span style=color:#8f5902;font-style:italic>// 左右孩子指针
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span> <span style=color:#000>BiTNode</span><span style=color:#000;font-weight:700>,</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>BiTree</span><span style=color:#000;font-weight:700>;</span>
</span></span>`</pre></div><p>（3）算法描述（C 语言）：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 函数功能：计算二叉树 T 中第 k 层的叶子结点个数
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 参数：T 为二叉树根结点指针，currentLevel 为当前结点所在层数（根结点为第 1 层），k 为指定层数
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 返回值：第 k 层的叶子结点个数
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>countLeafAtLevel</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>BiTree</span> <span style=color:#000>T</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>currentLevel</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>T</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#204a87>NULL</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span> <span style=color:#8f5902;font-style:italic>// 空树，返回 0
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>return</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>currentLevel</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span> <span style=color:#8f5902;font-style:italic>// 到达第 k 层
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#8f5902;font-style:italic>// 判断是否为叶子结点
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>T</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>lchild</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#204a87>NULL</span> <span style=color:#ce5c00;font-weight:700>&&</span> <span style=color:#000>T</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>rchild</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#204a87>NULL</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>return</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>return</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>currentLevel</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span> <span style=color:#8f5902;font-style:italic>// 当前层小于 k，继续向下递归
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>countLeafAtLevel</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>T</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>currentLevel</span> <span style=color:#ce5c00;font-weight:700>+</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>)</span> <span style=color:#ce5c00;font-weight:700>+</span>
</span></span><span style=display:flex><span>               <span style=color:#000>countLeafAtLevel</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>T</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>currentLevel</span> <span style=color:#ce5c00;font-weight:700>+</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000;font-weight:700>{</span> <span style=color:#8f5902;font-style:italic>// 当前层大于 k，不再递归
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>return</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 调用示例：int leafCount = countLeafAtLevel(root, 1, k);
</span></span></span>`</pre></div><p>**【解析】**
<p>算法设计思想解析：由于需要统计二叉树中指定层
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
的叶子结点个数，采用深度优先搜索（DFS）策略，通过递归遍历二叉树并在过程中跟踪当前层数。当层数等于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
时，判断当前结点是否为叶子结点并进行计数；若层数小于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
，则继续递归遍历左右子树；若层数大于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
，则提前返回，避免无效访问。这种方法只需遍历一次二叉树，且在层数超过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
时停止递归，提高了效率。
<p>存储结构采用标准的二叉链表，每个结点包含数据域和指向左右子树的指针，便于递归操作。
<p>算法实现时，递归终止条件包括：结点为空时返回 0；当前层数等于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
时，根据叶子结点定义返回 1 或 0；当前层数小于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
时，递归计算左右子树的叶子结点数之和；当前层数大于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
时直接返回 0。该算法的时间复杂度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
，最坏情况下需访问所有结点（当
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
大于等于树高时）；空间复杂度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">h</span><span class=mclose>)</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">h</span></span></span></span>
为树的高度，即递归栈的深度。注意题目中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7335em;vertical-align:-.0391em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，但算法对
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
同样适用，调用时传入 currentLevel=1 即可。
</div><h5 id=43>43</h5><p>（11 分）已知两个实数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>8.25</span></span></span></span>
，它们在 C 语言中定义为 float 型变量，分别存放在寄存器 A 和 B 中。另外，还有两个寄存器 C 和 D。A、B、C、D 都是 32 位的寄存器。请问下列问题（要求用十六进制表示二进制序列）：
（1）寄存器 A 和 B 中的内容分别是什么？
（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相加后的结果存放在 C 寄存器中，寄存器 C 中的内容是什么？
（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相减后的结果存放在 D 寄存器中，寄存器 D 中的内容是什么？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-3 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-3")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-3",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机组成原理

##### 43

（11 分）已知两个实数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>8.25</span></span></span></span>
，它们在 C 语言中定义为 float 型变量，分别存放在寄存器 A 和 B 中。另外，还有两个寄存器 C 和 D。A、B、C、D 都是 32 位的寄存器。请问下列问题（要求用十六进制表示二进制序列）：
（1）寄存器 A 和 B 中的内容分别是什么？
（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相加后的结果存放在 C 寄存器中，寄存器 C 中的内容是什么？
（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相减后的结果存放在 D 寄存器中，寄存器 D 中的内容是什么？

[tag_link]

<p>**【答案】**
（1）寄存器 A 中的内容为 0xC2880000，寄存器 B 中的内容为 0xC1040000。
（2）寄存器 C 中的内容为 0xC2988000。
（3）寄存器 D 中的内容为 0xC26F0000。
<p>**【解析】**
对于浮点数采用 IEEE 754 单精度格式（32 位），其中包含 1 位符号位、8 位指数位（偏移量 127）和 23 位尾数位。
<p>**（1）对于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>68</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1000100</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.000100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>133</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000101</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为隐藏最高位 1 后的小数部分
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>000100</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00010000000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000010100010000000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>2880000</span></span></span></span>
。</li></ul><p>**对于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>8.25</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>8.25</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1000.01</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.00001</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>130</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000010</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00001</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00001000000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000001000001000000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>1040000</span></span></span></span>
。</li></ul><p>**（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>68</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>8.25</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>76.25</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>76.25</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1001100.01</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.00110001</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>133</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000101</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00110001</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>00110001000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000010100110001000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>2988000</span></span></span></span>
。</li></ul><p>**（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>68</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>8.25</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>59.75</span></span></span></span>
：**
<ul><li>符号位
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">s</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
（负数）。</li><li>绝对值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>59.75</span></span></span></span>
的二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>111011.11</span></span></span></span>
，科学计数法表示为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.1101111</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">5</span></span></span></span></span></span></span></span></span></span></span></span>
，指数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>5</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>127</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>132</span></span></span></span>
，二进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10000100</span></span></span></span>
。</li><li>尾数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1101111</span></span></span></span>
，扩展至 23 位得到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11011110000000000000000</span></span></span></span>
。</li><li>组合得到二进制
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>11000010011011110000000000000000</span></span></span></span>
，十六进制为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord mathnormal">x</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>26</span><span class="mord mathnormal" style=margin-right:.13889em>F</span><span class=mord>0000</span></span></span></span>
。</li></ul></div><h5 id=44>44</h5><p>（12 分）现有 4 级流水线，分别完成取指、指令译码并取数、运算、回写四步操作。假设完成各部操作的时间依次为 100ns、100ns、80ns、50ns。请问：
（1）流水线的操作周期应设计为多少？
（2）若相邻两条指令如下，发生数据相关，而且在硬件上不采取措施，那么第 2 条指令要推迟多少时间进行？
<pre tabindex=0><code class=language-assembly data-lang=assembly>ADD R1, R2, R3     # R2 + R3 -> R1
SUB R4, R1, R5     # R1 - R5 -> R4
`</pre><p>（3）如果在硬件设计上加以改进，至少需要推迟多少时间？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 44

（12 分）现有 4 级流水线，分别完成取指、指令译码并取数、运算、回写四步操作。假设完成各部操作的时间依次为 100ns、100ns、80ns、50ns。请问：
（1）流水线的操作周期应设计为多少？
（2）若相邻两条指令如下，发生数据相关，而且在硬件上不采取措施，那么第 2 条指令要推迟多少时间进行？

（3）如果在硬件设计上加以改进，至少需要推迟多少时间？

[tag_link]

<p>**【解析】**
(1) 流水线操作的时钟周期
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span></span></span></span>
应按四步操作中的最长时间来考虑，所以
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
。
<p>(2) 两条指令在流水线中执行情况如下表所示：
<table><thead><tr><th>指令</th><th>时钟 1</th><th>时钟 2</th><th>时钟 3</th><th>时钟 4</th><th>时钟 5</th><th>时钟 6</th><th>时钟 7</th></tr></thead><tbody><tr><td>ADD</td><td>取指</td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td><td></td><td></td></tr><tr><td>SUB</td><td></td><td>取指</td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td><td></td></tr></tbody></table><p>ADD 指令在时钟 4 时将结果写入寄存器堆 (R1)，但 SUB 指令在时钟 3 时读寄存器堆 (R1)。本来 ADD 指令应先写入 R1，SUB 指令后读 R1，结果变成 SUB 指令先读 R1，ADD 指令后写 R1，因而发生两条指令间数据相关。如果硬件上不采取措施，第 2 条指令 SUB 至少应推迟 2 个操作时钟周期（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
），即将 SUB 指令中的指令译码并取数阶段推迟到 ADD 指令的写回阶段之后才能保证不会出错。如下表所示：
<table><thead><tr><th>指令</th><th>时钟 1</th><th>时钟 2</th><th>时钟 3</th><th>时钟 4</th><th>时钟 5</th><th>时钟 6</th><th>时钟 7</th></tr></thead><tbody><tr><td>ADD</td><td>取指</td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td><td></td><td></td></tr><tr><td>SUB</td><td></td><td>取指</td><td></td><td></td><td>指令译码并取数</td><td>运算</td><td>写回</td></tr></tbody></table><p>(3) 如果硬件上加以改进，可只延迟 1 个操作时钟周期（100ns）。因为在 ADD 指令中，运算阶段就已经得到结果了，因此可以通过数据旁路技术在运算结果一得到的时候将结果快速送入寄存器 R1，而不需要等到写回阶段完成。流水线中执行情况如下图所示：
<table><thead><tr><th>时钟</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr></thead><tbody><tr><td>ADD</td><td>取指</td><td>指令译码并取数</td><td>运算（并采用数据旁路技术写入寄存器 R1）</td><td>写回</td><td></td><td></td><td>取指</td></tr><tr><td>SUB</td><td></td><td>取指</td><td></td><td>指令译码并取数</td><td>运算</td><td>写回</td><td></td></tr></tbody></table></div><h5 id=45>45</h5><p>（7 分）一个主修动物行为学、辅修计算机科学的学生参加了一个课题。调查花果山的猴子是否能被教会理解死锁。他找到一处峡谷，横跨峡谷拉了一根绳索（假设为南北方向），这样猴子就可以攀着绳索越过峡谷。只要它们朝着相同的方向，同
<p>一时刻可以有多只猴子通过。但是如果是相反的方向上同时有猴子通过则会发生死锁（这些猴子将被卡在绳索中间，假设这些猴子无法在绳索上从另一只猴子身上翻过去）。如果一只猴子想越过峡谷，它必须看当前是否有别的猴子在逆向通过。请用 P、V 操作来解决该问题。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-5 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-5")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-5",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 操作系统

##### 45

（7 分）一个主修动物行为学、辅修计算机科学的学生参加了一个课题。调查花果山的猴子是否能被教会理解死锁。他找到一处峡谷，横跨峡谷拉了一根绳索（假设为南北方向），这样猴子就可以攀着绳索越过峡谷。只要它们朝着相同的方向，同

一时刻可以有多只猴子通过。但是如果是相反的方向上同时有猴子通过则会发生死锁（这些猴子将被卡在绳索中间，假设这些猴子无法在绳索上从另一只猴子身上翻过去）。如果一只猴子想越过峡谷，它必须看当前是否有别的猴子在逆向通过。请用 P、V 操作来解决该问题。

[tag_link]

<p>**【答案】**
信号量定义：
<ul><li>mutex：初值为 1，用于保护共享变量。</li><li>rope：初值为 1，用于控制绳索的访问。</li></ul><p>共享变量：
<ul><li>SN_count：从南向北的猴子数量，初值为 0。</li><li>NS_count：从北向南的猴子数量，初值为 0。</li></ul><pre tabindex=0>`semaphore mutex = 1;
semaphore rope = 1;
semaphore SN_count = 0;
semaphore NS_count = 0;
`</pre><p>从南向北的猴子执行以下操作：
<pre tabindex=0>`south_monkey() {
    P(mutex)
    SN_count++
    if (SN_count == 1) P(rope)
    V(mutex)

    // 通过绳索

    P(mutex)
    SN_count--
    if (SN_count == 0) V(rope)
    V(mutex)
}
`</pre><p>从北向南的猴子执行以下操作：
<pre tabindex=0>`north_monkey() {
    P(mutex)
    NS_count++
    if (NS_count == 1) P(rope)
    V(mutex)

    // 通过绳索

    P(mutex)
    NS_count--
    if (NS_count == 0) V(rope)
    V(mutex)
}
`</pre><p>**【解析】**
该问题本质上是单车道桥梁同步问题的变体，需要防止两个方向的猴子同时使用绳索导致死锁，同时允许同一方向的多只猴子共享绳索。使用 P、V 操作（信号量）来实现同步。
<p>首先，定义信号量 mutex 用于互斥访问共享变量 SN_count 和 NS_count，确保计数操作原子性。信号量 rope 用于控制绳索的访问权限，初值为 1 表示绳索空闲。
<p>对于从南向北的猴子：当第一只猴子到达时，在 mutex 保护下增加 SN_count，由于 SN_count 从 0 变为 1，它执行 P(rope) 获取绳索访问权，阻止北向南的猴子进入。之后释放 mutex，允许其他南向北猴子进入，它们增加 SN_count 但不会再次 P(rope)，因此同一方向多只猴子可以同时通过绳索。当猴子通过后，在 mutex 保护下减少 SN_count，如果 SN_count 变为 0，表示该方向没有猴子了，则执行 V(rope) 释放绳索访问权，允许另一方向猴子使用。
<p>对于从北向南的猴子，操作对称：第一只猴子获取 rope，后续猴子共享访问，最后一只猴子释放 rope。
<p>这种设计确保：只要有一个方向的猴子在使用绳索，rope 信号量就被持有，另一方向的猴子会在执行 P(rope) 时阻塞，直到当前方向所有猴子离开并释放 rope。因此，相反方向的猴子不会同时通过，避免了死锁。同一方向的猴子可以共享绳索，符合问题要求。整个过程通过 P、V 操作实现了同步，且不会产生饥饿，除非一个方向持续有猴子到达，但问题未要求公平性，故解法可行。
</div><h5 id=46>46</h5><p>（8 分）在某段式存储管理系统中，逻辑地址为 32 位，其中高 16 位为段号，低 16 位为段内偏移量，以下是段表（其中的地址均为 16 进制）：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:10.84em;vertical-align:-5.15em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.69em><span style=top:-7.65em><span class=pstrut style=height:7.65em></span><span class=mtable><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">段</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>3</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5</span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>6</span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>7</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">基地址</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>10000</span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11900</span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11</span><span class="mord mathnormal" style=margin-right:.02778em>D</span><span class=mord>00</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11</span><span class="mord mathnormal" style=margin-right:.13889em>F</span><span class=mord>00</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>13000</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">长度</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>18</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mord>0</span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>3</span><span class="mord mathnormal" style=margin-right:.13889em>FF</span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span><span class="mord mathnormal" style=margin-right:.13889em>FF</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1000</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>FFF</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.65em><span style=top:-7.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">保护</span></span></span></span><span style=top:-6.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">只读</span></span></span></span><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">只读</span></span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">读</span><span class=mord>/</span><span class="mord cjk_fallback">写</span></span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">禁止访问</span></span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">读</span><span class=mord>/</span><span class="mord cjk_fallback">写</span></span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">禁止访问</span></span></span></span><span style=top:.59em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">禁止访问</span></span></span></span><span style=top:1.79em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">读</span><span class=mord>/</span><span class="mord cjk_fallback">写</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.8em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-5.15em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:7.65em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-12.1em><span class=pstrut style=height:7.65em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-13.3em><span class=pstrut style=height:7.65em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:5.15em><span></span></span></span></span></span></span></span></span></span></div><p>以下是代码段的内容（代码前的数字表示存放代码的十六进制逻辑地址）：
<pre tabindex=0>`main
240  push x[10108H]
244  call sin
248  ...

sin
360  mov r2,4+(sp)
364  ...
368  ret
`</pre><p>试问：
<p>（1）x 的逻辑地址为 10108H，它的物理地址是多少？要求给出具体的计算过程。
（2）若栈指针 SP 的当前值为 70FF0H，push x 指令的执行过程：先将 SP 减 4，然后存储 x 的值。试问存储 x 的物理地址是多少？
（3）call sin 指令的执行过程：先将当前 PC 值入栈，然后在 PC 内装入目标 PC 值。请问：哪个值被压入栈了？新的 SP 指针的值是多少？新的 PC 值是多少？
（4）“mov r2,4+(SP)”的功能是什么？（假设指令集与 x86 系列 CPU 相同）
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 46

（8 分）在某段式存储管理系统中，逻辑地址为 32 位，其中高 16 位为段号，低 16 位为段内偏移量，以下是段表（其中的地址均为 16 进制）：

以下是代码段的内容（代码前的数字表示存放代码的十六进制逻辑地址）：

试问：

（1）x 的逻辑地址为 10108H，它的物理地址是多少？要求给出具体的计算过程。
（2）若栈指针 SP 的当前值为 70FF0H，push x 指令的执行过程：先将 SP 减 4，然后存储 x 的值。试问存储 x 的物理地址是多少？
（3）call sin 指令的执行过程：先将当前 PC 值入栈，然后在 PC 内装入目标 PC 值。请问：哪个值被压入栈了？新的 SP 指针的值是多少？新的 PC 值是多少？
（4）“mov r2,4+(SP)”的功能是什么？（假设指令集与 x86 系列 CPU 相同）

[tag_link]

<p>**【解析】**
本题考查逻辑地址和物理地址的转换等。
<p>(1) 高 16 位为段号，低 16 位为段内偏移，则 1 为段号（对应基地址为 11900H），0108H 为段内偏移量，则逻辑地址 10108H 对应的物理地址为 11900H + 0108H = 11A08H。
<p>(2) SP 的当前值为 70FF0H 中，先减 4H 后得 70FECH，7 为段号，0FECH 为段内偏移量，则对应的物理地址为 13000H + 0FECH = 13FECH，故存储 x 的物理地址为 13FECH。
<p>(3) 在调用 call sin 指令后，PC 自增为 248，所以逻辑地址 248 被压入栈。由 (2) 可知每次入栈时 SP 指针先减 4，因此当前 PC 值入栈后，SP 指针的值为 70FF0H - 4H - 4H = 70FE8H，故新的 SP 指针值为 70FE8H，新的 PC 值为转移指令的目的地址 360H。
<p>注意：有同学会问为什么入栈的不是物理地址？
<p>首先段式存储器（页式、段页式也一样）中 PC 的值一定是逻辑地址，然后取指令时系统才按照逻辑地址根据一定的规则转换为物理地址再去访问内存。所以入栈的是 PC 的内容，当然就是逻辑地址。
<p>(4) 70FE8(sp) + 4 = 70FECH，即 x 在栈中的逻辑地址（call sin 之前刚被 push 进去的），故其功能是把 x 的值送入寄存器 2，作为 sin 函数的参数。
</div><h5 id=47>47</h5><p>（9 分）在本地主机使用 Ping 命令测试与远端主机 192.168.0.101 的连通性，Ping 测试仅进行了一次，由于测试数据较大，在 IP 层进行了数据分片。Ping 命令执行时，使用 Sniffer 工具捕获本机以太网发送方向的所有通信流量，得到 6 个 IP 数据报，表 1 以 16 进制格式逐字节给出了六个 IP 数据报的前 40 个字节。
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord text"><span class=mspace style=margin-right:2em></span><span class="mord text"><span class="mord textbf cjk_fallback">表</span><span class="mord textbf"> 1 Sniffer </span><span class="mord textbf cjk_fallback">捕获到的</span><span class="mord textbf"> IP </span><span class="mord textbf cjk_fallback">数据报</span></span><span class=mord> </span><span class=mspace style=margin-right:2em></span></span></span></span></span></span></div><div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:28.24em;vertical-align:-13.85em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:14.39em><span style=top:-16.35em><span class=pstrut style=height:16.35em></span><span class=mtable><span class=vertical-separator style="height:28.2em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-13.85em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:14.35em><span style=top:-18.01em><span class=pstrut style=height:4.5em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">编号</span></span></span></span><span style=top:-15.15em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord>1</span></span></span><span style=top:-10.65em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-6.15em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord>3</span></span></span><span style=top:-1.65em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord>4</span></span></span><span style=top:2.85em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord>5</span></span></span><span style=top:7.35em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord>6</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:13.85em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:28.2em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-13.85em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:14.35em><span style=top:-18.01em><span class=pstrut style=height:4.5em></span><span class=mord><span class="mord text"><span class=mord>IP </span><span class="mord cjk_fallback">数据报前</span><span class=mord> 40 </span><span class="mord cjk_fallback">字节（每行</span><span class=mord> 16 </span><span class="mord cjk_fallback">字节，</span><span class=mord>4 </span><span class="mord cjk_fallback">字节一组）</span></span></span></span><span style=top:-15.15em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-3em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-1.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>45 00 05 DC </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 8F 04 20 00 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 39 0F 4B 52 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> C0 A8 00 15</span></span></span></span><span style=top:-3.16em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>C0 A8 00 65 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 08 00 32 7E </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 04 00 C1 04 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 61 62 63 64</span></span></span></span><span style=top:-1.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>65 66 67 68 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 69 6A 6B 6C</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span></span></span></span></span><span style=top:-10.65em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-3em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-1.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>45 00 02 80 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 8F F9 00 00 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 71 01 37 1D </span><span class=mspace style=margin-right:.2777em></span><span class=mord> C0 A8 00 15</span></span></span></span><span style=top:-3.16em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>C0 A8 00 01 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 08 00 AF 7D </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 04 00 CE 04 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 61 62 63 64</span></span></span></span><span style=top:-1.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>65 66 67 68 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 69 6A 6B 6C</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span></span></span></span></span><span style=top:-6.15em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-3em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-1.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>45 00 00 58 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 8F FA 40 00 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 80 06 E9 DA </span><span class=mspace style=margin-right:.2777em></span><span class=mord> C0 A8 00 15</span></span></span></span><span style=top:-3.16em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>C0 A8 00 02 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 04 2E 00 16 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 98 DE BE B3 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> AC 74 A0 86</span></span></span></span><span style=top:-1.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>50 18 3B 08 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> BC F5 00 F5</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span></span></span></span></span><span style=top:-1.65em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-3em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-1.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>45 00 05 DC </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 8F 04 20 B9 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 39 01 4A 99 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> C0 A8 00 15</span></span></span></span><span style=top:-3.16em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>C0 A8 00 65 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 61 62 63 64 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 65 66 67 68 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 69 6A 6B 6C</span></span></span></span><span style=top:-1.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>6D 6E 6F 70 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 71 72 73 74</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span></span></span></span></span><span style=top:2.85em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-3em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-1.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>45 00 05 9B </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 8F 04 01 72 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 39 01 6A 21 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> C0 A8 00 15</span></span></span></span><span style=top:-3.16em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>C0 A8 00 65 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 69 6A 6B 6C </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 6D 6E 6F 70 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 71 72 73 74</span></span></span></span><span style=top:-1.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>75 76 77 61 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 62 63 64 65</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span></span></span></span></span><span style=top:7.35em><span class=pstrut style=height:4.5em></span><span class=mord><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-3em><span class=pstrut style=height:2.84em></span><span class=mord></span></span><span style=top:-1.5em><span class=pstrut style=height:2.84em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.5em><span style=top:-4.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>45 00 00 58 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 8F 05 40 00 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 80 06 E9 CF </span><span class=mspace style=margin-right:.2777em></span><span class=mord> C0 A8 00 15</span></span></span></span><span style=top:-3.16em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>C0 A8 00 79 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 04 2E 00 16 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 98 DE BF 43 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> AC 74 E1 A6</span></span></span></span><span style=top:-1.66em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class="mord text"><span class=mord>50 18 3F D0 </span><span class=mspace style=margin-right:.2777em></span><span class=mord> 17 1A 00 00</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2em><span></span></span></span></span></span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:13.85em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:28.2em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-13.85em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-7em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-11.5em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-16em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-20.5em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-25em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-29.5em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-30.7em><span class=pstrut style=height:16.35em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:13.85em><span></span></span></span></span></span></span></span></span></span></div><p>IP 分组头的结构如图 1 所示。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-9e7e0d9f109c06ee1f6420b3463666a5-7 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/5/ data-page-title="模拟卷 5"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-9e7e0d9f109c06ee1f6420b3463666a5-7")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-9e7e0d9f109c06ee1f6420b3463666a5-7",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机网络

##### 47

（9 分）在本地主机使用 Ping 命令测试与远端主机 192.168.0.101 的连通性，Ping 测试仅进行了一次，由于测试数据较大，在 IP 层进行了数据分片。Ping 命令执行时，使用 Sniffer 工具捕获本机以太网发送方向的所有通信流量，得到 6 个 IP 数据报，表 1 以 16 进制格式逐字节给出了六个 IP 数据报的前 40 个字节。

IP 分组头的结构如图 1 所示。

[tag_link]

<p>**【解析】**
(1) Ping 命令测试的远端主机的地址即为目的地址，根据 IP 数据报的格式，找第 16 个字节开始的 C0 A8 00 65，即 192.168.0.101，则找出标识号一致、协议号一致的 IP 分组，所以，1、4、5 号数据报是该次 Ping 测试产生的。
<p>(2) 本机 IP 地址为第 12～15 个字节，即 C0 A8 00 15，转换成二进制为 192.168.0.21。根据 IP 分组头格式，从第 13 个字节开始，找到 TTL=0x39，即为二进制的 57。
<p>(3) 在 1、4、5 号数据报中，由 MF 位知，第 5 个数据报是分片的最后一片（MF=1，表示后面还有分片；MF=0，表示后面没有分片），由各个数据报中的总长度域（或由片偏移）知，1、4 号数据报的总长度均为 0x05DC=1500 字节，头部长度=5×4=20 字节，故净荷长度=1480 字节；5 号数据报的净荷长度=0x059B-20=1435-20=1415 字节，所以分片前的净荷=1480+1480+1415=4375，总长度=净荷+头部 20 字节=4375+20=4395 字节。

---
