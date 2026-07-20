---
title: "Kafka Streams 4.2.0 死信队列（DLQ）：从手工变通到内置的事务安全"
date: "2026-08-09T15:45:00"
track: "streaming"
presenters: "Eric Chang"
stype: "中文演讲"
room: "圆明厅"
---

在 Kafka Streams 中处理坏记录（bad record）乍看很简单：捕获坏记录，把它写到另一个 topic，然后继续。但在实践中，一旦牵涉到反序列化错误、自定义异常处理器和 exactly-once 处理，事情就变得更微妙了。

本次演讲是对 KIP-1034：Kafka Streams 中的死信队列（Dead Letter Queue）的实战讲解，这是一项由 Damien Gasparina 发起、并由 Damien Gasparina、Loic Greffier 和 Sebastien Viale 共同撰写的 Kafka 改进提案。我并非该 KIP 的作者；本次演讲是一名工程师对该特性的研读，以及借助可运行示例所做的实践探索。

在 Kafka 4.2.0 之前，增加一个死信队列往往意味着要编写并维护自定义的异常处理器、一个独立的 producer、producer 的生命周期代码，还要手工处理 source topic、分区、offset、异常类型、消息和堆栈跟踪等 header。Kafka Streams 4.2.0 引入了内置的死信队列支持，只需几行配置即可启用。Kafka Streams 会创建默认的死信队列记录，自动添加标准的错误 header，并通过其内部 producer 路径发送出去。

我们将对比 KIP-1034 之前的手工死信队列实现与 Kafka 4.2.0 的做法，然后看看为什么这对事务安全很重要。使用手工的 DLQ producer 时，死信队列的写入位于 Kafka Streams 的事务边界之外。如果该写入被提交，而随后 Streams 事务被中止，那么同一条坏输入记录可能会被重试，并再次被写入死信队列。KIP-1034 弥合了这一缺口，让死信队列的写入与正常输出记录一样，走 Kafka Streams 的内部写入路径。

听众离场时将获得一个实用的思维模型，了解 KIP-1034 在何时能帮上忙、它解决了哪些问题，以及如何从 Kafka Streams 中临时的（ad hoc）死信队列实现迁移过来。

参考资料：

- [关于本次演讲内容的博客文章](https://blog.unknowntpo.me/blog/kafka-kip-1034-dlQ)
- [KIP-1034](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1034%3A+Dead+letter+queue+in+Kafka+Streams)
以下是该 KIP 的链接：

### 讲师:


<img src="https://cdn.sessionize.com/image/66b0-400o400o1-UHasfsGgbmwaRvqqXqtoL1.png" width="200" /><br/>

Eric Chang：Apache Gravitino Committer、Apache Kafka 贡献者，以及 OpenSourceForYou（由 Chia-Ping Tsai 创立的、活跃的台湾开源社区）成员

Eric Chang 是驻台湾的 Apache Gravitino Committer 和 Apache Kafka 贡献者。他同时也是 OpenSourceForYou（由 Chia-Ping Tsai 创立的、活跃的台湾开源社区）的成员。Eric 对后端系统、Kafka 和分布式数据处理感兴趣，并通过带有可运行示例的技术文章来讲解实际的工程问题。他近期的工作聚焦于 Kafka Streams 的 KIP-1034，以及内置死信队列支持如何改变应用在 exactly-once 处理下处理坏记录的方式。