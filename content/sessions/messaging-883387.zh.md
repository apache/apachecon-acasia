---
title: "Apache Pulsar 在腾讯云上的高可用性最佳实践"
date: "2025-07-25T14:30:00"
room:  "静宜厅"
track: "messaging"
presenters: "韩明泽"
stype: "中文演讲"
---

Apache Pulsar 是一个云原生的分布式消息和流式传输平台。Apache Pulsar 采用存储与计算分离的架构，支持大型集群、多租户、百万级主题、跨区域数据复制、持久化存储、分层存储、高可扩展性等企业级及金融级服务。Apache Pulsar 提供统一的消费模型，同时支持消息队列和流式传输场景。它不仅能为队列场景提供企业级的读写服务质量和强一致性保证，还能为流式传输场景提供高吞吐量和低延迟。
Apache Pulsar 已在企业关键业务中落地，拥有丰富的应用场景。目前，腾讯云也已在生产实践中大规模应用 Apache Pulsar 近 5 年。在生产实践中，腾讯云对 Apache Pulsar 进行了一系列性能优化和稳定性增强，以确保用户在不同场景下系统能够稳定高效地运行。
本次演讲我们将重点讲解腾讯云上 Apache Pulsar 在高可用性方面的最佳实践，包括 Broker 集群和 Bookkeeper 集群的高可用性、Zookeeper 集群的高可用性以及跨集群的高可用性实践，希望能够为开发者提供一些参考。

### 讲师:

<img src="https://sessionize.com/image/9c17-400o400o1-JPuaxw3mCtQ2zt9Ew94C2n.jpg" width="200" /><br/>

韩明泽: 腾讯

毕业于武汉大学计算机专业。腾讯云高级研发工程师。开源社区爱好者。在美团和腾讯拥有超过 8 年的消息队列相关研发和运营经验。目前主要负责腾讯云 TDMQ for Pulsar 产品的核心部分。同时，我是 Apache Pulsar Contributor 和 RoP Maintenanceer。