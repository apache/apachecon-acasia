---
title: "Apache Gluten 和 Apache Celeborn 在小米的生产实践"
date: ""
track: "datastorage"
presenters: "Yongyuan Liang"
stype: "中文演讲"
---

本次演讲将深入探讨 Apache Gluten 和 Apache Celeborn 在小米的实际应用情况，涵盖技术背景、部署历程、挑战以及未来规划。

1. 技术背景
小米构建了一个以 Spark 为核心的大规模离线计算平台，支持每天运行超过 100,000 个离线作业。本节将介绍小米在离线计算中依赖的核心技术架构和关键组件，以及 Gluten 和 Celeborn 的定位。

2. Gluten 在生产环境中的应用
通过采用 Gluten，小米实现了作业运行时间和资源成本的平均降低超过 30%。我们将分享部署步骤、优化策略以及在集成过程中遇到的关键挑战。

3. Celeborn 在生产环境中的应用
Celeborn 在解决 Spark External Shuffle Service 的不稳定性方面发挥了关键作用，显著提高了资源利用率并降低了总体成本。我们将展示其在真实场景中的应用以及我们采用的性能调优技术。

4. 未来规划
我们将简要分享小米对 Spark 的未来计划，重点关注性能优化、稳定性提升以及新功能的引入方向。

### 讲师:

<img src="https://sessionize.com/image/791b-400o400o1-MfKwkHsY6VSRSHfZmGQa7o.jpg" width="200" /><br/>

Yongyuan Liang

Yongyuan Liang，计算引擎研发工程师，负责计算引擎的开发工作。