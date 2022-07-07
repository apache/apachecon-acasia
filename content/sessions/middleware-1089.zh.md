---
title: "拥抱云原生，基于 Kubernetes 的 ShardingSphere 云化改造"
date: "2022-07-29T16:10:00"
track: "middleware"
presenters: "李卓"
stype: "中文演讲"
---
背景
随着 Kubernetes 日趋成熟与稳定，SphereEx 在探索 ShardingSphere 未来的前景的路上也逐渐将其认为是 ShardingSphere 下一阶段的重要里程碑。在此背景下，SphereEx 云团队将对 ShardingSphere 云化改造作为重要目标注意。在实际过程中，团队遇到很多问题和挑战。本次演讲将分享一下团队对 ShardingSphere 云化改造中遇到的问题和做出的应对。
Kubernetes Operator 模式是什么
Kubernetes 的 Operator 模式概念允许你在不修改 Kubernetes 自身代码的情况下，通过为一个或多个自定义资源关联控制器来扩展集群的能力。 
Operator 是 Kubernetes API 的客户端，充当用户自定义资源的控制器。
Kubernetes CRD 是什么
定制资源（Custom Resource） 是对 Kubernetes API 的扩展。 用户可以使用资源定制对 Kubernetes 进行扩展。
在 Kubernetes 中，下列的几种能力都能被满足：
1. 使用客户端还有 CLI 可以直接对资源进行更新。
2. 使用 Kubectl 命令也可以直接对这个资源进行支持。
3. 利用 Kubernetes 的自动化机制，可以对这个资源的变动进行感知并且对这个对象的关联对象进行后续操作。
4. 使用 Kubernetes 原生能力能够做到自动化处理。
遇到的问题
在 ShardingSphere-Proxy 上云的过程中，团队遇到了几个问题，一个是没有一个在云环境中的标准的部署过程，现阶段 ShardingSphere-Proxy 只支持 Docker 还有二进制的部署模式。另外一个是 ShardingSphere-Proxy 依赖 Zookeeper 作为治理节点。有状态的服务，例如 Zookeeper 不是那么适合在云上进行处理。Kubernetes 由于其 Pod 的生命周期特性和强大的水平扩展能力，更加适合处理无状态应用。有了 Zookeeper 的加入，ShardingSphere-Proxy 变得没那么无状态。这是亟待云团队进行解决的棘手问题。
解决方案
现阶段，ShardingSphere 在 Kubernetes 环境探索从未停止。为了增强在 Kuerbenets 环境中适配能力还有自运维能力，SphereEx 云团队将 Kubernetes Operator 模式与 ShardingSphere 进行结合，对 ShardingSphere-Proxy 进行云化改造。并且结合 Kubernetes 的原生能力， 使ShardingSphere-Proxy 可以在 Kuebrnetes 环境中做到脱离 Zookeeper ，并保留集群模式单独进行运行。
以 ShardingSphere-Proxy 这个数据库治理中间件为例
通过结合 Kubernetes Operator 模式，能够做到增强 ShardingSphere-Proxy 在 Kubernetes 中的表现能力。主要体现在，自动运维，自动扩缩容以及自动节点状态监控。在部署结构和部署难度方面，Operator 也会降低这方面的难度。虽然现阶段，ShardingSphere-Proxy 已经正式支持了 Helm 进行部署。但是 Helm 只能够做到对一个 ShardingSphere-Proxy 集群环境进行快速部署和版本化管理，后续的自动运维包括集群状态检查还有自愈等能力是缺失的。ShardingSphere-Operator 的存在正好弥补了这方面的空白。利用声明式的资源描述，ShardingSphere-Operator 可以帮助用户简单快速的达到想要的 ShardingSphere-Proxy 部署模式终态。增加了云环境中 ShardingSphere-Proxy 集群的稳定性和可维护性。
另外定制资源这个 Kubernetes 扩展的存在，也可以帮助 ShardingSphere-Proxy 对运行时集群中依赖的元数据进行存储。依托于 Kubernetes 的中 CRD 的 list/watch 能力，能够做到对于元数据变动后向其他集群中的节点进行广播，并实时更新其余节点的运行时元数据。
DistSQL（Distributed SQL）是 Apache ShardingSphere 特有的操作语言。 它与标准 SQL 的使用方式完全一致，用于提供增量功能的 SQL 级别操作能力。在去 Zookeeper 的过程中，因为元数据变动的入口变得多元，如何将 DistSQL 写入的配置和用户直接修改 CRD 都提供支持，团队也提供了自己的思路。利用 ShardingSphere-Sidecar 结合 ShardingSphered 的做法，使 ShardingSphere-Proxy 可以做到对这两种元数据变动入口的同时支持。并且在未来 ShardingSphere-Sidecar 也有可能去支持 Service Mesh 的 xDS 协议。这样就大大的增加了 ShardingSphere-Proxy 在云环境中的扩展能力。
 ### Speakers: 
 <img src="images/speaker/1089.png" width="200" /><br>李卓: SphereEx, 云研发工程师, SphereEx 云研发部 云研发工程师、ShardingSphere-Operator 核心开发者、Apache ShardingSphere  Contributor

 