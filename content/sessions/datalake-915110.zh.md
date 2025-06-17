---
title: "Flink + Paimon 实时 Lakehouse 解决方案的技术演进"
date: ""
track: "datalake"
presenters: "Xuannan Su"
stype: "中文演讲"
---

近年来，Lakehouse 架构已成为一种变革趋势。Streaming Lakehouse 架构利用 Flink 作为流批统一处理引擎，并结合 Paimon 作为流批统一数据湖格式，实现了 Lakehouse 的实时数据更新。虽然结构化数据在 Paimon 中仍然被广泛使用，但半结构化和非结构化数据在人工智能应用中正变得越来越重要。Flink 和 Paimon 社区紧密合作，整合各自的优势，并集成前沿功能，为用户带来了显著的增强和优化。
在本次演讲中，我们将介绍一些重要的工作，包括：
* Flink 和 Paimon 如何利用 Variant 数据类型和 Variant 分解来提升处理半结构化数据的性能
；* Flink 如何利用 Paimon 的 bucket 机制加速与 Paimon 维度表的连接；
* 简化和提升用户数据湖管理体验的增强功能



### 讲师:

<img src="https://sessionize.com/image/6797-400o400o1-dbccedf4-ca5c-4ac7-9407-da8d909f00a6.jpg" width="200" /><br/>

Xuannan Su: 阿里巴巴

Xuannan 是阿里巴巴的一名软件工程师，2019 年获得卡内基梅隆大学硕士学位后，专注于 Apache Flink 及其生态系统的开发。