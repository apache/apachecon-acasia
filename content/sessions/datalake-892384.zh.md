---
title: "打破数据孤岛：Apache Gravitino在哔哩哔哩的生产实践"
date: ""
track: "datalake"
presenters: "Tianhang Li"
stype: "中文演讲"
--- 

Apache Gravitino 是哔哩哔哩采用的一个统一元数据管理平台，旨在解决数据孤岛问题，实现跨异构数据源（如 Hive、Iceberg、Kafka 等）的元数据视图集成。通过端到端的血缘追踪，Gravitino 能够追溯数据从摄入、处理到服务交付的整个工作流程，从而优化资源利用，并分析模式变更带来的影响。通过整合 Iceberg 的分区策略（如截断/分桶）和分支特性，Gravitino 支持灵活的数据版本控制、多流数据拼接以及隔离的测试环境。对于人工智能驱动的场景，该平台提供了系统化的训练数据集分区和模型版本管理，确保了可重复性和简化的 AI 资产管理。这一解决方案降低了跨数据源的维护开销，增强了数据一致性，并为哔哩哔哩的 AI 应用和全企业级数据治理建立了可扩展的技术基础。

### 讲师:

<img src="https://sessionize.com/image/1f8c-400o400o1-HBNHNwxpA2kUNRMibne31Z.jpg" width="200" /><br/>

李天航是哔哩哔哩的大数据开发工程师，专注于大规模数据场景下的元数据管理和 Spark 计算引擎优化。