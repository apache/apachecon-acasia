---
title: "Eloq ConvergedDB on Apache Cassandra: Built for Agentic AI"
date: ""
track: "datastorage"
presenters: "Hubert Zhang, Lintao Zhang"
stype: "英文演讲"
---

我们正迅速进入 **智能体应用时代**，在这个时代，AI 驱动的智能体不仅能够辅助人类，还能自主做出决策并管理任务。然而，支撑这些应用的数据基础设施在可扩展性、一致性和性能方面面临着重大挑战。

随着 Apache Cassandra 5.0 引入 **向量搜索** 功能，它已成为关键的 AI 数据库。然而，**智能体应用需要的不仅仅是向量能力**。在本次会议中，我们将首先探讨 Cassandra 5.0 的向量搜索特性，分析现有解决方案的关键局限性，并介绍 **基于 Apache Cassandra 的 Eloq ConvergedDB**，这是一种旨在克服这些挑战的创新方法。

如今，借助 [**LangChain**](https://www.langchain.com/) 和 [**LlamaIndex**](https://www.llamaindex.ai/) 等平台，开发者可以无缝地将多个数据库集成到 AI 工作流中，实现多模态数据的高效存储和检索。然而，这种方法往往带来几个挑战。

第一个挑战是 **管理复杂性**。AI 应用通常需要多个数据库来管理不同类型的数据。每个数据库来自不同的供应商，需要专门的技能集，并且具有独特的备份和故障恢复流程。不同数据库系统之间的备份策略和故障恢复操作差异显著，增加了整体基础设施管理的复杂性。

第二个挑战与 **灵活性和敏捷性** 有关。现代数据库通常设计用于处理特定类型的工作负载，在特定的性能范围内运行。例如，Redis 设计用于解决延迟问题，但牺牲了持久性；而 PostgreSQL 通过牺牲可扩展性来保证持久性。

第三个挑战是确保 **多个数据库之间的数据一致性**。AI 应用通常需要结合来自不同来源的数据，这引入了事务性挑战。传统数据库提供 ACID 事务语义，以简化应用开发的复杂性。然而，当查询需要由多个数据库执行时，这一宝贵特性就会丧失。

为了克服上述限制，我们提出了基于 Cassandra 的一站式解决方案 ConvergedDB，它能够：

- 消除可扩展性担忧：ConvergedDB 的架构确保无论业务是垂直增长还是水平增长，都能实现无缝扩展。
- 确保一致性：随着多智能体架构成为常态，ConvergedDB 的跨模型事务保证将证明其价值。
- 保持高性能：ConvergedDB 在不降低性能的情况下，为最苛刻的 AI 应用提供了稳健的解决方案。

AI 应用的未来需要可扩展、一致且高性能的数据基础设施。基于 Cassandra 的 ConvergedDB 在这三个方面都表现出色，使开发者能够专注于创新而非基础设施。

### 讲师:

<img src="https://sessionize.com/image/a965-400o400o1-E9kixxxRCcLxkKoQ9y7dRC.png" width="200" /><br/>

Hubert Zhang: EloqData CTO

Hubert Zhang 是 EloqData 的首席技术官（CTO）。在加入 EloqData 之前，Hubert 曾是 VMware Greenplum 数据库的技术负责人。他还是 Apache HAWQ 项目管理委员会（PMC）的成员。

<img src="https://sessionize.com/image/2f8b-400o400o1-MyxGEXHK65dpEA5LW96TB8.jpg" width="200" /><br/>

Lintao Zhang: Co-founder and CEO, EloqData

Lintao Zhang 是 EloqData 的联合创始人兼首席执行官，为人工智能时代的应用构建下一代数据库基础设施。 此前，他是微软研究院的合作伙伴研究经理，从事云基础设施、分布式系统和人工智能方面的研究。他是 PacificA 复制协议的发明人，该协议被用于 Apache Kafka、Apache Pegasus 和 ElasticSearch。他在顶级会议上发表了 50 多篇论文，并获得了许多研究奖项。林涛是 IEEE Fellow 和 ACM Distinguished Member。他拥有北京大学学士学位和普林斯顿大学博士学位。