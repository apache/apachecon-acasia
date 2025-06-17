---
title: "Practices of Metrics Collection for Apache Pulsar in Large-Scale Partition"
date: ""
track: "messaging"
presenters: "lin lin"
stype: "Chinese Session"
---

Apache Pulsar is a high-performance messaging queue that supports a massive number of Topics, allowing users to create hundreds of thousands or even millions of partitions within a single cluster. Metrics are a crucial tool for us to identify and diagnose issues in production environments. The effectiveness of observability directly impacts the speed of troubleshooting.
In scenarios with a large number of partitions, enabling Topic-level Metrics can generate a significant number of Metrics strings in a short period, causing severe memory fluctuations and potentially destabilizing the cluster.
This presentation will share our practical experience in collecting Metrics under such high-partition scenarios and explore how to maximize the collection of Metrics data without affecting the stability of online memory, thereby achieving efficient problem identification and system monitoring.

### Speakers:


<img src="https://sessionize.com/image/f542-400o400o1-4vaXwyGZYAujcJxNoeruQG.jpg" width="200" /><br/>

lin lin: Huawei, SDE expert, Middleware technology director

Lin Lin, Huawei SDE expert, Middleware technology director, worked for Tencent and Ant Financial
Focused on middleware and infrastructure, has more than 10 years of relevant experience, and is committed to building high-quality infrastructure
Apache Pulsar Committer & PMC member

