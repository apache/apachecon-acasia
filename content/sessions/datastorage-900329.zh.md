---
title: "Apache Ozone：通过磁盘平衡器实现数据均衡"
date: "2025-07-26T15:45:00"
room:  "万寿山会议室"
track: "datastorage"
presenters: "Sammi Chen"
stype: "中文演讲"
---

Apache Ozone 是 Hadoop 生态系统中的一个分布式存储系统。作为一个分布式存储系统，确保数据在 DataNodes 和磁盘之间均匀分布非常重要，这样才能高效且充分地利用存储空间和资源。为了实现这一目标，Ozone 支持 Container Balancer 和 Disk Balancer，前者用于解决数据在 DataNodes 之间均匀分布的需求，后者则用于解决数据在每个 DataNode 的所有磁盘之间均匀分布的需求。在本次会议中，我们将分享磁盘平衡器（Disk Balancer）功能的设计原理，以及如何使用磁盘平衡器功能来确保 DataNode 的磁盘利用率均衡。

### 讲师:

<img src="https://sessionize.com/image/f062-400o400o1-JwG1ArqNeWcX7KNGJHGgSv.jpg" width="200" /><br/>

Sammi Chen: Cloudera 首席存储工程师

Sammi Chen 是 Cloudera 的首席存储工程师，专注于 Apache Hadoop 和 Apache Ozone 内核开发。她目前是 Ozone 项目管理委员会（PMC）主席和 Hadoop PMC 成员，曾担任腾讯和英特尔的大数据存储技术负责人。