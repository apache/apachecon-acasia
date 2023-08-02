---
title: "RocketMQ Million Queue capability support - rocksdb kv storage"
date: "2023-08-20T14:00:00" 
track: "messaging"
presenters: "Zhao Fujian"
stype: "Chinese Session"
---
The existing rocketmq storage architecture has the following problems:
1 million queue topic, subion, consumerOffset about 200-300M, timing persistent serialization and CRC32 computing cpu pressure is large, followed by the overwrite disk util is high
1. The consumeQueue index is implemented based on mmap. In a million-queue scenario, random read/write bottlenecks occur for large numbers of small files and performance deteriorates sharply

To support millions of queues, rocksdb kv storage is introduced:
1. Metadata is written to the wal and memtable of the rocksdb. put and delete operations update the memory to avoid performance problems caused by real-time persistence
2. The lsm tree at the bottom of the rocksdb combines a large number of random reads and writes of small files in log append mode, solving the performance problem of random reads and writes of large numbers of small files in the consumeQueue scenario
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230617/1741264950.JPG" width="200" /><br>Zhao Fujian: Alibaba, Senior development engineer, He graduated from Southeast University in June 2020
He joined Alibaba in July 2020
 <br><br>