---
title: 'Resolving Data Silos: Apache Gravitino''s Production Implementation Practices
  at Bilibili'
date: '2026-08-09T14:00:00'
room: WanChun Hall
track: datalake
presenters: Tianhang Li
stype: Chinese Session
depth: advanced
practice_level: 5
projects:
- apache gravitino
- hive
- iceberg
- kafka
audience:
- 架构师
- 开发者
- SRE/运维
related_sessions:
- Apache Gravitino, the answer of metadata management in AI era
- Xiaomi's Efficient Data & AI Optimization with Apache Paimon
- Apache Gravitino Best Practices for Multi-Cluster Management
- 'From Data to AI: Building a Unified Analytics Platform with Apache Cloudberry'
- 'Catalogs as Context: Using metadata to power and govern the next wave of AI development'
---
Apache Gravitino is a unified metadata management platform adopted by Bilibili to address data silos, enabling metadata view integration across heterogeneous data sources such as Hive, Iceberg, Kafka and so on. Leveraging ​end-to-end lineage tracking, it traces data workflows from ingestion, processing, to service delivery, optimizing resource utilization and impact analysis of schema changes. By integrating Iceberg's partitioning strategies (e.g., Truncate/Bucket) and Branch features, Gravitino supports flexible data versioning, multi-stream data stitching, and isolated testing environments. For AI-driven scenarios, the platform provides systematic ​training dataset partitioning and model version management, ensuring reproducibility and streamlined AI asset governance. This solution reduces cross-source maintenance overhead, enhances data consistency, and establishes a scalable technical foundation for Bilibili's AI applications and enterprise-wide data governance

### Speakers:


<img src="https://sessionize.com/image/1f8c-400o400o1-HBNHNwxpA2kUNRMibne31Z.jpg" width="200" /><br/>

Tianhang Li: "Big Data Development Engineer at Bilibili | Apache Gravitino Contributor | Expert in Metadata Management & Spark Optimization"

Li Tianhang is a Big Data Development Engineer at Bilibili, where he specializes in metadata management and Spark computing engine optimization for large-scale data scenarios