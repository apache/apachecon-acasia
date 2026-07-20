---
title: "使用 SkyWalking 10.4 监控 LLM 应用：性能与成本的洞察"
date: "2026-08-09T14:00:00"
track: "observability"
presenters: "YiMing Shao"
stype: "中文演讲"
room: "阳山会议室"
---

本次演讲将从 Apache SkyWalking 10.4 的突破性特性——AI 可观测性（AI Observability）的介绍开始。我们将探讨监控大语言模型（LLM）应用的战略重要性，以及 Envoy AI Gateway 在基础设施边缘保障和管理 AI 流量方面所扮演的角色。

演讲的核心将聚焦于这一新特性的技术架构与原理。我们将以 SkyWalking Spring AI agent 插件和 Envoy AI Gateway 为主要示例，展示遥测数据如何在 AI 技术栈的不同层被采集。随后，我们将深入讲解可观测分析平台（OAP）如何处理这些数据，重点介绍如何把 OTLP 和 Zipkin 格式的链路数据转换为可操作的统计指标。整个工作流最终会以开箱即用的仪表盘如何将这些洞察可视化作为收尾。

为了提供更广阔的视角，我们将在最后讨论当前的 AI 可观测性版图。我们会考察 Langfuse 和 Arize AI 等业界领先者，分析他们各自独特的做法——从 LLM 生命周期链路追踪、prompt 管理，到模型评估与防护（guardrails）——并与 SkyWalking 的生态进行对比。

### 讲师:


<img src="https://cdn.sessionize.com/image/1dda-400o400o1-UaYwPFBbWkcjx4seCrUQP2.jpg" width="200" /><br/>

YiMing Shao：Apache SkyWalking Committer

Apache SkyWalking Committer
主要专注于可观测性领域的研究。