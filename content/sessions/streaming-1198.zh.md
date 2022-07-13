---
title: "让 Flink 在 K8s 上运行的更好"
date: "2022-07-30T16:10:00"
track: "streaming"
presenters: "赵波"
stype: "中文演讲"
---
让Flink在K8S运行的更好，当今K8S已经慢慢进入线上部署服务，在整个大数据技术演进过程中，我们对运行在K8S上的Flink job有了更高的需求，例如，
1. 在资源紧缺的情况下，我们需要Flink job能够按照一定的规则按序运行。
2. 集群资源可配置，不需要人工计算和配置Flink job运行时的资源，确保Flink job时的资源预占。
更广泛的需求是：
调度算法的多样性，调度性能的高效性，无缝对接主流计算框架，对异构设备的支持等等
Volcano正是针对这些需求应运而生的。同时，Volcano继承了Kubernetes接口的设计风格和核心概念。Volcano是CNCF下首个也是唯一的基于Kubernetes的容器批量计算平台，主要用于高性能计算场景。它提供了Kubernetes目前缺 少的一套调度机制，这些机制通常是机器学习大数据应用、科学计算、特效渲染等多种高性能工作负载所需的。

下面让我们针对CNCF PodGroup概念进行展开，领略一下Flink on K8S 和 volcano如何让Flink job按照我们的意愿运行。
 ### Speakers: 
 <img src="images/speaker/1198.png" width="200" /><br>赵波: 华为, 从事Flink计算框架相关研究

 
