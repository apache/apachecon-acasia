---
title: 使用 Apache Cloudberry 构建统一的 Lakehouse 解决方案
date: '2026-08-08T15:45:00'
room: 万春厅
track: datalake
presenters: Rose Duan
stype: 中文演讲
depth: intermediate
practice_level: 4
projects:
- apache cloudberry
audience:
- 架构师
- 开发者
related_sessions:
- 从数据到 AI：基于 Apache Cloudberry 构建统一分析平台
- Apache Cloudberry 简介：演变、主要特性和路线图
- 在实践中构建实时数据湖
- 在腾讯云上基于 Iceberg & Amoro & Gravitino 构建云原生 Lakehouse 架构
- Flink + Paimon 实时 Lakehouse 解决方案的技术演进
---
数据仓库擅长快速分析，而数据湖则注重可扩展存储和灵活的数据管理。Lakehouse
架构旨在将两者的优势结合起来——无缝集成跨数据湖和数据仓库的数据，以实现高效分析和统一治理。

作为下一代开源 MPP 数据库，Apache Cloudberry 扩展了其技术边界，构建了开放式 Lakehouse 解决方案。
本次演讲将介绍 Cloudberry 在实现统一 Lakehouse 架构方面的关键功能：

1. 加速 Parquet/ORC 格式的 Lake 查询，无需数据移动
2. 统一数据网关，用于跨异构数据源的查询和写入
3. 集成数据处理和同步管道，实现从数据采集到分析的端到端流程
4. 开放元数据和存储格式，简化生态系统集成并降低迁移成本

### 讲师:

<img src="https://sessionize.com/image/5feb-400o400o1-ns3S5cNdoMFDN2jL1rrsNH.jpg" width="200" /><br/>

Rose Duan: Apache Cloudberry 贡献者

Apache Cloudberry 贡献者，HashData 的数据库内核开发人员。