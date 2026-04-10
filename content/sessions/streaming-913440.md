---
title: Kwai Flink Cloud Native Architecture Evolution
date: '2026-08-07T17:45:00'
track: streaming
presenters: Mang Zhang, Heart Zhou
stype: Chinese Session
room: YuanMing Hall
depth: advanced
practice_level: 4
projects:
- flink
- kubernetes
- yarn
audience:
- 架构师
- 开发者
- SRE/运维
related_sessions:
- The Intelligent Evolution of Fully Managed Resource Management for Tencent's Real-Time
  Computing
- ' Unlocking maximize heterogeneous GPU utilization in Cloud Native way: Leveraging
  the Power of HAMi'
- 'When Flink Meets Fluss: The Future of Streaming Warehouse'
- 'Apache Flink 2.1: Continuing Evolution Toward Data + AI All-in-One'
- 'From Hadoop to Kubernetes: The Cloud-Native Evolution of Li Auto''s Big Data Platform'
---
After years of development, Kwai Flink has reached a resource scale of millions of cores, covering all business scenarios across the group, over tens of thousands of jobs running in the cluster. However, the Flink cluster exhibits significant load fluctuation effects, and cost issues are becoming increasingly prominent, alongside challenges in cluster scaling and operation and maintenance.
Kubernetes (K8S) has matured and is widely adopted, making cloud migration of engines an industry trend. K8S can unify dispersed resource pools for online services, real-time computing, and offline computing, maximizing resource utilization in the cluster through mutual load balancing. Therefore, the cloud-native transformation of Flink is urgent. Additionally, unifying under the K8S technology stack can also reduce operation and maintenance as well as development costs.
Kwai has gone through three major stages: Flink On YARN, Flink On YARN On K8S, and Flink Native On K8S. This presentation will discuss the challenges, solutions, and benefits encountered by Kwai during the cloud migration of Flink.

### Speakers:


<img src="https://sessionize.com/image/d342-400o400o1-wMgMNhMG7uPCpRJT7o2iXT.jpg" width="200" /><br/>

Mang Zhang: Flink Contributor

10 years of experience in big data engine development and big data architect. Rich experience in big data real-time and offline, good at architecture and solution design for big data scenarios.


<img src="https://sessionize.com/image/ac91-400o400o1-7VFwoH4QWgUqtcDeshVnqZ.jpg" width="200" /><br/>

Heart Zhou: Kwai

Streaming Engineer