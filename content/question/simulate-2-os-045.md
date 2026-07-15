---
title: "模拟卷2 操作系统 第45题"
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
number: 45
---

（7 分）系统有 5 个进程，其就绪时刻（指在该时刻已进入就绪队列）、服务时间如下表所示。分别计算采用先来先服务、短作业优先、高响应比优先的平均周转时间和带权周转时间。

[tag_link]

<p>**【答案】**
先来先服务：平均周转时间 8.6，平均带权周转时间 2.56
短作业优先：平均周转时间 7.6，平均带权周转时间 1.84
高响应比优先：平均周转时间 8.0，平均带权周转时间 2.14
<p>**【解析】**
(1) 采用先来先服务调度时，执行作业的次序为 P₁、P₂、P₃、P₄、P₅，如下表所示。
<table><thead><tr><th>作业号</th><th>就绪时刻</th><th>服务时间</th><th>等待时间</th><th>开始时刻</th><th>结束时刻</th><th>周期时间</th><th>带权周转时间</th></tr></thead><tbody><tr><td>P₁</td><td>0</td><td>3</td><td>0</td><td>0</td><td>3</td><td>3</td><td>3/3=1.0</td></tr><tr><td>P₂</td><td>2</td><td>6</td><td>1</td><td>3</td><td>9</td><td>7</td><td>7/6=1.17</td></tr><tr><td>P₃</td><td>4</td><td>4</td><td>5</td><td>9</td><td>13</td><td>9</td><td>9/4=2.25</td></tr><tr><td>P₄</td><td>6</td><td>5</td><td>7</td><td>13</td><td>18</td><td>12</td><td>12/5=2.4</td></tr><tr><td>P₅</td><td>8</td><td>2</td><td>10</td><td>18</td><td>20</td><td>12</td><td>12/2=6.0</td></tr><tr><td>平均</td><td></td><td></td><td></td><td></td><td></td><td>8.6</td><td>2.56</td></tr></tbody></table><p>(2) 采用短作业优先调度时，执行作业的次序为 P₁、P₂、P₅、P₃、P₄，如下表所示。
<table><thead><tr><th>作业号</th><th>就绪时刻</th><th>服务时间</th><th>等待时间</th><th>开始时刻</th><th>结束时刻</th><th>周期时间</th><th>带权周转时间</th></tr></thead><tbody><tr><td>P₁</td><td>0</td><td>3</td><td>0</td><td>0</td><td>3</td><td>3</td><td>3/3=1.0</td></tr><tr><td>P₂</td><td>2</td><td>6</td><td>1</td><td>3</td><td>9</td><td>7</td><td>7/6=1.17</td></tr><tr><td>P₅</td><td>8</td><td>2</td><td>1</td><td>9</td><td>11</td><td>3</td><td>3/2=1.5</td></tr><tr><td>P₃</td><td>4</td><td>4</td><td>7</td><td>11</td><td>15</td><td>11</td><td>11/4=2.75</td></tr><tr><td>P₄</td><td>6</td><td>5</td><td>9</td><td>15</td><td>20</td><td>14</td><td>14/5=2.8</td></tr><tr><td>平均</td><td></td><td></td><td></td><td></td><td></td><td>7.6</td><td>1.84</td></tr></tbody></table><p>(3) 采用高响应比优先调度时，响应比 = (等待时间 + 服务时间) / 运行时间。在时刻 0，只有进程 P₁ 就绪，执行 P₁，在时刻 3 结束。此时只有 P₂ 就绪，执行 P₂，在时刻 9 结束。此时 P₃、P₄、P₅ 均就绪，计算它们的响应比分别为 2.25、1.6、1.5，则选择执行 P₃，在时刻 13 结束。此时 P₄、P₅ 均就绪，计算它们的响应比分别为 2.4、3.5，则选择执行 P₅，在时刻 15 结束。此时只有 P₄ 就绪，执行 P₄，在时刻 20 结束。整个执行作业的次序为 P₁、P₂、P₃、P₅、P₄，如下���所示。
<table><thead><tr><th>作业号</th><th>就绪时刻</th><th>服务时间</th><th>等待时间</th><th>开始时刻</th><th>结束时刻</th><th>周期时间</th><th>带权周转时间</th></tr></thead><tbody><tr><td>P₁</td><td>0</td><td>3</td><td>0</td><td>0</td><td>3</td><td>3</td><td>3/3=1.0</td></tr><tr><td>P₂</td><td>2</td><td>6</td><td>1</td><td>3</td><td>9</td><td>7</td><td>7/6=1.17</td></tr><tr><td>P₃</td><td>4</td><td>4</td><td>5</td><td>9</td><td>13</td><td>9</td><td>9/4=2.25</td></tr><tr><td>P₅</td><td>8</td><td>2</td><td>5</td><td>13</td><td>15</td><td>7</td><td>7/2=3.5</td></tr><tr><td>P₄</td><td>6</td><td>5</td><td>9</td><td>15</td><td>20</td><td>14</td><td>14/5=2.8</td></tr><tr><td>平均</td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>2.14</td></tr></tbody></table></div><h5 id=46>46</h5><p>在一个分页存储管理系统中，地址空间分页（每页 1K），物理空间分块，设主存总量为 256KB，描述主存分配情况的位示意图如下右图所示（0 表示未分配，1 表示已分配），此时作业调度程序选中一个长为 5.2KB 的作业投入内存。试问：
<div class=img-container style=height:auto;width:80% oncontextmenu=return!1> [图片] </div><p>（1）为该作业分配内存后（分配内存时，首先分配低地址的内存空间），请填写该作业的页表内容。
<p>（2）页式存储管理有无内存碎片存在？若有，会存在哪种内存碎片？为该作业分配内存后，会产生内存碎片吗？如果产生，大小为多少？
<p>（3）假设一个 64MB 内存容量的计算机，采用页式存储管理（页面大小为 4K），内存分配采用位示图方式管理，请问位示图将占用多大的内存？
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-6869bcc00e31ab3a0b0139a586e91bbe-6 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/2/ data-page-title="模拟卷 2"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-6869bcc00e31ab3a0b0139a586e91bbe-6")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-6869bcc00e31ab3a0b0139a586e91bbe-6",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>
