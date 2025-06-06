---
title: "掌握大规模 Shuffle：Dream11 使用远程 Shuffle 服务的实战手册"
date: ""
track: "datastorage"
presenters: "Ravi Rana"
stype: "英文演讲"
--- 
 
在 Dream11，我们使用 Apache Celeborn 进行 PB 级规模的 Shuffle 操作，利用机架感知（rack awareness）来最小化跨机架的数据传输，并通过在不同机架间复制 Shuffle 数据来确保高可用性。它将 Shuffle 存储与计算节点解耦，使得存储能够独立于计算需求进行弹性扩展。并行分区写入和自适应 Shuffle 读取优化了吞吐量并降低了延迟。弹性扩展允许动态分配资源，在不同工作负载下保持成本效益。这种设计增强了容错能力，并将作业完成时间缩短了 50% 以上。
 
### 讲师:

<img src="https://sessionize.com/image/c023-400o400o1-XrDyFVcAPGBBg2RCKps4W4.jpg" width="200" /><br/>

Ravi Rana 是 Dream11 的技术负责人，拥有 10 年以上的软件工程专业经验。
