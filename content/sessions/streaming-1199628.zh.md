---
title: "Unifying Message Streaming and Data Lake: How We Built a Streaming Lakehouse Engine on Apache Pulsar"
date: ""
track: "streaming"
presenters: "Dawei Zhang"
stype: "中文演讲"
---

As organizations increasingly demand real-time analytics on streaming data, the gap between message streaming systems and data lakes becomes a critical bottleneck. BiFang is a streaming lakehouse engine built on top of Apache Pulsar that bridges this gap by deeply integrating Apache Iceberg, Apache Arrow (Flight RPC), and RocksDB KV storage.
In this talk, we will share how we extended Apache Pulsar's Broker architecture — without forking the core — to achieve unified streaming and lakehouse storage. Key topics include:
Delta Manifest Pipeline: How we generate and commit Iceberg Delta Manifests in real-time as messages flow through Pulsar, enabling sub-second data visibility in the data lake.
Arrow Flight Data Channel: How we built a high-performance columnar data read path using Arrow Flight gRPC, supporting zero-copy server-side column pruning that reduces network bandwidth by 85%+.
Two-Phase Tiered Storage: How we offload Pulsar Ledger data from AVRO_BLOCK to Parquet format using a Rust JNI Parquet Writer, achieving seamless integration with Spark, Flink, and Trino.
KV Storage with RocksDB: How we implemented primary key deduplication and CDC Changelog generation on the Broker side, enabling upsert semantics on streaming tables.

We will also share lessons learned from running BiFang in production at scale, including  threading model design, and protocol extension strategies for Apache Pulsar.
Attendees will learn practical patterns for building lakehouse capabilities on top of existing messaging systems, and gain insights into the future of streaming-lakehouse convergence.

### 讲师:


<img src="https://cdn.sessionize.com/image/e808-400o400o1-X3wB9Mg1L6DccyMb45ienS.png" width="200" /><br/>

Dawei Zhang: Tencent

Dawei Zhang is a softerware engineer  at Tencent, focusing on messaging and streaming infrastructure. He is a committer to Apache Pulsar and the creator of BiFang — a streaming lakehouse engine that unifies message streaming and data lake storage. He has extensive experience in distributed systems, real-time data processing, and open-source community development.

