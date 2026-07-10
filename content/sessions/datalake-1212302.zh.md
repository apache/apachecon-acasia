---
title: "构建统一湖仓：Apache Paimon 及其生态的最佳实践"
date: ""
track: "datalake"
presenters: "Zhoulong Liu"
stype: "中文演讲"
---

随着数据架构不断演进，为批处理和流处理分别维护独立的孤岛——Lambda 架构的标志——已经变得越来越昂贵和复杂。我们如何才能构建一个真正统一的平台，既能提供实时的数据新鲜度，又能在规模化场景下实现高性能分析？

在本次演讲中，我们将超越理论，深入构建以 Apache Paimon 为中心的下一代统一湖仓的实战一线。我们将分享身经百战的最佳实践和真实落地模式，演示如何通过深度的生态协同来架构一条无缝的数据管道：

Apache Flink + Paimon —— 稳健、低时延的实时入湖，进入事务型数据湖
Apache Paimon —— 核心存储层，支持 ACID 事务、schema 演进和流批统一读取
StarRocks 与 Apache Spark + Paimon —— 直接在湖上提供卓越的交互式和批处理查询性能
Apache Kyuubi —— 把这一切串联起来的统一、无服务器 SQL 网关
Apache Gravitino —— 统一元数据管理，支持跨引擎和数据源的集中化元数据治理
听众将带走一套围绕 Paimon 及其他关键组件构建统一湖仓的、经过验证的方法论，以及跨生态的组件选型、集成和生产调优的实用指导，还有额外的 Data+AI 应用场景。

### 讲师:


<img src="https://cdn.sessionize.com/image/be84-400o400o1-BzW6ygnHFUNsYubzvrwjzK.jpg" width="200" /><br/>

Zhoulong Liu：eclicktech 资深大数据专家

作为 eclicktech 大数据部门的负责人，他此前曾在搜狐视频和腾讯工作，擅长构建大数据平台及相关系统。
