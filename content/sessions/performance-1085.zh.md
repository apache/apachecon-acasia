---
title: "基于 Kubernetes 部署 Apache JMeter 进行大规模负载测试"
date: "2023-08-19T14:00:00" 
track: "performance"
presenters: "殷翀元"
stype: "中文演讲"
---
Apache JMeter 作为优秀的开源测试工具，自身具备分布式部署能力以支持较大并发，但仍难以支撑大型并发规模。为了使 JMeter 适用于百万量级规模的负载测试，我们对 JMeter 进行了改造，提升它在消息和数据处理上的吞吐能力，并以容器方式提供更强大灵活的水平扩展能力。为了统一管理发压容器的生命周期，进一步降低部署复杂性，并可从不同区域发起测试压力，我们将 JMeter 部署在 Kubernetes 集群上，以支持同时运行多个大规模负载测试，并设计了相关策略，在云环境上基于 VPC 对等连接实现多租户的私网负载测试。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/0934124610.png" width="200" /><br>殷翀元: EMQ, 项目经理, 殷翀元，EMQ XMeter 项目经理，负责性能测试平台 XMeter 产品，以及开源项目 mqtt-jmeter 的维护。曾于 ApacheCon Asia 2022 做题为《Apache JMeter 在 IoT 测试中的应用》的演讲。

EMQ 是一家开源物联网数据基础设施软件供应商，交付全球领先的开源云原生 MQTT 消息服务器和流处理数据库。EMQ 发起与运营的开源项目包括：开源物联网消息中间件项目 EMQ X，云原生分布式流处理数据库 HStreamDB，轻量级物联网边缘分析与流式处理开源软件 eKuiper，边缘工业协议网关软件 Neuron，跨平台 MQTT 客户端工具 MQTT X，MQTT JMeter 插件 mqtt-jmeter，等。
 <br><br>