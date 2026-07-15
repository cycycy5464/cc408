---
title: "模拟卷3 数据结构 第41题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 3
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 41
---

（13 分）设记录的关键字（key）集合：K={24, 15, 39, 26, 18, 31, 05, 22}，请回答：
（1）依次取 K 中各值，构造一棵二叉排序树（不要求平衡），并写出该树的前序、中序和后序遍历序列。
（2）设 Hash 表表长 m=16，Hash 函数 H(key)=(key)%13，处理冲突方法为“二次探测法”，请依次取 K 中各值，构造出满足所给条件的 Hash 表；并求出等概率条件下查找成功时的平均查找长度。
（3）将给定的 K 调整成一个堆顶元素取最大值的堆（即大根堆）。

[tag_link]

<p>**【解析】**
（1）将关键字{24，15，39，26，18，31，05，22}依次插入构成的二叉排序树如下：
<div class=img-container style=height:auto;width:35% oncontextmenu=return!1> [图片] </div><p>先序遍历序列：24，15，05，18，22，39，26，31
中序遍历序列：05，15，18，22，24，26，31，39
后序遍历序列：05，22，18，15，31，26，39，24
<p>（2）各关键字通过 Hash 函数得到的散列地址如下表。
<table><thead><tr><th>关键字</th><th>24</th><th>15</th><th>39</th><th>26</th><th>18</th><th>31</th><th>05</th><th>22</th></tr></thead><tbody><tr><td>散列地址</td><td>11</td><td>2</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>9</td></tr></tbody></table><p>Key=24、15、39 均没有冲突，H₀(26)=0，冲突，H₁(26)=0+1=1，没有冲突；
Key=18 没有冲突，H₀(31)=5，冲突，H₁(31)=5+1=6，没有冲突；H₀(05)=5，冲突，H₁(05)=5+1=6，冲突，H₂(05)=5-1=4，没有冲突；Key=22 没有冲突。故各个关键字的存储地址如下表所示。
<table><thead><tr><th>地址</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th></tr></thead><tbody><tr><td>关键字</td><td>39</td><td>26</td><td>15</td><td></td><td>05</td><td>18</td><td>31</td><td></td><td></td><td>22</td><td></td><td>24</td><td></td><td></td><td></td><td></td></tr></tbody></table><p>没有发生冲突的关键字，查找的比较次数为 1，发生冲突的关键字，查找的比较次数为冲突次数+1，因此，等概率下的平均查找长度为：
<p>ASL = (1+1+1+2+1+2+3+1)/2 = 1.5 次
<p>（3）首先对以 26 为根的子树进行调整，调整后的结果如图 b 所示；对以 39 为根的子树进行调整，调整后的结果如图 c 所示；再对以 15 为根的子树进行调整，调整后的结果如图 d 所示；最后对根结点进行调整，调整后的结果如图 e 所示。
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1> [图片]
