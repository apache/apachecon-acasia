---
title: "基于 Commitlog 和 RocksDB 的 RocketMQ 存储引擎"
date: ""
track: "messaging"
presenters: "Zhou Li"
stype: "中文演讲"
---

基于 Commitlog 和 RocksDB 的 RocketMQ 存储引擎
延迟消息、事务消息、POP 和索引是 RocketMQ 的核心功能。这些功能涉及内存中的多种状态转换，并且基于文件系统实现。现有实现面临以下问题：

1. 基于队列的实现会导致更多的合并操作（例如，POP 消费结果合并、事务消息与 OP 消息合并），从而导致工作流复杂、效率低下且可扩展性差。
2. TimerWheel、TimerLog、Revive 和 Index 文件需要额外的存储空间。
3. 内存中过多的中间状态会导致性能问题，例如在 POP 消费过程中，CK、ACK 和 CKMock 等临时对象会对堆内存造成巨大的 GC 压力。
4. 大量的磁盘文件和中间状态使分层存储和弹性伸缩变得复杂。

RocksDB 是 Facebook 开发的一款高性能嵌入式键值存储引擎，广泛应用于数据库、日志系统和分布式存储。RocksDB 与 Commitlog 和 RocksDB 统一存储引擎的关键在于将消息数据分离成两部分，在文件系统上 Commitlog 的同时迁移 RocksDB 中的所有索引模型。这种方法具有显著的优势：

1. 利用 RocksDB 的快速查找功能减少数据处理中的协调/同步，从而简化复杂性。例如，RocksDB 的键值存储 CRUD 操作可以取代 POP 消费中原有的双队列合并过程。
2. 重构存储模型，减少存储数据量，提高存储效率。例如，RocksDB 的索引功能可以完全替代现有的索引功能，无需再保存任何索引文件。
3. 使用 RocksDB 作为统一的数据迁移接口，简化了分层存储和弹性伸缩的流程，这比目前的实现方式要早得多。

这种存储架构显著优化了这些核心特性。重构不仅简化了代码库、降低了维护成本，还为 RocketMQ 提供了强大而灵活的解决方案，以应对不断增长的业务需求和复杂的存储环境。

### 讲师:

<img src="https://sessionize.com/image/89b7-400o400o1-3UL89hviMkFYw2SmgNyGZM.jpg" width="200" /><br/>

Zhou Li: 阿里云

阿里云消息专家，负责阿里巴巴核心消息中间件