---
title: "The Consistency Model in Apache Ratis"
date: "2026-08-08T14:00:00"
track: "datastorage"
presenters: "Tsz-Wo Nicholas Sze"
stype: "English Session"
room: "Mtn WanShou Hall"
---

Apache Ratis is an open source Java library for the Raft Consensus Protocol, a distributed consensus algorithm ensuring that multiple machines work together as a single, coherent unit.  Ratis constitutes a high performance implementation of Raft.  To accommodate a diverse array of use cases, Ratis supports various configurable consistency levels.  Furthermore, Ratis offers both synchronous and asynchronous APIs for read and write operations.  Numerous projects, such as Apache Ozone, Apache IoTDB, Apache Celeborn, and Alluxio, utilize Ratis.

Raft along with Ratis are designed to provide strong consistency; specifically, once a write operation is acknowledged as complete, all subsequent reads are guaranteed to reflect the effects of that write.  Read operations are more interesting since there is a fundamental trade-off between consistency and performance.  Ratis has implemented several read mechanisms, including direct read from the leader, linearizable read, read from the followers, read-after-write consistency and stale-read from followers.

This presentation will commence with a concise introduction to the Raft protocol. Subsequently, we will examine the consistency model within Ratis and detail the associated APIs and configurations.

### Speakers:


<img src="https://cdn.sessionize.com/image/ef71-400o400o1-MpFqHHnN7VnXA2oxvNY6T.jpg" width="200" /><br/>

Tsz-Wo Nicholas Sze: Principal Software Engineer

Dr. Tsz-Wo Nicholas Sze serves as a Principal Engineer at Cloudera. He holds the position of PMC Chair for Apache Ratis and is a PMC member for Apache Hadoop and Apache Ozone. His involvement with Apache Hadoop and HDFS dates back to 2007, making him one of the few initial contributors still active in the project. In 2016, he initiated the Apache Ratis project to facilitate high availability and high-performance write pipelines within Apache Ozone. Apache Ratis has since become one of the most widely adopted Raft Java libraries. He earned his Ph.D. degree in Computer Science from the University of Maryland College Park in 2007.