---
title: Apache IoTDB 系统监控框架的实施与调优实践
date: '2026-08-07T16:45:00'
room: 阳山会议室
track: cloudnative
presenters: 张洪胤
stype: 中文演讲
depth: intermediate
practice_level: 4
projects:
- apache iotdb
- prometheus
- grafana
audience:
- 开发者
- SRE/运维
related_sessions:
- IoTDB 时序数据订阅：设计与高效实践
- 优化可观测性：揭秘BanyanDB的热-温-冷架构
- Apache HertzBeat，新一代开源实时监控与告警平台
- Apache APISIX x IoT：让数据流更安全、更智能
- 消息系统可观察性最佳实践：Apache RocketMQ 和 OpenTelemetry 案例研究
---
自 1.0.0 版本起，Apache IoTDB 提供了统一的系统监控框架，允许数据库开发人员定义系统监控指标（如计数器）并将其注册以实现统一管理，同时支持 Prometheus + Grafana 监控指标可视化解决方案。经过一年的实践，已形成 4 个可视化监控面板及大量基于系统监控的调优经验。

### 讲师:

<img src="https://sessionize.com/image/4d3b-400o400o1-KCzTKrVsyHFxNEWdi4vEMv.jpg" width="200" /><br/>

张洪胤: Apache 贡献者，清华大学 2022 届硕士研究生

Apache 贡献者，清华大学 2022 届硕士研究生，目前负责 Apache IoTDB 的内存管理、系统监控及标准化测试工作。