---
title: "应用层 第12题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "计算机网络"
knowledge_points:
  - "HTTP"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 71
tags: ['课后题']
---

一个TCP 首部的数据信息(十六进制表示)为0x0D        280015505FA9060000000070
024000     C0290000。TCP 首部的格式如下图所示。请回答：
1) 源端口号和目的端口号各是多少?
2)发送的序号是多少?确认序号是多少?
3) TCP 首部的长度是多少?
4)这是一个使用什么协议的TCP 连接?该TCP 连接的状态是什么?
32位-
部位  0           8                16               24            31
部
TC
首
P
部
源端口
目的端口
20 固定
B 的
首
序号
确认号
数据
偏移
保留
UR G
AC K
P SH
RST
SYN
FIN
窗 口
检验和
紧急指针
选项(长度可变)
填充

[tag_link]

