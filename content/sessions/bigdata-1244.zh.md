---
title: "在Kubernetes集群上使用Livy会话执行交互式数据工程工作负载"
date: "2022-07-30T16:50:00"
track: "bigdata"
room: "B"
presenters: "Anmol Chaturvedi, Haripriya Bendapudi, Praneet Sharma"
stype: "英文演讲"
---
最近，对时间关键的短期交互spark工作负载的需求急剧增长。一个常见的用例是数据准备，其中通过与数据子集(数据工作表)进行spark驱动的交互来构建数据集成步骤的管道，并实时可视化转换数据响应。然后，这个交互式spark查询配方被发布出来，应用于超大规模的pb级数据。

Informatica通过与托管的Kubernetes集群上的Apache Livy的深度集成来支持这些用例。本节将详细介绍Apache Livy SDK支持并发异步提交spark代码片段(语句)的增强。该框架的深入研究将涵盖Livy服务器作为Kubernetes服务的惰性部署，在客户端代理应用程序中进行的优化以实现亚秒查询分派，以及一个新的基于Java *CompletableFuture*的用于异步查询监控和结果检索的侦听器。在本次演讲中，我们还将讨论该框架如何优先排序并支持快速故障调度模式，而不是像传统的批处理工作流需求，如作业恢复、集群状态正确性和懒惰作业资源可用性等。最后，我们将总结观察到的与常规Spark作业相比，该框架在作业运行时获得的性能提升。
 ### Speakers: 
 <img src="images/speaker/1244.png" width="200" /><br>Anmol Chaturvedi: Informatica公司, 工程总监, Anmol Chaturvedi负责在Informatica的弹性无服务器云数据引擎平台上集成了云MDM、云数据工程引擎、云分析和云数据质量套件。他曾负责数据虚拟化套件，以及Informatica内部设计的本地分布式数据处理引擎。他拥有超过15年的企业软件开发经验，涉及数据管理、分布式计算和数据库。
 <img src="images/speaker/1244_2.png" width="200" /><br>Haripriya Bendapudi:
高级软件工程师，Informatica。在过去3年多的时间里，一直从事云数据集成弹性产品的工作，通过利用Kubernetes上的Spark，帮助用户以时间和成本效益的方式运行实时数据集成管线。她拥有康奈尔大学的硕士学位。工作之余，她喜欢徒步旅行，并将她的烹饪技能用于测试。

 

<img src="images/speaker/1244_3.png" width="200" /><br>Praneet Sharma:
Informatica公司的首席软件工程师，在数据集成领域有8年的经验。负责利用Spark、Kubernetes和Livy等开源技术，在Informatica的云数据集成弹性和高级无服务器产品中设计和实现功能。

 

 