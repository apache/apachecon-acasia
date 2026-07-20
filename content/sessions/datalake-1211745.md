---
title: "Evolving a real-time lakehouse: Stability and performance breakthroughs at scale"
date: "2026-08-08T15:45:00"
track: "datalake"
presenters: "Zhuojun Jiang, Wenling Zhang"
stype: "Chinese Session"
room: "WanChun Hall"
---

As real-time data processing becomes the foundation of modern data platforms, the challenge is no longer just enabling real-time ingestion, but ensuring stability, consistency, and high performance under large-scale and high-concurrency workloads. Following our previous practice on building a real-time lakehouse, we further evolved the architecture to address critical bottlenecks in large-scale production environments.

In this session, we present a production-grade real-time lakehouse architecture based on Flink CDC 3.4, Apache Iceberg, and Apache Amoro, designed to support large-scale multi-business and highly sharded tables with second-level ingestion latency.

We redesigned the schema evolution mechanism to address performance bottlenecks and risks caused by redundant downstream writes during schema changes, achieving over 80% improvement in write efficiency. At the same time, we resolved schema consistency issues in distributed environments, significantly improving synchronization stability under high concurrency.

On the optimization side, by leveraging Apache Amoro’s adaptive refresh and zero-copy compaction mechanisms, we reduced Metastore load while achieving up to 4× improvement in file compaction performance. In addition, system robustness was enhanced through improvements in service restart and operational stability.

This session will cover two key areas:
● Distributed schema evolution and consistency guarantees for large-scale real-time ingestion
● Adaptive optimization techniques for improving performance and stability in lakehouse systems

These practices have been validated in production at telecom-scale workloads, providing a practical approach to building a high-performance and stable real-time lakehouse.

随着实时数据平台规模不断扩大，在高并发与大规模数据场景下保障系统的稳定性、一致性与高性能，成为实时湖仓建设的核心挑战。我们基于之前的实时湖仓实践，进一步对架构进行了持续演进，重点解决生产环境中的关键瓶颈问题。

本次分享将介绍一个基于 Flink CDC 3.4、Apache Iceberg 与 Apache Amoro 构建的生产级实时湖仓架构，支持多业务表、多分片场景下的秒级数据入湖能力。

在数据同步层，我们重构了 Schema Evolution 架构，消除了模式变更过程中下游重复写入带来的性能瓶颈，使写入效率提升 80% 以上。同时，针对分布式环境中的模式一致性问题进行了系统性优化，显著提升了高并发场景下的数据同步稳定性。

在数据优化层，基于 Apache Amoro 的自适应刷新与零拷贝合并机制，在显著降低 Metastore 负载的同时，实现了 4 倍的文件合并性能提升，并通过优化服务重启与运行机制进一步增强系统整体稳定性。

本次分享将重点介绍两方面实践经验：
● 面向大规模实时同步的分布式 Schema 演进与一致性保障
● 基于自适应优化机制的湖仓性能优化与系统稳定性提升

相关能力已在电信运营商生产环境中落地，支撑 PB 级数据规模，为构建高性能、高稳定性的实时湖仓提供可落地的实践路径。

### Speakers:


<img src="https://cdn.sessionize.com/image/9680-400o400o1-YG3mh3cmWmJDXyGB8CpYZy.jpg" width="200" /><br/>

Zhuojun Jiang: Senior Big Data Engineer, State Cloud

Zhuojun Jiang is a Senior Big Data Engineer at State Cloud, specializing in real-time data lakehouse architecture. She focuses on big data development, system performance optimization, and real-time data synchronization based on technologies like Apache FlinkCDC, Iceberg, and Amoro. Jiang actively contributes to the open-source community and shares practical insights through industry forums and technical talks.


<img src="https://cdn.sessionize.com/image/cc23-400o400o1-HUNA5fNUTQtYn6ZuzRMZPq.jpg" width="200" /><br/>

Wenling Zhang: StateCloud

Apache (incubating) Amoro contributor