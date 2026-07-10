---
title: "一种新的消费者 Offset 策略——'从现在起，我想要每一条消息'"
date: ""
track: "streaming"
presenters: "Jiunn-Yang Huang"
stype: "中文演讲"
---

Kafka 的 auto.offset.reset 只提供 earliest、latest 和 none 三种选择，但没有一种能满足最常见的诉求："从现在开始消费，但一条消息都不要漏"。latest 在分区扩展或日志截断时会悄悄丢数据；earliest 会强制重新处理海量历史数据；而 by_duration 由于动态时间戳计算，仍然存在丢数据的风险。
本次演讲介绍一种新的 offset 重置策略：by_start_time。它以消费组的创建时间戳作为唯一、稳定的锚点，统一处理所有场景——已有分区、新增分区，以及 offset 越界——全部通过一次 ListOffsetsRequest 完成，没有任何隐藏的分支。我们将梳理该 KIP 的设计演进、其中的权衡，以及对最终用户的实际影响。
目标听众：
任何有 Kafka 消费者实战经验、并在生产环境中遇到过 offset 重置问题的人。如果你曾在深夜调试过因分区扩展导致的数据丢失，或是对 auto.offset.reset 各选项之间的语义差异感到困惑，这场演讲正适合你。
核心收获：
(1) 理解现有策略在分区扩展与日志截断时是如何丢数据的。
(2) 掌握 by_start_time 的核心设计——一条以消费组创建时间戳为锚点、覆盖所有重置场景的统一规则。
(3) 了解该 KIP 的设计演进与已知局限。

### 讲师:


<img src="https://cdn.sessionize.com/image/1452-400o400o1-JyMyZrzbPcSemqnPycYmag.jpg" width="200" /><br/>

Jiunn-Yang Huang：后端工程师

我是一名后端工程师，也是 Apache Kafka 的贡献者。我热爱学习分布式系统和事件流——尤其是它们如何驱动大规模的实时数据平台。
