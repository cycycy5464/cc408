---
title: "模拟卷7 组成原理 第16题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "组成原理"
knowledge_points:
  - "访存过程"
  - "页面置换算法"
question_type: "choice"
difficulty: 3
number: 16

---

某虚拟存储系统采用页式存储管理，只有 a、b 和 c 三个页框，页面访问的顺序为：
0, 1, 2, 4, 2, 3, 0, 2, 1, 3, 2, 3, 0, 1, 4
若采用 FIFO 替换算法，则命中率为（ ）。

A\. 20%
B\. 26.7%
C\. 15%
D\. 50%

[访存过程](/study_methods/tags/408quiz//#%e8%ae%bf%e5%ad%98%e8%bf%87%e7%a8%8b)
[页面置换算法](/study_methods/tags/408quiz//#%e9%a1%b5%e9%9d%a2%e7%bd%ae%e6%8d%a2%e7%ae%97%e6%b3%95)

[tag_link]

正确答案：B
> <p> 本题考查 FIFO 算法。
> FIFO 算法指淘汰**先进入**的，易知替换顺序为：
<table><thead><tr><th>走向</th><th>0</th><th>1</th><th>2</th><th>4</th><th>2</th><th>3</th><th>0</th><th>2</th><th>1</th><th>3</th><th>2</th><th>3</th><th>0</th><th>1</th><th>4</th></tr></thead><tbody><tr><td>c</td><td></td><td></td><td>2</td><td>2</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>b</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td></tr><tr><td>a</td><td>0</td><td>0</td><td>0</td><td>4</td><td>4</td><td>4</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>命中否</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td></tr></tbody></table><p>表中除了标注为命中的，其余均未命中，所以命中率为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class=mord>4/15</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.8056em;vertical-align:-.0556em></span><span class=mord>26.7%</span></span></span></span>
。
>
