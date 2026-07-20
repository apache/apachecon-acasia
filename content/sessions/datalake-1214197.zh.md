---
title: "超越协议：在企业级规模下让 Iceberg REST Catalog 走向生产"
date: "2026-08-07T15:00:00"
track: "datalake"
presenters: "Jerry Shao"
stype: "中文演讲"
room: "万春厅"
---

尽管 Iceberg REST Catalog（IRC）为表管理提供了标准化的协议，但在关键任务的企业环境中落地它，会暴露出一个显著的"实现差距"。从传统的 Hive Metastore（HMS）迁移到基于 REST 的架构，需要的不仅仅是一个新的 API——它要求对安全、性能和数据连续性进行彻底的重新思考。

在本次演讲中，我们分享一套在生产环境中部署 IRC 的、经过实战检验的方案。我们把这次转型拆解为三大支柱：

无缝迁移：如何在不造成业务中断、也不出现"stop-the-world"维护窗口的情况下，把现有由 HMS 管理的表迁移到 IRC。
安全现代化：从 Hadoop 原生的 Kerberos 认证和基于 Ranger 的授权，迁移到现代的、云原生的 OAuth 和集中化身份提供者（identity provider）的策略。
大规模性能：把提交（commit）机制从客户端转移到服务端，为优化打开了新的大门。我们将探讨服务端的性能增强，它们能减少提交冲突并改善查询规划延迟。
听众将带走一份实用的路线图，用以弥合 IRC 规范与安全、高性能生产部署之间的差距。

### 讲师:


<img src="https://cdn.sessionize.com/image/396c-400o400o1-PCyrxuKZaPxmAUQMTrdp5J.jpg" width="200" /><br/>

Jerry Shao：Datastrato CTO

Jerry Shao 是 Datastrato 的联合创始人兼 CTO，专注于开源大数据领域已超过 10 年。他是 Apache 成员、Apache Spark 和 Apache Inlong 的 committer 和 PMC 成员，也是 Apache Gravitino 的原创建者。