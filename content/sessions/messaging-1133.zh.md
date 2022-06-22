---
title: "BIGO基于Pulsar在高吞吐追赶读场景下的性能优化实践"
date: "" 
track: "messaging"
presenters: "吴展鹏"
stype: "中文演讲"
---
BIGO 旗下目前有 BIGO Live 和 Likee 短视频两大视频产品与服务，当前 BIGO Live 直播业务已覆盖 150 多个国家与地区，Likee 短视频也拥有超过 1 亿用户，产品在 Z 世代中广泛流行。在过往的技术架构中，BIGO 采用开源的 Kafka 集群来支撑实时数据计算分析与短视频推荐业务。但随着业务不断快速发展，过往架构遇到了巨大挑战。Apache Pulsar 带来的分层架构及低延迟、持久化存储、水平易扩展等特性帮助我们解决了生产系统中面临的诸多问题。

本文将介绍 BIGO 基于 Pulsar 在高吞吐读写的环境下、针对追赶读场景完成的性能优化，本文的主要内容包括：追赶读对系统性能损耗的讨论、消息磁盘读的主要耗时阶段、BIGO 提出的全新的异步预读优化方案、新策略在生产环境中的实际表现效果，本文将以最贴近实际的方式和大家分享 BIGO 在优化追赶读场景时的思考和心得。
 ### Speakers: 
 <img src="images/speaker/1133.png" width="200" /><br>吴展鹏: BIGO, Staff Engineer, 吴展鹏是BIGO计算平台的高级大数据研发工程师，他目前主要关注的方向是流式系统的计算和存储，他同时也是Apache Pulsar、pulsar-flink的contributor、Kafka-on-Pulsar的maintainer，过去曾多次受邀在Pulsar Meetup、Pulsar Submit上做技术演讲。
 