---
title: "Fluss X Lakehouse: Unlocking Sub-Second Data Freshness on Your Data Lake"
date: "2026-08-08T16:15:00"
track: "datalake"
presenters: "Yuxia Luo"
stype: "Chinese Session"
room: "WanChun Hall"
---

Modern data platforms are torn between two worlds: streaming systems deliver fresh data but lack long-term
  storage, while lakehouses provide durable analytics but can't serve truly real-time queries. For primary-key
  tables, this gap is especially painful — Paimon requires compaction before new rows become visible, and Iceberg
  accumulates equality delete files that cripple query performance.

  Apache Fluss (incubating) closes this gap as a dedicated streaming storage layer that unifies with the lakehouse.
  In this talk, we'll walk through:

  - The Tiering Service that continuously syncs data from Fluss to Paimon, Iceberg, and Hudi
  - Union Read, which transparently merges real-time Fluss data with historical lake data in a single query
  - How Fluss leverages its native primary-key index to generate Deletion Vectors during tiering, eliminating the
  compaction bottleneck in Paimon and the equality-delete overhead in Iceberg
  - A live end-to-end demo using Fluss + Iceberg/Paimon + DuckDB, showing sub-second freshness on primary-key tables

  We'll close with the roadmap: multi-engine Union Read (Spark, Trino, StarRocks), broader lake support (Hudi,
  Delta), and heterogeneous tiering within a single Fluss cluster.

### Speakers:


<img src="https://cdn.sessionize.com/image/ca53-400o400o1-WCz7bXLtTwAYYZGVPMgNLv.png" width="200" /><br/>

Yuxia Luo: Apache Fluss PMC | Software Engineer @ Alibaba

Yuxia Luo is a software engineer at Alibaba and a PMC member of Apache Fluss, working on streaming
  storage and its convergence with modern lakehouse formats. He drives features around Tiering, Union Read, and
  real-time queryability for primary-key tables across Paimon, Iceberg. With years of experience on Apache
   Flink and large-scale real-time data platforms, he is passionate about closing the gap between streaming and the
   data lake. He has previously shared his work at Flink Forward and QCon.