---
title: "从数据库到实时湖仓：CDC、Kafka、Apicurio 与 Apache Iceberg"
date: ""
track: "datalake"
presenters: "Carles Arnal"
stype: "英文演讲"
---

批处理 ETL 在夜间运行。你的分析师查询的是过时数据。你的 ML 模型基于昨天的特征来训练。而流式优先（streaming-first）的湖仓用一条实时管道取代了这一切——而且你可以完全用开源工具来构建它。

在本次演讲中，我将演示一条完整的管道：Debezium 从 PostgreSQL 捕获行级变更，通过 Kafka 进行流转（其 schema 由 Apicurio Registry——一个 CNCF sandbox 项目——强制约束），最终落入 Apache Iceberg 表中——几秒钟内即可通过 Trino 或 Spark 查询。我还会讲解 Flink Dynamic Iceberg Sink 如何借助 schema registry 实现自动 schema 演进，从而消除困扰传统数据湖的手工 DDL 变更。

听众将带走：
- 一套可部署的、仅使用 Kubernetes 上开源组件的 CDC-to-Iceberg 管道架构
- 处理 Kafka 到 Iceberg 边界处 schema 演进的实用模式
- 清晰地理解这种方法何时能取代批处理 ETL，以及哪些场景下混合模式仍然合理

### 讲师:


<img src="https://cdn.sessionize.com/image/ebeb-400o400o1-nXA4VjZFgbUQrzL5Hm1DKV.jpg" width="200" /><br/>

Carles Arnal：Red Hat 软件首席工程师

Carles Arnal 是 IBM 的软件首席工程师，也是 Apicurio Registry（CNCF sandbox 项目）的核心维护者，活跃于 AI 与数据流领域。他还是 BarcelonaTech 的副教授，以及 Quarkus 的活跃 committer，拥有 10 年以上的行业经验。
