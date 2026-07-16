---
title: "查找 第5题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "数据结构"
knowledge_points:
  - "查找"
question_type: "comprehensive"
difficulty: 2
source: "课后题"
number: 69
tags: ['课后题']
---

设散列表为HT[0...12],    即表的大小为 m=13 。 现采用双散列法解决冲突，散列函数和 再散列函数分别为：
H₀(key)=key%13              注：%是取模运算(=mod)
H₁=(H₁-1+REV(key+1)%11+1)%13;i=1,2,3,…,m-1
其中，函数REV(x)表示颠倒十进制数x 的各位，如REV(37)=73 、REV(7)=7  等。若插 入的关键码序列为(2,8,31,20,19,18,53,27),请回答：
1)画出插入这8个关键码后的散列表。
2)计算查找成功的平均查找长度ASL。

[tag_link]

【解答】