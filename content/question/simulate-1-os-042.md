---
title: "模拟卷1 操作系统 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "comprehensive"
difficulty: 4
number: 42
---

（12 分）假设二叉树采用二叉链存储结构存储，设计一个算法，求出根结点到给定某结点之间的路径，要求：
（1）给出算法的基本设计思想。
（2）写出二叉树采用的存储结构代码。
（3）根据设计思想，采用 C 或 C++语言描述算法，关键之处给出注释。

[tag_link]

<p>**【答案】**
<p>（1）算法的基本设计思想：采用递归的深度优先搜索（DFS）方法。从根结点开始，先序遍历二叉树，在遍历过程中使用一个动态数组（如向量）记录当前访问路径。当访问到目标结点时，当前数组中的结点序列即为根结点到目标结点的路径；如果当前结点不是目标结点，则递归遍历其左子树和右子树。若左右子树均未找到目标结点，则进行回溯，从路径中移除当前结点，并返回上一层继续搜索。这种方法利用回溯确保路径的正确性。
<p>（2）二叉树采用的存储结构代码（C语言描述）：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#204a87;font-weight:700>typedef</span> <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>char</span> <span style=color:#000>data</span><span style=color:#000;font-weight:700>;</span>                      <span style=color:#8f5902;font-style:italic>// 结点数据，假设为字符型
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>BiTNode</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>;</span> <span style=color:#8f5902;font-style:italic>// 左右孩子指针
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span> <span style=color:#000>BiTNode</span><span style=color:#000;font-weight:700>,</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>BiTree</span><span style=color:#000;font-weight:700>;</span>
</span></span>`</pre></div><p>（3）算法描述（C++语言，基于上述存储结构）：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-cpp data-lang=cpp><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><vector></span><span style=color:#8f5902;font-style:italic>
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#204a87;font-weight:700>using</span> <span style=color:#204a87;font-weight:700>namespace</span> <span style=color:#000>std</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>
</span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 函数功能：查找从根结点到目标结点的路径
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 参数：root为当前子树根结点，target为目标结点，path用于存储路径
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 返回值：bool类型，找到路径返回true，否则返回false
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#204a87;font-weight:700>bool</span> <span style=color:#000>findPath</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>BiTree</span> <span style=color:#000>root</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>BiTree</span> <span style=color:#000>target</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>vector</span><span style=color:#ce5c00;font-weight:700><</span><span style=color:#000>BiTree</span><span style=color:#ce5c00;font-weight:700>></span> <span style=color:#ce5c00;font-weight:700>&</span><span style=color:#000>path</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>root</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#204a87;font-weight:700>nullptr</span><span style=color:#000;font-weight:700>)</span> <span style=color:#204a87;font-weight:700>return</span> <span style=color:#204a87>false</span><span style=color:#000;font-weight:700>;</span>   <span style=color:#8f5902;font-style:italic>// 空树，直接返回false
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#000>path</span><span style=color:#000;font-weight:700>.</span><span style=color:#000>push_back</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>root</span><span style=color:#000;font-weight:700>);</span>                <span style=color:#8f5902;font-style:italic>// 当前结点加入路径
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>root</span> <span style=color:#ce5c00;font-weight:700>==</span> <span style=color:#000>target</span><span style=color:#000;font-weight:700>)</span> <span style=color:#204a87;font-weight:700>return</span> <span style=color:#204a87>true</span><span style=color:#000;font-weight:700>;</span>     <span style=color:#8f5902;font-style:italic>// 找到目标结点，返回true
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#8f5902;font-style:italic>// 递归搜索左子树
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>findPath</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>root</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>target</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>path</span><span style=color:#000;font-weight:700>))</span> <span style=color:#204a87;font-weight:700>return</span> <span style=color:#204a87>true</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#8f5902;font-style:italic>// 递归搜索右子树
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>findPath</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>root</span><span style=color:#ce5c00;font-weight:700>-></span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>target</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>path</span><span style=color:#000;font-weight:700>))</span> <span style=color:#204a87;font-weight:700>return</span> <span style=color:#204a87>true</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#000>path</span><span style=color:#000;font-weight:700>.</span><span style=color:#000>pop_back</span><span style=color:#000;font-weight:700>();</span>                     <span style=color:#8f5902;font-style:italic>// 左右子树均未找到，回溯，移除当前结点
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#204a87>false</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 调用示例：假设root为根结点指针，target为目标结点指针，path为空的vector<BiTree>类型，
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>// 调���findPath(root, target, path)后，若返回true，则path中存储从根到目标的路径结点序列。
</span></span></span>`</pre></div><p>**【解析】**
<p>算法的核心思想是递归深度优先搜索，结合回溯记录路径。从根结点开始，先访问当前结点并加入路径，然后判断是否为给定结点：若是则成功；否则递归搜索左子树和右子树。递归调用前将当前结点加入路径，调用后若子树中找到目标，则当前结点保留在路径中（因为它是路径的一部分），否则通过pop_back()移除当前结点，实现回溯。这保证了路径从根结点到目标结点的顺序性。
<p>存储结构采用二叉链，每个结点包含数据域和左右孩子指针，便于递归遍历。算法的时间复杂度为O(n)，其中n为二叉树结点数，最坏情况下需要遍历所有结点；空间复杂度为O(h)，h为二叉树高度，主要由递归栈和路径向量占用，路径向量最多存储h个结点。该算法简洁有效，适用于二叉链存储的二叉树路径查找问题。
</div><h5 id=43>43</h5><p>（12 分）以下是计算两个向量点积的程序段：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#204a87;font-weight:700>float</span> <span style=color:#000>Dotproduct</span><span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>float</span> <span style=color:#000>x</span><span style=color:#000;font-weight:700>[</span><span style=color:#0000cf;font-weight:700>8</span><span style=color:#000;font-weight:700>],</span> <span style=color:#204a87;font-weight:700>float</span> <span style=color:#000>y</span><span style=color:#000;font-weight:700>[</span><span style=color:#0000cf;font-weight:700>8</span><span style=color:#000;font-weight:700>])</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>float</span> <span style=color:#000>sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0.0</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>i</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>for</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>i</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>i</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#0000cf;font-weight:700>8</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>i</span><span style=color:#ce5c00;font-weight:700>++</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#000>sum</span> <span style=color:#ce5c00;font-weight:700>+=</span> <span style=color:#000>x</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>i</span><span style=color:#000;font-weight:700>]</span> <span style=color:#ce5c00;font-weight:700>*</span> <span style=color:#000>y</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>i</span><span style=color:#000;font-weight:700>];</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>sum</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>请回答下列问题：
（1）请分析访问数组 x 和 y 时的时间局部性和空间局部性？
（2）假设数据 Cache 采用直接映射方式，Cache 容量为 32 字节，每个主存块大小为 16 字节；编译器将变量 sum 和 i 分配在寄存器中，内存按字节编址，数组 x 存放在 0000 0040H 开始的 32 字节的连续存储区中，数组 y 则紧跟在 x 后进行存放。该程序数据访问的命中率是多少？要求说明每次访问时 Cache 的命中情况。
（3）将上述（2）中的数据 Cache 改用 2-路组相联映射方式，块大小改为 8 字节，其他条件不变，则该程序数据访问的命中率是多少？
（4）在上述（2）中条件不变的情况下，将数组 x 定义为 float[12]，则数据访问的命中率是多少？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-ccaad5634fe13afd20771d2b1485bed0-3 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/1/ data-page-title="模拟卷 1"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-ccaad5634fe13afd20771d2b1485bed0-3")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-ccaad5634fe13afd20771d2b1485bed0-3",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
