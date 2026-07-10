---
title: "Fluss × 湖仓：在数据湖上解锁亚秒级数据新鲜度"
date: ""
track: "datalake"
presenters: "Yuxia Luo"
stype: "中文演讲"
---

现代数据平台被夹在两个世界之间：流式系统交付新鲜数据，却缺乏长期存储；湖仓提供持久的分析能力，却无法服务真正的实时查询。对于主键表而言，这一鸿沟尤为痛苦——Paimon 需要经过 compaction 才能让新行可见，而 Iceberg 则会累积 equality delete 文件，从而拖垮查询性能。

  Apache Fluss（孵化中）作为一个与湖仓统一的专用流式存储层，弥合了这一鸿沟。
  在本次演讲中，我们将走查：

  - Tiering Service：持续地把数据从 Fluss 同步到 Paimon、Iceberg 和 Hudi
  - Union Read：在一次查询中透明地合并实时 Fluss 数据与历史湖数据
  - Fluss 如何利用其原生主键索引，在分层（tiering）过程中生成 Deletion Vector，从而消除 Paimon 的 compaction 瓶颈和 Iceberg 的 equality-delete 开销
  - 一场使用 Fluss + Iceberg/Paimon + DuckDB 的端到端现场演示，展示主键表上的亚秒级新鲜度

  我们将以路线图收尾：多引擎 Union Read（Spark、Trino、StarRocks）、更广泛的湖支持（Hudi、Delta），以及单个 Fluss 集群内的异构分层（tiering）。

### 讲师:


<img src="https://cdn.sessionize.com/image/ca53-400o400o1-WCz7bXLtTwAYYZGVPMgNLv.png" width="200" /><br/>

Yuxia Luo：Apache Fluss PMC | 阿里巴巴软件工程师

Yuxia Luo 是阿里巴巴的软件工程师，也是 Apache Fluss 的 PMC 成员，从事流式存储及其与现代湖仓格式融合的工作。他主导了围绕 Tiering、Union Read 以及跨 Paimon、Iceberg 的主键表实时可查询性等特性。凭借在 Apache Flink 和大规模实时数据平台方面多年的经验，他热衷于弥合流式与数据湖之间的鸿沟。他曾在此前的 Flink Forward 和 QCon 上分享过他的工作。
