---
title: "Building a real-time data lakehouse in practice"
date: "2025-07-26T15:00:00"
room: "WanChun Hall"
track: "datalake"
presenters: "Congxian Qiu, Zhuojun Jiang"
stype: "Chinese Session"
---

In the era of real-time driven business decision-making, the architecture design of high-throughput data lake warehouse has become the decisive battlefield for enterprise digital transformation. Faced with the insurmountable timeliness bottleneck of traditional batch processing architecture, we built a streaming lake warehouse system based on Flink CDC 3.0 + Apache Iceberg + Apache Amoro, and successfully achieved the minute-level readiness and query performance transition of a single customer's daily average of tens of billions of data streams.

This sharing will introduce three aspects of practical experience:
Based on Flink CDC3.0, multi-business table heterogeneous data is entered into the datalake in seconds, solving the problem of accurate connection between historical data drift and incremental synchronization;
Iceberg performance tuning design improves complex query performance by 400% compared with Hive.
The innovative application of the Apache Amoro self-optimizing framework provides efficient reading performance while efficiently merging small files and cleaning data.

This system has been implemented in the production practice of telecom operators and supports the business peak of daily PB-level data processing, which can provide participants with a real-time lake warehouse architecture paradigm that can be seamlessly migrated.

### Speakers:


<img src="https://sessionize.com/image/25e4-400o400o1-9iGsggaDEwoFcYqGXtpqoM.jpg" width="200" /><br/>

Congxian Qiu: Apache Flink Committer, Apache(incubating) Amoro PMC member, Associate Director at StateCloud

Congxian Qiu has many years of experience in big data infrastructure research and development. Currently, He leads the development of large-scale data lake platform based on Apache Iceberg. He is an Apache Flink Committer and Apache(incubating) Amoro PMC member.

<img src="https://sessionize.com/image/dd80-400o400o1-SKrNUnGVHC8xTrBeHtFLHN.jpg" width="200" /><br/>

Zhuojun Jiang: Senior Big Data Engineer, China Telecom Cloud Technology Co., Ltd

Zhuojun Jiang is a Senior Big Data Engineer at China Telecom Cloud Technology Co., Ltd., specializing in real-time data lakehouse architecture. She focuses on big data development, system performance optimization, and real-time data synchronization based on technologies like Apache FlinkCDC, Iceberg, and Amoro. Jiang actively contributes to the open-source community and shares practical insights through industry forums and technical talks.
