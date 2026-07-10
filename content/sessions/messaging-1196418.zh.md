---
title: "Apache RocketMQ 路由控制面演进"
date: ""
track: "messaging"
presenters: "Xiao Yang"
stype: "中文演讲"
---

本次分享将讲解我们如何为 Apache RocketMQ 演进出一套轻量级的外部路由控制面，在不改动 broker、nameserver 以及客户端访问模式的前提下，支撑大规模集群的治理。

随着多条业务线逐步共用同一个集群，真正的挑战从吞吐量转向治理：更快的故障收敛、可控的 topic 迁移，以及灵活的基于泳道（lane）的流量隔离。在本次演讲中，我将说明为什么这些问题更适合在路由层解决，为什么现有的 NameServer 和 Broker 机制并不足够，以及如何将 broker 写隔离、topic 迁移和基于泳道的流量隔离统一在同一个控制面中，从而以更小的爆炸半径、更可控的治理方式支撑大规模集群的拆分。

### 讲师:


<img src="https://cdn.sessionize.com/image/ed42-400o400o1-3Jm5SmqbknYn3ZeVXQQXY2.jpg" width="200" /><br/>

Xiao Yang：同程旅行，消息中间件核心开发者

我是来自同程旅行基础架构工程团队的 Xiao Yang。我主要负责消息中间件的架构演进与维护。我热爱开源，是 Apache ShardingSphere 的 committer，同时也是 Apache RocketMQ 的活跃贡献者。
