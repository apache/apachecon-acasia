---
title: "Huawei Terminal Cloud optimizes Apache Pulsar in container scenarios"
date: "2023-08-18T14:45:00" 
track: "messaging"
presenters: "林琳"
stype: "Chinese Session"
---
Apache Pulsar is a cloud-native message queue that, based on its storage separation architecture, can often shrink the compute layer to save resources during periods of low traffic. We made a lot of optimizations for Apache Pulsar in containerization scenarios. Such as:
At present, the Pulsar load balancing algorithm relies on the past load data of nodes, and the process of achieving balance is relatively slow. When HPA is enabled, node capacity expansion may be triggered during load balancing, and capacity expansion triggers new load balancing. How can we optimize to make Pulsar more cloud-native?
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230525/1930494180.jpeg" width="200" /><br>Lin Lin: Huawei, SDE Expert, Huawei terminal SDE expert, Apache Pulsar PMC member, with nearly 10 years of experience in middleware and infrastructure design, is committed to creating stable and reliable infrastructure
 <br><br>