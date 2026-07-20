---
title: "用智能超分（Overcommitment）优化 Apache YARN 集群"
date: "2026-08-07T16:45:00"
track: "datastorage"
presenters: "Sumit Puri, Wasif Khan"
stype: "英文演讲"
room: "万寿山会议室"
---

运行 Apache Spark、Apache Tez 和 MapReduce 等计算框架的 Apache YARN 集群，常因静态的、由用户定义的资源分配而出现严重的低效。这会导致过度配置、利用率低下和基础设施成本攀升，同时需要持续的人工调优才能维持性能。
本次演讲介绍一种优化 YARN 的方法，通过实时、智能的资源管理来提升集群效率。该方法通过理解工作负载随时间变化的行为，并结合集群的实时状况做出动态决策，无需改动应用即可改善资源在各节点间的利用方式。
该方案在设计上内置了周全的防护措施，以确保在生产环境中的稳定性与可靠性，让组织能够在不损害应用性能或服务级别目标（SLO）的前提下采纳它。
本次演讲分享了一套以结果为导向、带来显著成效的方法：容器吞吐量提升了 100%，应用吞吐量提升了约 28.5%。与此同时，所需的活跃 YARN 节点数减少了 33%，直接缩减了基础设施占用。这些收益源于全集群范围内 CPU 与内存利用率的显著改善。
通过实现更智能、实时的资源分配，这套方法可以帮助组织提升吞吐量、降低基础设施成本，并简化集群运维。

详细讲解及视频 Demo 请参见此博客：https://engineering.acceldata.io/how-we-optimized-yarn-clusters-using-intelligent-overcommitment/


### 讲师:


<img src="https://cdn.sessionize.com/image/5502-400o400o1-Xudbf8rTBpCFNcw8zQnqsN.jpg" width="200" /><br/>

Sumit Puri：Acceldata Inc. 高级软件工程师

Sumit Puri 是 Acceldata 的高级软件工程师，从事大规模数据基础设施与资源优化系统的工作。他的工作重心是通过智能资源管理、实时遥测与预测建模，提升 YARN 与 Kubernetes 环境下的集群效率。

他在使用 Go、Kubernetes，以及 Spark、Tez 等大数据框架构建分布式系统方面有丰富的一手经验。他近期的工作探索了节点级优化策略、工作负载指纹识别以及自适应超分技术，以在保持稳定性的同时最大化基础设施利用率。


<img src="https://cdn.sessionize.com/image/0c3f-400o400o1-K7zab49Sy9ANFPEDSgMzt6.jpg" width="200" /><br/>

Wasif Khan：Acceldata 首席工程师

Acceldata 首席工程师，从事大数据可观测性解决方案的工作。