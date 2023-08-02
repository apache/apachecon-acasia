---
title: "阿里云基于 Flink CDC 的实时数据集成实践"
date: "2023-08-19T13:30:00" 
track: "streaming"
presenters: "阮航"
stype: "中文演讲"
---
CDC（Change Data Capture）是用于从数据库中捕获变更的技术，Flink CDC 是实时数据集成框架的开源代表，具有全增量一体化、无锁读取、并发读取、分布式架构等技术优势，在开源社区中非常受欢迎。
Flink CDC 支持强大的数据加工能力，可以通过 SQL 对数据库数据做实时关联、聚合、打宽等, 配合 Flink 丰富的下游生态可以将加工后的数据方便地写入 Kafka、Hudi、Iceberg 、Doris等下游，实现数据实时入湖入仓。
在本次分享中，我们将首先会介绍 Flink CDC 技术的核心设计和关键实现，详细讲解 2.4.0 版本的新特性。然后结合具体的业务场景，分享阿里云内部 Flink CDC 在不同场景针对业务痛点的解决方案，如入湖入仓场景，Binlog过期问题等。
 ### Speakers: 
<img src="https://img.bagevent.com/resource/20230616/1746465060.jpg" width="200" /><br>
阮航 阿里云高级研发工程师, Flink CDC Maintainer & Apache Flink Contributor
 <br><br>