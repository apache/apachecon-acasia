---
title: "From Vision to Production: How Apache Fluss Defines the Storage Layer for Real-Time Data Lakehouses"
date: ""
track: "datastorage"
presenters: "Yang Wang"
stype: "中文演讲"
---

Last year at Community Over Code Asia, we introduced Apache Fluss and its vision of a dedicated storage layer for real-time lakehouses. Several releases later, that vision has been validated in production at Alibaba's Double 11 scale.

In this talk, we present what we have delivered across three themes. First, pushing compute into storage: the Aggregation Merge Engine pushes real-time aggregation — including RoaringBitmap UV deduplication — into the storage layer with built-in exactly-once semantics, and log filter pushdown moves predicate evaluation from compute to storage, enabling Flink to offload aggregation, join, and wide-table state entirely to storage. Second, ecosystem and data model evolution: secondary indexes for flexible query patterns, Change Data Feed, complex data types, zero-copy schema evolution, and multi-language clients (Rust, Python, C++). Third, enterprise-grade foundation: goal-driven rebalance, zero-downtime rolling upgrades, fast Coordinator recovery, SASL authentication with three-level ACL, and deep RocksDB diagnostics.


### 讲师:


<img src="https://cdn.sessionize.com/image/caa5-400o400o1-7N761jmkijrU21jsU1NuAN.jpg" width="200" /><br/>

Yang Wang: Staff Engineer at Alibaba Cloud , HangZhou,  Apache Fluss Core Developer

Yang Wang is a Staff Engineer at Alibaba Cloud and a core development team member of Apache Fluss, a streaming storage system for real-time analytics. He focuses on storage engine internals — including the KV store (RocksDB integration, performance tuning, monitoring, and memory management), aggregation merge engine, secondary index support, and Flink connector enhancements such as filter pushdown and lookup joins. He is an active contributor to the Apache Fluss open-source community.

