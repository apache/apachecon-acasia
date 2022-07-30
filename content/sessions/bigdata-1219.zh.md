---
title: "Cloud Shuffle Service 在字节跳动 Spark 场景的应用实践"
date: "2022-07-30T16:10:00"
track: "bigdata"
room: "B"
presenters: "魏中佳"
stype: "中文演讲"
---
字节跳动内部主要使用 Spark 进行离线大数据处理，每天线上约有几十万的 Spark 作业。内部业务用户对 SLA 有明确需求，如果破线将对业务产生较大影响。Shuffle 是 Spark 引擎的一个重要操作，在大规模作业下，开源 ExternalShuffleService(ESS) 的实现机制容易带来大量随机读导致的磁盘 IOPS 瓶颈、Fetch 请求积压等问题，进而导致运算过程中经常会出现 Stage 重算甚至作业失败，继而引起资源使用的恶性循环，严重影响 SLA。此外，在字节跳动内部的在离线混部场景下，在线机器的磁盘容量等能力较小，运行中经常遇到磁盘满的问题。
在此背景下，字节跳动 Spark 团队一方面针对 ESS 做了大量的优化，包括 Shuffle 相关参数优化(减少随机读的请求)、增加 Shuffle 限流等，大大提高了 ESS 在 SSD 集群的稳定性；另一方面在 HDD 磁盘/在离线混部等场景的集群中，我们提出了 Cloud Shuffle Service(CSS) 作为解决方案，即 map task 通过 push 的方式将同一个 partition 的数据推送到同一个 CSS 工作节点，reduce task 可以从对应的节点进行顺序读，大大提高了读取的性能和 Shuffle 的稳定性，有效保障了SLA。
目前字节跳动内部的线上 Spark / Flink / MapReduce 均已接入CSS。
 ### Speakers: 
 <img src="images/speaker/1219.png" width="200" /><br>魏中佳: 毕业于电子科技大学，现任字节跳动基础架构大数据开发工程师，专注大数据分布式计算领域，主要负责 Spark 内核开发及字节自研 Shuffle Service 开发。

 