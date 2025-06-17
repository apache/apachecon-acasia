---
title: "Apache Iceberg ingestion with Apache NiFi and Polaris"
date: ""
track: "streaming"
presenters: "Lester Martin"
stype: "English Session"
---

A cornerstone requirement of an Iceberg-based data lakehouse is data ingestion. One approach is to leverage Apache NiFi. NiFi, a multimodal data pipelining tool, has a multitude of processors that can be assembled into a flow to address your specific scenarios. NiFi's low-code/no-code approach allows data engineers to rapidly build, deploy, and monitor their data ingestion & transformation pipelines. NiFi also allows custom processor development with a variety of languages, including Java and Python.

This presentation will iterate through a few common approaches and ultimately demonstrate a rich data pipeline that sources data from Kafka, performs typical transformation processing (including enrichment), and loads data into a high-performance Iceberg table that will be consumed via popular query engines and accessed via an Apache Polaris REST catalog.

### Speakers:


<img src="https://sessionize.com/image/7ced-400o400o1-nQpjeSxnTeKrZ8WmXy1V7q.jpg" width="200" /><br/>

Lester Martin: Trino Developer Advocate - Starburst

Lester Martin is a seasoned developer advocate, trainer, blogger, and data engineer focused on data pipelines & data lake analytics using Trino, Iceberg, Hive, Spark, Flink, Kafka, NiFi, NoSQL databases, and, of course, classical RDBMSs.  Check out Lester's blog at https://lestermartin.blog.
