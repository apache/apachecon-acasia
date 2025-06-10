---
title: "From Hadoop to Kubernetes: The Cloud-Native Evolution of Li Auto's Big Data Platform"
date: ""
track: "cloudnative"
presenters: "Han Qian"
stype: "Chinese Session"
---

Abstract:
In the construction of our big data platform, we transitioned from traditional deployments using the Apache Hadoop ecosystem to achieving storage-compute separation with JuiceFS, and finally migrated to a Kubernetes-centric scheduling system. This technological evolution spans three aspects: storage, computing, and cluster architecture, aiming to enhance data processing efficiency.

Storage Optimization
By replacing HDFS with JuiceFS, we implemented elastic computing with centralized storage, resolving capacity scaling and resource utilization challenges in cloud environments.

Compute Scheduling
Transitioning from YARN to Kubernetes, we focused on optimizing job scheduling policies, resource isolation, and job stability to improve scheduling efficiency.

Cluster Architecture Optimization
Through integrating Kubernetes and JuiceFS, we built a scalable cloud-native architecture that addresses compatibility and scalability issues of big data frameworks (e.g., Apache Spark, Flink) in cloud environments, ensuring efficient execution of large-scale AI and data processing tasks.

Discussion Topics
This session will share our technical practices and insights, including:

Adaptation experiences with Apache projects (Hadoop, Spark, YARN)
Challenges encountered in architecture evolution phases, such as JuiceFS metadata performance, Spark Shuffle on object storage, and Flink Checkpoint reliability, which were resolved through community collaboration
Strategies for maintaining production stability while advancing open-source technology ecosystems, balancing innovation with system reliability to avoid operational risks
We aim to provide actionable references for teams undergoing similar transformations, sharing decision-making logic for critical technology selections and migration paths at different stages. This case study documents an enterprise-level evolution of a big data platform while offering practical guidance to teams embracing cloud-native architectures.

### Speakers:


<img src="https://sessionize.com/image/e9db-400o400o1-pJDLPcWh44dKmtxc2n8k7U.jpg" width="200" /><br/>

Han Qian

Head of Big Data Infrastructure @ Li Auto
Lead Architect of 100PB-scale data platforms serving 1M+ connected vehicles

Core Expertise
Built streaming engine & OLAP system for Baidu Ads and JD Ads
Designed EB-scale data lake & 1M-core resource orchestration framework for ByteDance
