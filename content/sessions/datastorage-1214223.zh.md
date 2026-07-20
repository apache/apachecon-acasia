---
title: "用 Gravitino 统一 Lance 的元数据管理"
date: "2026-08-08T15:45:00"
track: "datastorage"
presenters: "Qi Yu"
stype: "中文演讲"
room: "万寿山会议室"
---

随着 AI 和基于向量的工作负载兴起，Lance 作为面向分析与机器学习场景的高性能数据格式，正受到越来越多的关注。然而，由于缺少统一的元数据层，跨系统管理 Lance 数据集仍然充满挑战。

在本次演讲中，我们将介绍 Apache Gravitino 如何通过其 Lance REST 服务集成，实现对 Lance 的集中化元数据管理。我们将演示如何用统一的目录抽象来建模 Lance 数据集，使其更易于在不同引擎间被管理、发现和访问。

我们还会分享这次集成背后的设计考量，演示如何通过 Gravitino 创建并访问 Lance 数据集，并讨论这种做法如何帮助构建一个更一致、更具扩展性的数据平台，以同时服务传统分析和新涌现的 AI 工作负载。

### 讲师:


<img src="https://cdn.sessionize.com/image/b330-400o400o1-TDqhGWSyPAGG48dG2H2tHm.jpg" width="200" /><br/>

Qi Yu：数据基础设施工程师，Apache Gravitino PMC

Datastrato 工程师、Apache Gravitino PMC 成员，从事大数据基础设施、元数据管理与数据库系统的工作，专注于可扩展数据平台的研发。