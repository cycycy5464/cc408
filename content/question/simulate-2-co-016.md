---
title: "模拟卷2 计算机组成原理 第16题"
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
question_type: "choice"
difficulty: 3
number: 16
---

某计算机的存储系统由 Cache-主存系统构成，Cache 的存取周期为 10ns，主存的存取周期为 50ns。在 CPU 执行一段程序时，Cache 完成存取的次数为 4800 次，主存完成的存取次数为 200 次，该 Cache-主存系统的效率是（ ）。（设 Cache 和主存不能同时访问）

A\. 0.833

B\. 0.856

C\. 0.958

D\. 0.862

[tag_link]

正确答案：A
> 首先，计算总存取次数：高速缓存完成 4800 次，主存完成 200 次，总次数为 4800 + 200 = 5000 命中率 H = 高速缓存存取次数 / 总次数 = 5000 4800 ​ = 0.96 由于高速缓存和主存不能同时访问，当高速缓存命中时，访问时间仅为高速缓存的存取周期 10 ns；
> 当高速缓存未命中时，需要先访问高速缓存（耗时 10 ns），发现未命中后再访问主存（耗时 50 ns），总时间为 10 ns + 50 ns = 60 ns 平均访问时间 T avg ​ = H × T cache ​ + ( 1 − H ) × ( T cache ​ + T mem ​ ) 代入数值 T avg ​ ​ = 0.96 × 10 ns + 0.04 × ( 10 ns + 50 ns ) = 9.6 ns + 0.04 × 60 ns = 9.6 ns + 2.4 ns = 12 ns ​ 也可使用简化公式 T avg ​ = T cache ​ + ( 1 − H ) × T mem ​ = 10 ns + 0.04 × 50 ns = 10 ns + 2 ns = 12 ns 两种公式结果一致，因为 H × T cache ​ + ( 1 − H ) × ( T cache ​ + T mem ​ ) = T cache ​ + ( 1 − H ) × T mem ​ 效率 e 定义为高速缓存存取周期与平均访问时间的比值，即 e = T avg ​ T cache ​ ​ = 12 ns 10 ns ​ ≈ 0.8333 对应选项 A。
>

