---
title: "RocketMQ 5 in Production at Meituan"
date: ""
track: "messaging"
presenters: "Jiangge Zhang"
stype: "中文演讲"
---

Meituan operates one of China's largest internal messaging platforms, originally built on an early Kafka fork—internally known as Mafka. Mafka served us well, but over time hit two hard limits. First, consumer scalability was capped by partition count: adding more consumer instances beyond the number of partitions yielded no throughput gain. Second, the client became a heavyweight artifact—carrying complex routing logic and a wire protocol that made cross-language support a maintenance nightmare.

Apache RocketMQ 5 addressed both. The Pop consumption model manages message lifecycle per message rather than per partition, allowing a queue to be shared across consumers simultaneously—unlocking horizontal elasticity. The Proxy architecture, built on gRPC, enables lightweight, language-agnostic clients. But RocketMQ 5 out of the box could not cover what Meituan needs at scale: a unified global metadata layer and enterprise-grade traffic isolation across multiple deployment environments and business units.

This talk walks through the decisions and trade-offs behind our production adoption of RocketMQ 5 at Meituan. We cover three areas: first, how we designed a three-tier topology—tenant, placement group, and cluster—where placement groups serve as blast-radius boundaries within a tenant; second, how we implemented multiple modes of traffic isolation and routing entirely outside RocketMQ, so the broker stays a pure messaging primitive and isolation policies can evolve independently; third, how we built a single authoritative metadata service to keep all components in sync.

We will ground the talk in real-world results from active production migration. Running at scale has validated our core architectural choices, but also surfaced hard problems we are still working through—from data-plane constraints in RocketMQ 5's replication model to capacity isolation challenges inherent in its shared commit log design. We hope these production learnings are useful to the broader RocketMQ community.

### 讲师:


<img src="https://cdn.sessionize.com/image/52fa-400o400o1-PcJvReCZbyEkp2HS9DpDKt.jpg" width="200" /><br/>

Jiangge Zhang: Software Architect at Meituan

Jiangge Zhang is an architect at Meituan, working on the messaging infrastructure team. He previously worked on SOA middleware and has been focused on large-scale distributed systems throughout his career.

