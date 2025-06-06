---
title: "Real-Time Assurance Practices for Tencent Big Data Flink on Cloud-Native Hybrid Low-Priority Cluster"
date: ""
track: "streaming"
presenters: "Pengxiang Wang"
stype: "Chinese Session"
--- 

1. Background
    a. Oceanus is Tencent's big data real-time computing platform, providing full lifecycle services for real-time applications based on Apache Flink.
    b. The computing resources are idle, low-cost, and low-priority resources mined by Tencent Big Data through cloud-native hybrid deployment, built on large-scale federated clusters. These resources offer high elasticity and low cost but are prone to eviction and instability.
    c. Under the goal of cost reduction and efficiency improvement, leveraging the low-priority computing resources has reduced real-time operational costs, meeting the demands of core businesses like Tencent Ads, while simultaneously posing severe challenges to Flink's real-time stability.

2. Stability Assurance
    a. Single-point restart: Tolerates minimal data loss while ensuring zero-interruption recovery at the Flink kernel level, with optimizations for scenarios like concurrent failures in upstream/downstream tasks and supporting bounded stream.
    b. Hot migration: Delivers seamless, interruption-free eviction and operational capabilities. Collaborating with Tencent's cloud-native architecture team, we've reengineered Kubernetes' eviction-reallocation mechanism into a state-preserving migration process, cutting transition latency by 60% and enabling reliable utilization of cost-efficient resources.
    c. Hot updates: Enables configuration adjustments at runtime, supporting horizontal rescaling with TaskManager resources reservation, cutting downtime from minutes to seconds.
    d. Leveraging container resource resize, we developed dynamic adjustment of NetworkBuffer (MaxDirectMemory) for horizontal elasticity and pod heap memory for vertical rescaling based on Tencent's kona JDK.

3. Performance Optimization
    a. Accelerating TM deployment: By packaging frequently-used business platform JARs into customized initContainer images and mounting them to the main container, we leverage image caching to eliminate repetitive downloads from HDFS, reducing bandwidth consumption.
    b. Flink data transfer optimization: By replacing the traditional rebalance strategy with a credit-based autoPartition mechanism, we effectively mitigate long-tail effect caused by slow nodes, achieving over 3x throughput improvement in advertising scenarios.

4. Future Roadmap
    a. Building upon the existing lossy single-point restart mechanism, we explore lossless recovery capabilities.
    b. Develop a universal JM failover high-availability solution to address single-point vulnerabilities of JobManager.



### Speakers:

<img src="https://sessionize.com/image/d261-400o400o1-fxPaH1DkrWnKKr7M1jP91s.jpg" width="200" /><br/>

Pengxiang Wang,  graduated from Beihang University, senior software engineer from Tencent big data, having lots of practicing experience in real-time data processing, mainly focusing on stability improvement of Flink in runtime.