---
title: "Exploration and Practice of Low-Latency Optimizations in Apache RocketMQ"
date: ""
track: "messaging"
presenters: "熙凯 魏"
stype: "中文演讲"
---

In some of our usage scenarios, strict low-latency requirements exist, with the core demand being that P99 or maximum latency is stably controlled within a fixed threshold. This talk shares the exploration and efforts our team has made in optimizing and implementing the low-latency mode of Apache RocketMQ. Starting from the core latency bottlenecks in the RocketMQ architecture, we sort out the key links affecting end-to-end latency, including network transmission, message scheduling, and resource allocation, and elaborate on the targeted optimizations, architectural adjustments, and implementation effect verification we have carried out. Additionally, this topic will share the methodologies and practical experiences of RocketMQ full-link latency tuning, hoping to provide some help to community developers and users.

### 讲师:


<img src="https://cdn.sessionize.com/image/6bdf-400o400o1-HSmKWKawRzfoxashePJybP.jpg" width="200" /><br/>

熙凯 魏: 腾讯云消息中间件高级开发工程师

腾讯云高级开发工程师，拥有多年计算、存储及分布式系统性能优化经验。

