---
title: "Apache Pulsar 的湖仓一体方案：Pulsar 的 Lakehouse 分层存储集成详解"
date: "2022-07-31T14:10:00"
track: "messaging"
room: "A"
presenters: "陈航"
stype: "中文演讲"
---
Apache Pulsar 是一种用于缓存数据并在不同系统之间解耦的消息总线。为了支持长期的主题数据存储，我们引入了分层存储，将冷数据卸载到分层存储中，例如 GCS、S3、HDFS 等。但是，当前卸载的数据是由 Pulsar 管理的非开放格式数据，是原始的数据格式，且只有 Pulsar 可以访问数据。因此很难将其与其他大数据组件集成，例如 Presto、Flink SQL 和 Spark SQL。

为了解决这个问题，我们引入了 Lakehouse 来管理卸载数据，并与当前的主题冷数据卸载机制集成。我们可以使用 Lakehouse 提供的所有功能，例如事务支持、Schema 强制和 BI 支持等。

我们会根据数据位置从 BookKeeper 或分层存储中读取数据，进行流数据读取。由于 Lakehouse 的开放存储格式，我们可以支持 Lakehouse 所维持的各种生态系统读取数据。

为了支持流卸载并使卸载机制更具可扩展性，我们引入了按 reader 卸载机制来从主题中读取数据并写入分层存储。

此外，我们还可以通过 offloader 提供压缩服务后端，并将主题作为表。键的每个更新操作都被转换为表的 upsert 操作。

 ### Speakers: 
 <img src="images/speaker/1188.png" width="200" /><br>陈航：StreamNative 高级工程师，Apache Pulsar PMC member，他专注于 Pulsar 存储模型，包括 BookKeeper、分层存储与  Lakehouse.

 