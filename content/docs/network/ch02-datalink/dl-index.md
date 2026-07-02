---
title: "数据链路层"
date: 2026-06-25
weight: 9
tags: [数据链路层]
difficulty: 1
prerequisites: []
subject: network
chapter: 1
chapter_title: "数据链路层"
---

在选择题中考察，个别年份也在大题中考察过，需熟练掌握介质访问控制的相关方法。

学习思维导图：
    
    
    
## 数据链路层的功能

## 组帧

## 差错控制

- 检错编码
- 纠错编码

## 流量控制和可靠传输机制

- 流量控制、可靠传输和滑动窗口
- 停等协议
- 回退N帧
- 选择性重传协议

## 介质访问控制

- 信道划分
- 随机访问：ALOHA, CSMA, CSMA/CD, CSMA/CA
- 轮询访问

## 局域网

- 基本概念和体系结构
- 以太网和IEEE 802.3
- 无限局域网和IEEE 802.11
- VLAN

## 广域网

- 基本概念
- PPP协议

## 数据链路层设备

- 以太网交换机和工作原理




**数据链路层功能**

  1. 封装数据帧（Frame Encapsulation）：
* 数据链路层将来自网络层的数据包封装成数据帧，这包括将源和目标地址添加到帧头部，以便在物理介质上的传输。



  2. 数据帧传输（Frame Transmission）：
* 数据链路层负责将数据帧从一个物理节点传输到另一个物理节点。这可能涉及到点对点的传输（例如，以太网）或多点广播传输（例如，Wi-Fi）。



  3. 物理地址寻址（Physical Addressing）：
* 数据链路层使用物理地址（通常是 MAC 地址）来标识设备。这些地址用于确定数据帧的目标设备。



  4. 帧同步和定界（Frame Synchronization and Framing）：
* 数据链路层确保接收端可以正确识别和分离不同的数据帧。这通常通过在帧的起始和结束位置使用特殊的比特模式来实现。



  5. 流量控制（Flow Control）：
* 数据链路层可以控制发送端的数据传输速率，以防止接收端不堪重负而丢失数据。这确保了适当的数据流量管理。



  6. 差错检测和纠正（Error Detection and Correction）：
* 数据链路层使用差错检测技术（如 CRC 校验）来检测帧在传输过程中是否受到损坏。一些数据链路层协议还可以进行错误纠正，尝试修复损坏的数据。




* * *

##### [组帧](</computer_network/datalink/framing/>)

##### [差错控制](</computer_network/datalink/error/>)

##### [流量控制](</computer_network/datalink/flow_control/>)

##### [介质访问控制](</computer_network/datalink/mac/>)

##### [局域网和广域网](</computer_network/datalink/lan/>)

##### [数据链路层设备](</computer_network/datalink/dev/>)
