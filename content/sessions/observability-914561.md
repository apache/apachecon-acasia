---
title: "eBPF + LLM: DeepFlow's Full-Stack Observability and AI Agent Practice Cases"
date: "2025-07-27T16:45:00"
room:  "Mtn Yang Hall"
track: "observability"
presenters: "Yang Xiang"
stype: "Chinese Session"
---

Apache APISIX, Kafka, RocketMQ, and Pulsar are excellent middleware software with widespread usage. However, observability for these middleware is typically limited to coarse-grained metrics exposure, without correlation to distributed tracing. Therefore, when facing long-tail performance issues, middleware operators often resort to basic tools like tcpdump or log analysis to troubleshoot and identify root causes, which is highly inefficient. eBPF's zero-intrusion characteristics effectively address these pain points. DeepFlow (an open-source project) leverages eBPF to implement full-stack observability covering "code functions, system calls, file I/O, and network forwarding" for various Apache middleware services without requiring any configuration changes or process restarts. Additionally, based on the full-stack observability data exposed through the MCP protocol, DeepFlow AI Agent can quickly and independently identify performance bottlenecks and provide optimization suggestions. This presentation will introduce DeepFlow's middleware full-stack observability implementation practices and typical troubleshooting cases using LLM-powered AI agent.

<img src="https://sessionize.com/image/b6e1-400o400o1-pQaQfhiHLxaGPmnakbBHWu.jpg" width="200" /><br/>

Yang Xiang: Yunshan Networks, President

Received a Ph.D. from Tsinghua University, and currently serving as President at Yunshan Networks and the head of the DeepFlow open-source community. He has presented academic papers on topics such as application observability and network measurement at top international academic conferences including ACM SIGCOMM and ACM IMC.