---
title: "Kafka 4.0 核心亮点：新特性、移除项与升级指南"
date: "2025-07-26T17:15:00"
room: "圆明厅"
track: "streaming"
presenters: "Jiunn-Yang Huang, Chia-Ping Tsai, PoAn Yang, TengYao Chi, YiHuan LEE, Kuan Po Tseng"
stype: "中文演讲"
---

虽然 Kafka 4.0 已经引起了广泛的讨论，但大多数讨论都集中在主要功能上，如 ZooKeeper 的移除或新 API 的引入。在本环节中，我们将重点介绍Kafka 4.0中一些鲜为人知但同样重要的变化。这些更新可能并不引人注目，但它们会对你在实际环境中如何配置、操作和调试Kafka产生重大影响。

用户面临的主要问题之一是如何升级到 Kafka 4.0。KIP-896 删除了对 2.0 及以下版本协议的支持，而 KIP-1124 则为升级 Kafka 客户端、Connect 和 Streams 提供了官方指导。在服务器端，用户必须确保与 JDK 兼容，并考虑如何从基于 ZooKeeper 的设置过渡到新架构。本节将介绍升级过程中需要牢记的最关键注意事项。

Kafka 测试框架也经历了重大演变。以前，测试是使用重继承设计编写的，子类从父类继承集群设置逻辑。这使得测试难以理解和调试，经常会引入隐藏的依赖关系和不必要的配置。新的测试框架通过使用 @ClusterTest 等 JUnit 注释简化了这一问题，使测试逻辑更清晰、更模块化、更易于维护。

Kafka 4.1 还将在如何处理机架感知再平衡方面引入更智能的行为。在早先的版本中，存储机架信息是通过


### Speakers:

<img src="https://sessionize.com/image/1452-400o400o1-JyMyZrzbPcSemqnPycYmag.jpg" width="200" /><br/>

Jiunn-Yang Huang: 后端工程师

我是一名为 Apache Kafka 做出贡献的后端工程师。我喜欢学习分布式系统和事件流，尤其是它们如何为大规模实时数据平台提供动力。去年，我提交了 100 多条建议，并致力于 Kafka 的内存优化。

<img src="https://sessionize.com/image/2d3c-400o400o1-S4UZTbkX3EfAsvqD57soTa.jpg" width="200" /><br/>

Chia-Ping Tsai: Apache 成员、Apache HBase PMC 成员、Apache Kafka PMC 成员、Apache YuniKorn PMC 成员

撰写分布式系统论文，成为博士。为分布式系统贡献代码，成为 PMC 成员。享受分布式系统，成为有价值的人


<img src="https://sessionize.com/image/cdca-400o400o1-KCJ6DRaPTfEdWiiTQ4Zzxy.jpg" width="200" /><br/>

PoAn Yang: ASF, Apache YuniKorn committer

我是一名开源软件爱好者，主要关注 Apache Kafka。我是前 20 名贡献者之一，我的工作包括增 AsyncKafkaConsumer 和开发下一代组协调器。


<img src="https://sessionize.com/image/b096-400o400o1-4neD1RFWbr1BXxdKrF69st.jpg" width="200" /><br/>

TengYao Chi: Apache Kafka Committer

TengYao 白天是一名软件工程师，晚上则是一名开源贡献者。
在过去的一年中，他是 Apache Kafka 所有贡献者中在过去 12 个月中提交次数最多的人。他的大部分贡献来自 async consumer、下一代组协调协议和 log4j2 的迁移。

他还喜欢企鹅。


<img src="https://sessionize.com/image/c5ac-400o400o1-DuGnE5zsb5qfQTHAKajgzb.jpg" width="200" /><br/>

YiHuan LEE: 国立成功大学研究生

我的研究重点是 “负载平衡对 Kafka 性能的影响”。

<img src="https://sessionize.com/image/4f33-400o400o1-U8VTJGFMti2BRV8KsAi6VB.png" width="200" /><br/>

Kuan Po Tseng: ASF, Apache Kafka 贡献者

我对 Kafka 确实充满热情，并致力于提高其性能、优化工具和增加测试覆盖率。与一群志同道合的朋友一起，我们一直在努力让Kafka变得更好。每当我为开源社区做出贡献时，我都感到非常兴奋，因为我们不仅仅是在增强Kafka的功能，我们还在构建一个更强大、更灵活的生态系统，让全球用户受益。对我来说，这是一个不断探索和挑战的旅程，让Kafka成为最好的Kafka是我一直努力的目标！