---
title: "掌握大规模 Shuffle：Dream11 使用远程 Shuffle 服务的实战手册"
date: ""
track: "datastorage"
presenters: "Ravi Rana, Mehul Batra, Mohit Jain"
stype: "英文演讲"
---
 
在 Dream11，我们使用 Apache Celeborn 进行 PB 级规模的 Shuffle 操作，利用机架感知（rack awareness）来最小化跨机架的数据传输，并通过在不同机架间复制 Shuffle 数据来确保高可用性。它将 Shuffle 存储与计算节点解耦，使得存储能够独立于计算需求进行弹性扩展。并行分区写入和自适应 Shuffle 读取优化了吞吐量并降低了延迟。弹性扩展允许动态分配资源，在不同工作负载下保持成本效益。这种设计增强了容错能力，并将作业完成时间缩短了 50% 以上。
 
### 讲师:

<img src="https://sessionize.com/image/c023-400o400o1-XrDyFVcAPGBBg2RCKps4W4.jpg" width="200" /><br/>

Ravi Rana: 技术负责人

Ravi Rana 是 Dream11 的技术负责人，拥有 10 年以上的软件工程专业经验。


<img src="https://sessionize.com/image/ff4d-400o400o1-Wr3YbdVGhUXaDsQG43bhfe.png" width="200" /><br/>

Mehul Batra: 技术负责人

一直在寻找吸引人的数据基础设施项目和读物
(训练你的思维和身体)


<img src="https://sessionize.com/image/cb28-400o400o1-Utccibvy6GXbntEwxXRRRY.jpg" width="200" /><br/>

Mohit Jain: 技术负责人

我在大数据和 ML 的交叉点工作，在扩展实时、批处理和 ML 工作负载的同时，使 Spark 和 Flink 的速度更快。无论是优化分布式计算、简化数据管道，还是构建直观的工具，我的目标都是将复杂的数据挑战转化为无缝、高性能的解决方案。
