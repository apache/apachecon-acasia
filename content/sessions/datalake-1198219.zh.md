---
title: "优化 Apache Iceberg 性能"
date: ""
track: "datalake"
presenters: "Lester Martin"
stype: "英文演讲"
---

加入 Lester 的这场实用、节奏紧凑的演讲，一起提升数据湖仓中的查询性能。虽然我们聚焦 Apache Iceberg，但这些技术同样广泛适用于 Delta Lake 和 Apache Hive。

我们会先从作为表消费者今天就能应用的优化讲起：维护统计信息、使用高效的过滤与投影，以及利用缓存来降低延迟。

随后我们会深入底层，展示湖仓表应当如何组织与维护以提升大规模下的性能，涵盖 join 优化与文件大小考量，以及 compaction、分区、分桶（bucketing）和文件级排序。

你将学到如何：

 - 借助统计信息、过滤和投影裁剪，减少扫描的数据量并加速查询。

 - 基于最佳实践，用分区策略设计可扩展的表。

 - 通过 compaction、元数据重写与过期清理来维护表。
 
你将带走可以立即应用的实用指导——无需迁移平台。 

### 讲师:


<img src="https://cdn.sessionize.com/image/56bd-400o400o1-SLSATk91i1WkexNwQJfSCN.jpg" width="200" /><br/>

Lester Martin：Trino 开发者布道师 - Starburst

Lester Martin 是一位资深的开发者布道师、培训师、博客作者、数据工程师和多语言程序员，专注于使用 Trino、Iceberg、Hive、Spark、Flink、Kafka、NiFi、NoSQL 数据库，当然还有经典 RDBMS 构建数据管道与数据湖分析。欢迎访问 https://linktr.ee/lestermartin 了解更多关于 Lester 的信息。
