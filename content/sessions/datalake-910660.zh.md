---
title: "统一数据湖接入与实时集成：解构 SeaTunnel 对 Hudi / Iceberg / Paimon 的架构级支持"
date: ""
track: "datalake"
presenters: "Lidong Dai"
stype: "英文演讲"
---

在当前湖仓一体、实时数据湖演进的趋势下，企业愈发需要一个统一、高性能、可扩展的数据集成框架来支撑对多种数据湖格式（如 Apache Hudi、Iceberg、Paimon）的数据写入与读取工具。Apache SeaTunnel 作为新一代数据集成引擎，通过其 Connector V2 架构和流批统一设计，构建了对三大主流数据湖格式的深度支持体系，涵盖批量加载、实时流式写入和一致性保障等关键能力。

演讲提纲：
一、SeaTunnel 架构与运行机制
流批一体架构设计理念
Connector V2 的插件注册、运行时加载与生命周期管理
支持近 200 种数据源，覆盖数据库、对象存储、消息队列、数据湖等生态
二、数据湖支持总览：Hudi / Iceberg / Paimon 的特性对比
三者的写入等机制差异
SeaTunnel 的统一处理策略与接口抽象能力
三、SeaTunnel 对 Iceberg 的支持架构详解
四、SeaTunnel 对 Hudi 的流式支持
五、SeaTunnel 对 Paimon 的融合实践
六、案例分享：企业级实时湖仓建设
从 MySQL CDC → SeaTunnel → Iceberg 构建商品实时数仓
七、未来展望与生态集成方向
支持 DeltaLake 的计划等

### 讲师:

<img src="https://sessionize.com/image/a63f-400o400o1-TAZzBju9ZdRb4umYVxMo2D.png" width="200" /><br/>

Lidong Dai: Whaleops Technology 联合创始人

Apache 孵化器导师、Apache DolphinScheduler PMC 主席和 Apache SeaTunnel PMC 成员