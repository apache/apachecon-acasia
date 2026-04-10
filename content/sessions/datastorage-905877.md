---
title: Production Practice of Apache Gluten and Apache Celeborn at Xiaomi
date: '2026-08-07T15:00:00'
room: Mtn WanShou Hall
track: datastorage
presenters: Yongyuan Liang
stype: Chinese Session
depth: intermediate
practice_level: 4
projects:
- apache gluten
- apache celeborn
- spark
audience:
- 架构师
- 开发者
- SRE/运维
related_sessions:
- SF Express's Journey with Apache Spark and Gluten
- Accelerating Spark jobs with Apache Gluten at ByteDance Scale
- Xiaomi's Efficient Data & AI Optimization with Apache Paimon
- Celeborn’s Revolution in Multi-Engine Support, Performance Mastery, and Enterprising
  Innovation
- 'Gluten: use native engine to accelerate spark and flink'
---
This talk will dive into the real-world adoption of Apache Gluten and Apache Celeborn at Xiaomi, covering technical background, deployment journey, challenges, and future roadmap.
1. Technology Landscape
Xiaomi has built a large-scale offline computing platform centered around Spark, supporting over 100,000+ offline jobs running daily. This section will introduce the core technical architecture and key components Xiaomi relies on in offline computing, as well as the positioning of Gluten and Celeborn.
2.  Gluten in Production
By adopting Gluten, Xiaomi achieved over 30% average reduction in job runtime and resource cost. We will share our deployment steps, optimization strategies, and the key challenges encountered during the integration.
3. Celeborn in Production
Celeborn played a key role in addressing the instability of Spark External Shuffle Service, significantly improving resource utilization and reducing overall costs. We will showcase its application in real scenarios and the performance tuning techniques we employed.
4. Future Roadmap
We will briefly share Xiaomi's future plans for Spark, focusing on directions for performance optimization, stability improvements, and the introduction of new features

### Speakers:


<img src="https://sessionize.com/image/791b-400o400o1-MfKwkHsY6VSRSHfZmGQa7o.jpg" width="200" /><br/>

Yongyuan Liang: Xiaomi,Beijing

Computing Engine R&D Engineer. Responsible for the development of computing engine