---
title: "规模化场景下的规约驱动开发（Spec-Driven Development）"
date: "2026-08-09T14:00:00"
track: "agenticcoding"
presenters: "Zhangjian He"
stype: "中文演讲"
room: "静明厅"
---

随着 AI 辅助开发成为主流，传统的代码组织方式与开发工作流正日益显得力不从心。大规模代码库、多仓库（multi-repository）环境，以及老旧的企业系统，都为有效应用 AI 带来了严峻挑战。

本次演讲介绍规约驱动开发（Spec-Driven Development，SDD），作为规模化 AI 辅助工程的一种实践方法。SDD 不再依赖临时的（ad-hoc）prompt，而是把规约（specification）视为一等公民，用以驱动代码生成、验证与演进。

本次演讲聚焦大规模环境下的真实挑战与解决方案：

- 代码库结构化：设计对 AI 友好、与规约对齐的仓库与模块结构
- 跨仓库协同：使用规约驱动的工作流，管理多个仓库之间的依赖与变更
- 企业集成：将 SDD 集成到现有系统、CI/CD 流水线以及开发流程中

### 讲师:


<img src="https://cdn.sessionize.com/image/a7d4-400o400o1-4GZYizF3DAJcbH1tVcZhj4.jpg" width="200" /><br/>

Zhangjian He：华为云高级工程师 | 华为云开源团队成员

开源爱好者，经验丰富的工程师。自 2017 年开始软件开发以来，我在华为云物联网平台的云原生转型以及工业物联网平台的开发中扮演了关键角色。我担任 Apache BookKeeper/ServiceComb 的 PMC 成员、Apache Pulsar Committer，以及 CNCF openGemini Maintainer。我的专长涵盖编码、软件工程、开源与生态建设，致力于推动最佳实践与开发标准。