---
title: 'Mastering Large-Scale Shuffle: The Dream11 Playbook with Remote Shuffle Service'
date: '2026-08-07T14:30:00'
room: Mtn WanShou Hall
track: datastorage
presenters: Amit Shinde, Mohit Jain
stype: English Session
depth: advanced
practice_level: 5
projects:
- apache celeborn
audience:
- 架构师
- 开发者
- SRE/运维
related_sessions:
- Supercharge Lakehouse Implementation with Apache Iceberg
- 'Elevating Data Processing: Strategies for Seamless Batch Management in Cloud Architectures'
- 'Apache Hop: Integrating LLMs, Graph Databases & Spreadsheets'
- 'Queue, Process, Predict: Kafka’s New Era with Flink LLMs and Datalake'
- The Future of ETL with Branching & Tagging in Apache Hive
---
At Dream11, Apache Celeborn is used for petabyte-scale shuffle, leveraging rack awareness to minimize cross-rack data transfer and ensure high availability by replicating shuffle data across different racks. It decouples shuffle storage from compute nodes, enabling elastic scaling of storage independent of compute demands. Parallel partition writes and adaptive shuffle reads optimize throughput and reduce latency. Elastic scaling allows dynamic resource allocation, maintaining cost efficiency under varying workloads. This design enhances fault tolerance and reduces job completion time by over 50%.

### Speakers:


<img src="https://sessionize.com/image/f103-400o400o2-UWzQTr6XwxL4WAQB6aPxgn.png" width="200" /><br/>

Amit Shinde: Technical Lead

Engineering Director at Dream11. 14+ professional experience in software engineering

<img src="https://sessionize.com/image/cb28-400o400o1-Utccibvy6GXbntEwxXRRRY.jpg" width="200" /><br/>

Mohit Jain: Technical Lead

I work at the intersection of big data and ML, making Spark and Flink faster while scaling real-time, batch, and ML workloads. Whether it's optimizing distributed computing, streamlining data pipelines, or building intuitive tools, my goal is to turn complex data challenges into seamless, high-performance solutions.