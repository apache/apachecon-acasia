---
title: "从湖仓到 AI 数据湖：小米 AI 场景数据存储与计算架构演进"
date: ""
track: "datalake"
presenters: "Kainan Bao"
stype: "中文演讲"
---

尽管湖仓架构已成为商业智能（BI）工作负载的事实标准，但当它被扩展到大规模基础模型训练管道时，却面临两个根本性瓶颈。与以结构化表格数据为中心的传统 BI 不同，AI 训练需要处理海量的非结构化数据（文本、图像、音频、视频），这暴露出统一非结构化数据治理方面的关键缺口，以及基于 Hadoop 的数据处理与云原生模型训练基础设施之间的架构孤岛。

本次演讲介绍小米经过生产验证的两阶段架构演进，以应对这些挑战。第一阶段使用 Gravitino 和 Fileset 将非结构化数据纳入统一的元数据治理层，并通过 GVFS 实现云对象存储与 Hadoop 生态之间的无缝互操作。第二阶段采用 Ray-Lance 技术栈，突破了传统 Hadoop 技术栈的局限——以 Ray 作为云原生分布式计算引擎，以 Lance 作为面向 AI 优化的存储格式。听众将了解到实际的实现细节，以及来自生产用例（包括增量数据去重和多模态数据管理）的真实性能收益。

### 讲师:


<img src="https://cdn.sessionize.com/image/a5e2-400o400o1-GdvaUKeFWkpXjmo5rWQVTC.jpg" width="200" /><br/>

Kainan Bao：小米软件工程师 | 小米 Mimo 模型核心贡献者 | Iceberg、Paimon 与 Gravitino 的贡献者

小米软件工程师，小米 Mimo 模型核心贡献者，负责小米 Mimo 基础模型训练的 PB 级数据处理。擅长解决处理海量多模态非结构化数据（包括文本、图像和视频）的独特挑战。

在数据湖治理方面经验丰富，曾向 Iceberg、Paimon 与 Gravitino 开源社区贡献。在本次演讲中，他将分享小米如何演进其传统数据湖、用 Gravitino 统一结构化与非结构化数据治理，并使用 Ray 和 Lance 构建 AI 原生数据处理系统。
