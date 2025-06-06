---
title: "基于Arm64架构，使用Gluten和Velox引擎加速Spark查询"
date: ""
track: "datalake"
presenters: "Yuqi Gu"
stype: "中文演讲"
--- 

Apache Spark SQL 提供了一个强大的解决方案，使用户能够高效地处理海量数据集。最近，Project Gluten 作为基于 Apache Arrow 的原生 SQL 引擎被引入，旨在增强 Spark SQL 的功能。与此同时，几个拥有活跃开源社区的向量化 SQL 引擎也受到了广泛关注。其中，由 Meta 领导的 Velox 项目脱颖而出，成为了一个有前途的向量化数据库加速库。

Gluten-Velox 的集成代表了向前迈出的重要一步，为 Arm 平台量身定制了一个优化的 Spark SQL 加速器。通过利用 Gluten-Velox，Spark SQL 克服了其传统基于行的数据处理和在 Arm64 架构上的 JVM 限制。这是通过 Arm64 SIMD 能力的垂直组合性和先进的向量化执行技术实现的。

在本次演讲中，我们将简要介绍原生引擎 Gluten 和 Velox，并探讨在 Arm64 上启用 Gluten 和 Velox 的情况，展示在 Arm Neoverse N2 平台上通过这种方法实现的潜在性能提升的实验结果。此外，我们还将讨论一个针对 Arm64 上 Velox 的优化案例，展示进一步增强性能的策略。

### 讲师:

<img src="https://sessionize.com/image/c0c6-400o400o1-ssHnQc9M2G2yMbua5opioP.jpg" width="200" /><br/>

- 任职于安谋科技（Arm China），与 Arm 基础设施业务线（Infra LoB）紧密合作。该职位涉及推动 ARM 基础设施产品（服务器和网络）从初步评估到最终部署的全过程。
- Apache Bigtop 项目管理委员会（PMC）成员，Apache Bigtop 前任主席（2021~2023）。
- Apache Ambari 项目管理委员会（PMC）成员，提交者。
- guyuqi@apache.org