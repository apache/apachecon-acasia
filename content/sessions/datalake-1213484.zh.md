---
title: "守护湖仓安全：用 Apache Gravitino 为 Iceberg REST 提供身份感知的治理"
date: "2026-08-09T15:45:00"
track: "datalake"
presenters: "Rory Qi"
stype: "英文演讲"
room: "万春厅"
---

Apache Iceberg 已经成为开放表格式的事实标准，而 Iceberg REST Catalog 是实现存算分离的关键。然而，尽管 REST 规范定义了如何交换元数据，却把安全——认证、授权和审计——留给了用户自行解决。对于从试验性项目迈向生产级湖仓的组织而言，这一"安全缺口"是一个重大障碍。
在本次演讲中，我们介绍 Apache REST——一个开源的联邦元数据湖，提供生产可用的 Iceberg REST 服务实现。我们将走查 REST 如何作为安全 catalog 代理的技术架构。
核心收获包括：
身份与认证：深入剖析 Gravitino 对 OAuth2、Basic、Kerberos 和 HTTPS 的支持，确保只有经过验证的客户端才能访问 catalog。
统一访问控制：如何在 catalog、namespace 和表级别管理细粒度权限（RBAC），即使在使用 Hive Metastore 或 JDBC 等传统后端时也能做到。
凭据分发（Credential Vending）：Gravitino 如何安全地向客户端发放短时有效的存储凭据（S3/GCS/Azure），确保数据层的安全性与元数据层一样强。
真实集成：演示 Spark、Trino 和 Flink 如何与受 Gravitino 安全保护的 Iceberg REST 端点交互，且无需对引擎进行自定义 fork 或打补丁。
无论你是构建多租户数据湖的平台工程师，还是关注开源治理的安全架构师，本次演讲都将为构建一套安全、厂商中立的 Iceberg 基础设施提供蓝图。


### 讲师:


<img src="https://cdn.sessionize.com/image/3df9-400o400o1-4yoKkoqsJnbKwTammtx8VP.jpg" width="200" /><br/>

Rory Qi：Apache Gravitino committer，Apache Uniffle PMC Chair

Apache Gravitino PMC 成员，Apache Uniffle PMC Chair，ASF 成员，Datastrato 工程师，曾就职于腾讯、百度