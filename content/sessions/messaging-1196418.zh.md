---
title: "Apache RocketMQ Routing Control Plane Evolution"
date: ""
track: "messaging"
presenters: "Xiao Yang"
stype: "中文演讲"
---

This session explains how we evolved a lightweight external routing control plane for Apache RocketMQ to support large-cluster governance without changing brokers, nameservers, or client access patterns.

As multiple business lines gradually shared one common cluster, the real challenge shifted from throughput to governance: faster failure convergence, controllable topic migration, and flexible lane-based traffic isolation. In this talk, I will show why these problems are better solved in the routing layer, why existing NameServer and Broker mechanisms are not sufficient, and how broker write isolation, topic migration, and lane-based traffic isolation can be unified in one control plane to support large-cluster split with a smaller blast radius and more controllable governance.

### 讲师:


<img src="https://cdn.sessionize.com/image/ed42-400o400o1-3Jm5SmqbknYn3ZeVXQQXY2.jpg" width="200" /><br/>

Xiao Yang: Tongcheng Travel, Messaging Middleware Core Developer

I am Xiao Yang from the Infrastructure Engineering team at Tongcheng Travel. I mainly focus on the architecture evolution and maintenance of messaging middleware. I am passionate about open source, a committer of Apache ShardingSphere, and an active contributor to Apache RocketMQ.

