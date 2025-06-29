---
title: "Apache Flink 2.0 的存算分离"
date: "2025-07-25T16:15:00"
room:  "圆明厅"
track: "streaming"
presenters: "Zhaoqian (Zakelly) Lan"
stype: "中文演讲"
---

过去十年间，Flink 的部署模式、工作负载特征以及硬件技术取得了革命性的发展。从 Map-Reduce 时代紧密耦合的计算-存储节点，我们已迈入云原生时代，容器化部署（如 Kubernetes）已成为主流范式。为充分适配这一变革，Flink 2.0 引入了全新的存算分离架构，以分布式文件系统（DFS）作为主要存储介质。这一架构创新既解决了云原生环境带来的关键挑战，又实现了前所未有的可扩展性、性能和灵活性突破。

在本次分享中，我们将深入解析 Flink 2.0 的存储设计与解耦状态管理方案的核心理念，包括：远程状态集成机制，异步状态访问框架，以及面向 DFS 的新型状态后端。

### 讲师:

<img src="https://sessionize.com/image/9fb0-400o400o1-3GuCetdzM1ZnG45ZrGcUgh.jpg" width="200" /><br/>

兰兆千: Apache Flink PMC 成员和 Committer，阿里云技术专家

兰兆千多年来一直致力于开源项目，是 Apache Flink 项目的活跃 PMC 成员及 Committer。他深耕于流计算引擎与状态存储技术。目前他就职于阿里云，专注于提升 Flink 的状态管理与检查点功能，推动功能创新与性能优化。
