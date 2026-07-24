---
title: "Apache Pulsar 多集群容灾与渐进式流量迁移"
date: "2026-08-09T15:45:00"
track: "messaging"
presenters: "Dezhi LIU"
stype: "中文演讲"
room: "静宜厅"
---

多集群 Pulsar 的运维面临两大核心挑战：主集群故障时的快速容灾切换，以及集群搬迁期间的平滑流量迁移。本次分享介绍一款 proxy 的设计与实现，它通过三项关键技术——定向连接关闭、原生加权路由以及渐进式迁移引擎——将容灾与调度统一起来，从而实现任意精度的流量分配与零爆炸半径的故障切换。

### 讲师:


<img src="https://cdn.sessionize.com/image/9fea-400o400o1-3hsAPnSmwMffEueB73VS6x.jpg" width="200" /><br/>

Dezhi LIU：Ascentstream Technology 联合创始人

● 谙流科技联合创始人

● 10 年以上大规模互联网/金融基础架构开发经验

● 前腾讯专家工程师，曾成功推动 Pulsar 在腾讯集团统一计费平台消息总线（可处理千亿级消息）以及腾讯云金融级消息服务（TDMQ）上的大规模落地
