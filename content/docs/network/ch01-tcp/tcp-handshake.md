---
title: "TCP 三次握手与四次挥手"
date: 2026-06-25
weight: 1
tags: [TCP, 连接管理, 可靠传输]
difficulty: 2
prerequisites: []
subject: network
chapter: 1
chapter_title: "计算机网络概述"
exam_points:
  - "TCP连接管理"
  - "TCP拥塞控制"
  - "可靠传输机制"
---

## TCP 连接建立（三次握手）

```
Client                          Server
  |  SYN=1, seq=x               |
  |---------------------------->|  LISTEN
  |                             |  SYN=1, seq=y
  |                             |  ACK=1, ack=x+1
  |<----------------------------|
  |  ACK=1, ack=y+1, seq=x+1    |
  |---------------------------->|  ESTABLISHED
  |                             |  ESTABLISHED
```

### 为什么要三次握手？

防止已失效的连接请求报文段突然又传送到了服务端，产生错误连接。

## TCP 连接释放（四次挥手）

```
Client                          Server
  |  FIN=1, seq=u               |  ESTABLISHED
  |---------------------------->|  ACTIVE CLOSE
  |                             |  ACK=1, ack=u+1
  |<----------------------------|  CLOSE WAIT
  |                             |  (Server应用层关闭)
  |  FIN=1, seq=w               |
  |---------------------------->|  LAST ACK
  |                             |  ACK=1, ack=w+1
  |<----------------------------|  CLOSED
  |  ACK=1, ack=w+1, seq=u+1    |
  |---------------------------->|  TIME WAIT (2MSL)
  |                             |  CLOSED
```

## TCP 拥塞控制

### 四个算法

1. **慢启动**：指数增长窗口
2. **拥塞避免**：线性增长窗口
3. **快重传**：收到3个重复ACK立即重传
4. **快恢复**：窗口减半而非归零

### 窗口变化

```
cwnd = 1
while (no loss) {
    cwnd = min(cwnd * 2, ssthresh);  // 慢启动
}
// 到达 ssthresh
while (no loss) {
    cwnd = cwnd + 1;  // 拥塞避免
}
// 发生超时
ssthresh = cwnd / 2;
cwnd = 1;
// 发生3个重复ACK
ssthresh = cwnd / 2;
cwnd = ssthresh;  // 快恢复
```

## TCP 可靠传输

- 序号机制
- 确认应答（ACK）
- 超时重传
- 流量控制（滑动窗口）
