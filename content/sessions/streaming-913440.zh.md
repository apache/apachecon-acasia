---
title: "Kwai Flink 云原生架构演进"
date: "2025-07-25T17:45:00"
track: "streaming"
presenters: "Mang Zhang, Heart Zhou"
stype: "中文演讲"
room: "圆明厅"
---

经过多年的发展，Kwai Flink 的资源规模已达到数百万内核，覆盖整个集团的所有业务场景，集群中运行的作业数以万计。然而，Flink 集群表现出明显的负载波动效应，成本问题日益突出，同时在集群扩展和运维方面也面临挑战。

Kubernetes（K8S）已经成熟并被广泛采用，引擎的云迁移已成为行业趋势。K8S 可以将分散的资源池统一用于在线服务、实时计算和离线计算，通过相互负载均衡最大化集群中的资源利用率。因此，Flink 的云原生转型迫在眉睫。此外，统一在 K8S 技术栈下还能降低运维与开发成本。

Kwai 经历了三个主要阶段： Flink On YARN、Flink On YARN On K8S 和 Flink Native On K8S。本演讲将讨论 Kwai 在 Flink 云迁移过程中遇到的挑战、解决方案和收益。

### 讲师:


<img src="https://sessionize.com/image/d342-400o400o1-wMgMNhMG7uPCpRJT7o2iXT.jpg" width="200" /><br/>

Mang Zhang: Flink Contributor

10 年大数据引擎开发和大数据架构师经验。丰富的大数据实时和离线经验，擅长大数据场景的架构和方案设计。


<img src="https://sessionize.com/image/ac91-400o400o1-7VFwoH4QWgUqtcDeshVnqZ.jpg" width="200" /><br/>

Heart Zhou: Kwai

流媒体工程师