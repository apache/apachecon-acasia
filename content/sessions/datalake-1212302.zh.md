---
title: "精简元数据，驾驭大数据：让 Apache Iceberg 中的查询保持飞快"
date: ""
track: "datalake"
presenters: "Hongyue Zhang"
stype: "英文演讲"
---

Apache Iceberg 的元数据层正是 schema 演进、分区演进和谓词下推（predicate pushdown）得以实现的基础。但在 PB 级规模下，这些元数据本身可能膨胀到数百 GB 甚至更多。当规划阶段拖慢了执行阶段，就总得有所取舍。

本次演讲探讨 Iceberg 的元数据是如何通过 manifest、分区摘要（partition summary）以及列级指标来组织的，以及为什么每一层都是为了支撑快速分析查询而存在。随后，我们将走查 Iceberg 的原生 API、procedure，以及把它们应用于大规模场景下控制元数据体量的实用策略。最后，我们会预览 Iceberg v4 规范中的一些提案，它们旨在让元数据在默认情况下更紧凑、更具可扩展性。

你将清晰地了解那数 GB 的元数据究竟从何而来，获得一份以 Iceberg 自身方式来控制元数据体量的"打法手册"，以及对 v4 规范足够的背景认知——足以让你开始参与贡献，并了解该格式未来的走向。


### 讲师:


<img src="https://cdn.sessionize.com/image/1050-400o400o1-3JfnogDnkgNnwSMLv7LeQm.jpg" width="200" /><br/>

Hongyue Zhang：Snowflake 软件工程师

Hongyue 自 2022 年起开始为 Apache Iceberg 项目做贡献，当时他在 Apple 数据平台工作。如今在 Snowflake，他围绕 Apache Iceberg 构建工具和系统，以帮助做出数据驱动的决策。
