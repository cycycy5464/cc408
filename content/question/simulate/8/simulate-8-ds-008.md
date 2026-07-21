---
title: "模拟卷8 数据结构 第8题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 8
subjects:
  - "数据结构"
knowledge_points:
  - "散列表"
question_type: "choice"
difficulty: 3
number: 8

---

散列表的地址范围为 0-17，散列函数为 H(k)=k mod 17。采用线性探测法处理冲突，将关键字序列 26,25,72,38,8,18,59 依次存储到散列表中。元素 59 存放在散列表中的地址是（ ）。

A\. 8
B\. 9
C\. 10
D\. 11

[散列表](/study_methods/tags/408quiz//#%e6%95%a3%e5%88%97%e8%a1%a8)

[tag_link]

正确答案：D
> <p> 散列表地址范围为 0 到 17，共 18 个地址。
> 散列函数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class="mord mathnormal" style=margin-right:.03148em>k</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span></span></span></span>
，采用线性探测法处理冲突。
> 将关键字序列 26, 25, 72, 38, 8, 18, 59 依次插入：
<ul><li>插入 26：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>26</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>26</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>9</span></span></span></span>
，地址 9 为空，存入。
> </li><li>插入 25：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>25</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>25</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
，地址 8 为空，存入。
> </li><li>插入 72：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>72</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>72</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span></span></span></span>
，地址 4 为空，存入。
> </li><li>插入 38：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>38</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>38</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>4</span></span></span></span>
，地址 4 冲突，线性探测下一个地址 5，地址 5 为空，存入。
> </li><li>插入 8：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>8</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>8</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
，地址 8 冲突，线性探测地址 9 冲突，地址 10 为空，存入。
> </li><li>插入 18：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>18</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>18</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
，地址 1 为空，存入。
> </li><li>插入 59：
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:1em;vertical-align:-.25em></span><span class="mord mathnormal" style=margin-right:.08125em>H</span><span class=mopen>(</span><span class=mord>59</span><span class=mclose>)</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6944em></span><span class=mord>59</span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span><span class=mbin><span class=mord><span class="mord mathrm">mod</span></span></span><span class=mspace style=margin-right:.0556em></span><span class=mspace style=margin-right:.2222em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>17</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>8</span></span></span></span>
，地址 8 冲突，线性探测地址 9 冲突，地址 10 冲突，地址 11 为空，存入。
> </li></ul><p>因此，元素 59 存放在地址 11。
>
