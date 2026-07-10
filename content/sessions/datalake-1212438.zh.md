---
title: "在 C++ 查询引擎中实现 Iceberg 特性的挑战"
date: ""
track: "datalake"
presenters: "Zoltán Borók-Nagy, Péter Rózsa"
stype: "英文演讲"
---

Apache Impala 是一个混合的大规模并行查询引擎：它的查询规划和元数据处理由 Java 实现，而执行引擎则用 C++ 编写。这种架构在集成 Apache Iceberg 时会带来独特的挑战——因为 Iceberg 的参考实现与生态主要以 Java 为基础。听众将了解到把 Iceberg 引入非 JVM 查询引擎时所面临的实际挑战。

我们将探讨 Iceberg 的特性如何在一个分布式 C++ 查询引擎中实现，以及 Impala 在哪些地方可以复用现有的 Iceberg 库、哪些地方又需要自定义实现。我们会深入具体案例，包括元数据处理和行级操作。本次演讲还会强调这种模式所带来的机遇，例如重新思考 merge-on-read 的实现方式。

最后，听众还将了解 Impala 对 Iceberg 支持的现状，以及我们朝着采用 Iceberg V3 所取得的进展。

### 讲师:


<img src="https://cdn.sessionize.com/image/84b3-400o400o1-7GoTobWcFvV4kLv5UvF1Mn.jpg" width="200" /><br/>

Zoltán Borók-Nagy：Cloudera，Principal Engineer

Zoltán 是 Cloudera 的软件工程师，从事 Apache Impala 相关工作。他也是该项目的 PMC 成员。目前他负责牵头 Impala/Iceberg 的集成工作。在加入 Cloudera 之前，Zoltán 从事 C++ 静态分析工具的开发。他感兴趣的方向包括分布式系统、大规模并行系统、数据库以及性能工程。


<img src="https://cdn.sessionize.com/image/0f03-400o400o1-VjFuA65v8Md5uQxrNPHre2.jpg" width="200" /><br/>

Péter Rózsa：Cloudera，软件工程师

Péter Rózsa 自 2020 年起在 Cloudera 担任软件工程师，于 2022 年开始为 Apache Impala 做贡献。他参与过 Impala 项目的多个部分，最近主要专注于 Iceberg 集成相关工作。
