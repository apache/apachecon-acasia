---
title: "Apache Flink 的分散式狀態管理"
date: ""
track: "streaming"
presenters: "Zhaoqian (Zakelly) Lan"
stype: "中文演讲"
--- 

過去十年，Flink 的部署模式、工作負載模式及硬體技術均經歷了革命性的演進。從 MapReduce 時代緊密耦合的計算-儲存節點，我們已轉向以 Kubernetes 容器化部署為常態的雲原生環境。为充分适应这一转变，Flink 2.0 引入了分布式状态管理，以分布式文件系统（DFS）作为主要存储介质。这一架构创新既解决了云原生环境带来的关键挑战，又实现了更高的可扩展性、性能和灵活性。
在本场会议中，我们将介绍Flink 2.0中存储与分布式状态管理的设计理念，包括远程状态集成、异步状态访问框架，以及专为DFS存储介质设计的全新状态后端。

### 讲师:

<img src="https://sessionize.com/image/9fb0-400o400o1-3GuCetdzM1ZnG45ZrGcUgh.jpg" width="200" /><br/>

Zhaoqian（Zakelly）兰多年来一直致力于开源项目，是Apache Flink项目的活跃PMC成员及提交者。他专精于流处理与键值存储技术。目前，赵谦就职于阿里云，专注于提升Flink的状态管理与检查点功能，推动技术创新与效率优化。