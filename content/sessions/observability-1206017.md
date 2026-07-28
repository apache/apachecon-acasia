---
title: "Observing LLM Applications with SkyWalking 10.4: From Performance and Cost to Quality"
date: "2026-08-09T13:30:00"
track: "observability"
presenters: "YiMing Shao"
stype: "Chinese Session"
room: "Mtn Yang Hall"
---

As large language models (LLMs) become increasingly integrated into production systems, traditional APM solutions are no longer sufficient to answer critical questions such as model selection, token consumption, time to first token (TTFT), inference cost, and response quality. This session introduces the AI observability capabilities of Apache SkyWalking 10.4 and demonstrates how LLM interactions can be transformed into correlated, analyzable, and actionable observability data.

Using the SkyWalking Spring AI 1.x Agent plugin as an example, the session will demonstrate how to automatically instrument Chat, Streaming, Tool Calling, RAG Retrieval, and Vector Search operations. It will also explain how these interactions are reported according to the OpenTelemetry GenAI Semantic Conventions, including model and provider information, token usage, TTFT, request and response metadata, and other GenAI telemetry. In addition, the session will briefly introduce how the Envoy AI Gateway exports GenAI metrics and access logs via OTLP, providing infrastructure-level observability for AI traffic.

The talk will then dive into the OAP processing pipeline. You'll learn how SkyWalking ingests traces from SkyWalking native agents, OTLP, and Zipkin, identifies the corresponding providers and models, applies configurable model pricing, estimates inference costs, and generates aggregated metrics for performance, token usage, SLA, and cost across providers and models. These insights are available immediately through out-of-the-box dashboards.

Finally, the session will present the evolving LLM as Judge evaluation capability. SkyWalking can sample GenAI spans for quality evaluation, apply configurable rubrics to generate quality records, ratings, and evaluation metrics, and correlate the results with traces, dashboards, and alerts. Together, these capabilities provide an end-to-end AI observability workflow—from telemetry collection and performance/cost analysis to automated quality evaluation.

### Speakers:


<img src="https://cdn.sessionize.com/image/1dda-400o400o1-UaYwPFBbWkcjx4seCrUQP2.jpg" width="200" /><br/>

YiMing Shao: Apache SkyWalking Committer

Apache SkyWalking Committer
Primarily focused on research in the observability domain.
