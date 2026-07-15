---
title: "模拟卷5 计算机网络 第35题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 5
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "choice"
difficulty: 3
number: 35
---

以下几种 CSMA 协议中，什么协议在监听到介质是空闲时一定发送（ ）。
I. 1-坚持 CSMA
II. p-坚持 CSMA
III. 非坚持 CSMA

A\. 只有 I
B\. I 和 III
C\. I 和 II
D\. I、II 和 III

[tag_link]

正确答案：B
> 本题考查 CSMA 协议的各种监听。
> 1-坚持 CSMA 和非坚持 CSMA 检测到信道空闲时，都立即发送数据帧，它们之间的区别是：如果检测到媒体忙时，是否持续监听媒体（1-坚持）还是等待一个随机的延迟时间后再监听（非坚持）。
> p-坚持 CSMA：当检测到媒体空闲时，该站点以概率 p 的可能性发送数据，而有 1-p 的概率会把发送数据帧的任务延迟到下一个时槽，Ⅱ错误。
>
