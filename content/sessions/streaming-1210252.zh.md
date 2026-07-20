---
title: "为湖流集成从 Kafka 迁移到 Fluss：落地实践"
date: "2026-08-09T16:15:00"
track: "streaming"
presenters: "zuo yan"
stype: "中文演讲"
room: "圆明厅"
---

用 Fluss 替换 Kafka 的主要收益如下：
Kafka 使用本地集中式存储，而 Fluss 把冷数据存放在 Paimon 中。借助部署在 HDD 上的 Paimon S3 存储，在不牺牲查询性能的前提下实现了显著的存储成本节省。

### 讲师:


<img src="https://cdn.sessionize.com/image/d1e8-400o400o1-MMvXTnvrxxYuEAieaKuXvD.png" width="200" /><br/>

zuo yan：技术专家

Zuo Yan，技术专家，负责数据中心与日志平台的建设。是 Apache Flink、Apache Doris、Flink CDC、StarRocks、Fluss 等开源项目的贡献者。