---
title: "Eloq ConvergedDB on Apache Cassandra: Built for Agentic AI"
date: "2025-07-25T16:45:00"
room: "Mtn WanShou Hall"
track: "datastorage"
presenters: "Hubert Zhang, Lintao Zhang"
stype: "English Session"
---

We are rapidly entering the **Agentic Application Age**, where AI-driven agents not only assist but autonomously make decisions and manage tasks. However, the data infrastructure underpinning these applications faces significant challenges in scalability, consistency, and performance.

With Apache Cassandra 5.0 introducing **Vector Search**, it has emerged as a key AI database. Yet, **Agentic Applications demand more than just vector capabilities**. In this session, we will first explore Cassandra 5.0’s Vector Search feature, examine the critical limitations of existing solutions, and introduce **Eloq ConvergedDB on Apache Cassandra**, an innovative approach designed to overcome these challenges.

Nowadays, with platforms like [**LangChain**](https://www.langchain.com/) and [**LlamaIndex**](https://www.llamaindex.ai/), developers can seamlessly integrate multiple databases into AI workflows, enabling efficient storage and retrieval of multi-modal data. However, this approach often causes several challenges.

The first challenge is **management complexity**. AI applications typically need multiple databases to manage different data types. Each database comes from a different vendor, requires specialized skill sets, and has unique backup and failure recovery procedures. Backup strategies and failure recovery operations vary significantly between database systems, complicating overall infrastructure management. 

The second challenge is related to **flexibility and agility**. Modern databases are often designed to handle a specific type of workload under a specific range of performance envelopes. For example, Redis is designed to address latency issues, by sacrificing persistency, while PostgreSQL guarantees durability by trading-off scalability. 

The third challenge is the difficulty of ensuring **data consistency across multiple databases**. AI applications often require combining data from diverse sources, which introduces transactional challenges. Databases traditionally provides ACID transactional semantics to ease the complexity of application development. This valuable property is lost when a query needs to be carried out by multiple databases. 

To overcome the above limitation, We proposed a one-stop solution ConvergedDB on Cassandra, which is able to:

- Eliminate Scalability Concerns: ConvergedDB’s architecture ensures seamless scalability, whether your business grows vertically or horizontally.
- Ensure Consistency: As multi-agent architectures become the norm, ConvergedDB’s cross-model transactional guarantees will prove invaluable.
- Maintain High Performance: With no performance degradation, ConvergedDB delivers a robust solution for the most demanding AI applications.

The future of AI applications requires data infrastructure that is scalable, consistent, and performant. ConvergedDB on Cassandra delivers on all three fronts, enabling developers to focus on innovation rather than infrastructure.

### Speakers:


<img src="https://sessionize.com/image/a965-400o400o1-E9kixxxRCcLxkKoQ9y7dRC.png" width="200" /><br/>

Hubert Zhang: EloqData CTO

Hubert Zhang serves as the Chief Technology Officer (CTO) at EloqData. Prior to joining EloqData, Hubert was the Technical Lead for the Greenplum Database at VMware. He is also a member of the Project Management Committee (PMC) for Apache HAWQ.


<img src="https://sessionize.com/image/2f8b-400o400o1-MyxGEXHK65dpEA5LW96TB8.jpg" width="200" /><br/>

Lintao Zhang: Co-founder and CEO, EloqData

Lintao Zhang is the Co-founder and CEO of EloqData, building the next generation database infrastructure for applications in the AI age.  Previously he was a Partner Research Manager at Microsoft Research, working on cloud infrastructures, distributed systems and AI. He was a inventor of the PacificA replication protocol that is used in Apache Kafka, Apache Pegasus, and ElasticSearch. He has published over fifty papers in top conferences and won many awards for his research. Lintao is an IEEE Fellow and a ACM Distinguished Member. He received his Bachelor's degree from Peking University, and his Ph.D. from Princeton University.