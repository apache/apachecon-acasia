---
title: "从数据混乱到可控：一家全球电信运营商如何用 Apache Iceberg 驯服 PB 级挑战"
date: "2026-08-08T16:45:00"
track: "streaming"
presenters: "Akshat Mathur, Bill Zhang"
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


<img src="https://cdn.sessionize.com/image/d598-400o400o1-TWRJCfGzVB3ZKDH85a4riC.jpg" width="200" /><br/>

Akshat Mathur：Cloudera 高级产品经理

在充满活力的数据工程领域拥有 8 年以上的专注经验，曾帮助多家组织架构并落地稳健的数据基础设施，助力其成功驾驭数据的力量，目前负责 Cloudera 数据湖仓（Data Lakehouse）的产品战略。

Akshat 还曾为 Apache Hive 和 Tez 做出过贡献。



<img src="https://cdn.sessionize.com/image/c664-400o400o1-D8zfmit88E5Ypmb4yaDdJ.jpg" width="200" /><br/>

Bill Zhang：Cloudera 产品副总裁，负责 Lakehouse 与 Iceberg 集成

Bill 是 Cloudera 的产品管理副总裁，负责开放数据湖仓（Open Data Lakehouse）的产品战略，以及 Apache Iceberg 与所有 Cloudera Data Platform（CDP）形态的集成。Bill 同时也主导 Apache Hive 的产品路线图与推广。此前不久，Bill 负责 SAP HANA Data Platform 和 SAP HANA Cloud 的方案管理。再之前，他负责 Sybase Replication Server 的产品管理。