---
title: "使用 Apache NiFi 和 Polaris 进行 Apache Iceberg 数据采集"
date: ""
track: "streaming"
presenters: "Lester Martin"
stype: "英文演讲"
---

基于 Iceberg 的数据湖的一项基本要求是数据采集。一种方法是利用 Apache NiFi。NiFi 是一款多模态数据流水线工具，拥有众多处理器，可以组合成一个流程，以满足您的特定场景。NiFi 的低代码/无代码方法使数据工程师能够快速构建、部署和监控其数据采集和转换流水线。NiFi 还支持使用多种语言（包括 Java 和 Python）进行自定义处理器开发。

本演示将介绍几种常用方法，最终演示一个丰富的数据流水线，该流水线从 Kafka 获取数据，执行典型的转换处理（包括数据丰富），并将数据加载到高性能 Iceberg 表中，该表将通过流行的查询引擎使用并通过 Apache Polaris REST 目录访问。

### 讲师:

<img src="https://sessionize.com/image/7ced-400o400o1-nQpjeSxnTeKrZ8WmXy1V7q.jpg" width="200" /><br/>

Lester Martin

Lester Martin 是一位经验丰富的开发倡导者、培训师、博主和数据工程师，专注于使用 Trino、Iceberg、Hive、Spark、Flink、Kafka、NiFi、NoSQL 数据库以及经典关系型数据库管理系统 (RDBMS) 进行数据管道和数据湖分析。访问 Lester 的博客：https://lestermartin.blog。