---
title: "AI 时代 Apache Kafka 的成本挑战：优化实践与社区最新进展"
date: ""
track: "messaging"
presenters: "Jian Fu"
stype: "中文演讲"
---

AI 驱动的数据爆发式增长，使得 Kafka 的工作负载和运维成本显著上升。本次分享聚焦于如何优化 Kafka 成本，涵盖以下几个关键方面：

1. Kafka 成本的构成，以及其与系统架构之间的关系
2. 如何着手 Kafka 成本优化，例如 KIP-1227（暴露 RackID）背后的动机
3. 近期与成本相关的 KIP 和 PR（例如 KAFKA-19909、KIP-1123、KIP-1241、KIP-1150）以及它们如何帮助降低成本
4. 除 Kafka 本身之外，其他降低成本的途径（例如非技术层面的努力、对 KIP-405 分层存储插件的改造）
5. 在真实成本优化过程中遇到的常见陷阱与挑战
6. AI 在成本优化中所扮演的角色及其特性

目标听众
关注 Kafka 成本管理与优化实践的工程师、架构师和技术负责人，或希望从成本视角了解 Kafka 架构的人士

预期收获
清晰地理解 Kafka 的成本结构、优化策略与常见陷阱，以及最新的技术进展和 AI 驱动的实践。这些方法论同样可以应用到其他软件系统的成本优化中。

### 讲师:


<img src="https://cdn.sessionize.com/image/acec-400o400o1-37K579fm9sFS3bKyoamxyW.jpg" width="200" /><br/>

Jian Fu：Zoom，工程经理

Zoom 工程经理，曾就职于 Cisco，负责 Zoom 消息队列系统的开发与运维，拥有 15 年以上构建高性能、高可用、弹性系统的经验。

研究：
	1 项美国专利，10 余篇已发表论文

认证：
        网络工程师
        信息系统项目管理师

开源贡献者：
	Netty
        Apache Kafka
	InfluxDB/InfluxDB-java
	Redis/Jedis
	Spring/Spring-data-redis
	Jenkins
	Apache Zookeeper

著作：
	独著：
		《Netty 原理剖析与应用》（Netty 作者 Trustin Lee 推荐）
	合著：
		《微服务之道：度量驱动开发》
		《完美测试：软件测试系列最佳实践》

Kafka 改进提案（KIP）作者：
                四项 KIP 已被采纳并实现

在线课程作者：
	极客时间：
		《Spring 编程常见错误 50 例》
		《Netty 源码剖析与实战》
