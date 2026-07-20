---
title: "下一代数据编织（Data Fabric）：移动云 DataStudio 上的 SeaTunnel 与 Gravitino"
date: "2026-08-09T15:15:00"
track: "datalake"
presenters: "li jie"
stype: "中文演讲"
room: "万春厅"
---

摘要：

本次演讲为中国移动云 DataStudio 引入一次范式转变：通过将 Apache SeaTunnel（高性能数据引擎）与 Apache Gravitino（统一元数据大脑）相结合，构建下一代联邦式数据编织（Federated Data Fabric）。

通过将元数据治理与数据执行解耦，我们实现了真正的 Zero-ETL 体验。Gravitino 提供集中化的 catalog、安全和 schema 治理，而 SeaTunnel 则基于这些策略执行超高速的分布式数据同步。

关键创新：

- 零配置集成：元数据驱动的管道免去了手工配置。
- 自动化 Schema 演进：跨数据湖进行安全、受治理的 DDL 变更。
- 实时血缘：在数据流转过程中捕获 100% 准确的列级血缘。
- 统一安全：面向企业合规的、跨云的基于 token 的数据访问。
二者结合，赋能 DataStudio 在多云时代交付一套高安全、敏捷且智能的湖仓架构。

### 讲师:


<img src="https://cdn.sessionize.com/image/c0e6-400o400o1-EzbRtZqHo8Lhg4r51CDvC9.jpg" width="200" /><br/>

li jie：cmss-suzhou 工程师

2024 年 12 月 – 至今 | 移动云