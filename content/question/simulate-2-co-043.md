---
title: "模拟卷2 组成原理 第43题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "组成原理"
knowledge_points:
  - "访存过程"
question_type: "comprehensive"
difficulty: 4
number: 43

---

（11 分）某计算机的主存地址数为 16 位，按字节编址。假定数据 Cache 中最多存放 32 个主存块，采用 2-路组相联方式，块大小为 16B，每块设置了 1 位有效位。采用一次性写回策略，为此每块设置了 1 位“脏”位。请问：

（1）主存地址中标记（Tag）、组号（Index）和块内地址（Offset）三部分的位置和位数分别是多少？该数据 Cache 的总位数是多少？

（2）设字长为 4B，Cache 起始为空，CPU 从主存单元 0，1，…，99，依次读出 100 个字（主存一次读出一个字），并重复按此次序读 6 次，问命中率是多少？

（3）如果块表中组号为 10、行号为 1 的 Cache 块的标记为 36H，有效位为 1，则在 CPU 送来主存的字地址为 36A8H 时是否命中？若命中，此时 Cache 的字地址为多少？

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)

[tag_link]

<p>**【解析】**
(1) 块大小为 16B，故块内地址为 4 位；Cache 有 32 个主存块，采用 2-路组相联，Cache 分为 16 组（32÷2=16），故组号为 4 位；剩余位为标记，即有 16 位 - 4 位 - 4 位 = 8 位。数据 Cache 的总位数应包括标记项的总位数和数据块的位数。每个 Cache 块对应一个标记项，标记项中包括标记字段、有效位和“脏”位（用于写回法）。主存地址中 Tag 为 8 位；组号为 4 位；块内地址为 4 位。标记项的总位数 = 32 × (8 + 1 + 1) = 16 × 10 = 320，数据块的位数 = 32 × 16 × 8 = 4096，因此数据 Cache 的总位数 = 320 + 4096 = 4416。
<p>(2) 由于每个字块有 4 个字，所以 CPU 的 0, 1, &mldr;, 99 字单元分别在字块 0 至 24 中，采用 2-路组相联映射，字块 0～字块 15 将分别映射到第 0 至第 15 组中；字块 16～字块 24 将分别映射到第 0 至第 8 组中。但 Cache 起始为空，每一组有两个 Cache 块，因此当访问主存块 16 时不会将主存块 0 置换出。所以第一次读时每一块中的第一个字没命中，但后面 5 次每个字均可以命中。所以命中率 = (6×100 - 25)/(6×100) = 95.8%。
<p>(3) 字地址 36A8H 对应的 Cache 组号为 AH=10、标记为 36H，块表中组号为 10、行号为 1 的块标记为 36H，且有效位为 1，则当 CPU 送来主存的字地址为 36A8H 时，其主存块号为 36H，所以命中。此时 Cache 字地址为 A8H。
</div><h5 id=44>44</h5><p>已知带返转指令的含义如下图所示：
<p>（1）机器周期长度固定，写出机器在执行带返转指令时，硬布线控制取指令段和执行阶段所需的全部微操作命令及节拍安排。
<p>（2）若采用微程序控制，还需增加哪些微操作？
<p>（3）假设该机指令系统采用 6 位定长操作码格式，共对应多少个微程序？
<p>（4）在原理、执行速度和灵活性三个方面分析硬布线控制和微程序控制的区别。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-6869bcc00e31ab3a0b0139a586e91bbe-4 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/2/ data-page-title="模拟卷 2"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-6869bcc00e31ab3a0b0139a586e91bbe-4")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-6869bcc00e31ab3a0b0139a586e91bbe-4",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
