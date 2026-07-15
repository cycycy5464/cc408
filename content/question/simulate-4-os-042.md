---
title: "模拟卷4 操作系统 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "comprehensive"
difficulty: 4
number: 42
---

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
