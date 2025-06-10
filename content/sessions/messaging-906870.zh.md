---
title: "使用 Apache RocketMQ 赋能无服务器消息架构"
date: ""
track: "messaging"
presenters: "Juntao Ji"
stype: "中文演讲"
---

我们最新的研究成果已被 ACM FSE 2025 行业专题收录，Apache RocketMQ 为无服务器消息系统奠定了坚实的基础，解决了传统中间件在可扩展性、成本和元数据方面的挑战。通过解耦存储和计算，Apache RocketMQ 实现了独立的资源扩展，这对于不可预测的云工作负载至关重要。其弹性写入分区消除了单队列吞吐量限制，而轻量级消息队列则以最小的冷启动延迟支持数百万个队列。

我们通过基于 RocketMQ 的 RabbitMQ 实现证明了这一点，该实现在克服 RabbitMQ 扩展限制的同时，保留了完整的协议兼容性。借助 RocketMQ 的架构，我们实现了无限的水平扩展能力，并将元数据管理效率提高了 1000% 以上。该无服务器解决方案已在阿里云上商业化运营。我们的经验表明，RocketMQ 能够将传统消息系统转型为云原生服务，为面向未来的无服务器架构提供了蓝图。

### 讲师:

<img src="https://sessionize.com/image/dd3d-400o400o1-JenBFKL54ncn91nqVyA8nE.jpg" width="200" /><br/>

Juntao Ji

阿里云计算高级中间件研发工程师，负责 RocketMQ 和 RabbitMQ 的功能开发。Apache RocketMQ 开源社区贡献者。在 CCF-A 会议或期刊（ASE 23'、FM 24'、FSE 25' 等）发表多篇顶级论文。