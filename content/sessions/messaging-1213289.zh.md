---
title: "Apache RocketMQ 低延迟优化的探索与实践"
date: "2026-08-09T14:30:00"
track: "messaging"
presenters: "熙凯 魏"
stype: "中文演讲"
room: "静宜厅"
---

在我们的一些使用场景中，存在严格的低延迟要求，核心诉求是将 P99 或最大延迟稳定控制在某个固定阈值之内。本次分享将介绍我们团队在 Apache RocketMQ 低延迟模式的优化与实现方面所做的探索和努力。我们从 RocketMQ 架构中的核心延迟瓶颈出发，梳理影响端到端延迟的关键环节，包括网络传输、消息调度和资源分配，并详细阐述我们针对性地进行的优化、架构调整以及实现效果的验证。此外，本议题还将分享 RocketMQ 全链路延迟调优的方法论和实践经验，希望能为社区的开发者和用户提供一些帮助。

### 讲师:


<img src="https://cdn.sessionize.com/image/6bdf-400o400o1-HSmKWKawRzfoxashePJybP.jpg" width="200" /><br/>

熙凯 魏: 腾讯云高级开发工程师

腾讯云高级开发工程师，拥有多年计算、存储及分布式系统性能优化经验。