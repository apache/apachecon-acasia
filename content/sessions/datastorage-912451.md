---
title: "Cross-Version Upgrade to HBase 2.3 and Stability Governance at Xiaomi"
date: ""
track: "datastorage"
presenters: "Zhiwen Deng"
stype: "Chinese Session"
---

Abstract:
At Xiaomi, HBase serves as a distributed wide-table service for both offline and online scenarios. However, 40% of nodes still operate on version 0.98 internally, resulting in high maintenance costs due to dual-version support. Unifying the version to 2.3 is critical to improving development efficiency. Additionally, version 2.3 itself faces stability challenges, such as GC issues and cluster-wide downtime recovery failures. This presentation shares Xiaomi’s practical experience in addressing these challenges.

Outline:
Session 1: Development History and Challenges
HBase has a long history at Xiaomi, but this has accumulated technical debt. Key challenges include:
- Version Fragmentation : The 2.3 upgrade spanned 3 years, with dual-version maintenance consuming significant resources.
- Version 2.3 Stability Issues : Problems like GC bottlenecks and unrecoverable cluster-wide downtime persisted.

Session 2: Solutions and Implementation
2.1 Version Unification
Historical upgrade failures eroded trust in cross-version upgrades, delaying unification. To address this:
- Optimized Log-split to ensure data is processed only by same-version servers, preventing data loss.
- Enhanced Replication to allow concurrent synchronization and upgrades, resolving critical upgrade roadblocks.
Completed smooth upgrades for all shared clusters, achieving full version unification.

2.2 GC Optimization
After migrating to 2.3, adopting Prometheus monitoring increased HBase memory usage due to jmx-to-Prometheus conversion , triggering frequent Full GC and long-term Young GC in production. Solutions included:
- Tuning G1 parameters to mitigate GC-induced latency spikes.
- Upgrading to JDK 17 and enabling ZGC on select clusters, reducing GC pauses to <10ms and stabilizing latency.

2.3 Service Enhancements
Additional optimizations to bolster stability:
- Meta request isolation , Zookeeper weak dependency , Balancer upgrades .
- Tackling RS request/restart blockages , adopting ZSTD compression , and automating service checks/fault recovery .
These efforts achieved 99.95% availability , meeting business requirements.

Session 3: Summary and Future Directions
- Xiaomi has invested heavily in stabilizing HBase over the past year. Future goals include:
  - Multi-data-center disaster recovery .
  - Second-level cluster scaling .
  - Multi-model engine integration (e.g., time-series, graph).
Aims to address evolving needs in cost efficiency, stability, and functionality.

### Speakers:


<img src="https://sessionize.com/image/6052-400o400o1-npyQeJA1PdnzCtTC2HXP7X.jpg" width="200" /><br/>

Zhiwen Deng: Xiaomi Software R&D Engineer

Xiaomi distributed system R&D engineer, participated in the design and implementation of message queues and HBase, and is also the committer of Apache RocketMQ

