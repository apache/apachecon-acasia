---
title: "Real-Time Lakehouse Pipeline: Native Lake Ingestion and Embedded Computation in Disaggregated Kafka"
date: ""
track: "messaging"
presenters: "Hongjian Fei"
stype: "中文演讲"
---

Apache Kafka has established itself as the central nervous system of modern real-time data architectures. Yet in conventional lakehouse designs, data from Kafka typically must traverse external compute engines such as Flink or Spark before it can be landed, modeled, and organized into analytical layers. This multi-hop "messaging → computation → storage" pipeline not only inflates operational complexity but also introduces weak state consistency, elevated end-to-end latency, and a fragmented hot/cold data lifecycle.

This talk focuses on disaggregated storage-compute architectures and explores the evolution of Kafka's native capabilities in lakehouse scenarios. We aim to restructure the real-time data pipeline through the following core techniques:

Disaggregated Storage-Compute with Intelligent Data Tiering. Built on a disaggregated storage-compute model with intelligent tiering and a lightweight high-availability architecture, we employ a dual-path Table-Topic synchronization mechanism that strikes an optimal balance between data freshness and system stability. By internalizing ingestion progress into the leader's metadata, we completely eliminate the dependency on external key-value stores, dramatically simplifying the pipeline while preserving strong consistency guarantees.

Dual Row-Columnar Engine with Strong Consistency Guarantees. Leveraging a pluggable architecture, we achieve protocol-aware parsing coupled with zero-copy direct writes in Apache Parquet columnar format — effectively turning streaming writes into immediate lakehouse persistence. A lightweight distributed transaction coordinator, integrated with an OSS-backed Table Catalog, strictly enforces Exactly-Once semantics and atomic file commits across node failures, delivering high-availability disaster recovery and autonomous state healing for the ingestion pipeline.

Embedded Declarative Stream Processing. Apache Calcite is embedded as a lightweight operator engine, enabling users to express computation logic through a SQL dialect. With operator pushdown and dynamic compilation of logical plans, filtering, aggregation, and transformation operations are executed in-situ within the Kafka pipeline, right at the data's point of origin.

### 讲师:


<img src="https://cdn.sessionize.com/image/1bd1-400o400o1-X3dGLdsBdwR23onKjs1wZj.png" width="200" /><br/>

Hongjian Fei: Alibaba Cloud, Middleware Development Engineer, Staff Engineer

Hongjian Fei (费红健) is an Apache Software Committer who has long been dedicated to development on RocketMQ and Kafka. At Alibaba Cloud, he is one of the core designers of disaggregated storage and compute architecture for Kafka, bringing extensive experience in Kafka development and operations.

