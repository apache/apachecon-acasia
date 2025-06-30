---
title: "小米利用 Apache Paimon 实现高效数据和 AI 优化"
date: "2025-07-27T17:15:00"
room: "万春厅"
track: "datalake"
presenters: "Houliang Qi"
stype: "中文演讲"
---

本次分享将重点介绍小米如何利用 Apache Paimon 提升信息化数仓、AI 数仓和 LLM 数据处理的效率并降低成本。同时，我们也将讨论如何利用 JuiceFS 支持 Paimon 的多云存储能力。最后，我们将介绍 Apache Gravitino 在管理 Paimon 元数据方面的应用。
提纲如下：
1. Apache Paimon 在信息化数仓中的应用实践
  - 我们将详细阐述如何使用 Paimon 作为维表替代 Iceberg 和 HBase，这一做法不仅满足了业务的时效性要求，还实现了 31% 的成本降低。此外，我们将讲解如何使用自定义 Lookup Shuffle 和远程存储作为 Lookup Cache 加速 Lookup Join 过程，使 Lookup Join 性能显著提升 60 倍。
2. Apache Paimon 在 AI 数仓中的应用实践
  - 在广告算法模型中，样本数据的数量和时效性至关重要。在引入 Paimon 之前，我们的离线和实时样本数据分别通过独立的系统进行处理，开发效率低下。通过引入 Paimon 的Partial Update和SPJ功能，我们实现了实时样本关联，将生成模型训练样本所需的时间从数天缩短到了小时级别。
3. Apache Paimon 在 LLM 数据预处理中的实践
  - 在 LLM 数据预处理中，数据去重是至关重要的一步。我们将介绍如何利用 Paimon 的主键表和Merge Engine特性，简化 LLM 数据预处理流程。
4. Apache Paimon 多云存储能力构建与实践
 - 云原生 Lakehouse 架构是新兴趋势，在小米，我们基于 JuiceFS 构建了多云存储能力。这种方式可以有效屏蔽业务应用底层存储（例如 OSS/Blob/KS3）的差异，不仅解决了自建 HDFS 存储成本高、慢节点等问题，还能充分发挥云存储低成本、高扩展性和高可靠性的优势，满足业务海量数据存储的需求。
5. 基于 Gravitino 的元数据湖统一实践
  - 我们将介绍如何使用 Gravitino 管理 Paimon 的元数据，并讨论统一元数据为我们的数据管理流程带来的优势。

通过本次分享，听众将了解小米如何利用 Apache Paimon 优化信息化/AI 数仓及 LLM 预处理，实现效率提升与成本节约；如何借助 Paimon 实现多云灵活性；以及如何使用 Apache Gravitino 进行统一的元数据管理。

### 讲师:

<img src="https://sessionize.com/image/8968-400o400o1-XFskLG5iSQjayU8GPBBL9V.jpg" width="200" /><br/>

Houliang Qi: 小米高级软件研发工程师

Apache IoTDB 和 Apache TsFile PMC 成员，目前专注于小米数据湖平台的开发与实施。