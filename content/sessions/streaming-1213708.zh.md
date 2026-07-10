---
title: "GeaFlow | 流式记忆（Streaming Memory）：构建实时有状态后端，赋能 AI+Graph 场景"
date: ""
track: "streaming"
presenters: "Litao Lin, Yao Zhongqiang"
stype: "中文演讲"
---

2026 年，AI Agent 的记忆架构正在经历一次范式转变。传统 AI Agent 的记忆系统大多采用"只追加写入 + 异步索引"的批处理模式。这导致记忆更新存在显著时延，难以支撑实时交互场景下的上下文演进。记忆的本质并非一个静态数据集，而是由对话、感知和决策构成的无界数据流。如何在这条流上进行低时延的状态管理与增量计算，是流计算技术在 AI 时代面临的新挑战。
本次演讲将聚焦流计算技术如何应对记忆这一挑战。Apache GeaFlow（孵化中）是一款开源的流式图计算引擎，定位为实时增量图计算层，作为 Agent 的实时有状态后端。与缺乏原生关系建模能力的传统图数据库和流计算引擎不同，GeaFlow 通过增量计算把到达的数据作为连续的图更新来处理——每个事件只触发必要的子图变更，从而避免昂贵的全量重算。
具体而言，GeaFlow 用增量流式计算取代全量计算，使局部子图能够在对话发生的瞬间实时更新。通过动态的图状态管理，它把时序记忆作为流状态来维护，解决长会话中的状态一致性问题。此外，它借助分布式快照机制，保障企业级多 Agent 协作下的状态容错与恢复。
在技术实践环节，我们将演示如何构建一个具备毫秒级记忆更新能力的知识助手。我们还将展示 GeaFlow 如何为运行在持续演进知识图谱之上的 AI 系统提供基础支撑。

### 讲师:


<img src="https://cdn.sessionize.com/image/942a-400o400o1-UTgxQ7mc7kgpLPSnYWcsvV.jpg" width="200" /><br/>

Litao Lin：Apache GeaFlow（孵化中）Committer

Apache GeaFlow（孵化中）Committer。作为项目的核心成员，他从零参与了 GeaFlow 图计算引擎的架构设计与开发，尤其专注于图计算 DSL 的设计与实现，以及数据智能技术的演进。他深度参与开源社区活动，目前就职于 Ant Group。


<img src="https://cdn.sessionize.com/image/8e82-400o400o1-fiJe6bcjN6hvokxoSwtyfp.jpg" width="200" /><br/>

Yao Zhongqiang：Ant Group 图计算专家与开发工程师

深耕大数据领域，专长于图计算、实时计算和 OLAP。所在团队目前专注于 Agent Memory 与 MARL。
