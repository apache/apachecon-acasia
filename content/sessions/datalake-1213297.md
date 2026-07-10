---
title: "Evolution to Lakehouse: Cost-Effective Hive Migration and Real-Time Ingestion at Scale"
date: ""
track: "datalake"
presenters: "Hangxiang Yu"
stype: "Chinese Session"
---

At Didi, scaling our Hive ecosystem to Iceberg required rebuilding our strategy of data integrity and governance beyond simple format conversion. We engineered a zero-downtime offline migration strategy using a snapshot-based approach, enabling consistency checks and instant rollbacks before cutover. To tackle metadata bloat and orphan files, we also integrated Apache Amoro for autonomous optimization.

Building on this foundation, we extended our architecture to real-time scenarios. By streamlining the ingestion pipeline with Iceberg, we reduced data latency from hourly to minute-level. This unified approach not only simplified ETL pipelines but also saved petabytes of storage and significantly cut computing costs. 

This session offers actionable insights into building a stable, high-performance Lakehouse in production.

### Speakers:


<img src="https://cdn.sessionize.com/image/d20f-400o400o1-WrCCe8TfkfC32qDkTEEfSN.jpg" width="200" /><br/>

Hangxiang Yu: Apache Flink Committer & Real-Time Computing Team Lead at Didi

Hangxiang Yu is an Apache Flink Committer and currently leads the real-time computing engineering team at Didi. With years of hands-on practice in distributed systems and storage, he manages Didi's real-time infrastructure, including Apache Flink, data ingestion pipelines, and P0-level real-time data warehousing. He is also focused on advancing Didi's Lakehouse architecture, working to improve data freshness, optimize infrastructure costs, and build self-managing governance capabilities.

