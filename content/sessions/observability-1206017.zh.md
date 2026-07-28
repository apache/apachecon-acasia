---
title: "使用 SkyWalking 10.4 监控 LLM 应用：从性能、成本到质量的可观测性"
date: "2026-08-09T13:30:00"
track: "observability"
presenters: "YiMing Shao"
stype: "中文演讲"
room: "阳山会议室"
---

  随着大语言模型逐步进入生产系统，传统 APM 已不足以回答模型选择、Token 消耗、首 Token 延迟、调用成本与输出质量等关键问
  题。本次演讲将介绍 Apache SkyWalking 10.4 的 AI 可观测性能力，展示如何将 LLM 调用转化为可关联、可分析、可运营的观测数
  据。

  演讲以 SkyWalking Spring AI 1.x Agent 插件为例，说明如何自动采集 Chat、Streaming、Tool Calling、RAG Retrieval、
 Vector Search 等调用，并遵循 OpenTelemetry GenAI Semantic Conventions 上报模型、Provider、Token、TTFT 及
  请求响应等数据。同时也会简要介绍 Envoy AI Gateway 如何从网关侧通过 OTLP 上报 GenAI 指标与访问日志，为 AI 流量提供基础
  设施层的观测入口。

  随后将深入 OAP 的处理流程：SkyWalking 如何接收 SkyWalking、OTLP 与 Zipkin Trace，匹配 Provider 与 Model，加载模型定价
  配置并计算预估成本，最终生成按 Provider 和 Model 聚合的性能、Token、SLA 与成本指标，并通过开箱即用的 Dashboard 展示。

  最后将介绍正在演进的 LLM as Judge 评测能力：系统可对 GenAI Span 进行采样评测，依据可配置的 Rubrics 生成质量记录、等级
  和评分指标，并与 Trace、Dashboard 和告警关联，形成从调用采集、性能与成本分析到质量评测的完整闭环。

### 讲师:


<img src="https://cdn.sessionize.com/image/1dda-400o400o1-UaYwPFBbWkcjx4seCrUQP2.jpg" width="200" /><br/>

YiMing Shao：Apache SkyWalking Committer

Apache SkyWalking Committer
主要专注于可观测性领域的研究。
