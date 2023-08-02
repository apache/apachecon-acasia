---
title: "华为终端云在容器场景中对Apache Pulsar的优化实践"
date: "2023-08-18T14:45:00" 
track: "messaging"
presenters: "林琳"
stype: "中文演讲"
---
Apache Pulsar是一款云原生消息队列，基于其存算分离架构，通常可以在业务低峰期缩容计算层来节省资源。我们在容器化场景下，针对Apache Pulsar做了大量优化。如：
现在Pulsar负载均衡算法依赖于节点过去的负载数据，达到平衡的过程比较缓慢。当开启HPA，节点在负载均衡的过程中很可能又会触发扩容，而扩容又会引发新的负载均衡。我们要如何优化来让Pulsar更加云原生？
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230525/1930494180.jpeg" width="200" /><br>林琳: 华为, SDE专家, 华为终端 SDE 专家，Apache Pulsar PMC 成员，拥有近10年中间件与基础架构设计经验，致力于打造稳定可靠的基础设施
 <br><br>