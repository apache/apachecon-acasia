---
title: "重新思考云端 Apache RocketMQ 的高可用：面向秒级故障恢复的 Protocol-Fenced 接管"
date: ""
track: "messaging"
presenters: "Rongtong Jin"
stype: "中文演讲"
---

云端有状态消息系统的高可用，往往受制于成本、稳态性能与故障恢复速度之间艰难的权衡。基于副本（replication）的方案可以缩短恢复时间，但通常会带来额外的写放大、资源开销和运维复杂度。相比之下，单副本部署能够保持性能与成本效率，但其在 Kubernetes 中的故障恢复路径往往被缓慢且不可控的 volume detach/attach 流程所主导。

在本次演讲中，我将分享我们如何重新思考云端 Apache RocketMQ 的高可用，并构建了一套经过生产验证的架构——在稳态下不增加额外数据副本即可实现秒级故障恢复。核心思路是保持 RocketMQ 常规存储路径不变，转而围绕 Multi-Attach 块存储和 NVMe Persistent Reservation 重新设计接管路径。这种 protocol-fenced 接管模型让新节点能够安全地抢占磁盘所有权、防止脑裂，并快速恢复服务，而无需等待传统的存储迁移流程。

我将讲解整体架构、故障检测与接管流程、安全性与一致性考量，以及在 Apache RocketMQ 中的实现细节。演讲还会介绍去中心化的租约探测（lease probing）、节点侧的接管编排，以及崩溃一致性恢复（crash-consistent recovery）如何协同工作，从而缩短并稳定故障恢复的关键路径。

最后，我将分享来自阿里云的生产经验——这套架构已部署于 Apache RocketMQ 服务，并通过了大规模容灾演练的验证。本议题背后的底层工作也被 FSE 2026 Industry track 收录，而本次演讲将聚焦于生产架构、工程权衡，以及从 Apache RocketMQ 中总结的实践教训。听众将获得在云原生环境下设计高可用有状态消息系统的实用洞察，并学会在真实生产系统中如何在恢复目标与成本、性能之间取得平衡。

### 讲师:


<img src="https://cdn.sessionize.com/image/c982-400o400o1-fRQaABrX2ckEWrDpwXmMNW.jpg" width="200" /><br/>

Rongtong Jin：阿里云技术专家，Apache RocketMQ PMC 成员

Rongtong Jin 是阿里云的技术专家，也是 Apache RocketMQ 的 PMC 成员。他从事云端消息系统的架构设计与生产运维，专注于高可用、存储可靠性和大规模有状态服务。他在 Apache RocketMQ 的云化演进、生产落地和稳定性工程方面拥有丰富经验。
