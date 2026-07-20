---
title: "The Anatomy of Iceberg Failures: Lessons from Real-World Escalations"
date: "2026-08-07T16:45:00"
track: "datalake"
presenters: "Noémi Pap-Takács, Boglárka Egyed"
stype: "English Session"
room: "WanChun Hall"
---

Apache Iceberg has revolutionized data lakes by bringing ACID transactions and flexible table updates. However, at enterprise scale, "hands-off" management is a myth. Without the right maintenance strategy, high-throughput systems often suffer from rising storage costs, query performance degradation, and failures.

In this session, we will dissect real-world customer escalations ranging from systems crashing because they had to process massive amounts of metadata, to cleanup tasks being blocked by constant data updates from multiple concurrent writers. 

Attendees will move beyond the documentation to learn a proven practical guide for switching from firefighting emergencies to proactive management, keeping the data lake healthy and performant.

We will cover:
- Observability: Key metrics to monitor to detect health issues before they trigger an escalation,
- Tips for performance: Reducing storage and compute costs,
- Maintenance strategies: Configure maintenance features and schedule compaction jobs without locking out production writers,
- Recovery: How to repair tables and recover from failures.

### Speakers:


<img src="https://cdn.sessionize.com/image/5a3f-400o400o1-BYhDA4rBpsGm8n4d5mcvhs.jpg" width="200" /><br/>

Noémi Pap-Takács: Apache Impala Committer

Noémi Pap-Takács is a software engineer at Cloudera and a committer on the Apache Impala project. Her focus lies in performance optimization and the integration of Apache Iceberg into Impala.


<img src="https://cdn.sessionize.com/image/bbcc-400o400o1-faLy6maxgVArZ88BQgaPnH.jpg" width="200" /><br/>

Boglárka Egyed: Engineering Director at Cloudera

Boglárka Egyed is an Engineering Director at Cloudera, leading the teams behind Apache Impala and Hive. A former automotive engineer turned big data enthusiast, she spent years as an Apache Sqoop developer before moving into leadership. Today, she focuses on scaling engineering excellence and advancing open-source innovation for modern data architecture.