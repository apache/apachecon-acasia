---
title: "Iceberg UDF Spec: Portable SQL Functions Across Engines"
date: ""
track: "datalake"
presenters: "Huaxin Gao, Yufei Gu"
stype: "英文演讲"
---

Iceberg’s UDF spec introduces a self-contained, versioned metadata format for SQL scalar and table functions that can move across catalogs and engines like Spark and Trino. This talk walks through the core model, definitions, parameter naming rules, return types, and dialect-specific representations, and explains how versioning, rollback, determinism, and null-handling hints make UDFs portable without sacrificing engine optimizations. We’ll highlight key design choices such as immutable signatures, overload compatibility with defaults, and secure functions, and close with practical guidance for implementing the spec in an engine or catalog.

### 讲师:


<img src="https://cdn.sessionize.com/image/be04-400o400o1-P3f2LM1B3ad2TjS4zYxdvG.jpg" width="200" /><br/>

Huaxin Gao: Software engineer at Snowflake

Huaxin Gao is a software engineer at Snowflake and an Apache Spark committer and PMC member. She is also a committer for Apache Iceberg and Apache DataFusion Comet, with contributions spanning query engines, table formats, and distributed data systems.


<img src="https://cdn.sessionize.com/image/f687-400o400o1-MLqGgndoS3yUwVgfUrDXTT.jpg" width="200" /><br/>

Yufei Gu: Senior software engineer at Snowflake

Apache Polaris PPMC member
Apache Iceberg PMC member
Apache Hadoop PMC member

