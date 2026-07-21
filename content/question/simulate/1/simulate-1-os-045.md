---
title: "模拟卷1 操作系统 第45题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "操作系统"
knowledge_points:
  - "磁盘概念"
  - "磁盘性能指标"
question_type: "comprehensive"
difficulty: 4
number: 45

---

（7 分）一个磁盘机有 19,456 个柱面，16 个读写磁头，并且每个磁道有 63 个扇区。磁盘以 5400rpm 的速度旋转。试问：

（1）如果磁盘的平均寻道时间是 10ms，那么读一个扇区的平均时间是多少？

（2）在一个请求分页系统中，若将该磁盘用作交换设备，而且页面大小和扇区的大小相同。读入一个换出页的平均时间和上面计算的相同。假设如果一个页必须被换出，则寻找换入页的平均寻道时间将只有 1ms，那么传输这两个页的平均时间是多少？

（3）如果在该系统中打开的文件数目远远多于驱动器的数目时，对磁盘机有什么影响？

[磁盘概念](/study_methods/tags/408quiz//#%e7%a3%81%e7%9b%98%e6%a6%82%e5%bf%b5)
[磁盘性能指标](/study_methods/tags/408quiz//#%e7%a3%81%e7%9b%98%e6%80%a7%e8%83%bd%e6%8c%87%e6%a0%87)

[tag_link]

<p>**【答案】**
(1) 读一个扇区的平均时间约为15.73 ms。
(2) 传输两个页（换入页和换出页）的平均时间约为22.46 ms。
(3) 可能导致饥饿或者抖动。
<p>**【解析】**
（1）读取一个扇区的平均时间由三部分组成：平均寻道时间、平均旋转延迟和数据传输时间。平均寻道时间给定为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。磁盘转速为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>5400</span><span class=mspace> </span><span class="mord text"><span class=mord>rpm</span></span></span></span></span>
，旋转一圈的时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>5400</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>60</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>90</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>1</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace> </span><span class="mord text"><span class=mord>s</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>11.111</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mpunct>,</span></span></span></span></span></div><p>平均旋转延迟为半圈时间，即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>5.556</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。每个磁道有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>63</span></span></span></span>
个扇区，一个扇区的数据传输时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:2.0074em;vertical-align:-.686em></span><span class=mord><span class="mopen nulldelimiter"></span><span class=mfrac><span class="vlist-t vlist-t2"><span class=vlist-r><span class=vlist style=height:1.3214em><span style=top:-2.314em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>63</span></span></span><span style=top:-3.23em><span class=pstrut style=height:3em></span><span class=frac-line style=border-bottom-width:.04em></span></span><span style=top:-3.677em><span class=pstrut style=height:3em></span><span class=mord><span class=mord>11.111</span></span></span></span><span class=vlist-s></span></span><span class=vlist-r><span class=vlist style=height:.686em><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.176</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mord>.</span></span></span></span></span></div><p>因此，总平均时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>10</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>5.556</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.176</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>15.73</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mord>.</span></span></span></span></span></div><p>（2）在请求分页系统中，页面大小与扇区相同。读入一个换出页的平均时间与（1）相同，为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>15.73</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。但当必须换出页时，寻找换入页的平均寻道时间减少为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
，因此换入页的传输时间变为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>1</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>5.556</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.176</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>6.73</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mord>.</span></span></span></span></span></div><p>对于换出页，其传输时间仍假设为正常写操作时间，即平均寻道时间
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>10</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
、旋转延迟
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>5.556</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
和数据传输
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>0.176</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
，合计约
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>15.73</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span></span></span></span>
。传输两个页（换入和换出）的总平均时间为

<div class=td-max-width-on-larger-screens><span class=katex-display><span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.7278em;vertical-align:-.0833em></span><span class=mord>6.73</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2222em></span><span class=mbin>+</span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>15.73</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mspace style=margin-right:.2778em></span><span class=mrel>≈</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>22.46</span><span class=mspace> </span><span class="mord text"><span class=mord>ms</span></span><span class=mord>.</span></span></span></span></span></div><p>（3）可能会产生两个后果：
第一个后果是**饥饿**，这是由于请求磁盘 I/O 操作的应用程序得不到满足而长时间在阻塞队列等待，从而导致饥饿；
第二个后果是**抖动**，由于每次磁盘 I/O 操作完成后都要进行磁盘的换入换出，从而导致抖动。
</div><h5 id=46>46</h5><p>（9 分）一个进程分配给 4 个页帧（下面的所有数字均为十进制数，每一项都是从 0 开始计数的）。最后一次把一页装入到一个页帧的时间、最后一次访问页帧中的页的时间、每个页帧中的虚页号以及每个页帧的访问位（R）和修改位（M）如下表所示（时间均为从进程开始到该事件之前的时钟值，而不是从事件发生到当前的时钟值）。
<table><thead><tr><th>虚页号</th><th>页帧</th><th>加载时间</th><th>访问时间</th><th>R 位</th><th>M 位</th></tr></thead><tbody><tr><td>2</td><td>0</td><td>60</td><td>161</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>130</td><td>160</td><td>0</td><td>0</td></tr><tr><td>0</td><td>2</td><td>26</td><td>162</td><td>1</td><td>0</td></tr><tr><td>3</td><td>3</td><td>20</td><td>163</td><td>1</td><td>1</td></tr></tbody></table><p>当虚页 4 发生缺页时，使用下列存储器管理策略，哪一个页帧将用于置换？解释每种情况的原因。
<p>（1）FIFO（先进先出）算法。
<p>（2）LRU（最近最少使用）算法。
<p>（3）改进的 Clock 算法。
<p>（4）在缺页之前给定上述的存储器状态，考虑下面的虚页访问串：
<p>4, 0, 0, 0, 2, 4, 2, 1, 0, 3, 2
<p>如果使用 LRU 页面置换算法，分给 4 个页帧，会发生多少缺页？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-ccaad5634fe13afd20771d2b1485bed0-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/1/ data-page-title="模拟卷 1"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-ccaad5634fe13afd20771d2b1485bed0-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-ccaad5634fe13afd20771d2b1485bed0-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
