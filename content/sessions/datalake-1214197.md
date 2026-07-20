---
title: "Beyond the Protocol: Productionizing the Iceberg REST Catalog at Enterprise Scale"
date: "2026-08-07T15:00:00"
track: "datalake"
presenters: "Jerry Shao"
stype: "Chinese Session"
room: "WanChun Hall"
---

While the Iceberg REST Catalog (IRC) provides a standardized protocol for table management, implementing it in a mission-critical enterprise environment reveals a significant "implementation gap." Moving from a legacy Hive Metastore (HMS) to a REST-based architecture requires more than just a new API—it demands a total rethink of security, performance, and data continuity.

In this session, we share a field-tested solution for deploying IRC in production. We break down the transition into three critical pillars:

Seamless Migration: How to move existing HMS-managed tables to IRC without business disruption or "stop-the-world" maintenance windows.
Modernizing Security: Strategies for transitioning from Hadoop-native Kerberos authentication and Ranger-based authorization to modern, cloud-native OAuth and centralized identity providers.
Performance at Scale: Shifting the commit mechanism from the client to the server opens new doors for optimization. We will explore server-side performance enhancements that reduce commit conflicts and improve query planning latency.
Attendees will walk away with a practical roadmap for closing the gap between the IRC specification and a secure, high-performance production deployment.

### Speakers:


<img src="https://cdn.sessionize.com/image/396c-400o400o1-PCyrxuKZaPxmAUQMTrdp5J.jpg" width="200" /><br/>

Jerry Shao: Datastrato, CTO

Jerry Shao is the co-founder and CTO of Datastrato, focused on open source Big Data are for more than 10 years. He is an Apache member, committer and PMC member of Apache Spark and Apache Inlong, the original creator of Apache Gravitino.