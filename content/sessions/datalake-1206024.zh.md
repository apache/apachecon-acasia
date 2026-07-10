---
title: "First-Class Constraint Metadata in Iceberg: Portable Data Quality Across Engines"
date: ""
track: "datalake"
presenters: "Huaxin Gao"
stype: "英文演讲"
---

Modern lakehouse deployments increasingly need reliable, portable data quality guarantees across the ecosystem. Today, constraints are handled inconsistently across engines and connectors, and Iceberg does not yet provide an engine-agnostic constraint model. This session proposes adding constraint support to Apache Iceberg as first-class metadata: stable IDs, binding by field IDs for schema-evolution safety, and consistent cross-engine introspection. Phase 1 is pragmatic: NOT NULL stays enforced via required fields; CHECK constraints are stored and exposed by Iceberg and enforced on writes by engines that support it; UNIQUE/PRIMARY KEY/FOREIGN KEY are informational. Phase 1 also delivers an end-to-end Spark DSv2 integration (CREATE/ALTER with constraints, validation on ADD CHECK, and write-time CHECK enforcement where supported). For ADD CHECK, engines validate existing data on a specific table version and Iceberg commits only if the current snapshot/version still matches the validated token (strict CAS), preventing races and stale validations.

### 讲师:


<img src="https://cdn.sessionize.com/image/be04-400o400o1-P3f2LM1B3ad2TjS4zYxdvG.jpg" width="200" /><br/>

Huaxin Gao: Software engineer at Snowflake

Huaxin Gao is a software engineer at Snowflake and an Apache Spark committer and PMC member. She is also a committer for Apache Iceberg and Apache DataFusion Comet, with contributions spanning query engines, table formats, and distributed data systems.

