---
title: "摆脱主题元数据的限制，Apache Pulsar的无限数据保留"
date: "2022-07-30T14:50:00"
track: "messaging"
room: "A"
presenters: "李鹏辉"
stype: "中文演讲"
---
Pulsar 主题数据不会受到单个节点存储资源的限制，无论该主题是未分区的主题还是单分区主题。最根本的原因是 Pulsar 使用了逻辑存储模型。Pulsar 主题数据将分布到更多的 bookie 节点，分区/主题不会 1:1 绑定到任何存储节点。

但是，逻辑存储模型还意味着我们需要为元数据存储中的每个数据段维护元数据，即一个 ledger 列表，以表明数据存储在哪个 ledger 中。如果想要无限的主题数据保存，元数据存储方式将成为瓶颈。减少 ledger 滚动的频率可以延长遇到瓶颈的时间，但主题卸载也会导致 ledger 滚动。加载 manager、重启 broker 或手动都会触发 ledger 滚动。

主题元数据限制主要分为两部分:

1. a) 用于维护主题元数据的大 Znode 大小
2. b) 内存消费以缓存一个主题的所有 ledger

这次演讲将分享 Apache Pulsar 如何摆脱限制，支持无限数据保留的主题。
 ### Speakers: 
 <img src="images/speaker/1185.png" width="200" /><br>李鹏辉：StreamNative 首席架构师，Apache Pulsar PMC 成员与 Committer。在加入 StreamNative 之前，李鹏辉就职于智联招聘(Zhaopin.com)担任软件工程师，并领导团队落地部署 Pulsar。

 