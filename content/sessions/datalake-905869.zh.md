---
title: "在实践中构建实时数据湖"
date: ""
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

Congxian Qiu

Congxian 是 StateCloud 研发专家，拥有多年大数据基础设施经验，参与并领导了大规模数据处理框架的开发。他是 Apache Committer 和 Apache（incubating）Amoro PMC 成员。

<img src="https://sessionize.com/image/dd80-400o400o1-SKrNUnGVHC8xTrBeHtFLHN.jpg" width="200" /><br/>

Zhuojun Jiang

Zhuojun Jiang 是中国电信云科技有限公司的高级大数据工程师，专注于实时数据湖库架构研究。她专注于基于 Apache FlinkCDC、Iceberg 和 Amoro 等技术的大数据开发、系统性能优化和实时数据同步。蒋卓君积极参与开源社区的贡献，并通过行业论坛和技术讲座分享实践见解。