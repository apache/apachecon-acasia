---
title: "在实践中构建实时数据湖"
date: "2025-07-26T15:00:00"
room: "万春厅"
track: "datalake"
presenters: "Congxian Qiu"
stype: "中文演讲"
---

在实时驱动业务决策的时代，高吞吐量数据湖仓库的架构设计已成为企业数字化转型的决战战场。面对传统批处理架构难以逾越的时效性瓶颈，我们基于 Flink CDC 3.0 + Apache Iceberg + Apache Amoro 构建了流式数据湖仓库系统，成功实现了单客户日均数百亿数据流的分钟级就绪和查询性能跨越。

本次分享将介绍三方面的实践经验：
基于 Flink CDC3.0，多业务表异构数据秒级入库，解决了历史数据漂移与增量同步的精准对接难题；
Iceberg 性能调优设计，复杂查询性能相比 Hive 提升 400%；
Apache Amoro 自优化框架的创新应用，在高效合并小文件和清洗数据的同时，提供高效的读取性能。

该系统已在电信运营商的生产实践中落地，支撑每日PB级数据处理的业务峰值，可为参与者提供可无缝迁移的实时湖仓架构范式。

### 讲师:

<img src="https://sessionize.com/image/25e4-400o400o1-9iGsggaDEwoFcYqGXtpqoM.jpg" width="200" /><br/>

Congxian Qiu: Apache Flink Committer、Apache（incubating）Amoro PMC 成员, 天翼云副总监

Congxian 拥有多年大数据基础设施研发经验。目前领导天翼云基于 Apache Iceberg 的数据湖架构开发和实现, 他是 Apache Flink Committer 和 Apache（incubating）Amoro PMC 成员。

<img src="https://sessionize.com/image/dd80-400o400o1-SKrNUnGVHC8xTrBeHtFLHN.jpg" width="200" /><br/>

Zhuojun Jiang: 天翼云 高级大数据工程师

Zhuojun Jiang 致力于大数据湖仓架构研发。她正在专注于基于Apache FlinkCDC、Iceberg 和 Amoro 等组件搭建的数据湖仓，深入数据同步、性能优化等技术领域，并积极参与开源社区贡献。