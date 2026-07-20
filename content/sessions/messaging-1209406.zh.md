---
title: "TDMQ for Apache Pulsar 的挑战与突破：多模态存储与延迟消息"
date: "2026-08-07T15:00:00"
track: "messaging"
presenters: "Xiaolong Ran"
stype: "中文演讲"
room: "静宜厅"
---

在 Apache Pulsar 的大规模部署中，存储架构与延迟消息是两个绕不开的核心挑战。

在延迟消息方面，社区方案在处理大量、延迟时间随机分布的延迟消息时，会遇到消息空洞（message hole）、索引内存占用过高以及索引加载时间过长等问题。虽然通过扩分区、加带宽、扩内存可以在一定程度上缓解这些问题，但其成本高得令人难以承受，也很难标准化为云产品。本次演讲将分享 TDMQ for Apache Pulsar 如何应对这些挑战，在实现稳定的大规模延迟消息的同时显著降低资源成本。

在延迟消息方面，社区方案在处理大量、延迟时间高度随机分布的延迟消息时会面临若干挑战，包括订阅进度对象内存占用过高、延迟消息索引加载时间过长等。尽管通过扩分区、加带宽、扩内存可在一定程度上缓解这些问题，但从经济角度看成本高得难以承受，从云产品标准化的角度也难以灵活适配多样的业务场景。本次演讲将分享 TDMQ for Apache Pulsar 应对这些挑战的优化思路与生产实践，保障大规模延迟消息的稳定运行，同时显著降低资源成本。

这两个议题都基于 TDMQ 团队的真实生产经验，旨在为云端大规模 Pulsar 部署提供有价值的参考。

### 讲师:


<img src="https://cdn.sessionize.com/image/252a-400o400o1-h3njznGdpVYDR3J9gMCkjd.jpg" width="200" /><br/>

Xiaolong Ran：腾讯云中间件高级研发工程师

Apache Pulsar Committer，Pulsar Go Functions、Go Client 和 pulsarctl 的作者，同时也是 RoP 的 Maintainer 和核心开发者之一。