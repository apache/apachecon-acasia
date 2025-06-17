---
title: "RocketMQ 5.0 中的虚拟队列：增强与传统基于远程处理的客户端的向后兼容性"
date: ""
track: "messaging"
presenters: "Shengzhong Liu"
stype: "中文演讲"
---

Apache RocketMQ 是一个分布式消息和流式传输平台，以其低延迟、高性能和高可靠性而闻名。最新发布的 5.0 版本有两大改进：
1. 将存储与计算解耦，从而提高可扩展性和云原生适应性。
2. 引入 POP 消费模式，将负载均衡逻辑从客户端转移到 Broker。
为了适配这些特性，社区推出了基于 gRPC 的新客户端。但是，使用基于远程处理的客户端访问 RocketMQ 的现有用户无法享受 5.0 的这些改进，除非他们修改代码并替换客户端 SDK。为了增强与传统基于远程处理的客户端的向后兼容性，我们在 RocketMQ 5.0 中提出了虚拟队列解决方案，并且该方案已在腾讯云实践中得到充分验证。

### 讲师:

<img src="https://sessionize.com/image/5517-400o400o1-QHVT45RWPFxxgwib7bn9VX.jpg" width="200" /><br/>

Shengzhong Liu: 腾讯

自2019年从东南大学毕业以来，我一直在腾讯云担任软件开发工程师，近年来专注于消息队列技术。