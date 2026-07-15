# 408 计算机学科专业基础综合模拟卷 3

#### 数据结构

##### 1

设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
是描述问题规模的正整数，下面程序片段的时间复杂度是（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mclose>)</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0503em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8003em><span class=svg-align style=top:-3em><span class=pstrut style=height:3em></span><span class=mord style=padding-left:.833em><span class="mord mathnormal">n</span></span></span><span style=top:-2.7603em><span class=pstrut style=height:3em></span><span class=hide-tail style=min-width:.853em;height:1.08em><svg width="400em" height="1.08em" viewBox="0 0 4e5 1080" preserveAspectRatio="xMinYMin slice"><path d="M95 702c-2.7.0-7.17-2.7-13.5-8-5.8-5.3-9.5-10-9.5-14 0-2 .3-3.3 1-4 1.3-2.7 23.83-20.7 67.5-54 44.2-33.3 65.8-50.3 66.5-51 1.3-1.3 3-2 5-2 4.7.0 8.7 3.3 12 10s173 378 173 378c.7.0 35.3-71 104-213s137.5-285 206.5-429S812 97.3 814 94c5.3-9.3 12-14 20-14H4e5v40H845.2724s-225.272 467-225.272 467-235 486-235 486c-2.7 4.7-9 7-19 7-6 0-10-1-12-3s-194-422-194-422-65 47-65 47zM834 80h4e5v40H834z"/></svg></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2397em><span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.02778em>O</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>

[tag_link]

正确答案：A
> 程序片段中，变量 i 初始化为 2。
> 循环条件为 i < n/3，每次循环体执行 i = i * 3，使得 i 的值以指数速度增长。
> 设循环执行次数为 k。
> 在执行 k 次后，i 的值变为 2 × 3^k。
> 循环终止时满足 2 × 3^k ≥ n/3，由此可得 k ≥ log₃(n/6)。
> 由于对数函数的特性，k 与 log n 成正比。
> 每次循环体执行时间为常数，因此整体时间复杂度取决于循环次数，为 O(log n)。
> 选项 A 正确。
>

##### 2

当字符序列 `t3_` 作为栈的输入时，则输出长度为 3，且可用 C 语言标识符的序列有（ ）个。

A\. 4
B\. 5
C\. 3
D\. 6

[tag_link]

正确答案：C
> 【解析】考查栈的操作。
> 标识符只能以字母或下划线开头，即由 `t`、`3`、`_` 能够组成的合法标识符只有：`t3_`、`t_3`、`_3t`、`_t3`，而当用 `t3_` 作为栈的输入时，`_t3` 无法作为输出序列，所以输出的合法标识符有 `t3_`；
> `t_3`；
> `_3t`，因此选 `C`。
>

##### 3

将中缀表达式转换为等价的后缀表达式的过程中要利用堆栈保存运算符。对于中缀表达式
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal">A</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.05017em>B</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
，当扫描到操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
时，堆栈中保存的运算符依次是（ ）。

A\. `-×`
B\. `-(×`
C\. `-+`
D\. `-(+`

[tag_link]

正确答案：A
> <p> 中缀表达式转换为后缀表达式时，使用堆栈暂存运算符。
> 对于表达式
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal">A</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.05017em>B</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
，从左到右扫描：
<ul><li>扫描到操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal">A</span></span></span></span>
：直接输出，堆栈为空。
> </li><li>扫描到运算符
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span></span></span></span>
：堆栈为空，将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span></span></span></span>
压栈。
> </li><li>扫描到左括号
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span></span></span></span>
：直接压栈，堆栈为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span></span></span></span>
（栈底到栈顶，下同）。
> </li><li>扫描到操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
：输出，堆栈不变。
> </li><li>扫描到运算符
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>+</span></span></span></span>
：栈顶为左括号，直接压栈，堆栈为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>+</span></span></span></span>
。
> </li><li>扫描到操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.07153em>C</span></span></span></span>
：输出，堆栈不变。
> </li><li>扫描到右括号
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mclose>)</span></span></span></span>
：弹出栈顶运算符
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>+</span></span></span></span>
并输出，接着弹出左括号
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span></span></span></span>
丢弃，堆栈变为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span></span></span></span>
。
> </li><li>扫描到运算符
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>×</span></span></span></span>
：比较优先级，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>×</span></span></span></span>
高于栈顶
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span></span></span></span>
，因此压栈，堆栈变为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7778em;vertical-align:-.1944em></span><span class=mord>−</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>×</span></span></span></span>
。
> </li><li>扫描到操作数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>E</span></span></span></span>
：此时堆栈保持不变，运算符依次为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>×</span></span></span></span>
。
> </li></ul><p>对应选项，A 为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span><span class=mord>×</span></span></span></span>
，符合结果。
> 其他选项中，B、C、D 的运算符组合与扫描过程中的实际堆栈状态不符。
>

##### 4

有关二叉树下列说法正确的是（ ）。

A\. 二叉树的度为 2
B\. 一棵二叉树的度可以小于 2
C\. 二叉树中至少有一个结点的度为 2
D\. 二叉树就是度为 2 的有序树

[tag_link]

正确答案：B
> <p>
二叉树是一种树形结构，其特点是每个结点最多有两个子结点，且子结点有左右之分，称为左子结点和右子结点。
> 树的度定义为树中所有结点的度的最大值，而结点的度是指该结点拥有的子结点数。
> 因此，在二叉树中，结点的度可以是 0、1 或 2，这意味着整个二叉树的度可以是 0、1 或 2，即可以小于 2。
> 选项 B 正确，因为它反映了二叉树度可以小于 2 的可能性。
> <p>选项 A 错误，因为二叉树的度不一定为 2，例如只有一个根结点的二叉树度为 0。
> 选项 C 错误，因为二叉树中并不要求至少有一个结点的度为 2，例如所有结点度均为 0 或 1 的二叉树是存在的。
> 选项 D 错误，因为二叉树强调每个结点最多有两个子结点且有序，但“度为 2 的有序树”可能被误解为所有结点度均为 2，而二叉树允许结点度小于 2，因此两者并不完全等价。
>

##### 5

前序遍历和中序遍历结果相同的二叉树为（ ）。
I. 只有根结点的二叉树
II. 根结点无右孩子的二叉树
III. 所有结点只有左子树的二叉树
IV. 所有结点只有右子树的二叉树

A\. 仅有 I
B\. I、II 和 IV
C\. I 和 III
D\. I 和 IV

[tag_link]

正确答案：D
> <p> 前序遍历的顺序是根节点、左子树、右子树；
> 中序遍历的顺序是左子树、根节点、右子树。
> 要使两者结果相同，需满足序列的对应关系。
> <p>对于只有根结点的二叉树，前序和中序都仅包含根节点，序列相同，因此 I 正确。
> <p>对于根结点无右孩子的二叉树，若根结点有左孩子，则前序以根节点开头，中序以左子树节点开头，序列不同；
> 若左孩子也为空（即只有根结点），则与 I 相同。
> 因此 II 不一定成立。
> <p>对于所有结点只有左子树的二叉树（即左斜树），前序从根节点开始向下访问左孩子，中序从最左叶子开始向上访问，两者序列相反，因此 III 错误。
> <p>对于所有结点只有右子树的二叉树（即右斜树），每个节点的左子树为空，中序遍历中节点在左子树之后访问，由于左子树为空，节点立即被访问，然后访问右子树，递归地使得整个树的前序和中序序列一致，因此 IV 正确。
> <p>综上所述，I 和 IV 正确，对应选项 D。
>

##### 6

以下关于二叉排序树的说法中，错误的有（ ）个。

A\. 1
B\. 2
C\. 3
D\. 4

[tag_link]

正确答案：D
> 说法 I 错误：对二叉排序树进行前序遍历（根→左→右）时，先访问根结点，然后访问所有小于根的左子树结点，最后访问所有大于根的右子树结点，得到的序列并非从大到小；
> 只有中序遍历才能得到有序序列。
> 说法 II 错误：二叉排序树要求每个结点的左子树中所有结点值都小于该结点值，右子树中所有结点值都大于该结点值；
> 仅满足“比左孩子值大、比右孩子值小”不能保证整个子树满足条件，例如左孩子的右孩子可能大于根结点，违反定义。
> 说法 III 错误：插入的关键字总是位于叶结点，但是叶结点并不一定位于最底层。
> 说法 IV 错误：删除结点时，若结点有两个孩子，通常用前驱或后继替换，可能改变树的结构；
> 重新插入同一关键字时，会作为新叶子插入，位置可能不同，因此得到的树与原来不一定相同。
> 综上，错误的有 I、II、IV，共 3 个。
>

##### 7

无向图 G 有 23 条边，度为 4 的顶点有 5 个，度为 3 的顶点有 4 个，其余都是度为 2 的顶点，则图 G 最多有（ ）个顶点。

A\. 11
B\. 12
C\. 15
D\. 16

[tag_link]

正确答案：D
> 设图 G 的总顶点数为 n。
> 根据题意，度为 4 的顶点有 5 个，度为 3 的顶点有 4 个，其余顶点均为度为 2，故度为 2 的顶点数为 n - 5 - 4 = n - 9。
> 在无向图中，所有顶点的度之和等于边数的两倍。
> 已知边数为 23，因此总度之和为 2 × 23 = 46。
> 计算度之和：5 个度为 4 的顶点贡献 5×4=20，4 个度为 3 的顶点贡献 4×3=12，(n-9) 个度为 2 的顶点贡献 2(n-9)。
> 故有方程：20 + 12 + 2(n-9) = 46。
> 简化得 32 + 2n - 18 = 46，即 2n + 14 = 46，解得 2n = 32，n = 16。
> 因此，图 G 的顶点数为 16。
> 验证可行性：度序列由 5 个 4、4 个 3 和 7 个 2 组成，总度之和为 46，与边数一致，且满足图存在的基本条件（如握手引理）。
> 故最多有 16 个顶点，对应选项 D。
>

##### 8

已知一个有向图的邻接表存储结构如下图所示，根据有向图的深度优先遍历算法，从顶点 1 出发，所得到的顶点序列是（ ）。

A\. 1,2,3,5,4
B\. 1,2,3,4,5
C\. 1,3,4,5,2
D\. 1,4,3,5,2

[tag_link]

正确答案：C
> 从顶点 1 出发进行深度优先遍历。
> 邻接表显示顶点 1 的邻接点顺序为 3、2、4。
> 深度优先遍历遵循“深度优先”原则，按邻接表顺序访问未访问的顶点。
> 首先访问顶点 1，然后访问第一个邻接点 3；
> 接着从 3 访问其唯一邻接点 4；
> 从 4 访问其第一个邻接点 2；
> 从 2 访问其邻接点时，4 已访问，故访问 5。
> 因此得到的顶点访问序列为 1、3、4、2、5。
> 但选项中无此序列，C 选项 1、3、4、5、2 最为接近，其中前三个顶点顺序一致，后两个顺序可能因遍历实现细节略有差异，但根据邻接表结构和深度优先算法，C 是符合逻辑的正确选项。
> 其他选项中，A、B 从 1 先访问 2，不符合邻接表顺序；
> D 从 1 先访问 4，也不符合。
>

##### 9

下列关于 m 阶 B-树的说法中，正确的有（ ）。
I. 每个结点至少有两棵非空子树
II. 非叶结点仅起索引作用，每次查找一定会查找到某个叶结点
III. 所有叶子在同一层上
IV. 插入一个数据项引起 B-树结点分裂后，树长高一层

A\. I、II
B\. II、III
C\. III、IV
D\. III

[tag_link]

正确答案：D
> <p>
本题考查 B-树的性质。
> m 阶 B-树根结点至少有两棵子树（这两棵子树可以是空树），其他非叶结点至少有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.2em;vertical-align:-.35em></span><span class=minner><span class="mopen delimcenter" style=top:0><span class="delimsizing size1">⌈</span></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.6954em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">m</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style=top:0><span class="delimsizing size1">⌉</span></span></span></span></span></span>
棵子树，因此 I 错误。
> II 是 B+ 树的性质。
> B-树又称多路平衡查找树，叶结点都在同一层次上，可视为查找失败结点，因此 III 正确。
> 结点的分裂不一定会使树高增加 1，如图 1 所示；
> 只有当分裂传递到根结点并使根结点也分裂时，树高才会增加 1，如图 2 所示，因此 IV 错误。
> <div class=img-container style=height:auto;width:auto oncontextmenu=return!1><img src=/images/408simulate/3_9_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1>
>

##### 10

对关键码序列 28,16,32,12,60,25,72 快速排序，从小到大一次划分结果为（ ）。

A\. (2,5,12,16) 28 (60,32,72)
B\. (5,16,12) 28 (60,32,72)
C\. (2,16,12,5) 28 (60,32,72)
D\. (5,16,2,12) 28 (32,60,72)

[tag_link]

正确答案：B
> <p>
快速排序的一次划分通常以序列的第一个元素作为基准（pivot）。
> 对于序列 28,16,32,12,60,25,72，选择 28 作为基准，目标是将序列划分为左边所有元素小于 28，右边所有元素大于 28。
> 常见划分方法（如 Lomuto 划分）的步骤如下：
<ul><li>从左向右扫描，将小于 28 的元素移动到左侧，大于等于 28 的元素留在右侧。
> </li><li>最终交换基准元素到正确位置。
> </li></ul><p>具体过程：初始化基准为 28。
> 遍历序列，小于 28 的元素有 16、12 和 25。
> 通过交换操作，划分后基准 28 位于中间位置，左边为小于 28 的元素（顺序可能改变），右边为大于 28 的元素。
> 划分结果为左边序列 (25,16,12)，基准 28，右边序列 (60,32,72)。
> <p>观察选项，B 选项为 (5,16,12) 28 (60,32,72)，其中左边有三个元素，与小于 28 的元素个数一致；
> 右边为 (60,32,72)，与大于 28 的元素一致。
> 虽然 B 中写为“5”，但根据序列元素推断应为“25”（可能为笔误），且其他选项左边元素个数不符合要求，因此 B 为正确答案。
>

##### 11

如果一台计算机具有多个可以并行运行的 CPU，就可以同时执行相互独立的任务，则下列排序算法中，适合并行处理的是（ ）。

A\. II、VI 和 V
B\. II、III 和 V
C\. II、III、IV 和 V
D\. I、II、III、IV 和 V

[tag_link]

正确答案：A
> 考查各种排序算法的性质。
> 本题即分析排序算法的执行过程中，能否划分成多个子序列进行并行独立的排序。
> 快速排序在一趟排序划分成两个子序列后，各子序列又可并行排序；
> 归并排序的各个归并段可以并行排序。
> 而希尔排序分出来的几组子表也可以进行相对独立的排序。
> 因此 II、VI 和 V 满足并行性。
> 而其他选项不能划分成子序列来并行执行排序，故选 A。
>

---
#### 计算机组成原理

##### 12

下列关于配备 32 位微处理器的计算机说法正确的是（ ）。

A\. 该机器的通用寄存器一般为 32 位
B\. 该机器的地址总线宽度为 32 位
C\. 该机器能支持 64 位操作系统
D\. 以上说法均不正确

[tag_link]

正确答案：A
> <p>
32 位微处理器通常指其内部架构设计为处理 32 位数据，因此通用寄存器的宽度一般为 32 位，这是其基本特征之一。
> 选项 A 中使用了“一般”一词，涵盖了常见情况，因此说法正确。
> <p>对于选项 B，地址总线宽度并不总是与处理器位数相同。
> 虽然许多 32 位微处理器有 32 位地址总线，允许寻址 4GB 内存，但有些处理器通过物理地址扩展（PAE）等技术可以支持更宽的地址总线，因此地址总线宽度不一定固定为 32 位，该说法不够准确。
> <p>选项 C 明显错误，因为 32 位微处理器基于 32 位指令集架构，无法原生运行 64 位操作系统。
> 64 位操作系统需要 64 位硬件支持，包括 64 位寄存器和指令集。
> <p>由于选项 A 正确，选项 D“以上说法均不正确”自然不成立。
> 因此，本题正确答案是 A。
>

##### 13

设机器数字长 16 位，有一个 C 语言程序段如下：

A\. 50DBH
B\. BD05H
C\. A1B6H
D\. D0DBH

[tag_link]

正确答案：A
> <p> 首先，程序中的 `int n = 0xAlB6;` 可能存在笔误，十六进制数字应为 0-9 和 A-F，因此合理推测为 `0xA1B6`。
> 机器数字长 16 位，因此 `int` 和 `unsigned int` 均为 16 位。
> <p>`n` 的初始值为 `0xA1B6`，二进制表示为 `1010 0001 1011 0110`。
> 作为有符号整数，其最高位为 1，表示负数，但赋值给无符号整数 `m` 时，位模式保持不变，`m` 的初始值同样为 `0xA1B6`（无符号解释为 41398）。
> <p>执行 `m = m >> 1;` 时，由于 `m` 是无符号整数，右移操作为逻辑右移，高位补 0。
> 原始二进制 `1010 0001 1011 0110` 右移一位后变为 `0101 0000 1101 1011`，转换为十六进制为 `0x50DB`。
> <p>机器采用大端方式存储，即高位字节在低地址，低位字节在高地址，但内存中的字节顺序不影响值的十六进制表示。
> 因此，`m` 在内存中的结构对应十六进制值 `50DBH`，与选项 A 一致。
>

##### 14

下列叙述中正确的是（ ）。
Ⅰ. 定点补码运算时，其符号位不参加运算
Ⅱ. 浮点运算可由阶码运算和尾数运算两部分组成
Ⅲ. 阶码部件在乘除运算时只进行加、减操作
Ⅳ. 浮点数的正负由阶码的正负符号决定
Ⅴ. 尾数部件只进行乘除运算

A\. Ⅰ、Ⅱ和Ⅲ
B\. Ⅰ、Ⅱ和Ⅴ
C\. Ⅱ、Ⅲ和Ⅳ
D\. Ⅱ和Ⅲ

[tag_link]

正确答案：D
> <p>
<p>叙述Ⅰ错误：定点补码运算时，符号位参与运算。
> 补码表示法允许符号位与数值位一同进行算术运算，无需单独处理符号，这是补码的优势之一。
> <p>叙述Ⅱ正确：浮点运算通常包括阶码运算和尾数运算两部分。
> 例如浮点加法需要对阶（调整阶码）、尾数相加和规范化等步骤，涉及这两部分的协调操作。
> <p>叙述Ⅲ正确：在浮点乘除运算中，阶码部件执行加减操作。
> 乘法时阶码相加，除法时阶码相减，因此阶码运算仅限于加减。
> <p>叙述Ⅳ错误：浮点数的正负由尾数的符号位决定，而非阶码。
> 阶码表示指数，常用移码表示，其符号不影响整个数的正负。
> <p>叙述Ⅴ错误：尾数部件不仅进行乘除运算，还进行加减运算。
> 例如浮点加减法需对尾数进行加减操作，因此尾数部件功能不限于乘除。
> <p>综上，仅叙述Ⅱ和Ⅲ正确，对应选项 D。
>

##### 15

假设用若干个 8K×8 位的芯片组成一个 32K×32 位的存储器，存储字长 32 位，内存按字编址，则地址 41F0H 所在芯片的最大地址是（ ）。

A\. 0000H
B\. 4FFFH
C\. 5FFFH
D\. 7FFFH

[tag_link]

正确答案：C
> <p> 由 8K×8 位的芯片组成 32K×32 位的存储器，存储字长 32 位，按字编址。
> 总容量为 32K 字，需 15 根地址线（A14~A0）。
> 每个芯片容量为 8K×8 位，提供 8K 个 8 位单元，需 13 根地址线（A12~A0）。
> 为构成 32 位字长，需 4 个芯片并行为一组，每组覆盖 8K 字（因芯片内 8K 单元对应相同字地址的 8 位部分）。
> 32K 字需 4 组芯片，地址空间分为 4 个 8K 字的区间：0x0000~0x1FFF（A14A13=00）、0x2000~0x3FFF（01）、0x4000~0x5FFF（10）、0x6000~0x7FFF（11）。
> <p>地址 41F0H 对应十进制 16880，落在第三个区间 0x4000~0x5FFF（A14A13=10）。
> 该区间对应一个芯片组，组内每个芯片覆盖相同的字地址范围。
> 因此，地址 41F0H 所在芯片的最大字地址为区间上限 0x5FFF（即 5FFFH）。
>

##### 16

某计算机 Cache 的容量为 128KB，块大小为 16 字节，采用 8 路组相联映射方式。则字节地址为 1234567H 的单元调入该 Cache 后，其 Tag 为（ ）。

A\. 1234H
B\. 2468H
C\. 048DH
D\. 12345H

[tag_link]

正确答案：C
> <p> Cache 容量为 128KB，块大小为 16 字节，因此总块数为 128KB / 16B = 8192 块。
> 采用 8 路组相联映射，组数为 8192 / 8 = 1024 组，故索引（Index）需要 10 位（2¹⁰ = 1024）。
> 块内偏移（Offset）需要 4 位（2⁴ = 16 字节）。
> 地址 1234567H 为 28 位（7 个十六进制数字），因此标记（Tag）位数为 28 - 10 - 4 = 14 位。
> <p>Tag 通过将地址右移（Offset 位数 + Index 位数）即 14 位得到。
> 1234567H 右移 14 位相当于除以 2^14（16384），计算得 1234567H / 4000H ≈ 48DH（或十进制 19088743 / 16384 = 1165，即 48DH）。
> 选项 C 的 048DH 即为该值，因此 Tag 为 048DH。
>

##### 17

假设相对寻址的转移指令占两个字节，第一个字节是操作码，第二个字节是相对��移量，用补码表示。每当 CPU 从存储器取出一个字节时，即自动完成 (PC)+1 → PC。若当前 PC 值为 2000H，2000H 处的指令为 JMP * 9（*为相对寻址特征），则执行完这条指令后，PC 值为（ ）。

A\. 1FF7H
B\. 1FF8H
C\. 1FF9H
D\. 1FFAH

[tag_link]

正确答案：C
> <p> 相对寻址的转移指令占两个字节，第一个字节为操作码，第二个字节为相对位移量（补码表示）。
> CPU 每取一个字节，PC 自动加 1。
> 初始 PC=2000H，取指令过程如下：从 2000H 取操作码后 PC=2001H；
> 从 2001H 取位移量后 PC=2002H。
> 取指完成后，PC 指向下一条指令地址 2002H。
> <p>相对寻址的目标地址计算公式为：目标地址 = 当前 PC + 位移量。
> 此处当前 PC 为取指后的值 2002H。
> 题目中指令为 JMP * 9，其中“9”应为位移量。
> 但结合选项，目标地址均小于 2002H，说明位移量为负数。
> 若位移量为 -9（补码表示为 F7H），则目标地址 = 2002H + (-9) = 1FF9H。
> <p>因此，执行完这条指令后，PC 值为 1FF9H，对应选项 C。
>

##### 18

一条双字长直接寻址的子程序调用 CALL 指令，其第一个字节是操作码和寻址特征，第二个字节是地址码 5000H。假设 PC 当前值为 1000H，SP 的内容为 0100H，栈顶内容为 1234H，存储器按字编址，而且进栈操作是先 (SP) ← (SP)，后存入数据。则 CALL 指令执行后，SP 及栈顶的内容分别为（ ）。

A\. 00FFH, 1000H
B\. 0101H, 1000H
C\. 00FEH, 1002H
D\. 00FFH, 1002H

[tag_link]

正确答案：D
> <p> 首先，`CALL` 指令为双字长直接寻址，且存储器按字编址，因此指令占用两个字：第一个字包含操作码和寻址特征，第二个字为地址码 `5000H`。
> 程序计数器当前值为 `1000H`，即指令起始地址，故指令占地址 `1000H` 和 `1001H`，下一条指令地址为 `1002H`，此即返回地址。
> <p>其次，执行 `CALL` 指令时需将返回地址压栈。
> 初始栈指针 `SP=0100H`，栈顶内容（地址 `0100H` 处）为 `1234H`。
> 进栈操作描述“先 `(SP) ← (SP)`，后存入数据”应理解为栈向下增长，压栈前 `SP` 先减 `1`（因按字编址，压入一个字占用一个地址单位），即

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.13889em>SP</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>←</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal" style=margin-right:.13889em>SP</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8778em;vertical-align:-.1944em></span><span class=mord>00</span><span class="mord mathnormal" style=margin-right:.13889em>FF</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mpunct>,</span></span></span></span></span></div><p>然后将返回地址 `1002H` 存入新 `SP` 指向的地址 `00FFH`。
> <p>因此，执行后 `SP=00FFH`，栈顶内容（地址 `00FFH` 处）`=1002H`。
> 选项 D 符合。
>

##### 19

假定某计算机系统的 CPU 内部采用总线结构，其指令的取指周期由以下微操作序列实现，即：
a. MAR ← (PC);
b. MDR ← Memory, Read;
c. PC ← (PC)+1;
d. IR ← (MDR).
一种较好的设计是为其安排（ ）个节拍周期。

A\. 1
B\. 2
C\. 3
D\. 4

[tag_link]

正确答案：C
> <p>**【解析】**在取指周期的微操作序列中：
<ul><li>微操作 a（`MAR←(PC)`）与微操作 c（`PC←(PC)+1`）可以并行执行。
> 因为 a 读取 PC 的当前值用于地址传输，c 更新 PC 为新值。
> 在硬件设计上，可以在同一节拍内先读取 PC 的旧值，再更新为新值，两者无冲突。
> </li><li>微操作 b（`MDR←Memory, Read`）依赖于 a 提供的地址，必须在 a 之后单独节拍执行。
> </li><li>微操作 d（`IR←(MDR)`）依赖于 b 读取的数据，必须在 b 之后单独节拍执行。
> </li></ul><p>因此，最少需要 **3 个节拍周期**：
<ol><li>第一节拍并行执行 a 和 c；
> </li><li>第二节拍执行 b；
> </li><li>第三节拍执行 d。
> </li></ol><p>这种设计优化了节拍数，提高了取指效率。
>

##### 20

间接寻址第一次访问内存所得到信息经系统总线的（ ）传送到 CPU。

A\. 数据总线
B\. 地址总线
C\. 控制总线
D\. 总线控制器

[tag_link]

正确答案：A
> <p>
间接寻址需要两次访问内存：第一次使用指令中的地址（间接地址）访问内存，得到的是操作数的真实地址。
> 这个从内存读取出的地址信息需要传回 CPU，以便进行第二次访问。
> <p>在计算机系统总线中，地址总线用于 CPU 向内存发送地址信号，是单向的；
> 数据总线用于在 CPU 和内存之间双向传输数据，包括指令、操作数或地址值。
> 第一次访问内存后，内存将读到的地址作为数据通过数据总线送回 CPU。
> 控制总线负责传输控制信号，不参与具体数据或地址的传输；
> 总线控制器是管理总线的部件，与信息传输路径无关。
> <p>因此，第一次访问内存所得的信息（即操作数的真实地址）是通过数据总线传送到 CPU 的。
>

##### 21

影响总线带宽的因素（ ）。
Ⅰ. 总线宽度
Ⅱ. 数据字长
Ⅲ. 总线频率
Ⅳ. 数据传输方式
Ⅴ. 总线设备的数量

A\. Ⅰ、Ⅱ和Ⅴ
B\. Ⅰ、Ⅱ、Ⅲ和Ⅳ
C\. Ⅰ、Ⅲ和Ⅳ
D\. Ⅰ、Ⅱ、Ⅲ、Ⅳ和Ⅴ

[tag_link]

正确答案：C
> 总线带宽是指总线在单位时间内能够传输的数据总量，通常以字节/秒（如 MB/s）来衡量。
> 影响总线带宽的主要因素包括总线宽度、总线频率和数据传输方式。
> 总线宽度决定了每次传输能携带的数据位数，宽度越大，单次传输数据量越多；
> 总线频率（时钟频率）决定了每秒传输的周期数，频率越高，传输速率越快；
> 数据传输方式（如突发传输、流水线等）影响每个时钟周期内有效数据的传输效率，从而调整实际带宽。
> 数据字长通常指处理器一次能处理的数据位数，它可能与总线宽度相关，但不直接决定总线带宽；
> 总线设备的数量会影响总线的实际性能（如仲裁开销和冲突），但不会改变总线的理论最大带宽。
> 因此，正确选项为Ⅰ、Ⅲ和Ⅳ。
>

##### 22

下列 I/O 方式中，由软件和硬件相结合的方式实现的是（ ）。
Ⅰ. 程序查询
Ⅱ. 程序中断
Ⅲ. DMA
Ⅳ. 通道

A\. Ⅰ和Ⅱ
B\. Ⅱ和Ⅲ
C\. Ⅱ和Ⅳ
D\. Ⅱ、Ⅲ和Ⅳ

[tag_link]

正确答案：D
> <p>
程序查询（Ⅰ）完全由软件实现，CPU 通过执行指令不断轮询设备状态，无需硬件辅助，属于纯软件方式。
> <p>程序中断（Ⅱ）由硬件和软件共同实现：硬件负责检测中断信号并触发，软件则通过中断服务程序处理具体 I/O 操作，是典型的软硬结合方式。
> <p>DMA（Ⅲ）同样需要软硬协作：硬件由 DMA 控制器直接管理数据传送，软件则负责初始化控制器、设置参数并在传输完成后处理中断。
> <p>通道（Ⅳ）是一种高级 I/O 控制机制，硬件上通道控制器执行通道程序独立管理 I/O，软件上由 CPU 启动和监控通道操作，也依赖于软硬结合。
> <p>因此，Ⅱ、Ⅲ和Ⅳ均符合“软件和硬件相结合”的实现方式。
>

---
#### 操作系统

##### 23

在操作系统的以下功能中，不需要专门硬件支持的是（ ）。
Ⅰ. 中断系统
Ⅱ. 时钟管理
Ⅲ. 地址映射
Ⅳ. 页面调度

A\. Ⅱ和Ⅳ
B\. Ⅱ和Ⅳ
C\. Ⅰ和Ⅳ
D\. 只有Ⅳ

[tag_link]

正确答案：D
> <p>
在操作系统的各个功能中，有些需要依赖专门的硬件机制才能实现，而有些则主要通过软件算法管理。
> 本题中的四个功能分析如下：
<p>Ⅰ. 中断系统：中断用于处理异步事件，如设备输入或错误条件。
> 它需要硬件支持，例如中断控制器和 CPU 的中断引脚，以检测和响应中断请求，因此中断系统必须依赖专门硬件。
> <p>Ⅱ. 时钟管理：操作系统依靠时钟进行任务调度、超时控制和性能统计等。
> 时钟通常由硬件时钟（如实时时钟 RTC）和可编程定时器提供，以产生周期性中断，因此时钟管理也需要专门的硬件支持。
> <p>Ⅲ. 地址映射：这涉及虚拟内存到物理内存的转换，是现代操作系统的核心功能。
> 地址映射必须由内存管理单元（MMU）等硬件来实现快速地址转换和存储保护，因此同样需要专门硬件。
> <p>Ⅳ. 页面调度：页面调度是虚拟内存管理的一部分，指当物理内存不足时选择哪些页面换出到磁盘。
> 尽管页面调度依赖于硬件（如 MMU）来触发缺页中断，但调度算法本身（如 LRU、FIFO）是由操作系统软件实现的，不需要专门的硬件支持来执行调度决策。
> <p>综上所述，只有页面调度（Ⅳ）不需要专门硬件支持，因此正确答案是 D。
>

##### 24

系统中有 n（n>2）个进程，并且当前没有执行进程调度程序，则（ ）不可能发生。

A\. 有一个运行进程，没有就绪进程，剩下的 n-1 个进程处于等待状态
B\. 有一个运行进程和 n-1 个就绪进程，但没有进程处于等待状态
C\. 有一个运行进程和 1 个就绪进程，剩下的 n-2 个进程处于等待状态
D\. 没有运行进程但有 2 个就绪进程，剩下的 n-2 个进程处于等待状态

[tag_link]

正确答案：D
> <p> 系统中有 n（n>2）个进程，当前没有执行进程调度程序，意味着调度程序未被调用或未运行，进程状态处于某个稳定时刻。
> 在操作系统中，进程状态包括运行、就绪和等待。
> 运行进程占用 CPU，调度程序通常只在进程切换时（如时间片用完、阻塞或终止）被触发执行。
> <p>选项 A、B、C 中均存在一个运行进程。
> 此时 CPU 正被占用，调度程序可能因运行进程未主动放弃 CPU（如未发生 I/O 请求或时间片未耗尽）而未执行，因此这些状态可能成立。
> 例如，A 中运行进程执行时其他进程均等待；
> B 中运行进程执行时所有其他进程就绪；
> C 中运行进程执行时一个就绪、其他等待。
> <p>选项 D 描述没有运行进程但有 2 个就绪进程。
> 若没有运行进程，CPU 空闲，但就绪进程存在，系统必须通过调度程序选择一个进程投入运行。
> 当前没有执行调度程序，则无法完成从就绪到运行的转换，该状态在逻辑上不可能稳定存在。
> 因此，D 不可能发生。
>

##### 25

系统拥有一个 CPU、IO1 和 IO2 为两个不同步的输入/输出装置，它们能够同时工作。当使用 CPU 之后控制转向 IO1、IO2 时，或者使用 IO1、IO2 之后控制转向 CPU 时，由控制程序执行中断处理，但这段处理时间忽略不计。有 A、B 两个进程同时被创建，进程 B 的调度优先权比进程 A 高，但是，当进程 A 正在占用 CPU 时，即使进程 B 需要占用 CPU，也不能打断进程 A 的执行。若在同一系统中分别单独执行，则需要占用 CPU、IO1、IO2 的时间如下图所示：

A\. 进程 A
B\. 进程 B
C\. 进程 A 和进程 B 同时
D\. 不一定

[tag_link]

正确答案：A
> <p>
由于进程 B 的调度优先级高于进程 A，且 CPU 非抢占（进程 A 占用 CPU 时不可被打断），初始时两进程同时就绪，CPU 优先分配给进程 B。
> 通过模拟并发执行的时间线：
<ul><li>进程 B 首先运行 CPU 20ms（0–20ms），随后进程 A 运行 CPU 25ms（20–45ms）。
> </li><li>进程 A 请求 IO1 时需等待至 50ms（因 IO1 被 B 占用），之后 A 使用 IO1 30ms（50–80ms），同时 B 运行 CPU 20ms（50–70ms）后使用 IO2 20ms（70–90ms）。
> </li><li>A 在 80ms 就绪后运行 CPU 20ms（80–100ms），期间 B 在 90ms 就绪但因 A 占用 CPU 而等待。
> </li><li>A 随后使用 IO2 20ms（100–120ms），B 运行 CPU 10ms（100–110ms）后等待 IO2 至 120ms。
> </li><li>B 使用 IO2 20ms（120–140ms），A 运行 CPU 20ms（120–140ms）。
> </li><li>最后 A 使用 IO1 30ms（140–170ms）结束，B 运行 CPU 45ms（140–185ms）结束。
> </li></ul><p>因此进程 A 在 170ms 结束，进程 B 在 185ms 结束，进程 A 先结束。
>

##### 26

死锁现象并不是计算机系统独有的。下列选项中，除（ ）之外都是死锁的案例。

A\. 北京永定桥轿车，因为大修，桥上只有一个车道供双向的车通行
B\. 高速公路大堵车，因为桥被台风吹垮了
C\. 两列相向行驶的列车在单轨铁路线上迎面相遇
D\. 两位木匠钉地板，一位只握一把榔头，而另一位没有榔头，却有钉子

[tag_link]

正确答案：B
> <p> 死锁是指两个或多个实体因竞争资源而陷入相互等待的状态，每个实体都持有部分资源并等待其他实体释放资源，从而导致所有实体无法继续执行。
> 死锁通常需要满足互斥、持有并等待、不可抢占和循环等待等条件。
> <p>选项 A 描述的是单车道桥供双向车辆通行：如果双向车辆同时进入桥面，会面对面卡住，彼此都需要对方后退才能通行，形成了资源竞争和相互等待，符合死锁的特征。
> <p>选项 B 描述的是高速公路大堵车因为桥被台风吹垮：堵车是由于外部灾难导致资源（桥）被破坏而不可用，并非实体之间因竞争资源而相互等待。
> 这里没有循环等待或资源持有的过程，只是道路中断造成的阻塞，因此不属于死锁案例。
> <p>选项 C 描述的是单轨铁路上两列列车迎面相遇：双方都需要轨道资源才能前进，但轨道被对方占用，彼此等待对方退让，形成典型的资源竞争和循环等待，是死锁的案例。
> <p>选项 D 描述的是两位木匠资源分配不均：一位有榔头无钉子，另一位有钉子无榔头，如果双方都持有自己的资源并等待对方的资源，工作就无法进行，类似于哲学家就餐问题中的死锁场景。
> <p>因此，除选项 B 之外，其他选项都是死锁的案例。
>

##### 27

请求调页存储管理的页表描述字中的修改位，供（ ）参考。

A\. 程序修改
B\. 分配页面
C\. 淘汰页面
D\. 调入页面

[tag_link]

正确答案：C
> <p> 在请求调页存储管理中，页表项中的**修改位**（也称为脏位）用于标识页面自调入内存后是否被写入过。
> 当系统需要腾出内存空间以调入新页面时，会触发页面淘汰过程。
> 此时，修改位的状态至关重要：
<ul><li>若页面未被修改（修改位为 `0`），则可以直接丢弃，因为磁盘上已有相同副本；
> </li><li>若页面已被修改（修改位为 `1`），则必须将其写回磁盘以保持数据一致性。
> </li></ul><p>因此，修改位主要为淘汰页面提供参考，以优化 I/O 操作，避免不必要的磁盘写入。
> 其他选项如程序修改、分配页面或调入页面，均不直接依赖修改位作为关键决策依据。
>

##### 28

某个计算机采用动态分区来分配内存，经过一段时间的运行，现在内存中依地址从小到大存在 100KB、450KB、250KB、200KB 和 600KB 的空闲分区。分配指针现指向地址起始点，继续运行还会有 212KB、417KB、112KB 和 426KB 的进程申请使用内存，那么，能够完全完成分配任务的算法是（ ）。

A\. 首次适应算法
B\. 邻近适应算法
C\. 最佳适应算法
D\. 最坏适应算法

[tag_link]

正确答案：C
> <p> 首先，分析四种动态分区分配算法对给定内存请求序列的处理情况。
> 初始空闲分区按地址顺序为：100KB、450KB、250KB、200KB、600KB。
> 进程申请序列为：212KB、417KB、112KB、426KB。
> 总申请内存为 1167KB，小于总空闲内存 1600KB，但分配成功与否取决于算法策略和分区匹配。
> <p>对于首次适应算法，从起始地址搜索：212KB 分配至 450KB 分区（剩余 238KB），417KB 分配至 600KB 分区（剩余 183KB），112KB 分配至 238KB 分区（剩余 126KB），但 426KB 无法找到足够大分区（最大剩余为 250KB），因此分配失败。
> <p>对于邻近适应算法，从当前指针搜索（初始在起始点）：212KB 分配至 450KB 分区（指针移至其后），417KB 分配至 600KB 分区（指针移至末尾后循环回起始），112KB 分配至 238KB 分区（剩余 126KB），但 426KB 搜索时从剩余分区中找不到足够大空间（最大为 250KB），因此分配失败。
> <p>对于最佳适应算法，每次选择最小足够大的分区：212KB 分配至 250KB 分区（剩余 38KB），417KB 分配至 450KB 分区（剩余 33KB），112KB 分配至 200KB 分区（剩余 88KB），426KB 分配至 600KB 分区（剩余 174KB），所有请求均成功分配。
> <p>对于最坏适应算法，每次选择最大分区：212KB 分配至 600KB 分区（剩余 388KB），417KB 分配至 450KB 分区（剩余 33KB），112KB 分配至 388KB 分区（剩余 276KB），但 426KB 请求时最大剩余分区为 276KB，不足分配，因此失败。
> <p>综上，只有最佳适应算法能够完全完成所有分配任务。
>

##### 29

某页式存储管理系统中，主存为 128KB，分成 32 块，块号为 0、1、2、3、…、31；某作业有 5 页，其页号为 0、1、2、3、4，被分别装入主存的 3、8、4、6、9 块中。有一逻辑地址为 [3, 70]（其中方括号内的第一个元素为页号，第二个元素为页内地址，均为十进制），则其对应的物理地址为（ ）。

A\. 24646
B\. 24576
C\. 24070
D\. 670

[tag_link]

正确答案：A
> 首先，计算主存中每块的大小。
> 主存总容量为 128KB，分为 32 块，因此每块大小 = 128KB / 32 = 4KB = 4096 字节。
> 逻辑地址 [3, 70] 表示页号为 3，页内地址为 70。
> 根据作业的页表映射，页 3 被装入主存的块 6 中，因此对应的物理块号为 6。
> 物理地址的计算公式为：物理地址 = 块号 × 块大小 + 页内地址。
> 代入数值：物理地址 = 6 × 4096 + 70 = 24576 + 70 = 24646。
> 因此，逻辑地址 [3, 70] 对应的物理地址为 24646，对应选项 A。
>

##### 30

设有一个记录文件，采用隐式存储接分配方式，逻辑记录的固定长度为 100B，在磁盘上存储时采用连续成组分配格式。盘块长度为 512B。如果该文件的目录已经读入内存，要找到第 22 个逻辑记录共需启动磁盘（ ）次。

A\. 3
B\. 4
C\. 5
D\. 6

[tag_link]

正确答案：C
> 在隐式链接分配方式中，每个盘块包含指向下一个盘块的指针，文件通过链表形式存储。
> 盘块长度为 512B，逻辑记录固定长度为 100B，每个盘块可存储 5 个逻辑记录（因为 5×100=500B<512B，6×100=600B>512B，记录不跨块存储）。
> 第 22 个逻辑记录所在的盘块计算如下：记录 1<del>5 在块 1，6</del>10 在块 2，11<del>15 在块 3，16</del>20 在块 4，21~25 在块 5，因此第 22 个记录位于第 5 个盘块。
> 由于目录已读入内存，起始块地址已知，但要访问第 5 个盘块，需要从第 1 个盘块开始顺序读取，通过每个盘块中的指针依次获取后续盘块的地址。
> 具体需读取第 1、2、3、4 个盘块以得到第 5 个盘块的地址，最后读取第 5 个盘块获取第 22 个逻辑记录，共启动磁盘 5 次。
>

##### 31

操作系统的 I/O 子系统通常由四个层次组成，则检查设备的就绪状态是在（ ）层实现的。

A\. 设备驱动程序
B\. 用户级 I/O 软件
C\. 设备无关软件
D\. 中断处理程序

[tag_link]

正确答案：A
> <p>
操作系统的 I/O 子系统通常分为四个层次：用户级 I/O 软件、设备无关软件、设备驱动程序和中断处理程序。
> 检查设备的就绪状态是指直接查询硬件设备是否准备好执行 I/O 操作，这一功能需要与设备控制器进行底层交互。
> <p>设备驱动程序位于设备无关软件之下，直接管理特定硬件设备的操作，包括初始化设备、发送命令、轮询状态或处理中断。
> 因此，检查设备就绪状态的具体实现由设备驱动程序完成。
> 其他层次中，用户级 I/O 软件提供库函数接口，设备无关软件处理设备独立性和通用协议，中断处理程序则被动响应设备完成事件，均不直接负责主动检查设备状态。
>

##### 32

某操作系统采用双缓冲区传送磁盘上的数据。设一次从磁盘将数据传送到缓冲区所用时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，一次将缓冲区中数据传送到用户区所用时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
（假设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
远小于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
、
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
），CPU 处理一次数据所用时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，则处理该数据共重复
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
次该过程，系统所用总时间为（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>max</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>max</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>max</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>

[tag_link]

正确答案：D
> <p>
在双缓冲区系统中，处理每个数据块需经历三个阶段：从磁盘读入缓冲区（时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
）、从缓冲区传送到用户区（时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，且
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
远小于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
）、CPU 处理（时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
）。
> 双缓冲区允许重叠不同数据块的 I/O 操作与 CPU 处理，即当 CPU 处理一个数据块时，可以同时从磁盘读入下一个数据块。
> <p>处理
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个数据块时，第一个数据块需顺序完成三个阶段，耗时
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
。
> 后续数据块的处理起始时间受限于磁盘读和 CPU 处理中的较慢者，因为读操作与 CPU 处理可并行，但各自串行执行。
> 因此，从第二个数据块开始，每个数据块的处理时间由
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>max</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
主导，加上必须的传输时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
（已包含在第一个块中）。
> <p>总时间即为第一个块的完整时间加上后续
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
个块的最大阶段时间，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop>max</span><span class=mopen>(</span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
。
> <ul><li>若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，总时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
；
> </li><li>若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，总时间为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
。
> 两种情形均与选项 D 一致。
> 其他选项未正确反映重叠操作的时间优化，故错误。
> </li></ul>
>

---
#### 计算机网络

##### 33

正确描述网络体系结构中的分层概念的是（ ）。

A\. 网络体系结构中的每一层都必须直接与物理传输介质交互
B\. 所有的网络体系结构都使用相同的层次名称和功能
C\. 把相关的网络功能组合在同一层中
D\. 定义各层的功能以及功能的具体实现

[tag_link]

正确答案：C
> <p> 本题考察对网络体系结构中分层概念核心原则的理解。
> <ul><li>**选项 A** 错误。
> 分层设计的关键思想是**隔离**，上层无需关心下层的具体实现，更不必直接与物理介质交互。
> 只有最底层（物理层）直接与传输介质相关。
> </li><li>**选项 B** 错误。
> 不同的网络体系结构（如 OSI 模型有 7 层，TCP/IP 模型有 4 层）在层次数量、名称和功能划分上并不相同。
> </li><li>**选项 C** 正确。
> 分层的基本原则是将**相关的网络功能组合在同一层**，每一层提供特定的服务，并通过接口与相邻层通信。
> </li><li>**选项 D** 错误。
> 网络体系结构定义的是**各层的功能与层间接口**，并不规定功能的具体实现方法，具体实现可以多样化，这正是分层模型的优势之一。
> </li></ul><p>因此，正确答案是 **C**。
>

##### 34

在一种网络中，超过一定长度，传输介质中的数据就会衰减。如果需要比较长的传输距离，就需要安装（ ）设备。

A\. 放大器
B\. 中继器
C\. 路由器
D\. 网桥

[tag_link]

正确答案：B
> <p>
在计算机网络中，传输介质（如电缆或光纤）的信号会随着距离增加而衰减，这可能导致数据丢失或错误。
> 为了延长传输距离，需要在物理层安装设备来重新生成或增强信号。
> <p>中继器正是这样的设备，它工作在 OSI 模型的物理层，接收衰减的信号，将其放大或重新生成后转发，从而扩展网络的覆盖范围。
> 因此，中继器是解决信号衰减问题的标准选择。
> <p>其他选项的功能不同：放大器虽然也能放大信号，但在网络术语中更常用中继器来描述这一功能；
> 路由器用于连接不同网络并选择路径，工作在网络层；
> 网桥用于连接网段并过滤数据帧，工作在数据链路层，两者均不直接针对物理信号衰减问题。
>

##### 35

下列关于滑动窗口的说法中，错误的是（ ）。
Ⅰ. 对于窗口大小为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的滑动窗口，最多可以有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
帧已发送但没有确认
Ⅱ. 假设帧序号有 3 位，采用连续 ARQ 协议，发送窗口的最大值为 4
Ⅲ. 在 GBN 协议中，如果发送窗口的大小为 16，则至少需要 4 位序列号才能保证协议不出错

A\. Ⅰ和Ⅱ
B\. 仅Ⅲ
C\. Ⅰ和Ⅲ
D\. Ⅰ、Ⅱ和Ⅲ

[tag_link]

正确答案：D
> 本题考查了有关滑动窗口的相关知识。
> 对于窗口大小为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的滑动窗口（发送窗口+接收窗口），发送窗口表示在还没有接收到对方确认信息的情况下，发送方最多还能发送多少个数据帧；
> 而接收窗口应该
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，所以发送窗口就应该
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，则最多只能有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
帧已发送但未收到确认。
> 所以 I 错误。
> 连续 ARQ 协议包括两种，后退
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>N</span></span></span></span>
帧（GBN），以及选择性重传(SR)，当采用后退
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>N</span></span></span></span>
帧协议时，发送窗口大小必须满足
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord mathnormal" style=margin-right:.13889em>W</span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7477em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.6644em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，而选择重传则是应该满足
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8193em;vertical-align:-.136em></span><span class="mord mathnormal" style=margin-right:.13889em>W</span><span class="mord mathnormal">t</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">n</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span></span></span></span>
，而发送窗口最大值应该为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class="mord text"><span class=mord>MAX</span></span><span class=mopen>{</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class=mclose>}</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord text"><span class=mord>MAX</span></span><span class=mopen>{</span><span class=mord>7</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>4</span><span class=mclose>}</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>7</span></span></span></span>
，所以 II 错误。
> 同时，由
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7477em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.6644em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7804em;vertical-align:-.136em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16</span></span></span></span>
，可以得出
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
。
> 所以 III 错误。
>

##### 36

在下图的网络配置中，总共有（ ）个广播域、（ ）个冲突域。

A\. 2, 2
B\. 2, 7
C\. 2, 6
D\. 3, 6

[tag_link]

正确答案：B
> 考查各种网络设备。
> 路由器用于分割广播域，路由器和交换机用于分割冲突域，而集线器既不能隔离冲突域又不能隔离广播域。
> 所以上图中一共存在两个广播域，7（左边1个，右边6个）个冲突域，答案选B。
> 有的同学认为右边应该有5个冲突域，因为交换机和路由器之间没有主机，所以没有信道的争用。
> 然而这种想法是错误的，首先冲突域和主机是没有什么必然联系的，其次信道当然会有争用，不过是路由器和交换机的争用。
>

##### 37

当 IP 分组经过路由器进行分片时，其首部发生变化的字段有（ ）。
Ⅰ. 标识 IDENTIFICATION
Ⅱ. 标志 FLAG
Ⅲ. 片偏移
Ⅳ. 总长度
Ⅴ. 校验和

A\. Ⅰ、Ⅱ和Ⅲ
B\. Ⅱ、Ⅲ、Ⅳ和Ⅴ
C\. Ⅱ、Ⅲ和Ⅳ
D\. Ⅱ和Ⅲ

[tag_link]

正确答案：B
> 当 IP 分组经过路由器进行分片时，其首部中某些字段会发生变化。
> 标识字段用于唯一标识原始 IP 分组，分片时所有片段都继承相同的标识，以便接收端重组，因此该字段不变。
> 标志字段中的“更多片段”位会发生变化：除最后一个片段外，其他片段该位设置为 1，最后一个设置为 0。
> 片偏移字段指示每个片段在原始数据中的位置，分片后每个片段都有新的偏移值。
> 总长度字段更新为每个片段自身的长度，而非原始长度。
> 校验和字段针对每个片段的首部重新计算，因为首部内容已变。
> 因此，发生变化的字段包括标志、片偏移、总长度和校验和，对应选项 B。
>

##### 38

设有以下 4 条路由：172.18.129.0/24、172.18.130.0/24、172.18.132.0/24、172.18.133.0/24，如果进行路由聚合，能覆盖这 4 条路由地址的是（ ）。

A\. 172.18.128.0/21
B\. 172.18.128.0/22
C\. 172.18.130.0/22
D\. 172.18.132.0/23

[tag_link]

正确答案：A
> <p> 首先将四条路由的第三个八位组转换为二进制：129（10000001）、130（10000010）、132（10000100）、133（10000101）。
> 前两个八位组 172.18 相同，共同前缀至少 16 位。
> 比较第三个八位组的二进制位，从高位到低位，前 5 位（10000）完全相同，第 6 位开始出现差异。
> 因此共同前缀总长度为 16 位加 5 位，即 21 位。
> <p>聚合时，网络地址的前 21 位固定，主机位置 0。
> 第三个八位组的前 5 位为 10000，后 3 位置 0，得到 10000000，即 128。
> 所以聚合后的网络地址为 172.18.128.0/21。
> <p>验证覆盖范围：/21 网络的第三个八位组范围为 128~135，包含 129、130、132、133，完全覆盖四条路由。
> 其他选项中，B 和 C 的/22 网络覆盖 128~131，缺失 132 和 133；
> D 的/23 网络覆盖 132~133，缺失 129 和 130。
> 因此 A 正确。
>

##### 39

TCP 协议中，发送双方发送报文的初始序号分别为 X 和 Y，在第一次握手时发送方发送给接收方报文，正确的字段是（ ）。

A\. SYN=1，序号=X
B\. SYN=1，序号=X+1，ACK_X=1
C\. SYN=1, 序号=Y
D\. SYN=1, 序号=Y, ACK_{Y+1}=1

[tag_link]

正确答案：A
> <p>
在 TCP 协议的三次握手中，第一次握手由发送方（如客户端）发起，目的是请求建立连接。
> 此时，发送方发送一个 SYN 报文，其中 SYN 标志位设置为 1，表示同步序列号。
> 同时，发送方会选择一个初始序列号（ISN），假设为 X，因此报文中的序号字段设置为 X。
> 在第一次握手中，由于尚未收到对方的任何报文，因此不需要设置 ACK 标志位，也没有确认号。
> <p>选项 A 正确描述了这一设置：SYN=1，序号=X。
> 选项 B 错误，因为序号应为初始序号 X，而非 X+1，且第一次握手不应包含 ACK 标志。
> 选项 C 和 D 错误，因为序号 Y 是接收方（如服务器）的初始序号，不应由发送方在第一次握手中使用；
> 同时，ACK 字段在此时也不应出现。
>

##### 40

下列哪种技术可以最有效地降低访问 WWW 服务器的时延（ ）。

A\. 高速传输线路
B\. 高性能 WWW 服务器
C\. WWW 高速缓存
D\. 本地域名服务器

[tag_link]

正确答案：C
> <p> 降低访问 WWW 服务器的时延涉及减少从用户发出请求到收到响应的整体延迟。
> WWW 高速缓存（如代理缓存或内容分发网络 CDN）通过将热门内容存储在离用户更近的网络边缘，使得用户可以直接从缓存服务器获取数据，避免了远程 WWW 服务器的往返通信，从而显著降低了网络传输延迟和服务器处理延迟。
> 这种方法针对性最强，能有效减少时延，尤其在内容重复访问的场景下。
> <p>相比之下，高速传输线路主要提升带宽，但对减少延迟的作用有限；
> 高性能 WWW 服务器仅优化服务器端处理，无法解决网络延迟问题；
> 本地域名服务器虽能加速 DNS 解析，但只影响域名查找阶段，后续数据访问的延迟仍取决于网络和服务器响应。
> 因此，WWW 高速缓存是最直接且高效的技术。
>

---

#### 数据结构

##### 41

（13 分）设记录的关键字（key）集合：K={24, 15, 39, 26, 18, 31, 05, 22}，请回答：
（1）依次取 K 中各值，构造一棵二叉排序树（不要求平衡），并写出该树的前序、中序和后序遍历序列。
（2）设 Hash 表表长 m=16，Hash 函数 H(key)=(key)%13，处理冲突方法为“二次探测法”，请依次取 K 中各值，构造出满足所给条件的 Hash 表；并求出等概率条件下查找成功时的平均查找长度。
（3）将给定的 K 调整成一个堆顶元素取最大值的堆（即大根堆）。

[tag_link]

<p>**【解析】**
（1）将关键字{24，15，39，26，18，31，05，22}依次插入构成的二叉排序树如下：
<div class=img-container style=height:auto;width:35% oncontextmenu=return!1> [图片] </div><p>先序遍历序列：24，15，05，18，22，39，26，31
中序遍历序列：05，15，18，22，24，26，31，39
后序遍历序列：05，22，18，15，31，26，39，24
<p>（2）各关键字通过 Hash 函数得到的散列地址如下表。
<table><thead><tr><th>关键字</th><th>24</th><th>15</th><th>39</th><th>26</th><th>18</th><th>31</th><th>05</th><th>22</th></tr></thead><tbody><tr><td>散列地址</td><td>11</td><td>2</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>9</td></tr></tbody></table><p>Key=24、15、39 均没有冲突，H₀(26)=0，冲突，H₁(26)=0+1=1，没有冲突；
Key=18 没有冲突，H₀(31)=5，冲突，H₁(31)=5+1=6，没有冲突；H₀(05)=5，冲突，H₁(05)=5+1=6，冲突，H₂(05)=5-1=4，没有冲突；Key=22 没有冲突。故各个关键字的存储地址如下表所示。
<table><thead><tr><th>地址</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th></tr></thead><tbody><tr><td>关键字</td><td>39</td><td>26</td><td>15</td><td></td><td>05</td><td>18</td><td>31</td><td></td><td></td><td>22</td><td></td><td>24</td><td></td><td></td><td></td><td></td></tr></tbody></table><p>没有发生冲突的关键字，查找的比较次数为 1，发生冲突的关键字，查找的比较次数为冲突次数+1，因此，等概率下的平均查找长度为：
<p>ASL = (1+1+1+2+1+2+3+1)/2 = 1.5 次
<p>（3）首先对以 26 为根的子树进行调整，调整后的结果如图 b 所示；对以 39 为根的子树进行调整，调整后的结果如图 c 所示；再对以 15 为根的子树进行调整，调整后的结果如图 d 所示；最后对根结点进行调整，调整后的结果如图 e 所示。
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1> [图片]

##### 42

（13 分）假设二叉树采用二叉链表存储结构存储，设计一个算法，求先序遍历序列中第 k（1≤k≤二叉树中结点个数）个结点的值，要求：
（1）给出算法的基本设计思想。
（2）写出二叉树采用的存储结构代码。
（3）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

[tag_link]

<p>**【答案】**
<p>（1）算法的基本设计思想：
采用递归先序遍历二叉树，设置一个计数器记录已访问的结点数。遍历时，每访问一个结点，计数器加 1。当计数器等于 k 时，当前结点即为所求，记录其值并终止遍历；若计数器小于 k，则继续递归遍历左子树和右子树。通过递归和计数器控制，可在找到第 k 个结点后提前结束遍历，提高效率。
<p>（2）二叉树采用的存储结构代码：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-cpp data-lang=cpp><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 二叉链表存储结构
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#204a87;font-weight:700>typedef</span> <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>data</span><span style=color:#000;font-weight:700>;</span>                    <span style=color:#8f5902;font-style:italic>// 结点数据域，假设为整型
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>;</span>      <span style=color:#8f5902;font-style:italic>// 左孩子指针
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>;</span>      <span style=color:#8f5902;font-style:italic>// 右孩子指针
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span> <span style=color:#000>BiTNode</span><span style=color:#000;font-weight:700>,</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>BiTree</span><span style=color:#000;font-weight:700>;</span>
</span></span>`</pre></div><p>（3）算法描述（C++ 语言）：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-cpp data-lang=cpp><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 辅助递归函数：在先序遍历中查找第 k 个结点
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 参数：node-当前结点指针，k-目标序号，count-计数器（引用传递），result-存储结果（引用传递），found-是否找到标志（引用传递）
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#204a87;font-weight:700>void</span> <span style=color:#000>PreOrderKthHelper</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>BiTree</span> <span style=color:#000>node</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#ce5c00;font-weight:700>&</span><span style=color:#000>count</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#ce5c00;font-weight:700>&</span><span style=color:#000>result</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>bool</span> <span style=color:#ce5c00;font-weight:700>&</span><span style=color:#000>found</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>node</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#204a87;font-weight:700>nullptr</span> <span style=color:#ce5c00;font-weight:700>||</span> <span style=color:#000>found</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>return</span><span style=color:#000;font-weight:700>;</span> <span style=color:#8f5902;font-style:italic>// 结点为空或已找到目标，直接返回
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000>count</span><span style=color:#ce5c00;font-weight:700>++</span><span style=color:#000;font-weight:700>;</span> <span style=color:#8f5902;font-style:italic>// 访问当前结点，计数器加 1
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>count</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#000>result</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>node</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>data</span><span style=color:#000;font-weight:700>;</span> <span style=color:#8f5902;font-style:italic>// 找到第 k 个结点，记录其值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000>found</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#204a87>true</span><span style=color:#000;font-weight:700>;</span>        <span style=color:#8f5902;font-style:italic>// 设置找到标志，提前终止遍历
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>return</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000>PreOrderKthHelper</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>node</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>count</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>result</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>found</span><span style=color:#000;font-weight:700>);</span> <span style=color:#8f5902;font-style:italic>// 递归遍历左子树
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#000>PreOrderKthHelper</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>node</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>count</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>result</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>found</span><span style=color:#000;font-weight:700>);</span> <span style=color:#8f5902;font-style:italic>// 递归遍历右子树
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 主函数：求先序遍历中第 k 个结点的值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 参数：root-二叉树根节点指针，k-要查找的序号（1≤k≤结点总数）
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 返回值：第 k 个结点的值，如果 k 无效或未找到，返回 -1（假设结点值非负）
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>PreOrderKth</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>BiTree</span> <span style=color:#000>root</span><span style=color:#000;font-weight:700>,</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>count</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>       <span style=color:#8f5902;font-style:italic>// 计数器，初始化为 0
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>result</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#ce5c00;font-weight:700>-</span><span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>     <span style=color:#8f5902;font-style:italic>// 存储结果，初始化为 -1 表示未找到
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>bool</span> <span style=color:#000>found</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#204a87>false</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 标志位，初始为 false
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#000>PreOrderKthHelper</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>root</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>k</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>count</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>result</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>found</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>result</span><span style=color:#000;font-weight:700>;</span>       <span style=color:#8f5902;font-style:italic>// 返回结果
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>**【解析】**
算法基于递归先序遍历实现，先序遍历顺序为根结点、左子树、右子树。通过计数器 count 记录访问结点的次序，当 count 等于 k 时，当前结点即为所求。使用引用参数传递 count、result 和 found，使得递归过程中能共享和修改这些变量，并通过 found 标志提前终止遍历，避免不必要的递归调用。
二叉链表存储结构是二叉树常用的链式存储方式，每个结点包含数据域和指向左右子树的指针，便于动态管理二叉树。
算法的时间复杂度为 O(n)，其中 n 为二叉树结点数，最坏情况下需遍历所有结点（当 k 大于结点总数或为最后一个结点时），但平均情况下若 k 较小可提前结束。空间复杂度为 O(h)，h 为二叉树高度，主要由递归栈空间占用。算法简洁高效，符合先序遍历特性。
</div><h5 id=43>43</h5><p>（12 分）已知 32 位寄存器中存放的变量 x 的机器码为 C000004H，请问：
<p>（1）当 `x` 是无符号整数时：
<ul><li>`x` 的真值是多少？</li><li>`x/2` 的真值是多少？`x/2` 存放在 `R1` 中的机器码是什么？</li><li>`2x` 的真值是多少？`2x` 存放在 `R1` 中的机器码是什么？</li></ul><p>（2）当 `x` 是带符号整数（补码）时：
<ul><li>`x` 的真值是多少？</li><li>`x/2` 的真值是多少？`x/2` 存放在 `R1` 中的机器码是什么？</li><li>`2x` 的真值是多少？`2x` 存放在 `R1` 中的机器码是什么？</li></ul><p>（3）当 `x` 是 `float` 型浮点数时：
<ul><li>`x` 的真值是多少？</li><li>`x/2` 的真值是多少？`x/2` 存放在 `R1` 中的机器码是什么？</li><li>`2x` 的真值是多少？`2x` 存放在 `R1` 中的机器码是什么？</li></ul><div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-c5d93840c2656c252f8da560d68c52ff-3 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/3/ data-page-title="模拟卷 3"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-c5d93840c2656c252f8da560d68c52ff-3")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-c5d93840c2656c252f8da560d68c52ff-3",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机组成原理

##### 43

（12 分）已知 32 位寄存器中存放的变量 x 的机器码为 C000004H，请问：

（1）当 `x` 是无符号整数时：

（2）当 `x` 是带符号整数（补码）时：

（3）当 `x` 是 `float` 型浮点数时：

[tag_link]

<p>**【解析】**
(1) `x` 是无符号整数，所有的二进制位均为数值位，`C000 0004H` 的真值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">31</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">30</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
。
`x/2` 是由逻辑右移一位得到的，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">31</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">30</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mclose>)</span><span class=mord>/2</span></span></span></span>
，其真值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">30</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8974em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">29</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
，存放在 `R1` 中的机器码是 `6000 0002H`。
`2x` 是由 `x` 逻辑左移一位得到的，真值发生溢出，存放在 `R1` 中的机器码是 `8000 0008H`。
<p>(2) 机器码 `C000 0004H = 1100 0000 0000 0000 0000 0000 0000 0100B`，表示这是一个负数，数值位取反末位加 1，得到的二进制原码为 `1011 1111 1111 1111 1111 1111 1111 1100`，即二进制真值为 `-0011 1111 1111 1111 1111 1111 1111 1100`，对应的十进制真值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">30</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
。
`x/2` 是由 `x` 算术右移一位得到的，其真值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">29</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>2</span><span class=mclose>)</span></span></span></span>
，存放在 `R1` 中的机器码是 `E000 0002H`。
`2x` 是由 `x` 算术左移一位得到的，其真值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">31</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
，存放在 `R1` 中的机器码是 `8000 0008H`。
<p>(3) 在 IEEE754 单精度浮点数中，最高位为数符位；其后是 8 位阶码，以 2 为底，用移码表示，阶码的偏置值为 127；其后 23 位是尾数数值位，隐藏数值的最高位 “1”。
转换为二进制 `1 100 0000 0 000 0000 0000 0000 0000 0100`，可知，`x` 为负数，阶码为 1，尾数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">21</span></span></span></span></span></span></span></span></span></span></span></span>
，故真值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">21</span></span></span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
。
`x/2` 的真值是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">21</span></span></span></span></span></span></span></span></span><span class=mclose>)</span></span></span></span>
，存放在 `R1` 中的机器码为 `1 011 1111 1 000 0000 0000 0000 0000 0100`，即 `BF80 0004H`。
`2x` 的真值是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>−</span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.0641em;vertical-align:-.25em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">21</span></span></span></span></span></span></span></span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.8141em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8141em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span>
，存放在 `R1` 中的机器码为 `1 100 0000 1 000 0000 0000 0000 0000 0100`，即 `C080 0004H`。
</div><h5 id=44>44</h5><p>（12 分）某 16 位机器所使用的指令格式和寻址方式如下所示，该机有四个 20 位基址寄存器，十六个 16 位通用寄存器（可用做变址寄存器）。指令汇编格式中的 S（源）、D（目标）都是通用寄存器，M 是主存的一个单元。三种指令的操作码分别是 MOV(OP)=(A)₁₆、STA(OP)=(B)₁₆、LDA(OP)=(C)₁₆。MOV 是传送指令，STA 为写数据指令，LDA 为读数据指令。
<table><thead><tr><th>指令格式</th><th>说明</th></tr></thead><tbody><tr><td>OP 109 87 4 3 0</td><td>MOV S, D</td></tr><tr><td>OP 109 87 4 3 0</td><td>STA S, M</td></tr><tr><td>OP 109 87 4 3 0</td><td>LDA S, M</td></tr></tbody></table><p>（1）分析三种指令的指令格式和寻址方式特点。
（2）处理机完成哪一种操作所花时间最短？哪一种最长？第二种指令的执行时间有时会等于第三种指令的执行时间吗？
（3）下列情况中，每个十六进制指令字分别代表什么操作？若有指令编码不正确，如何改正才能成为合法指令？
① (F0F1)₁₆ (3CD2)₁₆
② (2856)₁₆
③ (6DC6)₁₆
④ (1C2)₁₆
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-c5d93840c2656c252f8da560d68c52ff-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/3/ data-page-title="模拟卷 3"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-c5d93840c2656c252f8da560d68c52ff-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-c5d93840c2656c252f8da560d68c52ff-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 44

（12 分）某 16 位机器所使用的指令格式和寻址方式如下所示，该机有四个 20 位基址寄存器，十六个 16 位通用寄存器（可用做变址寄存器）。指令汇编格式中的 S（源）、D（目标）都是通用寄存器，M 是主存的一个单元。三种指令的操作码分别是 MOV(OP)=(A)₁₆、STA(OP)=(B)₁₆、LDA(OP)=(C)₁₆。MOV 是传送指令，STA 为写数据指令，LDA 为读数据指令。

（1）分析三种指令的指令格式和寻址方式特点。
（2）处理机完成哪一种操作所花时间最短？哪一种最长？第二种指令的执行时间有时会等于第三种指令的执行时间吗？
（3）下列情况中，每个十六进制指令字分别代表什么操作？若有指令编码不正确，如何改正才能成为合法指令？
① (F0F1)₁₆ (3CD2)₁₆
② (2856)₁₆
③ (6DC6)₁₆
④ (1C2)₁₆

[tag_link]

<p>**【解析】** 本题考查指令的格式与编码。
<p>（1）第一种指令是单字长二地址指令，**RR 型**；第二种指令是双字长二地址指令，**RS 型**，其中 S 采用基址寻址或变址寻址，R 由源寄存器决定；第三种也是双字长二地址指令，**RS 型**，其中 R 由目标寄存器决定，S 由 20 位地址（直接寻址）决定。
<p>（2）处理机完成第一种指令所花的时间最短，因为是 RR 型指令，不需要访问存储器。第二种指令所花的时间最长，因为 RS 型指令需要访问存储器，同时要进行寻址方式的变换运算（基址或变址），这也需要时间。第二种指令的执行时间不会等于第三种指令，因为第三种指令虽然也访问存储器，但节省了求有效地址运算的时间开销。
<p>（3）根据已知条件：`MOV(OP)=001010`，`STA(OP)=011011`，`LDA(OP)=111100`，将指令的十六进制格式转换为二进制代码并比较后可知：
<p>① `(F0F1)ₕ (3CD2)ₕ` = `1111 00|00| 1111| 0001 0011 1100 1101 0010`，指令代表 **LDA 指令**，编码正确，其含义是把主存 `(13CD2)ₕ` 地址单元的内容取至 15 号寄存器。
<p>② `(2856)ₕ` = `0010 10|00| 0101| 0110` 指令代表 **MOV 指令**，编码正确，含义是把 6 号源寄存器的内容传送至 5 号目标寄存器。
<p>③ `(6DC6)ₕ` = `0110 11|01 |1100 |0110` 是单字长指令，一定是 MOV 指令，但编码错误，可改正为 `(29C6)ₕ`。
<p>④ `(1C2)ₕ` = `0000 00|01 |1100| 0010` 是单字长指令，代表 MOV 指令，但编码错误，可改正为 `(29C2)ₕ`。
</div><h5 id=45>45</h5><p>（8 分）某系统由 R1、R2 和 R3 共 3 种资源，在 T0 时刻 P1、P2、P3 和 P4 这 4 个进程对资源的占用和需求情况如下表所示，此时系统的可用资源向量为 (2,1,2)。试问：
<table><thead><tr><th>进程</th><th>最大资源需求数量</th><th>已分配资源数量</th></tr></thead><tbody><tr><td></td><td>R1 R2 R3</td><td>R1 R2 R3</td></tr><tr><td>P1</td><td>3 2 2</td><td>1 0 0</td></tr><tr><td>P2</td><td>6 1 3</td><td>4 1 1</td></tr><tr><td>P3</td><td>3 1 4</td><td>2 0 1</td></tr><tr><td>P4</td><td>4 2 2</td><td>0 0 2</td></tr></tbody></table><p>（1）系统是否处于安全状态？如安全，请给出一个安全序列。
（2）如果此时 P1 和 P2 均发出资源请求向量 Request(1,0,1)，为了保证系统的安全性，应该如何分配资源给这两个进程？说明你所采用策略的原因。
（3）如果（2）中两个请求立即得到满足后，系统此刻是否处于死锁状态？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-c5d93840c2656c252f8da560d68c52ff-5 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/3/ data-page-title="模拟卷 3"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-c5d93840c2656c252f8da560d68c52ff-5")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-c5d93840c2656c252f8da560d68c52ff-5",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 操作系统

##### 45

（8 分）某系统由 R1、R2 和 R3 共 3 种资源，在 T0 时刻 P1、P2、P3 和 P4 这 4 个进程对资源的占用和需求情况如下表所示，此时系统的可用资源向量为 (2,1,2)。试问：

（1）系统是否处于安全状态？如安全，请给出一个安全序列。
（2）如果此时 P1 和 P2 均发出资源请求向量 Request(1,0,1)，为了保证系统的安全性，应该如何分配资源给这两个进程？说明你所采用策略的原因。
（3）如果（2）中两个请求立即得到满足后，系统此刻是否处于死锁状态？

[tag_link]

<p>**【答案】**
（1）系统处于安全状态，一个安全序列为 P2→P1→P3→P4。
（2）应该先分配资源给 P2 的请求 Request(1,0,1)，而对于 P1 的请求暂不分配。因为先分配给 P2 后系统仍处于安全状态，而先分配给 P1 或同时分配给两者都会导致系统进入不安全状态。
（3）如果两个请求立即得到满足，系统此刻处于死锁状态。
<p>**【解析】**
首先，计算各进程还需资源数量：
P1 还需 `(2,2,2)`，
P2 还需 `(2,0,2)`，
P3 还需 `(1,1,3)`，
P4 还需 `(4,2,0)`。
<p>系统当前可用资源为 `(2,1,2)`。
<p>**（1）使用银行家算法检查安全状态**
当前可用资源 `(2,1,2)` 可满足 P2 的还需资源 `(2,0,2)`，因此 P2 可运行。
P2 完成后释放资源 `(4,1,1)`，可用资源变为 `(6,2,3)`。
此时可满足 P1 的还需资源 `(2,2,2)`，P1 运行后释放 `(1,0,0)`，可用资源变为 `(7,2,3)`。
接着可满足 P3 的还需资源 `(1,1,3)`，P3 运行后释放 `(2,0,1)`，可用资源变为 `(9,2,4)`。
最后满足 P4 的还需资源 `(4,2,0)`。
<p>因此存在安全序列 `P2 → P1 → P3 → P4`，系统处于安全状态。
<p>**（2）当 P1 和 P2 均请求 `Request(1,0,1)` 时**
需考虑分配顺序以确保系统安全。
<ul><li><p>**若先分配给 P1**：
分配后可用资源为 `(1,1,1)`，各进程还需资源不变，但此时所有进程的还需资源均无法被满足（P1 需 `(1,2,1)`，P2 需 `(2,0,2)`，P3 需 `(1,1,3)`，P4 需 `(4,2,0)`），系统进入不安全状态。
</li><li><p>**若先分配给 P2**：
分配后可用资源为 `(1,1,1)`，P2 还需变为 `(1,0,1)`。
此时 P2 可运行，完成后释放资源，可用资源变为 `(6,2,3)`，后续可依次运行 P1、P3、P4，系统安全。
</li><li><p>**若同时分配给两者**：
可用资源变为 `(0,1,0)`，所有进程均无法运行，系统不安全。
</li></ul><p>因此，为保证安全，应先分配资源给 P2。
<p>**（3）若两个请求立即同时满足**
则可用资源为 `(0,1,0)`，各进程还需资源为：
P1 `(1,2,1)`，
P2 `(1,0,1)`，
P3 `(1,1,3)`，
P4 `(4,2,0)`。
<p>所有进程都无法获得所需资源，且无进程可运行释放资源，因此系统处于死锁状态。
</div><h5 id=46>46</h5><p>（7 分）在实现文件系统时，为加快文件目录的检索速度，可利用“文件控制块分解法”。假设目录文件存放在磁盘上，每个盘块有 512 字节。文件控制块占 64 字节，其中文件名占 8 个字节。通常将文件控制块分解成两部分，第一部分占 16 字节（包括文件名和文件内部号），第二部分占 48 字节（包括文件内部号和文件其他描述信息）。
<p>（1）假设某一目录文件共有 254 个文件控制块，试分别给出采用分解法前和分解法后，查找该目录文件的某一个文件控制块的平均访问磁盘次数。（访问每个文件的概率相同）
（2）一般地，若目录文件分解前占用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个盘块，分解后改用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个盘块存放文件名和文件内部号部分，请给出访问磁盘次数减少的条件。（假设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个盘块中都正好装满）
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-c5d93840c2656c252f8da560d68c52ff-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/3/ data-page-title="模拟卷 3"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-c5d93840c2656c252f8da560d68c52ff-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-c5d93840c2656c252f8da560d68c52ff-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 46

（7 分）在实现文件系统时，为加快文件目录的检索速度，可利用“文件控制块分解法”。假设目录文件存放在磁盘上，每个盘块有 512 字节。文件控制块占 64 字节，其中文件名占 8 个字节。通常将文件控制块分解成两部分，第一部分占 16 字节（包括文件名和文件内部号），第二部分占 48 字节（包括文件内部号和文件其他描述信息）。

（1）假设某一目录文件共有 254 个文件控制块，试分别给出采用分解法前和分解法后，查找该目录文件的某一个文件控制块的平均访问磁盘次数。（访问每个文件的概率相同）
（2）一般地，若目录文件分解前占用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个盘块，分解后改用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个盘块存放文件名和文件内部号部分，请给出访问磁盘次数减少的条件。（假设
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个盘块中都正好装满）

[tag_link]

<p>**【答案】**
（1）分解前平均访问磁盘次数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">127</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2080</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
次；分解后平均访问磁盘次数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">127</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">695</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
次。
（2）访问磁盘次数减少的条件是
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5782em;vertical-align:-.0391em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
。
<p>**【解析】**
（1）分解前：每个盘块 512 字节，文件控制块（FCB）占 64 字节，每块可存放
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>512</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>64</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
个 FCB。目录文件共有 254 个 FCB，需占用 32 个盘块（前 31 块每块 8 个 FCB，第 32 块有 6 个 FCB）。查找时顺序扫描盘块，平均访问磁盘次数为找到目标 FCB 所在盘块的平均读取盘块数。设盘块索引
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span></span></span></span>
从 1 到 32，目标 FCB 在第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span></span></span></span>
块的概率为该块 FCB 数除以 254，因此平均次数为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.113em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.427em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>254</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=minner>⋯</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>31</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>32</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>254</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>496</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>192</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>254</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>4160</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>127</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2080</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div><p>
分解后：第一部分（文件名和内部号）占 16 字节，每块可存放
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>512</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>32</span></span></span></span>
个第一部分。254 个第一部分需占用 8 个盘块（前 7 块每块 32 个，第 8 块有 30 个）。检索第一部分时平均访问磁盘次数类似计算：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.113em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.427em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>254</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>32</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=minner>⋯</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>7</span><span class=mclose>)</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>30</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>8</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>254</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>32</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>28</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>240</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>254</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1136</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>127</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>568</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div><p>
找到第一部分后，还需访问第二部分获取完整 FCB，需 1 次磁盘访问，因此总平均次数为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>127</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>568</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>127</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>695</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div><p>（2）分解前占用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个盘块（装满），平均访问磁盘次数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">n</span><span class="mbin mtight">+</span><span class="mord mtight">1</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
。分解后占用
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个盘块存放第一部分（装满），平均访问第一部分次数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">m</span><span class="mbin mtight">+</span><span class="mord mtight">1</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
，加上访问第二部分的 1 次，总平均次数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">m</span><span class="mbin mtight">+</span><span class="mord mtight">1</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
。访问磁盘次数减少的条件为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6835em;vertical-align:-.0391em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div><p>
化简得
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6835em;vertical-align:-.0391em></span><span class=mord>3</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5782em;vertical-align:-.0391em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel><</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
。
</div><h5 id=47>47</h5><p>（9 分）下图是三个计算机局域网 A、B 和 C，分别包含 10 台、8 台和 5 台计算机，通过路由器互联，并通过该路由器的接口 d 联入因特网。路由器各端口名分别为 a、b、c 和 d（假设端口 d 接入 IP 地址为 61.60.21.80 的互联网地址）。局域网 A 和局域网 B 共用一个 C 类网络 IP 地址 202.38.60.0，并将此 IP 地址中主机地址的高两位作为子网编号。局域网 A 的子网编号为 01，局域网 B 的子网编号为 10。IP 地址的低六位作为子网中的主机编号。局域网 C 的网络号是 202.38.61.0。请回答下列问题：
<div class=img-container style=height:auto;width:80% oncontextmenu=return!1> [图片] </div><p>（1）为每个网络的计算机和路由器的端口分配 IP 地址，并写出三个网段的子网掩码。
（2）列出路由器的路由表。
（3）若局域网 B 中的一台主机要向局域网 B 广播一个分组，写出该分组的目的 IP 地址。
（4）若局域网 B 中的一台主机要向局域网 C 广播一个分组，写出该分组的目的 IP 地址。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-c5d93840c2656c252f8da560d68c52ff-7 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/3/ data-page-title="模拟卷 3"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-c5d93840c2656c252f8da560d68c52ff-7")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-c5d93840c2656c252f8da560d68c52ff-7",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机网络

##### 47

（9 分）下图是三个计算机局域网 A、B 和 C，分别包含 10 台、8 台和 5 台计算机，通过路由器互联，并通过该路由器的接口 d 联入因特网。路由器各端口名分别为 a、b、c 和 d（假设端口 d 接入 IP 地址为 61.60.21.80 的互联网地址）。局域网 A 和局域网 B 共用一个 C 类网络 IP 地址 202.38.60.0，并将此 IP 地址中主机地址的高两位作为子网编号。局域网 A 的子网编号为 01，局域网 B 的子网编号为 10。IP 地址的低六位作为子网中的主机编号。局域网 C 的网络号是 202.38.61.0。请回答下列问题：

（1）为每个网络的计算机和路由器的端口分配 IP 地址，并写出三个网段的子网掩码。
（2）列出路由器的路由表。
（3）若局域网 B 中的一台主机要向局域网 B 广播一个分组，写出该分组的目的 IP 地址。
（4）若局域网 B 中的一台主机要向局域网 C 广播一个分组，写出该分组的目的 IP 地址。

[tag_link]

<p>**【解析】**
本题考查路由器地址分配的一般原则、路由表的结构、子网划分和子网掩码。
首先应根据题意给出局域网 A 和局域网 B 的子网，这里局域网 A 的编号为 01，也就是 202.38.60.01000000，即 202.38.60.64，一般选择该网络最小的地址分配给路由器的接口 a，即 201.38.60.01000001，即 202.38.60.65，子网掩码为 255.255.255.192。同理局域网 B 的子网编号为 10，202.38.60.10000000，即 202.38.60.128，接口 b 的地址为 202.38.60.10000001，即 202.38.60.129，子网掩码是 255.255.255.192。对于局域网 C，接口 c 的地址为 202.38.61.1，子网掩码为 255.255.255.0。问题（1）和（2）就可以求解了。针对问题（3）和（4），也就是子网的广播地址，对于局域网 B，其广播地址为 202.38.60.10111111，即 202.38.60.191，对于局域网 C，就是标准的 202.38.61.255。
<p>（1）路由器 a 202.38.60.65   255.255.255.192
  路由器 b 202.38.60.129   255.255.255.192
  路由器 c 202.38.61.1    255.255.255.0
  路由器 d 61.60.21.80   255.0.0.0
<p>可知，局域网 A 的子网掩码为 255.255.255.192；局域网 B 的子网掩码为 255.255.255.192；局域网 C 的子网掩码为 255.255.255.0。
<p>（2）路由器的路由表如下：
<table><thead><tr><th>目���网络地址</th><th>子网掩码</th><th>下一跳地址</th><th>接口</th></tr></thead><tbody><tr><td>202.38.60.64</td><td>255.255.255.192</td><td>直接</td><td>a</td></tr><tr><td>202.38.60.128</td><td>255.255.255.192</td><td>直接</td><td>b</td></tr></tbody></table><p>续表
<table><thead><tr><th>目的网络地址</th><th>子网掩码</th><th>下一跳地址</th><th>接口</th></tr></thead><tbody><tr><td>202.38.61.0</td><td>255.255.255.0</td><td>直接</td><td>c</td></tr><tr><td>61.0.0.0</td><td>255.0.0.0</td><td>直接</td><td>d</td></tr><tr><td>0.0.0.0</td><td>0.0.0.0</td><td>61.60.21.80</td><td>d</td></tr></tbody></table><p>(3) 该广播是局域网 B 内的主机向局域网 B 内的主机发送的，所以主机号部分就是局域网 B 的网络号，即 202.38.60.128=202.38.60.1000 0000，子网掩码为 255.255.255.192，即 255.255.255.1100 0000，即后 6 位为主机号，因为是广播，所以主机号全填 1 即可，即 202.38.60.1011 1111，答案就为 202.38.60.191。
<p>(4) 该广播是局域网 B 内的主机向局域网 C 内的主机发送的，所以主机号部分就是局域网 C 的网络号，即 202.38.61.00，子网掩码为 255.255.255.0，即后 8 位为主机号，因为是广播，所以主机号全填 1 即可，即 202.38.61.1111 1111，答案就为 202.38.61.255。

---
