---
title: "RocketMQ 5.0 中的虚拟队列：增强对 Remoting 协议客户端的向后兼容性"
date: "2025-07-26T16:15:00"
room: "静宜厅"
track: "messaging"
presenters: "Shengzhong Liu"
stype: "中文演讲"
---

Apache RocketMQ 是一个以低延迟、高性能和高可靠性著称的分布式消息与流处理平台。最新发布的 5.0 版本带来了两项重大进步：
1. 实现了存储与计算的解耦，进一步提升了系统的可扩展性和云原生适配能力。
2. 引入了 POP 消费模式，将负载均衡逻辑从客户端迁移到了 Broker 端。
为适应这些新特性，社区推出了全新的基于 gRPC 协议的客户端。然而，现有通过 Remoting 协议客户端接入 RocketMQ 的用户，若不更新代码和替换客户端 SDK，将无法享受到 5.0 的这些创新能力。为增强对 Remoting 协议客户端的向后兼容性，我们在 RocketMQ 5.0 中提出了虚拟队列方案，并已在腾讯云的实际应用中得到了充分验证。

### 讲师:

<img src="https://sessionize.com/image/5517-400o400o1-QHVT45RWPFxxgwib7bn9VX.jpg" width="200" /><br/>

Shengzhong Liu: 腾讯

自2019年从东南大学毕业以来，我一直在腾讯云担任软件开发工程师，近年来专注于消息队列技术的相关工作。