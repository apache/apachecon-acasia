---
title: "释放原生性能：Apache Iceberg-cpp 的架构与路线图"
date: ""
track: "datastorage"
presenters: "Gang Wu, Junwang Zhao"
stype: "中文演讲"
---

随着现代数据引擎转向原生执行（C++、Rust 以及 SIMD 优化的处理），业界对高性能、不依赖 JVM 的 Iceberg 实现的需求达到了前所未有的高度。本次演讲将深入剖析 iceberg-cpp 的起源与设计理念——这是 Apache Iceberg 规范的官方 C++ 实现。

我们将分享 Singdata 发起该项目的初衷——瞄准高性能的 Iceberg 实现以及与原生查询引擎的无缝集成。我们会介绍项目当前的进展，包括对 REST Catalog 的支持和 Arrow 原生集成，并勾勒写入支持与 V3 规范合规的路线图。此外，Singdata 还将分享把 iceberg-cpp 集成进其高性能技术栈的内部历程，以及我们对长期维护的承诺。本次演讲也是向 C++ 引擎开发者和性能爱好者发出的一封邀请函——欢迎加入我们，共同打造与 Iceberg 生态交互的最快方式。

### 讲师:


<img src="https://cdn.sessionize.com/image/3702-400o400o1-XuBH8pNbBQ2p81R8nvwzRh.jpg" width="200" /><br/>

Gang Wu：Singdata 软件工程师

Gang 是 Singdata 的软件工程师，从事湖仓存储相关工作。他是 Apache Arrow、Apache ORC、Apache Parquet 的 PMC 成员，也是 Apache Iceberg 的 Committer。他同时是 ASF 成员。加入 Singdata 之前，他先后在 Uber 从事 Apache Spark、在阿里巴巴从事 MaxCompute 云数据仓库的工作。


<img src="https://cdn.sessionize.com/image/db19-400o400o1-G2Uadqsg15vsGvMP6LJQqe.jpg" width="200" /><br/>

Junwang Zhao：蚂蚁集团数据库工程师

Junwang 是蚂蚁集团的数据库工程师，业余时间参与 PostgreSQL 的开发，并被授予 PostgreSQL Significant Contributor 称号。他也是 iceberg-cpp 项目的共同创建者之一，致力于构建开放、高性能的数据基础设施。
