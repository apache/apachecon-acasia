---
title: "Scaling Open Source Big Data Cloud Applications is Easy/Hard"
date: "" 
track: "bigdata"
presenters: "Paul Brebner"
stype: "English Session"
---
In the last decade, the development of modern horizontally scalable open-source Big Data technologies such as Apache Cassandra (for data storage), and Apache Kafka (for data streaming) enabled cost-effective, highly scalable, reliable, low-latency applications, and made these technologies increasingly ubiquitous. To enable reliable horizontal scalability, both Cassandra and Kafka utilize partitioning (for concurrency) and replication (for reliability and availability) across clustered servers. 

But building scalable applications isn’t as easy as just throwing more servers at the clusters, and unexpected speed humps are common. Consequently, you also need to understand the performance impact of new server types and partitions, replication, consumers, connections, etc; monitor the correct metrics to have an end-to-end view of applications and clusters; conduct careful benchmarking, and scale and tune iteratively to take into account performance insights and optimizations. 

In this presentation, Paul will explore some of the performance goals, challenges, solutions, and insights I discovered over the last 5 years of building multiple realistic demonstration applications. The examples include benchmarking and diagnosing a performance problem we encountered before releasing our managed Apache Kafka offering on AWS’s Graviton2 (ARM) instances, trade-offs and automation of elastic Cassandra auto-scaling, scaling a Cassandra and Kafka anomaly detection application to 19 Billion checks per day, understanding and mitigating the impact of Kafka partitions and replication on cluster throughput, and building low-latency streaming data pipelines using Kafka Connect.
 ### Speakers: 
 <img src="images/speaker/1043.png" width="200" /><br>Paul Brebner: Instaclustr, Chief Technology Evangelist, Paul is the Technology Evangelist at Instaclustr. He’s been learning new scalable technologies, solving realistic problems, building applications, and blogging and talking about many open source technologies including Apache Cassandra, Apache Kafka, Apache Spark, Apache Zookeeper, Redis, Elasticsearch, 
 PostgreSQL, Debezium, Cadence, and more. 
Since learning to program on a VAX 11/780, Paul has extensive R&D and consulting experience in distributed systems, technology innovation, software architecture and engineering, software performance and scalability, grid and cloud computing, and data analytics and machine learning.

Paul has worked at UNSW, several tech start-ups, CSIRO, UCL (UK), and NICTA. Paul has an MSc in Machine Learning and a BSc (Computer Science and Philosophy).
 