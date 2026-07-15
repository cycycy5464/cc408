---
title: "模拟卷1 计算机组成原理 第43题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "计算机组成原理"
knowledge_points:
  - "计算机组成原理"
question_type: "comprehensive"
difficulty: 4
number: 43
---

（12 分）以下是计算两个向量点积的程序段：

请回答下列问题：
（1）请分析访问数组 x 和 y 时的时间局部性和空间局部性？
（2）假设数据 Cache 采用直接映射方式，Cache 容量为 32 字节，每个主存块大小为 16 字节；编译器将变量 sum 和 i 分配在寄存器中，内存按字节编址，数组 x 存放在 0000 0040H 开始的 32 字节的连续存储区中，数组 y 则紧跟在 x 后进行存放。该程序数据访问的命中率是多少？要求说明每次访问时 Cache 的命中情况。
（3）将上述（2）中的数据 Cache 改用 2-路组相联映射方式，块大小改为 8 字节，其他条件不变，则该程序数据访问的命中率是多少？
（4）在上述（2）中条件不变的情况下，将数组 x 定义为 float[12]，则数据访问的命中率是多少？

[tag_link]

<p>**【答案】**
（1）时间局部性差，空间局部性好。
（2）命中率为0%。
（3）命中率为50%。
（4）命中率为75%。
<p>**【解析】**
（1）时间局部性指同一数据在短期内被重复访问的可能性，数组 `x` 和 `y` 的每个元素在循环中仅被访问一次，因此时间局部性较差；空间局部性指访问附近数据的可能性较高，数组元素按顺序访问且内存连续，因此空间局部性较好。
<p>(2) Cache 共有 32B / 16B = 2 行；4 个数组元素占一个主存块（现在的计算机中 float 型一般为 32 位，占 4B）；数组 x 的 8 个元素（共 32B）分别存放在主存 40H 开始的 32 个单元中，共占有 2 个主存块，其中 x[0]～x[3] 在第 4 块（00H-0FH 为第 0 块，10H-1FH 为第 1 块，以此类推，40H-4FH 为第 4 块，下同），x[4]～x[7] 在第 5 块中，数组 y 的 8 个元素分别在主存第 6 块和第 7 块中。所以，x[0]～x[3] 和 y[0]～y[3] 都映射到 Cache 第 0 行；x[4]～x[7] 和 y[4]～y[7] 都映射到 Cache 第 1 行，如下图所示。因为 x[i] 和 y[i]（0≤i≤7）总是映射到同一个 Cache 行，相互淘汰对方，故每次都不命中，命中率为 0。
<table><thead><tr><th>Cache——主存地址</th><th>40H～5FH</th><th>60H～7FH</th></tr></thead><tbody><tr><td>第 0 行</td><td>x[0]～x[3]（第四块）</td><td>y[0]～y[3]（第六块）</td></tr><tr><td>第 1 行</td><td>x[4]～x[7]（第五块）</td><td>y[4]～y[7]（第七块）</td></tr></tbody></table><p>**(3)** 若 Cache 改用 2-路组相联，块大小改为 8B，则 Cache 共有 4 行，每组 2 行，共 2 组。两个数组元素占一个主存块。数组 x 占 4 个主存块，数组元素 x[0]～x[1]，x[2]～x[3]，x[4]～x[5]，x[6]～x[7] 分别在第 8～11 块中（与上题同理，这里 00H～07H 为第 0 块，08H～0FH 为第 1 块，以此类推）；数组 y 占 4 个主存块，数组元素 y[0]～y[1]，y[2]～y[3]，y[4]～y[5]，y[6]～y[7] 分别在第 12～15 块中，映射关系如下图所示：因为每组有两行，所以 x[i] 和 y[i]（0≤i≤7）虽然映射到同一个 Cache 组，但可以存放到同一组的不同 Cache 行内，因此，不会发生冲突。每调入一个主存块，装入的 2 个数组元素中，第 2 个数组元素总是命中，故命中率为 50%。
<table><thead><tr><th>Cache——主存地址</th><th>40H～4FH</th><th>50H～5FH</th><th>60H～6FH</th><th>70H～7FH</th></tr></thead><tbody><tr><td>第一组</td><td>x[0]～x[1]</td><td>x[4]～x[5]</td><td>y[0]～y[1]</td><td>y[4]～y[5]</td></tr><tr><td>第二组</td><td>x[2]～x[3]</td><td>x[6]～x[7]</td><td>y[2]～y[3]</td><td>y[6]～y[7]</td></tr></tbody></table><p>**(4)** 将数组 x 定义为 12 个元素后，则 x 共有 48B，使得 y 从主存第 7 块开始存放，即 x[0]～x[3] 在第 4 块，x[4]～x[7] 在第 5 块，x[8]～x[11] 在第 6 块中；y[0]～y[3] 在第 7 块，y[4]～y[7] 在第 8 块。因此，x[i] 和 y[i]（0≤i≤7）就不会映射到同一个 Cache 行中，映射关系如下图所示。每调入一个主存块，装入 4 个数组元素，第一个元素不命中，后面 3 个总命中，故命中率为 75%。
<table><thead><tr><th>Cache——主存地址</th><th>40H～5FH</th><th>60H～7FH</th><th>80H～8FH</th></tr></thead><tbody><tr><td>第 0 行</td><td>x[0]～x[3]（第四块）</td><td>x[8]～x[11]（第六块）</td><td>y[4]～y[7]（第八块）</td></tr><tr><td>第 1 行</td><td>x[4]～x[7]（第五块）</td><td>y[0]～y[4]（第七块）</td><td>—</td></tr></tbody></table></div><h5 id=44>44</h5><p>（12 分）假定硬盘传输数据以 32 位的字为单位，传输速率为 1MB/s。CPU 的时钟频率为 50MHz。
<p>（1）采用程序查询的输入输出方式，假定不能使数据丢失，求传输程序运行周期占用 CPU 的时间比率。
<p>（2）采用中断方法进行控制，每次传输的开销（包括中断处理）为 100 个时钟周期。求 CPU 为传输硬盘数据花费的时间比率。
<p>（3）采用 DMA 控制器进行输入输出操作，假定 DMA 的启动操作需要 1000 个时钟周期，DMA 完成时处理中断需要 500 个时钟周期。如果平均传输的数据长度为 4KB（此处，1MB=1000KB），问在硬盘工作的一次传输中，处理器将用多少时间比重进行输入输出操作，忽略 DMA 申请使用总线的影响。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-ccaad5634fe13afd20771d2b1485bed0-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/1/ data-page-title="模拟卷 1"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-ccaad5634fe13afd20771d2b1485bed0-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-ccaad5634fe13afd20771d2b1485bed0-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
