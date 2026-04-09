---
title: '​​Building Inverted Indexes on Iceberg with Tantivy: A Hands-on Approach​​'
date: '2026-08-07T16:15:00'
room: WanChun Hall
track: datalake
presenters: Longfei Liu
stype: Chinese Session
depth: advanced
practice_level: 5
projects:
- apache iceberg
audience:
- 架构师
- 开发者
related_sessions: []
---
In big data scenarios, efficient data retrieval is a core requirement for many business applications.​​ As the cornerstone of full-text search and complex queries, inverted indexes can significantly improve query performance, particularly excelling in log analysis scenarios requiring fuzzy matching. Compared to traditional solutions, leveraging the storage scalability and compute-storage separation advantages of lakehouse table formats can effectively reduce index storage costs. However, implementing scalable, low-maintenance inverted indexes in data lake architectures using modern table formats (like Apache Iceberg) still presents multiple challenges, including real-time synchronization between indexes and data, consistency guarantees in distributed environments, and query optimization issues.

​​This presentation will share practical experiences in building a reliable inverted index system based on Apache Iceberg and Tantivy, covering the following key implementations:​​
​​1. Compatibility Analysis of Iceberg with Inverted Indexes​​
  Examining how Iceberg's ACID properties and metadata management capabilities support atomic updates and version control for indexes.
​​2. Challenges in Building Inverted Indexes with Tantivy​​
  Sharing practical approaches for data interaction with Rust and optimizing storage by pruning unnecessary files.
​​3. Integration Practices with Trino Query Engine​​
  Demonstrating how to effectively integrate the solution with Trino for enhanced query performance.

### Speakers:


<img src="https://sessionize.com/image/ef8c-400o400o1-E5oCBuuC86mqfMxuzYXMs1.png" width="200" /><br/>

Longfei Liu: ​​Senior Software Engineer​​ at ​​360 (Qihoo 360)​​

A decade of hands-on experience in big data infrastructure development, with deep expertise in distributed storage systems and query performance optimization.