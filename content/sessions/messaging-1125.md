---
title: "Millet RocketMQ cost reduction and efficiency and disaster recovery practice"
date: "2023-08-20T15:45:00" 
track: "messaging"
presenters: "邓志文"
stype: "Chinese Session"
---
Millet uses RocketMQ as an online message queue service, with the gradual expansion of business scale, some problems are gradually revealed, such as high cluster cost, frequent jitter and lack of room disaster recovery, this article will introduce millet in these aspects of some practical experience.
Outline:
- Development history and problems
During the two years that RocketMQ landed in Xiaomi, the scale of business daily production messages grew rapidly to 100 billion levels, covering orders, notifications, Iot and many other business scenarios. At the same time, the high cost of the machine, the lack of high version function in the community, and the imperfect disaster recovery plan have gradually emerged and need to be solved urgently.
- Solution ideas and practice
- Cost reduction practice
Xiaomi selected RocketMQ DLedger mode and realized automatic Failover based on Raft, but the three-copy redundancy brought high machine cost. This section will introduce how Xiaomi greatly reduced the machine cost through the single-machine multi-instance scheme.
- Performance Improvement
The development of business needs and the iteration speed of RocketMQ community versions are very fast, this section describes how Xiaomi weighs and trade-offs between the two, and improves business performance through the implementation of functions such as Batch consolidation, POP consumption, arbitrary delay messages, ZSTD compression upgrades, single multiple instances, etc
- Multi-scenario Dr
This section will introduce Xiaomi's thinking and practice process in the field of RocketMQ disaster recovery in detail, and analyze the pros and cons of three RocketMQ machine room level disaster recovery schemes in detail. This section has been organized into the article "RocketMQ in Millet multi-scenario disaster recovery practice case", published in the Apache RocketMQ public number.
- Summary and outlook
Millet in the process of RocketMQ landing, the cost, efficiency, disaster recovery and other issues have a relatively complete thinking and practice. In the future, we hope to explore cloud-native capabilities such as Stream, Severless and layered storage on the basis of community 5.0 version.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230601/1442446590.png" width="200" /><br>Deng Zhiwen: millet, Software development engineer, Apache RocketMQ Committer, Xiaomi R&D engineer, mainly responsible for message queuing related work.
 <br><br>