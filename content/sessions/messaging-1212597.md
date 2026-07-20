---
title: "Apache RocketMQ For AI: Reliable Collaboration Mechanisms for Multi-Agent Systems"
date: "2026-08-09T15:15:00"
track: "messaging"
presenters: "Zhou Li"
stype: "Chinese Session"
room: "JingYi Hall"
---

Section 1: Engineering Challenges in Agent Collaboration
1.1 Communication Complexity: Link fragmentation, resource contention, and scheduling blind spots under concurrent inference.
1.2 Engineering Hazards: Disrupted communication links, resource contention and scheduling failure caused by transient bursts, and the difficulty of fault recovery following the loss of collaborative context.

Section 2: Lite-Topic: Efficient Routing and Scheduling for Massive Sessions
2.1 Dynamic Session Management: Building a TTL-based, second-level dynamic topology to achieve logical isolation of session spaces between agents.
2.2 ReadySet Scheduling Mechanism: Optimizing the delivery efficiency of massive agent events via distributed brokers, addressing "thundering herd" problems and latency jitter under ultra-high concurrency.

Section 3: RocketMQ-A2A Asynchronous Interaction Model: Decoupling and Deterministic Control
3.1 Asynchronous Paradigm Refactoring: Building a full-link asynchronous model for "task orchestration, trigger execution, and result return," sinking collaboration logic into the RocketMQ foundation.
3.2 Deterministic Communication Orchestration: Defining standardized protocols for inter-agent communication to ensure the deterministic execution of complex business flows.

Section 4: Collaborative Consistency and Observability: Constructing Event-Driven Evidence Chains
4.1 Semantic Enhancement and State Recovery: Leveraging idempotency design and event logs to achieve atomic interruption replay and lossless state migration for agent collaboration flows.
4.2 Full-Link Collaborative Auditing: Creating "collaborative evidence chains" based on structured messages to transform fragmented agent behaviors into traceable and attributable system governance data.

Section 5: Large-Scale Cluster Performance and Practical Closed-Loop
5.1 Stability and fault recovery under high-pressure collaboration.
5.2 How AI gateways leverage the messaging foundation to achieve fault self-healing and collaborative task orchestration for large-scale multi-agent systems.

### Speakers:


<img src="https://cdn.sessionize.com/image/89b7-400o400o1-3UL89hviMkFYw2SmgNyGZM.jpg" width="200" /><br/>

Zhou Li: aliyun

Messaging Expert at Alibaba Cloud, responsible for Alibaba's core messaging middleware