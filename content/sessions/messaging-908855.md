---
title: "Virtual Queue in RocketMQ 5.0: Enhancing Backward Compatibility With Legacy Remoting-Based Clients"
date: "2025-07-26T16:15:00"
room: "JingYi Hall"
track: "messaging"
presenters: "Shengzhong Liu"
stype: "Chinese Session"
---

Apache RocketMQ is a distributed messaging and streaming platform known for its low latency, high performance, and high reliability. The newly released version 5.0 has two major advancements:
1. Decouples storage from compute to achieve better scalability and cloud-native adaptability.
2. Introduces POP consumption mode to shift the balancing logic from clients to the broker.
To adapt to these features, the community has launched a new gRPC-based client. However, existing users who access RocketMQ with a remoting-based client cannot benefit from these 5.0 advancements unless they update their code and replace the client SDK. To enhance backward compatibility with legacy remoting-based clients, we propose a virtual queue solution in RocketMQ 5.0, and it has been fully validated in practice on Tencent Cloud.

### Speakers:


<img src="https://sessionize.com/image/5517-400o400o1-QHVT45RWPFxxgwib7bn9VX.jpg" width="200" /><br/>

Shengzhong Liu: Tencent.

Since graduating from Southeast University in 2019, I have been working at Tencent Cloud as a software development engineer, with a focus on message queue technologies in recent years.