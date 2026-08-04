---
title: "从数据混乱到可控：一家全球电信运营商如何用 Apache Iceberg 驯服 PB 级挑战"
date: "2026-08-08T15:00:00"
track: "streaming"
presenters: "Attila Turóczy"
stype: "英文演讲"
room: "圆明厅"
---

当一家领先的电信运营商在其老旧的 Hive 基础设施上撞到扩展瓶颈时，跨数十亿条记录管理 PB 级客户数据变得难以为继。他们的 IDPR 工作负载饱受查询缓慢、存储成本上升、分区爆炸，以及 schema 变更破坏下游系统等问题的困扰。

本次演讲将解释他们为何选择 Apache Iceberg，以及它如何改造了他们的架构，其中包括用于在其他开放表格式之间选择 Iceberg 的业务与技术决策标准。

核心收获：
为何选择 Iceberg：ACID 保证、隐藏分区（hidden partitioning）、time travel、互操作性，以及促成决策层认同的方案陈述。
架构与最佳实践：高层架构，以及 Cloudera 推荐的 Iceberg + Impala 模式、分区策略、compaction 策略、元数据优化，以及面向工作负载的查询引擎调优。
可量化的影响：更快的查询、显著的存储与基础设施成本下降、更简单的运维，以及更强的合规性。


### 讲师:

<img src="https://cdn.sessionize.com/image/457d-0o0o0-pXaRdzu6oxK2Frg1bgmVJa.jpg" width="200" /><br/>

Attila Turóczy：Cloudera 工程高级总监

在 Cloudera 致力于 Apache Hive、Impala 及大数据领域的推广。