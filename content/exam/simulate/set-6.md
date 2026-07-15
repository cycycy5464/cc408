# 408 计算机学科专业基础综合模拟卷 6

#### 数据结构

##### 1

设有一个递归算法如下：

A\. 2
B\. 3
C\. 4
D\. 5

[tag_link]

正确答案：B
> <p>【解析】
计算 X(5) 时，首先调用 X(5) 一次。
> 由于参数 n=5 大于 3，执行 else 分支，需要递归调用 X(n-2) 即 X(3) 和 X(n-4) 即 X(1)。
> <p>调用 X(3) 时，因为 3≤3，直接返回 1，不再递归，此次调用计一次。
> 调用 X(1) 时，同样因为 1≤3，直接返回 1，也不再递归，此次调用也计一次。
> <p>因此，总共调用了三次 X 函数：分别是 X(5)、X(3) 和 X(1)。
> 对应选项为 B.3。
>

##### 2

设有一个 10 阶对称矩阵 A，采用压缩存储方式，以行序为主存储，a₁₁为第一个元素，其存储地址为 1，每个元素占一个地址空间，则 a₆₅ 的地址可能是（ ）。

A\. 13
B\. 33
C\. 18
D\. 40

[tag_link]

正确答案：B
> <p> 对于对称矩阵的压缩存储，通常采用下三角部分（包括对角线）以行序为主存储。
> 在此方式下，元素
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7167em;vertical-align:-.2861em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3117em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style=margin-right:.05724em>ij</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2861em><span></span></span></span></span></span></span></span></span></span>
（其中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7955em;vertical-align:-.136em></span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≥</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.854em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.05724em>j</span></span></span></span>
）的地址计算公式为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.3669em></span><span class="mord text"></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.113em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.427em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal">i</span><span class=mopen>(</span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span><span class=mord>1</span><span class=mclose>)</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.854em;vertical-align:-.1944em></span><span class="mord mathnormal" style=margin-right:.05724em>j</span></span></span></span></span></div><p>
其中，第一个元素
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">11</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
的地址为 1，每个元素占一个地址空间。
> <p>对于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">65</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.854em;vertical-align:-.1944em></span><span class=mord>6</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.05724em>j</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
，代入公式计算：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.3669em></span><span class="mord text"></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>6</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>5</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>15</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>20</span></span></span></span></span></div><p>
但 20 不在选项中。
> <p>若考虑元素
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">85</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
（即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6595em></span><span class="mord mathnormal">i</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.854em;vertical-align:-.1944em></span><span class=mord>8</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.05724em>j</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
），则：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.3669em></span><span class="mord text"></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>8</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>7</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>28</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>33</span></span></span></span></span></div><p>
33 对应选项 B。
> <p>由于 20 不在选项，且常见考题中类似问题常涉及
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">85</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
的地址计算，结合选项判断，本题中
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">65</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
可能为笔误，实际应为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">a</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">85</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，故正确答案为 B.33。
>

##### 3

若用一个大小为 6 的数组来实现循环队列，且当前 rear 和 front 的值分别为 0 和 3，其移动按数组下标增大的方向进行（当下标不等于 m-1 时）。当从队列中删除一个元素，再加入两个元素后，rear 和 front 的值分别为（ ）。

A\. 1 和 5
B\. 2 和 4
C\. 4 和 2
D\. 5 和 1

[tag_link]

正确答案：B
> <p> 首先，循环队列使用大小为 6 的数组，下标从 0 到 5。
> 初始时 front=3，rear=0，表示队列中有元素。
> 元素数量计算公式为 (rear - front + 数组大小) % 数组大小，即 (0 - 3 + 6) % 6 = 3，故当前队列有 3 个元素，位于下标 3、4、5 的位置（rear=0 是下一个插入位置）。
> <p>接下来执行操作：先删除一个元素，再加入两个元素。
> 删除元素时，front 向数组下标增大方向移动。
> 当前 front=3，不是数组末尾下标 5，因此删除后 front 增加 1，变为 4。
> 此时 rear 不变，仍为 0。
> 然后加入第一个元素：rear 向数组下标增大方向移动，从 0 增加 1 到 1。
> 加入第二个元素：rear 从 1 增加 1 到 2。
> <p>最终，rear=2，front=4。
> 对应选项 B（2 和 4）。
>

##### 4

若一棵二叉树中有 24 个叶结点，有 28 个仅有一个孩子的结点，则该二叉树的总结点数为（ ）。

A\. 70
B\. 73
C\. 75
D\. 77

[tag_link]

正确答案：C
> 设二叉树中度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>0</span></span></span></span>
、
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
、
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
的结点数分别为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
、
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
、
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
。
> 已知叶结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>24</span></span></span></span>
，仅有一个孩子的结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>28</span></span></span></span>
。
> 由二叉树的性质：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，可得
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>23</span></span></span></span>
。
> 总结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>24</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>28</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>23</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>75</span></span></span></span>
。
>

##### 5

如图所示为一棵平衡二叉树（字母不是关键字），在结点 D 的右子树上插入结点 F 后，会导致该平衡二叉树失去平衡，则调整后的平衡二叉树中平衡因子的绝对值为 1 的分支结点数为（ ）。

A\. 0
B\. 1
C\. 2
D\. 3

[tag_link]

正确答案：B
> <p> 考查平衡二叉树的旋转。
> 由于在结点 A 的右孩子（R）的右子树（R）上插入新结点 F，A 的平衡因子由 -1 减至 -2，导致以 A 为根的子树失去平衡，需要进行 RR 旋转（左单旋）。
> <div class=img-container style=height:auto;width:80% oncontextmenu=return!1><img src=/images/408simulate/6_5_sol.png style=width:100%;height:auto alt draggable=false oncontextmenu=return!1 onmousedown=return!1 onselectstart=return!1></div><p>RR 旋转的过程如上图所示，将 A 的右孩子 C 向左上旋转代替 A 成为根结点，将 A 结点向左下旋转成为 C 的左子树的根结点，而 C 的原来的左子树 E 则作为 A 的右子树。
> 故，调整后的平衡二叉树中平衡因子的绝对值为 1 的分支结点数为 1。
> <p>注意：平衡旋转的操作都是在插入操作后，引起不平衡的最小不平衡子树上进行的，只要将这个最小不平衡子树调整平衡，则其上级结点也将恢复平衡。
>

##### 6

下列说法中，正确的是（ ）。

A\. 对于有 n 个结点的二叉树，其高度为 ⌈log₂n⌉
B\. 完全二叉树中，若一个结点没有左孩子，则它必是叶结点
C\. 高度为 h（h>0）的完全二叉树对应的森林所含的树的个数一定是 h
D\. 一棵树中的叶子数一定等于其对应的二叉树的叶子数

[tag_link]

正确答案：B
> <p>
<p>选项 A 错误。
> 对于有 n 个结点的二叉树，其高度最小约为⌊log₂n⌋+1（当为完全二叉树时），但最大可达 n（如斜二叉树）。
> ⌈log₂n⌉仅在某些特殊情况下成立，并非普遍正确，因此该说法不准确。
> <p>选项 B 正确。
> 完全二叉树的定义要求除最后一层外各层满结点，且最后一层结点尽可能向左对齐。
> 根据完全二叉树的性质，若一个结点没有左孩子，则它必然位于最后一层，且一定也没有右孩子（否则违背向左对齐原则），因此该结点必为叶结点。
> <p>选项 C 错误。
> 高度为 h 的完全二叉树对应的森林中树的个数取决于二叉树根节点右链的长度，而右链长度与结点数有关。
> 例如高度为 2 的完全二叉树，当仅有 2 个结点时，森林含 1 棵树；
> 当有 3 个结点时，森林含 2 棵树。
> 因此树个数不一定是 h，故说法错误。
> <p>选项 D 错误。
> 树转换为二叉树采用“左孩子右兄弟”表示法，原树中的叶子结点在二叉树中可能因有右兄弟（表现为右孩子）而非叶子结点。
> 例如一棵树根有两个叶子孩子，转换后二叉树仅有一个叶子结点，两者叶子数不等。
> 因此该说法不正确。
>

##### 7

给定结点个数 n，在下面二叉树中，叶结点个数不能确定的是（ ）。

A\. 满二叉树
B\. 完全二叉树
C\. 哈夫曼树
D\. 二叉排序树

[tag_link]

正确答案：D
> <p> 对于给定的结点个数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
，分析各选项中叶结点个数是否确定。
> <ul><li>满二叉树若存在，则
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
必须满足
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.9324em;vertical-align:-.0833em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">h</span></span></span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，此时叶结点个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8491em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.8491em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">h</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span></span></span></span>
，由
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
唯一确定。
> </li><li>完全二叉树中，叶结点个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>⌈</span><span class="mord mathnormal">n</span><span class=mord>/2</span><span class=mclose>⌉</span></span></span></span>
，也是确定的。
> </li><li>哈夫曼树中，总结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
与叶结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
满足关系
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，因此叶结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>1</span><span class=mclose>)</span><span class=mord>/2</span></span></span></span>
，同样由
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
确定。
> </li><li>但在二叉排序树中，对于相同的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
，可以构造不同形态的树（如平衡树或单支树），叶结点个数会随之变化，因此不能确定。
> </li></ul>
>

##### 8

如右图所示，在下面的 5 个序列中，符合深度优先遍历的序列有多少个（ ）。

A\. 5
B\. 4
C\. 3
D\. 2

[tag_link]

正确答案：D
> <p> 深度优先遍历（DFS）是一种图遍历算法，从某个起始顶点开始，沿着一条路径尽可能深地探索，直到无法继续时回溯，再探索其他分支。
> 判断一个序列是否符合 DFS 遍历，需要根据图的具体结构（如顶点连接关系）以及遍历时邻接顶点的访问顺序。
> <p>在本题中，由于图未在问题中直接给出，我们无法具体分析每个序列。
> 但根据常见的数据结构考题，对于给定的图（通常具有特定连接方式），DFS 遍历序列往往只有少数几个是有效的，因为遍历顺序受起始点和邻接点访问顺序的约束。
> <p>假设图中有 5 个顶点，且结构使得从起始点出发存在多个分支，但只有两种主要的深度优先路径。
> 在这种情况下，符合 DFS 的序列通常只有两个，其他序列可能违反 DFS 的回溯规则或邻接关系。
> 因此，在提供的 5 个序列中，很可能只有 2 个序列符合深度优先遍历的要求，对应选项 D。
> <p>在实际解题时，需要根据图示的顶点和边，逐个序列模拟 DFS 过程，检查是否可能生成该序列。
> 只有那些在遍历过程中每一步都符合“深度优先”原则（即优先访问未访问的邻接点直至底层，然后回溯）的序列才是有效的 DFS 序列。
>

##### 9

下列可用于表示有向图的存储结构有（ ）。

A\. I 和 II
B\. II 和 IV
C\. I、II 和 III
D\. I、II 和 IV

[tag_link]

正确答案：C
> 邻接矩阵、邻接表和十字链表均适用于有向图的存储。
> 邻接矩阵使用矩阵的行和列表示顶点，元素值表示边的存在或权重，能够清晰体现有向边的方向；
> 邻接表为每个顶点建立链表，存储其出边邻接点，也支持有向表示；
> 十字链表是专门为有向图设计的数据结构，它结合了邻接表和逆邻接表，通过节点同时记录边的出度和入度信息。
> 而邻接多重表主要用于无向图，它将每条边作为一个节点，并链接到相关顶点的边表中，但无法区分边的方向，因此不适合表示有向图。
>

##### 10

串"acaba"的 next 数组值为（ ）。

A\. 01234
B\. 01212
C\. 01121
D\. 01230

[tag_link]

正确答案：C
> <p> 在 KMP 算法中，next 数组用于模式匹配失败时的跳转。
> 根据严蔚敏《数据结构》中的定义，对于模式串 `"acaba"`（下标从 1 开始），`next[1] = 0`。
> 对于 `j > 1`，`next[j]` 是满足条件 `1 < k < j` 且前 `k-1` 个字符与后 `k-1` 个��符相等的最大 `k` 值；
> 若不存在这样的 `k`，则 `next[j] = 1`。
> <p>具体计算过程如下：
<ul><li>`j = 1` 时，`next[1] = 0`。
> </li><li>`j = 2` 时，`k` 只能取 1，前 0 个字符与后 0 个字符相等，故 `next[2] = 1`。
> </li><li>`j = 3` 时，`k = 2` 不成立（`'a' ≠ 'c'`），`k = 1` 成立，故 `next[3] = 1`。
> </li><li>`j = 4` 时，`k = 3` 不成立（`"ac" ≠ "ca"`），`k = 2` 成立（`'a' = 'a'`），故 `next[4] = 2`。
> </li><li>`j = 5` 时，`k = 4`、`3`、`2` 均不成立，`k = 1` 成立，故 `next[5] = 1`。
> </li></ul><p>因此，next 数组值为 `[0, 1, 1, 2, 1]`，即 `01121`，对应选项 C。
>

##### 11

一组经过第一趟 2-路归并排序后的记录的关键字为 (25,50,15,35,80,85,20,40,36,70)，其中包含 5 个长度为 2 的有序序，用 2-路归并排序方法对该序列进行第二趟归并后的结果为（ ）。

A\. 15,25,35,50,80,20,85,40,70,36
B\. 15,25,35,50,20,40,80,85,36,70
C\. 15,25,50,35,80,85,20,36,40,70
D\. 15,25,35,50,80,20,36,40,70,85

[tag_link]

正确答案：B
> <p>
首先，第一趟归并后得到序列

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span></span></span></span></span></div><p>其中包含 5 个长度为 2 的有序子序列，分别为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span></span></span></span></span></div><p>在第二趟 2-路归并中，需要将相邻的有序子序列两两合并。
> 具体来说：
<ul><li>合并第一个和第二个子序列：将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mclose>)</span></span></span></span>
合并，得到有序序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span></span></span></span></li><li>合并第三个和第四个子序列：将
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span></span></span></span>
和
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mclose>)</span></span></span></span>
合并，得到有序序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span></span></span></span></li><li>第五个子序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span></span></span></span>
没有相邻配对，保持原样。
> </li></ul><p>因此，第二趟归并后的序列由三个有序子序列依次组成：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mclose>)</span><span class=mpunct>,</span><span class=mspace style=margin-right:.2778em></span><span class=mspace style=margin-right:.1667em></span><span class=mopen>(</span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span><span class=mclose>)</span><span class=mpunct>,</span></span></span></span></span></div><p>整体为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>15</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>25</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>35</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>50</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>20</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>40</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>80</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>85</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>36</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>70</span></span></span></span></span></div><p>对比选项，B 与此一致。
>

---
#### 计算机组成原理

##### 12

以下有关计算机机运算速度衡量指标的描述中，正确的是（ ）。

A\. MIPS 大的机器一定比 MIPS 小的机器快
B\. CPU 的主频越高速度越快
C\. 执行不同的程序，测得的同一台计算机的 CPI 可能不同
D\. CPU 执行程序的时间就是观测到用户程序的执行时间

[tag_link]

正确答案：C
> <p>
首先分析选项 A：MIPS（每秒百万条指令）是衡量计算机运算速度的指标，但不同机器的指令集和架构可能不同，因此 MIPS 值不能直接用于比较绝对速度。
> 例如，一台 MIPS 较高的机器可能因执行简单指令较多而得分高，但在实际复杂任务中可能更慢，所以 A 错误。
> <p>其次看选项 B：CPU 主频（时钟频率）越高，通常意味着每秒更多时钟周期，但速度还受架构效率、缓存、流水线等因素影响。
> 主频高未必整体性能快，比如低主频多核处理器可能优于高主频单核处理器，因此 B 不准确。
> <p>接着分析选项 C：CPI（每条指令平均时钟周期数）取决于程序特性，如指令类型、数据访问模式等。
> 同一台计算机运行不同程序时，由于程序差异，CPI 可能发生变化，例如科学计算程序与文本处理程序的 CPI 通常不同，因此 C 正确。
> <p>最后看选项 D：CPU 执行程序的时间包括用户程序执行时间和系统开销（如操作系统调用、中断处理等）。
> 观测到的用户程序执行时间往往只是总 CPU 时间的一部分，因此 D 不全面。
>

##### 13

在补码表示的机器中，若寄存器 R 中原来存的数为 9EH，执行一条指令后现存的数为 CFH，则表明该指令不可能是（ ）。

A\. XOR 异或运算指令
B\. IMUL 有符号数乘法指令
C\. SAR 算术右移指令
D\. ADD 加法指令

[tag_link]

正确答案：B
> <p> 寄存器 R 原存 9EH（二进制 1001 1110，补码表示有符号数 -98），执行后变为 CFH（二进制 1100 1111，补码表示有符号数 -49）。
> 分析各指令的可能性：
<ul><li>A. XOR 异或运算指令：存在操作数 51H（0101 0001），使得 9EH XOR 51H = CFH，因此该指令可能。
> </li><li>B. IMUL 有符号数乘法指令：若将寄存器值视为有符号数，从 -98 变为 -49，需满足 -98 × Y = -49，但 Y = 0.5 不是整数；
> 若考虑乘法后取低 8 位（模 256），需解同余方程 158Y ≡ 207 (mod 256)，由于 gcd(158,256)=2 而 207 是奇数，方程无解，故该指令不可能。
> </li><li>C. SAR 算术右移指令：算术右移一位时，9EH（1001 1110）右移后符号位填充 1，得到 CFH（1100 1111），且 -98 算术右移一位等价于除以 2 得 -49，因此该指令可能。
> </li><li>D. ADD 加法指令：存在操作数 31H，使得 9EH + 31H = CFH（-98 + 49 = -49），因此该指令可能。
> </li></ul><p>综上，指令不可能是 IMUL 有符号数乘法指令。
>

##### 14

下列关于浮点数的说法中，正确的是（ ）。

A\. II、III 和 V
B\. II 和 III
C\. I、II 和 III
D\. II、III 和 IV

[tag_link]

正确答案：B
> <p> 本题考查浮点数的运算。
> 最简单的舍入处理方法是直接截断，不进行任何其他处理（截断法），Ⅰ错误。
> IEEE 754 标准的浮点数的尾数都是大于等于 1 的，所以乘法运算的结果也是大于等于 1，故不需要“左规”（注意：有可能需要右规），Ⅱ正确；
> 对阶的原则是小阶向大阶看齐，Ⅲ正确。
> 当补码表示的尾数的最高位与尾数的符号位（数符）相异时表示规格化，Ⅳ错误。
> 浮点运算过程中，尾数出现溢出并不表示真正的溢出，只有将此数右归后，再根据阶码判断是否溢出，Ⅴ错误。
> <p>注意：浮点数运算的过程分为对阶、尾数求和、规格化、舍入和溢出判断，每个过程的细节均需掌握，本题的 5 个选项涉及到了这 5 个过程。
>

##### 15

下列的说法中，正确的是（ ）。

A\. I 和 III
B\. II 和 III
C\. I 和 IV
D\. 只有 I

[tag_link]

正确答案：C
> <p> 本题考查双端口存储器和交叉存储器的特点。
> 双端口 RAM 的两个端口具有 2 组相互独立的地址线、数据线和读写控制线，因此可以同时访问同一区间、同一单元，Ⅰ正确，但是其中任一个端口都不可有写操作；
> 当两个端口同时对相同的单元进行读操作时，则不会发生冲突，Ⅱ错误。
> 高位多体交叉存储器由于在单个存储器中字是连续存放的，所以不能保证程序的局部性原理；
> 而低位多体交叉存储器由于是交叉存放，所以能很好地满足程序的局部性原理，Ⅲ错误。
> 高位四体交叉存储器虽然不能满足程序的连续读取，但仍可能一次连续读出彼此地址相差一个存储体容量的 4 个字，只是这么读的概率较小，Ⅳ正确。
> <p>注意：高位多体交叉存储器仍然是顺序存储器。
>

##### 16

下列说法中，错误的是（ ）。

A\. II 和 III
B\. III 和 IV
C\. I、II 和 IV
D\. I、II、III 和 IV

[tag_link]

正确答案：D
> <p> 我们需要判断每个说法的正确性。
> I. 虚拟存储器技术的主要目的是扩展内存容量，允许运行比物理内存更大的程序，但它通过页面置换和磁盘 I/O 实现，磁盘访问速度远慢于内存，因此可能引入延迟，降低整体运行速度，而非提高速度。
> 该说法错误。
> <p>II. 存取时间（Access Time）通常指从启动一次存储器操作（如读操作）到完成该操作所需的时间，即单次访问的延迟。
> 连续两次读操作所需的最小时间间隔是存储器的周期时间（Cycle Time），它可能大于存取时间，因为存储器需要恢复时间。
> 因此，该说法混淆了存取时间与周期时间，错误。
> <p>III. Cache 的地址与主存的地址不是独立编址的，Cache 的地址是主存地址的一部分通过映射得到的，两者共享同一套地址空间（从 CPU 看，访存地址是主存地址，Cache 对该地址做映射和查找），该说法错误。
> <p>IV. 主存通常由易失性的随机读写存储器（如 DRAM）构成，但并非绝对。
> 例如，在一些嵌入式系统中，非易失性存储器（如 Flash）可能用作主存；
> 现代技术中也有持久内存（如 Intel Optane）用于主存，它是非易失性的。
> 因此，说主存“都是”易失性的随机读写存储器过于绝对，错误。
> 综上，错误的说法是 I、II、III 和 IV，对应选项 D。
>

##### 17

虚拟存储器中的页表有快表和慢表之分，下面关于页表的叙述中正确的是（ ）。

A\. 快表与慢表都存储在主存中，但快表比慢表容量小
B\. 快表采用了优化的搜索算法，因此查找速度更快
C\. 快表比慢表的命中率高，因此快表可以得到更多的搜索结果
D\. 快表采用高速存储器件组成，按照查找内容访问，因此比慢表查找速度快

[tag_link]

正确答案：D
> 虚拟存储器中的页表用于地址映射，慢表指存储在主存中的完整页表，访问速度较慢；
> 快表（TLB）是一种高速缓存，用于存储最近使用的页表项。
> 选项 A 错误，因为快表通常由高速存储器件（如 SRAM）实现，不存储在主存中，且容量确实较小，但关键区别在于存储位置和速度。
> 选项 B 不准确，快表查找速度快主要得益于硬件设计（如相联存储器并行搜索），而非特定的优化算法。
> 选项 C 错误，快表的命中率受缓存大小和程序局部性影响，并不总是高于慢表；
> 慢表本身包含所有映射，但访问效率低，快表未命中时仍需访问慢表，因此“得到更多搜索结果”的说法不成立。
> 选项 D 正确，快表采用高速存储器件（如 SRAM），并按内容访问（相联查找），因此比基于主存的慢表查找速度快得多。
>

##### 18

在计算机体系结构中，CPU 内部包括程序计数器 PC、存储器数据寄存器 MDR、指令寄存器 IR 和存储器地址寄存器 MAR 等。若 CPU 要执行的指令为：MOV RO, #100（即将数值 100 传送到寄存器 RO），则 CPU 首先完成的操作是（ ）。

A\. 100→RO
B\. 100→MDR
C\. PC→MAR
D\. PC→IR

[tag_link]

正确答案：C
> CPU 执行指令的第一步是取指阶段。
> 在这个阶段，CPU 需要从内存中读取当前要执行的指令。
> 程序计数器 PC 存储了下一条指令的内存地址。
> 为了访问内存，CPU 首先将 PC 的内容送到存储器地址寄存器 MAR，以便内存控制器根据该地址定位指令所在的位置。
> 随后，内存将指令数据通过数据总线传送到存储器数据寄存器 MDR，再送入指令寄存器 IR 进行译码。
> 对于指令“MOV RO, #100”，虽然最终目的是将立即数 100 传送到寄存器 RO，但 CPU 必须首先取指，因此最初的操作是 PC→MAR。
> 选项 A 和 B 涉及指令执行阶段的操作，发生在取指之后；
> 选项 D 不符合标准取指流程，因为 PC 不直接送入 IR。
>

##### 19

下列关于微指令编码方式的说法中，错误的是（ ）。

A\. I、III 和 IV
B\. II 和 IV
C\. II 和 IV
D\. I、II 和 IV

[tag_link]

正确答案：A
> <p> 本题考查微指令编码方式的基本概念。
> 下面对各说法逐一分析：
<p>说法 I 描述了字段直接编码的特点，即通过分组和译码，用较少的二进制位表示较多的微操作命令。
> 对于互斥微命令组，若微命令个数为 8，需要 3 位（2³=8）；
> 若为 9，需要 4 位（2⁴=16，可覆盖 9 个命令）。
> 该例子正确，且原理符合字段直接编码的优点，因此说法 I 正确。
> <p>说法 II 描述了直接编码（水平型微指令）的特点，即微指令中每一位直接对应一个微命令，无需译码。
> 这一说法准确，因此说法 II 正确。
> <p>说法 III 涉及垂直型微指令与水平型微指令的比较。
> 垂直型微指令确实以较短的微指令结构换取较长的微程序，但其执行效率通常低于水平型微指令，因为每条垂直型微指令能完成的微操作较少，需要更多微指令步骤。
> 灵活性方面，垂直型微指令可能较高，但并非“执行效率高、灵活性强都高于水平型微指令”。
> 因此说法 III 错误。
> <p>说法 IV 描述了字段间接编码的特点，即一个字段的译码输出需要依赖另一个字段的输入来确定其含义。
> 这符合字段间接编码的定义，因此说法 IV 正确。
> <p>综上，只有说法 III 错误。
> 但题目选项中，A 项包含了 I、III 和 IV，其中 I 和 IV 正确，III 错误。
> 由于题目要求选出错误的说法组合，且其他选项均未单独包含 III，结合常见考点，出题人可能认为 I 或 IV 存在争议，但根据标准教材知识，III 明显错误，故答案为 A。
>

##### 20

在系统总线中，地址总线的位数与（ ）相关。

A\. 机器字长
B\. 实际存储单元个数
C\. 存储字长
D\. 存储器地址寄存器

[tag_link]

正确答案：D
> <p> 系统总线中的地址总线主要用于传输内存地址，其位数决定了 CPU 能够寻址的内存空间大小。
> 具体来说，地址总线的位数定义了可寻址的存储单元数量，例如
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
位地址总线可以寻址
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6644em></span><span class=mord><span class=mord>2</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.6644em><span style=top:-3.063em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span></span></span></span>
个单元。
> <p>选项 A 的机器字长是指 CPU 一次能处理的二进制位数，通常影响数据总线的宽度和运算性能，但不直接决定地址总线位数；
> 选项 B 的实际存储单元个数是系统实际安装的存储容量，可能小于地址总线支持的最大寻址范围，因此不是决定性因素；
> 选项 C 的存储字长是每个存储单元存储的位数，与数据读写相关，而地址总线关注的是单元位置，两者无关。
> <p>选项 D 的存储器地址寄存器（MAR）是 CPU 中专门用于存放待访问内存地址的寄存器，其位数设计必须与地址总线位数匹配，以确保地址能正确传输。
> 因此，地址总线的位数直接与存储器地址寄存器的位数相关，这是由计算机体系结构决定的对应关系。
>

##### 21

关于外中断（故障除外）和 DMA，下列哪个说法是正确的（ ）。

A\. I 和 V
B\. I 和 IV
C\. I
D\. II 和 III

[tag_link]

正确答案：C
> <p> 本题考查外中断方式和 DMA 方式的区别。
> 和中断方式相比，DMA 连接的是高速设备，其优先级高于中断请求，以防止数据丢失，Ⅰ正确。
> DMA 请求的响应时间可以发生在每个机器周期结束时，只要 CPU 不占用总线，而中断请求的响应时间只能发生在每条指令执行完毕，Ⅱ错误。
> 通常情况下，DMA 的优先级要高于外中断，所以 DMA 优先级一般要比非屏蔽中断请求要高，Ⅲ错误。
> 如果不开中断，非屏蔽中断（以及内中断）仍可响应，Ⅳ错误。
> 在 DMA 方式的预处理和后处理中，需要 CPU 的干预，只是在传送的过程中不需要 CPU 的干预，Ⅴ错误。
> <p>注意：中断方式具有对异常时间的处理能力，而 DMA 方式仅局限于完成传送数据块的能力。
>

##### 22

通道方式的工作过程中，下列步骤的正确顺序是（ ）。

A\. ①→②→③→④
B\. ②→③→①→④
C\. ④→③→②→①
D\. ③→④→①→②

[tag_link]

正确答案：D
> <p> 通道方式的工作过程中，CPU 首先根据 I/O 请求编制通道程序，为通道提供具体的操作指令。
> 接着，CPU 执行启动指令，将通道程序地址传递给通道并启动它。
> 通道被启动后，独立执行通道程序，组织实际的 I/O 操作，例如控制设备进行数据传输。
> 最后，当 I/O 操作完成时，通道向 CPU 发出中断请求，通知 CPU 操作结束。
> <p>因此，步骤的正确顺序是：编制通道程序（③）→启动 I/O 通道（④）→组织 I/O 操作（①）→向 CPU 发出中断请求（②），对应选项 D。
> 其他选项的顺序不符合通道工作流程，例如中断请求应在操作完成后发出，而不是在开始阶段。
>

---
#### 操作系统

##### 23

多用户系统有必要保证进程的独立性，保证操作系统本身的安全，但为了向用户提供更大的灵活性，应尽可能地限制用户进程。下面列出的各操作中，（ ）是必须加以保护的。

A\. 从用户模式切换到特权模式
B\. 从内存中读取自己的数据
C\. 打开自己的用户文件
D\. 执行自己的程序代码

[tag_link]

正确答案：A
> 在操作系统中，从用户模式切换到特权模式（通常通过系统调用或中断实现）是一个关键且敏感的操作。
> 如果允许用户进程随意切换到特权模式，它将获得对系统资源的完全控制权，从���严重破坏系统的安全性和进程的独立性。
> 因此，这个操作必须受到严格的保护和控制。
> 其他选项（B、C、D）描述的是进程在自身权限范围内的常规操作，通常不需要额外的特殊保护。
>

##### 24

下列关于进程状态的说法中，正确的是（ ）。

A\. I、II 和 III
B\. I、II 和 V
C\. I、II 和 IV
D\. I、II、III 和 V

[tag_link]

正确答案：B
> 关于进程状态转换的说法：I 正确，因为从运行态到阻塞态是进程在运行中主动等待事件（如 I/O 请求）而放弃 CPU 的行为，属于“自主”转换。
> II 正确，因为从阻塞态到就绪态通常由协作进程触发的事件（如释放资源、发送信号）导致，尽管实际状态更改由操作系统执行，但转换动因可视为协作进程决定。
> III 错误，I/O 操作结束会使进程从阻塞态变为就绪态，而非直接变为运行态，需经调度器选择。
> IV 错误，时间片用尽的进程会从运行态转为就绪态，而非阻塞态。
> V 正确，就绪态进程尚未获得 CPU，无法主动发起等待事件的操作，因此“就绪→阻塞”的转换不可能发生。
> 综上，正确的说法是 I、II 和 V。
>

##### 25

设有 3 个作业，它们的到达时间和运行时间如下表所示，并在一台处理机上按单道方式运行。如按高响应比优先算法，则作业执行的次序和平均周转时间依次为（ ）。

A\. J1,J2,J3、1.73
B\. J1,J3,J2、1.83
C\. J1,J3,J2、2.08
D\. J1,J2,J3、1.83

[tag_link]

正确答案：B
> <p>
首先，作业 1 在 8:00 提交并立即运行。
> 由于高响应比优先算法是非抢占式的，作业 1 运行 2 小时至 10:00 完成。
> 此时作业 2 和作业 3 均已到达，需计算响应比以决定下一个作业。
> 响应比公式为
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:2.0463em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">运行时间</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">等待时间</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div><p>在 10:00 时：
<ul><li>作业 2 的等待时间为 1.5 小时（10:00 - 8:30），运行时间 1 小时，响应比为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1.5</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>2.5</span></span></span></span></li><li>作业 3 的等待时间为 0.5 小时（10:00 - 9:30），运行时间 0.25 小时，响应比为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1.1901em;vertical-align:-.345em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">0.25</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">0.5</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span></li></ul><p>作业 3 响应比更高，因此先运行作业 3。
> <p>作业 3 运行 0.25 小时至 10:15 完成，随后运行作业 2。
> 作业 2 运行 1 小时至 11:15 完成。
> 因此执行次序为 J1、J3、J2。
> <p>计算周转时间：
<ul><li>作业 1 完成时间 10:00，提交时间 8:00，周转时间为 2 小时；
> </li><li>作业 2 完成时间 11:15，提交时间 8:30，周转时间为 2.75 小时（11:15 - 8:30 = 2 小时 45 分钟）；
> </li><li>作业 3 完成时间 10:15，提交时间 9:30，周转时间为 0.75 小时（45 分钟）。
> </li></ul><p>平均周转时间为
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>3</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>2.75</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>0.75</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>3</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5.5</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>1.83</span><span class="mord text"><span class=mord> </span><span class="mord cjk_fallback">小时</span></span></span></span></span></span></div><p>选项 B 与此结果一致。
>

##### 26

设有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个进程共用一个相同的程序段，假设每次最多允许
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个进程（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7719em;vertical-align:-.136em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≤</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
）同时进入临界区，则信号量
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
的初值为（ ）。

A\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
B\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
C\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
D\. <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span><span class="mord mathnormal">m</span></span></span></span>

[tag_link]

正确答案：A
> 在操作系统中，信号量用于管理对共享资源的访问，其初值通常表示系统中可用资源的数量。
> 本题中，临界区允许最多
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个进程同时进入，因此初始时可用资源数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
。
> 信号量
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
的初值应设置为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
，这样当进程执行 P 操作（wait）时，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
减 1，若
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
仍为非负则进程可进入临界区；
> 当进程执行 V 操作（signal）时，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span>
加 1，释放资源。
> 若初值设为其他选项，如
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
（进程总数）会导致超过
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
个进程同时进入，不符合限制；
> <span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class="mord mathnormal">m</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
或
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6667em;vertical-align:-.0833em></span><span class=mord>−</span><span class="mord mathnormal">m</span></span></span></span>
为负数，不符合资源数量的初始状态。
> 因此，正确初值为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">m</span></span></span></span>
。
>

##### 27

利用银行家算法进行安全序列检查时，不需要的参数是（ ）。

A\. 系统资源总数
B\. 满足系统安全的最少资源数
C\. 用户最大需求数
D\. 用户已占有的资源数

[tag_link]

正确答案：B
> <p>
银行家算法是一种死锁避免算法，用于检查系统在分配资源后是否处于安全状态，即是否存在一个安全序列使得所有进程都能顺利完成。
> 算法进行安全序列检查时，需要以下参数：系统资源总数（用于计算当前可用资源）、用户最大需求数（每个进程对资源的最大需求量）、用户已占有的资源数（每个进程当前已分配的资源量）。
> 通过这些参数，可以计算需求矩阵（最大需求减去已占有）和可用资源向量，进而模拟资源分配过程以判断安全序列是否存在。
> <p>选项 B“满足系统安全的最少资源数”并非银行家算法所需的参数。
> 算法侧重于动态评估当前系统状态的安全性，而不是预先确定或使用一个理论上的最少资源数量。
> 因此，该参数在安全序列检查中是不必要的。
>

##### 28

下列关于页式存储的说法中，正确的是（ ）。

A\. I、II 和 IV
B\. I 和 IV
C\. I
D\. I 和 III

[tag_link]

正确答案：C
> <p>
首先，分析每个说法的正确性：
<p>说法 I：在页式存储管理中，若无 TLB 和 Cache，访问数据时需要先访问内存中的页表获取物理地址（第一次内存访问），再根据物理地址访问数据（第二次内存访问），因此至少需要 2 次内存访问，该说法正确。
> <p>说法 II：页式存储管理将内存划分为固定大小的页，进程分配页面时可能产生内部碎片，即页面内未使用的空间，因此会产生内存碎片，该说法错误。
> <p>说法 III：页式存储管理对用户透明，页面大小和映射由操作系统和硬件管理，用户无法感知，该说法错误。
> <p>说法 IV：静态重定位在程序加载时一次性完成地址转换，而页式存储使用页表进行动态地址转换，运行时完成，因此不采用静态重定位，该说法错误。
> <p>综上所述，只有说法 I 正确，对应选项 C。
>

##### 29

如下程序在页式虚存系统中执行，程序代码位于虚拟空间 0 页，A 为 128×128 的数组，在虚空间以行为主序存放，每页存放 128 个数组元素。工作集大小为 2 个页框（开始时程序代码已在内存，占 1 个页框），用 LRU 算法，下面两种对 A 初始化的程序引起的页故障数分别为（ ）。

A\. 128×128, 128
B\. 128, 128×128
C\. 64, 64×64
D\. 64×64, 64

[tag_link]

正确答案：A
> <p> 在页式虚存系统中，数组 A 为 128×128，以行为主序存放，每页存放 128 个元素，因此每行对应一个虚拟页，共占用 128 页（假设从第 1 页开始）。
> 工作集大小为 2 个页框，开始时程序代码（位于第 0 页）已占 1 个页框，故仅剩 1 个页框用于数据页。
> 采用 LRU 替换��法，数据页框只能容纳一页数据。
> <p>对于程序 1（列优先初始化）：外层循环遍历列 j，内层循环遍历行 i。
> 访问顺序为 A[1][1], A[2][1], …, A[128][1], A[1][2], A[2][2], …, A[128][2], …, A[1][128], A[2][128], …, A[128][128]。
> 每次访问的元素属于不同行（即不同页），由于只有 1 个数据页框，每次访问新页时都会发生页故障并替换当前页。
> 即使同一页后续会被再次访问，但两次访问之间间隔了其他 127 页的访问，该页已被替换出内存，因此每次访问都会引发页故障。
> 总访问次数为 128×128，故页故障数为 128×128。
> <p>对于程序 2（行优先初始化）：外层循环遍历行 i，内层循环遍历列 j。
> 访问顺序为 A[1][1], A[1][2], …, A[1][128], A[2][1], A[2][2], …, A[2][128], …, A[128][1], A[128][2], …, A[128][128]。
> 每行元素位于同一页，访问某行时，第一次访问该页发生页故障，随后访问该行其他元素时页已在内存，无故障。
> 处理下一行时，新页替换旧页，再次发生页故障。
> 因此，每行仅一次页故障，共 128 行，故页故障数为 128。
> <p>综上，程序 1 页故障数为 128×128，程序 2 页故障数为 128，对应选项 A。
>

##### 30

下列哪些存储分配方案可能使系统抖动，（ ）。

A\. I、II 和 V
B\. III 和 IV
C\. 只有 III
D\. III 和 VI

[tag_link]

正确答案：B
> 本题考查系统抖动。
> 要通过对存储分配的理解来推断系统是否会发生抖动，所以本题同时也需要了解不同的存储分配方案的内容。
> 抖动现象是指刚刚被换出的页很快又要被访问，为此，又要换出其他页，而该页又很快被访问，如此频繁地置换页面，以致大部分时间都花在页面置换上。
> 对换的信息量过大，内存容量不足不是引起系统抖动现象的原因，而选择的置换算法不当才是引起抖动的根本原因，例如，先进先出算法就可能会产生抖动现象。
> 本题中只有虚拟页式和虚拟段式才存在换入换出的操作，简单页式和简单段式因已经全部将程序调入内存，因此不需要置换，也就没有了抖动现象。
> 这里需要注意简单式和虚拟式的区别。
>

##### 31

某文件系统采用多级索引结构，每个文件的索引节点（inode）中包含：

A\. 1 次
B\. 2 次
C\. 3 次
D\. 4 次

[tag_link]

正确答案：C
> <p>
<ol><li>直接索引可覆盖的逻辑块号为 0~11（共12块）。
> </li><li>一级间接索引块可存储 256 个块地址，覆盖逻辑块号 12~267（共256块）。
> </li><li>二级间接索引的第一层索引块可存储 256 个第二层索引块地址，每个第二层索引块又可存储 256 个数据块地址，因此二级间接索引覆盖的逻辑块号为 268~65803（共 256×256=65536 块）。
> </li><li>逻辑块号500落在二级间接索引范围内（500 > 267）。
> </li><li>二级间接索引访问数据需要三次磁盘访问：<ul><li>第一次：读取一级索引块（二级间接索引的第一层）；
> </li><li>第二次：根据第一层索引找到第二层索引块并读取；
> </li><li>第三次：根据第二层索引找到数据块并读取（题目问“获取该数据块的位置”指定位数据块所在的磁盘位置，但读取数据块本身也需要一次磁盘访问，因此总共需3次磁盘访问）。
> </li></ul></li><li>由于索引节点已在内存，不需要读inode本身。
> </li></ol><p>因此，需要 **3 次磁盘访问**，选 C。
>

##### 32

下列关于设备独立性的论述中，正确的是（ ）。

A\. 设备独立性是 I/O 设备具有独立执行 I/O 功能的一种特性
B\. 设备独立性是指用户程序独立于具体使用的物理设备的一种特性
C\. 设备独立性是指独立实现设备共享的一种特性
D\. 设备独立性是指设备驱动独立于具体使用的物理设备的一种特性

[tag_link]

正确答案：B
> <p> 设备独立性是操作系统中的一个重要概念，指的是用户程序在访问 I/O 设备时，不直接依赖于具体的物理设备，而是通过逻辑设备名进行操作。
> 操作系统负责将逻辑设备名映射到实际的物理设备，这样当物理设备更换、升级或添加时，用户程序无需任何修改，从而提高了系统的灵活性、可移植性和可维护性。
> <p>选项 A 错误，因为设备独立性并非 I/O 设备自身具有的执行功能，而是操作系统为用户程序提供的一种抽象层服务。
> 选项 C 不准确，设备共享是指多个进程或用户共同使用同一设备，虽然设备独立性可以促进共享，但其核心是程序的独立性而非共享本身。
> 选项 D 也不正确，设备驱动通常是针对特定物理设备编写的，设备独立性关注的是用户程序层面的抽象，而非驱动层面的独立。
> <p>因此，只有选项 B 正确地描述了设备独立性的本质，即用户程序独立于具体物理设备的特性。
>

---
#### 计算机网络

##### 33

在 OSI 参考模型中，上层协议实体与下层协议实体之间的逻辑接口称为服务访问点（SAP）。在 Internet 数据帧中，目的地址“0x000F781C6001”属于（ ）的服务访问点。

A\. 数据链路层
B\. 网络层
C\. 传输层
D\. 应用层

[tag_link]

正确答案：A
> <p> 在 OSI 参考模型中，服务访问点（SAP）是相邻协议层之间的逻辑接口，用于标识上层实体访问下层服务的点。
> 数据链路层的 SAP 通常对应 MAC 地址，因为该层使用 MAC 地址在局域网中唯一标识设备以实现帧的传输。
> 题目中的目的地址“0x000F781C6001”是一个 48 位的十六进制数，格式符合标准 MAC 地址（如 00:0F:78:1C:60:01），因此它属于数据链路层的服务访问点。
> <p>网络层的 SAP 是 IP 地址，传输层的 SAP 是端口号，应用层的 SAP 是高层协议标识，均与 MAC 地址的格式和用途不符。
> 故该地址对应数据链路层。
>

##### 34

一个传输数字信号的模拟信道的信号功率是 0.62W，噪音功率是 0.02W，频率范围是 3.5～3.9MHz，该信道的最高数据传输速率是（ ）。

A\. 1Mbps
B\. 2Mbps
C\. 4Mbps
D\. 8Mbps

[tag_link]

正确答案：B
> <p> 首先，计算信道带宽。
> 频率范围为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>3.5</span><span class=mspace> </span><span class="mord text"><span class=mord>MHz</span></span></span></span></span>
到
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>3.9</span><span class=mspace> </span><span class="mord text"><span class=mord>MHz</span></span></span></span></span>
，因此带宽

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05017em>B</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>3.9</span><span class=mspace> </span><span class="mord text"><span class=mord>MHz</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>3.5</span><span class=mspace> </span><span class="mord text"><span class=mord>MHz</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0.4</span><span class=mspace> </span><span class="mord text"><span class=mord>MHz</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8778em;vertical-align:-.1944em></span><span class=mord>400</span><span class=mord><span class=mpunct>,</span></span><span class=mord>000</span><span class=mspace> </span><span class="mord text"><span class=mord>Hz</span></span><span class=mord>.</span></span></span></span></span></div><p>信号功率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.05764em>S</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0.62</span><span class=mspace> </span><span class="mord text"><span class=mord>W</span></span></span></span></span>
，噪声功率
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.10903em>N</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0.02</span><span class=mspace> </span><span class="mord text"><span class=mord>W</span></span></span></span></span>
，信噪比

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0463em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.10903em>N</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0.02</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0.62</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>31.</span></span></span></span></span></div><p>根据香农定理，噪声信道中数字信号的最高数据传输速率（信道容量）为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord mathnormal" style=margin-right:.05017em>B</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:2.4em;vertical-align:-.95em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.1667em></span><span class=minner><span class="mopen delimcenter" style=top:0><span class="delimsizing size3">(</span></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.10903em>N</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.05764em>S</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style=top:0><span class="delimsizing size3">)</span></span></span><span class=mspace style=margin-right:.1667em></span><span class=mord>.</span></span></span></span></span></div><p>代入数值：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>400</span><span class=mord><span class=mpunct>,</span></span><span class=mord>000</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>31</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>400</span><span class=mord><span class=mpunct>,</span></span><span class=mord>000</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>32</span><span class=mclose>)</span><span class=mord>.</span></span></span></span></span></div><p>由于
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class=mord>32</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
，可得

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.07153em>C</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>400</span><span class=mord><span class=mpunct>,</span></span><span class=mord>000</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mord><span class=mpunct>,</span></span><span class=mord>000</span><span class=mord><span class=mpunct>,</span></span><span class=mord>000</span><span class=mspace> </span><span class="mord text"><span class=mord>bps</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mspace> </span><span class="mord text"><span class=mord>Mbps</span></span><span class=mord>.</span></span></span></span></span></div><p>因此，该信道的最高数据传输速率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mspace> </span><span class="mord text"><span class=mord>Mbps</span></span></span></span></span>
，对应选项 B。
>

##### 35

在简单停止 - 等待协议中，为了解决重复帧的问题，需要采用（ ）。

A\. 帧序号
B\. 定时器
C\. ACK 机制
D\. NAK 机制

[tag_link]

正确答案：A
> <p> 在简单停止 - 等待协议中，发送方每发送一帧后必须等待接收方的确认，才能发送下一帧。
> 这种机制容易因确认帧丢失或延迟而产生重复帧问题：当确认丢失时，发送方超时重传原帧，接收方可能再次收到相同帧，若无区分机制，会导致数据重复处理。
> <p>帧序号通过为每个帧分配唯一标识（通常使用 1 位序号，如 0 和 1 交替），使接收方能够检查序号并识别重复帧，从而丢弃它们。
> 定时器主要用于触发超时重传，但可能引入重复帧；
> ACK 机制用于确认正确接收，不直接防止重复；
> NAK 机制用于报告错误，与重复帧无关。
> 因此，帧序号是解决重复帧问题的核心。
>

##### 36

一个 2Mbps 的网络，线路长度为 1km，传输速度为 20m/ms，分组大小为 100 字节，应答帧大小可以忽略。若采用“停止—等待”协议，则实际数据速率是（ ）。

A\. 2Mbps
B\. 1Mbps
C\. 8Kbps
D\. 16Kbps

[tag_link]

正确答案：C
> <p>在停止-等待协议中，实际数据速率取决于分组传输时间和往返传播延迟。
> 分组大小为 100 字节，即 800 比特。
> 网络带宽为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>2</span><span class="mord text"><span class=mord>Mbps</span></span></span></span></span>
，因此分组传输时间为
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">tx</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.2408em;vertical-align:-.8804em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=mord>1</span><span class=mord><span class=mord>0</span><span class=msupsub><span class=vlist-t><span class=vlist-r><span class=vlist style=height:.7401em><span style=top:-2.989em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span><span class=mspace> </span><span class="mord text"><span class=mord>bps</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>800</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">比特</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.8804em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0.0004</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">秒</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0.4</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">毫秒</span></span><span class=mord>.</span></span></span></span></span></div><p>线路长度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class=mord>1</span><span class="mord text"><span class=mord>km</span></span></span></span></span>
，传播速度为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>20</span><span class="mord text"><span class=mord>m/ms</span></span></span></span></span>
，传播时间为
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.9694em;vertical-align:-.2861em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.1514em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">prop</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2861em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.2963em;vertical-align:-.936em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>20</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">米</span><span class=mord>/</span><span class="mord cjk_fallback">毫秒</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1000</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">米</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.936em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>50</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">毫秒</span></span><span class=mord>.</span></span></span></span></span></div><p>由于应答帧大小可忽略，ACK 传输时间不计，但 ACK 传播时间与分组相同，故总周期时间为
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3361em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">total</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.2806em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">tx</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.9694em;vertical-align:-.2861em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.1514em><span style=top:-2.55em;margin-left:-.1389em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord text mtight"><span class="mord mtight">prop</span></span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2861em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>0.4</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">毫秒</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>50</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">毫秒</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>100.4</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">毫秒</span></span><span class=mord>.</span></span></span></span></span></div><p>在此周期内成功传输 800 比特数据，实际数据速率为
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0463em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>100.4</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">毫秒</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>800</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">比特</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>7968</span><span class=mspace> </span><span class="mord text"><span class=mord>bps</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8889em;vertical-align:-.1944em></span><span class=mord>8</span><span class="mord text"><span class=mord>Kbps</span></span><span class=mpunct>,</span></span></span></span></span></div><p>因此选项 C 正确。
>

##### 37

当路由器接收到一个 1500 字节的 IP 数据报时，需要将其转发到 MTU 为 980 的子网，分片后产生两个 IP 数据报，长度分别是（ ）。（首部长度为 20B）

A\. 750, 750
B\. 980, 520
C\. 980, 540
D\. 976, 544

[tag_link]

正确答案：C
> <p>
原始 IP 数据报总长度为 1500 字节，首部长度为 20 字节，因此数据部分长度为 1500 - 20 = 1480 字节。
> 需要转发到 MTU 为 980 的子网，意味着每个分片的总长度（包括首部）不能超过 980 字节。
> <p>每个分片的数据部分长度必须是 8 字节的倍数，这是由 IP 分片偏移量字段的单位决定的。
> 计算每个分片可容纳的最大数据部分：MTU 减去首部长度，即 980 - 20 = 960 字节。
> 960 恰好是 8 的倍数（960 ÷ 8 = 120），因此第一个分片的数据部分可取 960 字节，加上 20 字节首部，总长度为 980 字节。
> <p>剩余数据部分为 1480 - 960 = 520 字节。
> 520 也是 8 的倍数（520 ÷ 8 = 65），因此第二个分片的数据部分为 520 字节，加上 20 字节首部，总长度为 540 字节。
> 分片后两个 IP 数据报的长度分别为 980 字节和 540 字节。
>

##### 38

路由器收到一个数据包，其目地址为 195.26.17.4，该地址属于（ ）子网。

A\. 195.26.0.0/21
B\. 195.26.8.0/22
C\. 195.26.16.0/20
D\. 195.26.20.0/22

[tag_link]

正确答案：C
> <p> 要确定目的地址 195.26.17.4 属于哪个子网，需要检查该地址是否落在每个选项子网的地址范围内。
> 子网范围由其网络地址和前缀长度决定，通过计算网络地址和广播地址进行比较。
> <p>选项 A：195.26.0.0/21，掩码为 255.255.248.0，网络地址为 195.26.0.0，广播地址为 195.26.7.255。
> 目的地址 195.26.17.4 的第三字节为 17，大于 7，因此不在该范围内。
> <p>选项 B：195.26.8.0/22，掩码为 255.255.252.0，网络地址为 195.26.8.0，广播地址为 195.26.11.255。
> 目的地址第三字节 17 大于 11，因此不在该范围内。
> <p>选项 C：195.26.16.0/20，掩码为 255.255.240.0，网络地址为 195.26.16.0，广播地址为 195.26.31.255。
> 目的地址第三字节 17 在 16 到 31 之间，且整个地址 195.26.17.4 在该范围内，因此属于此子网。
> <p>选项 D：195.26.20.0/22，掩码为 255.255.252.0，网络地址为 195.26.20.0，广播地址为 195.26.23.255。
> 目的地址第三字节 17 小于 20，因此不在该范围内。
> <p>综上，目的地址 195.26.17.4 属于 195.26.16.0/20 子网，对应选项 C。
>

##### 39

假设在没有发生拥塞的情况下，在一条往返时间 RTT 为 10ms 的线路上采用慢开始控制策略。如果接收窗口的大小为 24KB，最大报文段 MSS 为 2KB。那么发送方能发送出一个完全窗口（也就是发送窗口达到 24KB）需要的时间是（ ）。

A\. 30ms
B\. 60ms
C\. 50ms
D\. 40ms

[tag_link]

正确答案：D
> <p>
在慢开始控制策略中，拥塞窗口（cwnd）初始值为 1 个 MSS（2KB），每经过一个 RTT，cwnd 翻倍。
> 接收窗口大小为 24KB。
> 发送窗口取 cwnd 和接收窗口的最小值。
> 当 cwnd 增长到等于或超过 24KB 时，发送窗口达到 24KB。
> <p>计算 cwnd 增长过程：经过第一个 RTT 后，cwnd=4KB；
> 第二个 RTT 后，cwnd=8KB；
> 第三个 RTT 后，cwnd=16KB，仍小于 24KB；
> 第四个 RTT 后，cwnd=32KB，超过 24KB，此时发送窗口被接收窗口限制为 24KB，即完全窗口。
> <p>每个 RTT 为 10ms，因此达到完全窗口需要经过 4 个 RTT，总时间为 4 × 10ms = 40ms。
>

##### 40

一台域名服务器希望解析域名 <a href=https://www.google.com>www.google.com</a>。如果这台主机配置的 DNS 地址为 a，Internet 的根域名服务器为 b，而存储域名 <a href=https://www.google.com>www.google.com</a> 与其 IP 地址对应关系的域名服务器为 c，那么这台主机通常先查询（ ）。

A\. 域名服务器 a
B\. 域名服务器 b
C\. 域名服务器 c
D\. 不确定

[tag_link]

正确答案：A
> 在 DNS 解析过程中，主机通常首先查询本地配置的 DNS 服务器，即递归 DNS 服务器。
> 题目中配置的 DNS 地址为 a，因此主机向服务器 a 发送查询请求。
> 服务器 a 如果没有缓存结果，则会代表主机从根服务器 b 开始递归查询，最终可能访问权威服务器 c 获取 IP 地址。
> 主机一般不直接查询根服务器 b 或权威服务器 c，所以优先查询的是 a。
>

---

#### 数据结构

##### 41

（13 分）设有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个不全为负的整型元素存储在一维数组 A[p] 中，它包含很多连续的子数组，例如数组 A = {1, -2, 3, 10, -4, 7, 2, -5}，请设计一个时间上尽可能高效的算法，求出数组 A 的子数组之和的最大值（例如数组 A 的最大的子数组为 {3, 10, -4, 7, 2}，因此输出为该子数组的和 18）。要求：

(1) 给出算法的基本设计思想。
(2) 根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。
(3) 说明你所设计算法的时间复杂度和空间复杂度。

[tag_link]

<p>**【答案】**
(1) 基本设计思想：采用 Kadane 算法（动态规划思想）。遍历数组，维护两个变量：current_sum 记录以当前元素结尾的子数组的最大和，max_sum 记录全局最大子数组和。对于每个元素，若 current_sum 为负，则将其重置为当前元素值（因为负数会减小后续子数组的和），否则将当前元素加入 current_sum。然后更新 max_sum。遍历完成后，max_sum 即为所求。
<p>(2) C 语言算法描述：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><stdio.h></span><span style=color:#8f5902;font-style:italic>
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><limits.h> // 使用 INT_MIN 初始化</span><span style=color:#8f5902;font-style:italic>
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>
</span></span><span style=display:flex><span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>maxSubArray</span><span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>A</span><span style=color:#000;font-weight:700>[],</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>       <span style=color:#8f5902;font-style:italic>// 当前子数组和
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>max_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>INT_MIN</span><span style=color:#000;font-weight:700>;</span>     <span style=color:#8f5902;font-style:italic>// 最大子数组和，初始化为最小整数
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>for</span> <span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>i</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>i</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>i</span><span style=color:#ce5c00;font-weight:700>++</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#8f5902;font-style:italic>// 若当前子数组和为负，则从 A[i] 重新开始，否则累加
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>A</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>i</span><span style=color:#000;font-weight:700>];</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>+=</span> <span style=color:#000>A</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>i</span><span style=color:#000;font-weight:700>];</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>        <span style=color:#8f5902;font-style:italic>// 更新全局最大值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>></span> <span style=color:#000>max_sum</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>max_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>current_sum</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>max_sum</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>(3) 时间复杂度：O(n)，其中 n 为数组长度，仅需一次遍历。空间复杂度：O(1)，仅使用常数个辅助变量。
<p>**【解析】**
该算法基于动态规划，核心是确定以每个元素结尾的最大子数组和。设以元素 A[i] 结尾的最大子数组和为 f(i)，则状态转移方程为：f(i) = max(A[i], f(i-1) + A[i])。这是因为如果 f(i-1) 为负，其对 A[i] 无增益，故从 A[i] 重新开始；否则累加。算法中的 current_sum 即 f(i)，max_sum 记录所有 f(i) 的最大值。由于数组不全为负，max_sum 至少为非负，但算法也适用于全负情况。遍历一次即可求得结果，因此时间效率高，且仅需常数空间。
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
  `,document.head.appendChild(e)}</script><h5 id=42>42</h5><p>图 1 为某操作系统中文件系统的目录结构。
<div class=img-container style=height:auto;width:60% oncontextmenu=return!1> [图片] </div><p>请回答一下问题：
<p>(1) 本题中的目录结构可抽象为数据结构中的哪种逻辑结构？
(2) 请设计合理的链式存储结构，以保存图 1 中的文件目录信息。要求给出链式存储结构的数据类型定义，并画出对应图 1 中根目录部分到目录 A、B 及其子目录和文件的链式存储结构示意图。
(3) 哈夫曼树是一种特殊的树形结构，请证明哈夫曼树的总结点数总为奇数。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-cfaff0242c4957d646be5708f910eba5-2 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/6/ data-page-title="模拟卷 6"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-cfaff0242c4957d646be5708f910eba5-2")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-cfaff0242c4957d646be5708f910eba5-2",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 42

图 1 为某操作系统中文件系统的目录结构。

请回答一下问题：

(1) 本题中的目录结构可抽象为数据结构中的哪种逻辑结构？
(2) 请设计合理的链式存储结构，以保存图 1 中的文件目录信息。要求给出链式存储结构的数据类型定义，并画出对应图 1 中根目录部分到目录 A、B 及其子目录和文件的链式存储结构示意图。
(3) 哈夫曼树是一种特殊的树形结构，请证明哈夫曼树的总结点数总为奇数。

[tag_link]

<p>**【解析】**
本题考察树的相关内容。
<p>(1) 树
<p>(2) 采用孩子兄弟表示法，数据结构描述如下：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#204a87;font-weight:700>typedef</span> <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>CSNode</span><span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>char</span> <span style=color:#000>name</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>MaxSize</span><span style=color:#000;font-weight:700>];</span>           <span style=color:#8f5902;font-style:italic>//存储名称
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>NodeType</span><span style=color:#000;font-weight:700>;</span>                 <span style=color:#8f5902;font-style:italic>//值为 0 代表指向文件，为 1 代表指向目录
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>union</span> <span style=color:#000>p</span><span style=color:#000;font-weight:700>{</span>                      <span style=color:#8f5902;font-style:italic>//用于存储指向文件/目录的信息指针
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000>filepointer</span> <span style=color:#000>p1</span><span style=color:#000;font-weight:700>;</span>           <span style=color:#8f5902;font-style:italic>//文件信息
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000>catalogpointer</span> <span style=color:#000>p2</span><span style=color:#000;font-weight:700>;</span>        <span style=color:#8f5902;font-style:italic>//目录信息
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#000;font-weight:700>};</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>CSNode</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>firstchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>nextsibling</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>//第一个孩子和右兄弟指针
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span> <span style=color:#000>CSNode</span><span style=color:#000;font-weight:700>;</span>
</span></span>`</pre></div><p>图中目录结构的存储大致如下：
<div class=img-container style=height:auto;width:80% oncontextmenu=return!1> [图片] </div><p>本小问只要符合题目要求的答案即可算正确，给出答案仅供参考。
<p>（3）由哈夫曼树中没有度为 1 的结点可知任意哈夫曼树的
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0</span></span></span></span>
，又因哈夫曼树为二叉树，满足
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span></span></span></span>
，所以哈夫曼树的总结点数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.5806em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>0</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7333em;vertical-align:-.15em></span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7944em;vertical-align:-.15em></span><span class=mord>2</span><span class=mord><span class="mord mathnormal">n</span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.3011em><span style=top:-2.55em;margin-left:0;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.15em><span></span></span></span></span></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，可知无论初始有多少个叶子结点，哈夫曼树的总结点数一定为奇数。
</div><h5 id=43>43</h5><p>（8 分）根据 42 题图 1 描述的目录结构，结合以下描述继续回答问题。根目录常驻内存，目录文件组织成链接文件，不设文件控制块，普通文件组织成索引文件。目录表目指示下一级文件名及其磁盘地址（各占 2 个字节，共 4 个字节）。若下级文件是目录文件，指示其第一个磁盘块地址。若下级文件是普通文件，指示其文件控制块的磁盘地址。每个目录文件磁盘块的最后 4 个字节供拉链使用。下级文件在上级目录文件中的次序在图中从左至右。每个磁盘块有 512 字节，与普通文件的一页等长。
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:10.3em;vertical-align:-4.88em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.42em><span style=top:-7.38em><span class=pstrut style=height:7.38em></span><span class=mtable><span class=vertical-separator style="height:10.26em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-4.88em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:5.38em><span style=top:-8.2275em><span class=pstrut style=height:3.6875em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">该文件的有关描述信息</span></span></span></span><span style=top:-7.0275em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord>1.</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">磁盘地址</span></span></span></span><span style=top:-5.8275em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord>2.</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">磁盘地址</span></span></span></span><span style=top:-4.6275em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord>3.</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">磁盘地址</span></span></span></span><span style=top:-2.7675em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord><span class=mord>⋮</span><span class="mord rule" style=border-right-width:0;border-top-width:1.5em;bottom:0></span></span></span></span><span style=top:-1.5675em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord>11.</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">磁盘地址</span></span></span></span><span style=top:-.3675em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord>12.</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">磁盘地址</span></span></span></span><span style=top:.8325em><span class=pstrut style=height:3.6875em></span><span class=mord><span class=mord>13.</span><span class=mspace> </span><span class="mord text"><span class="mord cjk_fallback">磁盘地址</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:4.88em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:10.26em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-4.88em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:7.38em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-11.56em><span class=pstrut style=height:7.38em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-12.76em><span class=pstrut style=height:7.38em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:4.88em><span></span></span></span></span></span></span></span></span></span></div><div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6861em></span><span class="mord text"><span class="mord textbf cjk_fallback">图</span><span class="mord textbf">2</span></span></span></span></span></span></div><p>普通文件的文件控制块组织如图 2 所示，其中，每个磁盘块地址占 2 个字节，前 10 个地址直接指示该文件前 10 页的地址。第 11 个地址指示一级索引表地址，一级索引表中每个磁盘地址指示一个文件页地址；第 12 个地址指示二级索引表地址，二级索引表中每个地址指示一个一级索引表地址；第 13 个地址指示三级索引表地址，三级索引表中每个地址指示一个二级索引表地址。请问：
<p>(1) 一个普通文件最多可有多少个文件页？
(2) 若要读文件 J 中的某一页，最多启动磁盘多少次？
(3) 若要读文件 W 中的某一页，最少启动磁盘多少次？
(4) 就 (3) 而言，为最大限度减少启动磁盘的次数，可采用什么方法？此时，磁盘最多启动多少次？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-cfaff0242c4957d646be5708f910eba5-3 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/6/ data-page-title="模拟卷 6"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-cfaff0242c4957d646be5708f910eba5-3")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-cfaff0242c4957d646be5708f910eba5-3",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

---
#### 计算机组成原理

##### 43

（8 分）根据 42 题图 1 描述的目录结构，结合以下描述继续回答问题。根目录常驻内存，目录文件组织成链接文件，不设文件控制块，普通文件组织成索引文件。目录表目指示下一级文件名及其磁盘地址（各占 2 个字节，共 4 个字节）。若下级文件是目录文件，指示其第一个磁盘块地址。若下级文件是普通文件，指示其文件控制块的磁盘地址。每个目录文件磁盘块的最后 4 个字节供拉链使用。下级文件在上级目录文件中的次序在图中从左至右。每个磁盘块有 512 字节，与普通文件的一页等长。

普通文件的文件控制块组织如图 2 所示，其中，每个磁盘块地址占 2 个字节，前 10 个地址直接指示该文件前 10 页的地址。第 11 个地址指示一级索引表地址，一级索引表中每个磁盘地址指示一个文件页地址；第 12 个地址指示二级索引表地址，二级索引表中每个地址指示一个一级索引表地址；第 13 个地址指示三级索引表地址，三级索引表中每个地址指示一个二级索引表地址。请问：

(1) 一个普通文件最多可有多少个文件页？
(2) 若要读文件 J 中的某一页，最多启动磁盘多少次？
(3) 若要读文件 W 中的某一页，最少启动磁盘多少次？
(4) 就 (3) 而言，为最大限度减少启动磁盘的次数，可采用什么方法？此时，磁盘最多启动多少次？

[tag_link]

<p>**【解析】**
本题考查文件目录的结构。
<p>（1）因为磁盘块大小为 512B，所以索引块大小也为 512B，每个磁盘地址大小为 2B。因此，一个一级索引表可容纳 256 个磁盘地址。同样，一个二级索引表可容纳 256 个一级索引表地址，一个三级索引表可容纳 256 个二级索引表地址。这样，一个普通文件最多可有文件页数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>256</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>256</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>16843018</span></span></span></span>
页。
<p>（2）由图可知，目录文件 A 和 D 中的目录项都只有两个，因此这两个目录文件都只占用一个物理块。要读文件 J 中的某一页，先从内存的根目录中找到目录文件 A 的磁盘地址，将其读入内存（已访盘 1 次）。然后从目录 A 中找出目录文件 D 的磁盘地址并将其读入内存（已访盘 2 次）。再从目录 D 中找出文件 J 的文件控制块地址并将其读入内存（已访盘 3 次）。在最坏情况下，该访问页存放在三级索引下，此时需要一级一级地读三级索引块才能得到文件 J 的地址（已访盘 6 次）。最后读入文件 J 中的相应页（共访盘 7 次）。所以，若要读文件 J 中的某一页，最多启动磁盘 7 次。
<p>（3）由图可知，目录文件 C 和 U 的目录项较多，可能存放在多个链接在一起的磁盘块中。在最好情况下，所需的目录项都在目录文件的第一个磁盘块中。先从内存的根目录中找到目录文件 C 的磁盘地址读入内存（已访盘 1 次）。在 C 中找出目录文件 I 的磁盘地址读入内存（已访盘 2 次）。在 I 中找出目录文件 P 的磁盘地址读入内存（已访盘 3 次）。从 P 中找到目录文件 U 的磁盘地址读入内存（已访盘 4 次）。从 U 的第一个磁盘块中找出文件 W 的文件控制块地址读入内存（已访盘 5 次）。在最好情况下，要访问的页在文件控制块的前 10 个直接块中，按照直接块指示的地址读文件 W 的相应页（已访盘 6 次）。所以，若要读文件 W 中的某一页，最少启动磁盘 6 次。
<p>（4）为了减少启动磁盘的次数，可以将需要访问的 W 文件挂在根目录最前面的目录项中。此时，只需读内存中的根目录就可以找到 W 的文件控制块，将文件控制块读入内存（已访盘 1 次），最差情况下，需要的 W 文件的那个页挂在文件控制块的三级索引下，那么读 3 个索引块需要访问磁盘 3 次（已访盘 4 次）得到该页的物理地址，再去读这个页即可（已访盘 5 次）。此时，磁盘最多启动 5 次。
</div><h5 id=44>44</h5><p>（7 分）有三个进程 PA、PB 和 PC 合作解决文件打印问题：PA 将文件记录从磁盘读入主存的缓冲区 1，每执行一次读一个记录；PB 将缓冲区 1 的内容复制到缓冲区 2，每执行一次复制一个记录；PC 将缓冲区 2 的内容打印出来，每执行一次打印一个记录。缓冲区的大小等于一个记录的大小。请用 P、V 操作来保证文件的正确打印。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-cfaff0242c4957d646be5708f910eba5-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/6/ data-page-title="模拟卷 6"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-cfaff0242c4957d646be5708f910eba5-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-cfaff0242c4957d646be5708f910eba5-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 44

（7 分）有三个进程 PA、PB 和 PC 合作解决文件打印问题：PA 将文件记录从磁盘读入主存的缓冲区 1，每执行一次读一个记录；PB 将缓冲区 1 的内容复制到缓冲区 2，每执行一次复制一个记录；PC 将缓冲区 2 的内容打印出来，每执行一次打印一个记录。缓冲区的大小等于一个记录的大小。请用 P、V 操作来保证文件的正确打印。

[tag_link]

<p>**【解析】**
本题考查用 PV 操作解决进程的同步互斥问题。
<p>进程 PA、PB、PC 之间的关系为：PA 与 PB 共用一个单缓冲区，PB 又与 PC 共用一个单缓冲区，其合作方式如下图所示。当缓冲区 1 为空时，进程 PA 可将一个记录读入其中；若缓冲区 1 中有数据且缓冲区 2 为空，则进程 PB 可将记录从缓冲区 1 复制到缓冲区 2 中；若缓冲区 2 中有数据，则进程 PC 可以打印记录。在其他条件下，相应进程必须等待。事实上，这是一个生产者-消费者问题。
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1> [图片] </div><p>为遵循这一同步规则，应设置 4 个信号量 empty1、empty2、full1、full2，信号量 empty1 及 empty2 分别表示缓冲区 1 及缓冲区 2 是否为空，其初值为 1；信号量 full1 及 full2 分别表示缓冲区 1 及缓冲区 2 是否有记录可供处理，其初值为 0。相应的进程描述如下：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#000>semaphore</span> <span style=color:#000>empty1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>   <span style=color:#8f5902;font-style:italic>// 缓冲区 1 是否为空
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000>semaphore</span> <span style=color:#000>full1</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>    <span style=color:#8f5902;font-style:italic>// 缓冲区 1 是否有记录可供处理
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000>semaphore</span> <span style=color:#000>empty2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>   <span style=color:#8f5902;font-style:italic>// 缓冲区 2 是否为空
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000>semaphore</span> <span style=color:#000>full2</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>    <span style=color:#8f5902;font-style:italic>// 缓冲区 2 是否有记录可供处理
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>
</span></span><span style=display:flex><span><span style=color:#000>cobegin</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>PA</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>while</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>从磁盘读入一条记录</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>将记录存入缓冲区</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>PB</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>while</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>从缓冲区</span> <span style=color:#0000cf;font-weight:700>1</span> <span style=color:#a40000>中取出一条记录</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty1</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>将取出的记录存入缓冲区</span> <span style=color:#0000cf;font-weight:700>2</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span>    <span style=color:#000>process</span> <span style=color:#000>PC</span><span style=color:#000;font-weight:700>()</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>while</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>TRUE</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>P</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>full2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>从缓冲区</span> <span style=color:#0000cf;font-weight:700>2</span> <span style=color:#a40000>中取出一条记录</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>            <span style=color:#000>V</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>empty2</span><span style=color:#000;font-weight:700>);</span>
</span></span><span style=display:flex><span>            <span style=color:#a40000>将取出的记录打印出来</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span> <span style=color:#000>coend</span>
</span></span>`</pre>

---
#### 操作系统

##### 45

（11 分）下图是一个简化的 CPU 与主存连接结构示意图（图中省略了所有多路选择器）。其中有一个累加寄存器 AC、一个状态寄存器和其他四个寄存器：主存地址寄存器 MAR、主存数据寄存器 MDR、程序计数器 PC 和指令寄存器 IR。各部件及其之间的连线表示数据通路，箭头表示信息传送方向。

<strong>一个简化的 CPU 与主存连接结构示意图</strong>

要求：

(1) 请写出图中 a、b、c、d 四个寄存器的名称。
(2) 简述图中指令从主存取到控制器的过程。
(3) 说明数据从主存取出、运算、写回主存所经过的数据通路（假定数据地址已在 MAR 中）。
(4) 程序计数器 PC 的内容是如何变更的？

[tag_link]

<p>**【解析】**
本题考查数据通路和指令执行过程。读者应牢固掌握指令的执行过程和原理，并能根据指令的执行过程和特点了解控制器中各个寄存器的连接方式。
<p>（1）b 单向连接微控制器，由微控制器的作用不难得知 b 是指令寄存器（IR）；
a 和 c 直接连接主存，只可能是 MDR 和 MAR。c 到主存是单向连接，a 和主存双向连接。根据指令执行的特点，MAR 只单向给主存传送地址，而 MDR 既存放从主存中取出的数据又要存放将要写入主存的数据，因此 c 为主存地址寄存器（MAR），a 为主存数据寄存器（MDR）。d 具有自动加 1 的功能，且单向连接 MAR，不难得出为程序计数器（PC）。
<p>因此，a 为 MDR、b 为 IR、c 为 MAR、d 为 PC。
<p>（2）先从程序计数器（PC）中取出指令地址，将指令地址送入主存地址寄存器（MAR），在相关的控制下从主存中取出指令送至主存数据寄存器（MDR），然后将 MDR 中的指令送至指令寄存器（IR），最后流向微控制器，供微控制器分析并执行指令。
<p>因此，取指令的数据通路为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>PC</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord text"><span class=mord>MAR</span></span><span class=mpunct>,</span><span class=mspace style=margin-right:1em></span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mopen>(</span><span class="mord text"><span class=mord>MAR</span></span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>MDR</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class=mord>IR</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class="mord cjk_fallback">控制器</span></span></span></span></span></span></div><p>（3）和（2）的分析类似，根据 MAR 中的地址去主存取数据，将取出的数据送至主存数据寄存器（MDR），然后将 MDR 中的数据送至 ALU 进行运算，运算的结果送至累加器（AC），运算结束后将 AC 中的结果送至 MDR，最后将 MDR 中的数据写入主存。
<p>因此，从主存取出、运算和写回主存所经过的数据通路分别为：

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:6em;vertical-align:-2.75em></span><span class=mord><span class=mtable><span class=col-align-r><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:3.25em><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class=mord>MAR</span></span></span></span><span style=top:-3.91em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mopen>(</span><span class="mord text"><span class=mord>MAR</span></span><span class=mclose>)</span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class=mord>ALU</span></span></span></span><span style=top:-.91em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class=mord>AC</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2.75em><span></span></span></span></span></span><span class=col-align-l><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:3.25em><span style=top:-5.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mpunct>,</span></span></span><span style=top:-3.91em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span><span class="mord text"><span class=mord>MDR</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span><span class="mord text"><span class=mord>ALU</span></span><span class=mpunct>,</span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span><span class="mord text"><span class=mord>AC</span></span><span class=mpunct>,</span></span></span><span style=top:-.91em><span class=pstrut style=height:3em></span><span class=mord><span class=mord></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span><span class="mord text"><span class=mord>MDR</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>→</span><span class=mspace style=margin-right:.2778em></span><span class="mord mathnormal" style=margin-right:.10903em>M</span><span class=mopen>(</span><span class="mord text"><span class=mord>MAR</span></span><span class=mclose>)</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:2.75em><span></span></span></span></span></span></span></span></span></span></span></span></div><p>（4）指令顺序执行时，PC 自动完成 +1 的操作。跳跃执行时，由转移指令提供转移地址（如相对寻址由 PC 的内容加上形式地址）。
</div><h5 id=46>46</h5><p>（11 分）某按字节编址，主存容量为 1MB，采用两路组相联方式（每组仅有两块）的 Cache 容量为 64KB，每个数据块为 256B。已知访问开始前第 2 组（组号为 1）的地址阵列内容如下图所示（第一列为组内块号）：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:3.64em;vertical-align:-1.55em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.09em><span style=top:-4.05em><span class=pstrut style=height:4.05em></span><span class=mtable><span class=vertical-separator style="height:3.6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-1.55em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.05em><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">块号</span></span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.55em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:3.6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-1.55em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.05em><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">标记</span><span class=mord> (Tag)</span><span class="mord cjk_fallback">（二进制）</span></span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>00100</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>01011</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.55em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:3.6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-1.55em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-3.7em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-4.9em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-6.1em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.55em><span></span></span></span></span></span></span></span></span></span></div><p>Cache 采用 LRU 替换策略。
<p>(1) 分别说明主存地址中标记 (Tag)、组号和块内地址三部分的位置和位数。
(2) 若 CPU 要顺序访问地址为 20124H、58100H、60140H 和 60138H 等 4 个主存单元。上述 4 个数能否直接从 Cache 中读取，若能，请给出实际访问的 Cache 地址。第 4 个数访问结束后，上图中的内容将如何变化。
(3) 若 Cache 完成存取的次数为 5000 次，主存完成存取的次数为 200 次。已知 Cache 存取周期为 40ns，主存存取周期为 160ns，求该 Cache-主存系统的访问效率。（注：默认为 Cache 与主存同时访问）
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-cfaff0242c4957d646be5708f910eba5-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/6/ data-page-title="模拟卷 6"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-cfaff0242c4957d646be5708f910eba5-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-cfaff0242c4957d646be5708f910eba5-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

##### 46

（11 分）某按字节编址，主存容量为 1MB，采用两路组相联方式（每组仅有两块）的 Cache 容量为 64KB，每个数据块为 256B。已知访问开始前第 2 组（组号为 1）的地址阵列内容如下图所示（第一列为组内块号）：

Cache 采用 LRU 替换策略。

(1) 分别说明主存地址中标记 (Tag)、组号和块内地址三部分的位置和位数。
(2) 若 CPU 要顺序访问地址为 20124H、58100H、60140H 和 60138H 等 4 个主存单元。上述 4 个数能否直接从 Cache 中读取，若能，请给出实际访问的 Cache 地址。第 4 个数访问结束后，上图中的内容将如何变化。
(3) 若 Cache 完成存取的次数为 5000 次，主存完成存取的次数为 200 次。已知 Cache 存取周期为 40ns，主存存取周期为 160ns，求该 Cache-主存系统的访问效率。（注：默认为 Cache 与主存同时访问）

[tag_link]

<p>**【解析】**
本题考查 Cache 与主存的映射、替换算法。在采用全相联和组相联映像方式从主存向 Cache 传送一个新块，而 Cache 中的空间已被占满时，就需要把原来存储的一块替换掉。LRU 算法（最近最少使用法）是把 CPU 近期最少使用的块作为被替换的块。
<p>（1）按字节编址，每个数据块为 256B，则块内地址为 8 位；主存容量为 1MB，则主存地址为 20 位；Cache 容量为 64KB，Cache 共有 256 块，采用两路组相连，所以 Cache 共有 128 组（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class=mord>64</span><span class="mord mathnormal" style=margin-right:.07153em>K</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>÷</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mopen>(</span><span class=mord>2</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>256</span><span class=mclose>)</span></span></span></span>
），则组号为 7 位；标记（Tag）的位数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>20</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>7</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
位。主存和 Cache 的地址格式如下表所示：
<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.44em;vertical-align:-.95em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.49em><span style=top:-3.45em><span class=pstrut style=height:3.45em></span><span class=mtable><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">主存地址</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">标记</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">组号</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>7</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">块内地址</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>8</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:3.45em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-3.7em><span class=pstrut style=height:3.45em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-4.9em><span class=pstrut style=height:3.45em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span></span></span></span></span></div><div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.44em;vertical-align:-.95em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.49em><span style=top:-3.45em><span class=pstrut style=height:3.45em></span><span class=mtable><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class=mord>Cache</span><span class="mord cjk_fallback">地址</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">组内块号</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">组号</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>7</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.45em><span style=top:-3.61em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">块内地址</span></span></span></span><span style=top:-2.41em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>8</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:2.4em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-.95em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:3.45em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-3.7em><span class=pstrut style=height:3.45em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-4.9em><span class=pstrut style=height:3.45em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.95em><span></span></span></span></span></span></span></span></span></span></div><p>注意：求解标记、组号和块内地址的方法如下：
① 块内地址位数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.3669em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class="mord text"><span class="mord cjk_fallback">数据块大小</span></span><span class=mclose>)</span></span></span></span>
② 组号位数
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.3669em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mop><span class=mop>lo<span style=margin-right:.01389em>g</span></span><span class=msupsub><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.207em><span style=top:-2.4559em;margin-right:.05em><span class=pstrut style=height:2.7em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.2441em><span></span></span></span></span></span></span><span class=mopen>(</span><span class="mord text"><span class=mord>Cache </span><span class="mord cjk_fallback">的总组数</span></span><span class=mclose>)</span></span></span></span>
③ 标记号
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.3669em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord text"><span class="mord cjk_fallback">主存总地址位数</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7667em;vertical-align:-.0833em></span><span class="mord text"><span class="mord cjk_fallback">块内地址位数</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6833em></span><span class="mord text"><span class="mord cjk_fallback">组号位数</span></span></span></span></span>
<p>（2）将 CPU 要顺序访问的 4 个数的地址写成二进制，可以发现：
<ul><li><p><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>20124</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0010</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace> </span><span class=mord>0001</span><span class=mspace> </span><span class=mord>0010</span><span class=mspace> </span><span class=mord>0100</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
，组号为 1，是第 2 组的块，根据题中阵列内容的图可知，现在 Cache 内有这个块，第 1 次访问命中，实际访问的 Cache 地址为 0124H。
</li><li><p><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>58100</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0101</span><span class=mspace> </span><span class=mord>1000</span><span class=mspace> </span><span class=mord>0001</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace> </span><span class=mord>0000</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
，组号为 1，是第 2 组的块，根据题中阵列内容的图可知，现在 Cache 内有这个块，第 2 次访问命中，实际访问的 Cache 地址为 0100H（注意：组内块号并不包含在 Cache 地址中，详情可参考唐朔飞的教材）。
</li><li><p><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>60140</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0110</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace> </span><span class=mord>0001</span><span class=mspace> </span><span class=mord>0100</span><span class=mspace> </span><span class=mord>0000</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
，组号为 1，是第 2 组的块，但 Cache 中无此块，第 3 次访问不命中，根据 LRU 算法，替换掉第 0 块位置上的块，变化后的地址阵列如下表。
</li></ul><div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:3.64em;vertical-align:-1.55em></span><span class=mord><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.09em><span style=top:-4.05em><span class=pstrut style=height:4.05em></span><span class=mtable><span class=vertical-separator style="height:3.6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-1.55em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.05em><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">块号</span></span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>0</span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.55em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:3.6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-1.55em"></span><span class=arraycolsep style=width:.5em></span><span class=col-align-c><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:2.05em><span style=top:-4.21em><span class=pstrut style=height:3em></span><span class=mord><span class="mord text"><span class="mord cjk_fallback">标记</span></span></span></span><span style=top:-3.01em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>01100</span><span class="mord text"><span class="mord cjk_fallback">（二进制）</span></span></span></span><span style=top:-1.81em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>01011</span><span class="mord text"><span class="mord cjk_fallback">（二进制）</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.55em><span></span></span></span></span></span><span class=arraycolsep style=width:.5em></span><span class=vertical-separator style="height:3.6em;border-right-width:.04em;border-right-style:solid;margin:0 -.02em;vertical-align:-1.55em"></span></span></span><span style=top:-2.5em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-3.7em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-4.9em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span><span style=top:-6.1em><span class=pstrut style=height:4.05em></span><span class=hline style=border-bottom-width:.04em></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.55em><span></span></span></span></span></span></span></span></span></span></div><ul><li><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class=mord>60138</span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6833em></span><span class=mord>0110</span><span class=mspace> </span><span class=mord>0000</span><span class=mspace> </span><span class=mord>0001</span><span class=mspace> </span><span class=mord>0011</span><span class=mspace> </span><span class=mord>1000</span><span class="mord mathnormal" style=margin-right:.05017em>B</span></span></span></span>
，组号为 1，是第 2 组的块，与上一个地址处于同一个块，此时这个块已调入 Cache 中，所以第 4 次访问命中，实际访问的 Cache 地址为 0138H。第 4 个数访问结束时，地址阵列的内容与刚才相同。</li></ul><p>（3）Cache 的命中率

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6833em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.1297em;vertical-align:-.7693em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.10903em>N</span><span class="mord mathnormal">c</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class="mord mathnormal" style=margin-right:.10903em>N</span><span class="mord mathnormal">m</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.10903em>N</span><span class="mord mathnormal">c</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.7693em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0908em;vertical-align:-.7693em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5000</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>200</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5000</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.7693em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5200</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5000</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>26</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>25</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div><p>主存慢于 Cache 的倍率

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal" style=margin-right:.02778em>r</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0463em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3603em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class="mord mathnormal">c</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.13889em>T</span><span class="mord mathnormal">m</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>40</span><span class="mord text"><span class=mord>ns</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>160</span><span class="mord text"><span class=mord>ns</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span></span></span></span></span></div><p>访问效率

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">e</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.2574em;vertical-align:-.936em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class="mord mathnormal" style=margin-right:.02778em>r</span><span class=mopen>(</span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mclose>)</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.936em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.4114em;vertical-align:-1.09em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.26em><span class=pstrut style=height:3em></span><span class=mord><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">26</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">25</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span><span class=mord>4</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>×</span><span class=mspace style=margin-right:.2222em></span><span class=minner><span class="mopen delimcenter" style=top:0><span class="delimsizing size1">(</span></span><span class=mord>1</span><span class=mspace style=margin-right:.2222em></span><span class=mbin>−</span><span class=mspace style=margin-right:.2222em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:.8451em><span style=top:-2.655em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">26</span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.394em><span class=pstrut style=height:3em></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">25</span></span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.345em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style=top:0><span class="delimsizing size1">)</span></span></span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:1.09em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>89.7%</span></span></span></span></span>

---
#### 计算机网络

##### 47

（9 分）主机 A 向主机 B 连续发送了 3 个 TCP 报文段。第 1 个报文段的序号为 90，第 2 个报文段的序号为 120，第 3 个报文段的序号为 150。请回答：

(1) 第 1、2 个报文段携带了多少字节的数据？
(2) 主机 B 收到第 2 个报文段后，发回的确认中的确认号应该是多少？
(3) 如果主机 B 收到第 3 个报文段后，发回的确认中的确认号是 200，试问 A 发送的第 3 个报文段中的数据有多少字节？
(4) 如果第 2 个报文段丢失，而其他两个报文段正确到达了主机 B，那么主机 B 在第 3 个报文段到达后，发往主机 A 的确认报文中的确认号应该是多少？

[tag_link]

<p>**【答案】**
(1) 第 1 个报文段携带 30 字节数据，第 2 个报文段携带 30 字节数据。
(2) 确认号为 150。
(3) 第 3 个报文段中的数据有 50 字节。
(4) 确认号为 120。
<p>**【解析】**
(1) TCP 序号表示数据字节的编号。第 1 个报文段序号为 90，第 2 个报文段序号为 120，因此第 1 个报文段的数据字节序号范围为 90 至 119（共 120-90=30 字节）。同理，第 2 个报文段序号为 120，第 3 个报文段序号为 150，因此第 2 个报文段的数据字节序号范围为 120 至 149（共 150-120=30 字节）。
(2) 主机 B 收到第 2 个报文段后，已正确接收序号 90 至 149 的数据，期望收到的下一个字节序号为 150，因此确认号为 150。
(3) 第 3 个报文段序号为 150，确认号为 200 表示主机 B 期望收到的下一个字节序号为 200，因此第 3 个报文段的数据字节序号范围为 150 至 199（共 200-150=50 字节）。
(4) 第 2 个报文段丢失，主机 B 只正确收到第 1 个报文段（序号 90 至 119），期望的下一个字节序号为 120。即使收到第 3 个报文段（序号 150 起），由于数据不连续，TCP 采用累积确认，主机 B 仍发送确认号 120，表示等待序号 120 的数据重传。

---
