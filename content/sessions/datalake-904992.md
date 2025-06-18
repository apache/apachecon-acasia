---
title: "Apache Amoro & iceberg in Huolala Prdouction"
date: "2025-07-25T15:00:00"
room:  "WanChun Hall"
track: "datalake"
presenters: "Zheng Yu Chen"
stype: "Chinese Session"
---

At Huolala, we leveraged Apache Amoro to build a next-generation lakehouse platform with Apache Iceberg as its core. While managing petabyte-scale daily data processing, we tackled critical stability challenges, including:

Production Stability Challenges:

- Small file compaction and snapshot expiration in production
- Large-scale data migration with object storage (e.g., S3, OSS)
- Real-time monitoring & alerting for merge tasks and metadata operations
- Optimized table design to minimize small files and compaction overhead

Architectural Innovations:

- Iceberg schema & partitioning strategies tailored for logistics data
- Preventive file management to reduce merge pressure
- Automated maintenance for long-term stability

In this session, we’ll share:

Lessons learned from scaling Iceberg in a high-volume logistics platform
Key optimizations for performance and reliability
Our lakehouse journey—from PoC to production at Huolala

This talk will provide actionable insights for data engineers and architects implementing Iceberg in large-scale, real-world environments.

### Speakers:


<img src="https://sessionize.com/image/8dab-400o400o1-wspZVa98jevB6AB6cPZU8m.jpg" width="200" /><br/>

Zheng Yu Chen: Apache Amoro PPMC , HuoLaLa Senior Big Data Dev

Chen Zheng Yu (ConradJam), Apache Flink Chinese community volunteer,Apache Amoro PPMC,he  has been engaged in data development in bigdata for a long time. At present, he is responsible for the design and construction of Flink public multi-cloud data solution, data synchronization and big data operation pipeline platform from 0 to 1