---
title: "Celeborn 的革新：多引擎支持、性能掌控与技术创新"
date: ""
track: "datastorage"
presenters: "Jiashu Xiong"
stype: "中文演讲"
--- 

Apache Celeborn 在过去一年中取得了显著进展，引入了新功能、性能优化以及扩展的引擎支持。

功能增强包括：
- 数据完整性的端到端验证
- 多层存储和 HybridShuffle，实现灵活的数据管理
- CLI 工具和 RESTful API，提升可用性
- 多级配额用于资源治理
- Worker 标签、动态配置等

性能改进针对：
- Spark 倾斜优化，消除倾斜场景下的额外排序
- SortShuffle 分区拆分，防止因分区不均匀导致的性能下降
- 通过优化同步瓶颈，减少 Commit 和 Fetch 阶段的延迟

引擎支持方面，现在除了现有的 MR 和 Spark 支持外，还增加了对 Blaze 和 Flink 的 HybridShuffle 支持。

此外，稳定性得到了加强，社区依然活跃，Celeborn 已成为全球许多组织首选的 shuffle 服务。

### 讲师:

<img src="https://sessionize.com/image/b0bb-400o400o1-Jde4MGnDZsTAE7Kbn5uYbL.jpg" width="200" /><br/>

Jiashu Xiong 是 Apache Celeborn 的项目管理委员会（PMC）成员，主要专注于 Apache Celeborn 的优化以及 Apache Celeborn 与 Flink、Spark 等引擎的集成。