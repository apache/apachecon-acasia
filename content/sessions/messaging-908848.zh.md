---
title: 构建云 MQTT 解决方案的经验教训
date: '2026-08-08T14:30:00'
room: 静宜厅
track: messaging
presenters: Senze Zhang
stype: 中文演讲
depth: advanced
practice_level: 4
projects:
- rocketmq
audience:
- 架构师
- 开发者
- SRE/运维
related_sessions:
- 小米 RocketMQ-MQTT 最佳实践：提升质量和成本效率之旅
- Apache Pulsar 在腾讯云上的高可用性最佳实践
- RocketMQ 5.0 中的虚拟队列：增强对 Remoting 协议客户端的向后兼容性
- 使用 Apache RocketMQ 赋能无服务器消息架构
- 消息系统可观察性最佳实践：Apache RocketMQ 和 OpenTelemetry 案例研究
---
MQTT 已成为物联网 (IoT) 的事实标准，为汽车、制造、电信、石油天然气等行业的众多应用提供支持。

在腾讯云，我们开发了基于共享弹性流日志的稳健云 MQTT 解决方案。在本次演讲中，我们将分享开发过程中的关键见解和经验教训。我们将首先概述整体架构，重点介绍性能优化，并分享最佳实践。接下来，我们将深入探讨如何在共享日志之上实现 MQTT 协议——这种设计可扩展以支持其他消息传递协议。我们还将探讨动态扩展系统以支持数百万连接设备并保持高性能和可靠性的策略。最后，我们将讨论如何将存储和计算分离，并结合专用的 MQTT 负载均衡器，帮助我们降低总体拥有成本 (TCO)，并灵活高效地应对流量高峰。

### 讲师:

<img src="https://sessionize.com/image/8338-400o400o1-J1yXkRRbD17bMbsVpMyBw8.png" width="200" /><br/>

Senze Zhang: Apache RocketMQ Committer

Senze Zhang 是一位资深的消息队列系统工程师，在高性能消息解决方案的设计、实现和优化方面拥有丰富的经验，参与部署过 RocketMQ、Kafka、MQTT 等多个业界领先的消息队列平台。