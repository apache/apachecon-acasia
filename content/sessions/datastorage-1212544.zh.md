---
title: "从愿景到生产：Apache Fluss 如何定义实时数据湖仓的存储层"
date: "2026-08-07T15:00:00"
track: "datastorage"
presenters: "Yang Wang"
stype: "中文演讲"
room: "万寿山会议室"
---

去年的 Community Over Code Asia 上，我们介绍了 Apache Fluss，以及它为实时湖仓打造专用存储层的愿景。经过几个版本的迭代，这一愿景已在阿里巴巴双十一规模的生产中得到验证。

在本次演讲中，我们将围绕三个主题介绍已交付的成果。第一，将计算下推到存储：聚合合并引擎（Aggregation Merge Engine）把实时聚合——包括基于 RoaringBitmap 的 UV 去重——下推到存储层，并内置 exactly-once 语义；日志过滤下推（log filter pushdown）则把谓词求值从计算侧移到存储侧，使 Flink 能够把聚合、join 和宽表状态完全卸载到存储。第二，生态与数据模型演进：用于灵活查询模式的二级索引、Change Data Feed、复杂数据类型、零拷贝模式演进，以及多语言客户端（Rust、Python、C++）。第三，企业级基础设施：目标驱动的 rebalance、零停机滚动升级、快速的 Coordinator 恢复、带三级 ACL 的 SASL 认证，以及深度的 RocksDB 诊断。


### 讲师:


<img src="https://cdn.sessionize.com/image/caa5-400o400o1-7N761jmkijrU21jsU1NuAN.jpg" width="200" /><br/>

Yang Wang：阿里云高级主任工程师，杭州，Apache Fluss 核心开发者

Yang Wang 是阿里云高级主任工程师，也是面向实时分析的流式存储系统 Apache Fluss 的核心开发团队成员。他专注于存储引擎内部实现——包括 KV 存储（RocksDB 集成、性能调优、监控与内存管理）、聚合合并引擎、二级索引支持，以及 Flink connector 的增强（如过滤下推、lookup join）。他是 Apache Fluss 开源社区的活跃贡献者。