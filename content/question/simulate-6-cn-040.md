---
title: "模拟卷6 计算机网络 第40题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "计算机网络"
knowledge_points:
  - "计算机网络"
question_type: "choice"
difficulty: 3
number: 40
---

一台域名服务器希望解析域名 www.google.com 。如果这台主机配置的 DNS 地址为 a，Internet 的根域名服务器为 b，而存储域名 www.google.com 与其 IP 地址对应关系的域名服务器为 c，那么这台主机通常先查询（ ）。

A\. 域名服务器 a

B\. 域名服务器 b

C\. 域名服务器 c

D\. 不确定

[tag_link]

正确答案：A
> 在 DNS 解析过程中，主机通常首先查询本地配置的 DNS 服务器，即递归 DNS 服务器。
> 题目中配置的 DNS 地址为 a，因此主机向服务器 a 发送查询请求。
> 服务器 a 如果没有缓存结果，则会代表主机从根服务器 b 开始递归查询，最终可能访问权威服务器 c 获取 IP 地址。
> 主机一般不直接查询根服务器 b 或权威服务器 c，所以优先查询的是 a。
>

