---
title: "迈向湖仓：高性价比的 Hive 迁移与大规模实时入湖"
date: "2026-08-08T15:00:00"
track: "datalake"
presenters: "Hangxiang Yu"
stype: "中文演讲"
room: "万春厅"
---

在滴滴，把我们的 Hive 生态扩展到 Iceberg，需要的不仅仅是简单的格式转换，而是重建我们的数据完整性与治理策略。我们设计了一套基于快照的零停机离线迁移策略，能够在切换之前进行一致性检查和即时回滚。为了应对元数据膨胀和孤儿文件问题，我们还集成了 Apache Amoro 来实现自主优化。

在这一基础上，我们把架构扩展到了实时场景。通过用 Iceberg 精简入湖管道，我们把数据延迟从小时级降低到了分钟级。这种统一的做法不仅简化了 ETL 管道，还节省了 PB 级的存储，并显著降低了计算成本。 

本次演讲提供关于在生产环境中构建稳定、高性能湖仓的可落地洞见。

### 讲师:


<img src="https://cdn.sessionize.com/image/d20f-400o400o1-WrCCe8TfkfC32qDkTEEfSN.jpg" width="200" /><br/>

Hangxiang Yu：Apache Flink Committer & 滴滴实时计算团队负责人

Hangxiang Yu 是 Apache Flink Committer，目前在滴滴带领实时计算工程团队。凭借在分布式系统和存储方面多年的实战经验，他管理着滴滴的实时基础设施，包括 Apache Flink、数据入湖管道以及 P0 级实时数据仓库。他还致力于推进滴滴的湖仓架构，努力提升数据新鲜度、优化基础设施成本，并构建自管理的治理能力。