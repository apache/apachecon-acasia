---
title: "使用 Apache Arrow 重塑 OpenTelemetry"
date: ""
track: "webserver"
presenters: "Lei Huang"
stype: "英文演讲"
---

OpenTelemetry 是一个广泛采用的开源标准，用于构建可观测性框架，提供用于生成、收集和导出遥测数据（例如指标、日志和轨迹）的工具、API 和 SDK。然而，其传输协议依赖于 Protocol Buffer 消息，这些消息无状态且易于解释，但其基于行的结构使压缩变得复杂。当跨网络边界传输大量数据时，这种限制会更加明显。

在我的演讲中，我将提出一项提案，通过使用 Apache Arrow（简称 OTel-Arrow）增强 OpenTelemetry 协议来解决这个问题。该计划旨在利用 Apache Arrow 在 OpenTelemetry 管道中进行批量数据压缩和传输。我们将讨论 OTel-Arrow 数据模型、已实现该模型的现有基础设施、将 OTel-Arrow 与原始实现进行比较的基准测试结果，以及我们使用 Apache Parquet 格式将 OTel-Arrow 集成到现代时间序列数据库中，以通过基于 Apache DataFusion 构建的实时查询引擎实现快速分析。

### 讲师:

<img src="https://sessionize.com/image/4df2-400o400o1-EVUc7f9M53frxPdweN8rwZ.jpg" width="200" /><br/>

Lei Huang: 中国杭州 Greptime 数据库开发人员

Lei 是一位来自中国的热情开源数据库开发者。在北京大学获得计算机科学硕士学位后，他加入支付宝，从事基础设施和中间件开发工作，并领导开发了用于交易处理的大规模消息队列。后来，他作为创始成员加入 Greptime，主要负责存储引擎的开发。他的主要兴趣是分布式系统和数据库存储子系统。