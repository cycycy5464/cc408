---
title: "存储系统 第7题"
date: 2026-07-16
type: question
years:
  - "课后题"
subjects:
  - "组成原理"
knowledge_points:
  - "虚拟存储器"
question_type: "choice"
difficulty: 2
source: "课后题"
number: 16
tags: ['课后题']
---

对于下列代码，以下哪种变化将使其具有更好的空间局部性()。
①int                 i,j,k,sum=0;②for(i=0;i<n;            i++) for(j=0;j<n;j++)for(k=0;k<n;k++)⑤              sum+=a[k][j][i];
①int                 i,j,k,sum=0;
②for(i=0;i<n;            i++) for(j=0;j<n;j++)
for(k=0;k<n;k++)
⑤              sum+=a[k][j][i];

A. 将第2行与第3行互换           B.   将第2行与第4行互换
C. 将第5行改为sum+=a[i][k]ij];             D.   将第5行改为sum+=a[j][i][k];

[tag_link]

正确答案：B