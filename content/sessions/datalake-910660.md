---
title: "Unified Data Lake Real-Time Integration: Decoding SeaTunnel’s Architectural Support for Hudi / Icebe"
date: "2025-07-27T16:45:00"
room:  "WanChun Hall"
track: "datalake"
presenters: "Lidong Dai"
stype: "English Session"
---

Abstract:
With the ongoing evolution of lakehouse architectures and real-time data lakes, enterprises increasingly require a unified, high-performance, and scalable data integration framework to support both writing to and reading from multiple data lake formats such as Apache Hudi, Iceberg, and Paimon.
As a next-generation data integration engine, Apache SeaTunnel leverages its Connector V2 architecture and stream-batch unified design to build deep integration support for these three mainstream data lake formats. It provides key capabilities such as batch ingestion, real-time streaming writes, and consistency guarantees.

Outline:
1. SeaTunnel Architecture and Runtime Mechanism

Stream-batch unified architecture design philosophy
Connector V2 plugin registration, runtime loading, and lifecycle management
Support for nearly 200 data sources, covering databases, object storage, message queues, data lakes, and more

2. Overview of Data Lake Support: Feature Comparison of Hudi / Iceberg / Paimon

Differences in write mechanisms among the three formats

SeaTunnel’s unified handling strategy and connector abstraction capability

3. Detailed Architecture Support for Iceberg in SeaTunnel

4. Streaming Integration Support for Apache Hudi

5. Seamless Integration Practices with Apache Paimon

6. Case Study: Enterprise-Grade Real-Time Lakehouse Implementation

Building a real-time product data warehouse with MySQL CDC → SeaTunnel → Iceberg

7. Future Outlook and Ecosystem Integration
Plans for supporting DeltaLake and more

### Speakers:


<img src="https://sessionize.com/image/a63f-400o400o1-TAZzBju9ZdRb4umYVxMo2D.png" width="200" /><br/>

Lidong Dai: WhaleOps Technology co-founder

Apache Incubator Mentor, Apache DolphinScheduler PMC Chair & Apache SeaTunnel PMC member