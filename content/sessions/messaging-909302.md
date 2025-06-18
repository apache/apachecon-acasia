---
title: "Storage Engine for RocketMQ Based on Commitlog and RocksDB"
date: "2025-07-26T15:45:00"
room:  "JingYi Hall"
track: "messaging"
presenters: "Zhou Li"
stype: "Chinese Session"
---

Storage Engine for RocketMQ Based on Commitlog and RocksDB
    Delay message, transaction message, POP and index are core features of RocketMQ. These features involve multiple state transitions in memory and are implemented based on the file system. The existing implementation faces the following issues:
1. Queue-Based Implementation cause more merge operations (e.g., POP consumption result merging, transaction message OP message merging) that result in complex workflows, low efficiency, and poor scalability.
2. TimerWheel, TimerLog, Revive, and Index Files require additional storage.
3. Excessive intermediate states in memory cause performance issues, such as heavy GC pressure on heap memory from temporary objects like CK, ACK, and CKMock in POP consumption.
4. The multitude of disk files and intermediate states complicates tiered storage and elastic scaling. 
    RocksDB is a high-performance embedded key-value storage engine developed by Facebook, widely used in databases, logging systems, and distributed storage. Unifying the storage engine with Commitlog and RocksDB，the key points is separating message data in two parts，Commitlog on the filesystem while migrating all index models in RocksDB. This approach offers significant advantages:
1. Using RocksDB's fast lookup capabilities to reduce coordination/synchronization in data processes to simplify complexity. For example, RocksDB's KV storage CRUD operations can replace the original two-queue merge process in POP consumption.
2. Restructures storage models to reduce the amount of stored data and improve storage efficiency. For instance, RocksDB's indexing capabilities can fully replace existing index features, don‘t need to save any Index Files anymore.
3. Uses RocksDB as a unified data migration interface to simplify the process of tiered storage and elastic scaling, it’s much earlier than current implementation.
    This storage architecture significantly optimizes those core features. The refactoring not only simplifies the codebase and reduces maintenance costs, but also provides a robust and flexible solution for RocketMQ to handle growing business demands and complex storage environments.
### Speakers:


<img src="https://sessionize.com/image/89b7-400o400o1-3UL89hviMkFYw2SmgNyGZM.jpg" width="200" /><br/>

Zhou Li: aliyun

Messaging Expert at Alibaba Cloud, responsible for Alibaba's core messaging middleware