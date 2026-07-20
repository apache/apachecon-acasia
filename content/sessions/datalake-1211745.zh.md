---
title: "演进中的实时湖仓：大规模下的稳定性与性能突破"
date: "2026-08-08T15:45:00"
track: "datalake"
presenters: "Zhuojun Jiang, Wenling Zhang"
stype: "中文演讲"
room: "万春厅"
---

随着实时数据平台规模不断扩大，在高并发与大规模数据场景下保障系统的稳定性、一致性与高性能，成为实时湖仓建设的核心挑战。我们基于之前的实时湖仓实践，进一步对架构进行了持续演进，重点解决生产环境中的关键瓶颈问题。

本次分享将介绍一个基于 Flink CDC 3.4、Apache Iceberg 与 Apache Amoro 构建的生产级实时湖仓架构，支持多业务表、多分片场景下的秒级数据入湖能力。

在数据同步层，我们重构了 Schema Evolution 架构，消除了模式变更过程中下游重复写入带来的性能瓶颈，使写入效率提升 80% 以上。同时，针对分布式环境中的模式一致性问题进行了系统性优化，显著提升了高并发场景下的数据同步稳定性。

在数据优化层，基于 Apache Amoro 的自适应刷新与零拷贝合并机制，在显著降低 Metastore 负载的同时，实现了 4 倍的文件合并性能提升，并通过优化服务重启与运行机制进一步增强系统整体稳定性。

本次分享将重点介绍两方面实践经验：
● 面向大规模实时同步的分布式 Schema 演进与一致性保障
● 基于自适应优化机制的湖仓性能优化与系统稳定性提升

相关能力已在电信运营商生产环境中落地，支撑 PB 级数据规模，为构建高性能、高稳定性的实时湖仓提供可落地的实践路径。

### 讲师:


<img src="https://cdn.sessionize.com/image/9680-400o400o1-YG3mh3cmWmJDXyGB8CpYZy.jpg" width="200" /><br/>

Zhuojun Jiang：State Cloud 资深大数据工程师

Zhuojun Jiang 是 State Cloud 的资深大数据工程师，专长于实时数据湖仓架构。她专注于基于 Apache FlinkCDC、Iceberg、Amoro 等技术的大数据开发、系统性能优化和实时数据同步。她积极参与开源社区，并通过行业论坛和技术分享传播实战经验。


<img src="https://cdn.sessionize.com/image/cc23-400o400o1-HUNA5fNUTQtYn6ZuzRMZPq.jpg" width="200" /><br/>

Wenling Zhang：StateCloud

Apache（孵化中）Amoro contributor