---
title: "Iceberg 故障剖析：来自真实线上升级事件的经验教训"
date: "2026-08-07T16:45:00"
track: "datalake"
presenters: "Noémi Pap-Takács, Boglárka Egyed"
stype: "英文演讲"
room: "万春厅"
---

Apache Iceberg 通过引入 ACID 事务和灵活的表更新，彻底改变了数据湖。然而在企业级规模下，"放手不管"式的管理只是一种幻想。如果没有正确的维护策略，高吞吐系统往往会饱受存储成本上升、查询性能退化乃至故障的困扰。

在本次演讲中，我们将剖析真实的客户升级事件——从因不得不处理海量元数据而崩溃的系统，到因多个并发写入者持续更新数据而导致清理任务被阻塞的情况。

听众将超越文档，学到一份经过验证的实用指南：从四处"救火"转向主动管理，让数据湖保持健康和高性能。

我们将涵盖：
- 可观测性：需要监控的关键指标，以便在问题升级为事件之前发现健康隐患。
- 性能技巧：降低存储与计算成本。
- 维护策略：配置维护特性并调度 compaction 作业，同时不锁死生产写入者。
- 恢复：如何修复表并从故障中恢复。

### 讲师:


<img src="https://cdn.sessionize.com/image/5a3f-400o400o1-BYhDA4rBpsGm8n4d5mcvhs.jpg" width="200" /><br/>

Noémi Pap-Takács：Apache Impala Committer

Noémi Pap-Takács 是 Cloudera 的软件工程师，也是 Apache Impala 项目的 committer。她的专长在于性能优化以及将 Apache Iceberg 集成到 Impala 中。


<img src="https://cdn.sessionize.com/image/bbcc-400o400o1-faLy6maxgVArZ88BQgaPnH.jpg" width="200" /><br/>

Boglárka Egyed：Cloudera 工程总监

Boglárka Egyed 是 Cloudera 的工程总监，带领着 Apache Impala 和 Hive 背后的团队。她从汽车工程师转型为大数据爱好者，在转向管理岗位之前，她曾作为 Apache Sqoop 开发者工作多年。如今，她专注于扩大工程卓越性，并为现代数据架构推进开源创新。