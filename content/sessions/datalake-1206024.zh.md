---
title: "Iceberg 中的一等公民约束元数据：跨引擎的可移植数据质量"
date: ""
track: "datalake"
presenters: "Huaxin Gao"
stype: "英文演讲"
---

现代湖仓部署越来越需要跨生态的、可靠且可移植的数据质量保证。如今，不同引擎和连接器对约束的处理并不一致，而 Iceberg 也尚未提供与引擎无关的约束模型。本次演讲提议在 Apache Iceberg 中将约束支持作为一等公民（first-class）元数据加入：稳定的 ID、按字段 ID 绑定以保障 schema 演进安全，以及跨引擎一致的元信息查询（introspection）。第一阶段以务实为主：NOT NULL 仍通过 required 字段来强制；CHECK 约束由 Iceberg 存储并暴露，由支持它的引擎在写入时强制执行；UNIQUE/PRIMARY KEY/FOREIGN KEY 则是信息性的。第一阶段还交付了端到端的 Spark DSv2 集成（带约束的 CREATE/ALTER、ADD CHECK 时的校验，以及在受支持情况下的写入时 CHECK 强制执行）。对于 ADD CHECK，引擎会在某个特定的表版本上校验已有数据，而 Iceberg 仅在当前快照/版本仍与已校验的 token 匹配时才提交（严格 CAS），从而防止竞态与过时校验。

### 讲师:


<img src="https://cdn.sessionize.com/image/be04-400o400o1-P3f2LM1B3ad2TjS4zYxdvG.jpg" width="200" /><br/>

Huaxin Gao：Snowflake 软件工程师

Huaxin Gao 是 Snowflake 的软件工程师，也是 Apache Spark 的 committer 和 PMC 成员。她还是 Apache Iceberg 和 Apache DataFusion Comet 的 committer，贡献横跨查询引擎、表格式和分布式数据系统。
