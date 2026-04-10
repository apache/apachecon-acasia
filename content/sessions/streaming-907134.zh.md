---
title: 利用流式图计算加速多流连接
date: '2026-08-07T14:00:00'
room: 圆明厅
track: streaming
presenters: Zhao Qingwen
stype: 中文演讲
depth: advanced
practice_level: 3
projects:
- flink
- spark
audience:
- 架构师
- 开发者
related_sessions:
- 统一调度器：支持流计算、批处理与图计算
- Flex：统一的流式和批处理矢量化引擎
- 当 Flink 遇见 Fluss：流式数据仓库的未来
- 蚂蚁集团基于 Apache 技术栈构建的新一代高 SLA 流式计算系统
- 使用外部状态和动态表实现可扩展的连接和聚合
---
流式计算在异常检测、搜索、推荐系统、金融交易等领域正变得越来越重要。传统的流式计算引擎（如 Flink 和 Spark Streaming）通常使用基于表的连接操作来处理多流连接场景。然而，随着分析维度的加深，这些基于表的流式引擎面临着显著的性能限制。开源流式图计算引擎 GeaFlow 以一种新颖的方法打破了这些限制。它不仅利用图数据中固有的关系高效地执行多跳查询，还集成了内置的增量图算法。这些算法显著减少了计算中涉及的子图规模，同时仍然提供与全图计算相当的结果。本主题探讨了传统流式引擎在多流连接分析中的局限性，并解释了 GeaFlow 作为流式图引擎如何通过图原生特性和独特的增量算法来加速分析性能。

### 讲师:

<img src="https://sessionize.com/image/b616-400o400o1-G8HEVFg7VaTfKEYWtC3oA7.jpg" width="200" /><br/>

Zhao Qingwen: 蚂蚁集团, 工程师

2019年加入蚂蚁集团，是GeaFlow的核心开发者之一。