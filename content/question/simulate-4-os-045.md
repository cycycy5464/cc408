---
title: "模拟卷4 操作系统 第45题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "操作系统"
knowledge_points:
  - "操作系统"
question_type: "comprehensive"
difficulty: 4
number: 45
---

（8 分）在一间酒吧里有 3 个音乐爱好者队列，第 1 队的音乐爱好者只有随身听，第 2 队只有音乐磁带，第 3 队只有电池。而要听音乐就必须随身听、音乐磁带和电池这 3 种物品俱全。酒吧老板一次出售这 3 种物品中的任意两种。当一名音乐爱好者得到这 3 种物品并听完一首乐曲后，酒吧老板才能再一次出售这 3 种物品中的任意两种。于是第 2 名音乐爱好者得到这 3 种物品，并开始听乐曲。全部买卖就这样进行下去。试用 P、V 操作正确解决这一买卖。

[tag_link]

本题考查用 PV 操作解决进程的同步互斥问题。 第 1 队音乐爱好者要竞争“待出售的音乐磁带和电池”，而且在初始状态下，系统并无“待出售的音乐磁带和电池”，故可为该种资源设置一初值为 0 的信号量 buy1 ；同样，需设置初值为 0 的 buy2 、 buy3 分别对应“待出售的随身听和电池”、“待出售的随身听和音乐磁带”。另外，为了同步买者的付费动作和卖者的给货动作，还需设置信号量 payment 和 goods ，以保证买者在付费后才能得到所需商品。信号量 music_over 用来同步音乐爱好者听乐曲和酒吧老师的下一次出售行为。具体的算法描述如下： semaphore buy1 = buy2 = buy3 = 0 ; semaphore payment = 0 ; semaphore goods = 0 ; semaphore music_over = 0 ; cobegin { process boss () { // 酒吧老板 while ( TRUE ) { 拿出任意两种物品出售； if ( 出售的是音乐磁带和电池 ) V ( buy1 ); else if ( 出售的是随身听和电池 ) V ( buy2 ); else if ( 出售的是随身听和音乐磁带 ) V ( buy3 ); P ( payment ); // 等待付费 V ( goods ); // 给货 P ( music_over ); // 等待乐曲结束 } } process fan1 () { // 第1队音乐爱好者 while ( TRUE ) { // 因为一个进程代表一队，而不是一个爱好者， // 所以这里是 while(true)，下同 P ( buy1 ); // 等有音乐磁带和电池出售 V ( payment ); // 付费 P ( goods ); // 取货 欣赏一曲乐曲； V ( music_over ); // 通知老板乐曲结束 } } process fan2 () { // 第2队音乐爱好者 while ( TRUE ) { P ( buy2 ); // 等有随身听和电池出售 V ( payment ); // 付费 P ( goods ); // 取货 欣赏一曲乐曲； V ( music_over ); // 通知老板乐曲结束 } } process fan3 () { // 第3队音乐爱好者 while ( TRUE ) { P ( buy3 ); // 等有随身听和音乐磁带出售 V ( payment ); // 付费 P ( goods ); // 取货 欣赏一曲乐曲； V ( music_over ); // 通知老板乐曲结束 } } } coend

