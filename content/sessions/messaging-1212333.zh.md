---
title: "Apache Pulsar multi-cluster disaster recovery and progressive traffic migration"
date: ""
track: "messaging"
presenters: "Dezhi LIU"
stype: "中文演讲"
---

Multi-cluster Pulsar operations face two core challenges: rapid disaster recovery failover in the event of a primary cluster failure, and smooth traffic migration during cluster relocation. This presentation introduces the design and implementation of a proxy, which unifies disaster recovery and scheduling through three key technologies—directed connection closure, native weighted routing, and a progressive migration engine—to achieve arbitrary-precision traffic allocation and zero-explosion-radius failover.

### 讲师:


<img src="https://cdn.sessionize.com/image/9fea-400o400o1-3hsAPnSmwMffEueB73VS6x.jpg" width="200" /><br/>

Dezhi LIU: Ascentstream Technology co-founder

● Co-founder of Anliu Technology

● 10+ years of experience in large-scale internet/financial infrastructure development

● Former expert engineer at Tencent, successfully driving the large-scale deployment of Pulsar on Tencent Group's unified billing platform's message bus (capable of handling hundreds of billions of messages) and Tencent Cloud's financial-grade messaging service (TDMQ).

● Apache Pulsar Committer.

