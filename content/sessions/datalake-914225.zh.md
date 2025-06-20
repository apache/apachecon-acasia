---
title: "Impala 在 Iceberg 上与 Puffins"
date: "2025-07-26T14:30:00"
room:  "万春厅"
track: "datalake"
presenters: "Daniel Becker"
stype: "英文演讲"
---

Apache Iceberg 表格式已成为大数据领域的事实标准。与基于传统文件系统的表格式相比，它拥有诸多优势，例如行级修改、事务、分区转换和时间旅行，使其成为许多项目自然而然的首选。数据统计

信息可以极大地帮助数据库引擎创建高效的查询计划。作为领先的表格式，Iceberg 旨在提供一种标准化的方式来存储这些统计信息：除了核心规范中已有的文件级属性（例如最小值和最大值）之外，它还引入了 Puffin 文件格式来存储整个表的统计信息。通过使用 Puffin 格式，各种数据库引擎可以共享统计信息，而无需每个引擎都计算和存储自己的版本，从而使多引擎工作流程更简单、更高效。

本次演讲将向您展示我们如何在 Apache Impala（一个开源、分布式、大规模并行数据库引擎）中引入对 Puffin 统计信息的支持。我们将介绍实现的所有阶段，从仅读取为最新快照计算的统计数据，到优化读取性能，再到考虑较旧快照中缺失的统计数据（较新的快照中缺失）。我们将讨论一个特别有趣的点，即当统计数据来自多个来源时，如何选择最相关的统计数据：这些来源包括 Puffin 文件和 Impala 的传统统计数据来源 Hive Metastore。

### 讲师:

<img src="https://sessionize.com/image/6933-400o400o1-72rRP3UXJeo1bZhvM4bFDm.jpg" width="200" /><br/>

Daniel Becker: 高级软件工程师

Daniel Becker 于 2019 年开始在 Cloudera 从事 Apache Impala 工作。他为 Impala 做出的贡献涵盖多个主题，包括 LLVM 代码生成、复杂类型、Parquet 和 Iceberg。他是 Apache Impala PMC 成员，拥有帕兹马尼彼得天主教大学的学位