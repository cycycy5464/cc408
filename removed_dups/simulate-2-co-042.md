---
title: "模拟卷2 计算机组成原理 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "comprehensive"
difficulty: 4
number: 42
---

（13 分）将一个数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转。输入一个已排好序数组的一个旋转，求该旋转数组的最小元素。如，数组 {3, 4, 5, 1, 2} 为有序数组 {1, 2, 3, 4, 5} 的一个旋转数组，该数组的最小值为 1。

（1）给出算法的基本设计思想。

（2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

（3）说明你所设计算法的时间复杂度和空间复杂度。

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)
[复杂度分析](/study_methods/tags/408quiz//#%e5%a4%8d%e6%9d%82%e5%ba%a6%e5%88%86%e6%9e%90)

[tag_link]

<p>**【答案】**
<p>（1）基本设计思想：
采用改进的二分查找。由于旋转数组由两个有序子数组构成，且最小元素是第二个子数组的首元素。设置两个指针 low 和 high 分别指向数组首尾，计算中间位置 mid。比较 nums[mid] 与 nums[high]：
<ul><li>若 nums[mid] > nums[high]，说明最小值在右半部分，令 low = mid + 1；</li><li>若 nums[mid] < nums[high]，说明最小值在左半部分（包含 mid），令 high = mid；</li><li>若相等，无法判断，但可通过 high&ndash; 缩小范围（不会丢失最小值）。
重复直到 low == high，此时指向最小元素。</li></ul><p>（2）算法描述（C++）：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-cpp data-lang=cpp><span style=display:flex><span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>findMin</span><span style=color:#000;font-weight:700>(</span><span style=color:#000>vector</span><span style=color:#ce5c00;font-weight:700><</span><span style=color:#204a87;font-weight:700>int</span><span style=color:#ce5c00;font-weight:700>>&</span> <span style=color:#000>nums</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>low</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>,</span> <span style=color:#000>high</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>nums</span><span style=color:#000;font-weight:700>.</span><span style=color:#000>size</span><span style=color:#000;font-weight:700>()</span> <span style=color:#ce5c00;font-weight:700>-</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>while</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>low</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#000>high</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>mid</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>low</span> <span style=color:#ce5c00;font-weight:700>+</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>high</span> <span style=color:#ce5c00;font-weight:700>-</span> <span style=color:#000>low</span><span style=color:#000;font-weight:700>)</span> <span style=color:#ce5c00;font-weight:700>/</span> <span style=color:#0000cf;font-weight:700>2</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 防止溢出
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>nums</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>mid</span><span style=color:#000;font-weight:700>]</span> <span style=color:#ce5c00;font-weight:700>></span> <span style=color:#000>nums</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>high</span><span style=color:#000;font-weight:700>])</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>low</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>mid</span> <span style=color:#ce5c00;font-weight:700>+</span> <span style=color:#0000cf;font-weight:700>1</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 最小值在右半部分
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>nums</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>mid</span><span style=color:#000;font-weight:700>]</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#000>nums</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>high</span><span style=color:#000;font-weight:700>])</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>high</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>mid</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 最小值在左半部分（可能为 mid）
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>high</span><span style=color:#ce5c00;font-weight:700>--</span><span style=color:#000;font-weight:700>;</span>  <span style=color:#8f5902;font-style:italic>// 相等时无法判断，缩小右边界
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>nums</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>low</span><span style=color:#000;font-weight:700>];</span>  <span style=color:#8f5902;font-style:italic>// low == high，指向最小值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>（3）时间复杂度：平均 O(log n)，最坏情况（全部相等） O(n)。
空间复杂度：O(1)，仅用了常数个变量。
<p>**【解析】**
本题是旋转数组找最小值的经典问题。原数组有序，旋转后形成两个有序子数组，且最小值位于第二个子数组开头。直接遍历需要 O(n) 时间，而利用二分思想可提升效率。
比较 nums[mid] 与 nums[high] 是关键：若 nums[mid] > nums[high]，说明 mid 属于第一个子数组，最小值必在 mid 右侧；若 nums[mid] < nums[high]，说明 mid 属于第二个子数组，最小值在 mid 左侧（含 mid）；若相等，则无法二分（如数组有重复元素），但通过 high&ndash; 可逐步缩小范围，确保不遗漏最小值。
算法在大部分情况下达到对数复杂度，仅当大量重复元素时退化为线性，这是处理重复情况下的最优方式之一。
</div><h5 id=43>43</h5><p>（11 分）某计算机的主存地址数为 16 位，按字节编址。假定数据 Cache 中最多存放 32 个主存块，采用 2-路组相联方式，块大小为 16B，每块设置了 1 位有效位。采用一次性写回策略，为此每块设置了 1 位“脏”位。请问：
<p>（1）主存地址中标记（Tag）、组号（Index）和块内地址（Offset）三部分的位置和位数分别是多少？该数据 Cache 的总位数是多少？
<p>（2）设字长为 4B，Cache 起始为空，CPU 从主存单元 0，1，…，99，依次读出 100 个字（主存一次读出一个字），并重复按此次序读 6 次，问命中率是多少？
<p>（3）如果块表中组号为 10、行号为 1 的 Cache 块的标记为 36H，有效位为 1，则在 CPU 送来主存的字地址为 36A8H 时是否命中？若命中，此时 Cache 的字地址为多少？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-6869bcc00e31ab3a0b0139a586e91bbe-3 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/2/ data-page-title="模拟卷 2"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-6869bcc00e31ab3a0b0139a586e91bbe-3")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-6869bcc00e31ab3a0b0139a586e91bbe-3",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
