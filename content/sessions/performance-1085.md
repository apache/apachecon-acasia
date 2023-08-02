---
title: "Deploy Apache JMeter for large-scale load testing based on Kubernetes"
date: "2023-08-19T14:00:00" 
track: "performance"
presenters: "殷翀元"
stype: "Chinese Session"
---
Apache JMeter, as an excellent open source testing tool, has its own distributed deployment capability to support large concurrency, but it is still difficult to support large-scale concurrency. In order to make JMeter suitable for million-scale load testing, we modified JMeter to increase its throughput for message and data processing, and to provide more powerful and flexible horizontal scaling in a container. In order to uniformly manage the life cycle of the pressure generator, further reduce deployment complexity, and initiate test stress from different regions, we deployed JMeter on a Kubernetes cluster to support running multiple large-scale load tests at the same time, and designed a strategy to do so. This section describes how to implement multi-tenant private network load testing based on VPC peer connections in the cloud environment.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/0934124610.png" width="200" /><br>Yin Chong Yuan: EMQ, Project manager, Yin Chong Yuan, EMQ XMeter Project Manager, is responsible for the maintenance of the performance test platform XMeter product, as well as the open source project mqtt-jmeter. He gave a talk on "Application of Apache JMeter in IoT Testing" at ApacheCon Asia 2022.

EMQ is an open source iot data infrastructure software provider that delivers the world's leading open source cloud-native MQTT message server and stream processing database. The open source projects initiated and operated by EMQ include: Open source iot messaging middleware project EMQ X, cloud native distributed stream processing database HStreamDB, lightweight iot edge analysis and stream processing open source software eKuiper, edge industrial protocol gateway software Neuron, Cross-platform MQTT client tool MQTT X, MQTT JMeter plugin MQTT-Jmeter, etc.
 <br><br>