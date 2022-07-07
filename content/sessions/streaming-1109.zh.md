---
title: "基于 Flink CDC 和 Hudi 高效地构建实时数据湖"
date: "2022-07-30T13:30:00"
track: "streaming"
presenters: "徐榜江"
stype: "中文演讲"
---
数据库中的业务数据是最有价值的数据之一，如何有效地将这些数据高效地同步到数据湖中是一个非常有价值的主题。
CDC（Change Data Capture）是用于从数据库中捕获变更的技术，Flink CDC 是实时数据集成框架的开源代表，具有全增量一体化、无锁读取、并发读取、分布式架构等技术优势，在开源社区中非常受欢迎。除了具备实时入湖入仓能力，Flink CDC 还支持强大的数据加工能力，可以通过 SQL 对数据库数据做实时关联、聚合、打宽等, 配合 Flink 丰富的下游生态可以将加工后的数据方便地写入 Kafka、Hudi、Iceberg 、Doris等下游。

在本次分享中，徐榜江老师首先会分享 Flink CDC 的无锁算法、并行读取、断点续传和分布式架构等核心设计和实现，并结合具体的业务场景，分享Flink CDC 在不同场景中的应用，然后配合 demo 详细介绍如何基于 Flink CDC 和 Hudi 高效地完成实时数据湖构建。
 ### Speakers: 
 <img src="images/speaker/1109.png" width="200" /><br>徐榜江: 阿里云, 高级研发工程师, Apache Flink Committer & Flink CDC Maintainer， 专注在Flink SQL，Flink CDC，数据集成领域，曾在国内外多次演讲和分享Apache Flink， Flink CDC 相关技术。
https://github.com/apache/flink
https://github.com/ververica/flink-cdc-connectors

 