---
title: "统一消息流与数据湖：我们如何在 Apache Pulsar 之上构建流式湖仓引擎"
date: "2026-08-09T14:00:00"
track: "streaming"
presenters: "Dawei Zhang"
stype: "中文演讲"
room: "圆明厅"
---

随着组织对流数据实时分析的需求日益增长，消息流系统与数据湖之间的鸿沟已成为一个关键瓶颈。BiFang 是一个构建在 Apache Pulsar 之上的流式湖仓引擎，通过深度集成 Apache Iceberg、Apache Arrow（Flight RPC）以及 RocksDB KV 存储，弥合了这一鸿沟。
在本次演讲中，我们将分享如何在不对核心进行 fork 的前提下扩展 Apache Pulsar 的 Broker 架构，实现流与湖仓的统一存储。关键话题包括：
Delta Manifest 管道：我们如何在消息流经 Pulsar 时实时生成并提交 Iceberg Delta Manifest，使数据湖中的数据达到亚秒级可见。
Arrow Flight 数据通道：我们如何使用 Arrow Flight gRPC 构建高性能的列式数据读取路径，支持服务端零拷贝列裁剪，从而将网络带宽消耗降低 85% 以上。
两阶段分层存储：我们如何使用 Rust JNI Parquet Writer 将 Pulsar Ledger 数据从 AVRO_BLOCK 卸载为 Parquet 格式，实现与 Spark、Flink 和 Trino 的无缝集成。
基于 RocksDB 的 KV 存储：我们如何在 Broker 侧实现主键去重和 CDC Changelog 生成，从而在流式表上支持 upsert 语义。

我们还将分享在大规模生产环境中运行 BiFang 所积累的经验教训，包括线程模型设计，以及针对 Apache Pulsar 的协议扩展策略。
听众将学到在现有消息系统之上构建湖仓能力的实用模式，并对流与湖仓融合的未来趋势获得洞见。

### 讲师:


<img src="https://cdn.sessionize.com/image/e808-400o400o1-X3wB9Mg1L6DccyMb45ienS.png" width="200" /><br/>

Dawei Zhang：腾讯

Dawei Zhang 是腾讯的软件工程师，专注于消息与流式基础设施。他是 Apache Pulsar 的 committer，也是 BiFang 的创建者——BiFang 是一个统一消息流与数据湖存储的流式湖仓引擎。他在分布式系统、实时数据处理以及开源社区发展方面拥有丰富经验。