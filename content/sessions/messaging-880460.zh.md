---
title: "Apache Pulsar 在大规模分区环境下的指标收集实践"
date: ""
track: "messaging"
presenters: "lin lin"
stype: "中文演讲"
--- 

Apache Pulsar 是一个高性能消息队列，支持海量 Topic，允许用户在单个集群内创建数十万甚至数百万个分区。指标是我们在生产环境中识别和诊断问题的关键工具。可观察性的有效性直接影响故障排除的速度。
在分区数量众多的场景下，启用 Topic 级指标可能会在短时间内生成大量指标字符串，从而导致严重的内存波动，并可能导致集群不稳定。
本次演讲将分享我们在此类高分区场景下收集指标的实践经验，并探讨如何在不影响在线内存稳定性的情况下最大限度地收集指标数据，从而实现高效的问题识别和系统监控。

### 讲师:

<img src="https://sessionize.com/image/f542-400o400o1-4vaXwyGZYAujcJxNoeruQG.jpg" width="200" /><br/>

Lin Lin，华为SDE专家，中间件技术总监，曾就职于腾讯、蚂蚁金服
专注于中间件和基础设施领域，拥有超过10年的相关经验，致力于打造高品质的基础设施
Apache Pulsar Committer & PMC成员