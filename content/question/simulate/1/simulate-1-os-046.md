---
title: "模拟卷1 操作系统 第46题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "操作系统"
knowledge_points:
  - "协议数据单元"
question_type: "comprehensive"
difficulty: 4
number: 46

---

（9 分）一个进程分配给 4 个页帧（下面的所有数字均为十进制数，每一项都是从 0 开始计数的）。最后一次把一页装入到一个页帧的时间、最后一次访问页帧中的页的时间、每个页帧中的虚页号以及每个页帧的访问位（R）和修改位（M）如下表所示（时间均为从进程开始到该事件之前的时钟值，而不是从事件发生到当前的时钟值）。

当虚页 4 发生缺页时，使用下列存储器管理策略，哪一个页帧将用于置换？解释每种情况的原因。

（1）FIFO（先进先出）算法。

（2）LRU（最近最少使用）算法。

（3）改进的 Clock 算法。

（4）在缺页之前给定上述的存储器状态，考虑下面的虚页访问串：

4, 0, 0, 0, 2, 4, 2, 1, 0, 3, 2

如果使用 LRU 页面置换算法，分给 4 个页帧，会发生多少缺页？

[协议数据单元](/study_methods/tags/408quiz//#%e5%8d%8f%e8%ae%ae%e6%95%b0%e6%8d%ae%e5%8d%95%e5%85%83)

[tag_link]

<p>**【答案】**
（1）页帧3
（2）页帧1
（3）页帧1
（4）3次缺页
<p>**【解析】**
（1）FIFO算法基于页面加载时间，选择加载时间最早的页面置换。表中加载时间分别为：页帧0（60）、页帧1（130）、页帧2（26）、页帧3（20）。页帧3的加载时间最早（20），因此用于置换。
<p>（2）LRU算法基于最近访问时间，选择访问时间最早的页面置换。表中访问时间分别为：页帧0（161）、页帧1（160）、页帧2（162）、页帧3（163）。页帧1的访问时间最早（160），因此用于置换。
<p>（3）改进的Clock算法优先选择R=0且M=0的页面。表中页帧状态：页帧0（R=0, M=1）、页帧1（R=0, M=0）、页帧2（R=1, M=0）、页帧3（R=1, M=1）。页帧1满足R=0且M=0，因此用于置换。算法扫描时（假设从页帧0开始），遇到页帧1即选中，无需进一步扫描。
<p>（4）使用LRU算法模拟虚页访问串。初始内存中有虚页0、1、2、3，最后访问时间如表所示（虚页1最早，虚页3最晚）。模拟过程：
<ul><li>访问虚页4：缺页，置换LRU页面虚页1（页帧1），装入虚页4。</li><li>访问虚页0：命中，更新访问时间。</li><li>访问虚页0：命中，更新访问时间。</li><li>访问虚页0：命中，更新访问时间。</li><li>访问虚页2：命中，更新访问时间。</li><li>访问虚页4：命中，更新访问时间。</li><li>访问虚页2：命中，更新访问时间。</li><li>访问虚页1：缺页，置换LRU页面虚页3（页帧3），装入虚页1。</li><li>访问虚页0：命中，更新访问时间。</li><li>访问虚页3：缺页，置换LRU页面虚页4（页帧1），装入虚页3。</li><li>访问虚页2：命中，更新访问时间。
缺页发生在访问4、1、3时，共3次缺页。</li></ul></div><h5 id=47>47</h5><p>（9 分）TCP 的拥塞窗口 cwnd 大小与传输轮次 n 的关系如下所示：
<table><thead><tr><th>cwnd</th><th>1</th><th>2</th><th>4</th><th>8</th><th>16</th><th>32</th><th>33</th><th>34</th><th>35</th><th>36</th><th>37</th><th>38</th><th>39</th></tr></thead><tbody><tr><td>n</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr></tbody></table><table><thead><tr><th>cwnd</th><th>40</th><th>41</th><th>42</th><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>1</th><th>2</th><th>4</th><th>8</th></tr></thead><tbody><tr><td>n</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td></tr></tbody></table><p>（1）画出 TCP 的拥塞窗口与传输轮次的关系曲线。
<p>（2）分别指明 TCP 工作在慢开始阶段和拥塞避免阶段的时间间隔。
<p>（3）在第 16 轮次和第 22 轮次之后发送方是通过收到三个重复的确认还是通过超时检测到丢失了报文段？
<p>（4）在第 1 轮次、第 18 轮次和第 24 轮次发送时，门限 ssthresh 分别被设置为多大？
<p>（5）在第几轮次发送出第 70 个报文段？
<p>（6）假定在第 26 轮次之后收到了三个重复的确认，因而检测出了报文段的丢失，那么拥塞窗口 cwnd 和门限 ssthresh 应设置为多大？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-ccaad5634fe13afd20771d2b1485bed0-7 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/1/ data-page-title="模拟卷 1"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-ccaad5634fe13afd20771d2b1485bed0-7")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-ccaad5634fe13afd20771d2b1485bed0-7",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
