---
title: "深入剖析 Flink CDC 架构与大规模生产实践"
date: "2026-08-09T13:30:00"
track: "streaming"
presenters: "Yanquan Lv"
stype: "中文演讲"
room: "圆明厅"
---

同步数百个数据库和数万张表、追踪 schema 变更、连接异构系统——这些都是企业实时数据集成中常见的痛点。Flink CDC 引入了一套全新的 Pipeline 架构，能够实现声明式的多表同步、自动 schema 变更追踪，以及一站式的数据转换。在 Pipeline 架构之外，Flink CDC 3.6 还新增了对 Flink 2.2 的支持，并与主流数据库（MySQL、PostgreSQL、Oracle）以及湖仓系统（Iceberg、Paimon、Hudi）实现了无缝集成。本次演讲将深入讲解 Pipeline 架构设计，并分享来自真实生产环境中大规模实时数据湖入湖实践的性能调优与生产部署经验，帮助听众构建可靠、可维护的企业级实时数据管道。

### 讲师:


<img src="https://cdn.sessionize.com/image/8ad5-400o400o1-T4JMvFAt2aBLBUHbfHNPzt.jpg" width="200" /><br/>

Yanquan Lv：Apache Flink Committer

我是 Apache Flink Committer，也是 Flink CDC 项目的主要维护者。
我目前在阿里云开源大数据团队工作，专注于实时数据同步与流批一体处理。我曾帮助众多企业落地大规模实时数据湖入湖方案，在分布式系统与实时计算方面经验丰富。