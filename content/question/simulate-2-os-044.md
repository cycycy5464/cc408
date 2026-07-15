---
title: "模拟卷2 操作系统 第44题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "comprehensive"
difficulty: 4
number: 44
---

已知带返转指令的含义如下图所示：

（1）机器周期长度固定，写出机器在执行带返转指令时，硬布线控制取指令段和执行阶段所需的全部微操作命令及节拍安排。

（2）若采用微程序控制，还需增加哪些微操作？

（3）假设该机指令系统采用 6 位定长操作码格式，共对应多少个微程序？

（4）在原理、执行速度和灵活性三个方面分析硬布线控制和微程序控制的区别。

[tag_link]

<p>**【解析】**
由图中可知，当子程序执行完毕时，返回地址存放在以 **K** 为地址的内存单元中（间址特征位为 1，即间接寻址）。带返回指令的执行阶段需要完成将返回地址 **M+1** 存入指令地址码字段 **K** 所指示的存储单元中，从 **K+1** 号单元开始才是子程序的真正内容，因此执行阶段的微操作命令及节拍安排如下：
<p>（1）取指周期：
节拍 T0：`PC → MAR，1 → R` （注：`M → MAR`）
节拍 T1：`M(MAR) → MDR，(PC) + 1 → PC`
节拍 T2：`MDR → IR，OP(IR) → ID`
<p>执行周期：
节拍 T0：`K(IR) → MAR` （把 K 放入 MAR）
节拍 T1：`PC → MDR，1 → W` （注：`M+1 → MDR`）（把 PC 放到 MDR 中，为存入主存做准备）
节拍 T2：`MDR → M(MAR)，K+1 → PC` （把要返回的 PC 保存到 K 中，同时更新 PC）
<p>（2）若采用微程序控制，还需增加的微操作有：
`M → CMAR`
// 将取指周期微程序首地址放入
`CM(CMAR) → CMDR`
// 将对应控存 M 地址单元中的第一条微指令读到控存数据寄存器中
`AD(CMDR) → CMAR`
// 让微指令的顺序控制字段指出下一条微指令的地址为 M+1，送入 CMAR
<p>（3）2⁶ = 64 个微程序，一条机器指令对应一段微程序。注：若单独把取指指令独立写成一个微程序，则微程序个数多 1；若 CPU 带有中断功能，微程序个数还要加一；如果把间址操作独立出来，也会多 1。因此微程序的数量根据情况不同应为 64–67 个。
<p>（4）微程序控制器采用“存储程序”原理，每条机器指令对应一个微程序，因此修改和扩充容易、灵活性好，但每条指令的执行都要访问控制存储器，所以速度较慢。硬布线控制器采用专门的逻辑电路实现，其速度主要取决于逻辑电路的延迟，因此速度快，但修改和扩展比较困难。
</div><h5 id=45>45</h5><p>（7 分）系统有 5 个进程，其就绪时刻（指在该时刻已进入就绪队列）、服务时间如下表所示。分别计算采用先来先服务、短作业优先、高响应比优先的平均周转时间和带权周转时间。
<table><thead><tr><th>进程</th><th>就绪时刻</th><th>服务时间</th></tr></thead><tbody><tr><td>P₁</td><td>0</td><td>3</td></tr><tr><td>P₂</td><td>2</td><td>6</td></tr><tr><td>P₃</td><td>4</td><td>4</td></tr><tr><td>P₄</td><td>6</td><td>5</td></tr><tr><td>P₅</td><td>8</td><td>2</td></tr></tbody></table><div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-6869bcc00e31ab3a0b0139a586e91bbe-5 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/2/ data-page-title="模拟卷 2"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-6869bcc00e31ab3a0b0139a586e91bbe-5")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-6869bcc00e31ab3a0b0139a586e91bbe-5",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
