---
title: "Best Practices for High Availability of Apache Pulsar on Tencent Cloud"
date: ""
track: "messaging"
presenters: "明泽 韩"
stype: "Chinese Session"
--- 

Apache Pulsar is is an cloud-native, distributed messaging and streaming platform. Apache Pulsar adopts a storage and computing separation architecture.Support large clusters, multi-tenants, million-level topics, cross-regional data replication, persistent storage, tiered storage, high scalability and other enterprise-level and financial services. Apache Pulsar provides a unified consumption model that supports both message queue and streaming scenarios. It can not only provide enterprise-level read and write service quality and strong consistency guarantee for queue scenarios, but also provide high throughput and low latency for streaming scenarios.
Apache Pulsar has been implemented in key enterprise businesses, and has rich application scenarios. At present, Tencent Cloud has also applied Apache Pulsar on a large scale in production practice for nearly 5 years. In production practice, Tencent Cloud has made a series of performance optimizations and stability enhancements for Apache Pulsar to ensure stable and efficient system operation for users in different scenarios. 
In this speech, we will focus on Apache Pulsar on Tencent Cloud's best practices for high availability, Including high availability of broker and bookkeeper clusters, high availability of zookeeper clusters, and high availability practices across clusters. Hope this speech can  provide some references for developers.

### Speakers:

<img src="https://sessionize.com/image/9c17-400o400o1-JPuaxw3mCtQ2zt9Ew94C2n.jpg" width="200" /><br/>

Graduated from Wuhan University majoring in computer science. Tencent Cloud senior R&D engineer. Open source community enthusiast. I have more than 8 years of experience in message queue-related R&D and operations in Meituan and Tencent. Currently, I am mainly responsible for the core part of Tencent Cloud TDMQ for Pulsar product. At the same time, I am an Apache Pulsar Contributor and RoP Maintainer.