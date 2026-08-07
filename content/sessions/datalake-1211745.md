---
title: "Evolving a real-time lakehouse: Stability and performance breakthroughs at scale"
date: "2026-08-08T15:45:00"
track: "datalake"
presenters: "Zhuojun Jiang, Wenling Zhang"
stype: "Chinese Session"
room: "MainRoom - YiHe Hall"
---

As real-time data processing becomes the foundation of modern data platforms, the challenge is no longer just enabling real-time ingestion, but ensuring stability, consistency, and high performance under large-scale and high-concurrency workloads. Following our previous practice on building a real-time lakehouse, we further evolved the architecture to address critical bottlenecks in large-scale production environments.

In this session, we present a production-grade real-time lakehouse architecture based on Flink CDC 3.4, Apache Iceberg, and Apache Amoro, designed to support large-scale multi-business and highly sharded tables with second-level ingestion latency.

We redesigned the schema evolution mechanism to address performance bottlenecks and risks caused by redundant downstream writes during schema changes, achieving over 80% improvement in write efficiency. At the same time, we resolved schema consistency issues in distributed environments, significantly improving synchronization stability under high concurrency.

On the optimization side, by leveraging Apache Amoro’s adaptive refresh and zero-copy compaction mechanisms, we reduced Metastore load while achieving up to 4× improvement in file compaction performance. In addition, system robustness was enhanced through improvements in service restart and operational stability.

This session will cover two key areas:

- Distributed schema evolution and consistency guarantees for large-scale real-time ingestion
- Adaptive optimization techniques for improving performance and stability in lakehouse systems

These practices have been validated in production at telecom-scale workloads, providing a practical approach to building a high-performance and stable real-time lakehouse.

### Speakers:


<img src="https://cdn.sessionize.com/image/9680-400o400o1-YG3mh3cmWmJDXyGB8CpYZy.jpg" width="200" /><br/>

Zhuojun Jiang: Senior Big Data Engineer, State Cloud

Zhuojun Jiang is a Senior Big Data Engineer at State Cloud, specializing in real-time data lakehouse architecture. She focuses on big data development, system performance optimization, and real-time data synchronization based on technologies like Apache FlinkCDC, Iceberg, and Amoro. Jiang actively contributes to the open-source community and shares practical insights through industry forums and technical talks.


<img src="https://cdn.sessionize.com/image/cc23-400o400o1-HUNA5fNUTQtYn6ZuzRMZPq.jpg" width="200" /><br/>

Wenling Zhang: Senior Big Data Engineer, State Cloud

Apache (incubating) Amoro contributor