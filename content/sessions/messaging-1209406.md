---
title: "Challenges and Breakthroughs in TDMQ for Apache Pulsar: Multi-Modal Storage  Delayed Messaging"
date: ""
track: "messaging"
presenters: "Xiaolong Ran"
stype: "Chinese Session"
---

In the large-scale deployment of Apache Pulsar, storage architecture and delayed messages are two unavoidable core challenges.

On the delayed messaging side, the community solution suffers from message hole issues, high index memory consumption, and long index loading times when dealing with a large volume of delayed messages with randomly distributed delay times. While scaling partitions, increasing bandwidth, and expanding memory can partially mitigate these issues, the cost is prohibitively high and difficult to standardize as a cloud product. This talk will share how TDMQ for Apache Pulsar addresses these challenges, enabling stable large-scale delayed messaging while significantly reducing resource costs.

On the delayed messaging side, the community solution faces several challenges when handling large volumes of delayed messages with highly random delay time distributions, including excessive memory consumption of subscription progress objects and prolonged loading times for delayed message indexes. Although these issues can be partially mitigated by expanding partitions, increasing bandwidth, and scaling up memory, the cost is prohibitively high from an economic perspective, and it is difficult to flexibly adapt to diverse business scenarios from a cloud product standardization standpoint. This talk will share TDMQ for Apache Pulsar's optimization approach and production practices to address these challenges, ensuring stable operation of large-scale delayed messaging while significantly reducing resource costs.

Both topics are based on real production experience from the TDMQ team, aiming to provide valuable insights for large-scale Pulsar deployments on the cloud.

### Speakers:


<img src="https://cdn.sessionize.com/image/252a-400o400o1-h3njznGdpVYDR3J9gMCkjd.jpg" width="200" /><br/>

Xiaolong Ran: Senior R&D Engineer at Tencent Cloud Middleware

Apache Pulsar Committer, author of Pulsar Go Functions, Go Client, and pulsarctl, as well as a Maintainer and one of the core developers of RoP.

