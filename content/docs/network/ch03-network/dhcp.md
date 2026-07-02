---
title: "DHCP协议"
date: 2026-06-25
weight: 20
tags: [体系结构]
difficulty: 2
prerequisites: []
subject: network
chapter: 3
chapter_title: "DHCP协议"
---

⭐ 中优先级

需掌握 DHCP 的功能和流程，可能在选择题中考察，也会在大题中考查一小问。

动态主机配置协议（DHCP）是一个网络管理协议，用于自动分配 **IP 地址** 和其他网络配置参数给网络设备，从而允许它们连接到 **IP 网络** 。

当你连接到一个网络中时，不管是通过 **无线网** ，还是在电脑上连接了 **以太网线** ，你会发现无需任何配置，你自动获取了一个 **IP 地址** ，并可以通过该 IP 地址进行网络通信。


![](/images/docs/network/2fe6b7b7ff.svg)


Here is your...Text is not SVG - cannot display

**DHCP** 的工作流程通常包括以下四个步骤，这个过程也被称作 **DORA** 过程，即 **Discover** , **Offer** , **Request** , 和 **Acknowledgment** 。

  1. **Discover** :
* 客户端通过网络 **广播** 一个 **DHCP DISCOVER** 消息，请求可用的网络配置信息。因为客户端还没有分配到 **IP 地址** ，所以这个消息的 **源 IP 地址** 是 _0.0.0.0_ ，**目的 IP 地址** 是 _255.255.255.255_ 。



  2. **Offer** :
* 网络上的 DHCP 服务器接收到 **DHCP DISCOVER** 消息后，会向客户端发送一个 **DHCP OFFER** 消息。这个消息包含了一个提供给客户端的 **IP 地址** 和其他配置信息，如 **子网掩码** 、**DNS 服务器地址** 和 **IP 地址租用期** 。



  3. **Request** :
* 客户端可能会从多个 DHCP 服务器收到多个 **DHCP OFFER** 消息。客户端选择其中一个提议，并通过 **广播** 一个 **DHCP REQUEST** 消息来响应这个提议，通知网络中的所有 DHCP 服务器它接受了哪个 DHCP 服务器的提议。



  4. **Acknowledgment** :
* 提供所选 IP 地址的 DHCP 服务器收到 **DHCP REQUEST** 消息后，会发送一个 **DHCP ACK** 给客户端，确认IP 地址和配置信息的租约。如果由于某种原因导致该 IP 地址不再可用或者有其他问题，DHCP 服务器可能会发送一个 **DHCP NAK** 。


