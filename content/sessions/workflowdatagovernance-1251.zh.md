---
title: "Apache Oozie 的深度实践"
date: "2022-07-29T14:10:00"
track: "workflowdatagovernance"
presenters: "张俊帆"
stype: "中文演讲"
---
大数据离线处理领域在近些年的发展逐渐成熟完善，而在对离线任务编排领域，也就是工作流这一块，各种项目工具也是层出不穷。Apache 的第一代工作流调度软件 Oozie 已经是有 10 余年的历史了，而新晋火热的 dolphinscheduler 和 airflow 也是关注度相当高，证明了在工作流编排领域依然有很强的活力。

本次演讲，将带来 Apache Oozie 作为一个非常古老的项目在爱奇艺的深度实践。涉及到 Oozie 功能与架构介绍、在爱奇艺的规模与应用、对 Oozie 的任务插件支持和改造、 单 Oozie 集群统一调度多集群的方案实现、Roadmap、社区贡献等5个方面来介绍

Oozie 功能与架构介绍
Oozie 的架构不同于 airflow 和 dolphinscheduler, 没有复杂的 master/slaves 架构, 是一个无状态架构。每一个节点均是 master，通过 zk 协调者来认领自己名下的 action(也就是各个 job)。

同时，相较于与业界知名的 dolphinscheduler 相比，它的 worker 的设计也是不同。Oozie 的 worker 并非是一个由 worker 组成的工作资源池，而是将其托管给 Hadoop Yarn 集群。对于每一个 Spark/Hive/MR/Flink(除了 SSH Action) 均会由一个 Oozie launcher 来启动。

优点是避免了维护一个大的 worker 集群，Oozie 的扩展性取决于了 Hadoop Yarn 的容量，同时降低了Oozie 的管理成本；
但是缺点也很明显，每一个 Oozie launcher 均会占据 1core/1g. Oozie5.0 之前的版本是 2core/2g(是一个 MR 任务，5.x 后是 Oozie 内部在 Yarn 上实现的 launcher AM)。

同时 Oozie 提供了类型繁多的 action (类比于 dolphinscheduler 的 task type), 同时也暴露了底层通用的接口，方便用户进行扩展。现在 Oozie 原生已经支持的通用大数据 action, 有 hive/spark/mr/distcp 等等，同时我们也扩展了 flink batch/ tony 等 action type.

在功能性上，Oozie 提供了定时启动、触发式启动、SLA 告警、指定节点重启等功能，基本满足了大数据的离线调度编排的需求。
但是因为其难用的界面，复杂的 xml 配置，导致一度让人望而生畏，因此在爱奇艺也只将 Oozie 作为底层的调度引擎，而在上层构建了数据开发平台，提供了可视化拖拽页面，增强易用性。但是借助 Oozie 的无状态架构，很好地支撑了爱奇艺大数据离线任务的发展。
 
在爱奇艺的应用
Oozie 自 2018 年以来，在爱奇艺支持10多个离线 Hadoop 集群（节点总数2w+）的日均 20+ 的工作流离线任务，不仅覆盖了推荐、广告等离线数据开发，还承担了一部分机器学习工作流编排的场景。

初期部署 Oozie 的方式是遵照 Oozie 的设计，即每个 Hadoop 集群都会对应部署一个 Oozie 集群（一般是 2-4 台物理机，使用的是 Oozie HA 模式），这种部署方式通过底层的物理隔离，使得单 Oozie 集群的调度量得到了限制，在稳定性上获得了很高的益处。

但是随着业务发展，多云多机房的 Hadoop 集群搭建，Oozie 与 Hadoop 绑定的部署模式，带来了很大的运维负担。每次对 Oozie 的变更上线，都需要一周左右的灰度发布时间。因此我们也对 Oozie 的部署模式做了深度的改造。
另外因为内部离线任务的提交入口都收缩到 Oozie 这个调度引擎上，使得需求众多，扩展了很多 action type， 比如 flink batch action 等。


Oozie action 插件的支持和改造
在应用 Oozie 初期将 Spark 任务提交入口从入口机迁移到 Oozie 时，也遇到一些兼容性问题。Oozie 原生的 Spark 提交模式，是通过将用户的 spark jar 在 launcher 启动的时候，利用 hadoop 的 distributed cache 下载到 launcher 任务目录下。但是此种方式，如果 用户 spark jar 中带有了一些与集群不兼容的 yarn 依赖，则直接使得 spark 任务失败。因此通过将下载 Spark jar 延后到 launcher 启动后，来彻底解决了这个问题。

另外初期在将公司入口机上的 crontab 任务迁移至平台时，大量推进了 ssh action 的应用（在 Oozie 侧使用远程登录用户入口机的方式，来执行任务）。因此对 ssh action 修复了若干 bug 和问题，均已经回馈社区。同时也发现了一些隐蔽 bug,  如偶发的调度死锁等问题 [OOZIE-3646] Possible dead-lock in SignalXCommand - 
 
在基于 Oozie 的调度服务逐步成熟的过程中，我们也进行了一些新的尝试与探索，包括支持 Flink batch on Oozie 和使用 Oozie 来调度机器学习的训练任务。

Flink batch action 是为了推进流批一体，实现的一个 Oozie action. 但是在实现过程中，发现 Oozie 的 Hadoop delegation token 机制，在 Flink 上尚未实现，因此给 Apache Flink 贡献了多个 PR， 如
1. https://issues.apache.org/jira/browse/FLINK-21700 
2. https://issues.apache.org/jira/browse/FLINK-21768
3. https://issues.apache.org/jira/browse/FLINK-22294 
4. https://issues.apache.org/jira/browse/FLINK-22329 
5. https://issues.apache.org/jira/browse/FLINK-22534

另外为了支持机器学习工作流的编排，我们在 Oozie 上也引入了 TonY（tensorflow/pytorch on Yarn），通过实现 tony action 来将数据处理、样本生成同机器学习训练连通起来

单 Oozie 集群统一调度多 Hadoop 集群任务
因为 Hadoop 集群的众多，包括自建和云上的集群，同时 Hadoop 版本也各异，使得在使用原先 Oozie 的部署模式，带来了很大的运维成本。因为每个 Hadoop 集群都需要部署一个 Oozie 集群。

同时也希望对高优任务进行集群调度层面的 HA 保障，为了实现这个目标，我们制定了三步骤的实施方案，从具备跨集群调度的能力、实现细粒度的调度隔离、实现智能的调度。

在具备跨集群调度的能力上，因为同时随着对 Oozie 的深入理解，也开始了对 Oozie 的深入改造，通过将调度集群配置与任务集群配置分离，实现了单 Oozie 集群同时负责调度公有云、自建 的 Hadoop2.x 和 3.x 多个版本集群。在改造后，在 Oozie 侧支持 Hadoop 新集群，只需要几分钟即可完成。

通过将多个集群的任务统一由单一 Oozie 集群调度，势必会造成集群间的干扰。因此实现了不同 Oozie server 之间的集群调度归属策略，隔离调度负载，保障任务的稳定性（配图）

目前，正在探索结合爱奇艺内部的 QBFS(一种基于 Hadoop HCFS 接口实现的虚拟文件系统)，来做任务的智能调度，对用户屏蔽掉底层的物理集群，提供统一的逻辑资源集群

Roadmap
1. 结合 QBFS，继续探索对任务的智能调度
2. 增加 Oozie 代码版本发布时的，细粒度灰度的能力，精确到指定工作流、指定用户，提升发布时的稳定性

Oozie 与相关项目的社区贡献
1. https://issues.apache.org/jira/browse/OOZIE-3646
2. https://issues.apache.org/jira/browse/OOZIE-3379
3. https://issues.apache.org/jira/browse/OOZIE-3594
4. https://issues.apache.org/jira/browse/OOZIE-3393
5. https://issues.apache.org/jira/browse/OOZIE-3569
6. https://issues.apache.org/jira/browse/OOZIE-3574
7. https://issues.apache.org/jira/browse/OOZIE-3589
增加 Flink batch action，Flink 侧的兼容
8. https://issues.apache.org/jira/browse/FLINK-21700 
9. https://issues.apache.org/jira/browse/FLINK-21768
10. https://issues.apache.org/jira/browse/FLINK-22294 
11. https://issues.apache.org/jira/browse/FLINK-22329 
12. https://issues.apache.org/jira/browse/FLINK-22534
 ### Speakers: 
 <img src="images/speaker/1251.png" width="200" /><br>张俊帆: 爱奇艺, 大数据工程师, 开源项目
个人参与 Flink/Oozie/Hadoop 等大数据项目，负责维护 github.com/tony-framework/tony
开源地址：github.com/zuston

过去无演讲记录

 