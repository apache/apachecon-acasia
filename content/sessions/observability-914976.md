---
title: "Best Practices for Messaging Systems Observability: A Case Study of Apache RocketMQ & OpenTelemetry"
date: "2025-07-27T14:00:00"
room:  "Mtn Yang Hall"
track: "observability"
presenters: "Minghui Zhang"
stype: "Chinese Session"
---

In distributed systems, Apache RocketMQ serves as a core messaging middleware, and its performance optimization and fault diagnosis often directly impact the stability and efficiency of the entire system. However, as business complexity grows, the observability of messaging systems is increasingly becoming a key factor in addressing production issues.
This session will focus on practical approaches to enhancing Apache RocketMQ's observability, with an emphasis on how OpenTelemetry can improve client transparency and address challenges in complex scenarios such as multi-messaging system integration. For the client-side, we will demonstrate the use of zero-code instrumentation tools to automatically monitor the operational status of producers and consumers. Key metrics like RED (Rate, Errors, Duration), consumer lag, and others will be observed, alongside an exploration of how distributed tracing technology can enable end-to-end correlation across upstream and downstream systems. This includes common send/receive operations, batch processing, and poll-mode scenarios. Additionally, we will introduce continuous profiling techniques to help capture performance bottlenecks in real-time and quickly pinpoint issues.
For specialized scenarios, we will take the Internet of Things (IoT) as an example to analyze the observability challenges when integrating MQTT with Apache RocketMQ. We will discuss strategies for building lightweight, unified TraceContext to achieve cross-protocol full-chain tracing.
By attending this session, you will gain a deep understanding of the core methodologies for integrating observability into messaging systems, along with actionable solutions ranging from client-side optimization to handling complex scenarios. These insights will empower you to tackle performance tuning and fault diagnosis challenges with greater confidence and efficiency.

### Speakers:


<img src="https://sessionize.com/image/9377-400o400o1-Ugp4XdU1Y7Gr49zsJjkss6.jpg" width="200" /><br/>

Minghui Zhang: Alibaba Cloud, Hangzhou

As the developer of Alibaba Cloud APM's auto instrumentation tools, I specialize in providing immediate, out-of-the-box solutions for Java, Golang, and more, leveraging the OpenTelemetry standard. My expertise in equipping users with cloud-native APM capabilities has enhanced application performance monitoring across various cloud environments.