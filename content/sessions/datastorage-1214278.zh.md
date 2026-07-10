---
title: "Paimon-cpp：为 Apache 生态带来原生高性能的湖仓访问"
date: ""
track: "datastorage"
presenters: "Xinyu Liu"
stype: "中文演讲"
---

Apache Paimon 已成为 Apache 生态中开发最活跃的湖仓格式之一。随着原生查询引擎越来越希望在不引入 JVM 开销的情况下直接访问湖仓数据，我们很高兴地介绍 Paimon-cpp——一套从头构建、高性能的 Apache Paimon 格式 C++ 实现，目前正贡献给 Apache Paimon 社区。

在本次演讲中，我们将涵盖：

- **为什么是 Paimon-cpp**：构建原生 C++ 实现的动机——在基于 JVM 的数据湖生态与日益壮大的原生查询引擎世界之间架起桥梁，同时与 Java 版 Paimon 保持完全的线协议兼容（wire-compatibility）。

- **格式与特性**：Paimon-cpp 为 append 表和主键表都提供完整的读/写/compaction 支持，包括 Merge-On-Read（MOR）和 Deletion Vector（DV）场景。它还支持模式演进、谓词下推、面向 AI 的数据演进模式，以及多种索引类型（如向量检索、全文检索）。

- **性能优化**：浅拷贝数据交换、用于预读的文件预取（prefetch）、面向主键表的多线程异步行列转换，以及 Blob I/O 优化。

- **架构与可扩展性**：构建在 Apache Arrow 列式内存格式之上，采用模块化、插件化的架构，为文件系统、文件格式、内存管理、执行器和可观测性提供了定义良好的接口——设计上便于嵌入任意原生引擎。

- **最佳实践与上手指南**：关于配置读/写/compaction 流水线、面向生产负载的调优，以及把 Paimon-cpp 集成到你自有引擎的实操指南。

Paimon-cpp 正积极贡献给 Apache Paimon 项目，预计在本次演讲之时已成为 Apache 官方仓库的一部分。我们热忱欢迎开发者、引擎构建者和数据爱好者试用、反馈问题并贡献代码——无论是新功能、bug 修复、文档，还是与你钟爱的原生引擎的集成。让我们共同打造原生的湖仓生态！

### 讲师:


<img src="https://cdn.sessionize.com/image/581f-400o400o1-wHvbmZBcWsHGkZircGN71i.jpg" width="200" /><br/>

Xinyu Liu：阿里巴巴高级软件工程师 | Paimon-cpp Maintainer | 3 年 Paimon 经验

我是阿里巴巴存储服务团队的高级软件工程师。我从事 Paimon-cpp 工作已有 3 年，目前担任 Paimon-cpp 开源库的 maintainer，并负责推动 Paimon-cpp 在阿里巴巴内部数据基础设施中的落地。在 Paimon 之前，我负责 Khronos——一个支撑阿里巴巴集团监控系统存储与检索的时序数据库。我的经验涵盖存储引擎设计、高性能数据格式以及系统级优化。我对开源协作充满热情，期待与 Apache 社区共同建设原生湖仓生态。
