# 408 计算机学科专业基础综合模拟卷 4

#### 数据结构

##### 1

若循环队列以数组 `Q[0..m-1]` 为其存储结构，变量 `rear` 表示循环队列中的队尾元素的实际位置，其移动按 `rear=(rear+1) MOD m` 进行，变量 `length` 表示当前循环队列中的元素个数，则循环队列的队首元素的实际位置是（ ）。

A\. `rear-length`
B\. `(rear-length+m) MOD m`
C\. `(1+rear-m-length) MOD m`
D\. `(rear-length-1) MOD m`

[tag_link]

正确答案：C
> <p> 循环队列中，队尾元素的位置由 `rear` 给出，队列当前元素个数为 `length`。
> 设��首元素的位置为 `front`，由于队列元素从 `front` 连续存储到 `rear`（考虑循环），因此 `rear` 与 `front` 满足关系：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord text"><span class=mord>rear</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord text"><span class=mord>front</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord text"><span class=mord>length</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span></span></div><p>解出 `front`，得：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord text"><span class=mord>front</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord text"><span class=mord>rear</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord text"><span class=mord>length</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span></span></div><p>选项 C 的表达式为 `(1 + rear - m - length) MOD m`，可化简为：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord text"><span class=mord>rear</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord text"><span class=mord>length</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">m</span><span class=mclose>)</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span></span></div><p>在模
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
运算下，减去
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
不改变余数，因此该表达式等价于：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord text"><span class=mord>rear</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord text"><span class=mord>length</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span></span></div><p>与推导结果一致。
> <p>通过实例验证：设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>10</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord text"><span class=mord>rear</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord text"><span class=mord>length</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
，则队首应为位置 9。
> 计算选项 C：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>5</span><span class=mclose>)</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>10</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>−</span><span class=mord>11</span><span class=mclose>)</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>10</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span></span></span></span></span></div><p>结果正确；
> 而其他选项均不满足。
> 因此，循环队列的队首元素实际位置为选项 C。
>

##### 2

若一个栈以向量 `V[1..n]` 存储，初始栈顶指针 `top` 为 `n+1`，则 `x` 进栈的正确操作是（ ）。

A\. `top=top+1; V[top]=x`
B\. `V[top]=x; top=top+1`
C\. `top=top-1; V[top]=x`
D\. `V[top]=x; top=top-1`

[tag_link]

正确答案：C
> <p>
栈以向量 `V[1..n]` 存储，初始栈顶指针 `top` 为 `n+1`，这表示栈为空且栈从数组末端向开头方向增长。
> 因为向量有效索引是 `1` 到 `n`，`top` 初始值 `n+1` 是一个无效位置，意味着栈底在索引 `n` 附近，栈顶指针向索引 `1` 方向移动。
> <p>进栈操作需要将元素 `x` 存入向量的有效位置，并更新栈顶指针指向新栈顶。
> 正确步骤应是先减小 `top` 指针，使其指向一个有效索引（如从 `n+1` 减到 `n`），然后将 `x` 存入该位置。
> 这样，栈顶元素位于 `V[top]`，`top` 指向当前栈顶。
> <p>分析选项：
<ul><li>**A** 和 **B** 中 `top` 增加会导致越界访问；
> </li><li>**D** 先存入 `x` 但初始 `top` 为 `n+1`，直接访问 `V[n+1]` 越界；
> </li><li>只有 **C** 先执行 `top = top - 1` 使指针有效，再执行 `V[top] = x`，符合栈的操作逻辑。
> </li></ul><p>因此，**C** 是正确操作。
>

##### 3

若一棵深度为 6 的完全二叉树的第 6 层有 3 个叶子结点，则该二叉树共有（ ）个叶子结点。

A\. 17
B\. 18
C\. 19
D\. 20

[tag_link]

正确答案：A
> 深度为 6 的完全二叉树，前 5 层必须是满二叉树，因此第 5 层有 2^(5-1)=16 个结点。
> 第 6 层有 3 个叶子结点，由于第 6 层是最底层，所有结点都是叶子结点，且这 3 个结点对应第 5 层前两个结点的子结点：第 5 层第 1 个结点有左右子结点，第 5 层第 2 个结点有左子结点。
> 因此，第 5 层中只有前两个结点有子结点，其余 14 个结点均无子结点，为叶子结点。
> 叶子结点总数等于第 6 层的 3 个加上第 5 层的 14 个，共 17 个。
>

##### 4

在一棵非空二叉树的中序遍历序列中，根结点的右边（ ）。

A\. 只有右子树上的所有结点
B\. 只有右子树上的部分结点
C\. 只有左子树上的部分结点
D\. 只有左子树上的所有结点

[tag_link]

正确答案：A
> 中序遍历二叉树的顺序是：先遍历左子树，然后访问根结点，最后遍历右子树。
> 因此，在中序遍历序列中，根结点的左边包含左子树上的所有结点，而根结点的右边包含右子树上的所有结点。
> 选项 A 正确描述了根结点右边只有右子树上的所有结点；
> 其他选项不符合中序遍历的定义。
>

##### 5

某二叉树结点的中序序列为 BDAECF，后序序列为 DBEFCA，则该二叉树对应的森林包括（ ）棵树。

A\. 1
B\. 2
C\. 3
D\. 4

[tag_link]

正确答案：C
> <p> 考查由遍历序列确定二叉树、森林与二叉树的转换。
> 根据后序序列，A 是二叉树的根结点。
> 根据中序遍历序列，则二叉树的形态一定如下图左所示。
> 对于 A 的左子树，由后序序列可知，因为 B 比 D 后被访问，因此，B 必为 D 的父结点，又由中序序列可知，D 是 B 的右儿子。
> 对于 A 的右子树，同理可确定结点 E、C、F 的关系。
> 此二叉树的形态如下图右所示。
> <div class=img-container style=height:auto;width:80% oncontextmenu=return!1><img src=/images/408simulate/4_5_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1></div><p>再根据二叉树与森林的对应关系。
> 森林中树的棵数即为其对应二叉树（向右上旋转 45° 后）中根结点 A 及其“右兄弟”数。
> 可知此森林中有 3 棵树，根结点分别为 A、C 和 F。
>

##### 6

在具有 n 个顶点的图 G 中，若最小生成树不唯一，则（ ）。

A\. G 的边数一定大于 n-1
B\. G 的权值最小的边一定有多条
C\. G 的最小生成树代价不一定相等
D\. 上述选项都不对

[tag_link]

正确答案：A
> 最小生成树（MST）不唯一意味着图 G 中存在至少两个不同的生成树，它们的总权值相同且都是最小的。
> 选项 A 指出 G 的边数一定大于 n-1。
> 这是因为如果图 G 的边数等于 n-1，则 G 本身是一棵树，其生成树唯一，与 MST 不唯一矛盾。
> 因此，要存在多个 MST，图 G 必须有多余的边，即边数至少为 n，故边数大于 n-1 必然成立。
> 选项 B 错误，因为 MST 不唯一并不要求权值最小的边有多条。
> 例如，一个包含三个顶点、边权分别为 1、2、2 的图，最小权值边只有一条（权值 1），但存在两个 MST（总权值均为 3）。
> 选项 C 错误，因为所有最小生成树的代价必须相等，否则其中代价较大的就不是“最小”生成树。
> 综上，选项 A 正确。
>

##### 7

以下关于图的表述中，正确的是（ ）。

A\. 强连通有向图的任何顶点到其他所有顶点都有弧
B\. 图与树的区别在于图的边数大于或等于顶点数
C\. 无向图的连通分量指无向图中的极大连通子图
D\. 假设有图
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">G</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⟨</span><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>{</span><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=mclose>}⟩</span></span></span></span>
，顶点集
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8879em;vertical-align:-.136em></span><span class=mord><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⊆</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.22222em>V</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8879em;vertical-align:-.136em></span><span class=mord><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⊆</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
，则
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7519em></span><span class=mord><span class="mord mathnormal" style=margin-right:.22222em>V</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0019em;vertical-align:-.25em></span><span class=mopen>{</span><span class=mord><span class="mord mathnormal" style=margin-right:.05764em>E</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7519em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class=mclose>}</span></span></span></span>
构成
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">G</span></span></span></span>
的子图。

[tag_link]

正确答案：C
> <p>
首先分析选项 A：强连通有向图要求任意两个顶点之间存在双向路径，但并不要求直接有弧（即直接的边）。
> 例如，一个包含三个顶点的有向环，顶点间通过路径相连而非都有直接弧，因此该表述错误。
> <p>接着看选项 B：图与树的区别在于树是无环连通图，且对于 n 个顶点的树，边数为 n-1。
> 图的边数可以小于、等于或大于顶点数，例如孤立顶点图边数少于顶点数，因此该表述不准确。
> <p>选项 C 正确，因为无向图的连通分量定义为极大连通子图，即不能再添加其他顶点和边而保持连通的子图，这是图论中的标准概念。
> <p>最后检查选项 D：子图需要顶点集 V&rsquo;⊆V 和边集 E&rsquo;⊆E，且 E&rsquo;中边的端点必须都在 V&rsquo;中。
> 选项仅说明 V&rsquo;和 E&rsquo;是子集，未强调边的端点限制，因此表述不完整，错误。
> <p>综上，正确选项为 C。
>

##### 8

在关键字随机分布的情况下，用二分查找树的方法进行查找，其平均查找长度与（ ）量级相当。

A\. 顺序查找
B\. 折半查找
C\. 分块查找
D\. 散列查找

[tag_link]

正确答案：B
> 在关键字随机分布的情况下，构建的二分查找树（BST）通常趋于平衡，树的高度平均为 O(log n)，其中 n 是关键字的数量。
> 因此，使用二分查找树进行查找的平均查找长度（ASL）量级为 O(log n)。
> 折半查找（即二分查找）在有序数组上进行，每次比较后将搜索范围减半，其平均查找长度也是 O(log n) 量级。
> 顺序查找的 ASL 为 O(n)，分块查找的 ASL 介于顺序查找和折半查找之间，通常优于 O(n) 但不如 O(log n)，而散列查找在理想情况下 ASL 为 O(1)。
> 因此，二分查找树在随机分布下的平均查找长度与折半查找同属于对数量级。
>

##### 9

一组数据 (30,20,10,15,35,1,10,5)，用堆排序（小顶堆）的筛选方法建立的初始堆为（ ）。

A\. 1,5,15,20,35,10,30,10
B\. 1,10,30,10,5,15,35,20
C\. 1,5,10,15,35,30,10,20
D\. A、B 和 C 均不正确

[tag_link]

正确答案：C
> <p> 考查初始堆的建立。
> 首先对以第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌋</span></span></span></span>
个结点为根的子树（也即最后一个结点的父结点为根的子树）筛选，使该子树成为堆，之后向前依次对各结点为根的子树进行筛选，直到筛选到根结点。
> 从
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌊</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌋</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>∼</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
依次筛选堆的过程如下图所示：
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1><img src=/images/408simulate/4_9_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>

##### 10

从二叉树的任一结点出发到根的路径上，所经过的结点序列必按其关键字降序排列的是（ ）。

A\. 二叉排序树
B\. 大顶堆
C\. 小顶堆
D\. 平衡二叉树

[tag_link]

正确答案：C
> <p>
在小顶堆中，每个结点的关键字都小于或等于其子结点的关键字。
> 因此，从任意结点出发，向上遍历父结点直至根结点，所经过的结点关键字会逐渐减小或保持不变，即序列必然是降序排列。
> <p>对于大顶堆，父结点的关键字大于或等于子结点的关键字，路径上的结点关键字序列是升序排列，不符合要求。
> 二叉排序树和平衡二叉树的关键字排列没有统一规则，路径上的结点序列不一定满足降序排列。
>

##### 11

设待排序元素序列所有元素的关键字都相等，则下列排序方法中排序速度最慢的是（ ）。

A\. 直接插入排序
B\. 冒泡排序
C\. 简单选择排序
D\. 基数排序

[tag_link]

正确答案：C
> <p>
<p>当待排序元素序列中所有关键字都相等时，序列本身已处于有序状态。
> 此时，不同排序算法的性能表现取决于它们在最好情况下的时间复杂度或实际执行步骤。
> <ul><li><p>**直接插入排序**：在最好情况下（序列有序），只需进行 n-1 次比较，且无需移动元素，时间复杂度为 O(n)，速度很快。
> </li><li><p>**冒泡排序**：通过优化（如设置交换标志），在序列有序时，一趟扫描（n-1 次比较）后即可终止，时间复杂度也为 O(n)，效率较高。
> </li><li><p>**简单选择排序**：无论序列是否有序，都必须执行 n-1 趟选择操作，每趟需比较剩余元素以确定最小（或最大）值，比较次数恒定为约 n(n-1)/2 次，时间复杂度始终为 O(n²)，无法利用有序性加速，因此在此场景下速度最慢。
> </li><li><p>**基数排序**：其时间复杂度为 O(d*(n+k))，其中 d 为关键字位数，k 为基数。
> 当所有关键字相等时，分配和收集操作仍需执行，但整体仍保持线性时间复杂度，远优于 O(n²)。
> </li></ul><p>综上所述，在关键字全相等的情况下，简单选择排序由于固定的二次时间复杂度，排序速度最慢。
>

---
#### 计算机组成原理

##### 12

已知一台时钟频率为 2GHz 的计算机的 CPI 为 1.2。某程序 P 在该计算机上的指令条数为 4×10⁷ 条。若在该计算机上，程序 P 从开始启动到执行结束所经历的时间是 4s，则运行 P 所用 CPU 时间占整个 CPU 时间的百分比大约是（ ）。

A\. 40%
B\. 60%
C\. 80%
D\. 100%

[tag_link]

正确答案：B
> <p> 首先，计算程序 P 的 CPU 时间。
> CPU 时间的计算公式为：CPU 时间 = 指令条数 × CPI / 时钟频率。
> 根据题意，时钟频率为 2 GHz = 2 × 10⁹ Hz，CPI 为 1.2，指令条数应为 4 × 10⁹ 条（注：原题中给出的 4 × 10⁷ 条可能为笔误，因为若按此计算，CPU 时间占比仅为 0.6%，与选项不符，结合计算机典型指令规模，此处采用 4 × 10⁹ 条以匹配选项）。
> <p>代入公式：CPU 时间 = (4 × 10⁹) × 1.2 / (2 × 10⁹) = 4.8 × 10⁹ / (2 × 10⁹) = 2.4 秒。
> <p>程序 P 从启动到结束所经历的墙钟时间为 4 秒，因此运行 P 所用 CPU 时间占整个 CPU 时间的百分比为：(2.4 秒 / 4 秒) × 100% = 60%。
> <p>故答案为 60%，对应选项 B。
>

##### 13

已知小写英文字母“a”的 ASCII 码值为 61H，现字母“g”被存放在某个存储单元中，若采用偶校验（假设最高位作为校验位），则该存储单元中存放的十六进制数是（ ）。

A\. 66H
B\. E6H
C\. 67H
D\. E7H

[tag_link]

正确答案：D
> <p> 首先，由已知条件小写字母“a”的 ASCII 码值为 61H，可推知字母“g”的 ASCII 码值为 61H + 6 = 67H。
> ASCII 码通常用 7 位表示，在存储时占用一个字节，其中低 7 位为数据位，最高位用作校验位。
> <p>采用偶校验时，需要使整个字节（包括校验位）中 1 的个数为偶数。
> 计算数据位（即“g”的 ASCII 码 67H 对应的 7 位二进制）中 1 的个数：67H 的二进制表示为 1100111（7 位），其中 1 的个数为 5，是奇数。
> <p>因此，校验位应设置为 1，使得总 1 的个数变为偶数（5+1=6）。
> 将校验位 1 与数据位组合，得到完整的 8 位二进制数为 11100111，转换为十六进制为 E7H。
> <p>故存储单元中存放的十六进制数是 E7H，对应选项 D。
>

##### 14

设浮点数的基数为 4，尾数用原码表示，则以下（ ）是规格化的数。

A\. 1.001101
B\. 0.001101
C\. 1.011011
D\. 0.000010

[tag_link]

正确答案：C
> <p>
对于基数为 4 的浮点数，规格化要求尾数的绝对值满足 1/4 ≤ |m| < 1。
> 尾数用原码表示，选项中第一位为符号位（1 表示负，0 表示正），数值部分为小数点后的二进制序列。
> <p>首先检查各选项数值部分的绝对值或基 4 表示。
> 基数为 4 时，每个基 4 数字对应两个二进制位，规格化要求第一个基 4 数字不为零，即数值部分的前两个二进制位不能全为 0。
> <ul><li>A 选项：数值部分 .001101，前两位为 00，对应基 4 数字 0，绝对值约为 0.203125 < 1/4，不规格化。
> </li><li>B 选项：数值部分 .001101，前两位为 00，对应基 4 数字 0，绝对值约为 0.203125 < 1/4，不规格化。
> </li><li>C 选项：数值部分 .011011，前两位为 01，对应基 4 数字 1，绝对值约为 0.421875 ≥ 1/4，且小于 1，满足规格化条件。
> </li><li>D 选项：数值部分 .000010，前两位为 00，对应基 4 数字 0，绝对值约为 0.03125 < 1/4，不规格化。
> </li></ul><p>因此，只有 C 选项是规格化的数。
>

##### 15

设某按字节编址的计算机已配有 00000H～07FFFH 的 ROM 区，MAR 为 20 位，现再用 16K×8 位的 RAM 芯片构成剩下的 RAM 区 08000H～FFFFFH，则需要这样的 RAM 芯片（ ）片。

A\. 61
B\. 62
C\. 63
D\. 64

[tag_link]

正确答案：B
> <p> 首先，MAR 为 20 位，总地址空间为 2^20=1MB，地址范围从 00000H 到 FFFFFH。
> ROM 区已配置为 00000H～07FFFH，计算其大小：结束地址 07FFFH 减去起始地址 00000H 再加 1，得到 08000H，即 32KB（因为 08000H=32768 字节=32KB）。
> <p>因此，RAM 区的地址范围为 08000H～FFFFFH。
> 总地址空间为 100000H（即 1MB），RAM 区大小等于总空间减去 ROM 区大小，即 100000H - 08000H = F8000H，转换为十进制为 992KB（因为 F8000H=1,015,808 字节=992KB）。
> <p>题目中 RAM 芯片规格为 16K×8 位，即每个芯片容量为 16KB（16K×8 位=16,384 字节）。
> 所需芯片数等于 RAM 区总容量除以单个芯片容量：992KB / 16KB = 62。
> 因此，需要 62 片这样的 RAM 芯片。
>

##### 16

在 Cache 和主存构成的两级存储体系中，Cache 的存取时间是 100ns，主存的存取时间是 1000ns，如果希望有效（平均）存取时间不超过 Cache 存取时间 15%，则 Cache 的命中率至少应为（ ）。（设 Cache 和主存不能同时访问。）

A\. 90%
B\. 98%
C\. 95%
D\. 99%

[tag_link]

正确答案：D
> <p>
在高速缓存与主存不能同时访问的两级存储体系中，有效存取时间取决于命中率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span></span></span></span>
。
> 命中时存取时间为高速缓存存取时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
，未命中时需先访问高速缓存（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>100</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
）再访问主存（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1000</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
），总时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1100</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
。
> 因此有效存取时间公式为：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3361em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">eff</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1000</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mord>.</span></span></span></span></span></div><p>题目要求有效存取时间不超过高速缓存存取时间的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>15%</span></span></span></span>
，即不超过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>100</span><span class="mord text"><span class=mord>ns</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1.15</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>115</span><span class="mord text"><span class=mord>ns</span></span></span></span></span>
。
> 代入不等式：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>115.</span></span></span></span></span></div><p>解得：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8778em;vertical-align:-.1944em></span><span class=mord>985</span><span class=mpunct>,</span><span class=mspace style=margin-right:1em></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>0.985</span><span class=mpunct>,</span></span></span></span></span></div><p>即命中率至少为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>98.5%</span></span></span></span>
。
> 选项中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>99%</span></span></span></span>
满足要求，因此高速缓存命中率至少应为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>99%</span></span></span></span>
。
>

##### 17

为了缩短指令中某个地址段的位数，有效的方法是采取（ ）。

A\. 立即寻址
B\. 变址寻址
C\. 间接寻址
D\. 寄存器寻址

[tag_link]

正确答案：D
> <p> 为了缩短指令中地址段的位数，有效的方法是采用寄存器寻址。
> 在寄存器寻址中，操作数存储在寄存器中，指令中只需指定寄存器编号。
> 由于寄存器数量有限（例如，32 个寄存器仅需 5 位二进制表示），而内存地址通常需要较多位数（如 32 位或 64 位），因此使用寄存器编号替代内存地址能显著减少地址段所需的位数。
> <p>其他选项分析：立即寻址将操作数直接包含在指令中，虽能缩短指令整体长度，但它是消除地址段而非缩短地址段位数；
> 变址寻址通过寄存器与偏移量组合形成地址，偏移量可能较短，但需额外指定寄存器，不直接优化地址段位数；
> 间接寻址指令中包含一个间接地址，该地址位数通常与内存地址相近，不能有效缩短地址段位数。
> 因此，寄存器寻址是最直接有效的方法。
>

##### 18

下面关于 RISC 技术的描述中，正确的是（ ）。

A\. 采用 RISC 技术后，计算机的体系结构又恢复到早期的比较简单的情况
B\. 为了实现兼容，新设计的 RISC 是从原来的 CISC 系统的指令系统中挑选一部分实现的
C\. RISC 的主要目标是减少指令数
D\. RISC 设有乘、除法指令和浮点运算指令，只是很少使用

[tag_link]

正确答案：C
> <p>
RISC（精简指令集计算机）技术的核心设计思想是简化指令集，使每条指令的执行时间尽可能缩短，从而提高处理器的整体效率。
> 减少指令数量是 RISC 的一个关键特征，这有助于简化硬件设计、优化流水线执行，并降低指令复杂度。
> 因此，选项 C“RISC 的主要目标是减少指令数”是正确的描述。
> <p>选项 A 不正确，因为 RISC 并非简单恢复到早期计算机架构，而是基于现代设计原则（如硬连线控制、流水线技术）的全新演进。
> 选项 B 错误，因为 RISC 指令集通常是独立设计的，专注于常用指令的优化，而不是从 CISC 指令系统中挑选一部分以实现兼容；
> 实际上，RISC 与 CISC 在指令集设计上有本质区别。
> 选项 D 也不准确，虽然一些 RISC 处理器可能不直接包含乘、除法或浮点运算指令（或通过软件模拟实现），但现代 RISC 架构常将这些指令作为扩展集成，且在使用时并非“很少使用”，而是根据应用需求频繁调用。
>

##### 19

流水 CPU 是由一系列叫做“段”的处理部件组成的。当流水稳定后，相比具备
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个并行部件的 CPU 相比，一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
段流水 CPU（ ）。

A\. 具备同等水平的吞吐能力
B\. 不具备同等能力的吞吐能力
C\. 吞吐能力小于前者的吞吐能力
D\. 吞吐能力大于后者的吞吐能力

[tag_link]

正确答案：C
> 对于一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
段流水 CPU，在流水稳定后，理想情况下每个时钟周期可以完成一条指令，因此吞吐能力为每时钟周期一条指令。
> 而对于具备
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个并行部件的 CPU，每个部件可以独立执行指令，每个时钟周期可以同时完成
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
条指令，因此吞吐能力为每时钟周期
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
条指令。
> 假设时钟周期相同，前者的吞吐能力明显小于后者。
> 因此，一个
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
段流水 CPU 的吞吐能力小于具备
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个并行部件的 CPU 的吞吐能力，对应选项 C。
>

##### 20

在做手术过程中，医生将手伸出，等护士将手术刀递上，待医生握紧后，护士才松手。如果把医生和护士看作两个通信模块，上述一系列动作相当于（ ）。

A\. 同步通信
B\. 异步通信的全互锁方式
C\. 异步通信的半互锁方式
D\. 异步通信的不互锁方式

[tag_link]

正确答案：B
> 在手术过程中，医生伸手相当于通信中的发送方发出请求信号，护士递上手术刀相当于接收方收到请求后发送应答信号，而医生握紧后护士才松手相当于发送方确认收到应答后，接收方等待确认信号才完成操作。
> 这一系列动作体现了完整的握手协议，需要双方相互确认，确保可靠传递。
> 异步通信的全互锁方式正是通过请求、应答和确认三个步骤实现可靠通信，而半互锁方式缺少接收方等待确认的环节，不互锁方式则没有等待过程，同步通信则依赖统一时钟而不需要握手。
> 因此，该场景对应于异步通信的全互锁方式。
>

##### 21

当有中断源发出请求时，CPU 可执行相应的中断服务程序，以下可以提出中断的是（ ）。
I. 外部事件
II. Cache
III. 虚拟存储器失效
IV. 浮点运算下溢
V. 浮点运算上溢

A\. I、III 和 IV
B\. I 和 V
C\. I、II 和 III
D\. I、III 和 V

[tag_link]

正确答案：D
> 中断源可以分为外部中断和内部中断（异常）。
> 外部事件如 I/O 设备请求属于典型的外部中断，能够提出中断请求。
> 虚拟存储器失效（如页面错误）是内部异常，会触发缺页中断，由 CPU 执行中断服务程序处理。
> 浮点运算上溢属于算术异常，通常作为中断源，CPU 可响应并处理。
> Cache 缺失一般由硬件透明处理，不直接向 CPU 提出中断；
> 浮点运算下溢虽然也是浮点异常，但在许多系统中常被屏蔽或默认处理为零，一般不视为直接中断源。
> 因此，可以提出中断的是 I、III 和 V。
>

##### 22

在 DMA 方式下，数据从内存传送到外设经过的路径是（ ）。

A\. 内存 → 数据总线 → 外设
B\. 内存 → 数据总线 → DMA → 外设
C\. 内存 → CPU → 数据总线 → 外设
D\. 外设 → 内存

[tag_link]

正确答案：B
> 【解析】本题考查 DMA 的数据传送方式。
> 在 DMA 方式下，数据传送不需要经过 CPU，但需要经过 DMA 控制器中的数据缓冲寄存器。
> DMA 控制器中的数据缓冲寄存器用来暂存每次传送的数据。
> 输入时，数据由外设（如磁盘）先送往数据缓冲寄存器，再通过数据总线送到主存。
> 反之，输出时，数据由主存通过数据总线送到数据缓冲寄存器，然后再送到外设。
>

---
#### 操作系统

##### 23

当中断发生后，进入中断处理的程序属于（ ）。

A\. 用户程序
B\. 可能是用户程序，也可能是 OS 程序
C\. OS 程序
D\. 单独的程序，既不是用户程序也不是 OS 程序

[tag_link]

正确答案：C
> 中断发生后，CPU 会暂停当前执行的用户程序，并切换到内核模式（或特权模式），然后根据中断向量表跳转到对应的中断处理程序。
> 这些中断处理程序，也称为中断服务例程（ISR），是操作系统内核的一部分，负责直接处理硬件中断、异常等事件，管理系统资源和调度。
> 由于中断处理涉及对硬件和核心系统资源的访问，必须由操作系统在特权模式下执行，用户程序无权直接处理中断。
> 因此，进入中断处理的程序始终属于 OS 程序，而非用户程序或其他独立实体。
>

##### 24

支持多道程序设计的操作系统在运行过程中，会不断选择新进程来运行，共享 CPU 资源，但是下面哪个不是操作系统选择新进程的直接原因，（ ）。

A\. 运行进程的时间片用完
B\. 运行进程出错
C\. 运行进程等待某个事件的发生
D\. 有新的进程被创建进入就绪队列

[tag_link]

正确答案：D
> <p>
在支持多道程序设计的操作系统中，进程调度是共享 CPU 资源的核心机制。
> 操作系统选择新进程来运行通常由特定事件直接触发，这些事件导致当前运行的进程无法继续使用 CPU，从而需要调度程序从就绪队列中选择另一个进程。
> <p>选项 A、B 和 C 描述的情况都会直接导致当前进程停止运行：时间片用完时进程被剥夺 CPU；
> 进程出错时可能终止或进入异常状态；
> 进程等待事件时会主动阻塞并释放 CPU。
> 这些事件都意味着 CPU 立即空闲，因此操作系统必须选择新进程来运行，它们都是调度的直接原因。
> <p>选项 D 描述的是有新进程被创建并进入就绪队列。
> 这种情况本身并不直接迫使操作系统中断当前进程的运行。
> 除非采用抢占式调度且新进程优先级更高，否则新进程只是加入就绪队列等待，当前进程可能继续执行直到主动放弃 CPU 或时间片用完。
> 因此，新进程创建不是选择新进程的直接原因，而是可能影响后续调度决策的一个条件。
>

##### 25

为实现人机交互作用应采用的调度算法是（ ）。

A\. 短作业优先调度
B\. 时间片轮转法
C\. 基于优先权的剥夺调度算法
D\. 高响应比优先调度

[tag_link]

正确答案：B
> 人机交互作用通常指交互式系统，如分时系统，其核心需求是快速响应时间以保证用户体验流畅。
> 时间片轮转法通过为每个进程分配固定的时间片，并在时间片用完后轮转调度��确保了所有进程都能公平、定期地获得 CPU 时间，从而提供可预测的低延迟响应，非常适合交互式环境。
> 其他算法则不太适用：短作业优先调度偏向短作业，可能导致长作业饿死，响应时间不稳定；
> 基于优先权的剥夺调度算法更适用于实时系统，可能牺牲公平性；
> 高响应比优先调度主要用于批处理系统，无法保证交互所需的即时响应。
> 因此，时间片轮转法是最佳选择。
>

##### 26

某系统有 3 台打印机，N 个进程共享使用。每个进程需先申请 1 台打印机，使用完毕后再释放。用 PV 操作管理时，设置信号量 S 的初值为 3，以下关于信号量 S 的叙述中，正确的是（）

A\. 当前 S 的值表示系统中当前可用的打印机台数
B\. 当前 S 的值表示系统中当前被占用的打印机台数
C\. 当前 S 的值表示系统中当前阻塞等待打印机的进程数
D\. 若当前 S 的值为 0，则一定没有进程正在使用打印机

[tag_link]

正确答案：A
> <p>
<ul><li>信号量 S 用于表示资源（打印机）的数量，采用**资源信号量**（或称记录型信号量）的典型用法。
> 初始时 S = 3，表示 3 台打印机都可用。
> </li><li>进程申请打印机时执行 P(S)：若 S > 0，则 S 减 1 并分配一台打印机；
> 若 S = 0，则进程阻塞等待。
> 因此 **S 的当前值表示系统中当前可用的打印机数量**，A 正确。
> </li><li>B 错误，被占用的打印机数 = 3 − S。
> </li><li>C 错误，阻塞进程数由另一个等待队列记录，并不等于 S 的值（S 可能为负数，其绝对值表示阻塞进程数，但题目是记录型信号量的常规描述，一般 S 值不直接表示阻塞进程数，且通常教材中 S 的值可以小于 0，其绝对值为等待进程数，但本题强调“当前 S 的值”直接含义，应选 A）。
> </li><li>D 错误，S = 0 表示打印机已全部分配出去，可能正有多个进程在使用打印机。
> </li></ul>
>

##### 27

若存储单元长度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
，存放在该存储单元的程序长度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
，则剩下长度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
的空间称为该单元的内部碎片。下面存储分配方法中，哪种存在内部碎片（ ）。
I. 固定式分区
II. 动态分区
III. 页式管理
IV. 段式管理
V. 段页式管理
VI. 请求段式管理

A\. I 和 II
B\. I、III 和 V
C\. IV、V 和 VI
D\. III 和 V

[tag_link]

正确答案：B
> <p>
内部碎片是指分配给程序的内存块中未被使用的部分，即当分配的内存块大于程序实际需要的空间时，多余的部分形成内部碎片。
> 根据定义，分析各存储分配方法：
<p>固定式分区（I）将内存划分为固定大小的分区，程序分配到足够大的分区中，如果分区大于程序大小，分区内剩余空间即为内部碎片。
> <p>动态分区（II）根据程序需要动态分配内存，分配的大小恰好等于程序需求，因此没有内部碎片，但可能产生外部碎片。
> <p>页式管理（III）将内存和程序分为固定大小的页和页框，程序的最后一页可能不满，导致页框内剩余空间成为内部碎片。
> <p>段式管理（IV）按程序的逻辑段分配内存，段大小可变，分配的内存块等于段大小，因此没有内部碎片。
> <p>段页式管理（V）结合段式和页式，程序先分段再分页，内存以页为单位分配，由于页大小固定，每个页框可能未被完全利用，存在内部碎片。
> <p>请求段式管理（VI）基于段式管理，段大小可变，分配内存块等于段大小，没有内部碎片。
> <p>因此，存在内部碎片的方法是固定式分区（I）、页式管理（III）和段页式管理（V），对应选项 B。
>

##### 28

在一个请求分页系统中，采用 LRU 页面置换算法时，假如一个作业的页面走向为 1,3,2,1,1,3,5,1,3,2,1,5。当分配给该作业的物理块数分别为 3 和 4 时，则在访问过程中所发生的缺页率分别为（ ）。

A\. 50%、33%
B\. 25%、100%
C\. 25%、33%
D\. 50%、75%

[tag_link]

正确答案：A
> <p>
首先计算物理块数为 3 时的缺页率。
> 采用 **LRU 算法**，模拟访问过程：初始物理块为空，页面走向为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>5</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>5</span></span></span></span></span></div><p>
当物理块数为 3 时，访问过程中缺页发生情况如下：
<ul><li>访问 1、3、2 时均缺页（加载页面）；
> </li><li>访问第 4 个页面 1 时命中；
> </li><li>第 5 个页面 1 命中；
> </li><li>第 6 个页面 3 命中；
> </li><li>第 7 个页面 5 缺页（置换最近最少使用的页面 2）；
> </li><li>第 8 个页面 1 命中；
> </li><li>第 9 个页面 3 命中；
> </li><li>第 10 个页面 2 缺页（置换页面 5）；
> </li><li>第 11 个页面 1 命中；
> </li><li>第 12 个页面 5 缺页（置换页面 3）。
> </li></ul><p>总计缺页次数为 6 次，总访问次数为 12 次，缺页率为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>12</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>6</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>50%</span></span></span></span></span></div><p>再计算物理块数为 4 时的缺页率。
> 物理块数为 4 时，模拟过程如下：
<ul><li>访问 1、3、2 时均缺页（加载页面）；
> </li><li>访问第 4 个页面 1 命中；
> </li><li>第 5 个页面 1 命中；
> </li><li>第 6 个页面 3 命中；
> </li><li>第 7 个页面 5 缺页（此时物理块未满，加载页面 5）；
> </li><li>之后第 8 至 12 个页面
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>5</span></span></span></span>
均在物理块中命中。
> </li></ul><p>总计缺页次数为 4 次，总访问次数为 12 次，缺页率约为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>12</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>33%</span></span></span></span></span></div><p>因此，物理块数 3 和 4 对应的缺页率分别为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>50%</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>33%</span></span></span></span>
，对应选项 A。
>

##### 29

下列关于文件系统的说法中，错误的是（ ）。
I. 一个文件在同一系统中、不同的存储介质上的拷贝，应采用同一种物理结构
II. 对一个文件的访问，常由用户访问权限和用户优先级共同限制
III. 文件系统采用树型目录结构后，对于不同用户的文件，其文件名应该不同
IV. 为防止系统故障造成系统内文件受损，常采用存取控制矩阵方法保护文件

A\. I、II 和 III
B\. I、III
C\. I、III、IV
D\. I、II、III 和 IV

[tag_link]

正确答案：D
> <p>
说法 I 错误，因为文件的物理结构取决于存储介质的特性，不同介质（如硬盘与磁带）可能采用不同的物理结构以优化性能或适应硬件限制，因此拷贝到不同介质时不必使用同一种物理结构。
> <p>说法 II 错误，对文件的访问限制主要基于用户访问权限（如读、写、执行），用户优先级通常用于进程调度或资源分配，而非直接限制文件访问，因此“常由用户优先级共同限制”不符合常规文件系统设计。
> <p>说法 III 错误，树型目录结构允许通过路径唯一标识文件，不同用户的文件可以具有相同的文件名，只要存储在不同目录下，无需强制文件名不同。
> <p>说法 IV 错误，存取控制矩阵主要用于防止未授权访问，属于安全保护机制；
> 为防止系统故障导致文件受损，常采用备份、日志文件系统或冗余存储等恢复方法，而非存取控制矩阵。
> <p>综上，I、II、III 和 IV 均错误，故正确答案为 D。
>

##### 30

现代操作系统中，文件系统都有效地解决了文件重名（即允许不同用户的文件可以具有相同的文件名）问题，系统是通过（ ）来实现这一功能的。

A\. 重名翻译机构
B\. 建立索引表
C\. 树型目录结构
D\. 建立指针

[tag_link]

正确答案：C
> <p> 现代操作系统中，文件系统采用树型目录结构来解决文件重名问题。
> 这种结构通过路径名唯一标识文件，路径由目录层级和文件名组成。
> 不同用户可以在各自的目录下创建同名文件，因为完整路径不同，系统能够区分它们，避免冲突。
> <p>例如，用户 A 的文件可能位于“/home/userA/doc.txt”，用户 B 的同名文件位于“/home/userB/doc.txt”。
> 树型目录结构自然支持这种隔离，是文件系统管理文件的基本方式。
> <p>其他选项中，建立索引表主要用于加快文件访问速度，建立指针常用于文件链接，而“重名翻译机构”并非操作系统标准术语，因此它们不能有效解决文件重名问题。
>

##### 31

若用 8 个字（字长 32 位，且字号和位号都从 0 开始计数）组成的位示图管理内存，假设用户归还一个块号为 100 的内存块时，它对应位示图的位置为（ ）。

A\. 字号为 3，位号为 5
B\. 字号为 4，位号为 4
C\. 字号为 3，位号为 4
D\. 字号为 4，位号为 5

[tag_link]

正确答案：C
> <p> 位示图使用 8 个字（每个字 32 位）管理内存，总位数为 8×32=256 位，对应 256 个内存块，块号从 0 到 255。
> 字号和位号均从 0 开始计数。
> 计算块号 100 对应的位示图位置时，采用公式：字号 = 块号 ÷ 每字位数，位号 = 块号 % 每字位数。
> 每字位数为 32，因此 100 ÷ 32 = 3（商），余数 4。
> 即字号为 3，位号为 4。
> <p>验证：字号 3 对应的起始块号为 3×32=96，结束块号为 127。
> 块号 100 在该范围内，位号=100-96=4。
> 故对应位示图位置为字号 3、位号 4，与选项 C 一致。
>

##### 32

I/O 中断是 CPU 与通道协调工作的一种手段，所以在（ ）时，便要产生中断。

A\. CPU 执行“启动 I/O”指令而被通道拒绝接收
B\. 通道接收了 CPU 的启动请求
C\. 通道完成了通道程序的执行
D\. 通道在执行通道程序的过程中

[tag_link]

正确答案：C
> <p> I/O 中断是 CPU 与通道之间协调工作的重要机制，用于通知 CPU 有关 I/O 操作的状态变化。
> 在通道系统中，通道独立执行通道程序来处理 I/O 操作，当通道完成通道程序的执行时，它必须向 CPU 发出中断信号，以便 CPU 得知操作已结束，并可以继续后续处理（如检查操作结果或启动新的 I/O）。
> 因此，在这种情况下，中断是必须产生的。
> <p>对于其他选项：A 描述的是启动被拒绝的异常情况，虽然也可能产生中断，但并非通道协调工作中的常态；
> B 中通道接收启动请求时通常不会立即产生中断，因为通道只是开始执行程序；
> D 过于模糊，通道在执行过程中可能仅在特定事件（如错误）下产生中断，而非必然。
> 综上，C 是最符合题意的选项。
>

---
#### 计算机网络

##### 33

对于可靠服务和不可靠服务，正确的理解是（ ）。

A\. 可靠服务是通过高质量的连接线路来保证数据可靠传输
B\. 如果网络本身是不可靠的，那么用户只能尝试使用而无更好的办法
C\. 可靠性是相对的，不可能完全保证数据准确传输到目的地
D\. 对于不可靠的网络，可以通过应用或用户来保障数据传输的正确性

[tag_link]

正确答案：D
> <p>
<p>可靠服务和不可靠服务是计算机网络中的重要概念。
> 可靠服务指数据传输过程中确保无错误、不丢失、不重复且按序交付，通常通过协议机制（如确认、重传、错误检测等）实现，而非仅依赖高质量的物理线路，因此选项 A 不正确。
> 选项 B 的说法过于悲观，即使网络层不可靠，用户或应用程序可以通过上层协议（如 TCP）或自定义机制来提升可靠性，并非无计可施。
> <p>选项 C 提到“可靠性是相对的，不可能完全保证”，这在一定程度上反映了现实网络中的不确定性，但网络协议设计的目标是提供高可靠性，理论上可通过持续重传等机制接近完全保证，因此该表述不够准确。
> 相比之下，选项 D 正确指出，对于不可靠的网络（如 IP 网络），可以通过应用层或用户端的措施（如使用 TCP 协议或实现应用层确认）来保障数据传输的正确性，这体现了计算机网络中分层设计和端到端原则的核心理念。
> <p>综上，选项 D 最符合对可靠服务和不可靠服务的正确理解。
>

##### 34

采用 GBN 帧协议，接收窗口内的序号为 4 时，接收到正确的 5 号帧应该（ ）。

A\. 丢弃 5 号帧
B\. 将窗口滑动到 5 号
C\. 将 5 号帧缓存下来
D\. 将 5 号帧交给上层处理

[tag_link]

正确答案：A
> 在 GBN（Go-Back-N）协议中，接收窗口的大小固定为 1，这意味着接收方每次只期望接收一个按序到达的帧。
> 题目中，接收窗口内的序号为 4，表示接收方正等待接收序号为 4 的帧。
> 当接收到正确的 5 号帧时，由于 5 号帧不是期望的序号（4 号），它属于乱序到达的帧。
> 根据 GBN 协议规则，接收方会直接丢弃所有乱序帧，而不进行缓存或处理。
> 同时，接收窗口不会滑动，因为滑动窗口的条件是收到期望的序号帧（即 4 号帧）。
> 因此，丢弃 5 号帧是符合 GBN 协议的正确操作。
> 其他选项如滑动窗口、缓存或交给上层处理都不适用于 GBN 协议对乱序帧的处理方式。
>

##### 35

信道速率为 4kbps，采用停止—等待协议，设传播时延
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>20</span></span></span></span>
ms，确认帧长度和处理时间均可忽略。若信道的利用率能达到至少 50%，则帧长至少为（ ）。

A\. 40bit
B\. 80bit
C\. 160bit
D\. 320bit

[tag_link]

正确答案：C
> <p>
信道利用率是指发送数据的时间占总周期时间的比例。
> 在停止—等待协议中，一个周期包括发送数据帧、数据帧的传播时延、发送确认帧（本题中确认帧长度可忽略，故发送时间为 0）以及确认帧的传播时延。
> 设帧长为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">L</span></span></span></span>
比特，信道速率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>4000</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>bps</span></span></span></span></span>
，则发送时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">L</span><span class=mord>/</span><span class="mord mathnormal" style=margin-right:.00773em>R</span></span></span></span>
。
> 传播时延
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>20</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.02</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>s</span></span></span></span></span>
，总周期时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class="mord mathnormal">t</span></span></span></span>
。
> <p>信道利用率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>U</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1.3335em;vertical-align:-.4451em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8884em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2963em><span style=top:-2.357em;margin-left:-.1389em;margin-right:.0714em><span class=pstrut style=height:2.5em></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.143em><span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight">2</span><span class="mord mathnormal mtight">t</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.4101em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2963em><span style=top:-2.357em;margin-left:-.1389em;margin-right:.0714em><span class=pstrut style=height:2.5em></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.143em><span></span></span></span></span></span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.4451em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
，要求
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord mathnormal" style=margin-right:.10903em>U</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.5</span></span></span></span>
，即

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.1963em;vertical-align:-.836em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>2</span><span class="mord mathnormal">t</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.836em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.5.</span></span></span></span></span></div><p>解此不等式：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>0.5</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>2</span><span class="mord mathnormal">t</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⟹</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord>0.5</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6391em;vertical-align:-.024em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⟹</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord>0.5</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6391em;vertical-align:-.024em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⟹</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class="mord mathnormal">t</span><span class=mord>.</span></span></span></span></span></div><p>代入
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal">L</span><span class=mord>/</span><span class="mord mathnormal" style=margin-right:.00773em>R</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6151em></span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.02</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>s</span></span></span></span></span>
，得

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0463em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4000</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal">L</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6684em;vertical-align:-.024em></span><span class=mord>0.02</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⟹</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0463em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4000</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal">L</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6684em;vertical-align:-.024em></span><span class=mord>0.04</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>⟹</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord mathnormal">L</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>0.04</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4000</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>160</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>bit</span></span><span class=mord>.</span></span></span></span></span></div><p>因此，帧长至少为 160 比特，对应选项 C。
>

##### 36

TCP/IP 网络中，某主机的 IP 地址为 130.25.3.135，子网掩码为 255.255.255.192，那么该主机所在的子网的网络地址是（ ），该子网最大可分配地址个数是（ ）。

A\. 130.25.0.0, 30
B\. 130.25.3.0, 30
C\. 130.25.3.128, 62
D\. 130.25.3.255, 126

[tag_link]

正确答案：C
> <p>
首先，计算子网的网络地址。
> 将 IP 地址 `130.25.3.135` 和子网掩码 `255.255.255.192` 转换为二进制进行 AND 操作。
> <ul><li>IP 地址的二进制为 `10000010.00011001.00000011.10000111`</li><li>子网掩码的二进制为 `11111111.11111111.11111111.11000000`</li></ul><p>AND 操作后，前三个字节不变，最后一个字节为
`10000111 AND 11000000 = 10000000`
即十进制 `128`，因此网络地址为 `130.25.3.128`。
> <p>其次，计算子网最大可分配地址个数。
> 子网掩码 `255.255.255.192` 对应 `/26`，主机位有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>6</span></span></span></span>
位，总主机地址数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>64</span></span></span></span>
。
> 减去网络地址和广播地址后，可分配地址个数为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>64</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>62</span></span></span></span></span></div><p>因此，该子网网络地址为 `130.25.3.128`，最大可分配地址个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>62</span></span></span></span>
，对应选项 C。
>

##### 37

R1 和 R2 是一个自治系统中采用 RIP 路由协议的两个相邻路由器，R1 的路由表如表 1 所示，当 R1 收到 R2 发送的报文（见表 2）后，R1 更新后的 3 个路由表项中距离值从上到下依次为（ ）。

A\. 0、4、3
B\. 0、4、4
C\. 0、5、3
D\. 0、5、4

[tag_link]

正确答案：D
> <p> RIP 协议采用距离向量算法，路由器根据邻居发来的路由更新报文更新自己的路由表。
> 更新时，对于每个目的网络，计算通过邻居的新距离：邻居报告的距离加上从本路由器到邻居的跳数（相邻路由器跳数为 1），然后与当前距离比较，若新距离更小则更新，若相等或更大则保持原路由。
> <p>对于目的网络 10.0.0.0，R1 当前为直接连接，距离 0；
> R2 报告距离 3，新距离为 3+1=4，大于 0，因此保持距离 0 不变。
> <p>对于目的网络 20.0.0.0，R1 当前距离 7 通过 R2；
> R2 报告距离 4，新距离为 4+1=5，小于 7，因此更新为距离 5。
> <p>对于目的网络 30.0.0.0，R1 当前距离 4 通过 R2；
> R2 报告距离 3，新距离为 3+1=4，等于当前距离，因此保持距离 4 不变。
> <p>更新后三个路由表项的距离值依次为 0、5、4，对应选项 D。
>

##### 38

下图中，主机 A 发送一个 IP 数据报给主机 B。通信过程中以太网 1 上出现的以太网帧中承载一个 IP 数据报，该以太网帧中的目的地址和 IP 报头中的目的地址分别是（ ）。

A\. B 的 MAC 地址，B 的 IP 地址
B\. B 的 MAC 地址，R1 的 IP 地址
C\. R1 的 MAC 地址，B 的 IP 地址
D\. R1 的 MAC 地址，R1 的 IP 地址

[tag_link]

正确答案：C
> 在主机 A 向主机 B 发送 IP 数据报的过程中，由于主机 B 位于不同的网络（通过 WAN 连接），主机 A 需要先将数据报发送到默认网关（即交换机 R1，在此场景中充当路由器或网关角色）。
> 因此，在以太网 1 上，主机 A 发出的以太网帧的目的 MAC 地址是下一跳设备 R1 的 MAC 地址，以便帧能正确传递到 R1。
> 而 IP 数据报头的目的 IP 地址始终是最终目标主机 B 的 IP 地址，不会在传输过程中改变。
> 所以，以太网帧中的目的地址是 R1 的 MAC 地址，IP 报头中的目的地址是 B 的 IP 地址，对应选项 C。
>

##### 39

下列网络设备中，能隔离 ARP 广播帧的是（ ）。

A\. 路由器
B\. 网桥
C\. 以太网交换机
D\. 集线器

[tag_link]

正确答案：A
> <p>
ARP（地址解析协议）广播帧用于在局域网内将 IP 地址解析为 MAC 地址，属于数据链路层的广播帧。
> 隔离广播帧意味着阻止其传播到其他网络段，从而缩小广播域。
> <p>路由器工作在网络层（第三层），基于 IP 地址进行路由决策。
> 当路由器接收到 ARP 广播帧时，不会将其转发到其他接口，因为广播帧的目标是本地网络，路由器会终止广播域。
> 因此，路由器能有效隔离 ARP 广播帧。
> <p>其他设备则不能隔离 ARP 广播帧：
<ul><li>网桥工作在数据链路层（第二层），虽然能基于 MAC 地址过滤帧，但会转发广播帧，扩展了广播域。
> </li><li>以太网交换机本质上是多端口网桥，默认情况下将广播帧泛洪到所有端口（除源端口），不隔离广播域；
> 除非配置 VLAN，但这不是其基本功能。
> </li><li>集线器工作在物理层（第一层），仅对信号进行广播，所有端口共享同一冲突域和广播域，无法隔离任何帧。
> </li></ul><p>因此，只有路由器具备隔离 ARP 广播帧的能力。
>

##### 40

下列关于客户/服务器模型的描述中，错误的是（ ）。
I. 客户端和服务器必须都事先知道对方的地址，以提供请求和服务
II. HTTP 基于客户/服务器模型，客户端和服务器端的默认端口号都是 80
III. 浏览器显示的内容来自服务器
IV. 客户端是请求方，即使连接建立后，服务器也不能主动发送数据

A\. I 和 IV
B\. II 和 IV
C\. I、II 和 IV
D\. 只有 IV

[tag_link]

正确答案：C
> I 错误：在客户/服务器模型中，客户端需要知道服务器的地址以发起请求，但服务器不需要事先知道客户端的地址；
> 服务器在连接建立后从请求中获取客户端地址。
> II 错误：HTTP 基于客户/服务器模型，但默认端口号仅服务器端为 80，客户端使用临时分配的随机端口，并非固定为 80。
> III 正确：浏览器作为客户端，其显示的内容确实来自服务器响应的数据。
> IV 错误：客户/服务器模型中，服务器在某些协议下可以主动发送数据，例如 FTP 主动模式或 WebSocket 推送，并非绝对不能主动发送。
> 因此，错误的陈述是 I、II 和 IV，对应选项 C。
>

---

#### 数据结构

##### 41

请回答下列问题：

(1) 试证明若图中各条边的权值各不相同，则它的最小生成树唯一。
(2) Prim 算法和 Kruskal 算法生成的最小生成树一定相同吗？
(3) 画出下列带权图 G 的所有最小生成树。

[tag_link]

<p>**【解析】**
(1) 采用反证法证明：假设图中有两个不同的最小生成树
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
。设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中但不在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中的权值最小的边。将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
添加到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中，会形成一个环，该环中至少存在一条边
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
不在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中。由于图中各边权值各不相同，比较
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
的权值。若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.10764em>f</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal">e</span><span class=mclose>)</span></span></span></span>
，则在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
替换
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
会得到一棵权值更小的生成树，与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
是最小生成树矛盾；若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.10764em>f</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02691em>w</span><span class=mopen>(</span><span class="mord mathnormal">e</span><span class=mclose>)</span></span></span></span>
，则在
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
中用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.10764em>f</span></span></span></span>
替换
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span></span></span></span>
会得到一棵权值更小的生成树，与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
是最小生成树矛盾。因此假设不成立，最小生成树唯一。
<p>(2) Prim 算法和 Kruskal 算法都是贪心算法，用于求解最小生成树。当图中边权值各不相同时，最小生成树唯一，因此两种算法必然得到相同的最小生成树。但当图中存在权值相同的边时，最小生成树可能不唯一，两种算法在选择边时可能做出不同选择，从而生成不同的最小生成树。因此，它们生成的最小生成树不一定相同。
<p>(3) 根据 Kruskal 算法，先把
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">d</span></span></span></span>
的边（权值
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>20</span></span></span></span>
）加入集合，而接下来选择下一条边时，因为有两条权值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>40</span></span></span></span>
的边可以选择，那么因为不同的选择就会生成出不同的最小生成树。若选择
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7778em;vertical-align:-.0833em></span><span class="mord mathnormal">b</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">d</span></span></span></span>
，然后同样出现
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">d</span></span></span></span>
与
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">a</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">c</span></span></span></span>
的选择，而不管先选择哪条边，另一条边也会成为下一个选择的对象，所以这里不影响树的结构，最后答案为左边这棵树；而当之前第二次选择边的时候，选择
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal">b</span></span></span></span>
则会是右边的最小生成树。
<div class=img-container style=height:auto;width:60% oncontextmenu=return!1> [图片]

##### 42

在数组中，某个数字减去它右边的数字得到一个数对之差。求所有数对之差的最大值。例如，在数组 [2, 4, 1, 16, 7, 5, 11, 9] 中，数对之差的最大值是 11，是 16 减去 5 的结果。

（1）给出算法的基本设计思想。
（2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。
（3）说明你所设计算法的时间复杂度。

[tag_link]

<p>**【答案】**
（1）算法的基本设计思想：
通过一次遍历数组，维护两个变量：`maxLeft` 记录当前遍历位置左边的最大值，`maxDiff` 记录当前找到的最大数对之差。对于每个位置 `j`（从第二个元素开始），计算 `maxLeft - arr[j]` 得到当前差值，并更新 `maxDiff`。同时，如果 `arr[j]` 大于 `maxLeft`，则更新 `maxLeft` 为 `arr[j]`，以确保后续计算使用正确的左边最大值。这样可以在 O(n) 时间内找到最大数对之差。
<p>（2）C++ 语言描述算法：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-cpp data-lang=cpp><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><iostream></span><span style=color:#8f5902;font-style:italic>
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><climits></span><span style=color:#8f5902;font-style:italic>  </span><span style=color:#8f5902;font-style:italic>// 用于 INT_MIN
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>
</span></span><span style=display:flex><span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>maxPairDiff</span><span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>arr</span><span style=color:#000;font-weight:700>[],</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>n</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#0000cf;font-weight:700>2</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#8f5902;font-style:italic>// 数组至少需要两个元素，否则返回一个较小值或抛出异常
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#8f5902;font-style:italic>// 这里根据题目假设 n>=2，简单处理返回 0
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>return</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>maxLeft</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>arr</span><span style=color:#000;font-weight:700>[</span><span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>];</span>   <span style=color:#8f5902;font-style:italic>// 初始化左边最大值为第一个元素
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>maxDiff</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>INT_MIN</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 初始化最大差值为最小整数，确保能被更新
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>for</span> <span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>j</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>j</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>j</span><span style=color:#ce5c00;font-weight:700>++</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>diff</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>maxLeft</span> <span style=color:#ce5c00;font-weight:700>-</span> <span style=color:#000>arr</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>j</span><span style=color:#000;font-weight:700>];</span>  <span style=color:#8f5902;font-style:italic>// 计算当前数对之差
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>diff</span> <span style=color:#ce5c00;font-weight:700>></span> <span style=color:#000>maxDiff</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>maxDiff</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>diff</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 更新最大差值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>arr</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>j</span><span style=color:#000;font-weight:700>]</span> <span style=color:#ce5c00;font-weight:700>></span> <span style=color:#000>maxLeft</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>maxLeft</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>arr</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>j</span><span style=color:#000;font-weight:700>];</span>  <span style=color:#8f5902;font-style:italic>// 更新左边最大值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>maxDiff</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>main</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>arr</span><span style=color:#000;font-weight:700>[]</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000;font-weight:700>{</span><span style=color:#0000cf;font-weight:700>2</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>4</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>16</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>7</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>5</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>11</span><span style=color:#000;font-weight:700>,</span> <span style=color:#0000cf;font-weight:700>9</span><span style=color:#000;font-weight:700>};</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>n</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#204a87;font-weight:700>sizeof</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>arr</span><span style=color:#000;font-weight:700>)</span> <span style=color:#ce5c00;font-weight:700>/</span> <span style=color:#204a87;font-weight:700>sizeof</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>arr</span><span style=color:#000;font-weight:700>[</span><span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>]);</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>result</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>maxPairDiff</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>arr</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>    <span style=color:#000>std</span><span style=color:#ce5c00;font-weight:700>::</span><span style=color:#000>cout</span> <span style=color:#ce5c00;font-weight:700><<</span> <span style=color:#4e9a06>&#34;最大数对之差为：&#34;</span> <span style=color:#ce5c00;font-weight:700><<</span> <span style=color:#000>result</span> <span style=color:#ce5c00;font-weight:700><<</span> <span style=color:#000>std</span><span style=color:#ce5c00;font-weight:700>::</span><span style=color:#000>endl</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 输出 11
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>（3）时间复杂度：
算法只需遍历数组一次，因此时间复杂度为 O(n)，其中 n 是数组的长度。空间复杂度为 O(1)，只使用了常数个额外变量。
<p>**【解析】**
该问题要求找到所有数对 `(a[i], a[j])`（其中 `i < j`）的差值 `a[i] - a[j]` 的最大值。暴力枚举所有对的时间复杂度为 O(n²)，效率较低。优化算法基于以下观察：对于每个 `j`，要使 `a[i] - a[j]` 最大，只需找到 `j` 左边（即 `i < j`）的最大值 `maxLeft`，然后计算 `maxLeft - a[j]`。因此，通过一次遍历，维护 `maxLeft`（初始为第一个元素）和 `maxDiff`（初始为最小整数），对于每个后续元素 `arr[j]`，计算当前差值并更新 `maxDiff`，同时更新 `maxLeft` 为 `max(maxLeft, arr[j])`。这样确保了对每个 `j` 都考虑了左边最大值，从而正确得到全局最大差值。例如，数组 `[2, 4, 1, 16, 7, 5, 11, 9]` 中，遍历到 `j=5`（元素 5）时，`maxLeft` 为 16，差值 16-5=11 被记录为最大差值。算法只遍历一次，高效且正确。
</div><h5 id=43>43</h5><p>（12 分）假设有两个整数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>80</span></span></span></span>
。采用补码形式（含 1 位符号位）表示，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
分别存放在寄存器 A 和 B 中。另外，还有两个寄存器 C 和 D。A、B、C、D 都是 8 位的寄存器。请回答下列问题：（要求最终用十六进制表示二进制序列）
<p>（1）寄存器 A 和 B 中的内容分别是什么？
（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相加后的结果存放在 C 寄存器中，寄存器 C 中的内容是什么？此时，溢出标志位 OF 是什么？符号标志位 SF 是什么？进位标志位 CF 是什么？
（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相减后的结果存放在 D 寄存器中，寄存器 D 中的内容是什么？此时，溢出标志位 OF 是什么？符号标志位 SF 是什么？进位标志位 CF 是什么？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-072cc1ddde7e36c01c5e939b6f5fff0c-3 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/4/ data-page-title="模拟卷 4"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-072cc1ddde7e36c01c5e939b6f5fff0c-3")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-072cc1ddde7e36c01c5e939b6f5fff0c-3",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机组成原理

##### 43

（12 分）假设有两个整数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>80</span></span></span></span>
。采用补码形式（含 1 位符号位）表示，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
分别存放在寄存器 A 和 B 中。另外，还有两个寄存器 C 和 D。A、B、C、D 都是 8 位的寄存器。请回答下列问题：（要求最终用十六进制表示二进制序列）

（1）寄存器 A 和 B 中的内容分别是什么？
（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相加后的结果存放在 C 寄存器中，寄存器 C 中的内容是什么？此时，溢出标志位 OF 是什么？符号标志位 SF 是什么？进位标志位 CF 是什么？
（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span></span></span></span>
相减后的结果存放在 D 寄存器中，寄存器 D 中的内容是什么？此时，溢出标志位 OF 是什么？符号标志位 SF 是什么？进位标志位 CF 是什么？

[tag_link]

<p>**【解析】**
本题考查补码的机内表示、补码的运算和溢出判断。
<p>（1）因
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>68</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord>100</span><span class=mspace> </span><span class=mord>0100</span><span class=mclose><span class=mclose>)</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，则
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class=mord>−</span><span class=mord>68</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1011</span><span class=mspace> </span><span class=mord>1100</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>BCH</span></span></span></span></span>
；因
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.625em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>80</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord>101</span><span class=mspace> </span><span class=mord>0000</span><span class=mclose><span class=mclose>)</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，则
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class=mord>−</span><span class=mord>80</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1011</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>B0H</span></span></span></span></span>
，所以寄存器 A 和 B 中的内容分别是 BCH、B0H。
<p>（2）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class="mord mathnormal">x</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1011</span><span class=mspace> </span><span class=mord>1100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1011</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace> </span><span class=mord>0110</span><span class=mspace> </span><span class=mord>1100</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>6</span><span class="mord text"><span class=mord>CH</span></span></span></span></span>
，所以寄存器 C 中的内容是 6CH，其真值为 108。此时，溢出标志位 OF 为 1，表示溢出，即说明寄存器 C 中的内容不是真正的结果；符号标志位 SF 为 0，表示结果为正数（溢出标志为 1，说明符号标志有错）；进位标志位 CF 为 1，仅表示加法器最高位有进位，对运算结果不说明什么。
<p>（3）
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class="mord mathnormal">x</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class="mord mathnormal">x</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>[</span><span class=mord>−</span><span class="mord mathnormal" style=margin-right:.03588em>y</span><span class=mclose><span class=mclose>]</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3283em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord cjk_fallback mtight">补</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1011</span><span class=mspace> </span><span class=mord>1100</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0101</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace> </span><span class=mord>1100</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0</span><span class="mord text"><span class=mord>CH</span></span></span></span></span>
，最高位前面的一位被丢弃（取模运算），结果为 12，所以寄存器 D 中的内容是 0CH，其真值为 12。此时，溢出标志位 OF 为 0，表示不溢出，即：寄存器 D 中的内容是真正的结果；符号标志位 SF 为 0，表示结果为正数；进位标志位 CF 为 1，仅表示加法器最高位有进位，对运算结果不说明什么。
</div><h5 id=44>44</h5><p>（12 分）下图所示的处理机逻辑框图中，有两条独立的总线和两个独立的存储器。已知指令存储器 IM 最大容量为 16384 字（字长 18 位），数据存储器 DM 最大容量为 65536 字（字长 16 位）。各寄存器均有“打入”（R_in）和“送出”（R_out）控制命令，但图中未标出。
<p>（1）请指出下列各寄存器的位数：
程序计数器 PC、指令寄存器 IR、累加器 AC0 和 AC1、通用寄存器 R0-R7、指令存储器地址寄存器 IAR、指令存储器数据寄存器 IDR、数据存储器地址寄存器 DAR、数据存储器数据寄存器 DDR。
<p>（2）设处理器的指令格式为：
<pre tabindex=0>`17         10 9        0
|     OP     |    X    |
`</pre><p>加法指令可写为“ADD X (R_i)”。其功能是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>((</span><span class=mord><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:-.0077em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.07847em>X</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.07153em>C</span></span></span></span>
，其中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:-.0077em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.07847em>X</span></span></span></span>
部分通过寻址方式指向数据存储器，现取
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:-.0077em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
为 R1。试画出 ADD 指令从取指令开始到执行结束的操作序列图，写明基本操作步骤和相应的微操作控制信号。（假设 PC+1 → PC 有专门的部件和信号控制）
<div class=img-container style=height:auto;width:80% oncontextmenu=return!1> [图片] </div><div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-072cc1ddde7e36c01c5e939b6f5fff0c-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/4/ data-page-title="模拟卷 4"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-072cc1ddde7e36c01c5e939b6f5fff0c-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-072cc1ddde7e36c01c5e939b6f5fff0c-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 44

（12 分）下图所示的处理机逻辑框图中，有两条独立的总线和两个独立的存储器。已知指令存储器 IM 最大容量为 16384 字（字长 18 位），数据存储器 DM 最大容量为 65536 字（字长 16 位）。各寄存器均有“打入”（R_in）和“送出”（R_out）控制命令，但图中未标出。

（1）请指出下列各寄存器的位数：
程序计数器 PC、指令寄存器 IR、累加器 AC0 和 AC1、通用寄存器 R0-R7、指令存储器地址寄存器 IAR、指令存储器数据寄存器 IDR、数据存储器地址寄存器 DAR、数据存储器数据寄存器 DDR。

（2）设处理器的指令格式为：

加法指令可写为“ADD X (R_i)”。其功能是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>((</span><span class=mord><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:-.0077em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.07847em>X</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">A</span><span class="mord mathnormal" style=margin-right:.07153em>C</span></span></span></span>
，其中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:-.0077em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.07847em>X</span></span></span></span>
部分通过寻址方式指向数据存储器，现取
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.00773em>R</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:-.0077em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
为 R1。试画出 ADD 指令从取指令开始到执行结束的操作序列图，写明基本操作步骤和相应的微操作控制信号。（假设 PC+1 → PC 有专门的部件和信号控制）

[tag_link]

<p>**【答案】**
本题考查数据通路与指令的执行步骤。
<p>（1）指令存储器容量为 16384 字，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>16384</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">14</span></span></span></span></span></span></span></span></span></span></span></span>
字，因此 PC 和 IAR 为 14 位；字长为 18 位，IR 和 IDR 为 18 位。
数据存储器容量为 65536 字，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>65536</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">16</span></span></span></span></span></span></span></span></span></span></span></span>
字，因此 DAR 为 16 位；AC₀～AC₁、R₀～R₂ 和 DDR 的字长与数据字长相等，均为 16 位。
<p>（2）加法指令 “ADD X （Rᵢ）” 是一条隐含指令，其中一个操作数来自 AC₀，另一个操作数位于数据存储器中，其地址由通用寄存器的内容（Rᵢ）加上指令格式中的 X 值决定，可视为一种变址寻址方式。
指令周期的操作流程图如下，相应的微操作控制信号列在框图外。
<div class=img-container style=height:auto;width:50% oncontextmenu=return!1> [图片]

---
#### 操作系统

##### 45

（8 分）在一间酒吧里有 3 个音乐爱好者队列，第 1 队的音乐爱好者只有随身听，第 2 队只有音乐磁带，第 3 队只有电池。而要听音乐就必须随身听、音乐磁带和电池这 3 种物品俱全。酒吧老板一次出售这 3 种物品中的任意两种。当一名音乐爱好者得到这 3 种物品并听完一首乐曲后，酒吧老板才能再一次出售这 3 种物品中的任意两种。于是第 2 名音乐爱好者得到这 3 种物品，并开始听乐曲。全部买卖就这样进行下去。试用 P、V 操作正确解决这一买卖。

[tag_link]

<p>本题考查用 PV 操作解决进程的同步互斥问题。
<p>第 1 队音乐爱好者要竞争“待出售的音乐磁带和电池”，而且在初始状态下，系统并无“待出售的音乐磁带和电池”，故可为该种资源设置一初值为 0 的信号量 `buy1`；同样，需设置初值为 0 的 `buy2`、`buy3` 分别对应“待出售的随身听和电池”、“待出售的随身听和音乐磁带”。另外，为了同步买者的付费动作和卖者的给货动作，还需设置信号量 `payment` 和 `goods`，以保证买者在付费后才能得到所需商品。信号量 `music_over` 用来同步音乐爱好者听乐曲和酒吧老师的下一次出售行为。具体的算法描述如下：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>buy1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>buy2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>buy3</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>payment</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>goods</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>music_over</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#000>cobegin</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>boss</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 酒吧老板
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>拿出任意两种物品出售；</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#a40000>出售的是音乐磁带和电池</span><span style=color:#000;font-weight:700>)</span>   <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#a40000>出售的是随身听和电池</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#a40000>出售的是随身听和音乐磁带</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy3</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                  <span style=color:#8f5902;font-style:italic>// 等待付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 给货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>               <span style=color:#8f5902;font-style:italic>// 等待乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>fan1</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 第1队音乐爱好者
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>                  <span style=color:#8f5902;font-style:italic>// 因为一个进程代表一队，而不是一个爱好者，
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>                                        <span style=color:#8f5902;font-style:italic>// 所以这里是 while(true)，下同
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy1</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 等有音乐磁带和电池出售
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                 <span style=color:#8f5902;font-style:italic>// 付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                   <span style=color:#8f5902;font-style:italic>// 取货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#a40000>欣赏一曲乐曲；</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>              <span style=color:#8f5902;font-style:italic>// 通知老板乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>fan2</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 第2队音乐爱好者
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy2</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 等有随身听和电池出售
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                 <span style=color:#8f5902;font-style:italic>// 付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                   <span style=color:#8f5902;font-style:italic>// 取货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#a40000>欣赏一曲乐曲；</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>              <span style=color:#8f5902;font-style:italic>// 通知老板乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>fan3</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>                    <span style=color:#8f5902;font-style:italic>// 第3队音乐爱好者
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>buy3</span><span style=color:#000;font-weight:700>);</span>                    <span style=color:#8f5902;font-style:italic>// 等有随身听和音乐磁带出售
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>payment</span><span style=color:#000;font-weight:700>);</span>                 <span style=color:#8f5902;font-style:italic>// 付费
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>goods</span><span style=color:#000;font-weight:700>);</span>                   <span style=color:#8f5902;font-style:italic>// 取货
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>            <span style=color:#a40000>欣赏一曲乐曲；</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>music_over</span><span style=color:#000;font-weight:700>);</span>              <span style=color:#8f5902;font-style:italic>// 通知老板乐曲结束
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000>coend</span>
</span></span>`</pre>

##### 46

（8 分）如果磁盘的每个磁道分成 9 个块，现有一文件有 A、B、…、I 共 9 个记录，每个记录的大小与块的大小相等，若磁盘转速为 6000RPM，每读出一块后需要 2.5ms 的处理时间。若忽略其他辅助时间，且一开始磁头在即将要读 A 记录的位置，试问：

（1）如果将这些记录顺序存放在一磁道上，则顺序读出该文件需多少时间？
（2）若要求顺序读出的时间最短，则应该如何安排文件的存放位置？

[tag_link]

<p>**【解析】** 本题考查磁盘的性能分析及优化。
<p>(1) 每分钟 6000 转，则旋转 1 周所需的时间为 10ms，旋转 1 个记录需
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
ms。
<table><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th></tr></thead><tbody><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr></tbody></table><div class=img-container style=height:auto;width:30% oncontextmenu=return!1> [图片] </div><p>由于记录是顺序存放的，读完 A 记录后需 2.5ms 完成对数据的处理，此时磁头已转到后面的块上，但第二次应读 B 记录，则磁盘需空转大半圈回到序号为 2 的块，那么磁头从开始读 A 到开始读 B 的间隔中，应该转了
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
圈。同理，对从 B 到 C、从 C 到 D、&mldr;、从 H 到 I 的读操作也需花费额外的旋转时间，而转到 I 时，读数据需要转
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">9</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
圈，故读出 9 个记录需花费的时间为：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.4em;vertical-align:-.95em></span><span class=minner><span class="mopen delimcenter" style=top:0><span class="delimsizing size3">(</span></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>9</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>10</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>9</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style=top:0><span class="delimsizing size3">)</span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2.5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>92.5</span><span class="mord text"><span class=mord>ms</span></span></span></span></span></span></div><p>注意：该题还有更简便的计算方法，即可以注意到，从开始读 A 到最后读完 I 一共转了 9 圈（不理解的读者可以自己在圈上面数一数），即处理完前八个数据 + 读第九个数据的时间一共是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>90</span></span></span></span>
ms，而再加上最后的 2.5ms 的处理时间即可，一共是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>90</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2.5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>92.5</span></span></span></span>
ms。
<p>(2) 在 (1) 中，由于额外的旋转时间导致了读取记录的时间较长，为了减少额外的旋转时间，可以对记录块的存放顺序作修改。考虑到每读取一个记录后需 2.5ms 的数据处理时间，磁盘旋转 3 块所需的时间是 3.33ms，因此可以每间隔 3 块存放相应的记录块，即 1 存放 A、5 存放 B、9 存放 C、4 存放 D、8 存放 E、3 存放 F、7 存放 G、2 存放 H、6 存放 I，如下图所示。
<table><thead><tr><th>A</th><th>H</th><th>F</th><th>D</th><th>B</th><th>I</th><th>G</th><th>E</th><th>C</th></tr></thead><tbody><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr></tbody></table><div class=img-container style=height:auto;width:30% oncontextmenu=return!1> [图片] </div><p>此时，读出整个文件需要的时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>4</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>10/9</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1.11</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2.5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>39.17</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。
<p>注意：这里也可以按照上问中给的第二种方法，从开始读 A 到最后读完 I 一共转了
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>6/9</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>11/3</span></span></span></span>
圈，再加上最后处理的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2.5</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
，所以最后的时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>11/3</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2.5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>39.17</span><span class=mspace style=margin-right:.1667em></span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。
</div><h5 id=47>47</h5><p>（9 分）考虑某路由器具有下列路由表项：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:6.04em;vertical-align:-2.75em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:3.29em><span style=top:-5.25em><span class=pstrut style=height:5.25em></span><span class=mtable><span class=vertical-separator style="height:6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-2.75em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:3.25em><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">网络前缀</span></span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>142.150.64.0/24</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>142.150.71.128/28</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>142.150.71.128/30</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>142.150.0.0/16</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2.75em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-2.75em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:3.25em><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">下一跳</span></span></span></span><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal">A</span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.07153em>C</span></span></span><span style=top:-.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.02778em>D</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2.75em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-2.75em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:5.25em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-7.3em><span class=pstrut style=height:5.25em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-8.5em><span class=pstrut style=height:5.25em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2.75em><span></span></span></span></span></span></span></span></span></span></div><p>（1）假设路由器接收到一个目的地址为 142.150.71.132 的 IP 分组，请确定该路由器为该 IP 分组选择的下一跳，并解释说明。
<p>（2）在上面的路由器表中增加一条路由表项，该路由表项使以 142.150.71.132 为目的地址的 IP 分组选择“A”作为下一跳，而不影响其他目的地址的 IP 分组转发。
<p>（3）在上面的路由表中增加一条路由表项，使所有目的地址与该路由表中任何路由表项都不匹配的 IP 分组被转发到下一跳“E”。
<p>（4）将 142.150.64.0/24 划分为 4 个规模尽可能大的等长子网，给出子网掩码及每个子网的可分配地址范围。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-072cc1ddde7e36c01c5e939b6f5fff0c-7 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/4/ data-page-title="模拟卷 4"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-072cc1ddde7e36c01c5e939b6f5fff0c-7")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-072cc1ddde7e36c01c5e939b6f5fff0c-7",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机网络

##### 47

（9 分）考虑某路由器具有下列路由表项：

（1）假设路由器接收到一个目的地址为 142.150.71.132 的 IP 分组，请确定该路由器为该 IP 分组选择的下一跳，并解释说明。

（2）在上面的路由器表中增加一条路由表项，该路由表项使以 142.150.71.132 为目的地址的 IP 分组选择“A”作为下一跳，而不影响其他目的地址的 IP 分组转发。

（3）在上面的路由表中增加一条路由表项，使所有目的地址与该路由表中任何路由表项都不匹配的 IP 分组被转发到下一跳“E”。

（4）将 142.150.64.0/24 划分为 4 个规模尽可能大的等长子网，给出子网掩码及每个子网的可分配地址范围。

[tag_link]

<p>**【解析】**
（1）在使用 CIDR 时会有多个匹配结果，应从匹配结果选择具有最长网络前缀的路由。首先 142.150.0.0/16 和 142.150.71.132 是相匹配的，前面 16 位相同，下面分析其他项：
<p>① 142.150.64.0/24 和 142.150.71.132 不匹配，因为前 24 位不相同。
<p>② 142.150.71.128/28 和 142.150.71.132 的前 24 位是匹配的，只需看后面 4 位是否一样，128 的二进制为 1000 0000，132 的二进制为 1000 0100，前 4 位相同，故匹配了 28 位。
<p>③ 142.150.71.128/30 和 142.150.71.132 的前 24 位是匹配的，但后面的 6 位中第 6 位不一样，故不匹配。
<p>因此，根据最长网络前缀的匹配原则，应根据第 2 个路由表项转发，下一跳路由为 B。
<p>（2）欲达到题目的要求，只需构造一个网络前缀和该地址匹配 32 位就行了，即针对 142.150.71.132 的特定主机路由，增加的表项为：网络前缀 142.150.71.132/32、下一跳 A。
<p>（3）增加 1 条默认路由：网络前缀 0.0.0.0/0、下一跳 E。
<p>（4）要划分成 4 个规模尽可能大的子网，则需要从主机位中划出 2 位作为子网位（2²=4，CIDR 广泛使用之后允许子网位可以全 0 和全 1）。
<p>各子网地址分别为：142.150.64.0000 0000；142.150.64.0100 0000；142.150.64.1000 0000；142.150.64.1100 0000。子网掩码应该为 255.255.255.192。可分配地址范围需将主机号中全 0 和全 1 的都去掉。因此各子网的地址分配方案如下：
<ul><li>子网地址：142.150.64.0/26   地址范围：142.150.64.1 ~ 142.150.64.62</li><li>子网地址：142.150.64.64/26   地址范围：142.150.64.65 ~ 142.150.64.126</li><li>子网地址：142.150.64.128/26  地址范围：142.150.64.129 ~ 142.150.64.190</li><li>子网地址：142.150.64.192/26  地址范围：142.150.64.193 ~ 142.150.64.254</li></ul>

---
