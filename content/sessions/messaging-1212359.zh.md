---
title: "实时湖仓管道：分离式 Kafka 中的原生入湖与内嵌计算"
date: "2026-08-09T13:30:00"
track: "messaging"
presenters: "Hongjian Fei"
stype: "中文演讲"
room: "静宜厅"
---

Apache Kafka 已经成为现代实时数据架构的中枢神经。然而在传统的湖仓设计中，来自 Kafka 的数据通常必须先经过 Flink 或 Spark 等外部计算引擎，才能被落库、建模并组织成分析层。这种多跳的"消息 → 计算 → 存储"管道不仅推高了运维复杂度，还带来了状态一致性较弱、端到端时延升高、冷热数据生命周期割裂等问题。

本次演讲聚焦于存储计算分离架构，探讨 Kafka 原生能力在湖仓场景下的演进。我们希望通过以下核心技术来重塑实时数据管道：

存储计算分离与智能数据分层。建立在存储计算分离模型之上，结合智能分层与轻量级高可用架构，我们采用了双路径 Table-Topic 同步机制，在数据新鲜度与系统稳定性之间取得最佳平衡。通过将摄入（ingestion）进度内化到 leader 的元数据中，我们彻底消除对外部 KV 存储的依赖，在保持强一致性保证的同时极大简化了管道。

具备强一致性保证的行列双引擎。借助可插拔架构，我们实现了协议感知（protocol-aware）的解析，并结合 Apache Parquet 列式格式的零拷贝直写——有效地把流式写入转化为即时的湖仓持久化。一个轻量级的分布式事务协调器与基于 OSS 的 Table Catalog 相结合，在节点故障情况下严格保证 Exactly-Once 语义与原子文件提交，为摄入管道提供高可用容灾与自主状态自愈能力。

内嵌的声明式流处理。我们将 Apache Calcite 作为轻量级算子引擎内嵌进来，让用户可以通过一种 SQL 方言来表达计算逻辑。借助算子下推与逻辑计划的动态编译，过滤、聚合和转换操作可直接在 Kafka 管道中、在数据的产生处就地执行。

### 讲师:


<img src="https://cdn.sessionize.com/image/1bd1-400o400o1-X3dGLdsBdwR23onKjs1wZj.png" width="200" /><br/>

Hongjian Fei：阿里云，中间件开发工程师，Staff Engineer

Hongjian Fei（费红健）是一位 Apache 软件基金会 Committer，长期致力于 RocketMQ 与 Kafka 的开发。在阿里云，他是 Kafka 存储计算分离架构的核心设计者之一，在 Kafka 的开发与运维方面经验丰富。