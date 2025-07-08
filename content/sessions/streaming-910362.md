---
title: "The Intelligent Evolution of Fully Managed Resource Management for Tencent's Real-Time Computing"
date: "2025-07-26T15:45:00"
room: "YuanMing Hall"
track: "streaming"
presenters: "Zihao Chen, Jiangang Liu"
stype: "Chinese Session"
---

1. Background and Industry Pain Points
  a. Flink, as a long-running stateful computation, is widely used in scenarios such as real-time data warehousing, real-time analytics, and online training.
  b. Real-time resource configuration and operations are a universal challenge: over-provisioning leads to waste, while under-provisioning causes lag and failover. Additionally, resource demands vary significantly over time.
2. Evolution of Autoscaling Architecture — Fully Managed Intelligent Resource Management
  a. Automated resource solutions for the entire lifecycle of jobs, including startup, runtime, upgrades, and exceptions (lag, failover).
  b. Leveraging AI models to achieve precise forecasting (reducing prediction errors from 25% to 10%), enabling a shift from reactive to proactive resource management.
  c. Extreme elasticity in cloud-native environments, integrating horizontal and vertical scaling technologies to improve job resource utilization to 90%.
3. Core Technology Optimization — Production-Ready Horizontal and Vertical Scaling
  a. Horizontal Scaling: Optimized with hot updates and preloading to achieve highly scalable second-level scaling.
  b. Vertical Scaling: Breakthroughs in in-place pod resource changes enable zero downtime for real-time jobs and personalized pod configurations.
4. Production Cases — From Technology to Business Value
  a. Stability: Applied to Tencent Video, finance, and gaming businesses, reducing failure rates by 70%.
  b. Resource Savings: Applied to real-time reporting and data synchronization scenarios, improving resource utilization by 30%.
5. Future Plans
  a. Large-model-driven full resource management services to further enhance intelligence.
  b. Horizontal Scaling: Implement elasticity at the operator level to avoid complete downtime.
  c. Vertical Scaling: Combine with hot migration technology for pods to break single-machine limitations.

### Speakers:


<img src="https://sessionize.com/image/c17d-400o400o1-3ksWtZ8Yz4P3kYR9cEC4tH.jpg" width="200" /><br/>

Zihao Chen: Tencent, Software Development Engineer

Zihao has been engaged in R&D related to the Flink kernel for many years. In recent years, he has mainly focused on developing the autoscaling capabilities of Flink, which are aimed at improving the stability and resource utilization of Flink jobs. Additionally, he published an industry paper at SIGMOD conference about autoscaling in streaming scenarios.

<img src="https://sessionize.com/image/95fa-400o400o1-pRGUUw1BJpnhknhJaHnEvg.png" width="200" /><br/>

Jiangang Liu: Tencent, Head of Real-time Computing Flink

Tencent Real-Time Computing Flink Lead, specializing in the cloud-native evolution, elastic scaling, and separation of storage and computation. Previously served as the Flink Technical Lead at Kuaishou, leading real-time computing architecture design and large-scale implementation, successfully driving the real-time connection project between Kuaishou and CCTV Spring Festival Gala in 2020. Prior to that, participated in Baidu Matrix's development work in offline hybrid computing.