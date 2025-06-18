---
title: "Empowering Serverless Messaging Architectures with Apache RocketMQ"
date: "2025-07-25T16:15:00"
room:  "JingYi Hall"
track: "messaging"
presenters: "Juntao Ji"
stype: "Chinese Session"
---

In our latest work, which was accepted to the the ACM FSE 2025 Industry Track, Apache RocketMQ serves as a powerful foundation for serverless messaging systems, addressing the scalability, cost, and metadata challenges of traditional middleware. By decoupling storage and compute, Apache RocketMQ enables independent resource scaling, critical for unpredictable cloud workloads. Its elastic write partitions eliminate single-queue throughput limits, while light message queue support millions of queues with minimal cold-start latency. 

We demonstrate this with our RocketMQ-based RabbitMQ implementation, which retains full protocol compatibility while overcoming RabbitMQ’s scaling limitations. Leveraging RocketMQ’s architecture, we achieved unlimited horizontal scalability and improved metadata management efficiency by over 1000%. This serverless solution operates commercially on Alibaba Cloud. Our experiences illustrate RocketMQ’s ability to transform legacy messaging systems into cloud-native services, providing a blueprint for future-proof serverless architectures.

### Speakers:


<img src="https://sessionize.com/image/dd3d-400o400o1-JenBFKL54ncn91nqVyA8nE.jpg" width="200" /><br/>

Juntao Ji: Senior Development Engineer (Alibaba Cloud Computing)

Senior middleware R&D engineer at Alibaba Cloud Computing, responsible for the feature development of RocketMQ and RabbitMQ. Contributor to the Apache RocketMQ open source community. Published several top papers in CCF-A conferences or journals (ASE 23', FM 24', FSE 25', etc.).