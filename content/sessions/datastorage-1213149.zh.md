---
title: "当优化器说谎时：调试 Apache Cloudberry 中的跨 Slice 执行"
date: "2026-08-08T16:45:00"
track: "datastorage"
presenters: "Alena Rybakina"
stype: "英文演讲"
room: "万寿山会议室"
---

在 Apache Cloudberry 中，优化器、规划器（planner）和执行器对同一条查询持有不同的抽象。当这些抽象之间出现分歧时，即使是简单的查询也可能引发严重的故障。
本次演讲分享一个涉及复制表（replicated table）上公共表表达式（CTE）共享扫描（Shared Scan）的真实 bug。当此类 CTE 被作为标量子查询多次引用时，查询可能无限期挂起，或报出"could not open existing temporary file"之类的错误。
根本原因在于逻辑执行与物理执行之间的错配：标量 SubPlan 向优化器隐藏了依赖关系，导致 slice 分配不正确，破坏了生产者—消费者的局部性。
在本次演讲中，我将梳理几种可选的修复方案，并解释每种方案是如何尝试解决这一问题的。我们会深入优化器内部，理解这个 bug 为何会产生、不同修复方案如何改变执行拓扑，以及为什么其中一些方案——尽管可行——却无法作为最终方案被接受。
有些修复会引入细微的回归、改变计划形态，或被迫回退到 Postgres 优化器，这凸显了在不破坏全局行为的前提下做局部改进的困难。
本次演讲展示了看似简单的查询模式如何暴露优化器与执行器之间深层的不一致——以及为什么修复这类问题往往需要在权衡中抉择，而非寻找一个唯一"正确"的答案。

### 讲师:


<img src="https://cdn.sessionize.com/image/62a6-400o400o1-LjXRcX4dAwc4VGESotUqiG.png" width="200" /><br/>

Alena Rybakina：软件开发工程师，Yandex Cloud

工作经历
拥有 5 年以上数据库系统专业经验，其中包括在 Postgres Professional 工作的 5 年。
主要兴趣
查询优化、MVCC 内部机制与数据库统计信息。
PostgreSQL 经验
拥有 4 年以上从事 PostgreSQL 内部实现、性能改进及优化器相关功能的一手经验。
主要项目与贡献
开发与优化相关的扩展和功能，包括 AQO（自适应查询优化，Adaptive Query Optimization）和自连接消除（Self-Join Elimination）。
对 PostgreSQL 查询规划器的实验性及面向生产的改进。
对 PostgreSQL 核心的贡献，包括优化器中的 OR-to-ANY 和 VALUES-to-ANY 转换。