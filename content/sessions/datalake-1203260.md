---
title: "From database to lakehouse in real-time: CDC, Kafka, Apicurio, and Apache Iceberg"
date: ""
track: "datalake"
presenters: "Carles Arnal"
stype: "English Session"
---

Batch ETL runs nightly. Your analysts query stale data. Your ML models train on yesterday's features. The streaming-first lakehouse replaces all of that with a single, real-time pipeline — and you can build it entirely with open-source tools.

In this talk, I'll demo a complete pipeline: Debezium captures row-level changes from PostgreSQL, streams them through Kafka with schemas enforced by Apicurio Registry (a CNCF sandbox project), and lands them in Apache Iceberg tables — queryable within seconds via Trino or Spark. I'll cover how the Flink Dynamic Iceberg Sink leverages schema registries for automatic schema evolution, eliminating the manual DDL changes that plague traditional data lakes.

Attendees will leave with:
- A deployable CDC-to-Iceberg pipeline architecture using only open-source components on Kubernetes
- Practical patterns for handling schema evolution across the Kafka-to-Iceberg boundary
- A clear understanding of when this approach replaces batch ETL and where hybrid patterns still make sense

### Speakers:


<img src="https://cdn.sessionize.com/image/ebeb-400o400o1-nXA4VjZFgbUQrzL5Hm1DKV.jpg" width="200" /><br/>

Carles Arnal: Principal Software Engineer at Red Hat

Carles Arnal is a Principal Software Engineer at IBM and a core maintainer of Apicurio Registry (CNCF sandbox project) working in the AI and Data Streaming space. He's also an associate professor at BarcelonaTech and he's an active committer of Quarkus with over 10 years of industry experience.

