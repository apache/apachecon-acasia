---
title: "Apache Ozone：基于 S3 生命周期配置的文件自动过期与删除"
date: ""
track: "datastorage"
presenters: "Chen Xi, Sammi Chen"
stype: "中文演讲"
---

Apache Ozone 是 Hadoop 生态中的分布式存储系统，同时支持 Hadoop 文件系统 API 和与 AWS S3 兼容的 RESTful API。在大数据生态的分布式存储系统中，通常有些文件是短生命周期的临时数据，有些则是长生命周期的持久化数据，系统管理员或用户不得不在临时文件不再使用时手动将其删除。在本次演讲中，我们将介绍即将在下一个 Ozone 2.2.0 版本中发布的新特性 S3 Lifecycle Configuration - 对象过期（Object Expiration），包括该特性的设计思路、如何通过对目标 bucket 设置生命周期配置来自动过期并删除临时文件，以及在生产环境中使用该特性的经验分享。

### 讲师:


<img src="https://cdn.sessionize.com/image/219f-400o400o1-7Sfo2ovJpEL8bf4Ev34E9n.jpg" width="200" /><br/>

Chen Xi：存储专家工程师，Shopee 数据基础设施团队

深耕存储领域，专注于分布式存储系统与性能优化。目前在 Shopee 数据基础设施团队工作，负责存储产品研发。


<img src="https://cdn.sessionize.com/image/f062-400o400o1-JwG1ArqNeWcX7KNGJHGgSv.jpg" width="200" /><br/>

Sammi Chen：Cloudera 首席存储工程师

Cloudera 首席存储工程师，专注于 Apache Hadoop 与 Apache Ozone 内核开发，现任 Ozone PMC 与 Hadoop PMC 主席，曾任腾讯与 Intel 的大数据存储技术负责人。
