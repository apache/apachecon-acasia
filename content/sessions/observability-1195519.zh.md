---
title: "Apache Cloudberry：为多个 PostgreSQL 实例执行的查询收集统计信息"
date: "2026-08-09T13:30:00"
track: "observability"
presenters: "Leonid Borchuk"
stype: "英文演讲"
room: "阳山会议室"
---

假设你拥有一个由多个 PostgreSQL 实例组成的 Apache Cloudberry 集群。它们共同执行同一条查询，而你希望收集执行该查询所耗费资源的一般性统计信息。内置的 pg_stat_statements 模块在这里已经不再适用，因为它只能工作在同一个数据库之内。我将介绍一个核心思路相似的方案——同样通过查询执行钩子（hook）来采集数据，但不再将数据存放在 PostgreSQL 的共享内存中，而是把原始数据发送给一个外部的 agent 进程。该进程负责对指标进行聚合，给出跨所有实例的统一视图，并提供额外的功能，例如强制终止有问题的会话；同时它并不仅限于 PostgreSQL：该方案还能从其他系统组件采集数据。我将介绍其架构、产品层面的任务，并分享相关仓库（Apache 2.0 License）的代码链接。

### 讲师:


<img src="https://cdn.sessionize.com/image/429e-400o400o1-X15FYUcE9UQzxFpN9AkBKZ.png" width="200" /><br/>

Leonid Borchuk：Yandex Cloud（莫斯科）开发者，Apache Cloudberry committer

Yandex Cloud MPP PostgreSQL 开发团队的团队负责人。他的职业生涯始于大型商用通用数据库和分析数据库的管理，而如今他终于开始编写自己的数据库。Apache Cloudberry committer。