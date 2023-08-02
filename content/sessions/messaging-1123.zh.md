---
title: "RocketMQ 百万队列能力支持 -- rocksdb kv 存储"
date: "2023-08-20T14:00:00" 
track: "messaging"
presenters: "赵福建"
stype: "中文演讲"
---
现有的 rocketmq 存储架构存在以下问题：
1.百万队列 topic 、subion、 consumerOffset 约需 200 - 300M，定时持久序列化和 CRC32 计算 cpu 压力较大，其次覆盖写磁盘 util 很高
2.consumeQueue 索引基于 mmap 实现，百万队列场景下大量小文件随机读写瓶颈显现、性能急剧下降

为支持百万级数量队列，引入 rocksdb kv 存储：
1.元数据写入 rocksdb 的 wal 和内存 memtable，put 与 delete 操作更新内存，避免了实时持久化带来的性能问题
2.rocksdb 底层 lsm 树采用日志追加的方式合并了大量小文件随机读写，解决了百万队列场景下 consumeQueue 大量小文件随机读写的性能问题
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230617/1741264950.JPG" width="200" /><br>赵福建: 阿里巴巴, 高级开发工程师, 2020年6月毕业于东南大学
2020年7月入职阿里巴巴
 <br><br>