---
title: "Building a real-time data lakehouse in practice"
date: ""
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

Congxian Qiu

Congxian Qiu is an expert in StateCloud R&D, with many years of experience in big data infrastructure. He has participated in and led the development of large-scale data processing frameworks. He is an Apache Committer and Apache(incubating) Amoro PMC member.

Congxian是StateCloud研发专家，拥有多年大数据基础设施经验，参与并领导了大规模数据处理框架的开发。他是Apache Committer和Apache（incubating）Amoro PMC成员。


<img src="https://sessionize.com/image/dd80-400o400o1-SKrNUnGVHC8xTrBeHtFLHN.jpg" width="200" /><br/>

Zhuojun Jiang

Zhuojun Jiang is a Senior Big Data Engineer at China Telecom Cloud Technology Co., Ltd., specializing in real-time data lakehouse architecture. She focuses on big data development, system performance optimization, and real-time data synchronization based on technologies like Apache FlinkCDC, Iceberg, and Amoro. Jiang actively contributes to the open-source community and shares practical insights through industry forums and technical talks.

Zhuojun Jiang 是中国电信云科技有限公司的高级大数据工程师，专注于实时数据湖库架构研究。她专注于基于 Apache FlinkCDC、Iceberg 和 Amoro 等技术的大数据开发、系统性能优化和实时数据同步。蒋卓君积极参与开源社区的贡献，并通过行业论坛和技术讲座分享实践见解。

