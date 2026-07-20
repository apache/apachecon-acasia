---
title: "Paimon-cpp: Bringing Native High-Performance Data Lakehouse Access to the Apache Ecosystem"
date: "2026-08-08T15:00:00"
track: "datastorage"
presenters: "Xinyu Liu"
stype: "Chinese Session"
room: "Mtn WanShou Hall"
---

Apache Paimon has become one of the most actively developed data lakehouse formats in the Apache ecosystem. As native query engines increasingly demand direct access to lakehouse data without JVM overhead, we are excited to introduce Paimon-cpp — a high-performance, ground-up C++ implementation of the Apache Paimon format, in the process of being contributed to the Apache Paimon community.

In this session, we will walk through:

- **Why Paimon-cpp**: The motivation behind building a native C++ implementation — bridging the gap between JVM-based data lake ecosystems and the growing world of native query engines, while maintaining full wire-compatibility with Java Paimon.

- **Format & Features**: Paimon-cpp provides full read/write/compaction support for both append tables and primary key tables, including Merge-On-Read (MOR) and Deletion Vector (DV) scenarios. It also supports schema evolution, predicate push-down, AI-oriented data evolution mode, and various index types (e.g., vector search, full text search).

- **Performance Optimizations**: Shallow data copy data exchange, file prefetching for read-ahead, multi-threaded & asynchronous row-columnar conversion for primary key tables, and Blob I/O optimizations.

- **Architecture & Extensibility**: Built on the Apache Arrow Columnar In-Memory Format, with a modular, plugin-oriented architecture providing well-defined interfaces for file systems, file formats, memory management, executors, and observability — designed to be easily embedded into any native engine.

- **Best Practices & Getting Started**: Practical guidance on configuring write/read/compaction pipelines, tuning for production workloads, and integrating Paimon-cpp into your own engine.

Paimon-cpp is being actively contributed to the Apache Paimon project and is expected to be part of the official Apache repository by the time of this talk. We warmly welcome developers, engine builders, and data enthusiasts to try it out, report issues, and contribute — whether it's new features, bug fixes, documentation, or integration with your favorite native engine. Let's build the native data lakehouse ecosystem together!

### Speakers:


<img src="https://cdn.sessionize.com/image/581f-400o400o1-wHvbmZBcWsHGkZircGN71i.jpg" width="200" /><br/>

Xinyu Liu: Senior Software Engineer at Alibaba | Maintainer of Paimon-cpp | 3 Years with Paimon

I am a Senior Software Engineer on the Storage Service team at Alibaba. I have been working on Paimon-cpp for 3 years, currently serving as the maintainer of the Paimon-cpp open-source library and leading the adoption of Paimon-cpp across Alibaba's internal data infrastructure. Prior to Paimon, I was responsible for Khronos, a time-series database that powers the monitoring system storage and retrieval for Alibaba Group. My experience spans storage engine design, high-performance data formats, and systems-level optimization. I am passionate about open-source collaboration and look forward to building the native data lakehouse ecosystem together with the Apache community.