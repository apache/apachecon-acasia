---
title: "Iceberg UDF 规范：跨引擎的可移植 SQL 函数"
date: "2026-08-09T13:30:00"
track: "datalake"
presenters: "Huaxin Gao"
stype: "英文演讲"
room: "万春厅"
---

Iceberg 的 UDF 规范引入了一种自包含、带版本的元数据格式，用于 SQL 标量函数和表函数，它们可以跨 catalog 和引擎（如 Spark 和 Trino）流转。本次演讲将走查核心模型、定义、参数命名规则、返回类型以及方言特定的表示方式，并解释版本管理、回滚、确定性（determinism）和空值处理提示如何让 UDF 具备可移植性，同时不牺牲引擎侧的优化。我们将重点介绍一些关键设计选择，例如不可变的函数签名、与默认值兼容的重载，以及安全函数（secure function），最后给出在引擎或 catalog 中实现该规范的实用指引。

### 讲师:


<img src="https://cdn.sessionize.com/image/be04-400o400o1-P3f2LM1B3ad2TjS4zYxdvG.jpg" width="200" /><br/>

Huaxin Gao：Snowflake 软件工程师

Huaxin Gao 是 Snowflake 的软件工程师，也是 Apache Spark 的 committer 和 PMC 成员。她还是 Apache Iceberg 和 Apache DataFusion Comet 的 committer，贡献横跨查询引擎、表格式和分布式数据系统。