---
title: "移动云RabbitMQ消息队列在Openstack超大规模应用中的实践"
date: "" 
track: "messaging"
presenters: "胡宗棠"
stype: "中文演讲"
---
RabbitMQ作为消息队列中间件，已经在中国移动内部诸多业务系统（电子商务平台、交易平台和门户管理平台）中被广泛使用和落地，尤其是面向云计算基础设施的OpenStack领域。RabbitMQ是OpenStack平台中不可或缺的消息通信基础设施组件，为其内部的Nova、Cinder和Neturon组件提供消息流转和异步解耦能力。随着，OpenStack在中国移动公有云端的部署规模越来越大（部署在单AZ可用区的计算节点超过5000个规模），开源RabbitMQ在脑裂故障问题、消息积压、集群弹性扩容、提升服务器资源利用率等方面，都面临着诸多的挑战。
胡宗棠作为本次议题分享的嘉宾，将主要从以下几个方面来介绍移动云自研RabbitMQ消息队列在移动云端OpenStack平台中的实践与应用。
（1）OpenStack接入开源RabbitMQ的问题；
（2）移动云RabbitMQ消息队列介绍；
（3）移动云自研RabbitMQ的设计与实践；
（4）移动云自研RabbitMQ的技术演进与未来展望；
 ### Speakers: 
 <img src="images/speaker/1246.png" width="200" /><br>胡宗棠: 中国移动云能力中心, 技术专家, 胡宗棠 中国移动云能力中心，云原生领域技术专家，
Apache RocketMQ Committer，SOFAJRaft Committer，
Alibaba/Nacos Committer，Linux OpenMessaging Member
熟悉分布式消息队列、API 网关和分布式事务等中间件设计原理、架构以及各种应用场景，具有丰富高性能、高可用和高并发经验。
 