---
title: "Flink 2.x 在腾讯的演进与生产实践"
date: ""
track: "streaming"
presenters: "Zihao Chen"
stype: "中文演讲"
---

1. 业务背景与架构演进
  a. 业务驱动：随着腾讯对实时湖仓方案以及大语言模型（LLM）数据预处理的需求激增，老旧 1.x 版本的迭代面临着人力成本高企、与开源社区日益脱节等挑战。
  b. Flink 2.x 的核心价值：Flink 2.x 所引入的增强与优化——涵盖存算分离、物化表（materialized table）、批处理优化、湖仓架构以及 AI 工作流——与腾讯的具体业务场景高度契合。

2. 引擎能力的迭代优化
  为了与开源社区更紧密地融合，我们已将一部分内部能力全面适配到 Flink 2.x 框架，并逐步回馈给社区。
  a. 计算性能：
    - 异步 I/O 优化：支持批量异步 I/O，通过批处理与异步处理技术提升吞吐。
    - Lookup Join 优化：支持批量异步 Lookup Join。
  b. AI on Flink：支持与 Triton Inference Server 集成。
  c. 增强 WindowStagger 一致性：解决了此前在开启 WindowStagger 特性时出现的窗口分配行为不一致问题。
  d. 改进运维与可观测能力：
    - 原生数据采样（Native Data Sampling）：支持对生产作业进行零侵入的数据探查，从而降低实时应用的调试与测试成本。
    - HistoryServer 优化：解决大规模生产集群中的归档瓶颈，确保历史作业的可靠可追溯。

3. 多样业务场景下的落地实践
  a. 流批一体：展示把流批一体场景升级到 Flink 2.x 后所获得的性能提升。
  b. AI 时代的实时数据流：
    - AI Functions：支持在 Flink SQL 中直接集成 AI 模型调用，构建低时延的 AI 数据处理管道。
    - PyFlink 性能优化：聚焦广告特征工程场景，分享我们如何通过优化 Python UDF 运行时显著提升特征计算效率。
  c. 超大规模状态治理：重点介绍如何利用 Delta Join 和 BiFang 来解决双流 Join 中状态过大相关的问题。

4. 未来展望：从流式计算到智能流式计算
  a. 平衡性能与成本：我们希望持续深化增量计算与物化视图的结合，实现最大化的算力复用，从而在性能与运维成本之间取得最佳平衡。
  b. 事件驱动的 AI Agents：探索 Flink Agents，把 Flink 从一个独立的数据处理引擎演进为一个事件驱动的流式 agent 框架。

### 讲师:


<img src="https://cdn.sessionize.com/image/c17d-400o400o1-3ksWtZ8Yz4P3kYR9cEC4tH.jpg" width="200" /><br/>

Zihao Chen：腾讯，资深软件开发工程师

Zihao 多年来一直从事 Flink 内核相关的研发。近年来，他主要专注于推动 Flink 2.x 的演进，以及开发 Flink 的自动扩缩容（autoscaling）能力，以保持 Flink 引擎的技术领先性，并提升 Flink 作业的稳定性与资源利用率。
