---
title: "小米利用 Apache Paimon 实现高效数据和 AI 优化"
date: ""
track: "datalake"
presenters: "Houliang Qi"
stype: "中文演讲"
--- 

本次会议将重点介绍小米如何利用 Apache Paimon 在信息化数据仓库、AI 数据仓库以及 LLM 数据处理中提升效率、降低成本。此外，我们将讨论如何利用 JuiceFS 支持 Paimon 的多云存储能力。最后，我们将介绍 Apache Gravitino 在 Paimon 元数据管理中的应用。
内容提要：
1. Apache Paimon 在信息化数据仓库中的应用实践
  - 我们将详细阐述如何使用 Paimon 作为维度表替代 Iceberg 和 HBase，在满足业务时效性要求的同时，实现 31% 的成本降低。此外，我们将讲解如何使用自定义 Lookup Shuffle 和远程存储作为 Lookup Cache 加速 Lookup Join 过程，使 Lookup Join 性能显著提升 60 倍。2
2. Apache Paimon 在 AI 数据仓库中的应用实践
  - 在广告算法模型中，样本数据的数量和时效性至关重要。在引入 Paimon 之前，我们的离线和实时样本数据分别通过独立的流水线进行处理。离线样本通过 Spark Join 进行连接，导致整体数据产出的时效性不高，计算成本也较高。此外，离线和实时样本架构是两个独立的系统，开发效率低下。通过引入 Paimon 的部分更新功能，我们实现了实时样本连接，将模型训练样本生成时间从数天缩短到数小时。3
3. Apache Paimon 在 LLM 数据预处理中的实践
  - 在 LLM 数据预处理中，数据去重是至关重要的一步。我们将介绍如何利用 Paimon 的主键表和聚合合并引擎特性，简化 LLM 数据预处理流程。4
4. Apache Paimon 多云存储能力构建与实践
 - 云原生 Lakehouse 架构是新兴趋势，在小米，我们基于 JuiceFS 构建了多云存储能力。这种方式可以有效屏蔽业务应用底层存储（例如 OSS/Blob/KS3/S3）的差异，不仅解决了自建 HDFS 存储成本高、节点偶尔慢的问题，还能充分发挥云存储低成本、高扩展性和高可靠性的优势，满足业务海量数据存储的需求。5
5. 基于 Gravitino 的元数据湖统一实践
  - 我们将介绍如何使用 Gravitino 管理 Paimon 的元数据，并探讨如何使用 Gravitino 统一跨数据湖的元数据，以及统一元数据为我们的数据管理流程带来的优势。

通过本次分享，用户将了解小米如何利用 Apache Paimon 优化数据/AI 仓储和 LLM 预处理以提高效率和节省成本，如何通过 Paimon 实现多云灵活性，以及​​如何使用 Apache Gravitino 统一元数据管理。

### 讲师:

<img src="https://sessionize.com/image/8968-400o400o1-XFskLG5iSQjayU8GPBBL9V.jpg" width="200" /><br/>

Apache IoTDB 和 Apache TsFile PMC 成员，小米软件研发工程师，专注于小米数据湖平台的开发与实施。