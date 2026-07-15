---
title: "模拟卷5 计算机组成原理 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "comprehensive"
difficulty: 4
number: 42
---

（12 分）假设二叉树采用二叉链表存储结构，设计一个算法求其指定的某一层
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span></span></span></span>
（
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7335em;vertical-align:-.0391em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>></span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
）的叶子结点个数，要求：
（1）给出算法的基本设计思想。
（2）写出二叉树采用的存储结构代码。
（3）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

[寄存器类型](/study_methods/tags/408quiz//#%e5%af%84%e5%ad%98%e5%99%a8%e7%b1%bb%e5%9e%8b)

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
