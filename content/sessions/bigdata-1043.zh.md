---
title: "扩展开源大数据云应用是容易/困难的"
date: "2022-07-29T15:30:00"
track: "bigdata"
room: "A"
presenters: "Paul Brebner"
stype: "英文演讲"
---
在过去的十年中，现代水平可伸缩的开源大数据技术的发展，如Apache Cassandra(用于数据存储)和Apache Kafka(用于数据流)，使成本低、高度可伸缩、可靠、低延迟的应用程序成为可能，并使这些技术越来越普遍。为了实现可靠的水平可伸缩性，Cassandra和Kafka都利用了跨集群服务器的分区(用于并发)和复制(用于可靠性和可用性)。

但是，构建可伸缩的应用程序并不像在集群中添加更多的服务器那么容易，意外的速度下降是常见的。因此，您还需要了解新的服务器类型和分区、复制、使用者、连接等对性能的影响;监控正确的指标，以获得应用程序和集群的端到端视图;进行仔细的基准测试，迭代地扩展和调优，以考虑性能洞察和优化。

在这次演讲中，Paul将探讨一些性能目标、挑战、解决方案和见解，这些是我在过去5年构建多个实际演示应用程序时发现的。这些例子包括在AWS的Graviton2 (ARM)实例上发布我们的管理Apache Kafka之前遇到的性能问题的基准测试和诊断，弹性Cassandra自动伸缩的折衷和自动化，将一个Cassandra和Kafka异常检测应用扩展到每天190亿次检查，理解和减轻Kafka分区和复制对集群吞吐量的影响，以及使用Kafka Connect构建低延迟的流数据管道。
 ### Speakers: 
 <img src="images/speaker/1043.png" width="200" /><br>Paul Brebner: Instaclustr, 首席技术专员, Paul是Instaclustr的技术布道者。他一直在学习新的可扩展技术，解决现实问题，构建应用程序，写博客，谈论很多开源技术，包括Apache Cassandra, Apache Kafka, Apache Spark, Apache Zookeeper, Redis, Elasticsearch，
PostgreSQL, Debezium, Cadence等等。
自从在VAX 11/780上学习编程以来，Paul在分布式系统、技术创新、软件架构和工程、软件性能和可伸缩性、网格和云计算、数据分析和机器学习方面拥有广泛的研发和咨询经验。

Paul曾在新南威尔士大学、几家科技初创企业、CSIRO、UCL(英国)和NICTA工作。Paul拥有机器学习硕士学位和计算机科学与哲学学士学位。

 