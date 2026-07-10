---
title: "ServerlessX：面向基于 RDMA 的分离式架构的内核态 Serverless 系统"
date: ""
track: "microservice"
presenters: "Mingxuan Liu"
stype: "中文演讲"
---

本演讲探讨一种新颖的 Linux 内核态 Serverless 框架，旨在弥合物理分离的硬件资源池（例如分离式内存）与现代 Serverless 函数即时执行语义之间的差距。通过构建一个跨越 RDMA 网络基础、分布式操作系统内核原语（RDMA Fork、Map 和 mmap）以及面向特定应用扩展策略的三层架构，我们展示了如何在分离式资源之间实现毫秒级的弹性伸缩。听众将深入了解三个实际案例，包括面向 LLM 推理的快速 GPU 扩展、面向推荐系统的动态内存扩容，以及面向存储引擎的解耦式 I/O 容量扩展。

### 讲师:


<img src="https://cdn.sessionize.com/image/16a6-400o400o1-KNwE7WjxEY3ppBwwGySxky.jpg" width="200" /><br/>

Mingxuan Liu：西北工业大学

Mingxuan Liu 是西北工业大学的应届博士研究生。他拥有十余年的研究经验，研究兴趣涵盖操作系统内核、RDMA 网络、Serverless 计算以及 LLM 基础设施。他的博士研究聚焦于面向 RDMA 分离式架构的内核态 Serverless 资源弹性伸缩方法。他已在 CCF-A/B 类顶级学术会议上发表十余篇第一作者论文。Mingxuan 即将加入澳门大学担任博士后研究员，继续推进高性能分布式系统的研究。
