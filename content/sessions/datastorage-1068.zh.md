---
title: "最近和即将发布的HBase版本有哪些新特性？"
date: "2023-08-18T13:30:00" 
track: "datastorage"
presenters: "张铎"
stype: "中文演讲"
---
Apache HBase™是Hadoop数据库，是一个分布式的、可扩展的、大数据存储。HBase社区正在准备新的主要版本3.0.0和新的次要版本2.6.0，新增了一些全新的功能。在本次演讲中，我们将介绍这些新功能，以及它们如何使我们的用户受益以及如何在HBase中实现它们，包括：

- OpenTelemetry跟踪：HBASE-22120，HBASE-26419
- 新的区域复制框架：HBASE-26233
- 将日志框架从log4j迁移到log4j2：HBASE-19577
- 云原生支持
  - 引入StoreFileTracker以支持更好的对象存储：HBASE-26067，HBASE-26584
  - K8s部署支持：HBASE-27827，正在进行中
- 不在ZooKeeper上持久化数据
- 将元数据位置移出ZooKeeper：HBASE-26193
- 基于表的复制队列存储：HBASE-27109
- 基于文件系统的复制对等存储：HBASE-27110
- 仅使用对象存储的根目录重新部署集群：HBASE-26245
- 未来？
  - 在Ozone上的HBase
  - 在Ozone上的WAL：HBASE-27740
  - 完全云原生，除了HBase本身没有其他自己部署的服务
  - 新的WAL实现：BookKeeper？嵌入式WAL服务？
  
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230603/2240000820.jpg" width="200" /><br>张铎: 神策数据, 首席架构师, 清华大学计算机科学与技术系本硕，长期从事开源软件的开发与维护。2015 至今历任ApacheHBase 项目的 Committer、PMC 成员、主席。2020 年成为 Apache 软件基金会的 Member。2018 年，在 Apache 软件基金会全球近 7000 名 Committer 中，贡献数量排名第三。曾任小米开源委员会主席，负责小米整体开源工作的规划与推进。目前在神策数据担任首席架构师。
 <br><br>