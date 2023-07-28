---
title: "没有Zookeeper的Kafka"
date: "2023-08-18T15:45:00" 
track: "messaging"
presenters: "Luke Chen,邓子明"
stype: "中文演讲"
---
目前，Kafka依赖ZooKeeper来存储它的元数据，例如:broker信息，topic, partition…等等。KRaft是没有Zookeeper的新一代Kafka。本讲座将包括:

1. 为什么Kafka需要开发新的KRaft特性。
2. 旧的(有Zookeeper) Kafka和新的(没有Zookeeper) Kafka的架构
3. 采用Kafka的好处
4. 它是如何在内部运作的。
5. 监控指标
6. 帮助解决 Kafka 问题的工具
7. 一个演示来展示我们目前所取得的成就。
8. Kafka社区走向KRaft的路线图。

在这次演讲之后，观众可以更好地了解KRaft是什么，它是如何工作的，以及它与基于Zookeeper的Kafka的区别是什么，最重要的是，如何监控它并对其进行故障排除。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230526/1018099720.jpg" width="200" /><br>Luke Chen: RedHat, 高级软件工程师, 我是RedHat的一名高级软件工程师，致力于在云上运行Apache Kafka的产品。我也是Apache Kafka的提交者和PMC成员。我为Apache Kafka贡献了3年多的时间。
 <br><br><img src="https://img.bagevent.com/resource/20230525/1008439060.jpg" width="200" /><br>邓子明: 字节跳动, 数据开发, Apache Kafka提交者
 <br><br>