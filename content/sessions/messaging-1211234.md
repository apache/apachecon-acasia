---
title: "Rethinking High Availability for Apache RocketMQ on the Cloud: Protocol-Fenced Takeover for Second-L"
date: ""
track: "messaging"
presenters: "Rongtong Jin"
stype: "Chinese Session"
---

High availability for stateful messaging systems in the cloud is often constrained by a difficult trade-off among cost, steady-state performance, and failover speed. Replication-based approaches can reduce recovery time, but they usually introduce extra write amplification, resource overhead, and operational complexity. In contrast, single-replica deployments preserve performance and cost efficiency, yet their failover path in Kubernetes is often dominated by slow and unpredictable volume detach/attach workflows.

In this session, I will share how we rethought high availability for Apache RocketMQ on the cloud and built a production-proven architecture that achieves second-level failover without adding extra data replicas in the steady state. The key idea is to keep RocketMQ’s normal storage path unchanged while redesigning the takeover path around Multi-Attach block storage and NVMe Persistent Reservation. This protocol-fenced takeover model allows a new node to safely preempt disk ownership, prevent split-brain, and resume service quickly without waiting for the traditional storage migration process.

I will walk through the architecture, failure detection and takeover workflow, safety and consistency considerations, and the implementation details in Apache RocketMQ. The talk will also cover how decentralized lease probing, node-side takeover orchestration, and crash-consistent recovery work together to shorten and stabilize the failover critical path.

Finally, I will share production experience from Alibaba Cloud, where this architecture has already been deployed for Apache RocketMQ services and validated through large-scale disaster recovery drills. The underlying work behind this session has also been accepted by the FSE 2026 Industry track, while this talk will focus on the production architecture, engineering trade-offs, and practical lessons learned from Apache RocketMQ. Attendees will gain practical insights into designing highly available stateful messaging systems in cloud-native environments, and learn how to balance recovery objectives with cost and performance in real-world production systems.

### Speakers:


<img src="https://cdn.sessionize.com/image/c982-400o400o1-fRQaABrX2ckEWrDpwXmMNW.jpg" width="200" /><br/>

Rongtong Jin: Technical Expert at Alibaba Cloud, Apache RocketMQ PMC Member

Rongtong Jin is a Technical Expert at Alibaba Cloud and a PMC Member of Apache RocketMQ. He works on the architecture and production operations of cloud messaging systems, with a focus on high availability, storage reliability, and large-scale stateful services. He has extensive experience in the cloud evolution, production rollout, and stability engineering of Apache RocketMQ.

