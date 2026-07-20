---
title: "Apache Ratis 中的一致性模型"
date: "2026-08-08T14:00:00"
track: "datastorage"
presenters: "Tsz-Wo Nicholas Sze"
stype: "英文演讲"
room: "万寿山会议室"
---

Apache Ratis 是一个实现 Raft 共识协议的开源 Java 库，Raft 是一种分布式共识算法，用于确保多台机器像一个协调一致的整体那样协同工作。Ratis 是 Raft 的高性能实现。为适应多种多样的使用场景，Ratis 支持多种可配置的一致性级别。此外，Ratis 为读写操作同时提供了同步与异步 API。众多项目都使用了 Ratis，例如 Apache Ozone、Apache IoTDB、Apache Celeborn 和 Alluxio。

Raft 与 Ratis 的设计目标都是提供强一致性——具体而言，一旦某次写操作被确认完成，此后所有的读操作都保证能反映这次写操作的效果。读操作则更有意思，因为一致性与性能之间存在根本性的权衡。Ratis 实现了多种读机制，包括从 leader 直接读取、线性一致读（linearizable read）、从 follower 读取、读后写（read-after-write）一致性以及从 follower 读取陈旧数据（stale-read）。

本次演讲将先简要介绍 Raft 协议，随后考察 Ratis 中的一致性模型，并详细说明相关的 API 与配置。

### 讲师:


<img src="https://cdn.sessionize.com/image/ef71-400o400o1-MpFqHHnN7VnXA2oxvNY6T.jpg" width="200" /><br/>

Tsz-Wo Nicholas Sze：首席软件工程师

Tsz-Wo Nicholas Sze 博士在 Cloudera 担任首席工程师。他是 Apache Ratis 的 PMC 主席，也是 Apache Hadoop 与 Apache Ozone 的 PMC 成员。他参与 Apache Hadoop 和 HDFS 的工作可追溯到 2007 年，是该项目为数不多、至今仍活跃的早期贡献者之一。2016 年，他发起了 Apache Ratis 项目，以支撑 Apache Ozone 中的高可用与高性能写入流水线。如今，Apache Ratis 已成为使用最广泛的 Raft Java 库之一。他于 2007 年获得马里兰大学帕克分校计算机科学博士学位。