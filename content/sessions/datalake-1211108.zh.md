---
title: "生产环境中的 Apache Iceberg V3：来自大规模部署的经验教训"
date: "2026-08-08T14:00:00"
track: "datalake"
presenters: "Yuming Wang"
stype: "中文演讲"
room: "万春厅"
---

Apache Iceberg V3 带来了强大的能力，但要可靠地在生产环境中运行它，需要的远不止一次版本升级。在本次演讲中，我们分享采用 Iceberg 1.10 的真实历程：表设计、写入/读取路径调优、compaction 策略，以及元数据生命周期管理。我们将剖析所面临的关键瓶颈——小文件增长、快照膨胀、合并/更新压力，以及查询延迟波动——以及那些既提升了稳定性又提高了成本效率的具体优化。你将带走实用的架构模式、反模式，以及一份身经百战的检查清单，从而有信心地从试点走向生产。

### 讲师:


<img src="https://cdn.sessionize.com/image/76e8-400o400o1-SFWqZ9h7n7AzYSjYd6fvns.jpg" width="200" /><br/>

Yuming Wang：eBay，计算与湖仓

Yuming Wang 是 Apache Spark 项目管理委员会（PMC）的成员，目前负责公司计算平台的建设与演进。他专注于在生产规模下对 Spark 进行架构设计、优化和运营，同时推动基于 Apache Iceberg 的湖仓架构的落地与运营。他致力于把前沿的开源数据技术转化为可靠、高效的企业级生产系统。