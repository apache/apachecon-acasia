---
title: "Lessons Learned in Building a Cloud MQTT Solution"
date: "2025-07-26T14:30:00"
room: "JingYi Hall"
track: "messaging"
presenters: "Senze Zhang"
stype: "Chinese Session"
---

MQTT has emerged as the de facto standard for the Internet of Things (IoT), powering a wide range of applications across industries such as automotive, manufacturing, telecommunications, oil and gas, and more.

At Tencent Cloud, we have developed a robust, cloud-based MQTT solution built on a shared, resilient stream log. In this presentation, we will share key insights and lessons learned from our development journey. We will begin by outlining the overall architecture, highlighting performance optimizations, and sharing operational best practices. Next, we will delve into how we implemented the MQTT protocol on top of a shared log—a design that can be extended to support other messaging protocols. We will also explore our strategies for scaling the system dynamically to support millions of connected devices while maintaining high performance and reliability. Finally, we will discuss how decoupling storage and computing, combined with a dedicated MQTT load balancer, enables us to reduce the total cost of ownership (TCO) and handle traffic spikes with flexibility and efficiency.
### Speakers:


<img src="https://sessionize.com/image/8338-400o400o1-J1yXkRRbD17bMbsVpMyBw8.png" width="200" /><br/>

Senze Zhang: Apache RocketMQ Committer

Senze Zhang is a seasoned engineer specializing in the field of message queuing systems. With extensive experience in the design, implementation, and optimization of high-performance messaging solutions, Senze has participated in deploying various industry-leading message queuing platforms including RocketMQ, Kafka, and MQTT.